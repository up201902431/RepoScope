# Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation

- source_pdf: ../../../../../pdf/Evaluation/secondary/Beyond%20Maintenance.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

Beyond Maintenance: A Benchmark and Multi-Agent Framework
for Repository-Usage Code Generation
Kaitao Lin∗
202230200292@mail.scut.edu.cn
South China University of Technology
Guangzhou, China
Songwen Gong∗
202421045674@mail.scut.edu.cn
South China University of Technology
Guangzhou, China
Adam Jatowt
jatowt@gmail.com
University of Innsbruck
Innsbruck, Austria
Jiexin Wang†
jiexinwang@scut.edu.cn
South China University of Technology
Guangzhou, China
Yi Cai†
ycai@scut.edu.cn
South China University of Technology
Guangzhou, China
Abstract
Repository-level code generation has attracted growing interest,
yet most benchmarks and methods remain maintainer-centric, em-
phasizing bug fixing and feature implementation. In contrast, a
common yet underexplored scenario is repository usage: external
users want to build applications by correctly invoking repository-
internal APIs, composing them into runnable end-to-end workflows
rather than modifying the codebase. To support this setting, we in-
troduce RUCCE, a benchmark for repository-usage code generation
built from real-world Python repositories. Each instance pairs a
natural-language usage instruction with grounded target APIs and
a verified reference script, enabling evaluation of both API retrieval
and repository-usage code generation. Building on RUCCE, we
propose RUCACoder, a closed-loop multi-agent framework with
a Retriever for hierarchical repository exploration, a Verifier for
reranking and validation, and a Coder for feedback-driven script
synthesis. Experiments across multiple backbone LLMs show that
RUCACoder consistently outperforms strong retrieval and genera-
tion baselines.1
CCS Concepts
• Information systems →Retrieval models and ranking.
Keywords
repository-usage code generation, multi-agent
ACM Reference Format:
Kaitao Lin, Songwen Gong, Adam Jatowt, Jiexin Wang, and Yi Cai. 2026. Be-
yond Maintenance: A Benchmark and Multi-Agent Framework for Repository-
Usage Code Generation. In Proceedings of the 49th International ACM SIGIR
Conference on Research and Development in Information Retrieval (SIGIR
’26), July 20–24, 2026, Melbourne, VIC, Australia. ACM, New York, NY, USA,
8 pages. https://doi.org/10.1145/3805712.3808589
∗Equal contribution.
†Corresponding authors.
1The RUCCE dataset and RUCACoder code are available at https://huggingface.co/
datasets/31dfaf/RUCCE.
This work is licensed under a Creative Commons Attribution 4.0 International License.
SIGIR ’26, Melbourne, VIC, Australia
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2599-9/2026/07
https://doi.org/10.1145/3805712.3808589
Figure 1: Motivating scenario: In large repositories, develop-
ers often struggle to navigate numerous files and modules to
identify correct APIs and compose them into an end-to-end
usage workflow. Without clear, runnable examples, this pro-
cess becomes slow, error-prone, and difficult to reproduce.
1
Introduction
Recent advances in large language models (LLMs) have enabled
strong performance on various code-related tasks, such as code
generation [3, 26], bug fixing [17, 32], and code translation [24, 25].
While early efforts focused on isolated functions or short code snip-
pets, there has been a notable shift towards repository-level tasks.
This shift has spurred the development of benchmarks and methods
for repository-level code generation [19, 37], code retrieval [9, 15],
and cross-file code repair [16], where models must reason about
cross-file dependencies, interconnected APIs, and shared resources.
Despite these advancements, existing repository-level bench-
marks and methods fail to support practical repository use in two
critical ways. First, they are largely maintenance-centric: they
prioritize bug fixing and feature implementation, and therefore pri-
marily target repository maintainers or experienced contributors.
This focus overlooks a common real-world need: many developers
engage with repositories as users rather than maintainers. Their
goal is not to modify the codebase but to quickly determine how
to use it—which modules to import, which internal components
to invoke, and how to assemble these calls into a valid end-to-
end workflow that adheres to the repository’s design assumptions.
For non-expert users, inferring such usage patterns directly from
the source code can be both costly and unreliable, particularly as
3292

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
Kaitao Lin, Songwen Gong, Adam Jatowt, Jiexin Wang, and Yi Cai
Table 1: Comparison between representative code generation
benchmarks and RUCCE. Comp. Annota. (following DevE-
val [21]) indicates whether a benchmark provides comprehen-
sive annotations, including natural-language requirements,
original repositories, and ground truths.
Benchmark
Language
Real Repo
Repo-level
Comp. Annota.
Consumer View
HumanEval (2021) [3]
Python
✗
✗
✗
✗
MBPP (2021) [2]
Python
✗
✗
✗
✗
ClassEval (2023) [6]
Python
✗
✓
✗
✗
RepoEval (2023) [37]
Python
✓
✓
✓
✗
SWE-bench (2024) [16]
Python
✓
✓
✓
✗
FEA-bench (2025) [19]
Python
✓
✓
✓
✗
DevEval (2024) [21]
Multi
✓
✓
✓
✗
RUCCE (Ours)
Python
✓
✓
✓
✓
repositories scale in size and complexity. As illustrated in Figure 1,
the combination of a complex structure and extensive API surface
can overwhelm users, making it difficult to locate the correct com-
ponents and assemble them into functioning programs. Second,
even when repository-level methods facilitate generation or re-
trieval, they are not optimized for this user-centric objective. Most
repository-level generation studies focus on completing partial con-
texts (e.g., SWE-bench [16]) or implementing isolated functions
(e.g., FEA-bench [19]) by leveraging a small subset of repository’s
APIs. In contrast, effective repository usage requires synthesizing
complete, executable programs that orchestrate multiple internal
APIs into a coherent execution pipeline. This requires a deeper
understanding of API signatures, call ordering constraints, inter-
module dependencies, and repository-specific conventions—going
beyond localized edits or isolated function completion.
To address these challenges, we introduce RUCCE (Repository
Use-Centric Code Evaluation), a benchmark designed to evaluate
LLMs’ capabilities in repository-usage code generation. RUCCE con-
sists of tasks in which models must generate complete, executable,
end-to-end programs by composing complex, multi-step internal
API sequences from a repository. Unlike maintenance-centric bench-
marks that emphasize localized edits or single-function completion,
RUCCE evaluates two key abilities: (i) identifying the correct in-
ternal APIs and relevant code evidence from a large codebase, and
(ii) organizing these APIs into a coherent, executable workflow by
generating code that respects repository-specific dependencies and
usage conventions. Table 1 provides a comparison between existing
code generation benchmarks and RUCCE. By shifting evaluation
from maintenance to consumer view, RUCCE enables systematic, re-
producible comparisons of LLM performance in practical repository-
usage scenarios within real-world, large-scale codebases.
Building upon RUCCE, we propose RUCACoder, a multi-agent
framework that integrates dynamic state tracking with iterative
reasoning and tool-based execution for repository-usage code gen-
eration. This framework enables multiple autonomous agents to
collaborate and explore repositories in a structured, hierarchical
manner. By continuously refining their understanding of repository
contents through feedback loops and utilizing external tools to inter-
act with the code, RUCACoder effectively bridges the gap between
high-level user intent and low-level code functionality. The multi-
agent system autonomously manages tasks such as interpreting
API documentation, identifying relevant code fragments, and facili-
tating repository interactions, thereby making complex repository
functionalities more accessible, particularly to non-expert users.
Extensive experiments on RUCCE demonstrate that RUCACoder
significantly improves both API retrieval accuracy and downstream
code generation quality compared to existing baselines.
In summary, this work presents three key contributions:
• We identify an important yet underexplored task, repository-usage
code generation, where models must synthesize complete pro-
grams that correctly orchestrate a repository’s internal APIs to
accomplish a usage-oriented goal. To enable reliable evaluation,
we introduce RUCCE, a benchmark of realistic usage scenarios
curated from repositories, designed to systematically measure
LLMs’ capability for end-to-end repository usage.
• We propose RUCACoder, a multi-agent framework tailored
for repository-usage code generation. RUCACoder orchestrates
autonomous, iterative repository exploration and verification-
driven code synthesis. It generates canonical internal API invoca-
tion patterns to bridge the gap between complex internal APIs
and user intent, significantly reducing the learning curve for
developers unfamiliar with the codebase.
• We conduct comprehensive experiments on RUCCE. The results
show that RUCACoder consistently outperforms strong baselines
on both API retrieval and end-to-end executable code generation,
demonstrating its effectiveness for repository-usage tasks.
2
Related Work
2.1
Code Generation with LLMs
Large language models (LLMs) have demonstrated strong perfor-
mance in code generation, enabling developers to translate high-
level intent into functional code. Early models such as Codex [3]
and AlphaCode [20] demonstrated the effectiveness of large-scale
pretraining, followed by strong open-source code LLMs including
CodeGen [26], InCoder [7], StarCoder [18], and CodeLlama [29].
More recent models like DeepSeek-Coder [11] and Qwen3 [33]
narrow the gap with strong proprietary models (e.g., GPT-4 [1])
via repository-level training and improved architectures, while
reasoning-enhanced models such as DeepSeek-R1 [10] show that
reinforcement learning further improves complex programming
performance. Beyond stronger backbones, agent-based code gen-
eration integrates planning, retrieval, and feedback to iteratively
refine solutions. Tool-augmented reasoning methods such as Re-
Act [35] and Toolformer [30] motivate this paradigm, while sys-
tems like SWE-Agent [34] operationalize it for software engineer-
ing. Multi-agent frameworks (e.g., MetaGPT [14], ChatDev [27])
further demonstrate that decomposing the workflow across spe-
cialized agents can improve robustness and performance. Some
approaches also rely on graph/AST preprocessing or execution-
dependent pipelines [4, 12, 22, 23], which can be costly to deploy.
However, these methods are largely optimized for localized syn-
thesis or maintenance-centric objectives, and are not tailored to
repository-usage code generation, which requires identifying the cor-
rect internal APIs and generating complete, executable workflows
under repository-specific conventions and dependencies.
2.2
Code Generation Benchmarks
Early code generation benchmarks [2, 3] primarily target function-
level synthesis, evaluating standalone Python functions in isolated
settings. Datasets such as HumanEval [3] and MBPP [2] assume
3293

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation
SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
Figure 2: Benchmark construction pipeline: a four-stage process from candidate repository selection to execution verification,
functional annotation/API distillation, and difficulty stratification.
minimal external dependencies, while APPS [13] increases problem
complexity but largely remains in the paradigm of self-contained
algorithmic solving. In contrast, real-world development occurs in
repository-level environments with cross-file dependencies and
modular abstractions. To better reflect this reality, later benchmarks
move beyond isolated contexts: CoderEval [36] introduces non-
standalone settings, ClassEval [6] targets class-level generation,
and more recent suites such as DevEval [21], FEABench [19], and
SWE-bench [16] evaluate models at the repository scale.
Functional Instruction
[instruction] Functionality: I need to implement an asynchronous web
application using the aiohttp framework that serves HTTP requests and logs
access information.
Target API
[method_name] setup_tracing
[full_name] asgi_monitor.integrations.aiohttp.setup_tracing
[file_path] asgi-monitor/src/asgi_monitor/integrations/aiohttp.py
[method_code] def setup_tracing(app: Application, config: TracingConfig) ->
None: ...
Repository Information
[repo_name] draincoder/asgi-monitor  [commit_id] a3e3c2f7b8d...
Reference Implementation
[reference_solution] import asyncio
...
async def index(requests: Request) -> Response:
 
logger.info('Start sleeping at %s', datetime.now(tz=timezone.utc)) ...
Figure 3: Components of a RUCCE instance.
Despite this progress, most repository-level benchmarks remain
maintainer-centric, emphasizing bug fixing or feature implementa-
tion within the source tree (e.g., SWE-bench [16], FEA-bench [19]).
Moreover, Table 1 shows that existing benchmarks typically miss
at least one key dimension needed for practical repository usage:
many are not grounded in real repositories (e.g., HumanEval/MBPP),
others are not fully repository-level or do not provide comprehen-
sive instance-level annotations, and all lack a consumer perspective.
In contrast, RUCCE satisfies all criteria in Table 1: it is built from
real repositories and repository-level tasks, and each instance pro-
vides comprehensive annotations, supporting reliable evaluation of
consumer-side API discovery and orchestration.
3
The RUCCE Benchmark
RUCCE comprises 272 instances drawn from 54 real-world Python
repositories and is designed to systematically evaluate LLMs in
repository-usage code generation. As illustrated in Figure 3, each
instance includes four components: (1) Functional Instruction, which
provides a high-level description of the desired usage behavior, (2)
Target APIs, which identify the repository-internal APIs required
to realize the expected functionality and provide their signatures
and documentation, (3) Repository Information, which records the
Repo Name and Commit ID for reproducibility, and (4) Reference
Implementation, which provides a correct repository-usage code
solution that fulfills the instruction.
3.1
Benchmark Construction
We construct RUCCE from real-world GitHub repositories with an
explicit goal: each instance must be (i) runnable and deterministic,
(ii) grounded in repository-internal APIs, and (iii) faithful to a realistic
usage scenario. To meet these criteria, we distill tasks from canonical
example scripts using a four-stage pipeline with strict quality gates
at each stage, as shown in Figure 2.
Stage 1: Repo Filtering and Selection. We first curate candidate
Python repositories to reduce contamination risk and ensure practi-
cal relevance. Specifically, we select repositories created after 2023
with >50 stars, and require a dedicated examples/ directory. Ex-
ample scripts are a strong signal of intended repository usage: they
typically encode the maintainers’ canonical API orchestration pat-
terns, making them ideal seeds for consumer-side tasks. We further
exclude repositories whose examples are primarily tutorials for
external tools (i.e., where core logic is outside the repository) to
ensure the task depends on internal APIs.
Stage 2: Environment Deployment and Execution Verification. To
guarantee that every instance is executable, we manually deploy
each repository in an isolated environment and run candidate ex-
ample scripts end-to-end. We pin the repository version via Commit
ID, install dependencies, and execute the scripts with fixed config-
urations when applicable. We retain only scripts that (i) run suc-
cessfully without manual code edits, (ii) yield deterministic outputs
under repeated runs. This execution-first filtering removes broken
examples, underspecified setups, and non-reproducible behaviors.
3294

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
Kaitao Lin, Songwen Gong, Adam Jatowt, Jiexin Wang, and Yi Cai
Figure 4: System overview of RUCACoder: a closed-loop collaboration among the Retriever (repository exploration), the Verifier
(candidate reranking and solution validation), and the Coder (end-to-end script synthesis with iterative refinement).
Stage 3: Functional Annotation and API Distillation. For each veri-
fied script, we translate the code into a user-facing task specification
via a hybrid LLM+human process. We first prompt an LLM to draft
a high-level functional instruction that describes the script’s observ-
able behavior, leveraging both the code and its surrounding context
(e.g., docstrings and comments). Then, four software-engineering
students (two Ph.D., one M.S., one undergraduate) review and revise
all instructions to enforce: (i) behavioral fidelity (the instruction
matches the script’s runtime behavior), (ii) completeness (all key
steps and required inputs/outputs are covered), and (iii) clarity (the
instruction is unambiguous and executable as a coding prompt). In
parallel, we extract repository-internal API calls using jedi2 and
manually sanity-check the results, retaining only APIs that are es-
sential to realizing the target workflow. This stage yields structured
instances pairing natural-language intent with grounded internal
APIs and a verified reference solution.
Stage 4: Difficulty Stratification. To enable stratified evaluation
and diagnostic analysis, we label each instance as Easy/Medium/Hard
based on two complementary signals: the number of internal API
calls (dependency breadth) and cyclomatic complexity (logic depth).
Specifically, we normalize both signals to [0, 1] by dividing by their
dataset maxima, and compute an overall difficulty score by equal-
weight averaging:
Score = 0.5 · Norm_API + 0.5 · Norm_CC.
(1)
Finally, we apply quantile binning on Score (bottom/middle/top
33%) to assign Easy/Medium/Hard.
4
RUCACoder
In this section, we present RUCACoder, a multi-agent framework for
repository-usage code generation that coordinates three specialized
agents. In contrast to monolithic single-agent systems, RUCACoder
decomposes the workflow into: a Retriever that explores the repos-
itory to locate candidate internal APIs, a Verifier that assesses and
reranks candidates with multi-aspect validation, and a Coder that
2https://github.com/davidhalter/jedi
synthesizes an end-to-end executable script grounded in the veri-
fied APIs. These agents operate in a closed loop, where verification
feedback iteratively refines both retrieval and code synthesis until
a quality criterion or iteration budget is reached. Figure 4 provides
an overview of the RUCACoder workflow.
4.1
Retriever
The Retriever aims to identify relevant repository-internal APIs.
Developers typically navigate unfamiliar repositories in a coarse-
to-fine manner: they first locate likely entry files (e.g., examples,
modules, or API surfaces), then inspect signatures, docstrings, and
implementations to confirm suitability. We mirror this behavior by
combining iterative reasoning with hierarchical exploration tools,
allowing the Retriever to progressively narrow the search space
from repository-level structure to concrete functions and classes.
Concretely, the Retriever follows an iterative Thought–Action–
Observation loop: at each step, it analyzes the current state and
reasons about missing information (Thought), then selects and in-
vokes an exploration tool (Action), and processes the returned re-
sults to update its state (Observation). The loop terminates when
the agent executes a Finish action to submit candidates or reaches
a maximum step budget 𝑇. To control context length, the Retriever
keeps only the system prompt, the original instruction, and the most
recent 𝑘turns (𝑘= 3), while maintaining a persistent structured
state that stores visited files, inspected symbols, accepted/rejected
candidates, and tool-call history. This state prevents redundant
exploration and supports consistent decision making across turns.
To emulate human navigation in unfamiliar repositories and
prevent unnecessary code loading, we equip the Retriever with a
hierarchical tool suite. Search_Files retrieves a small set of rel-
evant files by matching the instruction against paths, docstrings,
and signature-level cues. Get_File_Details provides file sum-
maries and enumerates contained symbols with fully qualified
names, enabling rapid pruning without reading full implementa-
tions. Read_Code selectively loads implementations of promising
candidates for disambiguation, checking semantics, dependencies,
3295

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation
SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
and expected input/output behavior. Finally, Finish terminates
retrieval and submits the resulting candidates. This design reduces
both exploration cost and prompt length by deferring source load-
ing until it is necessary for validation.
The Retriever outputs a candidate API set 𝐴cand together with
grounding evidence, including fully qualified names, signatures/-
docstrings, and minimal source snippets (e.g., definitions and rep-
resentative call sites). This evidence is passed to the Verifier to
improve precision and to support downstream program synthesis.
4.2
Verifier
Retriever outputs may contain irrelevant or redundant APIs, increas-
ing noise and the risk of API misuse during generation. The Verifier
mitigates this via two-stage quality control: context refinement
before code generation and code verification after generation.
For context refinement, given 𝐴cand, the Verifier reranks can-
didates to form a compact toolkit 𝐴ranked. Each API is scored along
two axes: semantic match, which measures how well the API’s
functionality aligns with the instruction, and code relevance, which
measures whether the API is a canonical entry point supported
by strong repository evidence such as call sites or example usage.
The top-𝐾APIs (𝐾=10) constitute 𝐴ranked for the Coder, reducing
noise and improving context efficiency. For code verification, af-
ter the Coder produces a script 𝐶gen, the Verifier evaluates it along
three dimensions: API usage compliance checks that imports, fully
qualified names, and argument usage match the API signatures and
documentation; Logic correctness assesses whether the generated
workflow satisfies the instruction 𝑄and respects ordering and de-
pendency constraints implied by the repository; and Completeness
verifies that the script is runnable end-to-end and includes the re-
quired steps and a valid entry point. Each dimension is scored from
0 to 10, and the solution is accepted only if all scores exceed 7.
When verification fails, Verifier routes targeted feedback to the
appropriate component: Codegen_Error for API misuse or logical
flaws triggers Coder revision; Retrieve_Error when 𝐴ranked lacks
necessary functionality directs Retriever search refinement. This
yields a self-correcting loop that alternates between improving the
toolkit and improving the implementation.
4.3
Coder
The Coder synthesizes a complete, executable script from the user
instruction and the refined toolkit 𝐴ranked. To ensure repository-
native implementations, the Coder adheres to repository conven-
tions, such as using fully qualified import paths, leveraging internal
utilities, and structuring the code with a self-contained main() en-
try point. This synthesis is performed iteratively: the Coder drafts
an initial solution conditioned on 𝐴ranked and then revises it using
structured Verifier feedback (e.g., fixing import paths, argument
mismatches, or missing steps). The loop continues until the Verifier
accepts the script or a maximum iteration limit is reached.
5
Experiments and Results
5.1
Experimental Setup and Evaluation Metrics
In our setting, given a natural-language description of a usage
scenario and access to the repository, the model must generate a
complete, executable script. Solving this task requires discovering
relevant repository-internal APIs and composing them into an end-
to-end workflow that satisfies the specification. Accordingly, we
evaluate performance along two dimensions: API retrieval quality
and code generation quality.
For retrieval, we report Recall@k and Precision@k. Recall@k
measures the fraction of ground-truth APIs appearing in the top-k
results, which determines the upper bound of downstream genera-
tion success. Precision@k measures the fraction of retrieved APIs
that are relevant, that higher precision reduces context noise and
improves the generator’s efficiency under a fixed context length.
For code generation, we use two repository-aware metrics. API
Reuse Rate measures the proportion of valid repository-internal
API calls in the generated script relative to the reference, indicating
reliance on repository abstractions rather than redundant reimple-
mentation. RepoNativeScore uses an LLM-as-a-judge to assess
whether the solution follows a repo-native strategy that leverages
internal APIs and architectural abstractions, as opposed to a brute-
force strategy that reimplements existing logic. This metric rewards
outputs that align with the repository’s intended design. Concretely,
each generated solution is independently scored by three judge
models (DeepSeek-V3.2, GPT-4.1-mini, and GPT-4o-mini), and we
report the average score as the final RepoNativeScore.
Furthermore, we design experiments to answer three key re-
search questions: (RQ1) how effective is our API retrieval compared
to baselines; (RQ2) how retrieval quality translates to downstream
code generation; and (RQ3) how effective is the Verifier in improv-
ing retrieval precision and downstream repo-native generation.
We evaluate three backbone LLMs: DeepSeek-V3.2 [5], Gemini-2.5-
flash [31], and GPT-5-mini [1].
5.2
RQ1: API Retrieval Experiment
We evaluate API retrieval on RUCCE by comparing RUCACoder
with three baselines. BM25 [28] is a sparse lexical retriever index-
ing APIs by signatures and summaries. UniXcoder [9] is a dense
retriever using FAISS nearest-neighbor search. AllianceCoder [8]
is a repository-level generation baseline with retrieval-augmented
generation. Results are shown in Table 2.
Overall, RUCACoder achieves the strongest performance across
all difficulty subsets and cutoffs. With DeepSeek-V3.2, it improves
Easy Recall@1 to 33.3 (vs. 24.2/14.8/2.8) and scales to 64.4 Recall@10
(vs. 44.1/41.8/17.9). Gains are even clearer on harder splits: on
Medium, RUCACoder reaches 15.8 Recall@1 and 57.4 Recall@10,
substantially above BM25 (6.1/23.2) and UniXcoder (4.2/28.5); on
Hard, it attains 7.4 Recall@1 and 42.0 Recall@10, again exceeding
BM25 (4.2/16.5) and UniXcoder (3.9/20.3). Precision follows the
same pattern: for DeepSeek-V3.2, RUCACoder improves Easy Preci-
sion@1 to 50.5 (vs. 29.7/19.8/4.4) and maintains high Precision@10
at 22.4 (vs. 6.6/6.4/3.1), indicating that the retrieved contexts are
not only broader but also substantially cleaner. RUCACoder also
remains strong under other backbones, suggesting retrieval quality
is robust to the underlying LLM. For instance, on Hard, it achieves
Recall@10 of 36.2 with Gemini-2.5-flash and 39.4 with GPT-5-mini,
while maintaining high Precision@1 (60.7 and 55.1). In contrast, Al-
lianceCoder remains weak even when paired with DeepSeek-V3.2,
implying that the gains are driven by our agentic retrieval design
rather than backbone strength.
3296

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
Kaitao Lin, Songwen Gong, Adam Jatowt, Jiexin Wang, and Yi Cai
Method
Backbone
Easy
Medium
Hard
Recall
Precision
Recall
Precision
Recall
Precision
@1 @3 @5 @10 @1 @3 @5 @10 @1 @3 @5 @10 @1 @3 @5 @10 @1 @3 @5 @10 @1 @3 @5 @10
BM25
—
24.2 36.3 37.5 44.1 29.7 16.1 10.3 6.6
6.1 13.4 15.0 23.2 17.4 13.8 10.0 8.3 4.2 10.1 13.9 16.5 37.1 27.7 23.1 14.6
UniXcoder
—
14.8 29.1 34.6 41.8 19.8 13.6 10.3 6.4
4.2 12.2 19.8 28.5 15.2 14.1 14.6 10.7 3.9 7.9 11.7 20.3 34.8 21.7 19.6 16.7
AllianceCoder DeepSeek-V3.2
2.8
4.8 10.1 17.9 4.4
2.6
3.3
3.1
1.3
2.7
5.1
8.7
5.4
3.6
3.9
3.4 0.6 2.7
4.0
8.4
5.6
7.1
6.7
6.5
RUCACoder DeepSeek-V3.2
33.3 53.7 58.8 64.4 50.5 33.5 27.1 22.4 15.8 35.7 46.2 57.4 55.4 44.2 35.5 25.9 7.4 24.2 32.4 42.0 56.2 54.7 47.0 34.4
Gemini-2.5-flash 28.5 38.7 41.8 42.9 42.9 31.9 28.6 26.5 13.8 35.1 44.4 47.1 49.5 45.4 37.4 30.5 8.3 20.7 27.5 36.2 60.7 53.6 45.9 36.2
GPT-5-mini
29.8 43.2 47.0 51.7 46.2 27.3 21.0 16.8 13.3 31.6 42.4 48.7 47.8 41.1 33.6 22.0 8.7 19.4 29.0 39.4 55.1 48.7 44.5 32.5
Table 2: API retrieval performance (%) across three difficulty levels, with backbone model specification.
Setting
DeepSeek-V3.2
Gemini-2.5-flash
GPT-5-mini
Easy
Medium
Hard
Easy
Medium
Hard
Easy
Medium
Hard
Score Reuse Score Reuse Score Reuse Score Reuse Score Reuse Score Reuse Score Reuse Score Reuse Score Reuse
Nocontext
0.167
—
0.185
—
0.186
—
0.156
—
0.188
—
0.183
—
0.153
—
0.187
—
0.165
—
Unixcoder
0.529
0.377
0.516
0.268
0.469
0.225
0.506
0.345
0.524
0.241
0.463
0.203
0.490
0.363
0.432
0.209
0.407
0.194
BM25
0.462
0.317
0.504
0.248
0.469
0.172
0.502
0.348
0.435
0.199
0.351
0.162
0.432
0.312
0.391
0.210
0.356
0.151
AllianceCoder 0.414
0.305
0.394
0.139
0.346
0.115
0.414
0.305
0.394
0.139
0.346
0.115
0.414
0.305
0.394
0.139
0.346
0.115
GT
0.701 0.634 0.689 0.577 0.607 0.507 0.699 0.654 0.706 0.541 0.648 0.511 0.600 0.566 0.617 0.494 0.571 0.458
RUCACoder
0.587
0.446
0.604
0.359
0.519
0.291
0.499
0.310
0.537
0.293
0.499
0.227
0.549
0.360
0.490
0.310
0.481
0.239
Table 3: Code generation performance across three backbones and difficulty levels. Score denotes RepoNativeScore, and Reuse
denotes API Reuse Rate. Underlined indicates the second-best model results.
Setting
Easy
Medium
Hard
Retrieval Generation Retrieval Generation Retrieval Generation
R@3 P@3 Reuse Score R@3 P@3 Reuse Score R@3 P@3 Reuse Score
w/o Verifier 46.3
28.8
40.3
55.5
30.7
37.0
35.7
59.2
19.8
46.1
30.2
52.8
Full Model 53.7 33.5
44.6
58.7
35.7 44.2
35.9
60.4
24.2 54.7
29.1
51.9
Table 4: Verifier Ablation study results.
These improvements stem from RUCACoder’s iterative, hierar-
chical exploration. It progressively narrows the search space from
file-level signals to symbol-level evidence, and selectively verifies
candidates via lightweight code inspection. This coarse-to-fine pro-
cess improves coverage while reducing false positives, yielding
stronger retrieval under a fixed context length.
5.3
RQ2: Code Generation Experiment
To assess how retrieval quality impacts downstream code genera-
tion, we evaluate several prompting. NoContext uses the instruc-
tion. BM25, UniXcoder, and AllianceCoder add their top re-
trieved APIs as context. RUCACoder uses our full pipeline with
exploration, reranking, and verification-guided refinement. GT sup-
plies ground-truth APIs as an approximate upper bound. All meth-
ods share the same backbone LLM. Results are reported in Table 3.
Except for GT, RUCACoder achieves the best performance across
all backbones and difficulty levels. With DeepSeek-V3.2 on Easy,
it attains 0.587 Score and 0.446 Reuse, outperforming UniXcoder
(0.529/0.377), BM25 (0.462/0.317), and AllianceCoder (0.414/0.305).
The gap widens on Hard: RUCACoder reaches 0.519 Score and 0.291
Reuse, while all baselines remain below 0.469 Score and 0.225 Reuse.
Similar trends hold for Gemini-2.5-flash and GPT-5-mini, indicating
that our iterative retrieval+verification loop consistently improves
repo-native API orchestration and end-to-end script quality.
Notably, even with access to ground-truth APIs, GT achieves
only 0.607 Score on Hard and averages around 0.66 across difficulty
levels. This suggests that correct APIs are necessary but not suffi-
cient: current LLMs often struggle to understand repository-specific
abstractions and compose long, constraint-heavy API chains into
coherent executable programs. Beyond improving retrieval accu-
racy, enhancing context utilization remains a key challenge for
repository-usage code generation.
5.4
RQ3: Verifier Ablation Study
To isolate the Verifier’s impact on retrieval and downstream gen-
eration, we conduct an ablation study using DeepSeek-V3.2 as the
backbone LLM. We compare the Full Model against w/o Verifier,
which removes candidate reranking and post-generation validation
and passes the Retriever outputs directly to the Coder.
Table 4 shows that the Verifier consistently improves retrieval
quality. On Easy, R@3/P@3 rises from 46.3/28.8 to 53.7/33.5; on
Medium, from 30.7/37.0 to 35.8/44.2; and on Hard, from 19.8/46.1
3297

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation
SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
to 24.2/54.7. These gains generally translate into stronger repo-
native generation on Easy/Medium, improving Reuse from 40.3
to 44.6 and from 35.7 to 35.9, and increasing Score from 55.5 to
58.7 and from 59.2 to 60.4. On Hard, we observe a slight drop in
generation metrics despite better retrieval, likely because these
instances demand stronger long-horizon orchestration to compose
lengthy API chains into coherent, executable workflows.
6
Conclusion
In this paper, we study repository-usage code generation, where
models must discover repository-internal APIs and synthesize com-
plete, executable workflows that follow repository conventions. To
enable systematic evaluation of this setting, we introduce RUCCE,
a benchmark curated from real-world Python repositories with
grounded target APIs and verified reference implementations. We
further propose RUCACoder, a closed-loop multi-agent framework
that integrates hierarchical repository exploration, verifier-guided
reranking, and iterative refinement to improve both API selection
and repo-native code synthesis. Experiments show clear gains over
strong retrieval and generation baselines, while harder instances
reveal a key challenge: composing long API chains and effectively
utilizing retrieved context to produce coherent end-to-end pro-
grams. We hope RUCCE and RUCACoder will advance practical,
user-centric repository assistance.
Acknowledgement
This research is supported by the Science and Technology Planning
Project of Guangdong Province (2025B0101120003), the Guangdong
Provincial Fund for Basic and Applied Basic Research—Regional
Joint Fund Project (Key Project) (2023B1515120078), National Natu-
ral Science Foundation of China (62402185, 62476097), Guangdong
Provincial Natural Science Foundation for Outstanding Youth Team
Project (2024B1515040010), the Fundamental Research Funds for
the Central Universities, South China University of Technology
(x2rjD2250190).
References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Floren-
cia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal
Anadkat, et al. 2023. Gpt-4 technical report.
[2] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk
Michalewski, et al. 2021. Program synthesis with large language models.
[3] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde
De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, et al. 2021. Evaluating large language models trained on code.
[4] Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang,
Viktor Prasanna, Arman Cohan, and Xingyao Wang. 2025. Locagent: Graph-
guided llm agents for code localization. 8697–8727 pages.
[5] DeepSeek-AI. 2025. DeepSeek-V3.2: Pushing the Frontier of Open Large Language
Models. https://arxiv.org/abs/2512.02556
[6] Xueying Du, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, et al. 2023.
Classeval: A manually-crafted benchmark for evaluating llms on class-level code
generation.
[7] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi,
Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2022. Incoder: A
generative model for code infilling and synthesis.
[8] Wenchao Gu, Juntao Chen, Yanlin Wang, Tianyue Jiang, Xingzhe Li, Mingwei
Liu, Xilin Liu, Yuchi Ma, and Zibin Zheng. 2025. What to Retrieve for Effective
Retrieval-Augmented Code Generation? An Empirical Study and Beyond.
[9] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. 2022.
Unixcoder: Unified cross-modal pre-training for code representation.
[10] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin
Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. 2025. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement learning.
[11] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang,
Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. 2024. DeepSeek-Coder: When the
Large Language Model Meets Programming–The Rise of Code Intelligence.
[12] Nam Le Hai, Dung Manh Nguyen, and Nghi D. Q. Bui. 2025. On the Impacts of
Contexts on Repository-Level Code Generation. 1496–1524 pages. doi:10.18653/
v1/2025.findings-naacl.82
[13] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora,
Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. 2021.
Measuring coding challenge competence with apps.
[14] Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng,
Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, et al.
2023. MetaGPT: Meta programming for a multi-agent collaborative framework.
[15] Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc
Brockschmidt. 2019. Codesearchnet challenge: Evaluating the state of semantic
code search.
[16] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir
Press, and Karthik Narasimhan. 2023. Swe-bench: Can language models resolve
real-world github issues?
[17] Harshit Joshi, José Cambronero Sanchez, Sumit Gulwani, Vu Le, Gust Verbruggen,
and Ivan Radiček. 2023. Repair is nearly generation: Multilingual program repair
with llms. 5131–5140 pages.
[18] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov,
Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. 2023.
Starcoder: may the source be with you!
[19] Wei Li, Xin Zhang, Zhongxin Guo, Shaoguang Mao, Wen Luo, Guangyue Peng,
Yangyu Huang, Houfeng Wang, and Scarlett Li. 2025. Fea-bench: A benchmark
for evaluating repository-level code generation for feature implementation.
[20] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi
Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022.
Competition-level code generation with alphacode. 1092–1097 pages.
[21] Yibing Li, Yuxiang Wang, Peng Ding, Shaohua Li, et al. 2024. DevEval: A Manually-
Annotated Code Generation Benchmark Aligning with Real-World Developmen-
tal Requirements.
[22] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and
Qianxiang Wang. 2024. Graphcoder: Enhancing repository-level code completion
via coarse-to-fine retrieval based on code context graph. 570–581 pages.
[23] Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang,
Michael Qizhe Shieh, and Wenmeng Zhou. 2025. Codexgraph: Bridging large
language models and code repositories via code graph databases. 142–160 pages.
[24] Stephen MacNeil, Andrew Tran, Arto Hellas, Joanne Kim, Sami Sarsa, Paul
Denny, Seth Bernstein, and Juho Leinonen. 2023. Experiences from using code
explanations generated by large language models in a web software development
e-book. 931–937 pages.
[25] Stephen MacNeil, Andrew Tran, Dan Mogil, Seth Bernstein, Erin Ross, and Ziheng
Huang. 2022. Generating diverse code explanations using the gpt-3 large language
model. 37–39 pages.
[26] Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou,
Silvio Savarese, and Caiming Xiong. 2022. Codegen: An open large language
model for code with multi-turn program synthesis.
[27] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng
Yang, Weize Chen, Yusheng Su, Xin Cong, et al. 2024. Chatdev: Communicative
agents for software development. 15174–15186 pages.
[28] Stephen Robertson, Hugo Zaragoza, et al. 2009. The probabilistic relevance
framework: BM25 and beyond. 333–389 pages.
[29] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiao-
qing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, et al. 2023.
Code llama: Open foundation models for code.
[30] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli,
Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023.
Toolformer: Language models can teach themselves to use tools.
68539–
68551 pages.
[31] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu,
Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al.
2023. Gemini: a family of highly capable multimodal models.
[32] Chunqiu Steven Xia and Lingming Zhang. 2022. Less training, more repair-
ing please: revisiting automated program repair via zero-shot learning. 959–
971 pages.
[33] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. 2025. Qwen3 technical
report.
[34] John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik
Narasimhan, and Ofir Press. 2024. Swe-agent: Agent-computer interfaces enable
automated software engineering. 50528–50652 pages.
[35] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan,
and Yuan Cao. 2022. React: Synergizing reasoning and acting in language models.
3298

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

SIGIR ’26, July 20–24, 2026, Melbourne, VIC, Australia
Kaitao Lin, Songwen Gong, Adam Jatowt, Jiexin Wang, and Yi Cai
[36] Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang,
Ying Li, Qianxiang Wang, and Tao Xie. 2024. Codereval: A benchmark of prag-
matic code generation with generative pre-trained models. 12 pages.
[37] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi
Mao, Jian-Guang Lou, and Weizhu Chen. 2023. Repocoder: Repository-level code
completion through iterative retrieval and generation.
3299

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/Beyond%20Maintenance/page-08.png)
