import ast
import json
import os
import re
from collections import defaultdict
from io import BytesIO
from typing import Generator, Optional
import tokenize

from src.config import Config, CONSTANTS
from src.utils import Tools, FilePathBuilder


class DatasetTask:
    def __init__(self, **kwargs):
        self.task_id: str = kwargs.get('task_id')
        self.repo: str = kwargs.get('repo')
        self.task_input: str = kwargs.get('task_input')
        self.context_start_lineno: int = kwargs.get('context_start_lineno')
        self.start_lineno: int = kwargs.get('start_lineno')
        self.sign_end_lineno: int = kwargs.get('sign_end_lineno')
        self.func_end_lineno: int = kwargs.get('func_end_lineno')
        self.func_name: Optional[str] = kwargs.get('func_name', None)
        self.plain_filepath: str = kwargs.get('plain_filepath')
        self.fpath_tuple: list = [self.repo] + self.plain_filepath.split(os.sep)
        self.plain_filepath = self.plain_filepath.removesuffix('.py')
        self.ref_code: str = kwargs.get('ref_code')
        self.gt_classes: set[str] = set(kwargs.get('gt_classes', []))
        self.gt_func_and_attrs: set[str] = set(kwargs.get('gt_func_and_attrs', []))
        self.level: str = kwargs.get('level', '')
        self.tests: list[str] = kwargs.get('tests', [])


class DataSetRepo:
    def __init__(self, repo: str):
        self.repo_name: str = repo
        self.repo_path: str = os.path.join(Config.Data.repos_path, repo)
        if not os.path.exists(self.repo_path) or not os.path.isdir(self.repo_path) or repo == '.pytype':
            raise NotADirectoryError(f'{repo} is not a valid repo')
        self.repo_pytype_path: str = os.path.join(Config.Data.repos_path, '.pytype', repo)
        if not os.path.exists(self.repo_pytype_path) or not os.path.isdir(self.repo_pytype_path):
            raise FileNotFoundError(f'{repo} has not built its pytype files')
        self.parser_cache_path = FilePathBuilder.parser_cache_path(repo)
        self.graph_info_cache_path = FilePathBuilder.graph_info_cache_path(repo)


class DatasetLoader:
    repos: list[DataSetRepo] = []
    tasks: list[DatasetTask] = []
    tasks_by_repo = defaultdict(list)
    total_tasks = len(Tools.load_jsonl(Config.Data.benchmark_path))

    @staticmethod
    def load_repos() -> Generator[DataSetRepo, None, None]:
        if len(DatasetLoader.repos) > 0:
            for repo in DatasetLoader.repos:
                yield repo
            return
        for repo_name in os.listdir(Config.Data.repos_path):
            try:
                repo = DataSetRepo(repo_name)
            except NotADirectoryError:
                print(f'{repo_name} is not a repo')
                continue
            DatasetLoader.repos.append(repo)
            yield repo
            if Config.Method.debug:
                return

    @classmethod
    def load_tasks(cls) -> Generator[DatasetTask, None, None]:
        if len(DatasetLoader.tasks) > 0:
            for task in DatasetLoader.tasks:
                yield task
            return
        benchmark_path = Config.Data.benchmark_path
        dataset = Config.Data.dataset
        data = Tools.convert_json_list_to_dict(
            Tools.load_jsonl(benchmark_path), CONSTANTS.dataset_to_id_key[dataset]
        )
        raw_data = failed_data = None
        if dataset == CONSTANTS.codereval:
            raw_data = Tools.convert_json_list_to_dict(
                Tools.load_json(benchmark_path.replace('.jsonl', '.json'))['RECORDS'], '_id'
            )
        elif dataset == CONSTANTS.deveval:
            failed_data = Tools.convert_json_list_to_dict(
                Tools.load_jsonl(benchmark_path.replace('.jsonl', '_failed_samples.jsonl')), 'namespace'
            ).keys()


        for idx, (task_id, task) in enumerate(sorted(data.items(), key=lambda item: item[0])):
            # if task_id != '62b45b396decaeff903e1001':
            #     continue
            if dataset == CONSTANTS.codereval:
                assert raw_data is not None
                raw_task = raw_data[task_id]
                task_input = task['input'].strip('\n')
                ref_code = raw_task['code'].strip('\n')
                repo = raw_task['project'].replace('/', '---')
                if repo in ['witten---atticmatic', 'witten---borgmatic', 'gopad---gopad-python']:
                    print(f'exclude task in repo: {repo}')
                    continue
                if repo == 'neo4j---neo4j-python-driver':
                    path_prefix = f'src'
                else:
                    path_prefix = ''
                if path_prefix != '':
                    path_prefix += os.sep
                plain_filepath = f'{path_prefix}{raw_task["file_path"].replace("/", os.sep)}'
                complete_filepath = str(os.path.join(Config.Data.repos_path, repo, plain_filepath))
                try:
                    start_lineno, func_end_lineno, sign_end_lineno = cls._locate_lineno_via_content(
                        complete_filepath, ref_code
                    )
                except (AssertionError, FileNotFoundError, RuntimeError) as e:
                    if isinstance(e, AssertionError):
                        print(f'{task_id} no function found')
                    elif isinstance(e, FileNotFoundError):
                        print(f'{task_id} incorrect file path')
                    else:
                        print(f'{task_id} {e}')
                    # start_lineno = int(raw_task['lineno'])
                    # func_end_lineno = int(raw_task['end_lineno'])
                    # sign_end_lineno = start_lineno + task_input.count('\n') + 1
                    continue
                # if raw_task['level'] == 'project_runnable':
                #     print(111)
                # if start_lineno != int(raw_task['lineno']) or func_end_lineno != int(raw_task['end_lineno']):
                #     print(task_id, start_lineno, func_end_lineno)
                oracle_context = json.loads(raw_task['oracle_context'])
                dataset_task = DatasetTask(
                    task_id=task_id,
                    repo=repo,
                    task_input=task_input,
                    context_start_lineno=start_lineno,  # lineno starts from 0
                    start_lineno=start_lineno,
                    sign_end_lineno=sign_end_lineno,  # end lineno is open interval
                    func_end_lineno=func_end_lineno,
                    func_name=raw_task['name'],
                    plain_filepath=plain_filepath,
                    ref_code=ref_code,
                    gt_classes=ast.literal_eval(oracle_context['classes']),
                    gt_func_and_attrs=ast.literal_eval(oracle_context['apis']) +
                                      ast.literal_eval(oracle_context['vars']),
                    level=raw_task['level']
                )
            elif dataset == CONSTANTS.deveval:
                if task_id in failed_data:
                    continue
                repo_path = task['project_path']
                repo = repo_path.split('/')[-1]
                func_name = task_id.split('.')[-1]
                plain_filepath = f'{task["completion_path"].removeprefix(repo_path + "/").replace("/", os.sep)}'
                complete_filepath = str(os.path.join(Config.Data.repos_path, repo, plain_filepath))
                code_lines = Tools.read_code(complete_filepath).splitlines()
                start_lineno, _ = tuple(task['signature_position'])
                sign_end_lineno, func_end_lineno = tuple(task['body_position'])
                start_lineno -= 1
                sign_end_lineno -= 1
                if not cls._check_function_in_place(complete_filepath, start_lineno, func_name):
                    continue
                dataset_task = DatasetTask(
                    task_id=task_id,
                    repo=repo,
                    task_input='\n'.join(code_lines[start_lineno: sign_end_lineno]),
                    context_start_lineno=start_lineno,  # lineno starts from 0
                    start_lineno=start_lineno,
                    sign_end_lineno=sign_end_lineno,  # end lineno is open interval
                    func_end_lineno=func_end_lineno,
                    func_name=func_name,
                    plain_filepath=plain_filepath,
                    ref_code='\n'.join(code_lines[start_lineno: func_end_lineno]),
                    tests=task['tests']
                )
            elif dataset == CONSTANTS.repoeval:
                task_meta_data = task['metadata']
                ref_code = task_meta_data['ground_truth']
                fpath_tuple = task_meta_data['fpath_tuple']
                start_lineno, context_end_lineno = task_meta_data['context_start_lineno'], task_meta_data['line_no']
                dataset_task = DatasetTask(
                    task_id=task_id,
                    repo=fpath_tuple[0],
                    task_input=task['prompt'],
                    context_start_lineno=start_lineno,  # lineno starts from 0
                    start_lineno=start_lineno,
                    sign_end_lineno=context_end_lineno,  # end lineno is open interval
                    func_end_lineno=context_end_lineno + len(ref_code.split('\n')),
                    plain_filepath=str(os.sep.join(fpath_tuple[1:])),
                    ref_code=ref_code
                )
            else:
                raise NotImplementedError()
            DatasetLoader.tasks.append(dataset_task)
            yield dataset_task

    @staticmethod
    def load_tasks_from_repo(repo: DataSetRepo) -> Generator[DatasetTask, None, None]:
        if repo in DatasetLoader.tasks_by_repo:
            for task in DatasetLoader.tasks_by_repo[repo]:
                yield task
            return
        for task in DatasetLoader.load_tasks():
            if task.repo == repo.repo_name:
                DatasetLoader.tasks_by_repo[repo].append(task)
                yield task

    @staticmethod
    def _locate_lineno_via_content(filepath: str, content: str) -> tuple[int, int, int]:
        start_index_in_content = content.find('def')
        assert start_index_in_content != -1
        content = content[start_index_in_content:].strip(' \t\n')
        code = Tools.read_code(filepath)
        start_index = code.find(content.splitlines()[0].split('(')[0].strip())
        assert start_index != -1
        start_lineno = code[:start_index].count('\n')
        func_end_delta, sign_end_delta = DatasetLoader._search_function_and_sign_end_lineno(
            '\n'.join(code.splitlines()[start_lineno:]),
        )
        func_end_lineno = start_lineno + func_end_delta
        sign_end_lineno = start_lineno + sign_end_delta
        # print('\n'.join(code.splitlines()[start_lineno:func_end_lineno]))
        return start_lineno, func_end_lineno, sign_end_lineno

    @staticmethod
    def _search_function_and_sign_end_lineno(code: str) -> tuple[int, int]:
        indents = 0
        sign_end_lineno = -1
        docstring_detected = False
        keyword_detected = False
        for token in tokenize.tokenize(BytesIO(code.encode('utf-8')).readline):
            if token.type == tokenize.STRING and not docstring_detected and '"""' in token.string:
                sign_end_lineno = token.end[0]
                docstring_detected = True
            elif token.type == tokenize.NAME and token.string == 'def':
                keyword_detected = True
            elif token.type == tokenize.INDENT and keyword_detected:
                indents += 1
                if sign_end_lineno == -1:
                    sign_end_lineno = token.end[0] - 1
            elif token.type == tokenize.DEDENT and keyword_detected:
                indents -= 1
                if indents == 0:
                    if sign_end_lineno == -1:
                        raise RuntimeError('no signature found')
                    # if not docstring_detected:
                    #     print('no docstring')
                    return token.start[0] - 1, sign_end_lineno
        raise RuntimeError('no function found')

    @staticmethod
    def _check_function_in_place(filepath: str, lineno: int, func_name: str):
        code = Tools.read_code(filepath)
        return len(re.findall(rf'def\s+{func_name}', code.splitlines()[lineno])) > 0


if __name__ == '__main__':
    count = 0
    # result = {}
    for t in DatasetLoader.load_tasks():
        # print(t.task_input)
    #     result[task.task_id] = {
    #         'task_id': task.task_id,
    #         'filepath': task.plain_filepath + '.py',
    #         'start_lineno': task.start_lineno,
    #         'end_linono': task.func_end_lineno
    #     }
        count += 1
    # print(json.dumps(result, indent=4))
    print(count)
