# RMGenie: An LLM-Based Agent Framework for Open Source Software README Generation

- source_pdf: ../../../../pdf/Documentation%20Generation/RMGenie.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RMGenie: An LLM-Based Agent Framework
for Open Source Software README Generation
Xing Cui†‡, Jingzheng Wu†, Zhiyuan Li†‡, Tianyue Luo†, Xiang Ling†‡
†Institute of Software, Chinese Academy of Sciences
‡University of Chinese Academy of Sciences
{cuixing, jingzheng08, lizhiyuan2021, tianyue, lingxiang}@iscas.ac.cn
Abstract—Open Source Software (OSS) plays a vital role
in modern software ecosystems, with README files providing
essential information on functionality, configuration, and usage.
However, approximately 9.03% of OSS projects lack adequate
README documentation, impacting developer efficiency and
software maintainability. Recent advances in natural language
processing and large language models (LLMs) have automated
README generation to reduce manual effort. Yet, existing
methods struggle with integrating real-time external knowledge,
parsing complex software structures, and adapting to project-
specific requirements. To address these challenges, this paper
introduces RMGenie, a framework that leverages LLM-based
agents and external tool invocation for automated README
generation. RMGenie constructs an agent-driven workflow en-
abling multi-round interactions with external tools to dynam-
ically extract critical code insights, particularly for complex
software structures. It employs a Tree of Actions model with
an entropy-based scoring mechanism to optimize decision paths
for README generation. Additionally, a reflexion Mechanism
enhances accuracy by mitigating decision biases and tool in-
vocation errors. Experimental results confirm that RMGenie
significantly outperforms baseline methods in content complete-
ness, instruction adherence, and factual accuracy. Furthermore,
we develop a plugin that integrates RMGenie to automatically
generate README files from GitHub repositories, improving
developer productivity and standardizing OSS documentation.
The plugin is available at VSCode Marketplace.
Index Terms—open source software, README generation,
large language models, intelligent agent.
I. INTRODUCTION
Open source software (OSS) has rapidly become a corner-
stone of the modern information industry. The exponential
growth of OSS provides developers with abundant techno-
logical resources but also presents challenges in software
comprehension and reuse [1]–[4]. README files are critical
in addressing these challenges, offering insights into a project’s
architecture, core functionalities, and usage. They typically
include an overview, installation steps, usage instructions, and
functional details, serving as the primary interface for users
and a key medium for showcasing project value. However,
creating high-quality README files demands time, expertise,
Q Jingzheng Wu and Xiang Ling are the corresponding authors.
and ongoing maintenance. As a result, many OSS projects,
especially smaller or newer ones, provide incomplete, poorly
structured, or entirely missing documentation [5], [6]. To
quantify this issue, we conduct an empirical study to analyze
100,000 OSS on GitHub, finding that approximately 9.03%
lack a README file. Even among those with README files,
many fail to include essential information or key details. This
deficiency hampers software adoption, increases the learning
curve for developers, and limits a project’s development.
To address this widespread issue of inadequate README
files, various methods for automated or assisted README
generation have been proposed. These approaches can broadly
be categorized into traditional methods and, more recently,
methods leveraging large language models (LLMs). LLMs,
capable of learning complex linguistic patterns from large-
scale datasets, have demonstrated strong potential in automat-
ing README generation [7]–[9]. Recent studies explore their
role in improving OSS documentation quality and usability
[10], [11]. Sun et al. propose PromptCS, a prompt-learning
framework for README summarization, combining code,
prompt, and fused embeddings [12]. By freezing model param-
eters and updating only prompt representations, PromptCS re-
duces computational overhead while maintaining compatibility
with various LLMs, enhancing LLM-driven summarization for
README completion. Koreeda et al. introduce LARCH, an
LLM-powered tool for automated README generation [13].
It employs gradient boosting trees to identify key code snippets
and generates structured prompts to guide GPT-3 in documen-
tation synthesis. Luo et al. develop RepoAgent, a framework
leveraging LLMs for deep code analysis and dynamic doc-
umentation management [14]. RepoAgent operates in three
stages: global structure analysis, documentation generation,
and continuous update tracking. It extracts metadata, applies
fine-grained documentation strategies, and integrates Git-based
tracking to ensure README consistency with code updates.
Despite significant progress in using LLMs for automated
README generation, several challenges remain. First, exist-
ing approaches primarily rely on static prompt engineering
and predefined rules, lacking dynamic reasoning capabilities.
505
2025 IEEE International Conference on Software Maintenance and Evolution (ICSME)
2576-3148/25/$31.00 ©2025 IEEE
DOI 10.1109/ICSME64153.2025.00052
2025 IEEE International Conference on Software Maintenance and Evolution (ICSME) | 979-8-3315-9587-6/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICSME64153.2025.00052
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 1](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-01.png)

![Página PDF 1, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

They follow fixed text patterns without exploring optimal
information organization during inference, limiting the log-
ical coherence and readability of the generated README
files. Second, most methods lack self-correction mechanisms,
making them unable to identify potential errors or incomplete
information, which may lead to omissions or inaccuracies in
the generated content. Furthermore, these methods often ex-
tract information at the code level while neglecting the global
structure of large or complex repositories. This limitation may
result in README files that fail to comprehensively cover
key functional components.
To overcome the limitations of existing README genera-
tion methods, we propose RMGenie, an automated README
generation framework for OSS. RMGenie first employs an
LLM-based agent as its core reasoning and decision unit,
enabling autonomous decision-making and information inte-
gration. By analyzing OSS repositories, it extracts key in-
formation on file structures, dependencies, and development
environments, ensuring a comprehensive understanding of core
components and addressing the limitations of existing methods
that rely on isolated code snippets and overlook global struc-
tures. Next, RMGenie introduces the Tree-of-Actions (ToA)
model to construct dynamic decision pathways. During infer-
ence, the agent iteratively expands reasoning paths. This model
overcomes the shortcomings of static prompt engineering and
predefined rules that often lead to suboptimal README gen-
eration. Finally, RMGenie incorporates a reflexion mechanism
for adaptive decision-making. The agent reviews decision
pathways, analyzes past actions, and dynamically refines its
strategy. When inefficiencies or errors are detected, it adjusts
its reasoning path and replans optimal actions. By integrat-
ing task-driven reasoning, hierarchical decision-making, and
adaptive optimization, RMGenie provides an intelligent and
efficient solution for README generation, ensuring com-
prehensive, structured, and self-optimizing documentation for
complex OSS repositories. In summary, RMGenie makes the
following contributions:
• We introduce RMGenie, an LLM-based agent framework
for automated README generation in OSS. It extracts
complex file structures, dependencies, and environment
information, enhancing documentation adaptability.
• We propose the ToA model to construct dynamic reason-
ing pathways. By iteratively refining content organiza-
tion, it enhances logical coherence and structural clarity
beyond static prompt-based methods.
• Experiments on a dataset of 150 GitHub OSS projects
show that RMGenie outperforms mainstream LLMs and
existing methods in satisfaction, completeness, accuracy,
and compliance. It achieves the highest scores across all
metrics, with an automated evaluation score of 84.33,
exceeding the best baseline by 15%, and the highest win
rate in human evaluation, confirming its effectiveness in
README generation.
• We develop a VSCode plugin for RMGenie, enabling au-
tomated README generation within the IDE, improving
efficiency and documentation consistency.
II. BACKGROUND
A. Automatic README Generation
Automatic README generation leverages natural language
processing (NLP) techniques and LLMs like GPT and Codex
to create and refine project documentation. It analyzes code
structure, comments, dependencies, and metadata to generate
structured README files with key details such as project
overviews, installation guides, and usage examples. This au-
tomation reduces developers’ documentation workload while
ensuring consistency and synchronization with the code, en-
hancing maintainability [15], [16].
B. LLMs and LLM-based Agents
LLMs, trained on vast text datasets, power autonomous
systems for complex tasks. LLM-based agents extend this by
enabling reasoning, planning, and interaction [17]–[20]. They
interpret instructions, execute tasks, and adapt dynamically,
excelling in complex scenarios. Their architecture includes a
decision-making LLM, memory for knowledge retention, a
planning module, and external tool access. In software engi-
neering, they can enhance README generation by optimizing
workflows, leveraging tools, and analyzing repositories for
greater efficiency.
C. Hierarchical Reasoning
Although LLM-based agents excel in problem-solving, their
reasoning and planning in complex tasks require further im-
provement. The tree-structured reasoning process enhances
LLMs by enabling parallel exploration of multiple reasoning
paths, reducing local optima risks, and improving efficiency.
By structuring thought expansion like a tree, this approach
strengthens planning and inference, allowing LLMs to tackle
complex tasks more effectively [21], [22].
D. Adaptive Reflexion
In agent research, the adaptive reflexion mechanism en-
hances adaptability by optimizing decision-making and en-
abling autonomous error correction in dynamic environments
[23]–[25]. It enables agents to analyze decision paths, identify
critical junctures, and detect errors through self-assessment
and logical reasoning, even without external guidance. Addi-
tionally, it facilitates strategy refinement and error mitigation,
improving execution reliability.
III. METHODOLOGY
A. Overview
This study explores the automated generation of README
files in complex OSS systems. We propose RMGenie, a novel
framework leveraging LLM-based agent comprising three key
components. As illustrated in Figure 1, RMGenie integrates
three core components. First, an LLM-based agent orchestrates
a structured workflow that analyzes repository data, integrates
user requirements, and iteratively refines README content
through distinct decision and execution phases (Section III-B).
506
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 2](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-02.png)

![Página PDF 2, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

User Query
“Generate a README for my 
Python web scraper with an MIT 
license, including installation, 
usage, and license details.”
LLM-Based Agent Workflow
Tree of Actions
Adapative Reflexion Mechanism 
Workspace
In this phase, I will decompose 
the README generation task, 
execute structured actions, and 
iteratively refine the content to 
ensure clarity and completeness.
In this phase, I will analyze the 
OSS repository structure, 
extract key metadata, and 
gather relevant external 
knowledge to construct a 
comprehensive README outline.
Decision Phase
     Execution Phase
OSS Repository  
Context Awareness  
My Web Scraper 
scraper.py  
Source Code  
LISENSE  
README.MD  
Semantic Analysis  
Knowledge Integration  
External 
Knowledge Base 
ToolChain
Action Decomposition  
Action Execution  
Refinement  
Select top k candidates based on 
TF-IDF and reward (k = 1 here).
I will refine the actions according to 
the feedback (eg. formatting errors)!
Finally, we get the 
ideal README file!
Open-source Policies
  
Filtered OSS Projects  
Toolset.py  
Code Parsers  
Error Detetion   
Historical 
Decision Review   
Action Adjustment   
Fig. 1. Overview of RMGenie
This process ensures the README aligns with the OSS’s
technical structure and industry standards. Second, the Tree
of Actions (ToA) model employs a hierarchical decision tree
to simulate the agent’s reasoning, optimizing action pathways
by prioritizing information-rich decisions across multiple in-
teraction rounds (Section III-C). Third, an adaptive reflexion
mechanism enhances robustness by enabling the agent to
review past decisions, detect errors, and dynamically adjust
its strategy based on execution feedback (Section III-D).
Together, these components enable RMGenie to systematically
decompose complex documentation tasks, improve decision
efficiency, and deliver tailored README files, with each
element detailed in the subsequent sections.
B. RMGenie’s Workflow
RMGenie employs an LLM-based agent architecture to
automate the generation of README for OSS repositories,
integrating the reasoning capabilities of LLMs with the practi-
cal task execution of an executor. This workflow is designed to
produce accurate and contextually relevant documentation by
systematically processing repository data, user requirements,
and external knowledge. The process unfolds in two primary
phases: the decision phase, where the agent strategizes based
on analysis and planning, and the execution phase, where
actions are implemented and iteratively refined. Together, these
phases ensure that the generated README aligns with the
technical specifications of the target OSS and adheres to best
practices, as detailed below.
1) Decision Phase: The decision phase serves as the foun-
dation of RMGenie’s workflow, enabling the agent to construct
a comprehensive strategy for README generation. In the
decision phase, RMGenie analyzes OSS structure and user
requirements, integrates external knowledge, and generates
execution directives to optimize README generation.
Context Awareness: The agent initially examines the OSS
repository to extract essential metadata, such as directory
structure, file organization, and programming language speci-
fications. By analyzing key files — such as .git configuration,
existing README.md (if available), and LICENSE files — the
agent constructs a structural representation of the OSS. Fur-
thermore, it processes user-defined requirements, identifying
specific directives and translating them into executable tasks.
This initial step ensures that subsequent actions are rooted in
the project’s context and aligned with user intent.
Semantic Analysis: Building upon context awareness, the
agent conducts semantic analysis to deepen its understanding
of the codebase. Through abstract syntax tree (AST) [26]
parsing, it interprets the code’s structural composition, ex-
tracting module functionalities, identifying critical APIs, and
mapping dependency relationships. Additionally, the agent
catalogs available toolchains within the repository, such as
documentation frameworks or static analysis tools, to enhance
the information available for README generation.
Knowledge Integration: The agent incorporates external
resources to refine its strategy. By referencing best practices
from established OSS projects and verifying license compati-
bility against open-source policies, the agent ensures that the
README meets industry standards while mitigating potential
legal risks. This structured progression—from context gather-
ing to semantic insight and external validation—culminates in
a set of execution directives that guide the next phase.
2) Execution Phase: In the execution phase, RMGenie op-
erationalizes the strategy developed during the decision phase,
transforming analytical insights into a polished README
through a structured and iterative process.
507
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 3](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-03.png)

![Página PDF 3, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

Prompt for Agent Workflow
Prompt for Executor
### OBJECTIVE
Document execution results for actions such as file operations, API 
requests, and code navigation.
### EXECUTION RESULTS FORMAT
1. Open Folder
OBSERVATION: Opened folder {folder_name} at {file_path}, 
containing: {file_tree_structure}.
2. API Request
OBSERVATION: Requested API {api_name} with 
{api_call_content}, response: {json_api_return}.
3. Open Code File
OBSERVATION: Opened code file {file_name} at {file_path}, 
content: {file_content}.
4. Navigate to Function
OBSERVATION: Clicked {func_name1} in {file_path1}, jumped 
to {func_name2} in {file_path2}, returning its content.
### RESPONSE FORMAT
Ensure structured output for consistent data retrieval.
### TASK DESCRIPTION
Follow the structured dialogue process strictly, adhering to the 
predefined format and interaction rules.
### DIALOGUE FORMAT
QUESTION: User query.
THOUGHT: Analyze input and determine the next action.
ACTION: Select an ACTION from {tool names} without 
modifications.
ACTION INPUT: Provide required parameters per tool schema.
OBSERVATION: System response to ACTION execution. Iterate 
as needed.
FINAL ANSWER: Conclusive response to the user query.
### TOOLS DESCRIPTION
Available tools: {tool names}
Detailed tool descriptions and input formats: {tool descs}
### EXECUTION GUIDELINES
- Follow the structure strictly.
- Execute each step precisely.
### START
QUESTION: {user query}
Fig. 2. Prompt for Agent Workflow and Executor
Action Plan Decomposition: The execution phase begins
with the agent crafting a detailed action plan. Leveraging
prompt engineering, it breaks down the README generation
task into subtasks—such as code analysis, license verification,
and content drafting—guided by the OSS repository’s state,
user requirements, and industry standards. The agent selects
appropriate tools (e.g., APIs, code parsers) and organizes these
subtasks into a structured sequence of instructions, setting the
stage for implementation.
Task Execution and Feedback Collection: Next, the agent
hands the action plan to the executor, which carries out
the specified tasks—querying the repository for code details,
invoking external APIs for license data, or drafting initial
README sections. Upon completion, the executor provides
structured feedback, including execution results or error logs,
giving the agent insight into the outcomes and any issues
encountered during task performance.
Refinement and Communication Standardization: Fi-
nally, the agent evaluates the feedback to identify discrepancies
(e.g., incomplete data or formatting errors) and refines the
README content through iterative adjustments. Prompt en-
gineering [27], as illustrated in Figure 2, standardizes commu-
nication between the agent and executor—defining workflow,
interaction format, and rules—ensuring the LLM efficiently
parses requirements, issues precise instructions, and processes
feedback to deliver a high-quality, tailored README.
By combining a methodical decision phase with a respon-
sive execution phase, RMGenie’s workflow achieves both
precision and adaptability. The decision phase establishes a an-
alytical foundation, while the execution phase operationalizes
this strategy through iterative refinement, guided by structured
prompts and executor feedback. This seamless integration of
reasoning and action enables RMGenie to address the com-
plexities of OSS documentation, producing README files
that are both technically accurate and professionally polished.
C. Tree of Actions
To simulate the decision making process of the RMGenie
intelligent agent, improve decision efficiency in multi-turn
interactions, and optimize path selection for complex tasks,
this study introduces the ToA model. This model employs
a hierarchical tree structure to represent the relationships
among decisions, dependencies between actions, and tran-
sitions between operational states in the agent’s reasoning
process. By leveraging this structured representation, the agent
continuously refines its decision path based on environmental
feedback throughout iterative reasoning, ensuring the genera-
tion of README documentation that accurately aligns with
user requirements.
The ToA model employs a hierarchical structure with a
root node, branch decision nodes, and terminal decision nodes
to describe an agent’s state evolution and decision-making
over multiple interaction rounds. The root node represents the
agent’s initial state, where it processes user query and selects
an initial action based on the environment (e.g., analyzing
code structure or querying external knowledge bases), with
all subsequent inference pathways originating from this node.
Branch decision nodes represent possible actions generated
during reasoning, each corresponding to a distinct decision
pathway. The agent dynamically expands the decision tree
by generating multiple action directives based on the current
environment and available resources (e.g., code files, APIs,
508
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 4](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-04.png)

![Página PDF 4, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

OSS dependencies). Terminal decision nodes mark the end of
reasoning, where the agent consolidates acquired information
and generates the final README instead of taking further
actions. Within RMGenie, the agent starts from the root node,
expanding decision pathways based on environmental states
and available tools while continuously refining its strategy.
The inference process terminates when the ToA reaches a
predefined threshold or when the agent identifies the optimal
pathway, triggering the final README generation.
In the ToA model, the agent expands multiple candidate
action nodes at the end of each interaction round based on
the current state and policy function to construct an efficient
decision pathway. During this process, the agent employs the
policy function A(st | θ) to explore and evaluate the action
space. In each decision round, the agent generates multiple
candidate actions ai using the policy function, given the
current state st. These actions represent all potential operations
available to the agent in that state. To ensure the effectiveness
and diversity of the search process, candidate actions should
not only encompass direct operations but also account for their
potential dependencies and execution order.
A(st | θ) = {a(t+1)
1
, a(t+1)
2
, . . . , a(t+1)
K
}
(1)
The formula describes the process of node expansion along
the decision path. At time t, given the state st, the policy
function A(st | θ) computes and selects K possible actions
{a(t+1)
1
, a(t+1)
2
, . . . , a(t+1)
K
} as candidates for the next step.
Each candidate action node a(n)
i
is connected to the root
node via directed edges, representing the execution order
and dependency relationships. The edge weights quantify the
information gain of actions, while the direction from the root
node to branch decision nodes defines the execution sequence,
ensuring the logical coherence and operational effectiveness
of the decision tree. Assuming the edge weight from node
nt = (st, ai) to node nt+1 = (st+1, aj) is wij,it is defined as:
wij = ∆I(ai, aj)
(2)
where ∆I(ai, aj) represents the information gain from action
ai to aj. By computing the information gain of each candidate,
RMGenie prioritizes those contributing more to inference, op-
timizing decision path and reducing redundant computations.
The ToA model employs a hierarchical structure, where
each decision layer depends on the previous one, forming a
progressive decision pathway. This hierarchical design enables
RMGenie to decompose complex global tasks into simpler
sub-tasks, allowing each decision round to focus on local infor-
mation and reducing overall decision complexity. Specifically,
at layer n, each candidate action a(n)
i
is selected based on the
previous layer’s state s(n−1)
t
. This relationship is expressed as:
s(n)
t
= f(s(n−1)
t
, a(n−1)
i
)
for a(n−1)
i
∈A(n−1)
(3)
where s(n)
t
represents the state at layer n, and f(·) denotes
the state transition function.
As the number of possible actions increases, computational
costs rise, and inference time extends. Efficient decision-
making necessitates pre-filtering the action tree to identify
optimal pathways. To achieve this, an evaluator is designed
to leverage information gain, simulate multi-round decision-
making, assess pathway rewards, and refine strategies through
backtracking. Information entropy quantifies information gain,
providing guidance for action selection. In the context of
README generation, the evaluation follows two principles.
First, selected actions should maximize information gain to
enhance the accuracy of the generated README. Second,
decision-making should integrate both current and past actions
to maintain coherence in reasoning. Based on these two
evaluation criteria, we design a TF-IDF-based [28] entropy
score as the evaluation function in the ToA model:
Estep(n)(astep(n)
i
|S) = T(Sstep(n)
i
|S) −T(Sstep(n)
i
|sstep(n)
i
, S) (4)
This formula quantifies the information gain from executing
action astep(n)
i
in state S. T(Sstep(n)
i
| S) represents the uncer-
tainty of state Sstep(n)
i
given S, while T(Sstep(n)
i
| sstep(n)
i
, S)
denotes the uncertainty after observing action sstep(n)
i
. Thus,
the formula measures the reduction in uncertainty, indicating
the information gain provided by astep(n)
i
. A higher information
gain suggests a greater contribution of the action to optimizing
the decision path, enabling more efficient inference.
Considering that the effectiveness of RMGenie’s actions
depends not only on the current state but also on historical
decisions and feedback, we introduce the branch reward to
evaluate the impact of an action on future decision space and
optimize action selection. The calculation is given by:
RB(astep(n)
i
) = T(D ∈Sstep(n)|S) −T(D ∈Sstep(n−1)|S)
(5)
where D represents all files in the current state, T(D ∈
Sstep(n)|S) denotes the TF-IDF value of the files in the current
directory relative to the entire repository after executing the
action, and T(D ∈Sstep(n−1)|S) represents the TF-IDF value
before execution. This formula indicates that if an action
significantly increases the TF-IDF importance of files, it
effectively expands the future decision space, leading to higher
information gain. The entropy-based evaluation function incor-
porating the branch reward is formulated as:
Estep(n)(astep(n)
i
) = T(Sstep(n)
i
|S)−
T(Sstep(n)
i
|sstep(n)
i
, S) + RB(astep(n)
i
)
(6)
This information gain mechanism enables RMGenie to
identify and retain actions that may have low short-term infor-
mation gain but contribute more to future decisions. Based on
this entropy score, we construct an information gain evaluator
to assess each action’s contribution to README generation
and select the optimal actions. During the evaluation, we adopt
a parametric strategy, retaining only the top k candidate actions
per decision layer to improve search efficiency. A larger k
considers more historical actions but increases computational
overhead. This evaluator operates in each decision round,
ensuring the selection of the optimal decision path.
509
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 5](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-05.png)

![Página PDF 5, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

D. Adaptive Reflexion Mechanism
In RMGenie, we introduce an adaptive reflexion mecha-
nism to enhance the agent’s ability to autonomously optimize
decision-making in complex tasks, particularly when handling
errors, repetitive actions, or inefficient decisions. This mech-
anism enables the agent to review past decisions, identify
potential errors, and dynamically adjust its action path to
improve decision quality and execution efficiency [29], [29].
When the executor encounters an error (e.g., API request
failure, inaccessible files, or redundant actions), the agent re-
ceives feedback, including the error state and its corresponding
action history, and traces back to a critical decision node for
reassessment. Based on this feedback, the agent analyzes past
decisions, identifies actions that led to undesirable outcomes,
and adjusts its strategy accordingly, resuming execution from
the most optimal point. The reflexion mechanism in RMGenie
consists of three key steps:
Error Detection and Feedback: Upon executing an action,
the agent evaluates the outcome to determine whether an
error has occurred (e.g., task failure or invalid operation).
If an action does not produce the expected result, the agent
immediately receives feedback to analyze the cause of failure.
Reviewing Historical Decisions: When an error or inef-
ficiency is detected, the agent reviews its historical decision
pathway, analyzing past actions, rationale, and outcomes to
identify potential biases or redundant operations. The agent
not only verifies the validity of the current action but also
evaluates whether each decision has effectively contributed to
the task objective.
Adjusting the Action Pathway: Based on the reflexion
results, the agent selects an appropriate historical node to
restart task execution. It may replan from the point of failure
or an earlier decision node to explore a more optimal solution.
If the executor O fails to execute action astep(t)
i
in environ-
ment Sstep(t), resulting in a failed state sstep(t+1)
i
, the agent
generates a reflexion based on the initial environment Sstep(t)
and the failure state sstep(t+1)
i
. It then selects a historical node
th to re-execute the task, formulated as:
th ←A(astep(t)
i
, sstep(t+1)
i
| Sstep(t))
(7)
t + 1 ←th
(8)
where A(·) is the agent’s reflexion function, responsible for
determining the optimal rollback node th to minimize the
impact of task failures and optimize the decision pathway.
IV. EVALUATION
A. Implementation
1) Experimental Dataset: To ensure the reliability and rep-
resentativeness of the experiment, we randomly collect 5,307
OSS from GitHub and apply predefined criteria to select 791
OSS that meet the experimental requirements. The selection
criteria include: (1) Multilingual Coverage. The selected data
includes OSS implemented in 5 mainstream programming
languages (Python, Java, C/C++, JavaScript) to enhance the
generalizability and robustness of the approach. (2) Star count
≥100. OSS with at least 100 GitHub stars are selected to en-
sure community recognition and representativeness. (3) Code
files ≥10. Each selected OSS contains at least 10 code files,
ensuring sufficient complexity and contextual information to
support README generation.
Given that OSS often contain diverse formatted content,
including code comments, configuration files, scripts, logs, and
documentation, these files frequently incorporate Markdown
syntax, hyperlinks, images, code snippets, tables, and badges,
which can introduce noise in text processing. To ensure data
consistency, we perform text preprocessing by retaining only
plain text while removing formatting elements and unneces-
sary content. Additionally, to mitigate encoding inconsisten-
cies, all text files are standardized to UTF-8 encoding, with
undecodable characters removed. To account for the structural
complexity of OSS and maintain dataset representativeness,
we employ a stratified sampling strategy. Specifically, we
classify the 791 OSS into 6 groups based on directory depth,
where a depth of 1 indicates all code files reside in the
root directory, while a depth of 6 represents projects with
extensive subdirectory nesting. From each group, we randomly
sample 25 OSS to capture a range of structural complexities,
facilitating a comprehensive evaluation of different methods
in handling intricate file organizations.
After data filtering, text preprocessing, and stratified sam-
pling, we construct a final dataset of 150 OSS, with an average
of 89 files per project and a total of 49,395 lines of code.
This dataset serves as the evaluation benchmark for RMGenie,
assessing its adaptability to varying project structures and
complexity levels.
2) Foundation LLM and Executor: This study employs
DeepSeek-R1 as the base LLM for RMGenie and conducts
comparative experiments to comprehensively evaluate its per-
formance. The executor component is responsible for interact-
ing with external APIs to retrieve relevant data. Specifically,
we utilize Python’s requests library to interface with the
GitHub REST API, enabling seamless access to repository
metadata and related information. Additionally, to facilitate
web search capabilities, we integrate Google Cloud’s Custom
Search JSON API, allowing the executor to query and retrieve
relevant search results efficiently.
B. Metrics
1) Human Evaluation: To comprehensively assess the qual-
ity and effectiveness of generated README files, we design
four evaluation criteria:
• Overall
satisfication.
Assesses
whether
the
generated
README meets user expectations in usefulness, logic, and
readability.
• Content completeness. Evaluates if the README ade-
quately covers core functionalities, installation, and contri-
bution guidelines.
• Factual accuracy. Evaluates the README correctly reflects
project functionality, APIs, and dependencies to prevent
misinformation.
510
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 6](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-06.png)

![Página PDF 6, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

• Instruction compliance. Checks if the README follows
user-specified requirements and formatting guidelines.
We conduct an anonymous evaluation with 10 experienced
software developers, who assess OSS README files gener-
ated by different models. Results are classified as win, tie, or
lose, where win indicates RMGenie outperforms the baseline,
tie denotes comparable quality, and lose signifies inferior
output. To ensure fairness and objectivity, evaluators possess
diverse expertise in technical writing, software engineering,
and open source contributions. In cases of disagreement, a
voting mechanism determines the outcome. If votes are evenly
split (e.g., win, tie, and loss each constituting one-third), the
README files are considered of equal quality, resulting in a
tie. This framework integrates multiple perspectives, reducing
individual bias and improving evaluation reliability.
2) Automated
Evaluation:
In
evaluating
RMGenie’s
README generation capability, we adopt the evaluation
methodology of SuperCLUE [30] and employ GPT-4o [31] as
the judge model. The model automatically scores README
files based on three dimensions: Overall preference, content
completeness, factual accuracy, and instruction compliance,
using a rating scale of 1 to 5. The evaluation covers 150
OSS, and the scores are normalized to ensure comparability
across
different
evaluation
criteria.
Specifically,
each
dimension’s score is normalized to the range of 0-1 using the
transformation:
s′
i = si −1
4
(9)
where si represents the original score for project i. The final
method score, denoted as Smethod, is computed by averaging the
three dimensions’ normalized scores and further normalizing
the result to a 100-point scale:
Smethod = P150
i=1
(ssatisficaition
i
+scompleteness
i
+saccuracy
i
+scompliance
i
)/4−1
4
(10)
This scoring framework provides a standardized evaluation,
ensuring consistency and objectivity in assessing the quality
of generated README files.
C. Experimental Setup
The experiments are conducted on a server running Ubuntu
5.15.0-78-generic, equipped with an Intel(R) Xeon(R) Plat-
inum 8463B CPU and two NVIDIA H800 80GB GPUs.
The software environment includes Python 3.10.13 and Torch
2.2.0.
D. Experimental Results and Analysis
In this section, we present the results of RMGenie ’s
evaluation of experiment datasets and answer the following
research questions:
• RQ1: How effective is RMGenie in README generation?
• RQ2: How do key components and different settings of
RMGenie influence its effectiveness?
• RQ3: What is the README generation performance of
RMGenie compared to the state-of-the-art techniques?
1) README Generation Performance: This section evalu-
ates RMGenie’s effectiveness in README generation. Built
on the DeepSeek-R1 model, RMGenie is compared against
five widely used LLMs, selected for their popularity among
developers. To systematically assess performance, we define
five customized requirements detailed as below, integrated into
the QUESTION component of the prompts in Figure 2, serving
as benchmarks for instruction adherence.
1. Generate a README for {repo name}.
2. Include a software description, installation guide, usage
instructions, features, and commands.
3. Add a disclaimer to the README for {repo name}.
4. Start with a feature list, providing short descriptions and
links to details. Ensure easy navigation with a table of contents
while keeping it concise.
5. Begin with a project overview, function details, and depen-
dencies. Include configuration steps, examples, customization
guidelines, and an FAQ section.
Given the token constraints in single-turn interactions with
LLMs, we prioritize the selection of the initial code files
and code snippets when processing lengthy code inputs.
The experimental setup involves five models—DeepSeek-R1
[32], [33], GPT-4o [31], ChatGLM4 [34], Qwen2.5 [35], and
Llama3.1 [36]—tasked with README generation. Addition-
ally, five distinct instruction variations, as depicted in Figure
2, are employed to evaluate the models’ capability in under-
standing and accommodating user-specific requirements. The
evaluation framework comprises four fine-grained assessment
dimensions: overall satisfaction, content completeness, factual
accuracy, and instruction compliance.
Table I shows that RMGenie surpasses direct LLM-based
README generation in both overall quality and detailed
metrics, with a significant edge in content completeness.
When a repository contains many files, direct LLM generation
is limited by token constraints, often resulting in missing
critical information. RMGenie overcomes this by enabling
multiple interactions with the repository, allowing it to handle
large, complex structures more effectively and produce more
comprehensive and accurate README files.
Table II presents the automated evaluation results con-
ducted by the judging model, comparing RMGenie with other
LLMs. The data indicates that DeepSeek-R1 achieves a final
score of 68.28, slightly lower than GPT-4o’s 69.33, while
ChatGLM4 (67.75), Qwen2.5 (64.41), and Llama3.1 (64.03)
obtain relatively lower scores. However, RMGenie, based on
DeepSeek-R1, demonstrates a significant improvement across
all evaluation dimensions, achieving a final score of 84.16,
which considerably surpasses all other models. Specifically,
RMGenie attains scores of 84.16 in overall satisfaction, 85.33
in content completeness, 83.66 in factual accuracy, and 83.5
in instruction compliance. These results suggest that RMGe-
nie exhibits a stronger overall capability in OSS README
generation, producing more comprehensive, accurate, and
instruction-compliant content.
511
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 7](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-07.png)

![Página PDF 7, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

TABLE I
COMPARISON OF RMGENIE AND LLMS ACROSS EVALUATION
DIMENSIONS
Dimension
Compared LLMs Win Tie Lose RMGenie Win
Overall
Satisfaction
DeepSeek-R1
90
59
1
60.00%
GPT-4o
91
58
1
60.67%
ChatGLM4
111
39
0
74.00%
Qwen2.5
114
36
0
76.00%
Llama3.1
117
33
0
78.00%
Content
Completeness
DeepSeek-R1
119
31
0
79.33%
GPT-4o
122
28
0
81.33%
ChatGLM4
124
26
0
82.66%
Qwen2.5
130
20
0
86.67%
Llama3.1
132
18
0
88.00%
Factual
Accuracy
DeepSeek-R1
99
51
0
66.00%
GPT-4o
93
55
2
62.00%
ChatGLM4
108
42
0
72.00%
Qwen2.5
121
29
0
80.67%
Llama3.1
115
35
0
76.67%
Instruction
Compliance
DeepSeek-R1
77
67
6
51.33%
GPT-4o
89
60
1
59.33%
ChatGLM4
106
44
0
70.67%
Qwen2.5
111
39
0
74.00%
Llama3.1
113
37
0
75.33%
TABLE II
AUTOMATED EVALUATION RESULTS OF RMGENIE AND OTHER LLMS
Model
Score
Overall
Satisfaction
Content
Completeness
Factual
Accuracy
Instruction
Compliance
DeepSeek-R1 68.28
68.16
67.5
67.66
69.83
GPT-4o
69.33
69.33
70.33
70.16
67.5
ChatGLM4
67.74
67.5
69.16
66.16
68.16
Qwen2.5
64.41
64.66
65.0
64.66
63.33
Llama3.1
64.03
63.83
64.33
63.33
64.66
RMGenie
84.33
84.83
85.33
83.66
83.5
Answer to RQ1: RMGenie excels at generating
README files, consistently surpassing direct LLM-
based methods across key metrics. It outperforms base-
lines significantly, especially in content completeness,
while also achieving higher overall satisfaction, factual
accuracy, and instruction compliance.
2) Ablation Study: To analyze the contribution of each
component to RMGenie’s effectiveness, we conduct experi-
ments focusing on its two components:ToA and reflexion.
(1) ToA component ablation study. This experiment compares
RMGenie with ToA and RMGenie without ToA, analyzing
the differences in the quality of generated README files
based on human and automated evaluation metrics. The results,
presented in Tables III and IV, illustrate the impact of ToA
across different evaluation dimensions, providing insights into
its contribution to README generation performance.
The experimental results show that the ToA component en-
hances the overall quality of README generation in RMGe-
nie. As presented in Table III, human evaluation indicates that
RMGenie with ToA achieves a win rate above 50% across all
dimensions, with Content Completeness and Factual Accuracy
TABLE III
HUMAN EVALUATION RESULTS OF TOA ABLATION STUDY
Method
Evaluation Dimension
Win
Tie
Win Rate
w/o ToA
Overall Satisfaction
86
64
57.33%
Content Completeness
90
60
60%
Factual Accuracy
90
60
60%
Instruction Compliance
84
66
56%
TABLE IV
AUTOMATIC EVALUATION RESULTS OF TOA ABLATION STUDY
Model
Final
Overall
Content
Factual
Instruction
Score Satisfaction Completeness Accuracy Compliance
w/o ToA
80.5
80.5
82.5
77.5
81.5
RMGenie 84.33
84.83
85.33
83.66
83.5
reaching 60%, suggesting its role in improving structure and
information accuracy. However, the overall advantage remains
modest. Table IV further confirms ToA’s impact, as RMGenie
with ToA outperforms its variant without it in all automatic
evaluation metrics. Notably, it improves the Final Score by
3.83 points, with the highest gain in Factual Accuracy (6.16
points), reinforcing ToA’s contribution to content reliability.
Additionally, the improvements in Content Completeness and
Instruction Compliance suggest that ToA helps standardize
README documentation, enhancing both clarity and adher-
ence to best practices.
(2) Reflexion component ablation study. We assess the
impact of reflexion by removing it, allowing the agent to return
erroneous text without correction and proceed unaffected. To
ensure fairness and stability, all models use a temperature of
0 during inference.
Table V shows that removing the reflexion component
reduces RMGenie’s performance across four key dimensions:
Overall Satisfaction, Content Completeness, Factual Accuracy,
and Instruction Compliance. Factual Accuracy is most af-
fected, with a win rate of 65.33%, underscoring reflexion’s
role in ensuring accuracy. The near-50% win rates for the other
dimensions suggest its contribution to content comprehensive-
ness. Table VI further confirms this, with the full RMGenie
model outperforming the ablated version in Final Score, Over-
all Satisfaction, Content Completeness, and Factual Accuracy.
Notably, Content Completeness rises from 82.5 to 85.33, and
Factual Accuracy improves from 81.33 to 83.66, highlighting
reflexion’s impact on both comprehensiveness and accuracy.
(3) Impact of evaluator parameter k. To evaluate the trade-
off between performance and computational cost in RMGenie,
we adjust the evaluator parameter k to control the number of
retained decision tree inference paths, balancing accuracy and
efficiency. The experiment sets k from 1 to 4 and analyzes
model performance in terms of human preference comparisons
and inference time. Here, k = 1 represents the baseline RM-
Genie model, and we gradually increase k, comparing human
preference scores and average inference time to examine its
impact on model effectiveness and computational overhead. To
ensure fairness, all models use the same inference parameters
512
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 8](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-08.png)

![Página PDF 8, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

TABLE V
HUMAN EVALUATION RESULTS OF REFLEXION ABLATION STUDY
Method
Evaluation Dimension
Win
Tie
Win Rate
w/o Reflexion
Overall Satisfaction
84
66
56%
Content Completeness
79
71
52.66%
Factual Correctness
98
52
65.33%
Instruction Compliance
84
66
56%
TABLE VI
AUTOMATIC EVALUATION RESULTS OF REFLEXION ABLATION STUDY
Model
Final
Overall
Content
Factual
Instruction
Score Satisfaction Completeness Accuracy Compliance
w/o Reflexion 83.08
83.66
82.5
81.33
84.83
RMGenie
84.33
84.83
85.33
83.66
83.5
and experimental data. Ultimately, overall satisfaction across
different k values serves as a reference for assessing the
balance between performance and efficiency.
Table VII shows that increasing the evaluator parameter
k improves RMGenie’s overall satisfaction but significantly
increases inference time. At k = 1, RMGenie achieves the
shortest inference time (58.6s), though no win rate data is
available. As k increases, the win rate rises from 18% (k = 2)
to 28.67% (k
= 4), indicating improved model quality.
However, inference time grows exponentially from 106.9s to
337.1s. Notably, at k = 4, despite the highest win rate, two
failures occur, suggesting diminishing returns. Thus, choosing
an optimal k requires balancing quality and computational cost
for different applications.
(4) Baseline model comparison with ToA and reflexion. In
addition to ToA and reflexion, we analyze the impact of differ-
ent baseline models on RMGenie’s generation performance.
The experimental results of Table VIII indicate that GPT-4o
and DeepSeek-R1 perform best in the README generation
task, achieving the highest final score of 84.62, the highest
overall satisfaction of 84.83, and the highest content complete-
ness of 85.33. This suggests that these models are more effec-
tive in generating structured and comprehensive documenta-
tion. In contrast, ChatGLM4, Qwen2.5, and LLama3.1 obtain
lower scores, with LLama3.1 achieving the lowest final score
of 79.12 and demonstrating the weakest performance in con-
tent completeness and factual accuracy. This indicates certain
limitations in producing high-quality README files. Overall,
GPT-4o and DeepSeek-R1 are more suitable for README
generation, while other models exhibit minor deficiencies in
content completeness and factual accuracy. These findings
highlight the significant impact of base model selection on
the final effectiveness of ToA and reflexion.
TABLE VII
INFERENCE TIME AND OVERALL SATISFACTION COMPARISON ACROSS
DIFFERENT k VALUES
k Value
Win
Tie
Loss
Win Rate
Avg. Inference Time (s)
k = 1
-
-
-
-
58.6
k = 2
28
122
0
18%
106.9
k = 3
38
112
0
25.33%
217.4
k = 4
43
105
2
28.67%
337.1
TABLE VIII
AUTOMATIC EVALUATION SCORES OF TOA AND REFLEXION WITH
DIFFERENT BASE MODELS
Base Model
Final
Overall
Content
Factual
Instruction
Score
Satisfaction
Completeness
Accuracy
Compliance
DeepSeek-R1 +
ToA + Reflexion
84.33
84.83
85.33
83.66
83.5
GPT-4o +
ToA + Reflexion
84.62
84.66
85.16
83.83
84.83
ChatGLM4 +
ToA + Reflexion
80.49
80.16
80.5
79.83
81.5
Qwen2.5 +
ToA + Reflexion
81.62
81.83
82.00
80.83
81.83
LLama3.1 +
ToA + Reflexion
79.12
79.16
78.5
79.66
79.16
Answer to RQ2: Ablation studies reveal that ToA
and reflexion significantly enhance RMGenie’s per-
formance, particularly in content completeness and
factual accuracy. Removing ToA or reflexion reduces
overall quality, especially factual accuracy. Increasing
k improves performance but also raises computational
costs, requiring a trade-off. GPT-4o and DeepSeek-R1
outperform other models, emphasizing the importance
of baseline model selection.
3) Comparison with Other Methods: In this section, we
compare RMGenie with several state-of-the-art methods and
their variants. We compare PromptCS, LARCH, and RepoA-
gent, three methods designed for repository-level README
generation. PromptCS employs a dual-model architecture,
generating prompts to guide the LLM in code summarization.
LARCH uses gradient boosting trees to extract representative
code snippets, capturing key information. RepoAgent con-
structs a project hierarchy using deep recursion and abstract
syntax trees, executing a single interaction. To ensure fairness,
all methods use DeepSeek-R1 as the baseline model with
identical hyperparameters, while other configurations remain
at their default settings. For RMGenie, we adopt the first
prompt instruction from Figure 2 and set k = 2 as the
evaluator parameter. Since these methods do not support user-
customized requirements, instruction compliance is excluded
from the evaluation criteria.
Table IX presents the human evaluation results, demon-
strating that RMGenie outperforms PromptCS, LARCH, and
RepoAgent in overall satisfaction, content completeness, and
factual accuracy. In human assessments, RMGenie achieves
513
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 9](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-09.png)

![Página PDF 9, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

TABLE IX
HUMAN EVALUATION COMPARISON OF RMGENIE VS OTHER README
GENERATION METHODS
Evaluation Dimension
Compared Methods
Win
Tie
Loss
RMGenie Win
Overall Satisfaction
PromptCS
114
36
0
76%
LARCH
95
49
6
63.33%
RepoAgent
88
57
5
58.67%
Content Completeness
PromptCS
119
31
0
79.33%
LARCH
110
40
0
73.33%
RepoAgent
104
46
0
69.33%
Factual Accuracy
PromptCS
109
41
0
72.67%
LARCH
99
51
0
66%
RepoAgent
95
55
0
63.33%
TABLE X
AUTOMATIC EVALUATION COMPARISON OF RMGENIE AND OTHER
README GENERATION METHODS
Method
Final
Overall
Content
Factual
Score
Satisfaction
Completeness
Accuracy
PromptCS
62.94
61.83
60.83
66.16
LARCH
71.64
71.44
71.83
71.66
RepoAgent
73.55
73.66
74.16
72.83
RMGenie
84.38
84.16
85.33
83.66
a win rate exceeding 58% across all three dimensions, with
content completeness reaching the highest win rate of 79.33%
compared to PromptCS. This indicates that RMGenie more
effectively captures the functional and key information of
the code. In contrast, other methods exhibit varying degrees
of content loss or missing information, which negatively
impacts the quality of the generated README. The automatic
evaluation results in Table X further validate RMGenie’s
superiority, as it achieves the highest final score of 84.38,
surpassing all other methods. RMGenie consistently attains
the best scores in overall satisfaction, content completeness,
and factual accuracy, confirming its ability to generate more
comprehensive and accurate README documentation. In
comparison, PromptCS, LARCH, and RepoAgent demonstrate
limited effectiveness in these aspects.
Answer to RQ3: RMGenie outperforms state-of-the-
art methods in README generation, achieving the
highest scores in overall satisfaction, content complete-
ness, and factual accuracy. With a 79.33% win rate
in content completeness and a final score of 84.38, it
surpasses all baselines, demonstrating its ability to gen-
erate more comprehensive and accurate documentation.
V. RELATED WORK
Automatically generating README files for OSS enhances
development efficiency and ensures software consistency.
Several existing tools, including Readme-AI [37], Readme-
md-generator [38], REGEN [39], and GPT4Reliability [40],
provide varying levels of support for this task. Specifically,
Readme-AI is a developer tool that leverages data extraction
and generative AI to produce structured README files,
incorporating elements such as code documentation, directory
structures, file summaries, installation guides, and contribution
instructions. Readme-md-generator is a command-line utility
that generates README files by extracting metadata from
a project’s package.json and git configuration, enabling rapid
documentation creation. REGEN assists developers in crafting
comprehensive README files by combining template-based
generation with user input, facilitating structured documen-
tation that covers project overviews, installation steps, usage
guidelines, and contribution policies. It supports multiple
output formats and customization options to accommodate
diverse project requirements. GPT4Reliability employs GPT-
4 to generate software documentation, accurately capturing
project features, setup procedures, and usage instructions while
integrating with various development environments and offer-
ing customization to align with specific project needs.
Existing tools simplify documentation workflows but have
key limitations. They rely on metadata, lack deep code un-
derstanding, and produce generic README that often require
manual refinement. Limited code analysis and missing multi-
language support further restrict their applicability. In contrast,
RMGenie uses an LLM-based agent for deep semantic anal-
ysis, optimizing decision paths with ToA for better document
structure and clarity. Its reflexion mechanism enables self-
correction and refinement, while agent-driven multi-language
processing ensures comprehensive, continuously updated doc-
umentation that stays synchronized with evolving repositories.
VI. THREATS TO VALIDITY
A. Internal Validity
The choice of model parameters poses a potential threat to
validity. RMGenie’s performance depends on the number of
optimal paths retained in the ToA model. While our experi-
ments analyze the trade-offs between settings, computational
cost, and document quality, the limited number of evaluators
restricts large-scale trend analysis, making it difficult to deter-
mine the optimal balance. Additionally, RMGenie’s prompt
design may not be fully optimized, as we reference exist-
ing frameworks but do not systematically compare multiple
prompt designs, potentially affecting output consistency.
B. External Validity
RMGenie relies on LLMs and external tools for knowledge
retrieval, which may introduce inaccurate or unreliable con-
tent. As it is based on an open source, large-scale pretrained
model without fine-tuning, existing automated evaluation met-
rics may not fully capture its documentation quality. Con-
sequently, human evaluation remains the primary assessment
method. However, the limited number of evaluators constrains
the sample size, potentially affecting result generalizability.
Additionally, evaluator biases may impact the broader appli-
cability and adoption of RMGenie.
514
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 10](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-10.png)

![Página PDF 10, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

VII. CONCLUSION
In this study, we propose RMGenie, an LLM-based frame-
work for automated README generation in OSS. RMGenie
employs an LLM-based agent for OSS analysis, extracting
structural and contextual information to ensure comprehen-
sive documentation. It introduces the ToA model for dy-
namic reasoning, optimizing README structure beyond static
prompt-based methods. The reflexion mechanism further en-
hances adaptability by refining decisions and correcting errors,
improving accuracy and completeness. Evaluations on 150
GitHub OSS show that RMGenie outperforms mainstream
LLMs and tools across multiple metrics, delivering superior
documentation quality. Additionally, we develop a VSCode
plugin to integrate RMGenie into development workflows,
improving efficiency and maintaining documentation consis-
tency. These contributions establish RMGenie as an effective,
adaptive, and scalable solution for README generation in
complex OSS ecosystems.
VIII. ACKNOWLEDGEMENT
This paper is supported by the the Strategic Priority Re-
search Program of the Chinese Academy of Sciences under
No. XDA0320401, the National Natural Science Foundation
of China under No. 62202457, and the Open Source Commu-
nity Software Bill of Materials (SBOM) Platform under No.
E3GX310201. This paper is also supported by YuanTu Large
Research Infrastructure.
REFERENCES
[1] J. Ghofrani, P. Heravi, K. A. Babaei, and M. D. Soorati, “Trust
challenges in reusing open source software: An interview-based initial
study,” in Proceedings of the 26th ACM international systems and
software product line conference-volume B, 2022, pp. 110–116.
[2] T. Dey, A. Karnauch, and A. Mockus, “Representation of developer ex-
pertise in open source software,” in 2021 IEEE/ACM 43rd International
Conference on Software Engineering (ICSE).
IEEE, 2021, pp. 995–
1007.
[3] L. Boughton, C. Miller, Y. Acar, D. Wermke, and C. K¨astner, “De-
composing and measuring trust in open-source software supply chains,”
in Proceedings of the 2024 ACM/IEEE 44th International Conference
on Software Engineering: New Ideas and Emerging Results, 2024, pp.
57–61.
[4] R. Tang, Y.-N. Chuang, and X. Hu, “The science of detecting llm-
generated text,” Communications of the ACM, vol. 67, no. 4, pp. 50–59,
2024.
[5] T. T. Doan, P. T. Nguyen, J. Di Rocco, and D. Di Ruscio, “Too
long; didn’t read: Automatic summarization of github readme. md with
transformers,” in Proceedings of the 27th International Conference on
Evaluation and Assessment in Software Engineering, 2023, pp. 267–272.
[6] A. Kelley and D. Garijo, “A framework for creating knowledge graphs
of scientific software metadata,” Quantitative Science Studies, vol. 2,
no. 4, pp. 1423–1446, 2021.
[7] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,
C. Wang, Y. Wang et al., “A survey on evaluation of large language
models,” ACM transactions on intelligent systems and technology,
vol. 15, no. 3, pp. 1–45, 2024.
[8] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
models to follow instructions with human feedback,” Advances in neural
information processing systems, vol. 35, pp. 27 730–27 744, 2022.
[9] X. Hou, Y. Zhao, Y. Liu, Z. Yang, K. Wang, L. Li, X. Luo, D. Lo,
J. Grundy, and H. Wang, “Large language models for software engi-
neering: A systematic literature review,” ACM Transactions on Software
Engineering and Methodology, vol. 33, no. 8, pp. 1–79, 2024.
[10] K. Jin, C.-Y. Wang, H. V. Pham, and H. Hemmati, “Can chatgpt support
developers? an empirical evaluation of large language models for code
generation,” in Proceedings of the 21st International Conference on
Mining Software Repositories, 2024, pp. 167–171.
[11] X. Du, M. Liu, K. Wang, H. Wang, J. Liu, Y. Chen, J. Feng, C. Sha,
X. Peng, and Y. Lou, “Evaluating large language models in class-level
code generation,” in Proceedings of the IEEE/ACM 46th International
Conference on Software Engineering, 2024, pp. 1–13.
[12] W. Sun, C. Fang, Y. You, Y. Chen, Y. Liu, C. Wang, J. Zhang, Q. Zhang,
H. Qian, W. Zhao et al., “A prompt learning framework for source code
summarization,” arXiv preprint arXiv:2312.16066, 2023.
[13] Y. Koreeda, T. Morishita, O. Imaichi, and Y. Sogawa, “Larch: Large
language model-based automatic readme creation with heuristics,” in
Proceedings of the 32nd ACM International Conference on Information
and Knowledge Management, 2023, pp. 5066–5070.
[14] Q. Luo, Y. Ye, S. Liang, Z. Zhang, Y. Qin, Y. Lu, Y. Wu, X. Cong,
Y. Lin, Y. Zhang et al., “Repoagent: An llm-powered open-source
framework for repository-level code documentation generation,” arXiv
preprint arXiv:2402.16667, 2024.
[15] M. Gaughan, K. Champion, S. Hwang, and A. Shaw, “The introduction
of readme and contributing files in open source software development,”
arXiv preprint arXiv:2502.18440, 2025.
[16] H. Gao, C. Treude, and M. Zahedi, “Evaluating transfer learning for
simplifying github readmes,” in Proceedings of the 31st ACM Joint
European Software Engineering Conference and Symposium on the
Foundations of Software Engineering, 2023, pp. 1548–1560.
[17] W. Yang, X. Bi, Y. Lin, S. Chen, J. Zhou, and X. Sun, “Watch out for
your agents! investigating backdoor threats to llm-based agents,” Ad-
vances in Neural Information Processing Systems, vol. 37, pp. 100 938–
100 964, 2024.
[18] Y. Guan, D. Wang, Z. Chu, S. Wang, F. Ni, R. Song, and C. Zhuang,
“Intelligent agents with llm-based process automation,” in Proceedings
of the 30th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, 2024, pp. 5018–5027.
[19] C. S. Xia, Y. Deng, S. Dunn, and L. Zhang, “Agentless: De-
mystifying llm-based software engineering agents,” arXiv preprint
arXiv:2407.01489, 2024.
[20] X. Huang, W. Liu, X. Chen, X. Wang, H. Wang, D. Lian, Y. Wang,
R. Tang, and E. Chen, “Understanding the planning of llm agents: A
survey,” arXiv preprint arXiv:2402.02716, 2024.
[21] S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and
K. Narasimhan, “Tree of thoughts: Deliberate problem solving with large
language models,” Advances in neural information processing systems,
vol. 36, pp. 11 809–11 822, 2023.
[22] S. Mo and M. Xin, “Tree of uncertain thoughts reasoning for large
language models,” in ICASSP 2024-2024 IEEE International Conference
on Acoustics, Speech and Signal Processing (ICASSP).
IEEE, 2024,
pp. 12 742–12 746.
[23] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao, “Reflex-
ion: Language agents with verbal reinforcement learning,” Advances in
Neural Information Processing Systems, vol. 36, pp. 8634–8652, 2023.
[24] X. Bo, Z. Zhang, Q. Dai, X. Feng, L. Wang, R. Li, X. Chen, and J.-
R. Wen, “Reflective multi-agent collaboration based on large language
models,” Advances in Neural Information Processing Systems, vol. 37,
pp. 138 595–138 631, 2024.
[25] A. Zhao, D. Huang, Q. Xu, M. Lin, Y.-J. Liu, and G. Huang, “Expel: Llm
agents are experiential learners,” in Proceedings of the AAAI Conference
on Artificial Intelligence, vol. 38, no. 17, 2024, pp. 19 632–19 642.
[26] K. Wang, M. Yan, H. Zhang, and H. Hu, “Unified abstract syntax
tree representation learning for cross-language program classification,”
in Proceedings of the 30th IEEE/ACM International Conference on
Program Comprehension, 2022, pp. 390–400.
[27] P. Denny, V. Kumar, and N. Giacaman, “Conversing with copilot:
Exploring prompt engineering for solving cs1 problems using natural
language,” in Proceedings of the 54th ACM technical symposium on
computer science education V. 1, 2023, pp. 1136–1142.
[28] Z. Yun-tao, G. Ling, and W. Yong-cheng, “An improved tf-idf approach
for text classification,” Journal of Zhejiang University-Science A, vol. 6,
no. 1, pp. 49–55, 2005.
[29] M. Renze and E. Guven, “Self-reflection in llm agents: Effects on
problem-solving performance,” arXiv preprint arXiv:2405.06682, 2024.
[30] L. Xu, A. Li, L. Zhu, H. Xue, C. Zhu, K. Zhao, H. He, X. Zhang,
Q. Kang, and Z. Lan, “Superclue: A comprehensive chinese large
language model benchmark,” arXiv preprint arXiv:2307.15020, 2023.
515
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 11](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-11.png)

![Página PDF 11, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

[31] OpenAI, “Gpt-4o,” 2022, https://openai.com/index/hello-gpt-4o/.
[32] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma,
P. Wang, X. Bi et al., “Deepseek-r1: Incentivizing reasoning capability
in llms via reinforcement learning,” arXiv preprint arXiv:2501.12948,
2025.
[33] DeepSeek,
“Deepseek-r1,”
2025,
https://github.com/deepseek-
ai/DeepSeek-R1.
[34] ZHIPUAI, “Glm-4,” 2025, https://github.com/THUDM/GLM-4.
[35] Qwen, “Qwen,” 2025, https://github.com/QwenLM/Qwen2.5.
[36] Llama, “Llama3.1,” 2025, https://ollama.com/library/llama3.1.
[37] readme ai, “readme-ai,” 2025, https://readme-ai.streamlit.app/.
[38] R.
md
generator,
“Readme-md-generator,”
2025,
https://github.com/kefranabg/readme-md-generator.
[39] REGEN, “Regen,” 2025, https://github.com/ivanleech/REGEN.
[40] GPT4Readability,
“Gpt4readability,”
2025,
https://github.com/loevlie/GPT4Readability/tree/main?source=postpage−
−−−−4bb5f12e85b2 −−−−−−−−−−−−−−−−−
−−−−−−−−.
516
Authorized licensed use limited to: b-on: UNIVERSIDADE DO PORTO. Downloaded on March 25,2026 at 12:02:36 UTC from IEEE Xplore.  Restrictions apply.

[Vista original de la página 12](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-12.png)

![Página PDF 12, representación visual original](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RMGenie/page-12.png)
