import os

from src.code_graph.parser import CodeGraphWrapper
from src.config import Config, CONSTANTS
from src.evaluate.evaluator import EvaluateResultWrapper
from src.evaluate.extractor import ExtractCodeWrapper
from src.generate.build_prompt import BuildPromptWrapper
from src.generate.llm_client import LLMClientWrapper
from src.retrieve.retriever import RetrieveWrapper

import sys

from src.utils import FilePathBuilder

sys.setrecursionlimit(10000)

def main():
    method = Config.Method.type

    if method in [CONSTANTS.OURS, CONSTANTS.CALLEE_GROUND_TRUTH, CONSTANTS.CALLEE_BASELINE, CONSTANTS.OURS_PLUS_RLCODER]:
        CodeGraphWrapper.parse_repos_and_generate_call_chains()
    # exit(-1)
    # Config.Data.reuse_cache = False
    RetrieveWrapper.vectorize_repos()

    if method == CONSTANTS.GROUND_TRUTH:
        RetrieveWrapper.retrieve_for_ground_truth()
    elif method in [CONSTANTS.BASELINE, CONSTANTS.REPO_CODER]:
        RetrieveWrapper.retrieve_for_baseline()
    elif method in [CONSTANTS.OURS, CONSTANTS.OURS_PLUS_REPO_CODER]:
        RetrieveWrapper.retrieve_for_baseline()
        if Config.Method.retrieve_fragments_for_call_chains:
            RetrieveWrapper.retrieve_for_call_chain()
    RetrieveWrapper.free_vectorizer()
    # exit(-1)
    if method == CONSTANTS.OURS:
        if Config.Method.context_include_strategy == CONSTANTS.AUTO:
            BuildPromptWrapper.build_context_plan_prompt()
            LLMClientWrapper.generate_context_plans()
        elif Config.Method.context_include_strategy == CONSTANTS.API_CHOOSE_BY_LLM:
            BuildPromptWrapper.build_api_choose_prompt()
            LLMClientWrapper.generate_api_choices()
            CodeGraphWrapper.supplement_llm_chosen_callees()

    BuildPromptWrapper.build_generate_prompt()
    # exit(-1)
    LLMClientWrapper.generate_completions()
    LLMClientWrapper.free_llm()

    ExtractCodeWrapper.extract()
    EvaluateResultWrapper.evaluate()

    if method in [CONSTANTS.REPO_CODER, CONSTANTS.OURS_PLUS_REPO_CODER]:
        # Config.Data.reuse_cache = False
        os.environ['PREDICT'] = 'true'
        # Config.Data.reuse_cache = False
        RetrieveWrapper.retrieve_for_prediction()
        # Config.Data.reuse_cache = True
        RetrieveWrapper.free_vectorizer()

        BuildPromptWrapper.build_generate_prompt()
        # exit(-1)
        LLMClientWrapper.generate_completions()
        LLMClientWrapper.free_llm()

        ExtractCodeWrapper.extract()
        EvaluateResultWrapper.evaluate()


def evaluate_baseline(method: str):
    base_dir = str(os.path.join(
        Config.Data.project_path, 'results', 'baselines', Config.Data.dataset, method
    ))
    model_base_dir = os.path.join(base_dir, Config.Generate.model_name)
    prompt_path = os.path.join(base_dir, 'prompt.jsonl')
    prediction_path = os.path.join(model_base_dir, 'raw_prediction.jsonl')
    FilePathBuilder.make_needed_dir(prediction_path)
    extract_path = os.path.join(model_base_dir, 'extracted.jsonl')
    std_extract_path = os.path.join(model_base_dir, 'std_extracted.jsonl')
    evaluate_path = os.path.join(model_base_dir, 'evaluated.jsonl')

    LLMClientWrapper.generate_completions(prompt_path=prompt_path, output_path=prediction_path)
    LLMClientWrapper.free_llm()
    ExtractCodeWrapper.extract(
        output_path=extract_path, std_output_path=std_extract_path, raw_prediction_path=prediction_path
    )
    EvaluateResultWrapper.evaluate(prediction_path=extract_path, evaluate_result_path=evaluate_path)


if __name__ == '__main__':
    main()
    # evaluate_baseline(method='CodeAgent')
