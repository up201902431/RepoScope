# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import itertools
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

from tqdm import tqdm

from src.config import CONSTANTS, Config
from src.retrieve.vectorizer import Vectorizer
from src.utils import Tools, FilePathBuilder
from src.utils.dataset_loader import DatasetLoader


def vectorize_initializer(vectorizer):
    Vectorizer.model = vectorizer


class VectorBuilder:
    @staticmethod
    def build(input_file_path):
        output_file_path = FilePathBuilder.vector_path(input_file_path)
        if Tools.check_and_reuse(output_file_path):
            return
        print(f'building one gram vector for {input_file_path}')
        futures = dict()
        lines = Tools.load_pickle(input_file_path)

        # if Vectorizer.model is None:
        #     Vectorizer.init()

        with ThreadPoolExecutor(
                max_workers=1,  # initializer=vectorize_initializer, initargs=(Vectorizer.model,)
        ) as executor:
            for line in lines:
                futures[executor.submit(Vectorizer.encode, line['context'])] = line
            new_lines = []
            for future in tqdm(as_completed(futures)):
                line = futures[future]
                tokenized = future.result()
                new_lines.append({
                    'context': line['context'],
                    'metadata': line['metadata'],
                    'data': [{'embedding': tokenized}]
                })
            Tools.dump_pickle(new_lines, output_file_path)


class BuildVectorWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def vector_for_repo_fragments():
        for fragment_size, slice_size in itertools.product(
                BuildVectorWrapper.fragment_sizes, BuildVectorWrapper.slice_sizes
        ):
            for repo in tqdm(
                    DatasetLoader.load_repos(), desc=f'Building vector for repos, ws = {fragment_size}, ss = {slice_size}'
            ):
                VectorBuilder.build(FilePathBuilder.repo_fragment_path(repo.repo_name, fragment_size, slice_size))

    @staticmethod
    def _vector_for_some(mode):
        for fragment_size in BuildVectorWrapper.fragment_sizes:
            for repo in tqdm(DatasetLoader.load_repos(), desc=f'Building vector for {mode}, ws = {fragment_size}'):
                VectorBuilder.build(FilePathBuilder.first_stage_fragment_path(mode, repo.repo_name, fragment_size))

    @staticmethod
    def vector_for_baseline():
        BuildVectorWrapper._vector_for_some(CONSTANTS.bl)

    @staticmethod
    def vector_for_ground_truth():
        BuildVectorWrapper._vector_for_some(CONSTANTS.gt)

    @staticmethod
    def vector_for_call_chain():
        BuildVectorWrapper._vector_for_some(CONSTANTS.cc)

    @staticmethod
    def vector_for_prediction():
        for fragment_size, slice_size in itertools.product(
                BuildVectorWrapper.fragment_sizes, BuildVectorWrapper.slice_sizes
        ):
            for repo in DatasetLoader.load_repos():
                fragment_path = FilePathBuilder.second_stage_fragment_path(repo.repo_name, fragment_size, slice_size)
                VectorBuilder.build(fragment_path)
