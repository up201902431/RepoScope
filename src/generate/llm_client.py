import gc
import time
from collections import Counter
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from itertools import product
from time import sleep
from typing import Union, Optional

import torch
from openai import OpenAI
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.config import Config, CONSTANTS
from src.utils import FilePathBuilder, Tools
from src.utils.dataset_loader import DatasetLoader


class Client:
    tokenizer = None
    model = None
    model_path: str = Config.Generate.model_path
    is_local_llm: bool = Config.Generate.is_local_llm
    is_chat_llm: bool = Config.Generate.is_chat_llm

    deepseek_client = OpenAI(
        api_key=Config.Generate.deepseek_api_key,
        base_url="https://api.deepseek.com"
    )

    @classmethod
    def init(cls):
        if cls.model is not None:
            return
        if cls.is_local_llm:
            cls.tokenizer = AutoTokenizer.from_pretrained(cls.model_path, trust_remote_code=True)
            if cls.tokenizer.pad_token_id is None:
                cls.tokenizer.pad_token_id = cls.tokenizer.eos_token_id
            cls.model = AutoModelForCausalLM.from_pretrained(
                cls.model_path, trust_remote_code=True, device_map='auto', max_memory=Config.Generate.memory_map()
            )
        else:
            cls.model = Client.model_path
        print('LLM initialized')

    def __init__(self):
        self.init()
        # self.lock = threading.Lock()
        self.messages = []

    def generate(self, user_request: Union[str, list[dict[str, str]]], **kwargs) -> tuple[str, Optional[str]]:
        if isinstance(user_request, str):
            self.messages.append({'role': 'user', 'content': user_request})
        else:
            self.messages = user_request
        temperature = kwargs.get('temperature', 0.0)
        if not self.is_local_llm:
            args = {
                'model': self.model,
                'temperature': 0,
                'messages': self.messages
            }
            if self.model.startswith('deepseek'):
                client = self.deepseek_client
            else:
                raise NotImplementedError()
            max_call = 20
            while True:
                try:
                    completion = client.chat.completions.create(**args)
                    return (
                        completion.choices[0].message.content,
                        completion.choices[0].message.reasoning_content if self.model == 'deepseek-reasoner' else None
                    )
                except Exception as e:
                    print(e)
                    max_call -= 1
                    if max_call == 0:
                        raise RuntimeError('Max retries exceeded')
                    time.sleep(10)
        else:
            if self.is_chat_llm:
                inputs = self.tokenizer.apply_chat_template(
                    self.messages, add_generation_prompt=True, return_tensors="pt"
                ).to(self.model.device)
            else:
                inputs = self.tokenizer(user_request, return_tensors="pt").to(self.model.device)['input_ids']
            attention_mask = torch.ones(inputs.shape, dtype=torch.long).to(self.model.device)
            max_new_tokens = kwargs.get('max_new_tokens', 512)
            do_sample = temperature > 0.0
            args = {'temperature': temperature, 'top_p': 0.95} if temperature > 0.0 else {}
            # self.lock.acquire()
            torch.cuda.empty_cache()
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs, max_new_tokens=max_new_tokens, do_sample=do_sample, top_k=50, num_return_sequences=1,
                    eos_token_id=self.tokenizer.eos_token_id, pad_token_id=self.tokenizer.pad_token_id,
                    attention_mask=attention_mask, **args
                )
            torch.cuda.empty_cache()
            # self.lock.release()
            result = self.tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
            del inputs, outputs
            self.messages.append({'role': 'assistant', 'content': result})
            return result, None

    @staticmethod
    def free():
        if Client.model is None:
            return
        # del Client.model
        torch.cuda.empty_cache()
        gc.collect()
        print('LLM freed')


class LLMClientWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def _generate(mode: str = CONSTANTS.GENERATE, prompt_path: str = '', output_path: str = ''):
        for fragment_size, slice_size in product(LLMClientWrapper.fragment_sizes, LLMClientWrapper.slice_sizes):
            if len(prompt_path + output_path) > 0:
                prompt_file = Tools.load_jsonl(prompt_path)
            elif mode == CONSTANTS.GENERATE:
                prompt_file = Tools.load_jsonl(FilePathBuilder.prompt_path(fragment_size, slice_size))
                output_path = FilePathBuilder.raw_prediction_path(fragment_size, slice_size)
            else:
                prompt_file = Tools.load_jsonl(FilePathBuilder.plan_prompt_path(mode, fragment_size, slice_size))
                output_path = FilePathBuilder.plan_prediction_path(mode, fragment_size, slice_size)
            task_id_2_prompt_item = {item['task_id']: item for item in prompt_file}
            print(output_path)
            # exit(-1)
            generations = Tools.load_jsonl(output_path)
            task_id_counter = Counter(generation_item['task_id'] for generation_item in generations)
            args = {}
            if hasattr(Config.Generate, 'temperature'):
                args['temperature'] = Config.Generate.temperature
            if hasattr(Config.Generate, 'max_new_tokens'):
                args['max_new_tokens'] = Config.Generate.max_new_tokens
            max_gen_per_item = 1
            if Config.Generate.is_local_llm:
                for prompt_item in tqdm(prompt_file, desc=f'Generating completions using {Config.Generate.model_name}'):
                    task_id = prompt_item['task_id']
                    while True:
                        if task_id in task_id_counter and task_id_counter[task_id] >= max_gen_per_item:
                            break
                        client = Client()
                        generation, reasoning = client.generate(prompt_item['prompt'], **args)
                        generations.append({
                            'task_id': task_id,
                            'generation': generation,
                            'reasoning': reasoning,
                            **prompt_item
                        })
                        # print(generation)
                        Tools.dump_jsonl(generations, output_path)
                        task_id_counter[task_id] += 1
            else:
                futures = {}
                # res = Client().generate(prompt_file[0]['prompt'], **args)
                executor_class = ThreadPoolExecutor
                max_workers = min(len(prompt_file), 128)
                with executor_class(max_workers=max_workers) as executor:
                    has_reminded = False
                    for task in DatasetLoader.load_tasks():
                        task_id = task.task_id
                        prompt_item = task_id_2_prompt_item[task_id]
                        while True:
                            if task_id in task_id_counter and task_id_counter[task_id] >= max_gen_per_item:
                                break
                            if not has_reminded:
                                for _ in tqdm(range(5), desc=f'We are going to call the {Client.model_path} on {Config.Data.dataset}! If this should not happen, press ctrl+c to exit. 15 seconds remaining'):
                                    sleep(1)
                                has_reminded = True
                            futures[(executor.submit(Client().generate, prompt_item['prompt'], **args))] = (
                                task_id, prompt_item
                            )
                            task_id_counter[task_id] += 1
                    for future in tqdm(
                            as_completed(futures), total=len(futures),
                            desc=f'Generating completions using {Config.Generate.model_name}'
                    ):
                        generation, reasoning = future.result()
                        task_id, prompt_item = futures[future]
                        generations.append({
                            'task_id': task_id,
                            'generation': generation,
                            'reasoning': reasoning,
                            **prompt_item
                        })
                        # print(generation)
                        Tools.dump_jsonl(generations, output_path)

    @staticmethod
    def free_llm():
        Client.free()

    @staticmethod
    def generate_completions(prompt_path: str = '', output_path: str = ''):
        LLMClientWrapper._generate(prompt_path=prompt_path, output_path=output_path)

    @staticmethod
    def generate_context_plans():
        LLMClientWrapper._generate(mode=CONSTANTS.CONTEXT_PLAN)

    @staticmethod
    def generate_api_choices():
        LLMClientWrapper._generate(mode=CONSTANTS.API_CHOOSE)


if __name__ == '__main__':
    while True:
        query = input('Query: ')
        print('\nReasoning: '.join(map(str, Client().generate(query))))