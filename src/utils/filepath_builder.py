# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import os
from src.config import Config, CONSTANTS


class FilePathBuilder:
    # api_completion_benchmark = 'datasets/random-api-completion.test.jsonl'
    # random_line_completion_benchmark = 'datasets/random-line-completion.test.jsonl'
    # # short version for codegen
    # short_api_completion_benchmark = 'datasets/random-api-completion-short-version.test.jsonl'
    # short_random_line_completion_benchmark = 'datasets/random-line-completion-short-version.test.jsonl'

    _config_hashcode = Config.hashcode
    _base_cache_path = Config.Data.base_cache_path
    _base_result_path = Config.Data.result_path
    _graph_parser_hashcode = Config.GraphParser.hashcode
    _embedder_name = Config.GraphParser.embedder_name
    _graph_info_hashcode = Config.GraphInfo.hashcode
    _vectorizer_name = Config.Retrieval.vectorizer_name
    _benchmark = Config.Data.benchmark
    _method = Config.Method.type
    _max_sim_fragments = Config.Retrieval.max_sim_fragments
    _prompt_sim_fragment_n = Config.Prompt.num_sim_fragments
    _prompt_call_chain_n = Config.Prompt.num_call_chains
    _max_prompt_length = Config.Generate.max_prompt_length
    _model_name = Config.Generate.model_name

    @staticmethod
    def make_needed_dir(file_path):
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def log_path():
        out_path = os.path.join(FilePathBuilder._base_cache_path, 'log.log')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def repo_fragment_path(repo, fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_cache_path, repo, 'fragment',
                                f'ws{fragment_size}_ss{slice_size}.pkl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def first_stage_fragment_path(mode, repo, fragment_size):
        out_path = os.path.join(FilePathBuilder._base_cache_path, repo, 'fragment',
                                f'{FilePathBuilder._benchmark}_{mode}_ws{fragment_size}.pkl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def second_stage_fragment_path(repo, fragment_size, slice_size):
        os.environ['PREDICT'] = 'false'
        prediction_path = FilePathBuilder.standard_extracted_prediction_path(fragment_size, slice_size)
        prediction_file_name = os.path.basename(os.path.dirname(prediction_path))
        out_path = os.path.join(FilePathBuilder._base_cache_path, repo, 'fragment',
                                f'.{prediction_file_name}.pkl')
        FilePathBuilder.make_needed_dir(out_path)
        os.environ['PREDICT'] = 'true'
        return out_path

    @staticmethod
    def vector_path(fragment_file):
        _vector_path = fragment_file.replace(f'{os.sep}fragment{os.sep}', f'{os.sep}vector{os.sep}').replace(
            '.pkl', f'.{FilePathBuilder._vectorizer_name}.pkl'
        )
        FilePathBuilder.make_needed_dir(_vector_path)
        return _vector_path

    @staticmethod
    def repo_vector_path(repo, fragment_size, slice_size):
        repo_fragment_path = FilePathBuilder.repo_fragment_path(repo, fragment_size, slice_size)
        return FilePathBuilder.vector_path(repo_fragment_path)

    @staticmethod
    def first_stage_vector_path(mode, repo, fragment_size):
        first_stage_fragments_path = FilePathBuilder.first_stage_fragment_path(mode, repo, fragment_size)
        return FilePathBuilder.vector_path(first_stage_fragments_path)

    @staticmethod
    def second_stage_vector_path(repo, fragment_size, slice_size):
        second_stage_fragments_path = FilePathBuilder.second_stage_fragment_path(repo, fragment_size, slice_size)
        return FilePathBuilder.vector_path(second_stage_fragments_path)

    @staticmethod
    def _retrieval_results_path(repo, fragment_size, slice_size, query_vector_file):
        retrieval_base_dir = os.path.dirname(
            query_vector_file.replace(f'{os.sep}vector{os.sep}', f'{os.sep}retrieval{os.sep}')
        )
        query_file_name = os.path.basename(query_vector_file).removesuffix(f'.{FilePathBuilder._vectorizer_name}.pkl')
        repo_file_name = os.path.basename(
            FilePathBuilder.repo_vector_path(repo, fragment_size, slice_size)
        )[:-len('.pkl')]
        out_path = os.path.join(
            retrieval_base_dir, f'{query_file_name}.{repo_file_name}.frag{FilePathBuilder._max_sim_fragments}.pkl'
        )
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def retrieval_results_path(mode, repo, fragment_size, slice_size):
        if os.getenv('PREDICT') == 'true':
            vector_path = FilePathBuilder.second_stage_vector_path(repo, fragment_size, slice_size)
        else:
            vector_path = FilePathBuilder.first_stage_vector_path(mode, repo, fragment_size)
        return FilePathBuilder._retrieval_results_path(repo, fragment_size, slice_size, vector_path)

    @staticmethod
    def prompt_path(fragment_size, slice_size):
        method = FilePathBuilder._method
        if os.getenv('PREDICT') == 'true':
            suffix = '.2'
        else:
            suffix = ''
            if method == CONSTANTS.REPO_CODER:
                method = CONSTANTS.BASELINE
            elif method == CONSTANTS.OURS_PLUS_REPO_CODER:
                method = CONSTANTS.OURS
        out_path = os.path.join(FilePathBuilder._base_result_path, 'prompt',
                                f'{FilePathBuilder._benchmark}_{method}'
                                f'.graph_{FilePathBuilder._embedder_name}_'
                                f'{FilePathBuilder._graph_parser_hashcode}_{FilePathBuilder._graph_info_hashcode}'
                                f'.retrieval_{FilePathBuilder._vectorizer_name}_ws{fragment_size}_ss{slice_size}'
                                f'.prompt_frag{FilePathBuilder._prompt_sim_fragment_n}_chain{FilePathBuilder._prompt_call_chain_n}'
                                f'.len{FilePathBuilder._max_prompt_length}.{FilePathBuilder._config_hashcode}'
                                f'{suffix}.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def plan_prompt_path(mode: str, fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_result_path, 'plan_prompt',
                                f'{FilePathBuilder._benchmark}_{mode}'
                                f'.graph_{FilePathBuilder._embedder_name}_'
                                f'{FilePathBuilder._graph_parser_hashcode}_{FilePathBuilder._graph_info_hashcode}'
                                f'.retrieval_{FilePathBuilder._vectorizer_name}_ws{fragment_size}_ss{slice_size}'
                                f'.prompt_frag{FilePathBuilder._prompt_sim_fragment_n}_chain{FilePathBuilder._prompt_call_chain_n}'
                                f'.len{FilePathBuilder._max_prompt_length}.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def plan_prediction_path(mode: str, fragment_size, slice_size):
        out_path = (FilePathBuilder.plan_prompt_path(mode, fragment_size, slice_size)
                    .replace(f'{os.sep}plan_prompt{os.sep}', f'{os.sep}plan_prediction{os.sep}')
                    .replace('.len', f'.{FilePathBuilder._model_name}_len'))
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def _base_prediction_path(fragment_size, slice_size):
        out_path = (FilePathBuilder.prompt_path(fragment_size, slice_size)
                    .replace(f'{os.sep}prompt{os.sep}', f'{os.sep}prediction{os.sep}')
                    .replace('.len', f'.{FilePathBuilder._model_name}_len')
                    .removesuffix('.jsonl'))
        return out_path

    @staticmethod
    def raw_prediction_path(fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_prediction_path(fragment_size, slice_size), 'raw.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def extracted_prediction_path(fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_prediction_path(fragment_size, slice_size), 'extracted.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def standard_extracted_prediction_path(fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_prediction_path(fragment_size, slice_size), 'standard_extracted.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def evaluated_prediction_path(fragment_size, slice_size):
        out_path = os.path.join(FilePathBuilder._base_prediction_path(fragment_size, slice_size), 'evaluated.jsonl')
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def evaluate_log_path(evaluated_path: str):
        out_path = evaluated_path.removesuffix('evaluated.jsonl') + 'evaluate.log'
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def config_archive_path(evaluated_path: str):
        out_path = evaluated_path.removesuffix('evaluated.jsonl') + 'config.yaml'
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def metrics_path(evaluated_path: str):
        out_path = evaluated_path.removesuffix('evaluated.jsonl') + 'metrics.json'
        FilePathBuilder.make_needed_dir(out_path)
        return out_path

    @staticmethod
    def parser_cache_path(repo: str):
        path = os.path.join(FilePathBuilder._base_cache_path, repo, 'code_graph',
                            f'{FilePathBuilder._embedder_name}_{FilePathBuilder._graph_parser_hashcode}_parser.pkl')
        FilePathBuilder.make_needed_dir(path)
        return path

    @staticmethod
    def graph_info_cache_path(repo: str):
        """
        {
            "task_id": {
                ...
            }
            ...
        }
        """
        path = os.path.join(FilePathBuilder._base_cache_path, repo, 'code_graph',
                            f'{FilePathBuilder._embedder_name}_{FilePathBuilder._graph_parser_hashcode}'
                            f'_{FilePathBuilder._graph_info_hashcode}_info.pkl')
        FilePathBuilder.make_needed_dir(path)
        return path
