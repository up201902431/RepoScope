import tiktoken
from transformers import AutoTokenizer

from src.config import Config, CONSTANTS


class Tokenizer:
    tokenizer = None
    llm_name = Config.Generate.model_name

    @staticmethod
    def init():
        if Tokenizer.tokenizer is not None:
            return
        if Tokenizer.llm_name == CONSTANTS.codex or not Config.Generate.is_local_llm:
            Tokenizer.tokenizer = tiktoken.get_encoding(CONSTANTS.p50k_base)
        else:
            Tokenizer.tokenizer = AutoTokenizer.from_pretrained(
                Config.Generate.model_path, clean_up_tokenization_spaces=True
            )
        print('Tokenizer initialized')
    
    @staticmethod
    def tokenize(text: str) -> list[int]:
        Tokenizer.init()
        if Tokenizer.llm_name == CONSTANTS.codex:
            return Tokenizer.tokenizer.encode_ordinary(text)
        else:
            return Tokenizer.tokenizer.encode(text)
