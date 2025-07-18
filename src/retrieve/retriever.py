# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import os

from src.retrieve.build_vector import BuildVectorWrapper
from src.retrieve.make_fragment import MakeFragmentWrapper
from src.retrieve.search_code import SearchCodeWrapper
from src.retrieve.vectorizer import Vectorizer

os.environ["TOKENIZERS_PARALLELISM"] = "false"


class RetrieveWrapper:
    @staticmethod
    def vectorize_repos():
        MakeFragmentWrapper.fragment_for_repo_files()
        BuildVectorWrapper.vector_for_repo_fragments()

    @staticmethod
    def retrieve_for_baseline():
        MakeFragmentWrapper.fragment_for_baseline()
        BuildVectorWrapper.vector_for_baseline()
        SearchCodeWrapper.search_for_baseline()

    @staticmethod
    def retrieve_for_ground_truth():
        MakeFragmentWrapper.fragment_for_ground_truth()
        BuildVectorWrapper.vector_for_ground_truth()
        SearchCodeWrapper.search_for_ground_truth()

    @staticmethod
    def retrieve_for_call_chain():
        MakeFragmentWrapper.fragment_for_call_chain()
        BuildVectorWrapper.vector_for_call_chain()
        SearchCodeWrapper.search_for_call_chain()

    @staticmethod
    def retrieve_for_prediction():
        MakeFragmentWrapper.fragment_for_prediction()
        BuildVectorWrapper.vector_for_prediction()
        SearchCodeWrapper.search_for_prediction()

    @staticmethod
    def free_vectorizer():
        Vectorizer.free()

if __name__ == '__main__':
    # main()
    pass
