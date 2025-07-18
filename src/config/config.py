import argparse
import hashlib
import json
import multiprocessing
import os
import re
import socket
import time
from typing import Any

import yaml
from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo

from src.config.constants import CONSTANTS


class Config:
    _initialized = False

    class GraphParser:
        @staticmethod
        def memory_map() -> dict[int, str]:
            free_gpus = Config._search_for_free_gpus(1000)
            if len(free_gpus) < 1:
                raise RuntimeError(f'No free GPUs for embedder')
            else:
                return {free_gpus[-1]: '1000MiB'}

    class GraphInfo:
        pass

    class Data:
        pass

    class Retrieval:
        @staticmethod
        def memory_map() -> dict[int, str]:
            return Config.GraphParser.memory_map()

    class Prompt:
        pass

    class Generate:
        @classmethod
        def memory_map(cls) -> dict[int, str]:
            if cls.is_local_llm:
                match = re.fullmatch(r'^.*?((\d+\.)?\d+)b$', cls.model_name)
                if match is None:
                    num_gpus = 1
                else:
                    model_size = float(match.group(1))
                    if model_size == 1.3:
                        num_gpus = 1
                    elif model_size == 7.0:
                        num_gpus = 4
                    elif model_size == 13.0:
                        num_gpus = 4
                    elif model_size == 14.0:
                        num_gpus = 5
                    else:
                        raise NotImplementedError()
                while True:
                    free_gpus = Config._search_for_free_gpus()
                    if num_gpus > len(free_gpus):
                        print(f'Insufficient number of GPUs: {num_gpus} needed, {len(free_gpus)} free, waiting...')
                        time.sleep(30)
                    else:
                        mem_map = {gpu_index: '24000MiB' for gpu_index in free_gpus[:num_gpus]}
                        mem_map[free_gpus[0]] = '20000MiB'
                        return mem_map
            else:
                raise RuntimeError('Online LLM does not need memory_map')

    class Method:
        pass

    @staticmethod
    def _search_for_free_gpus(memory_threshold: int = 24000) -> list[int]:
        free_gpus = []
        nvmlInit()
        for gpu_index in range(nvmlDeviceGetCount()):
            handle = nvmlDeviceGetHandleByIndex(gpu_index)
            if nvmlDeviceGetMemoryInfo(handle).free / 1024 ** 2 >= memory_threshold:
                free_gpus.append(gpu_index)
        return free_gpus

    @staticmethod
    def hash(obj: Any) -> str:
        string = json.dumps(obj, sort_keys=True)
        return hashlib.sha256(string.encode()).hexdigest()[16:24]

    @staticmethod
    def _bind_embedder_path(config_module, embedder_name: str, model_base_path: str):
        if embedder_name == CONSTANTS.jina_v3:
            config_module.model_path = os.path.join(model_base_path, 'jina-v3')
        elif embedder_name == CONSTANTS.bge_small:
            config_module.model_path = os.path.join(model_base_path, 'bge-small-en-v1.5')
        else:
            raise NotImplementedError()

    @classmethod
    def init(cls):
        if cls._initialized:
            return
        if multiprocessing.current_process().name == 'MainProcess':
            parser = argparse.ArgumentParser(description='Initializing Config')
            parser.add_argument('--config', type=str, help='config filename', default='config')
            args = parser.parse_args()
            os.environ['CODE_GRAPH_CONFIG_FILE'] = args.config
        config_filename = os.getenv('CODE_GRAPH_CONFIG_FILE')
        if config_filename is None:
            raise RuntimeError()
        _project_path = os.sep.join(__file__.split(os.sep)[:-3])
        _big_data_base_path = os.path.join('/home', 'shared_data', 'workspace', 'code_graph') \
            if socket.gethostname() == 'hello' else _project_path
        cls.config_path = os.path.join(_project_path, 'config', f'{config_filename}.yaml')
        with open(cls.config_path) as file:
            _config = yaml.load(file, Loader=yaml.FullLoader)
            for _key, _cls in [('graph_parser', cls.GraphParser), ('graph_info', cls.GraphInfo),
                               ('data', cls.Data), ('retrieval', cls.Retrieval), ('prompt', cls.Prompt),
                               ('generate', cls.Generate), ('method', cls.Method)]:
                _subconfig = _config[_key]
                for _param, _value in _subconfig.items():
                    setattr(_cls, _param, _value)
                for _key_to_remove in ['debug', 'reuse_cache']:
                    if _key_to_remove in _subconfig:
                        del _subconfig[_key_to_remove]
                if _cls == cls.Method:
                    if _subconfig['type'] in [
                        CONSTANTS.OURS, CONSTANTS.CALLEE_GROUND_TRUTH, CONSTANTS.CALLEE_BASELINE, CONSTANTS.OURS_PLUS_REPO_CODER, CONSTANTS.OURS_PLUS_RLCODER
                    ]:
                        if _subconfig['type'] == CONSTANTS.OURS_PLUS_REPO_CODER:
                            _subconfig['type'] = CONSTANTS.OURS
                        if _subconfig['context_include_strategy'] == CONSTANTS.FIXED:
                            del _subconfig['context_include_strategy']
                        elif _subconfig['context_include_strategy'] == CONSTANTS.AUTO:
                            for _key_to_remove in ['include_callers', 'include_call_chains']:
                                if _key_to_remove in _subconfig:
                                    del _subconfig[_key_to_remove]
                    else:
                        _type = _subconfig['type']
                        if _type == CONSTANTS.REPO_CODER:
                            _type = CONSTANTS.BASELINE
                        _config[_key] = {'type': _type}
                _cls.hashcode = cls.hash(_subconfig)
            cls.hashcode = cls.hash(_config)
        key_path = os.path.join(_project_path, 'config', f'_key.yaml')
        with open(key_path) as file:
            _key = yaml.load(file, Loader=yaml.FullLoader)
            for _key_name, _key_value in _key.items():
                setattr(cls.Generate, _key_name, _key_value)

        assert cls.Method.type in [
            CONSTANTS.DIRECT, CONSTANTS.BASELINE, CONSTANTS.GROUND_TRUTH,
            CONSTANTS.OURS, CONSTANTS.REPO_CODER, CONSTANTS.CALLEE_GROUND_TRUTH, CONSTANTS.CALLEE_BASELINE,
            CONSTANTS.OURS_PLUS_REPO_CODER, CONSTANTS.OURS_PLUS_RLCODER
        ]
        _dataset = cls.Data.dataset
        cls.Data.project_path = _project_path
        cls.Data.repos_path = os.path.join(_big_data_base_path, 'repos', _dataset)
        cls.Data.base_cache_path = os.path.join(_project_path, '.cache', _dataset)
        cls.Data.result_path = os.path.join(_project_path, 'results', _dataset)
        cls.Data.benchmark_path = os.path.join(_project_path, 'datasets', f'{_dataset}.jsonl')
        cls.Data.api_level = cls.Data.dataset == CONSTANTS.repoeval

        _model_base_path = os.path.join(_big_data_base_path, 'models')
        cls._bind_embedder_path(cls.GraphParser, cls.GraphParser.embedder_name, _model_base_path)

        if Config.Retrieval.vectorizer_type == CONSTANTS.EMBEDDER:
            cls._bind_embedder_path(cls.Retrieval, cls.Retrieval.vectorizer_name, _model_base_path)

        _generate_model = cls.Generate.model_name
        if _generate_model == CONSTANTS.codegen:
            max_prompt_length = 1000
            model_path = os.path.join(_model_base_path, 'codegen-6b-mono')
        elif _generate_model == CONSTANTS.codex:
            max_prompt_length = 2000
            model_path = ''
        elif _generate_model == CONSTANTS.codellama_13b:
            max_prompt_length = 4096
            model_path = os.path.join(_model_base_path, 'codellama-13b-base')
        elif _generate_model == CONSTANTS.deepseek_coder_7b:
            max_prompt_length = 6144
            model_path = os.path.join(_model_base_path, 'deepseek-coder-7b-instruct-v1.5')
        elif _generate_model == CONSTANTS.qwen_coder_14b:
            max_prompt_length = 4096
            model_path = os.path.join(_model_base_path, 'qwen2.5-coder-14b-instruct')
        else:
            max_prompt_length = 4096
            model_path = _generate_model
        is_local_llm = os.path.exists(model_path)

        if _generate_model in [CONSTANTS.codex, CONSTANTS.codegen, CONSTANTS.codellama_13b]:
            is_chat_llm = False
        else:
            is_chat_llm = True
        cls.Generate.max_prompt_length = max_prompt_length
        cls.Generate.model_path = model_path
        cls.Generate.is_local_llm = is_local_llm
        cls.Generate.is_chat_llm = is_chat_llm

        cls._initialized = True

        if multiprocessing.current_process().name == 'MainProcess':
            if cls.Method.debug:
                print('=' * 20 + 'DEBUG' + '=' * 20)
            print('Config Initialized')


Config.init()
