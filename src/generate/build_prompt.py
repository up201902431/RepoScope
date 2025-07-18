# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import functools
import itertools
import os.path
from collections import defaultdict
from typing import Optional, Union

from tqdm import tqdm

from src.code_graph.call_chain import CallChain
from src.code_graph.node.base_node import CodeGraphNode
from src.code_graph.node.func_node import FunctionNode
from src.config import Config, CONSTANTS
from src.evaluate.extractor import ExtractPlanWrapper
from src.generate.prompt_template import fragment_block_prompt, our_prompt, baseline_prompt, plan_prompt, \
    api_choose_prompt
from src.generate.tokenizer import Tokenizer
from src.utils import Tools, FilePathBuilder
from src.utils.dataset_loader import DatasetLoader, DataSetRepo


class PromptBuilder:
    def __init__(
            self, repo: DataSetRepo, fragment_size, slice_size,
            existed_task_ids: set[str], mode: str = CONSTANTS.GENERATE
    ):
        self.repo = repo
        self.repo_name = repo.repo_name
        self.fragment_size = fragment_size
        self.slice_size = slice_size
        self.context_planner = ExtractPlanWrapper(fragment_size, slice_size)
        self.existed_task_ids = existed_task_ids
        self.mode = mode
        self.method = Config.Method.type
        self.graph_info = None
        self.repo_parser = None

    @staticmethod
    def _make_a_fragment_block(retrieved_context):
        content, _ = retrieved_context
        metadata = content['metadata']
        # put the file path in the comment
        assert metadata[0]['fpath_tuple'][0] == metadata[0]['repo']
        f_paths = ['/'.join(x['fpath_tuple'][1:]) for x in metadata]
        f_paths_str = ', '.join(f_paths)
        # aggregate the comment and the code lines
        block_str = fragment_block_prompt(f_paths_str, content['context'])
        tokenized_block = Tokenizer.tokenize(block_str)
        token_len = len(tokenized_block)
        return block_str, token_len

    @staticmethod
    def _build_fragments(top_k_context, max_length: float):
        current_token_length = 0
        prepend_blocks = []
        chosen_context = []
        for retrieved_context in top_k_context[::-1]:
            if len(chosen_context) >= Config.Prompt.num_sim_fragments:
                break
            block_str, token_len = PromptBuilder._make_a_fragment_block(retrieved_context)
            if current_token_length + token_len <= max_length:
                prepend_blocks.insert(0, block_str) 
                current_token_length += token_len
                chosen_context.append(retrieved_context)
        return prepend_blocks, chosen_context, current_token_length

    def _build_call_chains_or_nodes(
            self, function_node: Optional[FunctionNode], top_k_choices: Union[list[CallChain], list[CodeGraphNode]],
            max_length: float, max_num_choices: int, use_function_full_content: bool
    ):
        combiner_builder = lambda combiner_func, choices: combiner_func(
            choices, sorted_by_distance_to=function_node, use_full_content=use_function_full_content
        )
        if len(top_k_choices) > 0 and isinstance(top_k_choices[0], CallChain):
            combiner = lambda choices: combiner_builder(CallChain.dump_call_chains, choices)[CONSTANTS.COMBINED]
        else:
            combiner = lambda choices: combiner_builder(CallChain.dump_nodes, choices)

        chosen = []
        chosen_token_length = 0
        for choice in top_k_choices:
            if self.method == CONSTANTS.OURS and len(chosen) >= max_num_choices:
                break
            combined = combiner(chosen + [choice])
            current_token_length = len(Tokenizer.tokenize(combined))
            if current_token_length <= max_length:
                chosen.insert(0, choice)
                chosen_token_length = current_token_length
        return combiner(chosen), chosen_token_length

    def _combine_retrieval_results(self):
        if self.mode == CONSTANTS.CONTEXT_PLAN:
            modes = [CONSTANTS.bl]
        elif self.mode == CONSTANTS.API_CHOOSE:
            modes = []
        elif self.mode == CONSTANTS.GENERATE:
            if self.method in [
                CONSTANTS.BASELINE, CONSTANTS.OURS, CONSTANTS.CALLEE_GROUND_TRUTH, CONSTANTS.CALLEE_BASELINE, CONSTANTS.OURS_PLUS_REPO_CODER
            ]:
                if os.getenv('PREDICT') == 'true':
                    modes = [None]
                else:
                    modes = [CONSTANTS.bl]
                if self.method != CONSTANTS.BASELINE and Config.Method.retrieve_fragments_for_call_chains:
                    modes.append(CONSTANTS.cc)
            elif self.method == CONSTANTS.GROUND_TRUTH:
                modes = [CONSTANTS.gt]
            elif self.method == CONSTANTS.REPO_CODER:
                if os.getenv('PREDICT') == 'true':
                    modes = [None]
                else:
                    modes = [CONSTANTS.bl]
            elif self.method in [CONSTANTS.DIRECT, CONSTANTS.OURS_PLUS_RLCODER]:
                modes = []
            else:
                raise NotImplementedError()
        else:
            raise NotImplementedError()
        task_id_to_retrieval_results = defaultdict(list)
        task_id_to_combined_retrieval_results = defaultdict(dict)
        for task in DatasetLoader.load_tasks_from_repo(self.repo):
            task_id_to_combined_retrieval_results[task.task_id] = {
                'metadata': {
                    'task_input': task.task_input
                },
                'query_fragments': [],
                'top_k_context': []
            }
        if self.method == CONSTANTS.OURS_PLUS_RLCODER:
            retrieved_results = Tools.convert_json_list_to_dict(
                Tools.load_jsonl(Config.Data.benchmark_path.replace('.jsonl', '_RLCoder_retrieved.jsonl')), 'task_id'
            )
            for task in DatasetLoader.load_tasks_from_repo(self.repo):
                task_id_to_combined_retrieval_results[task.task_id]['top_k_context'] = [
                    ({
                        'context': block['content'],
                        'metadata': [
                            {
                                'repo': block['filepath'].split('/')[0],
                                'fpath_tuple': block['filepath'].split('/')
                            }
                        ]
                    }, None) for block in retrieved_results[task.task_id]['blocks'][::-1]
                ]
            return task_id_to_combined_retrieval_results

        for mode in modes:
            retrieval_results_path = FilePathBuilder.retrieval_results_path(
                mode, self.repo_name, self.fragment_size, self.slice_size
            )
            retrieval_results = Tools.load_pickle(retrieval_results_path)
            for task in DatasetLoader.load_tasks_from_repo(self.repo):
                task_id = task.task_id
                task_retrieval_result = retrieval_results[task_id]
                for fragment_retrieval_result in task_retrieval_result:
                    task_id_to_retrieval_results[task_id].extend(fragment_retrieval_result['top_k_context'])
                    task_id_to_combined_retrieval_results[task_id]['metadata'] = task_retrieval_result[0]['metadata']
                    task_id_to_combined_retrieval_results[task_id]['query_fragments'].append({
                        'context': fragment_retrieval_result['context'],
                        'metadata': fragment_retrieval_result['metadata'],
                    })
        for task_id, retrieval_results in task_id_to_retrieval_results.items():
            existed_fragments = set()
            unique_retrieval_results = []
            for retrieval_result in sorted(retrieval_results, key=lambda x: x[1], reverse=True):
                context = retrieval_result[0]['context']
                if context not in existed_fragments:
                    existed_fragments.add(context)
                    unique_retrieval_results.append(retrieval_result)
            task_id_to_combined_retrieval_results[task_id]['top_k_context'] = sorted(
                unique_retrieval_results, key=lambda x: x[1], reverse=False
            )
        return task_id_to_combined_retrieval_results

    def build(self):
        new_prompt_lines = []
        retrieval_results = self._combine_retrieval_results()
        for task in DatasetLoader.load_tasks_from_repo(self.repo):
            task_id = task.task_id
            retrieval_result = retrieval_results[task_id]
            if task_id in self.existed_task_ids:
                continue
            task_input = retrieval_result['metadata']['task_input']

            fragments_alloc_weight = int(Config.Method.include_sim_fragments)
            call_chain_alloc_weight = int(Config.Method.include_call_chains)
            sim_function_alloc_weight = int(Config.Method.include_sim_functions)
            caller_alloc_weight = int(Config.Method.include_callers)

            if self.graph_info is None:
                self.graph_info = Tools.load_pickle(self.repo.graph_info_cache_path, default={})
            if self.method in [CONSTANTS.OURS, CONSTANTS.CALLEE_GROUND_TRUTH, CONSTANTS.CALLEE_BASELINE, CONSTANTS.OURS_PLUS_REPO_CODER, CONSTANTS.OURS_PLUS_RLCODER]:
                task_graph_info = self.graph_info[task_id]
                function_node: Optional[FunctionNode] = task_graph_info[CONSTANTS.FUNC_NODE]
                sim_functions = task_graph_info[CONSTANTS.SIM_FUNCS]
                callers = task_graph_info[CONSTANTS.CALLERS]
                task_path = function_node.formatted_parent_path if function_node is not None else ''
                if self.method in [CONSTANTS.OURS, CONSTANTS.OURS_PLUS_REPO_CODER, CONSTANTS.OURS_PLUS_RLCODER]:
                    call_chains: list[CallChain] = task_graph_info[CONSTANTS.PREDICT_CALL_CHAINS]
                elif self.method == CONSTANTS.CALLEE_GROUND_TRUTH:
                    call_chains = task_graph_info[CONSTANTS.GROUND_TRUTH_CALLEES]
                else:
                    call_chains = task_graph_info[CONSTANTS.DEFAULT_CALLEES]
                if self.mode == CONSTANTS.CONTEXT_PLAN:
                    prompt_builder = functools.partial(
                        plan_prompt, task_input=task_input, import_statements=task_graph_info[CONSTANTS.IMPORTS],
                        task_path=task_path,
                    )
                elif self.mode == CONSTANTS.API_CHOOSE:
                    prompt_builder = functools.partial(
                        api_choose_prompt, task_input=task_input, import_statements=task_graph_info[CONSTANTS.IMPORTS],
                        task_path=task_path
                    )
                    fragments_alloc_weight = sim_function_alloc_weight = caller_alloc_weight = 0
                elif self.mode == CONSTANTS.GENERATE:
                    self.context_planner.extract_and_map_plan(task_id)
                    prompt_builder = functools.partial(
                        our_prompt, task_input=task_input, import_statements=task_graph_info[CONSTANTS.IMPORTS],
                        task_path=task_path
                    )
                else:
                    raise NotImplementedError()
            else:
                prompt_builder = functools.partial(baseline_prompt, task_input=task_input)
                call_chain_alloc_weight = sim_function_alloc_weight = caller_alloc_weight = 0
                call_chains = sim_functions = callers = []
                function_node = None
                if self.method == CONSTANTS.DIRECT:
                    fragments_alloc_weight = 0

            total_weight = max(1,
                fragments_alloc_weight + call_chain_alloc_weight + sim_function_alloc_weight + caller_alloc_weight)
            current_length = len(Tokenizer.tokenize(prompt_builder(
                fragment_blocks=[], call_chain='', sim_function='', caller='', api_level=Config.Data.api_level,
            )))
            remaining_length = Config.Generate.max_prompt_length - current_length
            fragments_length = remaining_length * fragments_alloc_weight / total_weight
            call_chain_length = remaining_length * call_chain_alloc_weight / total_weight
            sim_function_length = remaining_length * sim_function_alloc_weight / total_weight
            caller_length = remaining_length * caller_alloc_weight / total_weight

            relevant_fragment_blocks = combined_callees = combined_sim_functions = \
                combined_callers = chosen_fragments = None
            for step in range(2):
                max_fragment_length = fragments_length if step == 0 else \
                    remaining_length - sim_function_length - call_chain_length - caller_length
                relevant_fragment_blocks, chosen_fragments, fragments_length = self._build_fragments(
                    retrieval_result['top_k_context'], max_fragment_length
                )
                max_sim_function_length = sim_function_length if step == 0 else \
                    remaining_length - fragments_length - call_chain_length - caller_length
                combined_sim_functions, sim_function_length = self._build_call_chains_or_nodes(
                    function_node, sim_functions, max_sim_function_length,
                    max_num_choices=Config.Prompt.num_sim_functions,
                    use_function_full_content=Config.Method.sim_function_use_full_content
                )
                max_call_chain_length = call_chain_length if step == 0 else \
                    remaining_length - fragments_length - sim_function_length - caller_length
                combined_callees, call_chain_length = self._build_call_chains_or_nodes(
                    function_node, call_chains, max_call_chain_length,
                    max_num_choices=Config.Prompt.num_call_chains,
                    use_function_full_content=Config.Method.call_chain_use_full_content
                )
                max_caller_length = caller_length if step == 0 else \
                    remaining_length - fragments_length - sim_function_length - call_chain_length
                combined_callers, caller_length = self._build_call_chains_or_nodes(
                    function_node, callers, max_caller_length,
                    max_num_choices=Config.Prompt.num_callers, use_function_full_content=True
                )

            new_prompt_line = {
                'task_id': task_id,
                'prompt': prompt_builder(
                    fragment_blocks=relevant_fragment_blocks, call_chain=combined_callees,
                    sim_function=combined_sim_functions, caller=combined_callers, api_level=Config.Data.api_level
                ),
                'metadata': {**retrieval_result['metadata']},
            }
            new_prompt_line['metadata']['query_fragments'] = [
                {
                    'context': x['context'],
                    'metadata': x['metadata'],
                } for x in retrieval_result['query_fragments']
            ]
            new_prompt_line['metadata']['top_k_context'] = [
                {
                    'context': x[0]['context'],
                    'metadata': x[0]['metadata'],
                    'sim_score': x[1],
                } for x in chosen_fragments
            ]
            new_prompt_lines.append(new_prompt_line)
        return new_prompt_lines


class BuildPromptWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def _run(mode: str = CONSTANTS.GENERATE):
        for fragment_size, slice_size in itertools.product(
                BuildPromptWrapper.fragment_sizes, BuildPromptWrapper.slice_sizes
        ):
            if mode == CONSTANTS.GENERATE:
                output_file_path = FilePathBuilder.prompt_path(fragment_size, slice_size)
            else:
                output_file_path = FilePathBuilder.plan_prompt_path(mode, fragment_size, slice_size)
            existed_task_ids = set()
            if os.path.exists(output_file_path):
                prompts = Tools.load_jsonl(output_file_path)
            else:
                prompts = []
            print(f'Building prompt, mode = {mode}')
            for prompt_item in prompts:
                existed_task_ids.add(prompt_item['task_id'])
            print(f'Existed prompts: {len(prompts)}')
            bar = tqdm(initial=len(prompts))
            # assert len(prompts) == 0
            for repo in DatasetLoader.load_repos():
                prompts.extend(PromptBuilder(repo, fragment_size, slice_size, existed_task_ids, mode).build())
                bar.n = len(prompts)
                bar.refresh()
            bar.close()
            Tools.dump_jsonl(prompts, output_file_path)
            print(output_file_path)
            # exit(-1)

    @staticmethod
    def build_generate_prompt():
        BuildPromptWrapper._run()

    @staticmethod
    def build_context_plan_prompt():
        BuildPromptWrapper._run(mode=CONSTANTS.CONTEXT_PLAN)

    @staticmethod
    def build_api_choose_prompt():
        BuildPromptWrapper._run(mode=CONSTANTS.API_CHOOSE)
