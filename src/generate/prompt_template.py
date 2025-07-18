from src.config import Config

seperator = '# ' + '-' * Config.Prompt.num_seperators


def fragment_block_prompt(fragment_paths: str, fragment_content: str):
    fragment_content = '\n'.join(f'# {line}' for line in fragment_content.strip().splitlines())
    return f"""
# Below code fragment can be found in: {fragment_paths}
{seperator}
{fragment_content}
{seperator}
""".strip()


def baseline_prompt(
        task_input: str, fragment_blocks: list[str], addition: str = '', api_level: bool = False, **kwargs
):
    for key, value in kwargs.items():
        assert len(value) == 0
    prefix = f'# You need to {"append **a new complete line** at the end of the incomplete code" if api_level else "implement the function"} located at the end of the instruction based on relevant repository information.'
    fragment_blocks_str = '\n'.join(fragment_blocks).strip()
    if len(fragment_blocks_str) == 0:
        if len(addition) == 0:
            prefix = ''
            fragment_blocks_prompt = ''
        else:
            fragment_blocks_prompt = seperator
    else:
        fragment_blocks_prompt = f"""
# Here are some relevant code fragments from the repo:
{seperator}
{fragment_blocks_str}
""".strip()

    if api_level:
        final_instruction = """
# Please append **a new complete line** at the end of the following incomplete code
# Only the newly added line needs to be output:
""".strip()
    else:
        final_instruction = """
# Please implement the following function:
""".strip()

    # return fragment_blocks_prompt
    return f"""
{prefix}
{fragment_blocks_prompt}
{addition}

{final_instruction}

{task_input}
""".strip()


def our_prompt(
        task_input: str, fragment_blocks: list[str], import_statements: list[str],
        task_path: str, call_chain: str, sim_function: str, caller: str, api_level: bool = False
):
    if not Config.Method.include_sim_fragments:
        fragment_blocks = []

    if Config.Method.include_imports:
        import_statements_str = '\n'.join(import_statements)
    else:
        import_statements_str = ''

    if Config.Method.include_func_path:
        task_path_prompt = f'\n# {task_path}'
    else:
        task_path_prompt = ''

    task_input = f"""
{import_statements_str}
{task_path_prompt}
{task_input}
""".strip()

    if len(caller) == 0 or not Config.Method.include_callers:
        caller_prompt = ''
    else:
        caller = '\n'.join('# ' + line for line in caller.splitlines()).strip()
        caller_prompt = f"""
# Here are some functions in the repo that invoke the {'last function' if api_level else 'target function'}:
{seperator}
{caller}
{seperator}
""".strip()

    if len(call_chain) > 0 and Config.Method.include_call_chains:
        call_chain = '\n'.join('# ' + line for line in call_chain.splitlines()).strip()
        call_chain_prompt = f"""
# Here are some relevant classes, functions, or attributes in the repo that you might use in the {'new line' if api_level else 'target function'}:
{seperator}
{call_chain}
{seperator}
""".strip()
    else:
        call_chain_prompt = ''

    if len(sim_function) > 0 and Config.Method.include_sim_functions:
        sim_function = '\n'.join('# ' + line for line in sim_function.splitlines()).strip()
        sim_function_prompt = f"""
# Here are some functions in the repo that are similar to the {'last function' if api_level else 'target function'}:
{seperator}
{sim_function}
{seperator}
""".strip()
    else:
        sim_function_prompt = ''

    addition = f"""
{caller_prompt}
{call_chain_prompt}
{sim_function_prompt}
""".strip()

    return baseline_prompt(task_input, fragment_blocks, addition=addition, api_level=api_level)


def plan_prompt(
        task_input: str, fragment_blocks: list[str], import_statements: list[str],
        task_path: str, call_chain: str, callers: list[str]
):
    fragment_blocks_str = '\n'.join(fragment_blocks).strip()
    if len(fragment_blocks_str) == 0:
        fragment_blocks_prompt = ''
    else:
        fragment_blocks_prompt = f"""
# Here are some relevant code fragments from the repo:
{seperator}
{fragment_blocks_str}
""".strip()

    import_statements_str = '\n'.join(import_statements)
    task_input = f"""
{import_statements_str}

# {task_path}
{task_input}
""".strip()

    if len(callers) == 0:
        callers_prompt = ''
    else:
        callers_str = '\n\n'.join(callers)
        callers_str = '\n'.join('# ' + line for line in callers_str.splitlines())
        callers_prompt = f"""
# This is the INVOKER:
{seperator}
{callers_str}
{seperator}
""".strip()

    if len(call_chain) == 0:
        call_chain_prompt = ''
    else:
        call_chain_str = '\n'.join('# ' + line for line in call_chain.splitlines()).strip()
        call_chain_prompt = f"""
# These are the APIs:
{seperator}
{call_chain_str}
{seperator}
""".strip()

    return f"""
# You need to decide if the given caller or APIs are needed to implement a function.
{fragment_blocks_prompt}
# You have the following options:
# 1. INVOKER: a function with full content that invokes the target function.
# 2. API: some APIs (i.e. classes, attributes or functions) that the target function may invoke.
# If the given INVOKER is necessary to understand the types of the target function's parameters or return value, you may want to choose option INVOKER.
# If the given APIS will be used in the target function and are necessary to understand them, you may want to choose option API.
# Multiple selections are allowed, and you should provide your reasoning and decision in a JSON format.
# This is a template for your output:
```
{{
    "Reasoning for INVOKER": "I think the INVOKER is unnecessary/necessary because ...<TODO>"
    "INVOKER": false/true,
    "Reasoning for API": "I think the APIS are unnecessary/necessary because ...<TODO>"
    "API": false/true,
}}
```
# If the known information is sufficient for you to implement the target function, you do not need to choose any option.
{seperator}
# The following is the function that needs to be decided:
{task_input}
{seperator}
{callers_prompt}
{call_chain_prompt}
# According to the given INVOKER and APIS, your decision for the above function is:
```
""".strip()


def api_choose_prompt(
        task_input: str, import_statements: list[str], task_path: str, call_chain: str, fragment_blocks: list[str] = None
):
    assert fragment_blocks is None
    import_statements_str = '\n'.join(import_statements)

    task_input = f"""
{import_statements_str}

# {task_path}
{task_input}
""".strip()

    return f"""
There is a code repository function generation task. You will be provided with the signature and documentation of the target function, as well as some potentially relevant APIs (including functions and attributes). 
You need to determine which APIs are helpful for generating the target function and select them. This includes, but is not limited to, the following scenarios:
1. The target function may invoke the selected APIs.
2. The target function and the selected function APIs may have highly similar implementations, making them useful as references for generating the target function.
The APIs will be provided in the format shown in the following example:
```
# src/my_file.py
class MyClass:
    my_attr1: int
    my_attr2: list[str]

    def my_func1(a: int, b: int) -> str:
        \"\"\"
        This is document for my_func1 
        \"\"\"
    
    def my_func2(a: int, b: int) -> str:
        \"\"\"
        This is document for my_func2 
        \"\"\"
    
    def my_func3(a: int, b: int) -> str:
        \"\"\"
        This is document for my_func3 
        \"\"\"
```
For example, if you believe that MyClass.my_attr1 and MyClass.my_func2 in src/my_file.py are helpful for generating the target function, you should output the following content in JSON format:
```
[
    {{
        "file_path": "src/my_file.py,
        "infile_api_path": "MyClass.my_attr1"
    }},
    {{
        "file_path": "src/my_file.py,
        "infile_api_path": "MyClass.my_func2"
    }}
]
```
{seperator}
The following are the candidate APIs:
```
{call_chain}
```
{seperator}
The following is the target function to be generated:
```
{task_input}
```
{seperator}
Now please provide your selection. If you believe none of the APIs are helpful, simply output an empty list:
```
""".strip()