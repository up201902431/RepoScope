import glob
import json
import os
import pickle
from typing import Union

from src.config import Config


class Tools:
    @staticmethod
    def read_code(filename):
        with open(filename, 'r', encoding='utf8') as f:
            return f.read()

    @staticmethod
    def write_file(text: str, filename):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(text)

    @staticmethod
    def append_write_file(text: str, filename):
        with open(filename, 'a', encoding='utf8') as f:
            f.write(text)

    @staticmethod
    def check_and_reuse(filename):
        if Config.Data.reuse_cache and os.path.exists(filename):
            print(f'Reuse cache file {filename}')
            return True
        return False

    @staticmethod
    def load_pickle(filename, default=None):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except EOFError:
            return default

    @staticmethod
    def dump_pickle(obj, filename):
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def dump_json(obj, filename, indent: int = 4):
        with open(filename, 'w', encoding='utf8') as f:
            json.dump(obj, f, indent=indent)

    @staticmethod
    def dump_jsonl(obj, filename):
        with open(filename, 'w', encoding='utf8') as f:
            for item in obj:
                f.write(json.dumps(item) + '\n')

    @staticmethod
    def load_json(filename):
        with open(filename, 'r', encoding='utf8') as f:
            return json.load(f)

    @staticmethod
    def load_jsonl(filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf8') as f:
            lines = []
            for line in f:
                lines.append(json.loads(line))
            return lines

    @staticmethod
    def convert_json_list_to_dict(json_list, key: Union[str, list[str]]):
        result = {}
        if isinstance(key, str):
            key = [key]
        for item in json_list:
            v = item
            for k in key:
                assert k in v
                v = v[k]
            result[v] = item
        return result

    @staticmethod
    def iterate_repository(repo):
        base_dir = Config.Data.repos_path
        pattern = os.path.join(f'{base_dir}{os.sep}{repo}', "**", "*.py")
        files = glob.glob(pattern, recursive=True)

        skipped_files = []
        loaded_code_files = dict()
        base_dir_list = os.path.normpath(base_dir).split(os.sep)
        for filename in files:
            try:
                code = Tools.read_code(filename)
                fpath_tuple = tuple(os.path.normpath(filename).split(os.sep)[len(base_dir_list):])
                loaded_code_files[fpath_tuple] = code
            except Exception as e:
                skipped_files.append((filename, e))
                continue

        if len(skipped_files) > 0:
            print(f"Skipped {len(skipped_files)} out of {len(files)} files due to I/O errors")
            for filename, e in skipped_files:
                print(f"{filename}: {e}")
        return loaded_code_files

    @staticmethod
    def print_info(*info):
        print(f"[INFO]", *info)
