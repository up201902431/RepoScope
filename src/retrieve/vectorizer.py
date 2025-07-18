import gc
from typing import Union

import numpy as np
import scipy
import tiktoken
import torch
from FlagEmbedding import FlagAutoModel
from transformers import AutoTokenizer, AutoModel

from src.config import Config, CONSTANTS


class Vectorizer:
    model = None
    vectorizer_type = Config.Retrieval.vectorizer_type
    vectorizer_name = Config.Retrieval.vectorizer_name

    @classmethod
    def init(cls):
        if cls.model is not None:
            return
        if cls.vectorizer_type == CONSTANTS.TOKENIZER:
            if cls.vectorizer_name == CONSTANTS.p50k_base:
                cls.model = tiktoken.get_encoding(CONSTANTS.p50k_base)
            elif cls.vectorizer_name == CONSTANTS.codegen_6b_mono:
                cls.model = AutoTokenizer.from_pretrained('Salesforce/codegen-6B-mono')
            else:
                raise NotImplementedError()
        else:
            model_path = Config.Retrieval.model_path
            memory_map = Config.Retrieval.memory_map()
            if cls.vectorizer_name == CONSTANTS.bge_small:
                cls.model = FlagAutoModel.from_finetuned(model_path, max_memory=memory_map)
            else:
                cls.model = AutoModel.from_pretrained(model_path, max_memory=memory_map, trust_remote_code=True)
        print('Vectorizer initialized')

    @classmethod
    def encode(cls, text: str) -> Union[np.ndarray, list[int]]:
        if cls.model is None:
            cls.init()
        if cls.vectorizer_name == CONSTANTS.p50k_base:
            return cls.model.encode_ordinary(text)
        else:
            with torch.no_grad():
                return cls.model.encode(text)

    @classmethod
    def free(cls):
        if cls.model is None or cls.vectorizer_type == CONSTANTS.TOKENIZER:
            return
        # del cls.model
        torch.cuda.empty_cache()
        gc.collect()
        print('Vectorizer freed')

    @classmethod
    def calculate_similarity(cls, vector1: np.ndarray, vector2: np.ndarray) -> float:
        if cls.vectorizer_type == CONSTANTS.TOKENIZER:
            return cls._jaccard_similarity(vector1, vector2)
        else:
            assert len(vector1) == len(vector2)
            return cls._cosine_similarity(vector1, vector2)

    @staticmethod
    def _cosine_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        return 1 - scipy.spatial.distance.cosine(embedding1, embedding2)

    @staticmethod
    def _jaccard_similarity(list1: np.ndarray, list2: np.ndarray) -> float:
        set1 = set(list1)
        set2 = set(list2)
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return float(intersection) / union
