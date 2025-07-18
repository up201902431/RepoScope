class CONSTANTS:
    gt = 'gt'
    bl = 'bl'
    cc = 'cc'

    # graph infos
    COMBINED = 'combined'
    SEPARATE = 'separate'
    PREDICT_CALL_CHAINS = 'predict_call_chains'
    LLM_CHOSEN_CALLEES = 'llm_chosen_callees'
    DEFAULT_CALLEES = 'default_callees'
    GROUND_TRUTH_CALLEES = 'ground_truth_callees'
    BASELINE_CALLEES = 'baseline_callees'
    SIM_FUNCS = 'sim_funcs'
    CALLERS = 'callers'
    IMPORTS = 'imports'
    FUNC_PATH = 'func_path'
    GRAPH_CONFIG = 'graph_config'
    FUNC_NODE = 'func_node'

    # embedders or tokenizers
    EMBEDDER = 'embedder'
    TOKENIZER = 'tokenizer'
    bge_small = 'bge-small'
    jina_v3 = 'jina-v3'
    p50k_base = 'p50k_base'
    codegen_6b_mono = 'codegen-6b-mono'

    # models
    codegen = 'codegen'
    codex = 'codex'
    codellama_13b = 'codellama-13b'
    deepseek_coder_7b = 'deepseek-coder-7b'
    qwen_coder_14b = 'qwen-coder-14b'

    # datasets
    codereval = 'codereval'
    deveval = 'deveval'
    repoeval = 'repoeval'
    dataset_to_id_key = {
        codereval: 'question_id',
        deveval: 'namespace',
        repoeval: ['metadata', 'task_id']
    }

    # prompt
    GENERATE = 'generate'
    CONTEXT_PLAN = 'context_plan'
    API_CHOOSE = 'api_choose'

    # context strategy
    FIXED = 'fixed'
    AUTO = 'auto'
    API_CHOOSE_BY_LLM = 'api_choose_by_llm'

    # methods
    DIRECT = 'direct'
    BASELINE = 'baseline'
    GROUND_TRUTH = 'ground_truth'
    REPO_CODER = 'repo_coder'

    OURS = 'ours'
    CALLEE_GROUND_TRUTH = 'callee_ground_truth'
    CALLEE_BASELINE = 'callee_baseline'
    OURS_PLUS_REPO_CODER = 'ours+repo_coder'
    OURS_PLUS_RLCODER = 'ours+rlcoder'
