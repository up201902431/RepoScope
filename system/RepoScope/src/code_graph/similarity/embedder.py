import gc
from typing import Union

import numpy as np
import tiktoken
import torch
from FlagEmbedding import FlagAutoModel
from numpy.linalg import norm
from transformers import AutoModel, logging
from src.config import Config, CONSTANTS

logging.set_verbosity_error()


class Embedder:
    model = None

    @staticmethod
    def init():
        if Embedder.model is not None:
            return
        embedder_name = Config.GraphParser.embedder_name
        if embedder_name == CONSTANTS.p50k_base:
            Embedder.model = tiktoken.get_encoding(CONSTANTS.p50k_base)
        else:
            model_path = Config.GraphParser.model_path
            if embedder_name == CONSTANTS.bge_small:
                if torch.cuda.is_available():
                    Embedder.model = FlagAutoModel.from_finetuned(
                        model_path, max_memory=Config.GraphParser.memory_map()
                    )
                else:
                    Embedder.model = FlagAutoModel.from_finetuned(
                        model_path, devices='cpu', use_fp16=False
                    )
            else:
                Embedder.model = AutoModel.from_pretrained(
                    model_path,
                    **({'max_memory': Config.GraphParser.memory_map()} if torch.cuda.is_available() else {}),
                    trust_remote_code=True
                )
                if not torch.cuda.is_available():
                    Embedder.model = Embedder.model.to('cpu')
        print('Embedder initialized')

    @staticmethod
    def encode(text: str) -> Union[np.ndarray, list[int]]:
        Embedder.init()
        if Embedder.model == CONSTANTS.p50k_base:
            return Embedder.model.encode_ordinary(text)
        with torch.no_grad():
            return Embedder.model.encode(text)

    @staticmethod
    def encode_many(texts: list[str], batch_size: int = 32) -> np.ndarray:
        Embedder.init()
        if Embedder.model == CONSTANTS.p50k_base:
            return np.asarray([Embedder.model.encode_ordinary(text) for text in texts])
        with torch.no_grad():
            return Embedder.model.encode(texts, batch_size=batch_size)

    @staticmethod
    def free():
        if Embedder.model is None:
            return
        # del Embedder.model
        torch.cuda.empty_cache()
        gc.collect()
        print('Embedder freed')

    @staticmethod
    def calculate_similarity(embedding1, embedding2) -> float:
        def cos_sim(a, b):
            return (a @ b.T) / (norm(a) * norm(b))

        def jaccard_similarity(list1, list2):
            set1 = set(list1)
            set2 = set(list2)
            intersection = len(set1 & set2)
            union = len(set1 | set2)
            return float(intersection) / union

        if Config.GraphParser.embedder_name == CONSTANTS.p50k_base:
            return jaccard_similarity(embedding1, embedding2)
        else:
            return cos_sim(embedding1, embedding2)

    @classmethod
    def calculate_similarity_for_text(cls, text1, text2):
        return cls.calculate_similarity(Embedder.encode(text1), Embedder.encode(text2))


if __name__ == '__main__':
    Embedder.init()
    _embedding1 = Embedder.encode('find a ball')
    _embedding2 = Embedder.encode('there is a basketball')
    print(Embedder.calculate_similarity(_embedding1, _embedding2))
