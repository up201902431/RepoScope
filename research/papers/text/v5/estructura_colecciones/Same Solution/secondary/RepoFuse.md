# RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale

- source_pdf: ../../../../../pdf/Same%20Solution/secondary/RepoFuse.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RepoFuse: A Dual-Context Approach to Repository-Level Code
Completion at Industrial Scale
Ming Liang
Ant Group
China
liangming.liang@antgroup.com
Xiaoheng Xie
Ant Group
China
xiexiemyself@gmail.com
Gehao Zhang
Ant Group
China
gehaozhang1999@gmail.com
Xunjin Zheng
Ant Group
China
zhengxunjin.zx@antgroup.com
Wei Jiang
Ant Group
China
jonny.jw@antgroup.com
Chengpeng Wang
HKUST
China
cwangch@cse.ust.hk
Gang Fan
Ant Group
China
fan.gang.cn@gmail.com
Peng Di
Ant Group & UNSW Sydney
China
dipeng.dp@antgroup.com
Abstract
Repository-level code completion requires understanding complex
cross-file dependencies, yet existing approaches struggle to bal-
ance context richness with the sub-200ms latency requirements of
real-time IDE integration. We present RepoFuse, a dual-context
framework deployed at Ant Group1 serving 10,000+ developers
across 50+ million lines of code.
In a production deployment at Ant Group, RepoFuse maintained
an average latency of 156ms and improved completion acceptance
rate by 18%. This was accomplished through systematic categoriza-
tion of cross-file context into semantic context (structural depen-
dencies via lightweight static analysis) and similar context (func-
tionally analogous patterns via similarity search), combined with a
relevance-guided selection algorithm that optimizes the efficiency-
accuracy trade-off.
Benchmark evaluation on CrossCodeEval demonstrates 4.26 and
3.01 improvements in exact match scores for Python and Java re-
spectively, while using only 25% of baseline token requirements.
More significantly, our one-week A/B test with 80,000 comple-
tion requests revealed that developers particularly valued the dual-
context approach when working across microservice boundaries,
with 73% reporting reduced context switching between files. The
system successfully operates under production constraints with
distributed caching, real-time graph updates, and p95 latency un-
der 190ms, demonstrating that principled context categorization
1Ant Group is a leading global fintech company that operates Alipay and provides
digital financial services to over 1 billion users. The company employs over 10,000+ de-
velopers who annually contribute millions of lines of code across diverse microservice
architectures.
AntGroup
Correspondence
to:
Gang
Fan
<fangang@antgroup.com>,
Wei
Jiang<jonny.jw@antgroup.com>.
This work is licensed under a Creative Commons Attribution 4.0 International License.
FSE Companion ’26, Montreal, QC, Canada
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2636-1/2026/07
https://doi.org/10.1145/3803437.3805230
enables practical repository-level completion at industrial scale.We
have open-sourced RepoFuse at GitHub2.
CCS Concepts
• Software and its engineering →Software development tech-
niques; • Computing methodologies →Machine learning.
Keywords
Code completion, Large language model, Retrieval augmented gen-
eration, Program analysis
ACM Reference Format:
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Cheng-
peng Wang, Gang Fan, and Peng Di. 2026. RepoFuse: A Dual-Context
Approach to Repository-Level Code Completion at Industrial Scale. In
34th ACM Joint European Software Engineering Conference and Sympo-
sium on the Foundations of Software Engineering (FSE Companion ’26), July
05–09, 2026, Montreal, QC, Canada. ACM, New York, NY, USA, 12 pages.
https://doi.org/10.1145/3803437.3805230
1
Introduction
Code Large Language Models (CodeLLMs) have demonstrated sub-
stantial improvements in code completion tasks through next-token
prediction based on in-file context [5, 21]. However, real-world
software development increasingly involves complex, multi-file
codebases where understanding cross-file dependencies is essen-
tial for accurate completion. This has motivated repository-level
code completion [10, 23, 46], which extends completion capabilities
beyond individual files to leverage repository-wide context.
Recent advances in repository-level code completion have made
significant progress, with methods like RepoFormer [40] achieving
strong benchmark results through sophisticated retrieval mecha-
nisms. However, these approaches face two fundamental challenges
that limit their practical adoption.
Challenge 1: Uniform Context Treatment. Existing methods
largely treat all cross-file contexts as equivalent, missing the insight
2Open-sourced link:https://github.com/codefuse-ai/RepoFuse
568

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
that different context types serve distinct purposes. Some contexts
provide structural dependencies (semantic relationships), while
others offer functional patterns (similar implementations). This
uniform treatment leads to suboptimal context selection and fusion
strategies.
Challenge 2: Efficiency-Accuracy Trade-off. While complex
architectures can achieve higher benchmark scores, they often
require computational resources that exceed the constraints of real-
time IDE integration. Developer productivity studies suggest that
85% of users expect code completion responses within 200ms [37],
creating a critical efficiency requirement.
To address these challenges, we propose RepoFuse, which intro-
duces a systematic approach to context categorization and efficient
fusion. The central hypothesis is that explicitly distinguishing be-
tween semantic contexts (structural dependencies and API relation-
ships) and similar contexts (functionally analogous code patterns)
enables more effective context utilization while maintaining practi-
cal efficiency constraints. RepoFuse synthesizes two pivotal types
of cross-file context. The Similar Context identifies code segments
with similar functionality through code similarity analysis [43].
The Semantic Context provides semantic understanding of class
taxonomies and API interactions. To ensure efficiency, RepoFuse
employs Relevance-Guided Context Selection (RCS), which selec-
tively filters the most pertinent context to fit within limited token
windows while maintaining completion accuracy.
This work makes three distinct contributions to repository-level
code completion:
Systematic Context Categorization: We provide a principled
framework for categorizing cross-file contexts based on their se-
mantic roles, moving beyond uniform context treatment to enable
targeted utilization strategies.
Efficient Graph-based Context Extraction: The Repository-
Specific Semantic Graph (RSSG) captures essential code relation-
ships through lightweight static analysis, avoiding the computa-
tional overhead of full program analysis while preserving critical
semantic information.
Relevance-Guided Context Selection: The proposed algorithm
optimizes the trade-off between context completeness and inference
speed through relevance scoring, ensuring practical deployability
without sacrificing completion quality.
Evaluation on the CrossCodeEval benchmark across Python and
Java datasets indicates that RepoFuse achieves improvements of
4.26 and 3.01 in exact match scores for Python and Java respectively,
while requiring only 25% of the token window size to achieve 97.6%
of optimal performance. These results suggest a 1.3× speedup in
inference, validating the efficiency-focused design. More impor-
tantly, industrial deployment with 10,000+ developers shows an
18% improvement in acceptance rate while maintaining sub-200ms
latency, confirming the practical value of the approach.
2
Preliminaries
For convenience in demonstrating the approach, several important
concepts are introduced as preliminaries.
Definition 1. (Completion Environment) A completion environ-
ment 𝐸𝑛𝑣is (𝑠𝑒, 𝐹𝑟), where 𝑠𝑒is the content of the file under the edit
and 𝐹𝑟is the list of source code files.
Figure 1: Motivating example
Intuitively, the completion environment formalizes the scenario
of writing the code in a given repository. Following existing studies
on the code completion [46], we introduce the concepts of code
chunk and code chunk cover.
Definition 2. (Code Chunk) A code chunk 𝑐𝑘is a code snippet
containing a fixed line of code.
Definition 3. (Code Chunk Cover) Given a completion environ-
ment (𝑠𝑒, 𝐹𝑟), a chunk size bound ℓ𝑐𝑘, and a sliding step 𝜂, all the
source files are splited into a set of code chunks 
𝐶𝐶𝐾. The code chunk
obtained by sliding 𝜂lines forward from 𝑐𝑘is denoted as 𝑠𝑢𝑐𝑐(𝑐𝑘),
which effectively illustrates the coding outcome when considering the
code elements commonly shared between code chunk 𝑐𝑘.
In the completion environment (𝑠𝑒, 𝐹𝑟), the Code Chunks in 𝑠𝑒
that end at the completion point are denoted as unfinished code
chunk 𝑐𝑘∗, which reveals the code at the editing point. In a code
completion task, the aim is to generate and append a token sequence
to 𝑐𝑘∗according to the completion environment.
3
Methodology
This methodology addresses the core challenge of repository-level
code completion: effectively utilizing cross-file context while main-
taining practical efficiency constraints. We draw inspiration from
established software development practices where programmers
rely on two complementary information sources when working in
large codebases.
Semantic Understanding: Developers must comprehend the
project’s structural elements—API definitions, class hierarchies,
module interfaces, and dependency relationships. This semantic
knowledge enables accurate integration with existing code archi-
tecture and prevents interface mismatches.
Pattern Recognition: Developers frequently examine exist-
ing implementations with similar functionality to understand es-
tablished patterns, coding conventions, and successful design ap-
proaches within the codebase.
Motivating Example: Figure 1 illustrates why both context
types are essential. A developer implementing an API that uses a
config object needs semantic understanding of the object’s struc-
ture (fast_token_limit attribute definition) and similar context
showing how related configurations are typically implemented
569

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale
FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Retriever
Analyzer
Similar Context
coding
incomplete code
code in repo
def foo():
a = A()
a.run()
…
def goo():
a = B(3)
a.run()
…
def hoo():
…
a = A(b)
a.exe()
Semantic Context
Import
Relation
Call
Relation
Instance
Relation
LLMs
Scoring Strategy
. . .
Selection
code with 
completion
prompt
Relevance-based Context Selection
Figure 2: The workflow of RepoFuse
(self.fast_llm_model assignment pattern). Models focusing on
only one context type would miss critical information leading to
incorrect completions.
Building on this insight, RepoFuse introduces a dual-context
framework that systematically captures and fuses these comple-
mentary information sources. We define semantic context (SE) as
structured representations of code entities and their relationships,
and similar context (SI) as functionally analogous code segments
identified through similarity analysis. The integration of these con-
texts through the Relevance-Guided Context Selection (RCS) algo-
rithm enables effective repository-level completion within practical
token budget constraints.
Figure 2 depicts RepoFuse’s three-stage pipeline: semantic con-
text extraction via RSSG construction, similar context retrieval
through similarity analysis, and optimal context selection via RCS.
The following subsections detail each component’s design and im-
plementation.
3.1
Semantic Context
Definition 4. (Semantic Context) Given a completion environ-
ment 𝐸𝑛𝑣:= (𝑠𝑒, 𝐹𝑟), a SE Γ𝑠𝑒is a triple (Σ𝐹, Σ𝐶, Σ𝑀), where Σ𝐹, Σ𝐶,
and Σ𝑀are the signatures of functions/methods, classes/interfaces,
and modules/packages, respectively. Specifically, the signature of a
class/interface is the concatenation of the signatures of its fields and
methods, while the signature of a module/package is the concatenation
of the signatures of its classes/interfaces, including their fields and
methods, as well as the module’s functions.
To construct the SE Γ𝑠𝑒= (Σ𝐹, Σ𝐶, Σ𝑀) effectively, we employ a
specialized tool, the Repo-specific Semantic Graph (RSSG). This
graph extends the traditional Code Property Graph[42] by focusing
specifically on context retrieval for code completion tasks within
repositories.
Constructing RSSG: The graph construction begins with pars-
ing each code file’s Abstract Syntax Tree (AST). We extract vital
code entities such as modules/packages, classes/interfaces, func-
tions/methods, and variables/fields:
• A module/package entity includes its file path.
• A class/interface entity stores its name, signature, and file location.
• A function/method entity captures its name, signature, body, and
file location.
• A variable/field entity holds its name, declaration, and file location.
Using these entities, we establish both natural containment re-
lations and more complex relationships among them. These rela-
tionships are formed through symbol resolution, type inference,
and dataflow analysis, constructing a comprehensive semantic net-
work within the repository. The edges representing these relations
are meticulously recorded in the graph, detailing the connections
# UserManagement/UserService/user_service.py
from UserManagement.models import User
from UserManagement import UserService
from UserManagement.helpers import log_activity
class UserManager:
def __init__(self):
self.user_service = UserService()
def authenticate_user(self, user: User) -> bool:
result = self.user_service.
class User(BaseModel):
id: int
name: str
class UserService:
def __init__(self) -> None
def register(self, user: User) -> AuthToken
def authenticate(self, user_id: int) -> bool
def log_activity(activity_details: dict, log_path: str) -> None
(b) Semantic Context
se1
se2
se3
@self.app.post("/login")
def login(user: User) -> bool:
result = self.user_service.authenticate(user.id)
return result
@self.app.get("/status")
def create_user(self, user: User) -> AuthToken:
auth_token = self.user_service.register(user)
return auth_token
manager = UserManager()
if __name__ == "__main__":
uvicorn.run(manager.app, port=8000, host="0.0.0.0")
(a) Similar Context
si1
si2
(c) Current file
authenticate(user.id)
???
complete
Similar Code
Class & Method
Figure 3: Illustrative example of semantic and similar con-
texts
among various code entities. The types of relations are summarized
in table 1.
Table 1: Relation types in RSSG
Type
Components
Type Inference
Object Creation, Inheritance, Overrides, Field
Access
Structural Dependency
Imports, Composition
Control Flow
Calls, Def-Use
Utilizing Semantic Relations for Context Retrieval: For an
incomplete cursor line within a file, we identify the innermost node
in RSSG that encompasses it. This node acts as the starting point for
extracting SE information. We retrieve all neighboring nodes of this
central node and concatenate them into a candidate list for context
aggregation. For each candidate, we append their signatures to the
final SE list. This process results in a nuanced and contextually rich
representation of the code segment under consideration.
Consider the example in fig. 3. In the file shown in fig. 3(c), we
derive three import statements, which import two classes and meth-
ods from other modules in the repository. These import statements
define which tokens are available for use in the current completion
environment. After localizing the definitions of the imported classes
and methods, we extract their signatures to form a SE, as shown in
fig. 3(b). In this example, we obtain Γ𝑠𝑒= (𝑠𝑒3, (𝑠𝑒1,𝑠𝑒2), ∅). Due to
space constraints, a full package signature example is omitted.
The incorporation of such detailed semantic relationships is cru-
cial for improving the accuracy of code completion. By understand-
ing the intricate relationships and dependencies among various
code entities, the model can make more informed and contextually
appropriate predictions.
3.2
Similar Context
Definition 5. (Similar Context) A SI Γ𝑠𝑖is a set of code chunks,
where a code chunk 𝑐𝑘∈Γ𝑠𝑖is highly similar to an unfinished code
chunk 𝑐𝑘∗in the currently edited file.
To compute the SI, we analyze the currently edited file to identify
unfinished code chunks (𝑐𝑘∗). We then discover several similar code
chunks in other source files, whose successors provide informative
guidance for completion. This process is formalized through the
concept of the SI.
570

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
In fig. 3(a), the SI is derived based on the content of the current
file (fig. 3(c)). Specifically, the code chunks 𝑒𝑐1 and 𝑒𝑐2 share similar
tokens with the current file, such as "user" and "service." These high
similarities indicate that the chunks in the SI should be prioritized
during the prompting process, as they are likely to exhibit similar
or identical functionalities to the code in the current file.
3.3
Relevance-Guided Context Selection
As demonstrated by section 3.1 and section 3.2, the two kinds of
contexts offer insightful clues to guide the completion for a specific
completion environment. However, code completion has a high
requirement on the efficiency in real-world scenarios. Simply con-
catenating the SE with the SI in the prompt construction would
result in a lengthy prompt, introducing extra overhead in the LLM
inference phase.
To efficiently utilize the two contexts, RCS merges the two con-
texts into a prompt of fixed size, formalized by the concept of
Optimized Dual Context (ODC) and Relevance Score as follows:
Definition 6. (Optimized Dual Context Γ𝑜𝑑𝑐) Given a SE Γ𝑠𝑒=
(Σ𝐹, Σ𝐶, Σ𝑀), a SI Γ𝑠𝑖, and the last chunk 𝑐𝑘∗at the end of the cur-
rently edited file, an ODC is a set Γ𝑜𝑑𝑐⊆(Γ𝑠𝑒∪Γ𝑠𝑖) introducing the
best code completion performance. It satisfies the following constraints:
• (Size constraint) The total length of all items in Γ𝑜𝑑𝑐is bounded
by the token window size 𝐿, i.e., Í
𝑒∈Γ𝑜𝑑𝑐len(𝑒) ≤𝐿, where
the function len measures the number of tokens.
• (Performance constraint) The items in Γ𝑜𝑑𝑐are selected such
that the code completion performance metrics is the highest
with the prompt constructed from Γ𝑜𝑑𝑐.
Reliance on post-execution metrics such as the EM value for eval-
uating code completions often fails to provide actionable insights in
real-time scenarios, as these metrics only assess outcomes after all
computations are completed. To address this limitation, we use the
relevance score 𝑟𝑐𝑘∗as a proactive indicator that can approximate
the value of the outputs before the actual code completion occurs.
Definition 7. (Relevance Score 𝑟𝑐𝑘∗) Given a code chunk inside
the repository, 𝑟𝑐𝑘∗measures the relevance between the current code
chunk and 𝑐𝑘∗.
This score can be computed using various distances and light-
weight embedding models, and plays a pivotal role in predicting
the performance of code completions. We evaluate the impact of
different scoring functions in section 5.3.
For computation of ODC, accurately assessing the completion
performance of each potential subset is essential to generate Γ𝑜𝑑𝑐.
This task mirrors the subset selection problem, recognized as an
NP-hard problem [14]. Due to its NP-hard classification, procur-
ing a direct optimal solution becomes computationally untenable
for large datasets. To address this, we have developed a relevance-
guided approximate algorithm that employs a greedy strategy en-
hanced by a priority queue to efficiently manage spatial constraints.
(section 3.3)
[H] [1] SE Γ𝑠𝑒, SI Γ𝑠𝑖, Current code chunk𝑐𝑘, Token Window Size
𝐿ODC Γ𝑜𝑑𝑐Γ𝑜𝑑𝑐←∅𝑈←Γ𝑠𝑒∪Γ𝑠𝑖Sort𝑈by descending relevance
score 𝑟𝑐𝑘∗Remove duplicate candidates from 𝑈𝑙𝑒𝑛𝑔𝑡ℎ←0 each
𝑒∈𝑈𝑙𝑒𝑛𝑔𝑡ℎ+ len(𝑒) ≤𝐿Add 𝑒to Γ𝑜𝑑𝑐𝑙𝑒𝑛𝑔𝑡ℎ←𝑙𝑒𝑛𝑔𝑡ℎ+ len(𝑒)
Γ𝑜𝑑𝑐
In the example shown in fig. 3, the RCS strategy selects 𝑠𝑒1, 𝑠𝑒2,
and 𝑠𝑖1 to create the ODC. RepoFuse then follows the implementa-
tion in𝑠𝑖1 and generates a token sequence authenticate(user.id),
which invokes the method authenticate on self.user_service,
passing user.uid as arguments. The method authenticate and
the fields uid of UidTok are all present in the SE. Guided by the
ODC, RepoFuse can learn from similar implementations and choose
valid program constructs, thereby achieving better completion per-
formance at the repository level. For a more comprehensive un-
derstanding of the RCS setting and its implementation, refer to
section 4.4.
4
Experimental Setup
This section presents a comprehensive evaluation framework de-
signed to assess both the effectiveness and efficiency of RepoFuse.
We detail the benchmark datasets, baseline methods, evaluation
metrics, and implementation specifics that enable rigorous compar-
ison with existing approaches.
4.1
Benchmark
We evaluate RepoFuse using the CrossCodeEval benchmark [10],
which specifically targets repository-level code completion by en-
suring completion tasks require cross-file context understanding.
The benchmark includes repositories from four programming lan-
guages (Python, Java, C#, and TypeScript), with each completion
example verified to contain at least one cross-file API reference.
For evaluation, focus is placed on Python and Java subsets, which
provide substantial datasets: 471 Python repositories with 1,368
files and 2,665 completion examples, and 239 Java repositories with
745 files and 2,139 examples. This selection balances evaluation
comprehensiveness with computational feasibility while covering
the most widely-used languages in industrial development. The
approach’s language-agnostic design ensures generalizability to
other programming languages without modification.
4.2
Baselines
To evaluate RepoFuse comprehensively, we compare against three
established open-source retrieval-augmented methods that operate
without pre-training requirements. This enables fair comparison un-
der similar computational constraints. While state-of-the-art meth-
ods like RepoFormer [40] demonstrate superior benchmark per-
formance, we focus on approaches readily deployable in resource-
constrained environments typical of industrial IDE integration.
The baseline selection addresses the practical deployment con-
siderations that often limit the adoption of research prototypes:
• CCFinder [11]: Constructs project context graphs through
import statement analysis and retrieves k-hop neighbors
(k=2) of code entities. This graph-based approach provides a
direct comparison for the RSSG methodology, though limited
to Python.
• RG-1 and RepoCoder [46]: Implements iterative retrieve-
generate pipelines with fixed token windows and text similarity-
based retrieval. RG-1 represents single-iteration results, while
RepoCoder uses 2 iterations. This comparison highlights the
efficiency gains of the relevance-guided selection over itera-
tive approaches.
571

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale
FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
• RLPG [34]: Generates example-specific prompts using learned
prompt generators and classifiers. We utilize RLPG’s gener-
ated prompts to input maximal context, providing compari-
son with learned context selection strategies (Java only).
These baselines represent different paradigms in repository-level
completion: graph-based context extraction (CCFinder), iterative
refinement (RepoCoder), and learned prompt generation (RLPG),
enabling comprehensive evaluation of the dual-context approach.
4.3
Evaluation Metrics
For evaluation, we employed the following metrics, the first three
follow the methodology outlined in [10].:
Exact Match (EM): This metric assesses whether the generated
code exactly matches the reference code.
Edit Similarity (ES): This metric measures the similarity between
the generated code and the reference code, calculated using the
Levenshtein distance.
F1 Score for Identifier Match (ID-F1): This evaluates the preci-
sion and recall of correctly predicted identifiers.
Speedup: This metric measures the percentage of inference speed
improvement by reducing prompt lengths, reflecting the model’s
efficiency gains.
4.4
Implementation Details
Context Construction: The context construction process imple-
ments the theoretical framework described in Section 3. For seman-
tic context (SE), we construct the RSSG using the process detailed
in section 3.1, extracting function signatures, class definitions, and
module interfaces through static analysis. For similar context (SI),
we utilize CrossCodeEval’s provided crossfile_context, which em-
ploys BM25 similarity with chunk size 𝑙𝑐𝑘= 10 and sliding step
𝜂= 10. We retain the top-5 most similar chunks per completion
target, ensuring consistent comparison across all methods. The
Relevance-Guided Context Selection (section 3.3) then generates
the optimized dual context Γ𝑜𝑑𝑐.
Infilling Setup Justification: We employ the infilling para-
digm where models complete code given both prefix and suffix
contexts. While this differs from typical IDE scenarios with only
prefix context, this choice is methodologically sound for several
reasons:
Standardized Evaluation: Infilling provides a controlled evalua-
tion framework that eliminates variability from suffix prediction,
enabling fair comparison across methods as established in recent
benchmarks [10].
Model Alignment: Modern CodeLLMs like CodeLlama [32] and
StarCoder [21] are explicitly trained with fill-in-the-middle objec-
tives, making infilling evaluation representative of their designed
capabilities.
Upper Bound Analysis: Infilling represents the theoretical upper
bound of context utilization, helping isolate the effectiveness of
different context selection strategies from the challenges of suffix
generation.
Industrial Validation: Critically, industrial deployment demon-
strates that insights from infilling experiments transfer effectively
to practical left-to-right completion, achieving 18% acceptance rate
improvement in real-world usage.
# Here are some relevant code fragments from other files of the repo:
# the below code fragment is found in [Code_Chunk_1_File_Path]
# [Code_Chunk_1_Content]
# the below code fragment is found in [Code_Chunk_2_File_Path]
# [Code_Chunk_2_Content]
……
# the below code fragment is found in [Code_Chunk_n_File_Path]
# [Code_Chunk_n_Content]
Figure 4: Prompt construction of ODC
Figure 5: Token distribution of different context types (sorted
by length)
The relative performance differences between methods remain
consistent across both evaluation paradigms, validating the experi-
mental approach for research purposes while acknowledging the
limitation for direct IDE performance prediction.
We ultimately input the Prompt to the model as follows:
<fim_begin> + [crossfile_context] + [prefix] + <fim_hole> +
[suffix] + <fim_end>
where <fim_begin>, <fim_hole>, and <fim_end>are special to-
kens in the Fill-In-The-Middle setting, and their specific content
varies by model. The [prefix] and [suffix] represent the content
before and after the line to be completed, respectively. The [cross-
file_context] is composed of the set ODC Γ𝑜𝑑𝑐. Specifically, we
concatenate each element in the set in the following format, as
illustrated in fig. 4:
Model Selection: The repository collected in CrossCodeEval
spans from March 5, 2023 to June 15, 2023. To prevent potential
data leaks, CodeLLMs released before mid-2023 were selected. They
are StarCoderBase with 1B, 3B and 7B size [21], DeepSeek-Coder
with 1B and 7B size [16], which are trained with fill-in-the-middle
ability on a large corpus of multilingual code, GitHub issues and
other code related information. The evaluation focused on models
that support 8k input tokens to incorporate information from all
cross files.
RCS Setting: As discussed in section 3.3, we evaluate Token
Window Size varies from 256 to 4096. We represent the crossfile
context length distribution of the evaluated data in fig. 5. In the
context of a 4096-token length, the majority of samples remain
untruncated, allowing us to approximate it as “Unlimited”. We have
set the maximum sequence length for infile context to 2048 tokens,
thereby preventing any truncation of infile information that could
affect the results.
To evaluate the RCS score function𝑟𝑐𝑘∗, we consider four distinct
Score Functions as follows:
572

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
Table 2: Performance comparison with baselines on the CrossCodeEval dataset for Python and Java datasets over five CodeLLMs.
RepoFuse’s token windows are set to 1024 and 4096, baselines’ are set to 4096. Numbers are shown in percentage (%), with the
best performance highlighted in bold.
(a) Python dataset
Methods
DeepSeek-Coder-1B
DeepSeek-Coder-7B
StarCoder-1B
StarCoder-3B
StarCoder-7B
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
RG-1_4096
31.59
73.55
66.65
38.61
77.7
72.21
29.49
72.41
65.24
32.95
74.48
68.5
35.61
76.12
69.28
RepoCoder_4096
37.49
76.45
70.88
44.92
80.71
76.41
32.42
73.32
67.14
36.62
76.06
70.53
40.15
77.94
50.13
CCFinder_4096
36.96
74.97
69.64
44.47
79.48
75.94
33.06
73.21
67.29
37.60
76.14
71.35
41.16
77.80
73.62
RepoFuse_1024
38.24
76.13
71.19
46.34
81.10
77.88
34.67
74.72
69.21
39.70
77.77
73.14
42.96
79.80
75.40
RepoFuse_4096
40.41 77.76 73.27 49.64 82.64 80.17
36.47 75.55 70.79 42.40 78.96 75.26 45.63
80.71 77.27
(b) Java dataset
Methods
DeepSeek-Coder-1B
DeepSeek-Coder-7B
StarCoder-1B
StarCoder-3B
StarCoder-7B
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
EM
ES
ID-F1
RG-1_4096
40.21
78.88
43.41
50.49
83.90
80.41
33.05
76.44
69.78
40.16
79.79
74.51
44.04
82.18
77.52
RepoCoder_4096
40.81
79.12
73.85
49.79
83.71
79.66
33.8
76.73
70.05
40.77
80.2
74.92
44.88
82.63
78.11
RLPG_4096
41.94
78.58
74.00
52.64
83.32
81.04
35.72
76.38
70.44
41.51
78.52
74.11
48.64
82.00
78.24
RepoFuse_1024
42.87
79.40
74.46
52.17
84.09
81.09
36.09
77.35
71.41
42.64
80.40
75.64
47.41
82.61
78.74
RepoFuse_4096
45.82 80.78 76.40 55.59 85.44 82.91
37.82 77.44 71.94 44.51 80.87 76.52 49.98
83.30 80.06
Oracle: In this idealized scenario, each retrieved context 𝑒∈𝑈is
used as a prompt for the language model, and the resulting code’s
Edit Similarity metric with the Ground Truth is taken as its rele-
vance score. The Oracle represents the theoretical best-case perfor-
mance for any Score Function but is impractical for real-world use
due to significant computational demands.
Semantic Similarity: We encode the semantic representation of
each context𝑒and the unfinished code chunk𝑐𝑘∗using an encoding
model. The cosine similarity of these embeddings serves as the score.
We employ encoding models such as CodeBERT [12], CodeSage
[45] and UniXcoder [15].
Lexical Similarity: This score is determined using simple textual
comparisons, particularly Jaccard Similarity and Edit Similarity
measures.
Random: Scores are assigned randomly, serving as a baseline to
underscore the effectiveness of the other Score Functions.
5
Results and Analysis
This section outlines the experimental results obtained from deploy-
ing RepoFuse and provides a detailed analysis of its performance
in comparison with established baseline methods. Additionally, we
evaluate RepoFuse in large-scale industrial scenarios, incorporat-
ing rigorous efficiency assessments, extensive A/B testing. These
experiments underscore RepoFuse’s ability to meet the demands
of real-world applications, proving it is well-suited for industry
environments, particularly in terms of resource efficiency.
5.1
Performance Analysis
Comparison with Baseline Methods The evaluation strategy
involved a comprehensive comparison with baseline approaches
specified in section 4.2. Given the pivotal role of information se-
lection in repository-level code completion, we standardized token
window size across all baseline methods to 4096 tokens to ensure a
fair assessment.
For a robust evaluation of RepoFuse, we evaluate across dif-
ferent token window sizes and utilize the CrossCodeEval datasets
for both Python and Java languages. As shown in table 2, the out-
comes clearly demonstrate that RepoFuse excels in performance.
Specifically, within the Python dataset, RepoFuse exhibited a 4.26
improvement in EM and a 3.79 increase in identifier F1-score. In the
Java dataset, it showed a 3.01 improvement in EM and a 2 increase in
identifier F1-score compared to the state-of-the-art baseline meth-
ods.
Table 3: Performance of RepoFuse on TypeScript and C#
Model
TypeScript
C#
EM
ES
ID-F1
EM
ES
ID-F1
DeepSeek-Coder-1B
31.88
72.51
68.80
50.23
83.74
77.27
DeepSeek-Coder-7B
39.66
77.45
74.62
58.99
86.73
82.52
Starcoder-1B
28.10
70.36
65.58
37.82
77.44
71.94
Starcoder-3B
32.81
73.77
69.99
44.51
80.87
76.52
Starcoder-7B
37.22
76.40
73.58
49.98
83.30
80.06
Remarkably, even when configured with a reduced token window
size of 1024 tokens, RepoFuse consistently exceeded the perfor-
mance of all baseline methods using the larger 4096 token window
size. This underscores the robustness of the RCS strategy, which
enhances code completion accuracy even under stringent input
constraints.
Comprehensive Performance Across Other Languages For
detailed performance results of RepoFuse across other language
datasets in CrossCodeEval for all code language models, please
refer to table 3. Additionally, in real-world applications, RepoFuse
573

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale
FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Table 4: Inference efficiency comparison of RepoFuse at dif-
ferent prompt lengths on the Python subset using StarCoder-
7B. ODC w/o RCS refers to using both SI and SE with the full
prompt length (4096 tokens).
Methods
Length
ES
ID-F1
Speedup
SI
4096
76.25
70.04
1x
SE
4096
78.72
74.75
1x
ODC w.o RCS
4096
80.71
77.27
1x
ODC with RCS
2048
80.37
76.59
1.19x
ODC with RCS
1024
79.80
75.40
1.30x
has been successfully employed for code completion across mul-
tiple programming languages, demonstrating its versatility and
effectiveness.
Inference Efficiency with RCS Strategy: While RepoFuse
with the 4096-token ODC configuration provides the highest ac-
curacy, it significantly slows down inference. To address this, we
evaluated RepoFuse with ODC along with reduced token windows
of 2048 and 1024 tokens using StarCoder-7B. As shown in table 4,
when ODC with RCS on 1024 tokens achieves a 1.3x speedup, with
only a slight drop in ES from 80.71 to 79.80 and ID-F1 from 77.27 to
75.40. Similarly, for 2048 tokens, the speedup improvement is 1.19x,
with a minor reduction in performance.
Despite the shorter prompt lengths, RepoFuse using ODC with
RCS (1024 tokens) still outperforms RepoFuse only using SI or SE
with 4096 tokens, improving SI’s EM by 19.4%. This demonstrates
that RepoFuse with RCS strikes a balance between high accuracy
and faster inference.
The RCS configuration is highly effective in real-world scenarios
where speed and efficiency are critical. By reducing prompt size,
RCS still keeps the context richness, offering significant speed im-
provements with minimal performance loss, making it ideal for
latency-sensitive applications (i.e., IDE).
5.2
Ablation Study
Effectiveness of ODC: To analyze the effectiveness of ODC in
RepoFuse, we conducted an ablation study, the results of which
are illustrated in fig. 6. We evaluated various models under three
distinct context settings with token window sizes varying from 256
to 4096.
As previously discussed in section 4.4, maintaining minimal in-
formation loss at a token window size of 4096 enables an effective
evaluation of the impact of different contexts on model perfor-
mance. As illustrated in fig. 6, the ODC consistently outperforms
the baseline SI and SE solely across various CodeLLMs. Specifically,
within the ES metric at this token window size, ODC demonstrates
a significant improvement, increasing from 3.49 to 4.73 over the SI
and from 1.98 to 2.49 over the SE.
When the token window size is reduced to 256, which is fully oc-
cupied by the retrieved context of all the three settings, both SI and
SE display closely matched ES performance. However, ODC still
achieves superior results, highlighting that similar and semantic
information are complementary and their integration significantly
boosts performance. This advantage is evident even at a token win-
dow size of 1024, where ODC continues to outperform SI and SE,
particularly when the window size is expanded to 4096, underscor-
ing ODC’s robustness across varying context sizes.
Convergence Analysis: The convergence trends for exact match
instances within the CodeLLMs are highlighted in fig. 7. Analysis of
the three context types—SI, SE, and ODC— in DeepSeek-Coder-7B
reveals that SE accounts for 1213 exact matches, SI for 1029, and
ODC leads with 1303. The superior performance of ODC can be
attributed to two primary factors. Firstly, by amalgamating contex-
tual information from both SI and SE, ODC provides a richer, more
complementary context, enabling CodeLLMs to prioritize the most
pertinent information for diverse sample types. Secondly, ODC
resolves certain cases that cannot be adequately addressed using
exclusively SI or SE. In fig. 7, 47 such cases are evident where the
combined insights from both contexts are essential for precise code
completion.
Table 5: Performance comparison of Relation Types in RSSG
Over CodeLLMs.
Model
Relation Type
EM
ES
#_Chunk
StarCoder-1B
None-SE
24.02 68.62
0
StructuralDependency 32.50 73.15
3.3
ControlFlow
24.32 68.68
0.8
TypeInference
25.93 69.68
0.4
Full-SE
33.28 73.41
4.5
StarCoder-3B
None-SE
28.11 71.05
0
StructuralDependency 38.09 76.28
3.3
ControlFlow
28.63 71.14
0.8
TypeInference
30.24 72.18
0.4
Full-SE
38.91
76.7
4.5
StarCoder-7B
None-SE
30.21 72.75
0
StructuralDependency 41.73 78.50
3.3
ControlFlow
30.58 72.96
0.8
TypeInference
32.46 74.00
0.4
Full-SE
42.29 78.72
4.5
DeepSeek-Coder-1B
None-SE
26.90 69.44
0
StructuralDependency 37.79 75.11
3.3
ControlFlow
27.09 69.66
0.8
TypeInference
29.08 70.64
0.4
Full-SE
38.35 75.47
4.5
DeepSeek-Coder-7B
None-SE
33.10 73.95
0
StructuralDependency 45.40 80.17
3.3
ControlFlow
33.70 74.15
0.8
TypeInference
35.53 75.51
0.4
Full-SE
46.08 80.42
4.5
Impact of Different Edges in RSSG: We conducted ablation
studies on the CrossCodeEval Python dataset to evaluate how dif-
ferent relation types in RSSG affect RepoFuse’s performance. As
shown in table 5, RepoFuse with full SE consistently achieved the
highest EM and ES scores and RepoFuse with any relation contexts
from RSSG outperformed baseline (None-SE). For StarCoder-7B,
the StructuralDependency edge type performed closest to full
SE, with an EM of 41.73 (98.67% of full SE’s 42.29). In contrast,
ControlFlow and TypeInference provided smaller gains, with
EM scores of 30.58 and 32.46, respectively. For DeepSeek-Coder-7B,
574

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
Figure 6: ES performance for SI, SE, and ODC on CrossCodeEval Python dataset across different token windows.
50
23
47
727
240
112
16
SE
SI
ODC
StarCoder-3B
49
29
47
882
269
105
13
SE
SI
ODC
DeepSeek-Coder-7B
Figure 7: Convergence analysis of exactly matched cases by
SE, SI, and ODC.
Figure 8: EM values across token windows using ODC with
diverse scoring functions.
Figure 9: EM values using different arranging strategies (H2L,
L2H, Random).
StructuralDependency was especially effective, reaching 98.52%
of full SE’s EM score and matching 99.68% ES.
Since CrossCodeEval is designed for API-level completion, Struc-
turalDependency is particularly beneficial, as Imports type pro-
vides crucial context for such tasks. However, in real-world applica-
tions, where scenarios like multi-line completion are more common,
other relation types, such as TypeInference and ControlFlow,
play a more significant role. These more complex scenarios require
deeper contextual understanding, where different types of relations
could outperform structural information alone.
5.3
Evaluation of RCS Score Functions
We analyzed various scoring functions pivotal for RCS within the
specified token window size, as discussed in section 3. According to
fig. 8, the Oracle function significantly outperforms others at a to-
ken window size of 512, while differences among strategies become
negligible at 2048. This observation underscores the importance of
scoring functions in enhancing context relevance, and improving
inference efficiency in CodeLLMs. UniXcoder surpasses other score
functions in effectiveness, and Random function and CodeBERT
exhibit the lowest performance, aligning with the findings in [23].
The multi-modal pre-training of UniXcoder, which integrates Ab-
stract Syntax Trees (AST) and comments, effectively complements
SE to enhance understanding in CodeLLMs.
5.4
Impact of Contexts Ordering
Evaluating the impact of the order in which contexts are placed
within prompts is crucial for optimizing the performance of CodeLLMs.
We assessed the EM performance using three distinct strategies for
arranging contexts—LowToHigh, HighToLow, and Random—across
various token window sizes from 256 to 4096 tokens using the
StarCoder-1B model. The findings, as illustrated in fig. 9, show
minimal differences in performance among these strategies. Specif-
ically, at a token window size of 512, both HighToLow and Random
strategies slightly outperform the LowToHigh arrangement. Con-
versely, at the maximum token window size of 4096, Random shows
a marginal advantage over the other strategies. The results for all
strategies are nearly identical in other token window sizes. This
analysis suggests that CodeLLMs may be relatively indifferent to the
order of contexts within prompts, indicating that the specific order
of contexts may not significantly influence the overall effectiveness
of the model as previously thought.
5.5
Online A/B Testing in Industrial
Environment
To evaluate the effectiveness of the repository-level code comple-
tion approach, a comprehensive one-week online A/B test was
575

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale
FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
conducted within a large-scale industrial environment. The deploy-
ment involved 5,000 Java backend developers working on enterprise
microservice architectures, collecting 80,000 code completion re-
quests and approximately 400,000 developer interactions.
Deployment Context and Architecture: RepoFuse was in-
tegrated into the company’s internal IDE plugin infrastructure,
serving code completions for a diverse codebase spanning over
50 million lines of code across 2,000+ repositories, with approxi-
mately 5,000 active developers. The system operates in a distributed
architecture with:
Real-time RSSG updates triggered by repository commits
Distributed caching for frequently accessed semantic contexts
Load-balanced inference servers maintaining p95 latency under
190ms
Developer Experience and Qualitative Insights: Beyond
quantitative metrics, we collected developer feedback through post-
completion micro-surveys and IDE telemetry:
Cross-service Integration: Developers reported that RepoFuse
particularly excelled when working across microservice boundaries,
with the SE providing crucial API signatures and the SI offering
implementation patterns from similar services.
Reduced Context Switching: 73% of surveyed developers noted
reduced need to switch between files or documentation, as the dual-
context approach provided both "what to use" (SE) and "how to use
it" (SI).
Learning from Codebase: Junior developers particularly valued
the SI, which helped them discover and adopt team coding patterns
without explicit documentation.
Quantitative Results: User acceptance rate serves as the pri-
mary metric, measuring the proportion of suggestions developers
find valuable enough to accept. Following the methodology in [31],
we define:
acceptance_rate = Accepted&Valid Requests Count
Valid Requests Count
where Valid Requests have exposure time > 750ms (ensuring
developers had time to evaluate suggestions).
The A/B test allocated traffic as: 40% baseline, 20% each for SI-
only, SE-only, and full ODC. Results showed:
• SI Only: 12% improvement - particularly effective for imple-
menting common patterns
• SE Only: 10% improvement - excelled in correct API usage
• ODC (Full RepoFuse): 18% improvement - synergistic ben-
efits of both contexts
Latency and Resource Utilization: Critical to adoption was
maintaining performance under production load:
Average end-to-end latency: 156ms (well below the 200ms thresh-
old)
RSSG construction: 2.3ms average per file update
Context retrieval: 18ms for SI, 12ms for SE
Model inference: 124ms average
These results validate that RepoFuse successfully balances con-
text richness with practical latency constraints, achieving signifi-
cant improvements in developer productivity while maintaining
the responsiveness required for seamless IDE integration.
Table 6: Acceptance rate based on usage of SI, SE and ODC.
Method
SI
SE
Req Count
Accept Rate
Baseline
N
N
309102(40%)
𝑋
SI Approach
N
Y
80212(20%)
1.12 × 𝑋
SE Approach
Y
N
79220(20%)
1.10 × 𝑋
ODC Approach
Y
Y
78219(20%)
1.18 × 𝑋
6
Related Work
Code Language Models: In recent years, CodeLLMs have found
extensive application in the field of software engineering, notably
contributing to the enhancement of development efficiency, with
code completion scenarios being particularly prominent [38]. A
diverse range of Pretrained CodeLLMs has been deployed in this
context (Codex [5], StarCoder [21], CodeGen [28], CodeLlama [32],
In-Coder [13], SantaCoder [1], CodeGeex [49], CodeFuse [9], Pan-
guCoder [8], DeepSeek-Coder [16]). Many of these works have
harnessed the Transformer Decoder architecture for training in
the Next Token Prediction task using source code data, allowing
them to directly apply their models to Code Completion tasks. Ad-
ditionally, certain studies have incorporated the Fill-in-the-Middle
task into their training stage ([4, 16, 21, 32]) to better align with
real-world code completion scenarios. Most of these CodeLLMs
mainly concentrate on local information within individual files
and lack comprehensive support for entire code repositories except
DeepSeek-Coder [16], which make the first attempt to incorporate
repository-level data construction in pre-training stage.
There is a growing research interest in expanding the token
window size of large language models to include more context
within prompts[6, 19, 27, 36]. Notable advancements include models
like Gemini-Pro[35], which can handle over 1 million tokens in a
single prompt. While recognizing the potential benefits of such
models, particularly in contexts requiring extensive information
processing, this research focuses on optimizing code completion
within IDEs. These environments are often constrained by limited
computational resources. Therefore, the significant results achieved
with smaller-scale language models and a truncation size of 512
tokens are especially relevant for real-world applications where
efficiency and resource management are critical.
Repository-level Context-aware Code Completion: Research
into repository-level analysis has gained traction as a method for un-
derstanding code at scale [2, 3, 17, 20]. In the context of repository-
level code completion, numerous works aim to utilize the vast
amount of code available in repositories to aid CodeLLMs in gen-
erating better completions [10, 23, 29]. Early approaches focused
on retrieval-based methods: [46] propose an iterative retrieval gen-
eration pipeline for high-quality prompts, [39] introduce RLCoder
using reinforcement learning to train retrievers without labeled
data, while [34] generate example-specific prompts using a learned
Prompt Proposal Generator. [33] employ a fine-tuned Fusion-in-
Decoder model to integrate repository information, and [11] utilize
a Cross-file Context Finder based on Project Context Graphs, com-
pressing cross-file information into embedding representations for
enhanced code generation.
576

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
Alternative approaches explore diverse information sources: [44]
introduce private-library-oriented completion using API documen-
tation, [7] retrieve semantic context through data-flow analysis, and
[26] leverage similar code snippets from collected databases. Graph-
based methods have also emerged, with GraphCoder [24] intro-
ducing a retrieval-augmented framework leveraging Code Context
Graphs to capture control-flow and data dependencies.CodeFuse-
Query [41] employs a Datalog-based query system over structured
code data models, enabling large-scale extraction of reusable code
facts that can serve as repository-level context.
Recent advances have significantly improved repository-level
code completion performance and efficiency. RepoFormer [40]
achieves state-of-the-art performance through selective retrieval
augmentation, demonstrating that not all cross-file contexts are
beneficial. While RepoFormer excels through sophisticated selective
retrieval mechanisms, RepoFuse takes a complementary approach
by focusing on the quality and type of retrieved context rather
than just retrieval decisions. RepoHyper [30] introduces a graph-
based search-expand-refine approach using Repo-level Semantic
Graphs with GNN-based link prediction, while GraphCoder [25]
similarly leverages code context graphs. Although these graph-
based methods excel at capturing structural relationships, they
incur significant computational overhead for graph construction
and traversal. Hierarchical Context Pruning [48] further improves
prompt construction efficiency by proposing a function-level prun-
ing strategy that maintains topological dependencies while reduc-
ing prompt length. Recent work has also explored IDE integration
and tool-based approaches. [22] focus on integrating IDE-derived
static context to improve coding tool precision through static analy-
sis, while [47] introduce CodeAgent, utilizing tool-integrated agent
systems for real-world coding challenges. RepoExec [18] and recent
benchmarks [10, 23] have highlighted the importance of executable
code generation and cross-file understanding, yet as fast response
development scenarios require efficient approaches, many existing
methods may not be applicable in practice, highlighting the need
for solutions like RepoFuse that strike an optimal balance between
effectiveness and efficiency while maintaining sub-200ms latency
requirements and achieving an 18% improvement in acceptance
rate during industrial deployment.
7
Threats to Validity
7.1
Internal Validity
The study’s internal validity faces several methodological limita-
tions that warrant careful consideration. The RSSG construction
relies on static analysis, which assumes codebases are statically ana-
lyzable with inferable types and dependencies. In environments fea-
turing dynamic typing, reflection, or extensive metaprogramming,
static analysis may miss critical semantic relationships, potentially
reducing the method’s effectiveness. This limitation particularly
affects dynamically-typed languages like Python when heavy use
of dynamic features obscures code relationships.
The RCS algorithm’s performance depends on the choice of
scoring function, and while the current implementation showed
consistent results across evaluated repositories, different scoring
approaches might yield varied effectiveness. This dependency re-
quires careful tuning when adapting to new domains or coding
styles significantly different from the evaluation datasets.
The evaluation metrics (EM, ID-F1) capture syntactic and identifier-
level correctness but may not fully reflect practical developer pro-
ductivity gains. Factors such as code maintainability, readability
improvements, and learning effects from repository-wide context
remain unmeasured. Additionally, the controlled experimental en-
vironment cannot account for real-world variables like network
latency, IDE responsiveness, and developer interruption patterns
that could influence actual usage effectiveness.
7.2
External Validity
The generalizability of these findings extends beyond the initial
evaluation scope, supported by real-world deployment evidence.
While the controlled evaluation focuses on CrossCodeEval’s Python
and Java repositories, industrial deployment across a 50M+ line
codebase with 2,000+ repositories demonstrates effectiveness across
diverse architectural patterns and development practices.
The assumption of full repository access for context construction
represents an idealized scenario. However, industrial deployment
successfully operates in environments with restricted access, par-
tial repository visibility, and microservices architectures where
complete dependency graphs are unavailable. This suggests the
approach adapts reasonably to realistic deployment constraints.
The evaluation’s focus on models up to 7B parameters reflects
practical resource constraints in many industrial environments.
While larger models might achieve higher absolute performance,
the efficiency-focused design principles remain relevant for resource-
constrained deployment scenarios that represent a significant por-
tion of real-world usage.
8
Conclusion
This paper presents RepoFuse, demonstrating that systematic con-
text categorization enables practical repository-level code comple-
tion at industrial scale. One year of production deployment serving
10,000+ developers validates the approach: 18% acceptance rate
improvement with sub-200ms latency, while benchmark evaluation
shows 4.26 and 3.01 EM gains for Python and Java using only 25%
of baseline tokens.
Key Industrial Findings: Production data revealed that dual-
context benefits concentrate in cross-microservice scenarios (24%
improvement) while providing minimal value for algorithmic code
(< 5%). Developers proved more sensitive to latency than accu-
racy—acceptance rates dropped 40% beyond 300ms regardless of
completion quality. The gap between research prototype and pro-
duction system required 3 engineer-months for infrastructure (in-
cremental graph updates, distributed caching, cold-start optimiza-
tion).
Practitioner Recommendations: Organizations should: (1) pi-
lot in high-impact scenarios (API integration, framework adoption)
before universal rollout; (2) measure acceptance rate and latency
alongside accuracy; (3) budget engineering effort for production
infrastructure beyond core algorithms; (4) adapt semantic graph
edges to organizational patterns.
577

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale
FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
References
[1] Loubna Ben Allal, Raymond Li, Denis Kocetkov, Chenghao Mou, Christopher
Akiki, Carlos Muñoz Ferrandis, Niklas Muennighoff, Mayank Mishra, Alex Gu,
Manan Dey, Logesh Kumar Umapathi, Carolyn Jane Anderson, Yangtian Zi, Joel
Lamy-Poirier, Hailey Schoelkopf, Sergey Troshin, Dmitry Abulkhanov, Manuel
Romero, Michael Lappert, Francesco De Toni, Bernardo García del Río, Qian Liu,
Shamik Bose, Urvashi Bhattacharyya, Terry Yue Zhuo, Ian Yu, Paulo Villegas,
Marco Zocca, Sourab Mangrulkar, David Lansky, Huu Nguyen, Danish Contractor,
Luis Villa, Jia Li, Dzmitry Bahdanau, Yacine Jernite, Sean Hughes, Daniel Fried,
Arjun Guha, Harm de Vries, and Leandro von Werra. 2023. SantaCoder: don’t
reach for the stars! CoRR abs/2301.03988 (2023). https://doi.org/10.48550/ARXIV.
2301.03988 arXiv:2301.03988
[2] Miltiadis Allamanis and Charles Sutton. 2013. Mining source code repositories
at massive scale using language modeling. In Proceedings of the 10th Working
Conference on Mining Software Repositories (San Francisco, CA, USA) (MSR ’13).
IEEE Press, 207–216.
[3] Ramakrishna Bairi, Atharv Sonwane, Aditya Kanade, Vageesh D C, Arun Iyer,
Suresh Parthasarathy, Sriram Rajamani, B. Ashok, and Shashank Shet. 2023.
CodePlan: Repository-level Coding using LLMs and Planning. In NeurIPS 2023
Foundation Models for Decision Making Workshop. https://openreview.net/forum?
id=d0A2pc2kFp
[4] Mohammad Bavarian, Heewoo Jun, Nikolas Tezak, John Schulman, Christine
McLeavey, Jerry Tworek, and Mark Chen. 2022. Efficient Training of Language
Models to Fill in the Middle. CoRR abs/2207.14255 (2022). https://doi.org/10.
48550/ARXIV.2207.14255 arXiv:2207.14255
[5] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de
Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg
Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf,
Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail
Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter,
Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fo-
tios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex
Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shan-
tanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh
Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles
Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei,
Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. 2021. Evaluating Large
Language Models Trained on Code. arXiv:2107.03374 [cs.LG]
[6] Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. 2023. Ex-
tending Context Window of Large Language Models via Positional Interpolation.
arXiv:2306.15595 [cs.CL]
[7] Wei Cheng, Yuhan Wu, and Wei Hu. 2024. Dataflow-Guided Retrieval Augmen-
tation for Repository-Level Code Completion. arXiv:2405.19782 [cs.SE]
[8] Fenia Christopoulou, Gerasimos Lampouras, Milan Gritta, Guchun Zhang, Yin-
peng Guo, Zhongqi Li, Qi Zhang, Meng Xiao, Bo Shen, Lin Li, Hao Yu, Li
Yan, Pingyi Zhou, Xin Wang, Yuchi Ma, Ignacio Iacobacci, Yasheng Wang,
Guangtai Liang, Jiansheng Wei, Xin Jiang, Qianxiang Wang, and Qun Liu.
2022. PanGu-Coder: Program Synthesis with Function-Level Language Model-
ing. CoRR abs/2207.11280 (2022). https://doi.org/10.48550/ARXIV.2207.11280
arXiv:2207.11280
[9] Peng Di, Jianguo Li, Hang Yu, Wei Jiang, Wenting Cai, Yang Cao, Chaoyu Chen,
Dajun Chen, Hongwei Chen, Liang Chen, Gang Fan, Jie Gong, Zi Gong, Wen Hu,
Tingting Guo, Zhichao Lei, Ting Li, Zheng Li, Ming Liang, Cong Liao, Bingchang
Liu, Jiachen Liu, Zhiwei Liu, Shaojun Lu, Min Shen, Guangpei Wang, Huan Wang,
Zhi Wang, Zhaogui Xu, Jiawei Yang, Qing Ye, Gehao Zhang, Yu Zhang, Zelin Zhao,
Xunjin Zheng, Hailian Zhou, Lifu Zhu, and Xianying Zhu. 2023. CodeFuse-13B:
A Pretrained Multi-lingual Code Large Language Model. CoRR abs/2310.06266
(2023). https://doi.org/10.48550/ARXIV.2310.06266 arXiv:2310.06266
[10] Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan,
Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia,
Dan Roth, and Bing Xiang. 2023. CrossCodeEval: A Diverse and Multilingual
Benchmark for Cross-File Code Completion. arXiv:2310.11248 [cs.LG]
[11] Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Murali Krishna Ramanathan,
Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang. 2022. CoCoMIC:
Code Completion By Jointly Modeling In-file and Cross-file Context. ArXiv
abs/2212.10007 (2022). https://api.semanticscholar.org/CorpusID:254877371
[12] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong,
Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, and Ming Zhou. 2020. CodeBERT:
A Pre-Trained Model for Programming and Natural Languages. In Findings of the
Association for Computational Linguistics: EMNLP 2020, Trevor Cohn, Yulan He,
and Yang Liu (Eds.). Association for Computational Linguistics, Online, 1536–
1547. https://doi.org/10.18653/v1/2020.findings-emnlp.139
[13] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi,
Ruiqi Zhong, Scott Yih, Luke Zettlemoyer, and Mike Lewis. 2023. InCoder: A
Generative Model for Code Infilling and Synthesis. In The Eleventh International
Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023.
OpenReview.net. https://openreview.net/pdf?id=hQwb-lbM6EL
[14] M.R. Garey and D.S. Johnson. 1979. Computers and Intractability: A Guide to the
Theory of NP-completeness. Freeman. https://books.google.com.br/books?id=
fjxGAQAAIAAJ
[15] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. 2022.
UniXcoder: Unified Cross-Modal Pre-training for Code Representation. In Pro-
ceedings of the 60th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), Smaranda Muresan, Preslav Nakov, and Aline Villavicen-
cio (Eds.). Association for Computational Linguistics, Dublin, Ireland, 7212–7225.
https://doi.org/10.18653/v1/2022.acl-long.499
[16] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guant-
ing Chen, Xiao Bi, Y. Wu, Y. K. Li, Fuli Luo, Yingfei Xiong, and Wenfeng Liang.
2024. DeepSeek-Coder: When the Large Language Model Meets Programming –
The Rise of Code Intelligence. arXiv:2401.14196 [cs.SE]
[17] Priyanshu Gupta, Avishree Khare, Yasharth Bajpai, Saikat Chakraborty, Sumit
Gulwani, Aditya Kanade, Arjun Radhakrishna, Gustavo Soares, and Ashish Tiwari.
2023. Grace: Language Models Meet Code Edits. (September 2023).
https:
//www.microsoft.com/en-us/research/publication/grace/ To appear at ESEC/FSE
’23.
[18] Nam Le Hai, Dung Manh Nguyen, and Nghi D. Q. Bui. 2025. On the Impacts of
Contexts on Repository-Level Code Generation. In Findings of the Association for
Computational Linguistics: NAACL 2025, Luis Chiruzzo, Alan Ritter, and Lu Wang
(Eds.). Association for Computational Linguistics, Albuquerque, New Mexico,
1496–1524. https://doi.org/10.18653/v1/2025.findings-naacl.82
[19] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2021. LoRA: Low-Rank Adaptation of Large
Language Models. arXiv:2106.09685 [cs.CL]
[20] Rafael-Michael Karampatsis, Hlib Babii, Romain Robbes, Charles Sutton, and
Andrea Janes. 2020. Big code != big vocabulary: open-vocabulary models for
source code. In Proceedings of the ACM/IEEE 42nd International Conference on
Software Engineering (Seoul, South Korea) (ICSE ’20). Association for Computing
Machinery, New York, NY, USA, 1073–1085.
https://doi.org/10.1145/3377811.
3380342
[21] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov,
Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, Qian Liu,
Evgenii Zheltonozhskii, Terry Yue Zhuo, Thomas Wang, Olivier Dehaene, Mishig
Davaadorj, Joel Lamy-Poirier, João Monteiro, Oleh Shliazhko, Nicolas Gontier,
Nicholas Meade, Armel Zebaze, Ming-Ho Yee, Logesh Kumar Umapathi, Jian Zhu,
Benjamin Lipkin, Muhtasham Oblokulov, Zhiruo Wang, Rudra Murthy, Jason
Stillerman, Siva Sankalp Patel, Dmitry Abulkhanov, Marco Zocca, Manan Dey,
Zhihan Zhang, Nour Fahmy, Urvashi Bhattacharyya, Wenhao Yu, Swayam Singh,
Sasha Luccioni, Paulo Villegas, Maxim Kunakov, Fedor Zhdanov, Manuel Romero,
Tony Lee, Nadav Timor, Jennifer Ding, Claire Schlesinger, Hailey Schoelkopf, Jan
Ebert, Tri Dao, Mayank Mishra, Alex Gu, Jennifer Robinson, Carolyn Jane Ander-
son, Brendan Dolan-Gavitt, Danish Contractor, Siva Reddy, Daniel Fried, Dzmitry
Bahdanau, Yacine Jernite, Carlos Muñoz Ferrandis, Sean Hughes, Thomas Wolf,
Arjun Guha, and Leandro von Werra. 2023. StarCoder: may the source be with
you! arXiv:2305.06161 [cs.CL]
[22] Yichen Li, Yun Peng, Yintong Huo, and Michael R. Lyu. 2024. Enhancing LLM-
Based Coding Tools through Native Integration of IDE-Derived Static Context.
arXiv:2402.03630 [cs.SE]
[23] Tianyang Liu, Canwen Xu, and Julian McAuley. 2023. RepoBench: Benchmarking
Repository-Level Code Auto-Completion Systems. arXiv:2306.03091 [cs.CL]
[24] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi
Jin, and Qianxiang Wang. 2024.
GraphCoder: Enhancing Repository-Level
Code Completion via Code Context Graph-based Retrieval and Language Model.
arXiv:2406.07003 [cs.SE] https://arxiv.org/abs/2406.07003
[25] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin,
and Qianxiang Wang. 2024. GraphCoder: Enhancing Repository-Level Code
Completion via Code Context Graph-based Retrieval and Language Model. arXiv
preprint arXiv:2406.07003 (2024).
[26] Shuai Lu, Nan Duan, Hojae Han, Daya Guo, Seung-won Hwang, and Alexey Svy-
atkovskiy. 2022. ReACC: A Retrieval-Augmented Code Completion Framework.
In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Smaranda Muresan, Preslav Nakov, and Aline
Villavicencio (Eds.). Association for Computational Linguistics, Dublin, Ireland,
6227–6240. https://doi.org/10.18653/v1/2022.acl-long.431
[27] Amirkeivan Mohtashami and Martin Jaggi. 2023. Landmark Attention: Random-
Access Infinite Context Length for Transformers. arXiv:2305.16300 [cs.CL]
[28] Erik Nijkamp, Hiroaki Hayashi, Caiming Xiong, Silvio Savarese, and Yingbo
Zhou. 2023. CodeGen2: Lessons for Training LLMs on Programming and Natural
Languages. ICLR (2023).
[29] Hengzhi Pei, Jinman Zhao, Leonard Lausen, Sheng Zha, and George Karypis. 2023.
Better Context Makes Better Code Language Models: A Case Study on Function
Call Argument Completion. In Thirty-Seventh AAAI Conference on Artificial
Intelligence, AAAI 2023, Thirty-Fifth Conference on Innovative Applications of
Artificial Intelligence, IAAI 2023, Thirteenth Symposium on Educational Advances
in Artificial Intelligence, EAAI 2023, Washington, DC, USA, February 7-14, 2023,
Brian Williams, Yiling Chen, and Jennifer Neville (Eds.). AAAI Press, 5230–5238.
https://doi.org/10.1609/AAAI.V37I4.25653
578

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

FSE Companion ’26, July 05–09, 2026, Montreal, QC, Canada
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, and Peng Di
[30] Huy N Phan, Hoang N Phan, Tien N Nguyen, and Nghi DQ Bui. 2024. RepoHyper:
Better Context Retrieval Is All You Need for Repository-Level Code Completion.
arXiv preprint arXiv:2403.06095 (2024).
[31] Google Research. Year. ML-enhanced code completion improves developer produc-
tivity. https://research.google/blog/ml-enhanced-code-completion-improves-
developer-productivity/ Accessed: Date.
[32] Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xi-
aoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, Artyom
Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian Canton Fer-
rer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal
Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and
Gabriel Synnaeve. 2023.
Code Llama: Open Foundation Models for Code.
arXiv:2308.12950 [cs.CL]
[33] Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, and
Torsten Scholak. 2023. RepoFusion: Training Code Models to Understand Your
Repository. arXiv:2306.10998 [cs.LG]
[34] Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2023. Repository-Level
Prompt Generation for Large Language Models of Code. In Proceedings of the 40th
International Conference on Machine Learning (Honolulu, Hawaii, USA) (ICML’23).
JMLR.org, Article 1314, 23 pages.
[35] Gemini Team. 2025. Gemini: A Family of Highly Capable Multimodal Models.
arXiv:2312.11805 [cs.CL] https://arxiv.org/abs/2312.11805
[36] Szymon Tworkowski, Konrad Staniszewski, Mikołaj Pacek, Yuhuai Wu, Henryk
Michalewski, and Piotr Miłoś. 2023. Focused Transformer: Contrastive Training
for Context Scaling. arXiv:2307.03170 [cs.CL]
[37] Chaozheng Wang, Junhao Hu, Cuiyun Gao, Yu Jin, Tao Xie, Hailiang Huang,
Zhenyu Lei, and Yuetang Deng. 2023. How Practitioners Expect Code Com-
pletion?. In Proceedings of the 31st ACM Joint European Software Engineering
Conference and Symposium on the Foundations of Software Engineering (, San
Francisco, CA, USA,) (ESEC/FSE 2023). Association for Computing Machinery,
New York, NY, USA, 1294–1306. https://doi.org/10.1145/3611643.3616280
[38] Chaozheng Wang, Junhao Hu, Cuiyun Gao, Yu Jin, Tao Xie, Hailiang Huang,
Zhenyu Lei, and Yuetang Deng. 2023.
Practitioners’ Expectations on Code
Completion. CoRR abs/2301.03846 (2023). https://doi.org/10.48550/ARXIV.2301.
03846 arXiv:2301.03846
[39] Yanlin Wang, Yanli Wang, Daya Guo, Jiachi Chen, Ruikai Zhang, Yuchi Ma, and
Zibin Zheng. 2025. RLCoder: Reinforcement Learning for Repository-Level Code
Completion. IEEE Press, 1140–1152.
https://doi.org/10.1109/ICSE55347.2025.
00014
[40] Di Wu, Wasi Uddin Ahmad, Dejiao Zhang, Murali Krishna Ramanathan, and
Xiaofei Ma. 2024. Repoformer: Selective Retrieval for Repository-Level Code
Completion. arXiv:2403.10059 [cs.SE]
[41] Xiaoheng Xie, Gang Fan, Xiaojun Lin, Ang Zhou, Shijie Li, Xunjin Zheng, Yinan
Liang, Yu Zhang, Na Yu, Haokun Li, Xinyu Chen, Yingzhuang Chen, Yi Zhen,
Dejun Dong, Xianjin Fu, Jinzhou Su, Fuxiong Pan, Pengshuai Luo, Youzheng Feng,
Ruoxiang Hu, Jing Fan, Jinguo Zhou, Xiao Xiao, and Peng Di. 2024. CodeFuse-
Query: A Data-Centric Static Code Analysis System for Large-Scale Organiza-
tions. arXiv:2401.01571 [cs.SE] https://arxiv.org/abs/2401.01571
[42] Fabian Yamaguchi, Nico Golde, Daniel Arp, and Konrad Rieck. 2014. Modeling and
Discovering Vulnerabilities with Code Property Graphs. In 2014 IEEE Symposium
on Security and Privacy. 590–604. https://doi.org/10.1109/SP.2014.44
[43] Morteza Zakeri-Nasrabadi, Saeed Parsa, Mohammad Ramezani, Chanchal Roy,
and Masoud Ekhtiarzadeh. 2023. A systematic literature review on source code
similarity measurement and clone detection: techniques, applications, and chal-
lenges. arXiv:2306.16171 [cs.SE]
[44] Daoguang Zan, Bei Chen, Yongshun Gong, Junzhi Cao, Fengji Zhang, Bingchao
Wu, Bei Guan, Yilong Yin, and Yongji Wang. 2025. Private-library-oriented code
generation with large language models. Knowledge-Based Systems 326 (2025),
113934. https://doi.org/10.1016/j.knosys.2025.113934
[45] Dejiao Zhang*, Wasi Ahmad*, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan
Roth, Xiaofei Ma, and Bing Xiang. 2024. CodeSage: Code Representation Learning
At Scale. In The Twelfth International Conference on Learning Representations.
https://openreview.net/forum?id=vfzRRjumpX
[46] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao,
Jian-Guang Lou, and Weizhu Chen. 2023. RepoCoder: Repository-Level Code
Completion Through Iterative Retrieval and Generation. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing, Houda Bouamor,
Juan Pino, and Kalika Bali (Eds.). Association for Computational Linguistics,
Singapore, 2471–2484. https://doi.org/10.18653/v1/2023.emnlp-main.151
[47] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024. CodeAgent: Enhancing
Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level
Coding Challenges. arXiv:2401.07339 [cs.SE]
[48] Lei Zhang, Yunshui Li, Jiaming Li, Xiaobo Xia, Jiaxi Yang, Run Luo, Minzheng
Wang, Longze Chen, Junhao Liu, and Min Yang. 2024. Hierarchical Context Prun-
ing: Optimizing Real-World Code Completion with Repository-Level Pretrained
Code LLMs. arXiv:2406.18294 [cs.CL] https://arxiv.org/abs/2406.18294
[49] Qinkai Zheng, Xiao Xia, Xu Zou, Yuxiao Dong, Shan Wang, Yufei Xue, Zihan
Wang, Lei Shen, Andi Wang, Yang Li, Teng Su, Zhilin Yang, and Jie Tang. 2023.
CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Evalua-
tions on HumanEval-X. CoRR abs/2303.17568 (2023). https://doi.org/10.48550/
ARXIV.2303.17568 arXiv:2303.17568
579

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse/page-12.png)
