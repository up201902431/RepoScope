# FeatLens: Feature-Guided Dependency Retrieval for Repository-Level Code Generation

- source_pdf: ../../../../../pdf/Same%20Solution/fourth/FeatLens.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

FeatLens: Feature-Guided Dependency Retrieval for
Repository-Level Code Generation
XUTIAN LI, Peking University, China
BO XIONG, Peking University, China
YIFENG ZHU, Peking University, China
RUNBANG YAN, Peking University, China
YANZHEN ZOU, Peking University, China
LU ZHANG, Peking University, China
BING XIE, Peking University, China
Retrieving task-relevant code dependencies is critical for repository-level code generation. Existing approaches
obtain dependency context through similarity-based retrieval, repository graphs, or LLM-driven exploration.
A central challenge is to identify the dispersed dependencies needed to implement a functional requirement,
rather than merely retrieve broadly related code. This paper presents FeatLens, a feature-guided dependency
retrieval approach for repository-level code generation. FeatLens first builds an offline index linking natural-
language feature descriptions to function-level code entities. Given a task requirement and target function
location, it selects relevant features and constructs dependency seeds. It then expands the seed graph and
applies semantic and structural heuristics to select dependencies for inclusion in the generation context.
Experiments on DevEval and EvoCodeBench show that FeatLens achieves the highest dependency recall
among the evaluated baselines at each fixed retrieval budget, reaching DR@15 values of 0.527 and 0.529,
respectively. On DevEval, the retrieved context supports the highest non-oracle Pass@1 with both DeepSeek-
V3.2 and GPT-5-mini. These results are obtained without LLM calls in the online dependency retrieval stage.
CCS Concepts: • Software and its engineering →Software functional properties; Software mainte-
nance tools; • Computing methodologies →Machine learning; Natural language processing; Knowledge
representation and reasoning.
Additional Key Words and Phrases: repository-level code generation, retrieval-augmented generation, code
graph, feature-guided retrieval
1
Introduction
Recent advances in large language models (LLMs) have shifted code generation research from
isolated function-level completion tasks [2, 51] toward repository-level generation [12, 26, 27, 50].
Repository-level code generation requires an LLM not only to locate the code to be modified,
but also to track its call relations, code dependencies, data constraints, and cross-file semantic
links throughout the repository. The absence of such global relational context often leads to par-
tial modifications, logic bugs, and violations of the system’s existing architecture. Consequently,
capturing repository-wide code dependencies is the key to improving repository-level code genera-
tion [24, 31, 55].
Existing work mainly follows two directions. The first direction retrieves relevant code directly
from repositories. Representative approaches either embed source code for similarity-based re-
trieval [52] or build structured representations, such as code context graphs and call-chain-aware
graphs, to capture relationships among program entities [33, 35, 45]. They then retrieve candidate
context through embedding search, graph expansion, or structure-aware reranking. The second
direction adopts agent-driven exploration. Starting from the task description, LLM agents iteratively
inspect code, invoke tools, and, when available, leverage execution or test feedback to discover
Contact: Xutian Li, xtli25@stu.pku.edu.cn.
arXiv:2609.26480v2  [cs.SE]  28 Oct 2026

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

2
Li et al.
Task (mrjob.hadoop.HadoopJobRunner._stream_history_log_dirs)
Task Description: Iterate over deduplicated log directories, yielding each as a history log search path.
Ours (FeatLens)
[Intermediate Output] Search_Terms (5): job.xml, getJobHistoryDir,
log.debug, FileSystem.exists, log.info
[Final Output] Search Results (15):  
mrjob.sim.ls
mrjob.logs.mixin._stream_history_log_dirs
mrjob.pool.debug
mrjob.tools.diagnose.info
mrjob.fs.base.Filesystem
mrjob.spark.runner.CompositeFilesystem
mrjob.spark.runner.GCSFilesystem
mrjob.spark.runner.S3Filesystem
mrjob.logs.mixin.LogInterpretationMixin
……(omit 4)
mrjob.fs.s3.S3Filesystem.md5sum
mrjob.runner.can_handle_path
UniXCoder Retrieval
[Final Output] Search Results (14):
mrjob.logs.mixin.LogInterpretationMixin._stream_history_l
og_dirs
mrjob.logs.mixin.LogInterpretationMixin._ls_history_logs
mrjob.logs.history._ls_history_logs
mrjob.hadoop.HadoopJobRunner._stream_task_log_dirs
mrjob.hadoop.HadoopJobRunner._hadoop_dirs
……(omit 7)
mrjob.logs.history._match_history_log_path
mrjob.fs.hadoop.HadoopFilesystem.__init__
RepoGraph Retrieval
CodexGraph Retrieval
[Intermediate Output] Cypher Query: 
MATCH (mod:MODULE {name: 'mrjob.hadoop'})
-[:CONTAINS]-> (cls:CLASS {name: 'HadoopJobRunner'})
-[:HAS_METHOD|HAS_FIELD|INHERITS]-> (n)
RETURN cls.name, n
[Final Output] Search Results (26):  
mrjob.hadoop._hadoop_log_dirs
mrjob.hadoop.fs
mrjob.hadoop.counters
mrjob.hadoop._stream_task_log_dirs
mrjob.hadoop._stream_history_log_dirs
mrjob.hadoop._manifest_download_commands
……(omit 18)
mrjob.hadoop._default_opts
mrjob.hadoop.__init__
[Intermediate Output] Entities in Seed Graph (15): 
{Shown in the yellow region on the left.}
[Intermediate Output] Entities in Expanded Graph (35):
{Shown in the whole figure above.} 
[Final Output] Search Results (16):  
{Shown in the green region on the right.}
mrjob.util.unique
mrjob.hadoop.HadoopJobRunner._hadoop_log_dirs
mrjob.hadoop.HadoopJobRunner.fs
mrjob.logs.mixin.LogInterpretationMixin._read_logs
mrjob.logs.wrap._logs_exist
mrjob.hadoop.log
mrjob.hadoop.HadoopJobRunner._hadoop_dirs
mrjob.logs.history._match_history_log_path
……(omit 6)
mrjob.logs.history._pre_yarn_history_unescape
mrjob.logs.mixin.LogInterpretationMixin._ls_history_logs
Ground Truth
mrjob.hadoop.HadoopJobRunner._hadoop_log_dirs
mrjob.hadoop.HadoopJobRunner.fs
mrjob.hadoop.log
mrjob.logs.mixin.LogInterpretationMixin._read_logs
mrjob.logs.wrap._logs_exist
mrjob.util.unique
P=0.0%, DR=0.0%
P=7.7%, DR=33.3%
P=14.3%, DR=33.3%
P=37.5%, 
DR=100.0%
P=26.7%, 
DR=66.7%
P=17.1%, 
DR=100.0%
Inappropriate 
search terms!
Query with too 
narrow scope!
Fig. 1. A motivating example of dependency retrieval for a history-log directory task in Mrjob. P and DR
denote precision and dependency recall, respectively.
relevant implementation contexts [4, 49, 54]. Both directions substantially improve repository-level
code generation by providing richer contextual information than isolated code completion.
Despite these advances, connecting functional requirements to dispersed implementation de-
pendencies remains challenging. Code that is semantically similar to a requirement may omit
supporting interfaces, while repository structure alone does not determine which dependencies are
needed for implementation. Work on graph-based RAG has highlighted that pre-built structures
may not align with the reasoning needs of individual queries [7]. Agent-driven exploration offers
a flexible alternative, but incurs online interaction costs through multi-step LLM reasoning [16].
Errors can also propagate across successive reasoning and tool-use steps, potentially derailing
the exploration [48]. These observations motivate an approach that uses functional organization
to identify dependency candidates and combines semantic and structural heuristics to construct
task-specific dependency context for implementation, without online LLM exploration.
To this end, this paper proposes FeatLens, a feature-guided dependency retrieval approach
for repository-level code generation. The basic idea of FeatLens is to use features as a bridge
connecting developers’ task requirements to the target code and its dependencies. It establishes a
bidirectional mapping between functional features and the repository code. Specifically, FeatLens
first produces a hierarchical functional summary of the repository and constructs a systematic
index that links natural-language feature descriptions to function-level code entities. Then, upon
receiving a generation task, it automatically matches relevant features, performs dependency
seeding, expands the dependency context, and refines it through semantic-structural scoring and
personalized PageRank. Finally, the refined dependency context is provided to the LLM to support
code generation.
We evaluate dependency retrieval on DevEval [27] and EvoCodeBench [26] and downstream func-
tion generation on DevEval using two LLMs. Compared with UniXcoder RAG, FeatLens improves
DR@15 by 11.2 percentage points on DevEval and 17.4 percentage points on EvoCodeBench. On
DevEval, it achieves the highest reported Pass@1 among non-oracle methods, reaching 42.24% with
DeepSeek-V3.2 and 55.03% with GPT-5-mini, while producing the shortest code under both models.
These results are obtained without online LLM retrieval calls. Component analysis shows that

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

FeatLens
3
our feature index and feature-heuristic reranking (FeatHeur) mechanism can improve dependency
retrieval over other settings.
The main contributions of this paper are as follows:
• We propose FeatLens, a feature-guided dependency retrieval approach for repository-level
code generation that uses a feature-to-function index to connect task requirements with
repository dependencies and construct dependency context on demand.
• We present a semantic–structural dependency context refinement approach that combines
code semantics and seed-derived structural signals through personalized PageRank to select
a bounded dependency context.
• We conduct an empirical evaluation on DevEval and EvoCodeBench showing higher depen-
dency recall than the evaluated baselines, together with the highest non-oracle Pass@1 and
shortest generated completions on DevEval under both generation models, without online
LLM retrieval calls.
2
Background and Motivation
More recently, features have been treated as a useful unit for organizing and implementing user
requirements. For example, EvoDev [32] decomposes user requirements into features and coor-
dinates their implementation through dependency-aware planning, enabling design knowledge
and business logic to propagate across development iterations. FeatX [30] takes a feature-editing
perspective for repository-level code evolution by translating feature edits into code patches. These
studies indicate that feature-level abstraction can provide useful guidance for repository-level
development beyond isolated code fragments.
2.1
Feature-Guided Dependency Retrieval
Repository-level code generation tasks require a model to implement a target function within
an existing repository. Such tasks are typically specified as functional requirements, yet correct
implementations depend on task-relevant repository context, including existing functions, APIs,
and data definitions. Following requirements-engineering terminology [10], we use feature to
denote the functional unit described by a requirement. Operationally, we represent a feature as
an automatically identified cluster of structurally and semantically related functions paired with
a natural-language summary, using this representation as a code-derived approximation of a
functional unit. These indexed features serve as retrieval anchors that connect natural-language
task intent to reusable repository code.
Let 𝑅denote a repository, 𝐶𝑅denote its code entities, and 𝐿𝑅denote the structural relations
among these entities. Code entities include functions, classes, files, and variables. Structural relations
include calls, definitions, uses, containment, and imports. We associate 𝑅with a set of functional
features 𝐹𝑅= {𝑓1, . . . , 𝑓𝑛}, where each feature 𝑓𝑖has a textual description 𝑑𝑖and is supported by a
subset of code entities 𝐶𝑖⊆𝐶𝑅.
Given a requirement 𝑞and a target function location 𝑡, feature-guided dependency retrieval aims
to identify a compact dependency context 𝐷𝑞,𝑡= (𝑉𝑞,𝑡, 𝐸𝑞,𝑡), where 𝑉𝑞,𝑡⊆𝐶𝑅contains reusable
entities and 𝐸𝑞,𝑡⊆𝐿𝑅preserves their structural constraints for generation. Unlike conventional
code search, the desired output is not merely code that is textually similar to 𝑞, but the dependencies
that should be reused or respected during implementation. This requires aligning 𝑞with repository
features, recovering structural dependencies that may be lexically indirect, and avoiding excessive
irrelevant context. The following example illustrates why existing retrieval strategies struggle with
this formulation.

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

4
Li et al.
2.2
Motivation and Challenges
Figure 1 illustrates dependency retrieval for implementing _stream_history_log_dirs in Mr-
job’s HadoopJobRunner. The task is to yield existing history-log directories while respecting the
log-reading policy and removing duplicates. Correct implementation depends not only on log-
directory routines, but also on cross-file helpers such as unique for deduplication and _logs_exist
for existence checks through the repository’s filesystem interface. This example highlights two
challenges.
Challenge 1: Bridging task intent and dispersed implementation dependencies. Requirements de-
scribe a functional goal, whereas the code supporting that goal is distributed across files and
abstraction levels. Similarity-based retrieval may favor history-log parsers or similarly named
methods over supporting helpers whose names do not express their role in log discovery. Likewise,
graph exploration centered on HadoopJobRunner can locate relevant methods without recovering
the cross-file implementations they reuse. The difficulty is therefore to connect task intent to the
entities that jointly support the requested behavior, rather than to code that merely shares its topic
or location. A feature-level representation offers a useful retrieval anchor: the log-discovery feature
groups directory-enumeration routines with reusable helpers, making their functional association
explicit beyond lexical similarity and class boundaries.
Challenge 2: Preserving task-critical dependencies under a bounded context budget. A relevant
feature provides an entry point, not a complete dependency context. Structural expansion can
recover additional supporting interfaces, but it also introduces code from neighboring workflows
that the target task does not require. Restricting the context by semantic similarity alone risks
discarding generic yet necessary helpers; retaining the entire neighborhood exposes the generator
to unnecessary code. The challenge is to distinguish task-critical dependencies from broadly related
candidates while balancing coverage and context size. This requires considering both semantic
relevance and structural relationships, rather than treating either as sufficient evidence of usefulness.
These challenges motivate FeatLens’s combination of feature-guided dependency seeding and
semantic–structural context refinement. Section 4.5 revisits this example to examine how the
retrieved interfaces relate to generation outcomes, and contrasts it with a case where refinement
removes a required dependency.
3
Approach
Figure 2 presents an overview of FeatLens, whose core method consists of three stages before
code generation. First, FeatLens builds a feature-oriented repository index from the source reposi-
tory. Second, given a task description and target function location, it performs feature retrieval
and dependency seeding using the feature index. Third, it performs dependency expansion and
semantic-structural dependency context refinement, producing a task-specific dependency graph.
The resulting dependency graph provides context for downstream code generation.
3.1
Feature-Oriented Repository Indexing
The first stage builds an offline feature index that maps natural-language feature descriptions
to function-level code entities. FeatLens adapts the feature-oriented repository summarization
procedure proposed by Zhu et al. [58], but uses the resulting feature structure as a retrieval index
rather than as repository documentation.
Given a repository 𝑅, FeatLens first analyzes the repository from both structural and semantic
perspectives. Structural static analysis extracts code entities (functions, classes, and files) and

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

FeatLens
5
Task Requirement
Semantic 
Scoring
③Semantic-Structural 
Dependency Context Refinement
②Feature Retrieval     & 
& Dependency Seeding
Score 
Fusion
Structural 
Scoring
Personalized 
PageRank
Dependency 
Expansion
Top-𝑲𝑲 
Selection
Task-Specific
Dependency Graph
FeatHeur 
Reranking
Similarity
Computation
Top-𝒏𝒏 Feature
Selection
Dependency 
Seeds
Code Generation
Code Patch
①Feature-Oriented Repository Indexing
Code Repository
Feature Index
Feature Summarization
Static Analysis
Semantic Analysis
Hierarchical Clustering
update
Task Description 𝑞𝑞
Target Func. Location 𝑡𝑡
Legend  |   Bold = Operation  |  Regular = Data Artifact  |         = Input  |         = Output
Fig. 2. Overview of FeatLens. An offline feature index guides online dependency seeding, expansion, and
semantic–structural refinement to construct context for code generation.
records lightweight structural relations (calls and imports) using ENRE. Semantic analysis rep-
resents each function according to its implementation semantics using lightweight descriptions
and embeddings. These structural relations capture coarse interactions among entities, while the
semantic representations capture what functionality they provide.
To organize repository functions into feature-level groups, FeatLens applies hierarchical cluster-
ing based on the structural and semantic information extracted above. Specifically, it uses Leiden
community detection to first group files and then cluster functions within each file group using
fused semantic and structural similarities. Each resulting function cluster is summarized by an LLM
into a natural-language feature description and linked to its constituent functions, yielding the
feature index:
I𝑅= {𝑓𝑖}𝑀
𝑖=1 = {(𝑑𝑖,𝐶func
𝑖
)}𝑀
𝑖=1,
(1)
where 𝑓𝑖denotes the 𝑖-th feature, 𝑑𝑖is its natural-language description, and 𝐶func
𝑖
denotes the
subset of code entities associated with this feature at the function granularity. This feature-to-
function index serves as the basis for feature-guided retrieval in the next stage.
3.2
Feature Retrieval and Dependency Seeding
The second stage retrieves relevant features from the offline index and constructs a task-specific
seed graph from their associated functions. Given a task description 𝑞, comprising the functional
requirement and parameter descriptions, and the target function location 𝑡, FeatLens first retrieves
feature clusters whose descriptions are semantically aligned with the task. For each indexed feature
𝑓𝑖= (𝑑𝑖,𝐶func
𝑖
), FeatLens computes:
sim(𝑞,𝑑𝑖) = cos (𝜙(𝑞),𝜙(𝑑𝑖)) .
(2)

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

6
Li et al.
Ranking features solely by description similarity may retrieve features that are textually close to
the task but weakly connected to the target location. FeatLens therefore applies feature-heuristic
reranking (FeatHeur) during dependency seeding to prioritize the feature associated with the target
function. The target function’s namespace identifies the feature cluster containing it, denoted
by 𝑓𝑡, in the stored index. When available, 𝑓𝑡is ranked first, followed by the remaining features
in descending order of semantic similarity. Equivalently, clusters are ordered by the following
descending lexicographic key:
key(𝑞, 𝑓𝑖,𝑡) =  1[𝑓𝑖= 𝑓𝑡], sim(𝑞,𝑑𝑖).
(3)
Notably, FeatLens operates on a repository in which the target function body is replaced with a
pass statement before feature indexing. Consequently, both index construction and subsequent
feature lookup have access only to the target function’s signature and placeholder body, not its
original implementation. After FeatHeur reranking, FeatLens selects the top 𝑛= 3 feature clusters
to form F𝑞and collects their function entities as the dependency seeds:
𝑆𝑞=
Ø
𝑓𝑖∈F𝑞
𝐶func
𝑖
.
(4)
FeatLens constructs a directed seed graph 𝐺0 = (𝑉0, 𝐸0) from the selected functions, with 𝑉0 = 𝑆𝑞.
It matches these functions to ENRE entities using normalized qualified names and forms 𝐸0 from
the structural relations connecting pairs of seed nodes. This seed graph links the feature-guided
dependency seeds through their structural relations and serves as the starting point for dependency
expansion.
3.3
Semantic–Structural Dependency Context Refinement
FeatLens expands the seed graph 𝐺0 to recover dependencies beyond the selected features. From
each seed function, it follows outgoing Call, Use, and Contain relations to function entities
and incoming Call relations to callers, then adds the defining classes of all retained functions
through incoming Define relations. Let 𝑁func(𝑉0) denote these function neighbors and 𝐶owner(𝑉)
the defining classes of functions in 𝑉. The expanded graph 𝐺𝑒= (𝑉𝑒, 𝐸𝑒) is constructed as:
𝑉𝑓= 𝑉0 ∪𝑁func(𝑉0),
𝑉𝑒= 𝑉𝑓∪𝐶owner(𝑉𝑓),
(5)
where 𝐸𝑒contains the seed edges and the edges added during expansion.
To prioritize task-relevant nodes in 𝐺𝑒, FeatLens combines semantic relevance with structural
guidance from the seeds. The semantic score 𝑠semantic(𝑣) is the cosine similarity between code-
retrieval embeddings of the query and node code, clipped at zero; function nodes use their stored
code, and class nodes use skeleton code. Structural guidance uses three potentially overlapping
seed indicators relative to the target: same-file identifies functions in the target’s source file, same-
feature identifies functions in its indexed feature cluster, and similar-function identifies the three
functions ranked highest by BM25-based function-signature matching. Each seed𝑢receives a weight
𝑏(𝑢) = 𝛼𝐼sameFile(𝑢) + 𝛽𝐼sameFeature(𝑢) + 𝛾𝐼similarFunction(𝑢), which contributes to its newly expanded
neighbors. With 𝑁𝑒(𝑣) containing the predecessors and successors of 𝑣in 𝐺𝑒, the accumulated
structural score is:
𝑠struct(𝑣) = 1[𝑣∉𝑉0]
∑︁
𝑢∈𝑉0∩𝑁𝑒(𝑣)
𝑏(𝑢).
(6)
The fused score 𝑤(𝑣) = 𝑠semantic(𝑣)+𝜆𝑠struct(𝑣) balances semantic relevance and structural guidance.
FeatLens normalizes these scores into a restart vector 𝑠, using a uniform vector when all scores are
zero.

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

FeatLens
7
Algorithm 1: Semantic-Structural Dependency Context Refinement
Input: Task 𝑞, seed graph 𝐺0, target function 𝑡, hyperparameters Θ.
Output: Task-specific dependency graph 𝐺∗.
1 Function RefineContext(𝑞,𝐺0,𝑡, Θ):
2
Expand 𝐺0 to obtain 𝐺𝑒= (𝑉𝑒, 𝐸𝑒) using Eq. (5)
3
foreach 𝑣∈𝑉𝑒do
4
𝑠semantic(𝑣) ←max{0, cos(𝜙code(𝑞),𝜙code(code(𝑣)))}
5
Compute 𝑠struct(𝑣) using Eq. (6)
6
𝑤(𝑣) ←𝑠semantic(𝑣) + 𝜆𝑠struct(𝑣)
7
Normalize 𝑤into 𝑠; use a uniform vector if all scores are zero
8
𝑝←PersonalizedPageRank(𝐺𝑒,𝑠, 𝜇)
9
𝑉∗←TopK𝑣≠𝑡(𝑝)
10
𝐸∗←{(𝑢, 𝑣) ∈𝐸𝑒| 𝑢, 𝑣∈𝑉∗}
11
return 𝐺∗= (𝑉∗, 𝐸∗)
FeatLens then applies personalized PageRank to propagate these preferences over 𝐺𝑒. With 𝐴
denoting the column-normalized transition matrix and 𝜇the restart probability, the ranking scores
are updated as:
𝑝(𝑟+1) = (1 −𝜇)𝐴𝑝(𝑟) + 𝜇𝑠.
(7)
After convergence, FeatLens selects the Top-𝐾nodes excluding the target function 𝑡and retains
the edges among them, yielding the task-specific dependency graph:
𝐺∗= (𝑉∗, 𝐸∗),
𝑉∗= TopK𝑣≠𝑡(𝑝),
𝐸∗= {(𝑢, 𝑣) ∈𝐸𝑒| 𝑢, 𝑣∈𝑉∗}.
(8)
Algorithm 1 summarizes this process. The selected dependency context is provided to the generator
together with the task description and target function location.
4
Evaluation
We evaluate dependency retrieval quality and downstream generation utility; offline indexing
investment, online LLM retrieval overhead, and dependency-context size; and the contributions of
feature guidance, dependency seeding, and context refinement. Our evaluation is guided by the
following research questions (RQs).
RQ1 Effectiveness of FeatLens. Compared with alternative methods, how effective is FeatLens
in retrieving task-relevant repository dependencies and generating code?
RQ2 Indexing and Retrieval Overhead. What offline indexing investment and online retrieval
overhead does FeatLens incur, and how large is the resulting dependency context?
RQ3 Component Contributions and Context-Budget Sensitivity. How does refinement
improve different retrieval strategies, how do Feature and FeatHeur contribute to retrieval
quality, and how does the context budget affect dependency recall and precision?
4.1
Experimental Setup
4.1.1
Benchmarks. We evaluate FeatLens on DevEval [27] and EvoCodeBench [26]. Each task
requires implementing a target function at a known repository location from its signature and
natural-language requirement. Table 1 summarizes the evaluated subsets. The complete retained
task lists are available in our replication package.
DevEval contains 1,825 tasks from 115 Python projects across ten domains. Due to environment-
reproduction difficulties, we retained 90 projects whose reference implementations passed the

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

8
Li et al.
Table 1. Statistics of the DevEval and EvoCodeBench subsets retained for evaluation.
Dataset
Domain
#Repos. Avg. #Files Avg. #Funcs. Avg. LOC #Tasks Avg. #Deps./Task
DevEval
Communication
10
87.6
1485.2
31168.7
159
3.08
Database
11
24.2
302.1
7206.6
153
3.75
Internet
9
92.7
1039.3
23186.4
269
2.85
Multimedia
4
35.3
340.8
6769.3
115
2.91
Scientific-Engineering
6
114.2
954.7
34276.7
51
2.65
Security
13
71.1
687.1
16519.9
161
2.89
Software-Development
7
189.0
1147.3
69154.6
74
1.91
System
9
41.8
371.1
8616.9
188
2.11
Text-Processing
10
32.4
228.7
5653.1
47
1.81
Utilities
11
57.7
444.4
14564.7
213
2.32
Overall
90
70.9
711.0
20283.5
1430
2.72
EvoCodeBench Overall
5
81.0
768.0
17353.4
123
3.67
benchmark tests in our environment. We evaluate code generation on all 1,430 retained tasks and
dependency retrieval on the 1,146 tasks with nonempty reference-dependency annotations.
EvoCodeBench contains 275 tasks from 25 Python projects. Environment-reproduction difficul-
ties limited our evaluation to dependency retrieval. Three authors independently selected projects
based on substantial task counts and high task density, source-code completeness and dependency
traceability, and coverage of machine learning, computer vision, and LLM tooling, which are less
represented in DevEval. The intersection of their selections yielded five projects with 123 tasks; the
109 tasks with nonempty reference-dependency annotations are used for retrieval evaluation.
For each task, we replace the target function body with a pass statement and then build an
offline feature index from the resulting repository snapshot, as detailed in Section 3.1. RQ2 reports
the mean offline index construction time and cost per task.
4.1.2
Baseline Methods. We compare FeatLens with seven baselines covering no-context gener-
ation, lexical and dense retrieval, repository-graph retrieval, multi-view structural context, and
agentic repository exploration.
(1) No-context: the generator receives only the task requirement and target function signature,
without retrieved repository context.
(2) BM25 RAG [42]: a lexical retrieval baseline that ranks repository functions by BM25 similarity
between the task requirement and function code.
(3) UniXcoder RAG [17]: a dense retrieval baseline that embeds the requirement and repository
functions with UniXcoder and ranks functions by embedding similarity.
(4) RepoGraph [38]: a graph-based retrieval baseline that uses a line-level repository graph.
An LLM generates search terms from the requirement, and the graph is searched to retrieve
task-relevant context.
(5) RepoScope [35]: a static-analysis-based method that constructs a repository structural-
semantic graph and assembles multi-view context, including callers, callees, similar functions, and
similar code fragments, while preserving structural relations in the prompt.
(6) LocAgent [8]: an agent-based repository exploration method adapted for dependency local-
ization. It iteratively searches repository structure and code through tool interactions to identify
task-relevant locations.
(7) CodexGraph [34]: an LLM-based repository exploration method that stores repository
entities and relations in Neo4j and uses LLM-generated Cypher queries to retrieve task-relevant
context.

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

FeatLens
9
We additionally include an Oracle condition in which the code of the dependencies annotated
in DevEval is supplied directly to the generation model as context, without retrieval.
For RepoGraph, CodexGraph, and LocAgent, online retrieval or exploration calls use DeepSeek-
V3.2 with temperature 0. LocAgent is limited to five model calls, with a 32K-token context limit per
call. CodexGraph uses the best setting of two retrieval iterations, with a one-iteration fallback for
101 of 1,430 tasks.
4.1.3
Evaluation Metrics. We evaluate both dependency retrieval and downstream generation.
(1) DR@K measures the fraction of reference dependencies covered by the Top-𝐾retrieved
results:
DR@𝐾= |𝐷retrieved ∩𝐷gt|
|𝐷gt|
.
(9)
Here, 𝐷gt is the deduplicated union of the benchmark’s intra-class, intra-file, and cross-file
annotations.
(2) Precision (P) measures the proportion of retrieved results that are ground-truth dependencies.
(3) F1 is the harmonic mean of DR@𝐾and Precision, capturing the trade-off between dependency
coverage and context noise.
(4) DIR (Dependency Invocation Rate) [19] measures how many ground-truth dependencies are
invoked by generated code:
DIR = |𝐷invoked ∩𝐷gt|
|𝐷gt|
.
(10)
Tasks with empty reference-dependency annotations are excluded from DIR computation.
(5) Pass@1 measures the fraction of tasks whose single generated program passes all unit tests.
(6) Code Length measures the number of tokens obtained by tokenizing the generated code
completion. We report the mean token count across evaluated completions.
(7) CC (Cyclomatic Complexity) is computed as an AST-based approximation of McCabe’s
metric [37]. Lower values indicate less structurally complex implementations.
4.1.4
Implementation and Parameter Settings. We use CodeT5-base-multi-sum [46] to generate
function descriptions and Sentence-Transformers encoders [41], including all-mpnet-base-v2
for clustering and all-MiniLM-L6-v2 for feature retrieval. Node semantic scoring uses
BAAI/bge-code-v1 [25]. For context refinement, we set 𝛼= 𝛽= 𝛾= 0.1 and 𝜆= 1. Per-
sonalized PageRank uses a restart probability of 𝜇= 0.15, a maximum of 100 iterations, and a
convergence tolerance of 10−6. For FeatLens, we evaluate final context budgets 𝐾∈{10, 15, 20}
and use 𝐾= 15 for downstream generation. Code generation uses deepseek-v3.2-251201 and
gpt-5-mini-2025-08-07 with temperature 0 and top-𝑝0.95. DeepSeek-V3.2 runs in non-thinking
mode, while GPT-5-mini uses the minimal reasoning-effort setting. Retrieval queries consist
of the task requirements and parameter descriptions and are constructed independently of the
feature-index descriptions. The LLM prompt templates used in our experiments are provided in
our replication package.
Statistical analysis. On DevEval, we use paired task-level comparisons with repository-cluster
bootstrap confidence intervals, two-sided sign-flip tests, and Holm correction for multiple com-
parisons. In Tables 2 and 3, ∗marks a significant difference from FeatLens (𝑝adj < 0.05), in either
direction. Statistical analyses cover DR, DIR, and Pass@1 on DevEval; Oracle is excluded. No
statistical significance tests are performed on EvoCodeBench.

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

10
Li et al.
Table 2. Dependency recall of retrieval and exploration methods on DevEval and EvoCodeBench.
Method
DevEval
EvoCodeBench
DR@10
DR@15
DR@20
DR@10
DR@15
DR@20
BM25 RAG
0.261∗
0.296∗
0.322∗
0.204
0.241
0.273
UniXcoder RAG
0.354∗
0.415∗
0.453∗
0.311
0.355
0.371
RepoGraph
0.097∗
0.099∗
0.100∗
0.106
0.106
0.108
RepoScope
0.272∗
0.338∗
0.345∗
0.299
0.332
0.334
LocAgent
0.491†,∗
0.477†
CodexGraph
0.239∗
0.309∗
0.344∗
0.244
0.354
0.402
FeatLens
0.498
0.527
0.547
0.510
0.529
0.553
†LocAgent returns variable-sized results; its recall differs significantly from FeatLens on DevEval at 𝐾= 15, 20.
4.2
RQ1: Effectiveness of Dependency Retrieval and Code Generation
4.2.1
Dependency Retrieval Effectiveness. As shown in Table 2, FeatLens achieves the highest
dependency recall at all three fixed retrieval budgets on both datasets. At 𝐾= 15, which is also
used for downstream generation, FeatLens reaches 0.527 on DevEval and 0.529 on EvoCodeBench,
exceeding UniXcoder RAG by 11.2 and 17.4 percentage points, respectively. These results show
that FeatLens covers more reference dependencies within the same retrieval budget. On DevEval,
the recall gains over all fixed-budget baselines are statistically significant at each budget.
The recall advantage also holds when FeatLens is given a smaller retrieval budget than competing
methods. Its DR@10 exceeds the highest DR@20 among the fixed-budget baselines on both datasets:
0.498 versus 0.453 for UniXcoder RAG on DevEval, and 0.510 versus 0.402 for CodexGraph on
EvoCodeBench. Thus, FeatLens covers more reference dependencies with half the maximum number
of retrieved entries in these comparisons, showing that its recall advantage does not rely on a larger
retrieval budget.
4.2.2
Code Generation Performance. Table 3 reports code generation performance on DevEval using
the Top-15 retrieved context, except for LocAgent, whose variable-sized context is used instead.
FeatLens achieves the highest non-oracle Pass@1 under both DeepSeek-V3.2 (42.24%) and GPT-5-
mini (55.03%). The gains over No-context, BM25 RAG, RepoGraph, and CodexGraph are statistically
significant under both models. Under DeepSeek-V3.2, FeatLens achieves a Pass@1 of 42.24%,
compared with 41.40% for UniXcoder RAG and 40.67% for RepoScope, although neither difference
is statistically significant. These results support the downstream utility of the retrieved dependency
context of FeatLens, with improvements over several baselines and competitive performance against
the strongest alternatives.
To examine whether these generation results are accompanied by greater reuse of repository
dependencies, we compare dependency invocation rates (DIR). FeatLens increases DIR over No-
context from 17.08% to 52.91% with DeepSeek-V3.2 and from 15.92% to 53.58% with GPT-5-mini,
ranking first and second among non-oracle methods, respectively. Together with the Pass@1 results,
these increases support the utility of the retrieved context for dependency reuse and function
implementation. The Oracle condition, which directly supplies the benchmark-annotated reference
dependencies, further raises DIR to 76.68% and 81.02%, yet its Pass@1 values of 42.73% and 54.41%
remain within one percentage point of FeatLens’s. This suggests that FeatLens’s retrieved context
may already provide much of the dependency information that the evaluated models can effectively
exploit for correct implementation, leaving limited additional correctness gains from directly
supplying the reference dependencies. FeatLens also produces relatively concise code with low

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

FeatLens
11
Table 3. Code generation performance on DevEval with DeepSeek-V3.2 and GPT-5-mini.
Method
DeepSeek-V3.2
GPT-5-mini
DIR(%)
Pass@1(%)
Code Len.
CC
DIR(%)
Pass@1(%)
Code Len.
CC
No-context
17.08∗
17.20∗
65.8
4.05
15.92∗
29.23∗
252.2
16.00
BM25 RAG
42.59∗
32.17∗
66.1
3.95
44.07∗
48.18∗
128.6
7.82
UniXcoder RAG
49.18∗
41.40
65.8
3.82
51.92
53.43
108.8
6.55
RepoGraph
29.92∗
23.01∗
73.6
4.72
36.21∗
36.29∗
167.0
10.43
RepoScope
37.77
40.67
120.9
5.77
38.44
47.91
119.9
6.84
LocAgent
45.22∗
33.71∗
65.5
4.46
61.59∗
50.98
115.5
7.13
CodexGraph
48.16
35.61∗
76.2
4.57
45.98∗
36.88∗
138.5
9.21
FeatLens
52.91
42.24
65.3
3.87
53.58
55.03
101.1
6.10
Oracle
76.68
42.73
68.0
4.06
81.02
54.41
112.3
7.03
Table 4. Feature-index statistics and mean offline construction time and cost per task.
Dataset
#Func.
#Feat.
#Func./Feat.
Time (s)
Cost (USD)
DevEval
711.0
132.7
5.53
269.4
0.21
EvoCodeBench
768.0
179.6
5.25
316.6
0.30
control-flow complexity: code length is among the lowest under both models, while CC ranks
second-lowest with DeepSeek-V3.2 and lowest with GPT-5-mini among non-oracle methods.
Summary for RQ1: FeatLens retrieves more reference dependencies within a limited
retrieval budget: its Top-10 recall exceeds the Top-20 recall of every fixed-budget baseline
on both datasets. The retrieved context also supports effective code generation, yielding
the highest non-oracle Pass@1 point estimates under both models and results within one
percentage point of the reference-dependency Oracle.
4.3
RQ2: Indexing and Retrieval Overhead
4.3.1
Offline Feature Indexing. As shown in Table 4, the offline index organizes an average of 711.0
functions into 132.7 features on DevEval and 768.0 functions into 179.6 features on EvoCodeBench.
Each feature contains about five functions on average, providing function groups for subsequent
task-specific dependency seeding. Under our evaluation protocol, indexing is performed on each
task’s repository snapshot after masking the target function body. Mean construction time is 269.4
seconds on DevEval and 316.6 seconds on EvoCodeBench, with corresponding costs of USD 0.21
and USD 0.30 per task. These results indicate a modest offline indexing investment to establish the
feature-to-function mappings used by online retrieval.
4.3.2
Task-Specific Retrieval and Context Overhead. Table 5 reports graph sizes and online LLM
retrieval overhead on DevEval. Repository-level graph sizes are amortized over tasks sharing each
graph, whereas FeatLens reports its final task-specific graph after refinement. RepoGraph uses
line-level nodes, while the other reported graphs use code entities. Retrieval tokens and calls count
online LLM interactions; context tokens measure only the code supplied to the generator, using the
p50k_base tokenizer.
FeatLens supports the retrieval and generation effectiveness reported in RQ1 with a compact
task-specific dependency graph. Its final graph averages 14.7 nodes and 13.7 edges, compared

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

12
Li et al.
Table 5. Engineering overhead of retrieval and exploration methods on DevEval (per-task averages).
Method
Graph Scope +
Retrieval Mode
Graph Size
LLM Retrieval
Context Tokens
#Nodes
#Edges
Retrieval Tokens
Model Calls
RepoGraph
Repo + LLM
38.3
1580.0
287.2
1
2182.4
RepoScope
Repo + Static
95.6
97.3
0
0
2097.4
CodexGraph
Repo + LLM
111.8
243.6
12,097.1
1.36
9694.4
LocAgent
None + LLM
–
–
30,958.7
4.75
3457.8
FeatLens
Task + Static
14.7
13.7
0
0
3217.2
with the amortized repository-graph sizes of 95.6 nodes and 97.3 edges for RepoScope and 111.8
nodes and 243.6 edges for CodexGraph. The graph processed during FeatLens’s refinement is
also task-local, containing 35.4 nodes on average after expansion from feature-selected seeds
(Table 7). Together with RQ1, these results show that feature-guided retrieval can provide effective
dependency context through localized graph construction and refinement, without constructing a
full repository dependency graph for each task.
This feature-guided retrieval and refinement pipeline requires no online LLM decisions. Like
RepoScope, FeatLens incurs zero online LLM retrieval calls or tokens. In contrast, RepoGraph uses
one model call to generate search terms, while CodexGraph and LocAgent rely on iterative LLM
interactions, averaging 1.36 and 4.75 calls and approximately 12.1K and 31.0K retrieval tokens per
task, respectively. FeatLens achieves the retrieval and generation results reported in RQ1 through
feature-guided seeding and task-specific refinement, without the online model interactions used by
LLM-assisted exploration.
The resulting code context averages 3217.2 tokens per task, close to LocAgent’s 3457.8 tokens
and approximately one-third of CodexGraph’s 9694.4 tokens. RepoGraph and RepoScope supply
shorter contexts of 2182.4 and 2097.4 tokens, respectively, but achieve lower dependency recall in
RQ1. FeatLens therefore combines higher dependency coverage with a code-context size in the
middle of the range reported for the evaluated methods, rather than relying on the largest context
input to obtain its retrieval and generation results.
Summary for RQ2: With a modest offline indexing investment, FeatLens performs on-
line dependency retrieval without LLM calls. The resulting task-specific context averages
14.7 nodes, 13.7 edges, and approximately 3.2K code tokens per task, supporting effective
dependency retrieval and code generation with a compact graph and moderate-sized code
context.
4.4
RQ3: Component Contributions and Context-Budget Sensitivity
RQ3 examines whether refinement improves different retrieval strategies, how Feature and FeatHeur
contribute to dependency retrieval, and how the context budget affects the resulting coverage and
precision.
4.4.1
Refinement across Retrieval Strategies and Feature Guidance. Table 6 supports two comple-
mentary comparisons: changes from initial retrieval to the refined context within each row, and
differences among retrieval strategies within each column. Direct retrieves the top 15 functions.
For function-level methods, Seed matches the average count of functions in FeatLens’s top three
retrieved features. In contrast, feature-based methods collect the functions associated with their

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

FeatLens
13
Table 6. Dependency retrieval before and after refinement with different seeding strategies and feature
guidance on DevEval.
Method
Direct
Seed
Final
DR
P
F1
DR
P
F1
DR
P
F1
BM25-Code
.309
.061
.094
.324
.058
.090
.398
.081
.124
BM25-Description
.313
.062
.096
.324
.061
.094
.402
.082
.127
BM25-Signature(aka. FeatHeur)
.343
.068
.106
.358
.066
.102
.425
.087
.133
UniXcoder
.425
.085
.132
.438
.084
.129
.480
.098
.151
Summary Only
.330
.065
.101
.349
.064
.099
.423
.086
.133
Feature
/
/
/
.390
.082
.123
.426
.092
.141
FeatLens: Feature (+FeatHeur)
/
/
/
.491
.104
.157
.527
.112
.172
selected features. Final applies the refinement stage, including structural expansion, scoring, and
selection, with 𝐾= 15.
Across all configurations, refinement improves DR, precision, and F1 over the seeds. For methods
with Direct results, the refined context also outperforms direct retrieval at the same final budget of
15 entries. For example, DR increases from 0.309 to 0.398 for BM25-Code, from 0.425 to 0.480 for
UniXcoder, and from 0.330 to 0.423 for Summary Only. These improvements show that refinement
is not restricted to feature-based seeds: it also turns candidates from lexical, dense, and function-
description retrieval into more effective dependency contexts.
Comparing the representations used for seeding shows the contribution of the Feature Index.
Summary Only retrieves individual functions through their CodeT5-generated descriptions, whereas
Feature further groups functions through clustering and retrieves the resulting feature summaries.
Moving from Summary Only to Feature raises Seed DR from 0.349 to 0.390 and Seed F1 from 0.099
to 0.123. After refinement, although the DR gain is smaller (from 0.423 to 0.426), precision and F1
increase from 0.086 to 0.092 and from 0.133 to 0.141, respectively. Feature organization therefore
improves the initial candidate set and retains an advantage in the concentration of reference
dependencies in the final context.
Feature Only and BM25-Signature yield similar Final DR (0.426 and 0.425), but combining Feature
with FeatHeur raises it to 0.527. Actually, BM25-Signature in the table serves as a function-level
heuristic counterpart: it uses signature matching to select candidates, whereas FeatHeur in FeatLens
prioritizes the feature group containing the target function during dependency seeding. Viewed
from the Feature configuration, adding FeatHeur improves Seed/Final DR from 0.390/0.426 to
0.491/0.527. Viewed from the signature-based heuristic configuration, the feature-guided component
improves these values from 0.358/0.425 to 0.491/0.527. The complete FeatLens approach also achieves
the highest precision and F1 at both Seed and Final. Together, these comparisons support the
complementary value of functional grouping and heuristic guidance rather than relying on either
retrieval signal alone.
4.4.2
Context Refinement and Context-Budget Sensitivity. Table 7 traces how refinement expands
the candidate set and then selects a bounded context. On DevEval, expansion increases the average
node count from 17.8 to 35.4 and DR from 0.491 to 0.655; on EvoCodeBench, the corresponding
changes are 15.0 to 30.5 nodes and 0.478 to 0.671 DR. Subsequent ranking and selection at 𝐾= 15
retain DR of 0.527 and 0.529, respectively. Although selection discards some dependencies from the
expanded candidates, the final context improves aggregate DR, precision, and F1 over the seeds
on both datasets. Refinement thus preserves part of the coverage gained through expansion while
producing a more concentrated dependency context under the output budget.

[Vista original de la página 13](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-13.png)

![Página PDF 13, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-13.png)


<!-- PDF page 14 -->

## Página PDF 14

14
Li et al.
Table 7. Graph size and dependency retrieval performance across FeatLens stages and context budgets on
DevEval and EvoCodeBench.
Domain /
Repository
Dependency Seeds
Dependency
Expansion
Task-Specific Dependency Graph
K=10
K=15
K=20
#N.
DR
P
F1
#N.
DR
DR
P
F1
DR
P
F1
DR
P
F1
DevEval
Communication
17.9
.444
.097
.145
36.8
.588
.435
.143
.200
.483
.109
.168
.505
.091
.146
Database
15.2
.410
.126
.169
33.4
.585
.422
.184
.221
.435
.133
.179
.464
.110
.158
Internet
21.2
.456
.093
.144
41.0
.631
.464
.144
.209
.493
.105
.166
.512
.084
.139
Multimedia
24.1
.500
.079
.127
41.0
.615
.468
.141
.199
.515
.115
.173
.538
.095
.150
Sci.-Eng.
16.9
.319
.084
.123
34.3
.479
.357
.128
.175
.372
.090
.136
.372
.070
.111
Security
16.9
.522
.112
.167
32.8
.717
.542
.166
.228
.565
.119
.179
.583
.096
.152
Softw.-Dev.
15.5
.439
.082
.124
34.1
.599
.460
.117
.173
.474
.083
.133
.474
.067
.110
System
14.4
.530
.104
.161
33.7
.744
.573
.137
.206
.616
.104
.167
.631
.083
.139
Text-Proc.
15.5
.532
.092
.147
28.0
.587
.504
.120
.183
.549
.095
.155
.549
.075
.126
Utilities
16.6
.629
.130
.199
30.5
.763
.612
.175
.256
.630
.128
.202
.659
.109
.177
Overall
17.8
.491
.104
.157
35.4
.655
.498
.152
.213
.527
.112
.172
.547
.092
.147
EvoCodeBench
litdata
13.3
.441
.142
.183
25.5
.611
.491
.187
.223
.499
.134
.180
.537
.116
.167
UniRef
13.2
.513
.152
.210
24.6
.700
.511
.196
.231
.530
.149
.199
.555
.134
.192
EasyVolcap
14.4
.388
.092
.124
42.8
.730
.467
.111
.158
.467
.078
.118
.481
.067
.104
ollama-python
15.6
.567
.085
.140
25.0
.733
.567
.125
.190
.650
.106
.173
.650
.079
.135
tanuki_py
31.0
.712
.129
.202
55.1
.763
.656
.300
.385
.684
.217
.311
.684
.163
.250
Overall
15.0
.478
.128
.174
30.5
.671
.510
.176
.221
.529
.130
.181
.553
.110
.162
Notes. Sci.-Eng. = Scientific-Engineering; Softw.-Dev. = Software-Development; Text-Proc. = Text-Processing.
The final context budget controls the trade-off between dependency recall and retrieval precision.
On both datasets, 𝐾= 10 yields the highest aggregate precision and F1, whereas 𝐾= 20 yields the
highest recall (0.547 on DevEval and 0.553 on EvoCodeBench). The benefit of additional entries
varies across repositories: increasing 𝐾from 15 to 20 raises recall on EasyVolcap but not on ollama-
python. We use 𝐾= 15 as a common operating budget for generation: it retains more than 95%
of the recall obtained at 𝐾= 20 on both datasets while reducing the maximum node budget by
25%. This provides a practical balance between dependency coverage and context size among the
evaluated budgets.
Summary for RQ3: Refinement improves dependency retrieval across all evaluated seeding
strategies, not only feature-based retrieval. Feature organization and FeatHeur provide com-
plementary guidance, with their combination achieving the strongest Seed and Final results.
The context budget controls the trade-off between dependency coverage and concentration;
𝐾= 15 provides a practical operating compromise.
4.5
Case Study
We use two contrasting cases to examine whether retrieved context preserves the interfaces needed
for correct implementation (Figure 3). The Mrjob case illustrates the benefit of recovering cross-
file dependencies beyond the target class; the Boto case exposes the risk of removing a required
interface during refinement. Generation results use GPT-5-mini.

[Vista original de la página 14](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-14.png)

![Página PDF 14, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-14.png)


<!-- PDF page 15 -->

## Página PDF 15

FeatLens
15
✓
Case 1: Successful Dependency Retrieval (Mrjob — Log Directory Task)  #1078
×
1. Task Requirement
HadoopJobrunner.
_stream_history
_log_dirs
Yield existing 
directories for 
history-log 
search.
2. Feature Description
Hadoop Log Discovery
Locate and access 
Hadoop job logs across 
configured and fallback 
directories for monitoring 
and troubleshooting.
_hadoop_log_dirs
_read_logs
unique
_logs_exist
fs
_hadoop_log_dirs
(HadoopJobRunner)
_stream_task_log_dirs
(HadoopJobRunner)
Unique
(mrjob.util)
_logs_exist
(mrjob.logs.wrap)
3. Dependency Seeds
5. Final Context
6. Generated Code
✓ All tests passed
if not self._read_logs():
return
for log_dir in unique(self.
_hadoop_log_dirs(...)):
if _logs_exist(self.fs, l
og_dir):
yield [log_dir]
1. Task Requirement
Table._put_item
Save an  
item to a 
DynamoDB 
table.
2. Feature Description
DynamoDB Item 
Save/Update
Support full or partial 
updates and conflict 
detection while preserving 
data integrity.
DynamoDB Table 
Management
Manage DynamoDB 
tables and items, including 
conditional writes, queries, 
and updates.
Item.save
build_expects
make_request
make_request
(DynamoDBConnection)
save
(Item)
build_expects
(Item)
put_item
(DynamoDBConnection)
3. Dependency Seeds
5. Final Context
6. Generated Code
Case 2: Failed Dependency Retrieval (Boto — Save Item Task)  #382
✕Tests failed
payload = {
'TableName': self.name,
'Item': item_data
}
self.connection.make_requ
est(
'PutItem', json.dumps(p
ayload))
Error: Nonexistent Attribute
_stream_history_log_dirs
_logs_exist
fs
_read_logs
unique
_hadoop_log_dirs
_stream_task_log_dirs
4. Context Refinement
Table._put_item
Item.save
make_request
4. Context Refinement
build_expects
DynamoDBConnection.put_item
Some others…
Incorrectly removed
In Seeds & Final Context
In Expansion & Final Context
In Expansion & Be Removed
In Seeds & Be Removed
Fig. 3. Case studies of FeatLens dependency retrieval and code generation.
Success: preserving repository-specific interface behavior. The Mrjob task from Section 2.2 distin-
guishes locating relevant code from retrieving the interfaces that constrain a correct implementation.
In particular, _logs_exist checks paths through the repository’s filesystem abstraction and returns
None on an IOError. Its implementation therefore provides concrete guidance on filesystem access
and error handling that a log-related method name or target-class location alone does not supply.
LocAgent and CodexGraph retrieve context around HadoopJobRunner, but neither supplies the
implementation of _logs_exist in its final generation context. Their generated code violates the
corresponding behavior in different ways: LocAgent uses os.path.exists and yields no directory
in the HDFS-path test, whereas CodexGraph omits the existence check and fails to skip inaccessible
paths. BM25 and UniXcoder exhibit a related path-semantics error, appending an unnecessary
history/ suffix to the candidate directory.
FeatLens instead connects the log-discovery feature to cross-file helpers and expands the seeds
to include the log-reading and filesystem interfaces. Refinement retains these dependencies in the
final context. With this context, GPT-5-mini reuses the repository interfaces, yields the candidate
directory without altering its path, and passes the tests. The contrast illustrates the value of retaining
behavior-defining dependencies rather than merely retrieving code near the target or about the
same topic.
Failure: removing a critical interface despite a relevant feature match. The Boto task, Table._put_item,
exposes the complementary limitation: a useful feature-guided entry point does not guar-
antee that refinement preserves the interface needed for implementation. The selected
feature covers the DynamoDB item-save workflow, and the initial seeds already contain
DynamoDBConnection.put_item. However, refinement removes this interface when selecting 15
nodes from the 42-node expanded context, while retaining more general request-construction
routines such as make_request.
The generated code constructs the request payload itself and accesses the nonexistent attribute
self.name, causing an AttributeError. In contrast, the BM25 and UniXcoder implementations

[Vista original de la página 15](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-15.png)

![Página PDF 15, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-15.png)


<!-- PDF page 16 -->

## Página PDF 16

16
Li et al.
invoke self.connection.put_item(self.table_name, ...) and pass the tests. Here, the re-
trieval failure lies not in discovering the relevant workflow or admitting the correct interface into
the candidate set, but in retaining that interface under the context budget.
Together, the cases distinguish functional relevance from implementation sufficiency: feature
guidance can expose dependencies missed by topic- or location-centered retrieval, but budgeted
refinement must preserve the interfaces that define the required behavior, and the generator must
still use them correctly.
5
Discussion
5.1
Implications and Applicability Boundaries
Overall, the results highlight the value of combining functional abstraction with repository structure
to construct task-relevant dependency context. The feature index connects task requirements to
groups of repository functions, while feature-heuristic reranking prioritizes the group containing
the target function. Structural expansion and semantic–structural refinement then transform
these groups into a bounded dependency context for code generation. The component results in
Section 4.4 support the effectiveness of feature-guided seeding with target-location guidance and
show that subsequent expansion and refinement improve dependency retrieval over the initial
seeds.
The results further suggest that feature guidance and structural reasoning play complementary
roles. Feature-guided seeding provides functionally coherent entry points, while expansion recovers
dependencies beyond the initial feature groups and refinement prioritizes them under a bounded
context budget. This design provides a practical balance between dependency coverage and con-
text concentration, and also motivates adaptive context budgets based on retrieval confidence or
structural connectivity.
The two case studies further highlight the importance of preserving repository-specific interfaces
during context refinement. In Mrjob, the final context retains the repository-specific interfaces
reused by the passing implementation. In Boto, the relevant interface is identified in the seeds
but is not retained in the final context, and the generated implementation instead constructs a
request using a nonexistent attribute. These observations suggest that refinement can further
benefit from explicitly considering which interfaces encode implementation-specific behavior. A
direction for future work is to combine context refinement with execution feedback to further
improve dependency selection and generated implementations.
FeatLens is most naturally applicable when the target function location is known and the required
implementation depends on statically traceable repository entities, such as reusable functions,
class members, and cross-file APIs. Its benefits are likely to be less predictable when behavior is
introduced through runtime binding, implicit framework conventions, external configuration, or
low-level interfaces that are weakly represented by feature clusters. Tasks requiring coordinated
edits across multiple files or iterative test-driven repair also extend beyond the setting evaluated in
this paper. These boundaries define the current role of FeatLens as a repository-aware dependency
context constructor for function generation, while motivating extensions toward multi-file feature
implementation and execution-guided refinement.
5.2
Threats to Validity
External validity. Our evidence comes from selected Python repositories in DevEval and
EvoCodeBench. DevEval projects were retained when their reference implementations passed the
tests in our configured environments, while EvoCodeBench projects were selected using explicit
domain and dependency-traceability criteria rather than random sampling. EvoCodeBench supports

[Vista original de la página 16](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-16.png)

![Página PDF 16, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-16.png)


<!-- PDF page 17 -->

## Página PDF 17

FeatLens
17
retrieval conclusions only in this study. The findings therefore characterize repository-aware func-
tion generation and dependency retrieval in the evaluated Python settings; generalization to other
languages, industrial repositories, dynamic dependency structures, and full feature-development
benchmarks remains to be established.
Construct validity. DR, precision, and F1 measure retrieval coverage and context concentration;
DIR measures whether generated code invokes annotated dependencies; and Pass@1 measures
executable correctness. Code length and cyclomatic complexity provide proxies for conciseness
and structural complexity, while the retrieval metrics inherit the scope and granularity of the
benchmark annotations.
Internal validity. Results may depend on retrieval parameters, prompts, candidate budgets,
and implementation choices across systems. The downstream generation comparison fixes 𝐾= 15
without independent held-out tuning. Finally, offline feature summarization and static relations
may miss runtime binding and implicit framework behavior.
6
Related Work
Related work on repository-level code generation can be broadly grouped into three directions:
dependency retrieval, LLM-based repository exploration, and feature-oriented software develop-
ment. FeatLens connects these lines of research by using feature-level intent to guide dependency
context retrieval.
6.1
Dependency Retrieval in Repository-Level Code Generation
Retrieval-augmented code generation selects relevant repository context through semantic or
structural signals. Semantic methods use sparse matching [6, 18, 42], code embeddings [15, 17], or
learned retrieval strategies such as RLCoder [47], AlignCoder [21], and Hierarchical Embedding Fu-
sion [43]. Since semantic similarity may miss cross-file dependencies [9], structure-aware methods
further exploit code graphs. RepoGraph [38] and GraphCoder [33] model repository dependencies
for graph-based retrieval, while later work considers multi-hop reasoning [40], multi-granularity
structure [45], architecture preservation [35], and knowledge graphs [1]. InlineCoder [20] orga-
nizes dependency context around a generated draft, whereas FastCoder [56] emphasizes retrieval
efficiency.
Overall, these methods organize retrieval mainly around repository code or intermediate genera-
tion states. FeatLens instead uses functional features as retrieval anchors, linking each feature to
candidate functions that serve as seeds for dynamic dependency expansion and refinement.
6.2
LLM-Based Repository Exploration
LLM-based repository exploration lets agents iteratively search and inspect repositories to iden-
tify task-relevant context. Early agents, including SWE-Agent [49], AutoCodeRover [54], and
CodeAgent [53], explore repositories mainly through autonomous tool use. This flexibility is useful,
but an unconstrained search space makes reliable localization difficult. Subsequent work introduces
structured repository graphs to guide localization and reasoning [8, 22]. CodexGraph [34] enables
LLMs to explore a repository graph database through Cypher queries, while GraphCodeAgent [28]
couples a requirement graph with a code graph for agent-driven multi-hop reasoning between
intent and dependencies. More recent approaches pursue stronger but heavier exploration, using
Monte Carlo tree search [36], autonomous multi-round context construction [44], or knowledge
graphs with working memory for long-horizon navigation [39].
These methods improve contextual coverage but often require repeated LLM decisions. FeatLens
instead narrows the search space with feature-guided dependency seeds and retrieves dependency
context without online LLM decisions.

[Vista original de la página 17](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-17.png)

![Página PDF 17, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-17.png)


<!-- PDF page 18 -->

## Página PDF 18

18
Li et al.
6.3
Feature-Oriented Software Development
Feature-oriented software development views features as high-level units for understanding, orga-
nizing, and evolving software functionality [3, 23]. Feature location techniques aim to identify the
program entities responsible for implementing a given functionality [13]. Recent repository un-
derstanding approaches extend this idea to large-scale codebases by constructing feature-oriented
representations and traceability links. For example, RepoSummary [58] extracts repository sum-
maries organized around functional features and associates feature descriptions with relevant
implementation components. These studies demonstrate that a feature is rarely implemented by a
single function; instead, realizing a functionality often requires locating a set of interacting and
distributed code entities.
More recently, features have become natural task units in LLM-based repository-level software
engineering. Benchmarks such as FEA-Bench [29], FeatBench [5], NoCode-bench [11], and Fea-
tureBench [57] evaluate whether LLM-based systems can implement concrete feature requests
in existing repositories. Beyond evaluation, SWE-Dev [14] and EvoDev [32] investigate feature-
driven autonomous development and dependency modeling, while FeatX [30] supports repository
evolution through feature-level editing interactions. Together, these studies establish features as
meaningful units for repository-level development. However, they mainly treat features as task
specifications, evaluation targets, or editing units, rather than as retrieval signals for identifying
reusable code context.
FeatLens builds on this perspective by treating feature-level intent as an operational retrieval
signal. It maps feature descriptions to supporting repository entities and uses them as dependency
seeds for constructing task-specific code context, thereby connecting functional requirements with
the code dependencies needed for implementation.
7
Conclusion
This paper introduced FeatLens, a feature-guided dependency retrieval approach for repository-level
code generation. FeatLens maps feature-level intent to function-level dependency context through
Feature-Oriented Repository Indexing, Feature Retrieval and Dependency Seeding, and Semantic-
Structural Dependency Context Refinement. Retrieval experiments on DevEval and EvoCodeBench
show that FeatLens achieves the highest dependency recall among the evaluated methods at each
fixed context budget, without online LLM retrieval calls. Downstream generation experiments
on DevEval yield the highest non-oracle Pass@1 point estimates and the shortest generated
completions under both DeepSeek-V3.2 and GPT-5-mini. Future work will strengthen dependency
context refinement for runtime binding, implicit framework conventions, and dependencies that
are weakly aligned with feature clusters, and broaden evaluation with more diverse repository-level
code generation benchmarks.
References
[1] Mihir Athale and Vishal Vaddina. 2025. Knowledge Graph Based Repository-Level Code Generation. In 2025 IEEE/ACM
International Workshop on Large Language Models for Code (LLM4Code) (Ottawa, ON, Canada). IEEE Press, 169–176.
doi:10.1109/LLM4Code66737.2025.00026
[2] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang,
Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. 2021. Program Synthesis with Large Language Models.
arXiv:2108.07732 [cs.PL] https://arxiv.org/abs/2108.07732
[3] D. Batory. 2004. Feature-oriented programming and the AHEAD tool suite. In Proceedings. 26th International Conference
on Software Engineering. 702–703. doi:10.1109/ICSE.2004.1317496
[4] Islem Bouzenia, Premkumar Devanbu, and Michael Pradel. 2025. RepairAgent: An Autonomous, LLM-Based Agent
for Program Repair. In 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE). 2188–2200.
doi:10.1109/ICSE55347.2025.00157

[Vista original de la página 18](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-18.png)

![Página PDF 18, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-18.png)


<!-- PDF page 19 -->

## Página PDF 19

FeatLens
19
[5] Haorui Chen, Chengze Li, and Jia Li. 2026. FeatBench: Towards More Realistic Evaluation of Feature-level Code
Generation. arXiv:2509.22237 [cs.CL] https://arxiv.org/abs/2509.22237
[6] Junkai Chen, Xing Hu, Zhenhao Li, Cuiyun Gao, Xin Xia, and David Lo. 2024. Code Search is All You Need?
Improving Code Suggestions with Code Search. In Proceedings of the IEEE/ACM 46th International Conference on
Software Engineering (Lisbon, Portugal) (ICSE ’24). Association for Computing Machinery, New York, NY, USA, Article
73, 13 pages. doi:10.1145/3597503.3639085
[7] Shengyuan Chen, Chuang Zhou, Zheng Yuan, Qinggang Zhang, Zeyang Cui, Hao Chen, Yilin Xiao, Jiannong Cao, and
Xiao Huang. 2026. You don’t need pre-built graphs for RAG: retrieval augmented generation with adaptive reasoning
structures. In Proceedings of the Fortieth AAAI Conference on Artificial Intelligence and Thirty-Eighth Conference
on Innovative Applications of Artificial Intelligence and Sixteenth Symposium on Educational Advances in Artificial
Intelligence (AAAI’26/IAAI’26/EAAI’26). AAAI Press, Article 3377, 9 pages. doi:10.1609/aaai.v40i36.40278
[8] Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan,
and Xingyao Wang. 2025. LocAgent: Graph-Guided LLM Agents for Code Localization. In Proceedings of the 63rd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Wanxiang Che, Joyce Nabende,
Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). Association for Computational Linguistics, Vienna, Austria,
8697–8727. doi:10.18653/v1/2025.acl-long.426
[9] Wei Cheng, Yuhan Wu, and Wei Hu. 2024. Dataflow-Guided Retrieval Augmentation for Repository-Level Code
Completion. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok,
Thailand, 7957–7977. doi:10.18653/v1/2024.acl-long.431
[10] Mike Cohn. 2004. User Stories Applied: For Agile Software Development. Addison Wesley Longman Publishing Co., Inc.,
USA.
[11] Le Deng, Zhonghao Jiang, Jialun Cao, Michael Pradel, and Zhongxin Liu. 2025. NoCode-bench: A Benchmark for
Evaluating Natural Language-Driven Feature Addition. arXiv:2507.18130 [cs.SE] https://arxiv.org/abs/2507.18130
[12] Yangruibo Ding, Zijian Wang, Wasi Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh
Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang. 2023. CrossCodeEval: A Diverse and Multilingual Benchmark
for Cross-File Code Completion. In Advances in Neural Information Processing Systems, A. Oh, T. Naumann, A. Globerson,
K. Saenko, M. Hardt, and S. Levine (Eds.), Vol. 36. Curran Associates, Inc., 46701–46723. https://proceedings.neurips.
cc/paper_files/paper/2023/file/920f2dced7d32ab2ba2f1970bc306af6-Paper-Datasets_and_Benchmarks.pdf
[13] Bogdan Dit, Meghan Revelle, Malcom Gethers, and Denys Poshyvanyk. 2013.
Feature location in
source code: a taxonomy and survey.
Journal of Software: Evolution and Process 25, 1 (2013), 53–95.
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/smr.567 doi:10.1002/smr.567
[14] Yaxin Du, Yuzhu Cai, Yifan Zhou, Cheng Wang, Yu Qian, Xianghe Pang, Qian Liu, Yue Hu, and Siheng Chen. 2026.
SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development. arXiv:2505.16975 [cs.SE]
https://arxiv.org/abs/2505.16975
[15] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu,
Daxin Jiang, and Ming Zhou. 2020. CodeBERT: A Pre-Trained Model for Programming and Natural Languages. In
Findings of the Association for Computational Linguistics: EMNLP 2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.).
Association for Computational Linguistics, Online, 1536–1547. doi:10.18653/v1/2020.findings-emnlp.139
[16] Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan-Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming
Xiong, Heng Ji, and Shafiq Joty. 2026. SWERank: Software Issue Localization with Code Ranking. In International
Conference on Learning Representations, C. Vondrick, B. Hariharan, C. Raffel, L. Pinto, D. Yang, and A. Faust (Eds.),
Vol. 2026. 78997–79011. https://proceedings.iclr.cc/paper_files/paper/2026/file/7f6901ebab786e43b21530328fc989ca-
Paper-Conference.pdf
[17] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. 2022. UniXcoder: Unified Cross-Modal
Pre-training for Code Representation. In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (Eds.). Association for
Computational Linguistics, Dublin, Ireland, 7212–7225. doi:10.18653/v1/2022.acl-long.499
[18] Qi Guo, Xiaohong Li, Xiaofei Xie, Shangqing Liu, Ze Tang, Ruitao Feng, Junjie Wang, Jidong Ge, and Lei Bu. 2024.
FT2Ra: A Fine-Tuning-Inspired Approach to Retrieval-Augmented Code Completion. In Proceedings of the 33rd ACM
SIGSOFT International Symposium on Software Testing and Analysis (Vienna, Austria) (ISSTA 2024). Association for
Computing Machinery, New York, NY, USA, 313–324. doi:10.1145/3650212.3652130
[19] Nam Le Hai, Dung Manh Nguyen, and Nghi D. Q. Bui. 2025. On the Impacts of Contexts on Repository-Level Code
Generation. In Findings of the Association for Computational Linguistics: NAACL 2025, Luis Chiruzzo, Alan Ritter, and
Lu Wang (Eds.). Association for Computational Linguistics, Albuquerque, New Mexico, 1496–1524. doi:10.18653/v1/
2025.findings-naacl.82

[Vista original de la página 19](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-19.png)

![Página PDF 19, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-19.png)


<!-- PDF page 20 -->

## Página PDF 20

20
Li et al.
[20] Chao Hu, Wenhao Zeng, Yuling Shi, Beijun Shen, and Xiaodong Gu. 2026. In Line with Context: Repository-Level Code
Generation via Context Inlining. Proc. ACM Softw. Eng. 3, FSE, Article FSE066 (June 2026), 23 pages. doi:10.1145/3797094
[21] Tianyue Jiang, Yanli Wang, Yanlin Wang, Daya Guo, Ensheng Shi, Yuchi Ma, Jiachi Chen, and Zibin Zheng. 2025.
AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion. In 2025 40th IEEE/ACM
International Conference on Automated Software Engineering (ASE). 971–982. doi:10.1109/ASE63991.2025.00085
[22] Zhonghao Jiang, Xiaoxue Ren, Meng Yan, Wei Jiang, Yong Li, and Zhongxin Liu. 2025. Issue Localization via LLM-
Driven Iterative Code Graph Searching. In 2025 40th IEEE/ACM International Conference on Automated Software
Engineering (ASE). 3034–3045. doi:10.1109/ASE63991.2025.00249
[23] Christian Kästner and Sven Apel. 2013. Feature-Oriented Software Development. Springer Berlin Heidelberg, Berlin,
Heidelberg, 346–382. doi:10.1007/978-3-642-35992-7_10
[24] Minh Le-Anh, Huyen Nguyen, Khanh An Tran, Nam Le Hai, Linh Ngo Van, Nghi D. Q. Bui, and Bach Le.
2026. Do Not Treat Code as Natural Language: Implications for Repository-Level Code Generation and Beyond.
arXiv:2602.11671 [cs.SE] https://arxiv.org/abs/2602.11671
[25] Chaofan Li, Jianlyu Chen, Yingxia Shao, Defu Lian, and Zheng Liu. 2025. Towards A Generalist Code Embedding
Model Based On Massive Data Synthesis. arXiv:2505.12697 [cs.IR] https://arxiv.org/abs/2505.12697
[26] Jia Li, Ge Li, Xuanming Zhang, Yunfei Zhao, Yihong Dong, Zhi Jin, Binhua Li, Fei Huang, and Yongbin Li. 2024.
EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations. In Advances in Neural
Information Processing Systems, A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang
(Eds.), Vol. 37. Curran Associates, Inc., 57619–57641. doi:10.52202/079017-1837
[27] Jia Li, Ge Li, Yunfei Zhao, Yongmin Li, Huanyu Liu, Hao Zhu, Lecheng Wang, Kaibo Liu, Zheng Fang, Lanshen
Wang, Jiazheng Ding, Xuanming Zhang, Yuqi Zhu, Yihong Dong, Zhi Jin, Binhua Li, Fei Huang, Yongbin Li, Bin
Gu, and Mengfei Yang. 2024. DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-
World Code Repositories. In Findings of the Association for Computational Linguistics: ACL 2024, Lun-Wei Ku, Andre
Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 3603–3614.
doi:10.18653/v1/2024.findings-acl.214
[28] Jia Li, Xianjie Shi, Kechi Zhang, Ge Li, Zhi Jin, Lei Li, Huangzhao Zhang, Jia Li, Fang Liu, Yuwei Zhang, Zhengwei
Tao, Yihong Dong, Yuqi Zhu, and Chongyang Tao. 2025. GraphCodeAgent: Dual Graph-Guided LLM Agent for
Retrieval-Augmented Repo-Level Code Generation. arXiv:2504.10046 [cs.SE] https://arxiv.org/abs/2504.10046
[29] Wei Li, Xin Zhang, Zhongxin Guo, Shaoguang Mao, Wen Luo, Guangyue Peng, Yangyu Huang, Houfeng Wang,
and Scarlett Li. 2025. FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation for Feature
Implementation. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). Association
for Computational Linguistics, Vienna, Austria, 17160–17176. doi:10.18653/v1/2025.acl-long.839
[30] Xutian Li, Yifeng Zhu, Xianlin Zhao, Yanzhen Zou, Lu Zhang, and Bing Xie. 2026. FeatX: Editing Software by Editing
Features for Repository-Level Code Evolution. arXiv:2606.31206 [cs.SE] https://arxiv.org/abs/2606.31206
[31] Fang Liu, Yang Liu, Lin Shi, Zhen Yang, Li Zhang, Xiaoli Lian, Zhongqi Li, and Yuchi Ma. 2026. Beyond Functional
Correctness: Exploring Hallucinations in LLM-Generated Code. IEEE Transactions on Software Engineering 52, 3 (2026),
1037–1055. doi:10.1109/TSE.2026.3657432
[32] Junwei Liu, Chen Xu, Chong Wang, Tong Bai, Weitong Chen, Kaseng Wong, Yiling Lou, and Xin Peng. 2026. Towards
Iterative End-to-End Software Development: A Feature-Driven Multi-Agent Framework. arXiv:2511.02399 [cs.SE]
https://arxiv.org/abs/2511.02399
[33] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang. 2024. Graph-
Coder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph. In
Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (Sacramento, CA, USA)
(ASE ’24). Association for Computing Machinery, New York, NY, USA, 570–581. doi:10.1145/3691620.3695054
[34] Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, and Wenmeng
Zhou. 2025. CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases. In
Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers), Luis Chiruzzo, Alan Ritter, and Lu Wang (Eds.). Association for
Computational Linguistics, Albuquerque, New Mexico, 142–160. doi:10.18653/v1/2025.naacl-long.7
[35] Yang Liu, Li Zhang, Fang Liu, Zhuohang Wang, Donglin Wei, Zhishuo Yang, Kechi Zhang, Jia Li, and Lin Shi.
2025.
RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation.
arXiv:2507.14791 [cs.SE] https://arxiv.org/abs/2507.14791
[36] Yingwei Ma, Qingping Yang, Rongyu Cao, Binhua Li, Fei Huang, and Yongbin Li. 2025. Alibaba LingmaAgent: Improving
Automated Issue Resolution via Comprehensive Repository Exploration. In Proceedings of the 33rd ACM International
Conference on the Foundations of Software Engineering (Clarion Hotel Trondheim, Trondheim, Norway) (FSE Companion
’25). Association for Computing Machinery, New York, NY, USA, 238–249. doi:10.1145/3696630.3728549

[Vista original de la página 20](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-20.png)

![Página PDF 20, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-20.png)


<!-- PDF page 21 -->

## Página PDF 21

FeatLens
21
[37] T.J. McCabe. 1976. A Complexity Measure. IEEE Transactions on Software Engineering SE-2, 4 (1976), 308–320.
doi:10.1109/TSE.1976.233837
[38] Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, and
Dong Yu. 2025. RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph. In International
Conference on Learning Representations, Y. Yue, A. Garg, N. Peng, F. Sha, and R. Yu (Eds.), Vol. 2025. 30098–30121.
https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf
[39] Yue Pan, Zimin Chen, Siyu Lu, Zhaoyang Chu, Xiang Li, Han Li, Yang Feng, Claire Le Goues, Federica Sarro, Martin
Monperrus, and He Ye. 2026. Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem
Solving. arXiv:2507.19942 [cs.SE] https://arxiv.org/abs/2507.19942
[40] Huy N. Phan, Hoang N. Phan, Tien N. Nguyen, and Nghi D. Q. Bui. 2025. RepoHyper: Search-Expand-Refine on
Semantic Graphs for Repository-Level Code Completion. In 2025 IEEE/ACM Second International Conference on AI
Foundation Models and Software Engineering (Forge). 14–25. doi:10.1109/Forge66646.2025.00009
[41] Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP), Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan
(Eds.). Association for Computational Linguistics, Hong Kong, China, 3982–3992. doi:10.18653/v1/D19-1410
[42] Stephen Robertson and Hugo Zaragoza. 2009. The Probabilistic Relevance Framework: BM25 and Beyond. Foundations
and Trends in Information Retrieval 4, 1-2 (09 2009), 1–174. arXiv:https://www.emerald.com/ftinr/article-pdf/4/1-
2/1/11486410/1500000019en.pdf doi:10.1561/1500000019
[43] Nikita Sorokin, Ivan Sedykh, and Valentin Malykh. 2026. Hierarchical Embedding Fusion for Retrieval-Augmented
Code Generation. In Proceedings of the 49th International ACM SIGIR Conference on Research and Development in
Information Retrieval (Australia) (SIGIR ’26). Association for Computing Machinery, New York, NY, USA, 1656–1664.
doi:10.1145/3805712.3809571
[44] Huacan Wang, Ziyi Ni, Shuo Zhang, Shuo Lu, Sen Hu, Ziyang He, Chen Hu, Jiaye Lin, Yifu Guo, Yuntao Du, and
Pin Lyu. 2025. RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task
Solving. In Advances in Neural Information Processing Systems, D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz,
M. Ghassemi, and N. Chen (Eds.), Vol. 38. Curran Associates, Inc., 106320–106359. https://proceedings.neurips.cc/
paper_files/paper/2025/file/98da9cdb7e8af9192f1fe2cb38690d60-Paper-Conference.pdf
[45] Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, and Shuiguang Deng. 2025. GRACE:
Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion. arXiv:2509.05980 [cs.SE]
https://arxiv.org/abs/2509.05980
[46] Yue Wang, Weishi Wang, Shafiq Joty, and Steven C.H. Hoi. 2021. CodeT5: Identifier-aware Unified Pre-trained
Encoder-Decoder Models for Code Understanding and Generation. In Proceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing, Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau
Yih (Eds.). Association for Computational Linguistics, Online and Punta Cana, Dominican Republic, 8696–8708.
doi:10.18653/v1/2021.emnlp-main.685
[47] Yanlin Wang, Yanli Wang, Daya Guo, Jiachi Chen, Ruikai Zhang, Yuchi Ma, and Zibin Zheng. 2025. RLCoder:
Reinforcement Learning for Repository-Level Code Completion. In 2025 IEEE/ACM 47th International Conference on
Software Engineering (ICSE). 1140–1152. doi:10.1109/ICSE55347.2025.00014
[48] Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2025. Demystifying LLM-Based Software
Engineering Agents. Proc. ACM Softw. Eng. 2, FSE, Article FSE037 (June 2025), 24 pages. doi:10.1145/3715754
[49] John Yang, Carlos Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. 2024.
SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. In Advances in Neural Information
Processing Systems, A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (Eds.), Vol. 37.
Curran Associates, Inc., 50528–50652. doi:10.52202/079017-1601
[50] Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao
Xie. 2024. CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models. In Proceedings
of the IEEE/ACM 46th International Conference on Software Engineering (Lisbon, Portugal) (ICSE ’24). Association for
Computing Machinery, New York, NY, USA, Article 37, 12 pages. doi:10.1145/3597503.3623316
[51] Zhaojian Yu, Yilun Zhao, Arman Cohan, and Xiao-Ping Zhang. 2025. HumanEval Pro and MBPP Pro: Evaluating Large
Language Models on Self-invoking Code Generation Task. In Findings of the Association for Computational Linguistics:
ACL 2025, Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). Association for
Computational Linguistics, Vienna, Austria, 13253–13279. doi:10.18653/v1/2025.findings-acl.686
[52] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen.
2023. RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation. In Proceedings of
the 2023 Conference on Empirical Methods in Natural Language Processing, Houda Bouamor, Juan Pino, and Kalika Bali
(Eds.). Association for Computational Linguistics, Singapore, 2471–2484. doi:10.18653/v1/2023.emnlp-main.151

[Vista original de la página 21](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-21.png)

![Página PDF 21, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-21.png)


<!-- PDF page 22 -->

## Página PDF 22

22
Li et al.
[53] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024. CodeAgent: Enhancing Code Generation with Tool-Integrated
Agent Systems for Real-World Repo-level Coding Challenges. In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), Lun-Wei Ku, Andre Martins, and Vivek Srikumar
(Eds.). Association for Computational Linguistics, Bangkok, Thailand, 13643–13658. doi:10.18653/v1/2024.acl-long.737
[54] Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Abhik Roychoudhury. 2024. AutoCodeRover: Autonomous Program
Improvement. In Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis
(Vienna, Austria) (ISSTA 2024). Association for Computing Machinery, New York, NY, USA, 1592–1604. doi:10.1145/
3650212.3680384
[55] Ziyao Zhang, Chong Wang, Yanlin Wang, Ensheng Shi, Yuchi Ma, Wanjun Zhong, Jiachi Chen, Mingzhi Mao, and
Zibin Zheng. 2025. LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation. Proc.
ACM Softw. Eng. 2, ISSTA, Article ISSTA022 (June 2025), 23 pages. doi:10.1145/3728894
[56] Qianhui Zhao, Li Zhang, Fang Liu, Xiaoli Lian, Qiaoyuanhe Meng, Ziqian Jiao, Zetong Zhou, Jia Li, and Lin Shi.
2025. FastCoder: Accelerating Repository-level Code Generation via Efficient Retrieval and Verification. In 2025 40th
IEEE/ACM International Conference on Automated Software Engineering (ASE) (Seoul, Korea, Republic of). IEEE Press,
2299–2311. doi:10.1109/ASE63991.2025.00190
[57] Qixing Zhou, Jiacheng Zhang, Haiyang Wang, Rui Hao, Jiahe Wang, Minghao Han, Yuxue Yang, Shuzhe Wu, Feiyang
Pan, Lue Fan, Dandan Tu, and Zhaoxiang Zhang. 2026. FeatureBench: Benchmarking Agentic Coding for Complex
Feature Development. arXiv:2602.10975 [cs.SE] https://arxiv.org/abs/2602.10975
[58] Yifeng Zhu, Xianlin Zhao, Xutian Li, Yanzhen Zou, Haizhuo Yuan, Yue Wang, and Bing Xie. 2025. RepoSummary:
Feature-Oriented Summarization and Documentation Generation for Code Repositories. arXiv:2510.11039 [cs.SE]
https://arxiv.org/abs/2510.11039

[Vista original de la página 22](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-22.png)

![Página PDF 22, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens/page-22.png)
