# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import itertools
import os.path
import re
from collections import defaultdict

from src.config import CONSTANTS, Config
from src.utils import Tools, FilePathBuilder
from src.utils.dataset_loader import DatasetLoader, DataSetRepo


class RepoFragmentMaker:
    def __init__(self, repo: DataSetRepo, fragment_size, slice_size):
        self.repo_name = repo.repo_name
        self.fragment_size = fragment_size
        self.slice_size = slice_size
        self.slice_step = 1 if fragment_size // slice_size == 0 else fragment_size // slice_size
        
    def _build_fragments_for_a_file(self, fpath_tuple, code):
        code_fragments = []
        code_lines = code.splitlines()
        delta_size = self.fragment_size // 2
        for line_no in range(0, len(code_lines), self.slice_step):  # line_no starts from 0
            start_line_no = max(0, line_no - delta_size)
            end_line_no = min(len(code_lines), line_no + self.fragment_size - delta_size)
            fragment_lines = [i for i in code_lines[start_line_no:end_line_no]]
            if not fragment_lines:  # all empty lines
                continue
            fragment_text = '\n'.join(fragment_lines)
            code_fragments.append({
                'context': fragment_text,
                'metadata': {
                    'fpath_tuple': fpath_tuple,
                    'line_no': line_no,
                    'start_line_no': start_line_no,
                    'end_line_no': end_line_no,
                    'fragment_size': self.fragment_size,
                    'repo': self.repo_name,
                    'slice_size': self.slice_size,
                }
            })
        return code_fragments

    @staticmethod
    def _merge_fragments_with_same_context(code_fragments):
        merged_code_fragments = defaultdict(list)
        for code_fragment in code_fragments:
            context = code_fragment['context']
            metadata = code_fragment['metadata']
            merged_code_fragments[context].append(metadata)
        json_lines = []
        for context, metadata_list in merged_code_fragments.items():
            json_lines.append({
                'context': context,
                'metadata': metadata_list
            })
        return json_lines

    def build_fragments(self):
        output_path = FilePathBuilder.repo_fragment_path(self.repo_name, self.fragment_size, self.slice_size)
        if Tools.check_and_reuse(output_path):
            return
        all_code_fragments = []
        for fpath_tuple, code in Tools.iterate_repository(self.repo_name).items():
            all_code_fragments += self._build_fragments_for_a_file(fpath_tuple, code)
        merged_code_fragments = self._merge_fragments_with_same_context(all_code_fragments)
        print(f'built {len(merged_code_fragments)} fragments for {self.repo_name} with fragment size '
              f'{self.fragment_size} and slice {self.slice_size}')
        Tools.dump_pickle(merged_code_fragments, output_path)


class CodeSnippetFragmentMaker:
    """the retrieve-and-generate approach"""
    def __init__(self, repo: DataSetRepo, fragment_size):
        self.repo = repo
        self.repo_name = repo.repo_name
        self.fragment_size = fragment_size
        self.source_code = Tools.iterate_repository(repo.repo_name)
        self.graph_info = None
    
    def build_fragment(self, mode):
        output_path = FilePathBuilder.first_stage_fragment_path(mode, self.repo_name, self.fragment_size)
        if Tools.check_and_reuse(output_path):
            return
        code_fragments = []
        if mode == CONSTANTS.cc and self.graph_info is None:
            self.graph_info = Tools.load_json(self.repo.graph_info_cache_path)
        for task in DatasetLoader.load_tasks_from_repo(self.repo):
            line_no = task.func_end_lineno
            context_start_lineno = task.context_start_lineno
            if mode == CONSTANTS.gt:
                contexts = [task.ref_code]
            elif mode == CONSTANTS.bl:
                contexts = [task.task_input]
                if Config.Data.api_level:
                    delta_size = max(-self.fragment_size, context_start_lineno - task.sign_end_lineno)
                    contexts[0] = '\n'.join(contexts[0].splitlines()[delta_size:])
            else:
                contexts = self.graph_info[task.task_id][CONSTANTS.SEPARATE]
            for context in contexts:
                code_fragments.append({
                    'context': context,
                    'metadata': {
                        'task_input': task.task_input,
                        'fpath_tuple': task.fpath_tuple,
                        'line_no': line_no,  # line_no starts from 0
                        'task_id': task.task_id,
                        'end_line_no': line_no,
                        'fragment_size': self.fragment_size,
                        'context_start_lineno': task.context_start_lineno,
                        'repo': self.repo_name
                    }
                })
        print(f'build {len(code_fragments)} {mode} fragments for {self.repo_name} with fragment size {self.fragment_size}')
        Tools.dump_pickle(code_fragments, output_path)


class PredictionFragmentMaker:
    def __init__(self, repo: DataSetRepo, fragment_size, slice_size):
        self.repo = repo
        self.fragment_size = fragment_size
        self.slice_size = slice_size
        os.environ['PREDICT'] = 'false'
        self.prediction_path = FilePathBuilder.raw_prediction_path(fragment_size, slice_size)
        os.environ['PREDICT'] = 'true'
        _predictions = Tools.load_jsonl(self.prediction_path)
        self.predictions = {prediction['task_id']: prediction for prediction in _predictions}
    
    def build_fragment(self, _type='centered'):
        output_path = FilePathBuilder.second_stage_fragment_path(self.repo.repo_name, self.fragment_size, self.slice_size)
        if Tools.check_and_reuse(output_path):
            return
        code_fragments = []
        for task in DatasetLoader.load_tasks_from_repo(self.repo):
            task_id = task.task_id
            prediction = self.predictions[task_id]['generation']
            try:
                code = max(re.findall(r'```.*?\n(.*)\n```', prediction, re.DOTALL), key=len)
            except ValueError:
                code = prediction
            if Config.Data.api_level:
                delta_size = max(-self.fragment_size, task.context_start_lineno - task.sign_end_lineno - len(code.splitlines()))
                code = '\n'.join([task.task_input, code])
                code = '\n'.join(code.splitlines()[delta_size:])
            code_fragments.append({
                'context': code,
                'metadata': {
                    'task_input': task.task_input,
                    'fpath_tuple': task.fpath_tuple,
                    'line_no': task.sign_end_lineno,
                    'task_id': task_id,
                    'context_start_lineno': task.context_start_lineno,
                    'repo': self.repo.repo_name
                }
            })
        print(f'build {len(code_fragments)} prediction fragments for {self.repo.repo_name}')
        Tools.dump_pickle(code_fragments, output_path)


class MakeFragmentWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def fragment_for_repo_files():
        for fragment_size, slice_size in itertools.product(MakeFragmentWrapper.fragment_sizes, MakeFragmentWrapper.slice_sizes):
            for repo in DatasetLoader.load_repos():
                RepoFragmentMaker(repo, fragment_size, slice_size).build_fragments()

    @staticmethod
    def _fragment_for_some(mode):
        for fragment_size in MakeFragmentWrapper.fragment_sizes:
            for repo in DatasetLoader.load_repos():
                CodeSnippetFragmentMaker(repo, fragment_size).build_fragment(mode)

    @staticmethod
    def fragment_for_baseline():
        MakeFragmentWrapper._fragment_for_some(CONSTANTS.bl)

    @staticmethod
    def fragment_for_ground_truth():
        MakeFragmentWrapper._fragment_for_some(CONSTANTS.gt)

    @staticmethod
    def fragment_for_call_chain():
        MakeFragmentWrapper._fragment_for_some(CONSTANTS.cc)

    @staticmethod
    def fragment_for_prediction():
        for fragment_size, slice_size in itertools.product(MakeFragmentWrapper.fragment_sizes, MakeFragmentWrapper.slice_sizes):
            for repo in DatasetLoader.load_repos():
                PredictionFragmentMaker(repo, fragment_size, slice_size).build_fragment()
