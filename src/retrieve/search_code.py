# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import copy
import itertools
import os
from collections import defaultdict
from concurrent.futures import as_completed, ProcessPoolExecutor

import numpy as np
import tqdm

from src.config import CONSTANTS, Config
from src.retrieve.vectorizer import Vectorizer
from src.utils import Tools, FilePathBuilder
from src.utils.dataset_loader import DatasetLoader


class CodeSearchWorker:
    def __init__(self, repo_embedding_lines, query_embedding_lines, output_path):
        self.repo_embedding_lines = repo_embedding_lines  # list
        self.query_embedding_lines = query_embedding_lines  # list
        self.output_path = output_path

    @staticmethod
    def _is_context_after_hole(repo_embedding_line, query_line):
        hole_fpath_tuple = tuple(query_line['metadata']['fpath_tuple'])
        context_is_not_after_hole = []
        for metadata in repo_embedding_line['metadata']:
            if tuple(metadata['fpath_tuple']) != hole_fpath_tuple:
                context_is_not_after_hole.append(True)
                continue
            # now we know that the repo line is in the same file as the hole
            if metadata['end_line_no'] <= query_line['metadata']['context_start_lineno']:
                context_is_not_after_hole.append(True)
                continue
            context_is_not_after_hole.append(False)
        return not any(context_is_not_after_hole)
        
    def _find_top_k_context(self, query_line):
        top_k_context = []
        query_embedding = np.array(query_line['data'][0]['embedding'])
        for repo_embedding_line in self.repo_embedding_lines:
            if self._is_context_after_hole(repo_embedding_line, query_line):
                continue
            repo_line_embedding = np.array(repo_embedding_line['data'][0]['embedding'])
            similarity_score = Vectorizer.calculate_similarity(query_embedding, repo_line_embedding)
            top_k_context.append((repo_embedding_line, similarity_score))
        top_k_context = sorted(top_k_context, key=lambda x: x[1], reverse=False)[-Config.Retrieval.max_sim_fragments:]
        return top_k_context

    def run(self):
        if Tools.check_and_reuse(self.output_path):
            return
        query_lines_with_retrieved_results = defaultdict(list)
        for query_line in self.query_embedding_lines:
            new_line = copy.deepcopy(query_line)
            top_k_context = self._find_top_k_context(new_line)
            new_line['top_k_context'] = top_k_context
            query_lines_with_retrieved_results[query_line['metadata']['task_id']].append(new_line)
        Tools.dump_pickle(query_lines_with_retrieved_results, self.output_path)


class SearchCodeWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def _run_parallel(mode):
        workers = []
        for fragment_size, slice_size in itertools.product(SearchCodeWrapper.fragment_sizes, SearchCodeWrapper.slice_sizes):
            for repo in DatasetLoader.load_repos():
                repo_name = repo.repo_name
                output_path = FilePathBuilder.retrieval_results_path(mode, repo_name, fragment_size, slice_size)
                if Tools.check_and_reuse(output_path):
                    continue
                if os.getenv('PREDICT') == 'true':
                    query_embedding_path = FilePathBuilder.second_stage_vector_path(repo_name, fragment_size, slice_size)
                else:
                    query_embedding_path = FilePathBuilder.first_stage_vector_path(mode, repo_name, fragment_size)
                repo_embedding_path = FilePathBuilder.repo_vector_path(repo_name, fragment_size, slice_size)
                repo_embedding_lines = Tools.load_pickle(repo_embedding_path)
                query_embedding_lines = Tools.load_pickle(query_embedding_path)
                worker = CodeSearchWorker(repo_embedding_lines, query_embedding_lines, output_path)
                workers.append(worker)
        # process pool
        with ProcessPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(worker.run, ) for worker in workers}
            for future in tqdm.tqdm(as_completed(futures), total=len(futures), desc=f'Searching code for {mode}'):
                future.result()

    @staticmethod
    def search_for_baseline():
        SearchCodeWrapper._run_parallel(CONSTANTS.bl)

    @staticmethod
    def search_for_ground_truth():
        SearchCodeWrapper._run_parallel(CONSTANTS.gt)

    @staticmethod
    def search_for_call_chain():
        SearchCodeWrapper._run_parallel(CONSTANTS.cc)

    @staticmethod
    def search_for_prediction():
        SearchCodeWrapper._run_parallel(None)
