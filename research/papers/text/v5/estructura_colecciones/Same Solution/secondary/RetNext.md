# RetNext: Code Retrieval for Repository-Level Next Edit Suggestion

- source_pdf: ../../../../../pdf/Same%20Solution/secondary/RetNext.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RetNext: Code Retrieval for Repository-Level Next Edit
Suggestion
Zhaoyuan Pan∗
School of Computer Science and
Technology
University of Science and Technology
of China
Hefei, Anhui, China
State Key Laboratory of Cognitive
Intelligence
Hefei, Anhui, China
zhaoyuanpan@mail.ustc.edu.cn
Zheng Zhang
School of Computer Science and
Technology
University of Science and Technology
of China
Hefei, Anhui, China
State Key Laboratory of Cognitive
Intelligence
Hefei, Anhui, China
zhangzheng@mail.ustc.edu.cn
Cheng Cheng
School of Computer Science and
Technology
University of Science and Technology
of China
Hefei, Anhui, China
State Key Laboratory of Cognitive
Intelligence
Hefei, Anhui, China
doublecheng@mail.ustc.edu.cn
Abstract
Modern software development increasingly relies on intelligent
coding assistants, where Next Edit Suggestion (NES) aims to predict
and automate a developer’s subsequent actions by analyzing their
current edits. However, real-world software development often
involves complex, repository-level operations. The core problem
of extending the scope of NES from single-file to the repository
level hinges on how to efficiently and accurately retrieve the next
most likely code location to be edited based on the current context.
While NES has been widely adopted in tools such as Cursor, existing
methods and benchmarks are generally limited to single-file edit
patterns, failing to capture cross-file dependencies and the need
for low-cost deployment during frequent model updates. To bridge
these gaps, the objective of this paper is to explore and resolve
the repository-level Next Edit Localization (NEL) task. We first
construct RetNextBench, a novel benchmark dataset dedicated to
cross-file editing, comprising 583 high-quality evaluation instances
and approximately 26k training pairs extracted from 18 popular
GitHub repositories. Based on this dataset, we propose RetNext,
a novel retrieval-based framework. The novelty of the proposed
technique lies in leveraging task-specific LoRA adapters, which
efficiently map current edits to the next edit locations while strictly
maintaining a shared, static codebase index, thus enabling low-
cost model and codebase reuse. Extensive experimental results and
analyses demonstrate that RetNext significantly improves retrieval
performance in complex cross-file scenarios, achieving a 16.2%
improvement in MRR and a 10.3% improvement in Recall@10 on
RetNextBench. Furthermore, analyses on the general-purpose CoIR
benchmark validate the robustness and generalization ability of
the framework, proving its effectiveness as a practical solution for
repository-level next edit suggestion without sacrificing general
code retrieval capabilities.
∗Corresponding author.
This work is licensed under a Creative Commons Attribution 4.0 International License.
DSDE 2026, Chengdu, China
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2106-9/26/06
https://doi.org/10.1145/3830340.3830348
CCS Concepts
• Software and its engineering →Software maintenance tools;
• Information systems →Query representation; • Computing
methodologies →Natural language processing.
Keywords
Code Editing, Code Retrieval, Code Generation
ACM Reference Format:
Zhaoyuan Pan, Zheng Zhang, and Cheng Cheng. 2026. RetNext: Code Re-
trieval for Repository-Level Next Edit Suggestion. In 2026 The 9th Inter-
national Conference on Data Storage and Data Engineering (DSDE 2026),
June 12–14, 2026, Chengdu, China. ACM, New York, NY, USA, 5 pages.
https://doi.org/10.1145/3830340.3830348
1
Introduction
Next Edit Suggestion (NES) aims to predict and automate a devel-
oper’s next action by analyzing their current edit. With the rapid
advancement of code Large Language Models (LLMs) [4, 9, 14],
NES has been widely adopted in tools such as Cursor [1], GitHub
Copilot [3], and Zeta [19]. However, current suggestions are gener-
ally confined to a single file, which limits their ability to support
the cross-file requirements of real-world software development.
For example, as shown in Figure 1, after a developer modifies the
core code in oauth2.py, the corresponding schema in the test file
test_tutorial003.py must also be updated, illustrating a typical
cross-file editing scenario.
An intuitive approach is to feed the entire code repository as
context into LLMs. However, this is not only expensive and inef-
ficient, but can also exceed the model’s context limit. To address
this issue, we design a repository-level next edit suggestion work-
flow, which consists of a retrieval stage followed by a generation
stage (see Figure 1). Specifically, we first use the developer’s cur-
rent actions as a query to the retriever, which identifies the next
most likely code chunk to be edited. This retrieved chunk is then
provided as context to the generator to produce editing suggestions.
Since the quality of the retrieved code chunk directly affects the
quality of the suggestion, we focus on the retrieval stage and desig-
nate this task as repository-level next edit localization (NEL). More
specifically, we study how to localize the next most likely code
region to be edited, given the developer’s current edit, because the
51

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

DSDE 2026, June 12–14, 2026, Chengdu, China
Pan et al.
-
+
fastapi/security/oauth2.py
        ],
        password: Annotated[
            str,
            Form(),
            Form(json_schema_extra={"format": "password"}),
            Doc(
                """
                `password` string. The OAuth2 spec requires the exact 
field name
+
+
+
+
-
+
tests/test_tutorial/test_security/test_tutorial003.py
                            }
                        ),
                        "username": {"title": "Username", "type": "string"},
                        "password": {"title": "Password", "type": "string"},
                        "password": {
                            "title": "Password",
                            "type": "string",
                            "format": "password",
                        },
                        "scope": {"title": "Scope", "type": "string", "default": 
""},
                        "client_id": IsDict(
                            {
tests/test_tutorial/test_security/test_tutorial003.py
                            }
                        ),
                        "username": {"title": "Username", "type": "string"},
                        "password": {"title": "Password", "type": "string"},
                        "scope": {"title": "Scope", "type": "string", 
"default": ""},
                        "client_id": IsDict(
                            {
...
Query
Code 
Chunk
Editing
...
Retriever
Generator
Figure 1: The workflow of repository-level next edit sugges-
tion. This research focuses on the retrieval part (marked in
green).
quality of the generated suggestion strongly depends on whether
the retrieved repository context is relevant and precise. Formally,
repository-level Next Edit Localization (NEL) can be viewed as a
retrieval problem. Given the developer’s current edit represented as
a query diff and a repository represented as a set of candidate code
chunks, the goal is to identify the chunk or chunks in which the
developer’s subsequent edit is most likely to occur. The retrieval
model is therefore expected to rank the true next-edit locations as
highly as possible among all repository candidates.
A primary challenge for NEL is how to construct effective train-
ing data and evaluation methods. NEL needs to capture complex
cross-file dependencies and development workflow patterns. How-
ever, existing code editing benchmarks, such as [2, 11, 16], pri-
marily focus on the single-file level and lack systematic collection
and annotation of cross-file editing patterns. Consequently, they
cannot adequately support the effective training and evaluation of
repository-level NEL. To address this issue, we use GitHub reposi-
tories as our data source, as they are open-source and exhibit real-
world cross-file development patterns. Based on GitHub, we design
a three-stage data construction pipeline and build RetNextBench.
It comprises 583 instances of current edit–next edit location pairs,
extracted from 18 popular code repositories across 4 programming
languages. In addition to the benchmark, this process also pro-
duced a training set of approximately 26k pairs to facilitate model
development.
With the constructed training data, we can fine-tune a dedi-
cated retrieval model specifically for the next edit suggestion task.
However, in real-world development, NES-related models are often
updated frequently, as developers’ adoption or rejection behaviors
provide clear signals. The data generated from these interactions
can be used to further optimize the models, thereby improving
the quality of the suggestions. This frequent update cycle makes
the associated indexing, storage, and deployment costs a primary
concern. In real-world scenarios, a codebase index is often already
created by other code retrieval tasks (such as Text2Code [6, 8, 10],
Code2Code [17], Code Question Answering [18], etc.). We expect
the NEL retriever to reuse this shared codebase index, and its own
updates must not cause any changes to it. Additionally, to ensure
effective load balancing, the number of deployed models must be
minimized.
To address these challenges, we propose RetNext, a framework
for training retrievers for NEL that meets real-world deployment
requirements. Our framework focuses on the localization task of
mapping a current edit to the next edit location. It also utilizes task-
specific LoRA (Low-rank Adaptation) [7] adapters to ensure the
effective reuse of models and codebases across diverse code retrieval
tasks. Evaluation results on RetNextBench demonstrate that our
proposed method can effectively enhance the code retriever’s abil-
ity to retrieve the next edit location, with improvements of 16.2%
in Mean Reciprocal Rank (MRR) and 10.3% in Recall@10. More-
over, the results on the general code retrieval benchmark CoIR [12]
further highlight the effectiveness of our framework, validating
the robustness and generalization ability of our framework across
diverse code retrieval tasks.
2
RetNextBench
In this section, we first present the formal definition of NEL, fol-
lowed by the construction process of RetNextBench.
NEL Problem Definition. Given a code repository 𝑅repre-
sented as a collection of code chunks {𝑐1,𝑐2, . . . ,𝑐𝑁}, and a query
diff 𝑞representing the user’s current edit, the goal is to retrieve one
or more target code chunks, which form a set of positive targets
𝐶𝑡⊆𝑅, where the next edits are most likely to occur. A retrieval
model is trained to rank the chunks belonging to 𝐶𝑡as high as
possible among all candidate chunks in the repository.
The first step toward advancing repository-level NEL is the con-
struction of a suitable benchmark. However, existing code editing
datasets primarily focus on intent understanding or single-file code
generation. They lack a systematic characterization of cross-file
editing dependencies, making them insufficient for evaluating the
retrieval-based task of navigating from a current edit to the next
edit location.
To address this gap, we introduce RetNextBench, a new evalua-
tion benchmark specifically designed to measure a model’s accuracy
in localizing the next most likely code location to be edited within
a repository, given the current edit content (diff). RetNextBench
is derived from real-world development activities in high-quality
open-source projects, covering four programming languages and 18
representative repositories. This process, as illustrated in Figure 3,
includes three main stages: (1) Dependency Graph Generation;
(2) Data Construction; (3) Quality Filtering. Statistics are shown
in Figure 2.
Stage I: Dependency Graph Generation. We begin by analyz-
ing commits from code repositories, filtering for those with 2-10
diffs to focus on meaningful cross-file edits. For each commit, an
LLM generates a dependency graph linking related diffs.
Stage II: Data construction. Each cross-file edge (indicated in
red in Figure 3) in this graph is converted into a query-positive pair:
the source diff becomes the query, and the pre-edit code chunk at
52

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

RetNext: Code Retrieval for Repository-Level Next Edit Suggestion
DSDE 2026, June 12–14, 2026, Chengdu, China
nlohmann/json
40
fmtlib/fmt
34
yhirose/cpp-httplib
33
catchorg/Catch2
31
simdjson/simdjson
26
google/guava
40
alibaba/fastjson2
35
mockito/mockito
32
elastic/logstash
29
django/django
37
psf/requests
35
fastapi/fastapi
32
pallets/flask
31
sharkdp/fd
35
nushell/nushell
33
tokio-rs/tracing
29
rayon-rs/rayon
26
clap-rs/clap
25
C++
Java
Python
Rust
0
500
1000
1500
Token Count
0
25
50
75
100
125
150
Frequency
0
100
200
Number of Modified Lines
0
100
200
300
Frequency
Figure 2: Left: Distribution of instances across different repos-
itories and languages. Right: Distribution of the number of
query tokens and the number of modified lines.
1
2
6
3
4
5
1
2
2
3
3
4
6
2
Query
Positive
LLM Filtering
Human Annotation
Dependency Graph
https://github.com/django/django
123abc
django/db/models/sql/where.py
django/db/models/sql/where.py
django/tests/xor_lookups/tests.py
releases/5.0.txt
@@ -129,12 +130,16 @@
@@ -6,6 +6,7 @@
@@ -19,6 +19,27 @@
@@ -424,6 +424,11 @@
1
2
6
3
4
5
django/tests/xor_lookups/tests.py
@@ -50,7 +50,8 @@
releases/5.0.txt
@@ -440,5 +440,9 @@
1
2
3a
3b
Figure 3: Data construction pipeline for the RetNextBench.
• Synchronization of Implementation and Tests: edits that update test code to reflect changes in the 
corresponding implementation.
• Synchronization of Interface and Implementation: modifications that ensure the implementation of a 
function or class aligns with its declared interface.
• Synchronization of Configuration and Feature Updates: changes in configuration files or scripts that 
correspond to a new or updated feature.
• Code Refactoring: edits that improve the internal structure of the code without changing its external 
behavior, such as function extraction and migration.
• Synchronization of Data Model and View/Interface: updates to the user interface or API endpoints to 
match changes in the underlying data schema or model.
• Synchronization of Documentation and Code: revisions to comments, README files, or other 
documentation to keep them consistent with code changes.
• Adaptation for Dependency Library Updates: modifications to the codebase to ensure compatibility 
with a newly updated or changed dependency.
• Synchronous Clone Modification: applying consistent changes to sections of code that were copied 
or duplicated.
Figure 4: Human annotation criteria.
the destination serves as the ground truth. An instance may contain
multiple ground truths.
Stage III: Quality Filtering. The automatically generated pairs
undergo an initial screening by Qwen3-235B-A22B. The model
assesses the logical relevance of the edit represented by each pair.
For each repository, we extract 50 instances as the test set for
subsequent human annotation, and the remaining 26k data serve
as the training set. Pairs that pass the LLM screening are submitted
to three experienced software engineers for final review. Figure 4
shows the acceptance criteria for the quality filtering process.
For each instance, the majority opinion (accept or reject) is ap-
plied. Then, three other annotators are asked to repeat this process
to ensure the consistency of the annotations. Only the instances
that are accepted in both rounds of annotation are retained, and
the annotation consistency between the two rounds is 95.6%.
Attention
Weights
Attention
Weights
Hidden State
Hidden State
Hidden State
Hidden State
N x Transformer Block
Query Encoder
Chunk Encoder
Query
Embedding
Chunk
Embedding
Pooling
& Normalization
Pooling
& Normalization
Shared
Cosine
Similarity
Contrastive
Loss
Figure 5: RetNext Framework Overview.
Table 1: Comparison of training strategies. 𝑛represents the
number of tasks.
Method
Shared Index
# Models
Mixed–data training
✗
1
w/ frozen chunk enc.
✓
2
Task-wise training
✗
𝑛
Task-specific LoRA
✓
1 Backbone + 𝑛Adapter (≈1)
3
Method
In this section, we present our proposed RetNext framework for the
task of NEL. Constrained by the continuous training and deploy-
ment requirements of real-world code retrieval applications, we
aim to keep the code chunk index static across model iterations and
to deploy as few models as possible. Inspired by Jina-embedding-
v3 [15], and as illustrated in Figure 5, we use task-specific LoRA
adapters to train the query encoder separately for different tasks,
while the chunk encoder is always kept frozen. This approach en-
sures that different tasks can share the code chunk index, while
only requiring the deployment of a single backbone model along
with multiple adapters. Table 1 shows a comparison of the different
training strategies.
3.1
Task-specific LoRA Adapter
To strike a balance between computational efficiency and task speci-
ficity, we introduce task-specific LoRA to the Query Encoder (𝐸𝑞).
The core concept of LoRA involves freezing the original weights
𝑊0 of the pre-trained model and injecting a trainable, low-rank de-
composed matrix Δ𝑊= 𝐵𝐴, where 𝐵∈R𝑑×𝑟and 𝐴∈R𝑟×𝑘, with
the rank 𝑟≪min(𝑑,𝑘). Consequently, the forward propagation
process is updated to ℎ= 𝑊0𝑥+ 𝐵𝐴𝑥.
In RetNext, each task T is associated with an independent LoRA
adapter (𝐴T, 𝐵T), and only its parameters are updated during train-
ing. This strategy enables the model to perform specific optimiza-
tions on different tasks, while the base weights of the Query Encoder
and the entire Chunk Encoder (𝐸𝑐) are shared and remain frozen.
As a result, all tasks can share a unified set of code chunk vector in-
dices, which significantly reduces both storage and computational
overhead.
53

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

DSDE 2026, June 12–14, 2026, Chengdu, China
Pan et al.
Table 2: Main Results on RetNextBench.
Model
Python
Java
C++
Rust
Avg.
MRR
R@10
MRR
R@10
MRR
R@10
MRR
R@10
MRR
R@10
SFR-embedding-code-400m_r
15.50
35.56
14.04
33.09
13.59
31.10
18.47
42.45
15.38
35.48
Jina-embedding-v2-base-code
19.14
47.41
19.65
45.59
19.46
40.75
22.11
47.86
20.10
45.23
Codesage-small-v2
18.07
38.15
17.23
37.50
17.03
38.72
17.68
38.06
17.48
38.14
Qwen3-embedding-0.6b
24.16
54.44
20.82
48.16
20.06
46.75
21.82
48.70
21.63
49.36
RetNext-SFR
20.60
44.81
16.57
34.07
17.18
34.25
22.22
44.37
19.11
39.22
RetNext-Jina
21.96
48.89
20.26
45.59
20.10
47.15
25.09
51.41
21.84
48.27
RetNext-Codesage
21.92
41.11
19.86
43.01
23.97
45.02
19.04
42.06
21.28
42.90
RetNext-Qwen
26.64
59.63
24.00
49.26
22.62
50.51
27.56
58.73
25.13
54.42
-+
 requests/models.py
else:
                url = '%s?%s' % (url, 
self._enc_params)
        if self.config.get('encode_urls'):
        if self.config.get('encode_uri'):
            url = requote_uri(url)
        return url
c1a44259d
-
+
 requests/defaults.py
defaults['max_retries'] = 0
defaults['safe_mode'] = False
defaults['keep_alive'] = True
defaults['encode_urls'] = True
defaults['encode_uri'] = True
psf/requests
 requests/models.py
else:
                url = '%s?%s' % (url, 
self._enc_params)
        if self.config.get('encode_urls'):
            url = requote_uri(url)
        return url
Rank: 10 (Qwen) Rank: 1 (RetNext-Qwen)
(Qwen2.5-Coder-7B)
Query
Ideal Code Chunk
Ideal Editing Code 
Retriever
Generator
Figure 6: A case study from psf/requests.
3.2
Training Objective
We employ the InfoNCE loss for contrastive learning. In a given
training batch of size 𝑁, let {(𝑞𝑖, 𝑝+
𝑖)}𝑁
𝑖=1 be the set of training
pairs, where 𝑞𝑖is the i-th query (the current edit diff) and 𝑝+
𝑖is its
corresponding positive sample (the ground-truth next edit location).
The query is encoded into a vector 𝑢𝑖= 𝐸𝑞(𝑞𝑖), and the positive
sample into 𝑣+
𝑖= 𝐸𝑐(𝑝+
𝑖). For the query 𝑢𝑖, its positive sample is 𝑣+
𝑖,
and all other positive samples {𝑣+
𝑗}𝑗≠𝑖within the same batch serve
as negative samples. The overall loss L for the batch is the average
of the individual sample losses, defined as:
L = −1
𝑁
𝑁
∑︁
𝑖=1
log
exp(𝑠(𝑢𝑖, 𝑣+
𝑖))
Í𝑁
𝑗=1 exp(𝑠(𝑢𝑖, 𝑣+
𝑗))
Here,𝑠(𝑢, 𝑣) = sim(𝑢, 𝑣)/𝜏represents the cosine similarity scaled
by a temperature hyperparameter 𝜏.
4
Experiments
In this section, we evaluate the performance of four SOTA code
retrievers (SFR-embedding-code-400m_r [13], Jina-embedding-v2-
base-code [5], Codesage-small-v2 [20] and Qwen3-embedding-0.6b [21]),
alongside their counterparts fine-tuned with the RetNext frame-
work, on the RetNextBench. We report the Mean Reciprocal Rank
(MRR) and Recall@10 (R@10) for each programming language,
as well as the average metrics. Next, we present a case study to
demonstrate the framework’s applicability to repository-level NES.
Finally, we fine-tune these models with different Task LoRA, and
report the Normalized Discounted Cumulative Gain (NDCG@10)
on several subsets of the CoIR benchmark, including Apps [6],
CosQA [8], CodeTrans-Contest [17], StackOverflow-QA [12], and
CodeFeedBack-MT [22].
4.1
Performance on RetNextBench
As shown in Table 2, the experimental results clearly demonstrate
that the RetNext framework significantly enhances the performance
of all base models on the task of NEL. Specifically, all fine-tuned
models outperform their original versions on both MRR and R@10
metrics across all four programming languages (Python, Java, C++,
and Rust).
Among all models evaluated, RetNext-Qwen achieved the best
performance, establishing a new state-of-the-art result on Ret-
NextBench. This model not only secured the top spot in average
MRR (25.13) and R@10 (54.42) but also obtained the highest scores
in nearly every individual language test, as indicated by the bold
numbers in the table. Furthermore, we observed a difference in
retrieval difficulty among languages; most models generally per-
formed worse on C++ than on the others, which may reflect the
more complex editing dependencies in C++ codebases. Overall,
these results provide strong validation for the effectiveness of our
proposed training framework in enhancing a code retriever’s ability
to locate cross-file editing contexts.
4.2
Case Study
In this section, we demonstrate how RetNext supports LLMs in
generating repository-level Next Edit Suggestions. Due to the lim-
itations of the context window size and generation latency, we
restrict the generator (Qwen2.5-Coder-7B) to receive the Top-5
code chunks as context for generating the next suggestion. Fig-
ure 6 illustrates a case from the psf/requests, where a devel-
oper renamed the configuration key encode_urls to encode_uri.
This action in defaults.py requires a corresponding update in
models.py, where the key is used. This example represents a typ-
ical repository-level editing scenario in which a seemingly local
modification introduces a non-local dependency that cannot be
reliably handled by single-file completion alone. While the Qwen3-
embedding-0.6b ranked the correct location at 10, our fine-tuned
RetNext-Qwen successfully identified this cross-file dependency
and promoted it to rank 1. This improvement is critical, because
the correct location would be excluded from the generator input
when using the original embedding model under the Top-5 context
constraint. This case highlights our framework’s superior ability to
understand code semantics for accurate, repository-level NEL. At
54

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

RetNext: Code Retrieval for Repository-Level Next Edit Suggestion
DSDE 2026, June 12–14, 2026, Chengdu, China
Table 3: Results on CoIR benchmark.
Model
Apps
CosQA
CT-C
SO-QA
CF-MT
SFR
49.61
33.88
78.09
89.98
52.33
Jina
14.41
29.64
77.69
88.19
51.67
Codesage
31.91
15.91
78.19
70.41
51.83
Qwen
73.70
38.67
84.95
88.29
88.15
RetNext-SFR
50.57
35.83
79.65
90.16
84.11
RetNext-Jina
23.49
41.34
78.48
88.96
71.13
RetNext-Codesage
37.35
38.89
78.26
79.37
68.33
RetNext-Qwen
77.92
40.23
86.18
90.04
92.38
the same time, it also demonstrates how RetNext plays a crucial role
in enabling the generator to produce high-quality final suggestions.
4.3
Performance on CoIR
To validate the generalizability of our framework, we also conducted
evaluations on the general-purpose code retrieval benchmark, CoIR.
As shown in Table 3, all fine-tuned models outperformed their base
versions on multiple subtasks. This result fully demonstrates the
effectiveness of our adopted task-specific LoRA adapter strategy: it
enables the model to efficiently adapt to new tasks while keeping the
code chunk index unchanged. This mitigates the problem in prac-
tical deployments where the entire codebase must be re-encoded
with each model update, showcasing its significant practical value.
5
Conclusion and Future Work
In this paper, to extend next edit suggestion to the repository level,
we introduce the repository-level Next Edit Localization (NEL) task,
which aims to identify the code chunk most likely to be modified by
the developer. We first construct RetNextBench, a new benchmark
derived from open-source GitHub repositories. Then, we propose
RetNext, a framework that enables the model to specialize in pre-
dicting the next edit location while maintaining a shared, static
code chunk index for general-purpose retrieval. Experimental re-
sults demonstrate that our framework significantly improves the
performance of state-of-the-art models on RetNextBench.
Several directions remain for future research. First, although this
work focuses on repository-level next edit localization, the synthesis
of high-quality training data and the evaluation of generation-
side models for repository-level next edit suggestion remain open
problems. Second, beyond the retrieval stage, it is important to
investigate reranking mechanisms over recalled candidates so as
to provide more informative and effective context for downstream
generation models. Third, online adaptation based on developer
acceptance or rejection feedback may further improve retrieval
quality in practical usage. Finally, more realistic evaluation settings,
including real-world IDE environments and dynamically evolving
repositories, are needed to better assess the effectiveness of the
framework in real development scenarios.
Acknowledgments
This research was supported by grants from the Fundamental Re-
search Funds for the Central Universities (No.WK2150110038).
References
[1] Anysphere. 2026. Cursor: The best way to code with AI. https://cursor.com.
Accessed: 2026-05-01.
[2] Federico Cassano, Luisa Li, Akul Sethi, Noah Shinn, Abby Brennan-Jones, Jacob
Ginesin, Edward Berman, George Chakhnashvili, Anton Lozhkov, Carolyn Jane
Anderson, et al. 2023. Can it edit? evaluating the ability of large language models
to follow code editing instructions. arXiv preprint arXiv:2312.12450 (2023).
[3] GitHub. 2026. GitHub Copilot: Your AI Pair Programmer. https://github.com/
features/copilot. Accessed: 2026-05-01.
[4] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang,
Guanting Chen, Xiao Bi, Yu Wu, Yukun Li, Fuli Luo, Yingfei Xiong, and Wen-
feng Liang. 2024. DeepSeek-Coder: When the Large Language Model Meets
Programming – The Rise of Code Intelligence. arXiv:2401.14196 [cs.CL] https:
//arxiv.org/abs/2401.14196
[5] Michael Günther, Jackmin Ong, Isabelle Mohr, Alaeddine Abdessalem, Tanguy
Abel, Mohammad Kalim Akram, Susana Guzman, Georgios Mastrapas, Saba
Sturua, Bo Wang, Maximilian Werk, Nan Wang, and Han Xiao. 2024. Jina Em-
beddings 2: 8192-Token General-Purpose Text Embeddings for Long Documents.
arXiv:2310.19923 [cs] doi:10.48550/arXiv.2310.19923
[6] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora,
Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, and Jacob
Steinhardt. 2021. Measuring Coding Challenge Competence With APPS. NeurIPS
(2021).
[7] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, Weizhu Chen, et al. 2022. Lora: Low-rank adaptation of large
language models. ICLR 1, 2 (2022), 3.
[8] Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming
Zhou, and Nan Duan. 2020. CoSQA: 20, 000+ Web Queries for Code Search and
Question Answering. In ACL/IJCNLP.
[9] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu
Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. 2024. Qwen2. 5-coder technical
report. arXiv preprint arXiv:2409.12186 (2024).
[10] Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc
Brockschmidt. 2019. CodeSearchNet challenge: Evaluating the state of semantic
code search. arXiv preprint arXiv:1909.09436 (2019).
[11] Hao Jiang, Qi Liu, Rui Li, Shengyu Ye, and Shijin Wang. 2024. Cursorcore: Assist
programming through aligning anything. arXiv preprint arXiv:2410.07002 (2024).
[12] Xiangyang Li, Kuicai Dong, Yi Quan Lee, Wei Xia, Hao Zhang, Xinyi Dai, Yasheng
Wang, and Ruiming Tang. 2025. CoIR: A Comprehensive Benchmark for Code
Information Retrieval Models. In Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers) (Vienna, Aus-
tria, 2025-07), Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Moham-
mad Taher Pilehvar (Eds.). Association for Computational Linguistics, 22074–
22091. doi:10.18653/v1/2025.acl-long.1072
[13] Ye Liu, Rui Meng, Shafiq Jot, Silvio Savarese, Caiming Xiong, Yingbo Zhou, and
Semih Yavuz. 2024. CodeXEmbed: A Generalist Embedding Model Family for
Multiligual and Multi-task Code Retrieval. arXiv preprint arXiv:2411.12644 (2024).
[14] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiao-
qing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, et al. 2023.
Code llama: Open foundation models for code. arXiv preprint arXiv:2308.12950
(2023).
[15] Saba Sturua, Isabelle Mohr, Mohammad Kalim Akram, Michael Günther, Bo Wang,
Markus Krimmel, Feng Wang, Georgios Mastrapas, Andreas Koukounas, Andreas
Koukounas, Nan Wang, and Han Xiao. 2024. jina-embeddings-v3: Multilingual
Embeddings With Task LoRA. arXiv:2409.10173 [cs.CL]
[16] Jiayi Wei, Greg Durrett, and Isil Dillig. 2024. Coeditor: Leveraging repo-level
diffs for code auto-editing. In The Twelfth International Conference on Learning
Representations.
[17] Weixiang Yan, Yuchen Tian, Yunzhe Li, Qian Chen, and Wen Wang. 2023. Code-
TransOcean: A Comprehensive Multilingual Benchmark for Code Translation. In
Findings of the Association for Computational Linguistics: EMNLP 2023 (Singapore,
2023-12), Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). Association for
Computational Linguistics, 5067–5089. doi:10.18653/v1/2023.findings-emnlp.337
[18] Ziyu Yao, Daniel S Weld, Wei-Peng Chen, and Huan Sun. 2018. StaQC: A Sys-
tematically Mined Question-Code Dataset from Stack Overflow. In Proceedings of
the 2018 World Wide Web Conference on World Wide Web. International World
Wide Web Conferences Steering Committee, 1693–1703.
[19] Zed Industries. 2024. zed-industries/zeta. https://huggingface.co/datasets/zed-
industries/zeta. Accessed: 2026-05-01.
[20] Dejiao Zhang, Wasi Uddin Ahmad, Ming Tan, Hantian Ding, Ramesh Nallap-
ati, Dan Roth, Xiaofei Ma, and Bing Xiang. 2024. CODE REPRESENTATION
LEARNING AT SCALE. In The Twelfth International Conference on Learning
Representations. https://openreview.net/forum?id=vfzRRjumpX
[21] Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang,
Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren Zhou.
2025. Qwen3 Embedding: Advancing Text Embedding and Reranking Through
Foundation Models. arXiv preprint arXiv:2506.05176 (2025).
[22] Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu,
Wenhu Chen, and Xiang Yue. 2024. OpenCodeInterpreter: Integrating Code
Generation with Execution and Refinement. arXiv preprint arXiv:2402.14658
(2024).
55

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/RetNext/page-05.png)
