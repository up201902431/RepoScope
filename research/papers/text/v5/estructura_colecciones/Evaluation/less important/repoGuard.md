# RepoGuard: Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation

- source_pdf: ../../../../../pdf/Evaluation/less%20important/repoGuard.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RepoGuard: Harmonising Security and Functional Correctness in
LLM-Guided Repository-Level Code Generation
Cassiano Darif Zago∗
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
cassianodz@gmail.com
Fábio Lúcio Lopes de Mendonça
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
fabio.mendonca@redes.unb.br
Georges D. Amvame Nze
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
georges@unb.br
João José Costa Gondim
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
gondim@unb.br
Robson De Oliveira
Albuquerque
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
robson@redes.unb.br
Jorge Osvaldo A. Lima Torres
Department of Electrical Engineering
University of Brasília
Brasília, DF, Brazil
jorge.torres@redes.unb.br
Abstract
The rapid adoption of Large Language Models (LLMs) for code
generation has significantly enhanced developer productivity while
simultaneously increasing the risk of introducing insecure or func-
tionally incorrect code into software repositories. This paper presents
RepoGuard-Agent, an orchestration architecture that integrates
LLM-driven repair with deterministic program analysis to auto-
matically generate safer, compilable patches for vulnerable code.
RepoGuard combines context retrieval (via AST-based repository
analysis), prompt-engineered LLM correction, an Auto-Importer
post-processor, and a hybrid validation oracle comprising ensemble
Static Application Security Testing (SAST) scanners and dynamic
unit tests. The proposed pipeline prioritises in-context learning and
agent orchestration over resource-intensive fine-tuning, thereby
reducing infrastructure overhead while maintaining practical ro-
bustness. Evaluation on a synthetic multi-CWE script demonstrates
that RepoGuard converges to a safer, functionally correct solution
within Recursive Criticism and Improvement (RCI) iterations, suc-
cessfully mitigating security vulnerabilities without compromising
functionality. Results highlight the critical role of AST-based import
repair and ensemble validation in addressing LLM scope myopia
and static analyser noise. Finally, limitations, human-in-the-loop
policies, and integration pathways for CI/CD deployment are dis-
cussed.
CCS Concepts
• Software and its engineering →Automatic programming; •
Security and privacy →Software and application security; •
Computing methodologies →Artificial intelligence.
∗Corresponding author.
This work is licensed under a Creative Commons Attribution 4.0 International License.
ICICT 2026, Honolulu, HI, USA
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2252-3/26/03
https://doi.org/10.1145/3803291.3803376
Keywords
Large Language Models, Code Generation, Static Analysis, Auto-
mated Repair, Software Security, RCI
ACM Reference Format:
Cassiano Darif Zago, Fábio Lúcio Lopes de Mendonça, Georges D. Amvame
Nze, João José Costa Gondim, Robson De Oliveira Albuquerque, and Jorge
Osvaldo A. Lima Torres. 2026. RepoGuard: Harmonising Security and Func-
tional Correctness in LLM-Guided Repository-Level Code Generation. In
2026 The 9th International Conference on Information and Computer Technolo-
gies (ICICT 2026), March 11–13, 2026, Honolulu, HI, USA. ACM, New York,
NY, USA, 9 pages. https://doi.org/10.1145/3803291.3803376
1
Introduction
Recent advances in code-focused language modelling have trans-
formed software development workflows by automating tasks that
traditionally used to require intensive manual review. However,
the application of LLMs to code generation and repair introduces a
significant practical challenge: models capable of producing syn-
tactically correct code frequently generate insecure, incomplete, or
non-executable fragments within the context of real-world reposito-
ries. This phenomenon, termed “scope myopia”, reflects a tendency
to prioritise local logic while disregarding global dependencies and
boilerplate requirements, resulting in failures, regressions, and a
false sense of security when rigorous validation is absent.
In the domain of AI-assisted software security, numerous re-
search efforts have sought to mitigate these risks. Approaches re-
lying solely on prompt engineering, specialised benchmarks, or
fine-tuning continue to face difficulties in generalising to repository-
level contexts and in simultaneously preserving both security and
functionality. Moreover, traditional static analysers generate ex-
cessive noise (false positives), which, when directly fed back to an
LLM, can induce unproductive correction loops. Consequently, a
design that integrates the creativity and adaptability of probabilis-
tic models with deterministic checks ensuring compilability and
expected behaviour is required.
Addressing this landscape, we propose RepoGuard-Agent, whose
central hypothesis is that the combination of (i) AST-based context
retrieval, (ii) security-persona-guided prompt engineering, (iii) syn-
tactic post-processing (Auto-Importer), and (iv) hybrid validation
378

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Zago et al.
(ensemble SAST + test execution) enables the generation of patches
that are simultaneously safer and functional without requiring
model retraining. The agent operates in Recursive Criticism and
Improvement (RCI) cycles, receiving structured feedback from the
validation stage and iteratively refining corrections until security
metrics and unit tests are satisfied or an iteration limit is reached.
The primary objectives and contributions of this work are:
• To design and implement an orchestration architecture (RepoGuard-
Agent) integrating LLMs, AST analysis, and hybrid validation
for the automatic repair of insecure code;
• To introduce the Auto-Importer module, an AST-based post-
processor that surgically detects and inserts missing imports,
eliminating common LLM scope errors;
• To demonstrate, through a controlled case study, that the
proposed combination rapidly converges (two RCI iterations
in the experiment) to safer solutions while preserving func-
tional correctness;
• To discuss false-positive filtering strategies, human-in-the-
loop policies, and pathways for integration into CI/CD pipelines.
The remainder of the paper is organised as follows. Section 2 re-
views related work and positions the proposal relative to recent
benchmarks and techniques. Section 3 details the RepoGuard archi-
tecture, its components, and the RCI workflow. Section 4 presents
the experimental design and results. Finally, Section 5 concludes
with lessons learned, limitations, and future directions.
2
Related Work
Growing concerns regarding the security of code generated by
Large Language Models (LLMs) have spurred a range of innovative
approaches. The CodeSpeak framework [4] enhances vulnerability
detection in smart contracts by combining LLM code comprehen-
sion with structured prompt engineering. Its four-phase methodol-
ogy—data preparation to remove redundancies, LLM-assisted code
analysis using audit-mimicking instructions, knowledge integration
via structured prompt templates, and prompt tuning—outperformed
Graph Neural Network-based approaches and traditional static tools
(e.g., Mythril and Slither) in precision and recall for vulnerabilities
such as Reentrancy and Timestamp dependence, while reducing
detection time by 98.7% relative to manual analysis. Limitations
include dependence on prompt quality and the computational cost
of commercial APIs.
Complementarily, Tony et al. [20] proposed a pipeline employing
Genetic Algorithms with two novel LLM-assisted security-focused
mutation techniques—self-guided and feedback-guided—combined
with generic methods such as back-translation. This approach sub-
stantially reduced security weaknesses in Python code generated
by models including GPT-4 and DeepSeek-Coder, outperforming
manual prompts and generic optimisations, though prompt trans-
ferability across models remained low.
In cybersecurity rule evaluation, Bertiger et al. [1] developed a
holdout-set-validated benchmarking framework comparing rules
generated by the ADÉ system against human-crafted rules from
the Sublime Security Core Feed, achieving syntactically correct and
effective rules after iterative refinement while quantifying the cost
of failed attempts. Challenges persist in measuring production false
negatives and addressing human-machine comparison asymmetry.
Meanwhile, GRASP [14] introduced structured reasoning over
Secure Coding Practices via a directed acyclic graph to guide LLMs
systematically, attaining security rates above 80% on GPT-4o and
Claude with strong generalisation to zero-day vulnerabilities, though
smaller models such as Phi-2 struggled with complex graph reason-
ing.
A large-scale perspective is offered by the FormAI-v2 dataset [18],
comprising 331,000 C programs generated by nine LLMs and for-
mally verified with ESBMC, revealing that at least 62.07% are vul-
nerable (particularly to buffer overflows and pointer dereferencing),
even in lower-cyclomatic-complexity models such as GPT-4o-mini,
with limitations confined to C and verifier coverage.
Taeb et al. [17] compared CodeX, CodeBERT, and GPT-3.5 in
an educational context, concluding that CodeX produced the most
secure and accurate code, GPT-3.5 excelled at vulnerability expla-
nation, and CodeBERT performed worst on security, though the
study was limited to isolated snippets and suffers from rapid model
obsolescence.
Charalambous et al. [5] explored automated repair of C neural
network implementations using LLMs guided by formal verifica-
tion with ESBMC and an expanded NeuroCodeBench, finding that
providing only the vulnerable line or specific personas significantly
improved compilable patch rates, albeit with single-attempt success
below 18%, necessitating costly iterations.
Bruni et al. [3] developed an automated benchmark and Prompt
Agent demonstrating that simple security prefixes reduce vulnera-
bilities by up to 56% in GPT-4o and that Recursive Criticism and
Improvement (RCI) repairs 41.9%–68.7% of failures, despite reliance
solely on static scanners.
Keltek et al. [12] presented LSAST, combining conservative SAST
scanners with local Llama-3 and HackerOne-sourced RAG, outper-
forming traditional tools on real critical vulnerabilities and showing
that feeding SAST results to the LLM markedly enhances novel
flaw discovery, though poorly calibrated RAG can introduce noise.
In HIPAA-compliant secure chatbot construction, Salyers et
al. [15] described Be Well Buddy, employing closed-domain ar-
chitecture, SHA-256 encryption, IP whitelisting, and IBM Watson
solely for intent classification, achieving over 99% accuracy and
validating data transfer security in beta testing, albeit with small
sample size and short duration.
For holistic security evaluation, Bhatt et al. [2] introduced CY-
BERSECEVAL, assessing both LLM propensity to generate insecure
code (covering 50 CWEs across eight languages) and compliance in
assisting cyberattacks, revealing paradoxically higher vulnerability
rates (average 30%) and offensive assistance compliance ( 53%) in
higher-capability coding models.
Similarly, Wang et al. [21] proposed CodeSecEval, targeting
both secure code generation and insecure code repair, finding that
vulnerability-aware problem descriptions and explicit insecure code
explanations significantly improve performance, though self-repair
capability varies widely by vulnerability type.
However, the effectiveness of secure generation techniques is
questioned by Dai, Xu, and Tao [10], who criticise independent
evaluation of security and functionality. Introducing the unified
SAFE metric and multiple static scanners (CodeQL, Bearer, Bandit),
they showed that current techniques such as SVEN and CodeGuard+
379

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

RepoGuard: Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation
ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
often sacrifice functionality (e.g., removing essential logic) to appear
more secure and that CodeQL misses over 20% of real vulnerabilities.
Transitioning from isolated snippets to repository level intro-
duces new challenges. Dilgren et al. [11] launched SECREPOBENCH,
demonstrating that LLM performance on isolated-function bench-
marks (e.g., SecCodePLT) does not translate to real C/C++ reposito-
ries, where prompt engineering effective in isolation loses efficacy,
and models struggle to produce simultaneously compilable, correct,
and secure code.
Corroborating repository-level difficulties, Chen et al. [6] pre-
sented SecureAgentBench for evaluating coding agents (e.g., SWE-
agent, OpenHands), reporting alarmingly low rates (best agents
achieving only 15.2% correct and secure solutions) and frequent in-
troduction of novel vulnerabilities, suggesting that simple security
instructions are insufficient for multi-file editing contexts.
Investigating specific prompting techniques, Tony et al. [19]
systematically examined Recursive Criticism and Improvement
(RCI) and Chain-of-Thought, finding RCI particularly effective at
reducing vulnerability density in Python and C code generated by
models such as GPT-4, outperforming few-shot approaches and
underscoring the value of self-reflection mechanisms.
In high-specificity domains, Councilman et al. [8] addressed cor-
rectness assurance in LLM-generated Ansible scripts via Astrogator,
using formal query language and symbolic state calculation to for-
mally prove correctness in 83% of cases and identify incorrect code
in 92%, mitigating natural language ambiguity in system configura-
tion tasks.
Also domain-specific, Malamas et al. [13] explored “vibe coding”
through the DSL Agent, a conversational interface for domain-
specific languages integrated into the low-code Locsys platform,
demonstrating that dynamic in-context learning generates valid
DSL models with greater accuracy and efficiency than novice de-
velopers while preserving structural integrity.
In offensive security, Shao et al. [16] developed the NYU CTF
Bench to evaluate LLM performance on Capture the Flag challenges,
revealing severe limitations in open-source models and consistent
failures in multi-step reasoning and external tool use, despite pro-
prietary models solving 50% of specific categories.
Finally, the human dimension is examined by De La Cruz et
al. [9], who qualitatively explored the redefinition of programmer
roles in the AI era, noting persistent anxiety over the “illusion of
confidence” trap wherein syntactically perfect but logically insecure
LLM-generated code may evade detection due to automation bias,
necessitating renewed emphasis on ethical oversight and security
validation.
Table 1 positions RepoGuard-Agent relative to related work, illus-
trating how the solution addresses critical gaps in automation and
context through its hybrid validation approach. The satisfaction of
marked criteria is detailed below:
• Focus on Generation and Repair: The solution extends
beyond mere vulnerability detection. Its core employs LLMs.
In this case, qwen2.5-coder, to actively rewrite insecure
code segments, delivering ready-to-apply patches rather
than alerts alone.
• Prompt Engineering: Rather than relying on costly fine-
tuning, the system leverages advanced in-context learning
strategies, employing structured prompts with defined per-
sonas (“SRE Security Specialist”), explicit negative constraints
(e.g., prohibition of eval), and dynamic injection of AST-
extracted context.
• Use of Agents: The RepoGuardEngine functions as an au-
tonomous agent orchestrating external tools (scanners, in-
terpreters, filesystem). It makes control-flow decisions—such
as persisting with correction, reverting changes, or abort-
ing—based on environmental feedback, without per-iteration
human intervention.
• Repository Level: Through the FileSystemContext and Auto-
Importer modules, the agent overcomes the local-vision lim-
itation common in LLMs. It analyses global dependencies
and injects required imports based on project structure, en-
suring overall software integrity and preventing reference
errors (NameError). This mitigates frequent LLM failures
involving missing imports, duplicated declarations, and hal-
lucinations. Context is further enhanced using os.walk() to
identify related project files and ast parsing to optimise con-
text utilisation for comprehensive prompt injection.
• Hybrid Validation (SAST + Dynamic): The proposal avoids
blind trust in model output by implementing a validation
oracle combining rigorous static analysis (ensemble of Ban-
dit and PyASTScanner) with dynamic unit test execution
(unittest). Code is accepted only if simultaneously safer
and functional.
• Human Evaluation: The tool adopts a human-in-the-loop
philosophy. Although repair is automated, final patch ap-
plication is submitted to an interactive CLI interface where
developers review the proposed diff, ensuring human over-
sight of critical changes.
Notably, unlike works focused on new datasets or model retraining,
this proposal emphasises orchestration architecture. The deliber-
ate avoidance of fine-tuning demonstrates that a robust validation
and context-retrieval pipeline suffices for high-quality repairs using
generic open-source code models, thereby reducing computational
cost and facilitating local deployment.
3
Proposed Solution: RepoGuard
To address the limitations identified in the literature, specially the
challenge of preserving functional correctness while repairing vul-
nerabilities and the models’ blindness to repository context, we
developed RepoGuard.
The implementation employs a modular architecture based on
dependency injection to facilitate component substitution. At its
core is an iterative refinement engine (RCI Loop) orchestrating
interactions among Static Application Security Testing (SAST) tools,
unit tests, and local Large Language Models.
Figure 1 provides an overview of the implemented architecture.
The detailed operation of the developed components is described
below.
3.1
Context Retrieval and AST Parsing
Unlike purely text-based approaches, the FileSystemContext module
employs Python’s native ast library to perform syntactic parsing
of adjacent repository files, extracting function signatures, class
380

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Zago et al.
Table 1: Comparison of approaches and contributions in related work.
Work
Focus on
Generation
Focus on
Detection/Repair
Proposes New
Benchmark
Prompt
Engineering
Fine-Tuning
Use of
Agents
Repository
Level
Static
Analysis (SAST)
Formal/Dynamic
Verification
Human
Evaluation
[4]
√
√
√
[20]
√
√
[1]
√
√
[14]
√
√
[18]
√
√
√
[17]
√
√
[5]
√
√
√
[3]
√
√
√
√
√
√
[12]
√
√
[15]
√
√
[8]
√
√
√
√
[19]
√
√
√
[2]
√
√
√
[21]
√
√
√
√
[10]
√
√
√
√
√
[11]
√
√
√
√
[6]
√
√
√
√
√
√
[13]
√
√
√
√
√
[16]
√
√
√
√
√
[9]
√
Proposed Solution
√
√
√
√
√
√
√
√
definitions, and global imports. This context is injected into the
system prompt, enabling the model to reference external defini-
tions without exceeding the LLM context window and mitigating
hallucinations regarding non-existent functions.
3.2
Correction Agent and Syntactic Refinement
(Auto-Importer)
The OllamaFixer component is architected for fully offline, privacy-
preserving operation, eliminating the need for external APIs or data
transmission. It utilises the qwen2.5-coder:7b model, selected for
its state-of-the-art performance in coding tasks among parameter-
efficient models. To demonstrate the accessibility and resource
efficiency of the proposed architecture, all inference tasks were
executed in a CPU-only environment (without CUDA acceleration)
on a standard workstation equipped with an AMD Ryzen 7 5800XT
processor and 64GB of RAM. This configuration underscores that
robust automated repair is achievable on commodity hardware,
reducing the barrier to entry for local deployment. The prompt
381

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

RepoGuard: Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation
ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Vulnerable
Code + Tests
1. Context Re-
trieval (AST
Analysis)
2. LLM Fixer
+ Auto-Import
3. Hybrid Valida-
tion (Ensemble
SAST + Unittest)
Approved?
Safer Code
Feedback
Loop
Yes
No
Figure 1: Iterative refinement (RCI) workflow of RepoGuard
with syntactic post-processing.
engineering strategy incorporates specific personas (“SRE Security
Specialist”) and strict constraint rules to prevent the reintroduction
of common vulnerabilities, such as eval() or pickle.
A significant technical challenge observed during development
was the LLM’s tendency to generate syntactically incomplete snip-
pets, frequently omitting import statements (e.g., using List or
Optional without importing typing), or ignoring semantically
distinct structures and entities. This arises from the probabilistic
nature of Transformer attention mechanisms, which prioritise local
token probabilities during vulnerability-focused correction while
neglecting global file scope and header dependencies. Many train-
ing datasets comprising isolated functions further reinforce this
bias toward omitting necessary boilerplate [11].
To address this deterministically, we implemented the Auto-
Importer module as an AST-based linter post-processor:
(1) The LLM-generated code is parsed into an AST.
(2) An AST traversal algorithm identifies Name nodes with load
context representing used variables or types.
(3) Orphaned symbols are checked against a hash table of safe
standard libraries (e.g., typing, json, os).
(4) Missing imports are surgically injected at the file top.
This hybrid approach combines the LLM’s semantic creativity (for
logic correction) with AST rigor (for compilation assurance), almost
eliminating all NameError issues prior to testing.
3.3
Hybrid Validation and Noise Filtering
Security validation employs ensemble scanning combining:
• Custom PyASTScanner: A syntactic analyser developed for
this work that deterministically detects prohibited patterns
(e.g., os.system or pickle.loads calls).
• Bandit SAST: An industry-standard Python security tool.
A critical challenge overcome was false-positive handling. Static
tools generate excessive noise, potentially trapping the LLM in
stagnation loops. For instance, Bandit flags B404 (subprocess secu-
rity implication) on mere import, even when used correctly. The
RepoGuardEngine implements intelligent filtering that ignores infor-
mational codes (B404, B603) when deep PyASTScanner analysis con-
firms best-practice implementation (e.g., list-based subprocess.run),
breaking negative feedback cycles.
The rationale for this ensemble architecture aligns with the
Condorcet Jury Theorem [7]. The theorem demonstrates that
for a group of independent voters, each with a competence 𝑝> 0.5,
the probability of a correct majority decision approaches certainty
as the number of voters increases. By aggregating outputs from
disparate scanning tools, the system leverages this probabilistic
convergence to maximise detection accuracy.
3.4
RCI Cycle (Recursive Criticism and
Improvement)
The central engine orchestrates a closed-loop repair process con-
strained by a maximum of five iterations. As illustrated in Figure 1,
the pipeline operates as a control system designed to bridge the
gap between stochastic Large Language Model (LLM) generation
and deterministic execution requirements.
The process initiates with the ingestion of the vulnerable file
and its associated test suite. In the preliminary stage, the Context
Retrieval module parses the repository structure via Abstract Syntax
Tree (AST) analysis to ground the model’s modifications within the
actual project scope, effectively mitigating hallucinated references.
The core repair loop relies on an Adaptive Prompting Strat-
egy. Unlike standard RCI implementations that blindly feed back
raw error logs, RepoGuard classifies validation failures into three
distinct domains:
(1) Security Violations: Triggered by SAST tools (e.g., Bandit),
resulting in pattern-specific constraints (e.g., enforcement
of parameterized queries).
(2) Dependency Failures: Triggered by ImportError or NameError
exceptions, resulting in syntax-focused recovery instruc-
tions.
(3) Logic Errors: Triggered by unit test assertions, resulting in
functional correction directives.
Following candidate generation, the Auto-Importer functions
as a deterministic sanitization layer. This module intercepts the
raw LLM output and enforces strict dependency resolution rules,
mechanically correcting common hallucinated imports (e.g., depre-
cated Flask submodules) before the code reaches the interpreter.
Finally, the candidate is subjected to the Hybrid Validation oracle,
which rigorously enforces dual constraints: functional correctness
via unit tests and security compliance via ensemble SAST tools. If
382

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Zago et al.
any constraint is violated, the aggregated error metadata is struc-
tured into the next adaptive prompt, driving a recursive feedback
loop that persists until the candidate satisfies all acceptance criteria
or the iteration limit is reached.
3.5
Theoretical Underpinnings
The design of RepoGuard is grounded in Control Theory and
Program Synthesis principles. We conceptualise the automated
repair process not as a text generation task, but as a Closed-Loop
Control System.
• Stochastic Controller (LLM): The LLM acts as a probabilis-
tic controller 𝑃(𝑦|𝑥,𝑐), generating a candidate patch 𝑦given
vulnerable code 𝑥and context 𝑐. However, as noted in recent
literature, 𝑃(𝑦|𝑥) is prone to entropy (hallucinations).
• Deterministic Feedback Loop (RCI): To counteract en-
tropy, the RCI cycle functions as a negative feedback mech-
anism. The error signal 𝐸—derived from the distance be-
tween the current state and the desired state (secure + func-
tional)—modulates the next input prompt. This transforms
the open-loop generation (𝑥→𝑦) into a feedback-driven
convergence process (𝑥→𝑦0 →𝐸0 →𝑦1 . . . ), mathemati-
cally increasing the probability of arriving at a valid solution
state.
• AST-Based Grounding: The Auto-Importer implements
the principle of Syntactic constraints. By imposing a rigid
grammatical structure on the probabilistic output, we reduce
the search space of possible solutions, effectively pruning
branches of the generation tree that are syntactically invalid
(e.g., NameError), thereby accelerating convergence.
4
Methodology and Evaluation
To rigorously validate the theoretical model proposed above, we
designed an experimental methodology focused on measuring two
critical dimensions of automated repair: Convergence Stability (the
ability of the feedback loop to reach a valid state) and Generalization
Capability (performance across diverse vulnerability classes).
Our evaluation strategy is dual-layered:
(1) Micro-Level Qualitative Analysis: A deep-dive case study
on a complex, multi-vulnerability artefact to trace the inter-
nal mechanics of the RCI cycle, specifically analyzing how
the error signal 𝐸(validation feedback) drives the reduction
of vulnerability density over time.
(2) Macro-Level Quantitative Benchmarking: A compara-
tive analysis against a baseline model using a dataset derived
from the OWASP Top 10. This phase isolates the impact of
the RepoGuard architecture by treating the underlying LLM
(Qwen-2.5-7B) as a controlled variable, thereby measuring
the specific contribution of the agentic orchestration and
Auto-Importer modules.
4.1
Qualitative Case Study: Mechanism
Validation
To assess the effectiveness of the RCI cycle in a controlled envi-
ronment, a case study was conducted using a synthetic Python
script intentionally designed to contain multiple critical Common
Weakness Enumerations (CWEs) commonly encountered in real ap-
plications. The objective was to evaluate the system’s convergence
to a safer and functional solution.
4.1.1
Test Scenario. The test artefact, vulnerable_code.py, in-
corporated several high-severity vulnerabilities:
• CWE-78 (Command Injection): Use of os.system with
concatenated user input.
• CWE-95 (Code Injection): Direct eval() on unsanitised
input.
• CWE-502 (Deserialization): pickle.loads on binary data.
• CWE-798 (Hardcoded Credentials): Passwords and to-
kens defined directly in source.
A unit test suite (test_example.py) served as the functionality or-
acle, ensuring preservation of business logic (e.g., sum calculations
and data return) post-refactoring.
4.1.2
Execution Results. The experiment demonstrated complete
code sanitisation in only two iterations. Table 2 details the evolution
of metrics during the repair process, evidencing both syntactic and
security corrections.
Table 2: Evolution of security, syntactic integrity, and perfor-
mance metrics during the qualitative case study.
Iteration
Vulnerabilities
Syntactic Errors
Test Status
Size
Time (s)
Initial
9 (Critical)
0
N/A
1322 bytes
-
1
9 (Detected)
0 (Auto-Import Fixed)
Passed
1322 bytes
15.4
2
0 (Safer)
0
Passed
980 bytes
28.2
In Iteration 1, the critical role of the Auto-Importer was evi-
dent. The LLM generated corrections utilizing type hints such as
Optional and Dict in function signatures but omitted the nec-
essary from typing import ... statements. Without the AST
post-processing module, the execution would have failed with a
NameError, halting the repair cycle. The module detected the miss-
ing types and mechanically injected the required imports, enabling
successful test execution and the identification of residual vulnera-
bilities.
In Iteration 2, the security corrections proved effective against
specific high-severity flaws:
(1) Command Injection (CWE-78): As shown in Figure 2,
the vulnerability was mitigated by replacing the insecure
os.system(f"...") call with subprocess.run(["cmd", arg]).
This change enforces argument isolation, preventing shell
meta-character injection (Figure 3).
Figure 2: Occurrence of CWE-
78
Figure 3: Correction applied
(2) Code Injection (CWE-95): The use of eval() (Figure 4)
was replaced with ast.literal_eval() (Figure 5), correctly
restricting evaluation to safe literals only.
383

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

RepoGuard: Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation
ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Figure 4: Occurrence of CWE-
95
Figure 5: Correction applied
(3) Insecure Deserialization (CWE-502): The vulnerability
associated with pickle (Figure 6) was eliminated by switch-
ing to the secure JSON serialisation protocol (Figure 7).
Figure 6: Occurrence of CWE-
502
Figure 7: Correction applied
(4) Path Traversal (CWE-35): The code in Figure 8 initially per-
mitted writing outside the intended directory. The correction
employed path isolation via os.path.join and validation
(Figure 9).
Figure 8: Occurrence of CWE-
35
Figure 9: Correction applied
The resulting code in Iteration 2 was reduced to 980 bytes while
passing all functional tests. Furthermore, the noise filtering mecha-
nisms successfully prevented Bandit alerts characterized as "hints"
from triggering infinite correction loops, a common failure mode
in iterative LLM repair.
4.2
Quantitative Comparative Analysis
To validate the generalization capabilities of RepoGuard beyond a
single instance, we conducted a comparative benchmark against a
vanilla baseline model (Qwen-2.5-7B).
4.2.1
Dataset Selection. Identifying fully functional open-source
projects that contain severe, exploitable vulnerabilities suitable for
automated repair benchmarking is a known challenge in software
engineering research. To ensure a robust and reproducible eval-
uation, we curated a dataset of 7 distinct test cases derived from
established security testing repositories (e.g., OWASP Benchmark,
CWE reference implementations). These repositories provide realis-
tic, isolated implementations of the OWASP Top 10 vulnerabilities,
mirroring the logic found in production environments without the
noise of unrelated infrastructure code.
4.2.2
Results. The results of this comparative analysis are pre-
sented in Table 3.
Table 3: Comparative Analysis of Automated Repair Success
Rates.
The baseline model (Qwen-2.5-7B) introduced regression er-
rors in 2 out of 7 test cases (28.5% failure rate), primarily
due to hallucinated or missing dependencies. RepoGuard
autonomously resolved all regressions, achieving a 100% suc-
cess rate across the OWASP Top 10 benchmark dataset in
under 3 iterations.
Benchmark Case
Base LLM
RepoGuard
Ite.
Time (s)
Deserialization
✓
✓
2
24.14
Hard Credentials
✓
✓
2
16.78
Insecure Hashing
✓
✓
1
0.44
Path Traversal
✗
✓
1
0.54
SQL Injection
✓
✓
2
20.81
Unsafe YAML
✓
✓
2
15.24
XSS (Reflected)
✗
✓
1
0.52
The data reveals a critical insight: while the baseline LLM is
often capable of generating the correct logic to fix a vulnerabil-
ity, it frequently introduces regression errors that break the build.
Specifically, in the Path Traversal and XSS test cases, the baseline
model correctly identified the security flaw but failed to import
the necessary libraries (e.g., werkzeug or markupsafe), resulting
in ImportError and NameError exceptions (7).
RepoGuard, leveraging its Auto-Importer and RCI cycle, de-
tected these environmental regressions and autonomously repaired
them, achieving a 100% success rate (3) . This demonstrates that Re-
poGuard provides significant stability improvements over raw LLM
generation, ensuring that security patches are not only theoretically
correct but also functionally executable.
4.3
Limitations and Failure Modes
While the experimental results demonstrate high convergence rates
(100% success on the selected dataset), RepoGuard-Agent is not
immune to failure, particularly when scaling to more complex, logic-
heavy applications. Our extensive testing revealed two distinct
failure modes where the Recursive Criticism and Improvement
(RCI) cycle struggles to converge within the maximum iteration
limit.
4.3.1
Correction Oscillation. We observed scenarios, particularly
in early tests of cmd_injection and medium_app, where the LLM
entered a "fix-break" loop. In these cases, the model would success-
fully patch the security vulnerability (satisfying the SAST scanner)
but inadvertently break the functional logic (failing the unit test). In
the subsequent iteration, the model would revert the security fix to
restore functionality, re-introducing the vulnerability. To mitigate
this, RepoGuard employs a "fail-safe" architecture, where if the
system detects oscillation or fails to converge after 5 iterations, it
discards the generated changes and flags the file for manual human
intervention, prioritizing system stability over forced, potentially
broken patches.
384

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
Zago et al.
4.3.2
Dependency Hallucination and Contextual Ambiguity. A per-
sistent challenge for LLMs, as evidenced by the baseline model’s fail-
ure in our Path Traversal and XSS benchmarks, is the hallucination
of non-existent or deprecated library functions (e.g., flask.safe_join,
flask.escape). While our Auto-Importer successfully resolved
100% of these cases in our dataset, there remains a risk of Contex-
tual Ambiguity in larger repositories where symbols with identical
names exist across different libraries (e.g., json vs. simplejson). In
such rare events, the AST post-processor may incorrectly resolve
the dependency, leading to runtime ImportErrors that require
deeper, project-wide dependency analysis to resolve.
4.3.3
Benchmark Scope. Finally, we acknowledge that while our
dataset was derived from real-world security specifications (OWASP/CWE),
it remains a controlled benchmark. The transition to large-scale,
legacy enterprise repositories introduces variables such as non-
standard build systems and complex inter-module dependencies
that were not fully captured in this study. Future work will focus on
integrating RepoGuard into CI/CD pipelines of active open-source
projects to gather longitudinal data on repair performance in wild
environments.
5
Conclusion
This paper presented RepoGuard, demonstrating that AI-assisted
code security requires a robust hybrid architecture incorporating
recursive, iterative refinement for continual improvement. The
primary contribution lies in integrating a stochastic probabilistic
generation pipeline (LLM) with deterministic validation (AST) and
adaptive feedback mechanisms.
Our evaluation confirms that, although Large Language Mod-
els are proficient in generating local remediation logic, they suffer
from "scope myopia" and frequent hallucination of environmental
dependencies. The comparative analysis against a baseline model
revealed that standard LLMs introduced regression errors (specifi-
cally ImportError and NameError) in 28.5% of test cases, despite
correctly identifying the security vulnerability.
RepoGuard effectively bridged this gap through two key mecha-
nisms:
(1) Deterministic Auto-Importer: This module proved es-
sential for ensuring executability by aggressively sanitizing
hallucinated imports (e.g., deprecated Flask submodules) and
mechanically injecting required dependencies, achieving a
100% recovery rate from baseline regressions.
(2) Adaptive RCI Cycle: By classifying validation failures into
specific domains (Security, Dependency, Logic) and tailoring
the feedback prompt accordingly, the system avoided the
infinite loops common in static feedback loops, successfully
satisfying strict SAST scanners (Bandit).
Combined with hybrid scanning and AST-based context retrieval,
the system successfully remediated a diverse spectrum of critical
vulnerabilities—including Command Injection (CWE-78), Code In-
jection (CWE-95), Insecure Deserialization (CWE-502), and Hard-
coded Credentials (CWE-798)—while rigorously maintaining func-
tional integrity. These findings indicate that substantial advance-
ments in automated repair are achieved not merely by scaling model
parameters, but by encapsulating stochastic generators within de-
terministic architectural guardrails.
Furthermore, the architectural decision to utilise a parameter-
efficient local model (7B) rather than relying on external API-based
proprietary models opens significant avenues for deployment in
sensitive and resource-constrained environments. By enabling fully
on-premise operation, RepoGuard addresses critical concerns re-
garding data sovereignty, intellectual property leakage, and regula-
tory compliance that currently prohibit the use of cloud-based LLMs
in defense, banking, and healthcare sectors. This demonstrates that
effective automated repair infrastructures can be established within
air-gapped networks using commodity hardware, democratising
access to AI-driven security tools without compromising confiden-
tiality or requiring prohibitive GPU infrastructure.
To ensure research transparency and facilitate community adop-
tion, the complete source code of the RepoGuard framework, in-
cluding the benchmark dataset used in this study, has been made
publicly available. The project is accessible at: https://github.com/
cassianodz/RepoGuardCore.
Future work will focus on integrating the tool into CI/CD pipelines
for proactive vulnerability remediation and expanding the Auto-
Importer’s knowledge base to support a wider range of third-party
ecosystems.
Acknowledgments
The authors acknowledge the support of the LATITUDE Labora-
tory, University of Brasília, TED 01/2021 of the National Secretariat
of Social Assistance – SNAS/DGSUAS/CGRS, TED 01/2021 of the
Attorney General’s Office of the National Treasury – PGFN, the SIS-
TER City Project (Grant 625/2022 – FAP/DF), the SISPRO-DF Project
(Grant 497/2023 – FAP/DF), the Dean of Research and Innovation –
DPI/UnB and FAP/DF.
References
[1] Anna Bertiger, Bobby Filar, Aryan Luthra, Stefano Meschiari, Aiden Mitchell,
Sam Scholten, and Vivek Sharath. 2025. Evaluating LLM Generated Detection
Rules in Cybersecurity. arXiv preprint arXiv:2509.16749 [cs.CR].
[2] Manish Bhatt, Sahana Chennabasappa, Cyrus Nikolaidis, Shengye Wan, Ivan
Evtimov, Dominik Gabi, Daniel Song, Faizan Ahmad, Cornelius Aschermann,
Lorenzo Fontana, et al. 2023. Purple Llama CYBERSECEVAL: A Secure Coding
Benchmark for Language Models. arXiv preprint arXiv:2312.04724. doi:10.48550/
arXiv.2312.04724
[3] Marc Bruni, Fabio Gabrielli, Mohammad Ghafari, and Martin Kropp. 2025. Bench-
marking Prompt Engineering Techniques for Secure Code Generation with GPT
Models. arXiv preprint arXiv:2502.06039 [cs.SE].
[4] Shuyu Chang, Chen Geng, Haiping Huang, Rui Wang, Qi Li, and Yang Zhang.
2025. CodeSpeak: Improving smart contract vulnerability detection via LLM-
assisted code analysis. The Journal of Systems and Software 231 (2025), 112635.
doi:10.1016/j.jss.2025.112635
[5] Yiannis Charalambous, Edoardo Manino, and Lucas C. Cordeiro. 2024. Automated
Repair of AI Code with Large Language Models and Formal Verification. arXiv
preprint arXiv:2405.08848 [cs.SE].
[6] Junkai Chen, Huihui Huang, Yunbo Lyu, Junwen An, Jieke Shi, Chengran Yang,
Ting Zhang, Haoye Tian, Yikun Li, Zhenhao Li, Xin Zhou, Xing Hu, and David Lo.
2025. SecureAgentBench: Benchmarking Secure Code Generation under Realistic
Vulnerability Scenarios. arXiv preprint arXiv:2509.22097. doi:10.48550/arXiv.
2509.22097
[7] Marquis de Condorcet, Marie-Jean-Antoine-Nicolas de Caritat. 1785. Essai sur
l’application de l’analyse à la probabilité des décisions rendues à la pluralité des
voix. Imprimerie Royale, Paris. Disponível em: https://archive.org/details/bub_
gb_RzAVAAAAQAAJ Acesso em: 27/11/2025.
[8] Aaron Councilman, David Fu, Aryan Gupta, Chengxiao Wang, David Grove,
Yu-Xiong Wang, and Vikram Adve. 2025.
Towards Formal Verification
of LLM-Generated Code from Natural Language Prompts.
arXiv preprint
arXiv:2507.13290. doi:10.48550/arXiv.2507.13290
[9] Elyson De La Cruz, Hanh Le, Karthik Meduri, Geeta Sandeep Nadella, and Hari
Gonaygunta. 2025. Redefining the Programmer: Human-AI Collaboration, LLMs,
385

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

RepoGuard: Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation
ICICT 2026, March 11–13, 2026, Honolulu, HI, USA
and Security in Modern Software Engineering. Computers, Materials & Continua
85, 2 (2025), 3569–3582. doi:10.32604/cmc.2025.068137
[10] Shih-Chieh Dai, Jun Xu, and Guanhong Tao. 2025. Rethinking the Evaluation of
Secure Code Generation. In 2026 IEEE/ACM 48th International Conference on
Software Engineering (ICSE ’26). ACM, Rio de Janeiro, Brazil, 1–13. doi:10.1145/
3744916.3773217
[11] Connor Dilgren, Purva Chiniya, Luke Griffith, Yu Ding, and Yizheng Chen. 2025.
SecRepoBench: Benchmarking LLMs for Secure Code Generation in Real-World
Repositories. arXiv preprint arXiv:2504.21205. doi:10.48550/arXiv.2504.21205
[12] Mete Keltek, Rong Hu, Mohammadreza Fani Sani, and Ziyue Li. 2024. Boosting
Cybersecurity Vulnerability Scanning based on LLM-supported Static Application
Security Testing. arXiv preprint arXiv:2409.15735 [cs.CR].
[13] Nikolaos Malamas, Emmanouil Tsardoulias, Konstantinos Panayiotou, and An-
dreas L. Symeonidis. 2025. Toward efficient vibe coding: An LLM-based agent
for low-code software development. Journal of Computer Languages 85 (2025),
101367. doi:10.1016/j.cola.2025.101367
[14] Rupam Patir, Keyan Guo, Haipeng Cai, and Hongxin Hu. 2025. Fortifying LLM-
Based Code Generation with Graph-Based Reasoning on Secure Coding Practices.
arXiv preprint arXiv:2510.09682 [cs.CR].
[15] Adam Jerome Salyers, Sheana Bull, Joshva Silvasstar, Kevin Howell, Tara Wright,
and Farnoush Banaei-Kashani. 2025. Building and Beta-Testing Be Well Buddy
Chatbot, a Secure, Credible and Trustworthy AI Chatbot That Will Not Misinform,
Hallucinate or Stigmatize Substance Use Disorder: Development and Usability
Study. JMIR Human Factors 12 (2025), e69144. doi:10.2196/69144
[16] Minghao Shao, Sofija Jancheska, Meet Udeshi, Brendan Dolan-Gavitt, Haoran Xi,
Kimberly Milner, Boyuan Chen, Max Yin, Siddharth Garg, Prashanth Krishna-
murthy, Farshad Khorrami, Ramesh Karri, and Muhammad Shafique. 2024. NYU
CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs
in Offensive Security. In 38th Conference on Neural Information Processing
Systems (NeurIPS 2024) Track on Datasets and Benchmarks. Curran Associates,
Inc., Red Hook, NY, USA, 1–14. doi:10.48550/arXiv.2406.05590
[17] Maryam Taeb, Hongmei Chi, and Shonda Bernadin. 2024. Assessing the Ef-
fectiveness and Security Implications of AI Code Generators. Journal of The
Colloquium for Information Systems Security Education 11, 1 (2024), 6–16.
[18] Norbert Tihanyi, Tamas Bisztray, Mohamed Amine Ferrag, Ridhi Jain, and Lucas C.
Cordeiro. 2025. How secure is AI-generated code: a large-scale comparison of
large language models. Empirical Software Engineering 30, 2 (2025), 47. doi:10.
1007/s10664-024-10590-1
[19] Catherine Tony, Nicolás E. Díaz Ferreyra, Markus Mutas, Salem Dhif, and Riccardo
Scandariato. 2024. Prompting Techniques for Secure Code Generation: A System-
atic Investigation. arXiv preprint arXiv:2407.07064. doi:10.48550/arXiv.2407.07064
[20] Catherine Tony, Maura Pintor, Max Kretschmann, and Riccardo Scandariato. 2025.
Discrete Prompt Optimization Using Genetic Algorithm for Secure Python Code
Generation. The Journal of Systems and Software 232 (2025), 112682. doi:10.
1016/j.jss.2025.112682
[21] Jiexin Wang, Xitong Luo, Liuwen Cao, Hongkui He, Hailin Huang, Jiayuan
Xie, Adam Jatowt, and Yi Cai. 2024. Is Your AI-Generated Code Really Secure?
Evaluating Large Language Models on Secure Code Generation with CodeSecEval.
arXiv preprint arXiv:2407.02395. doi:10.48550/arXiv.2407.02395
386

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/less%20important/repoGuard/page-09.png)
