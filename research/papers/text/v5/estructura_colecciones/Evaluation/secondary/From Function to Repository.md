# From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation

- source_pdf: ../../../../../pdf/Evaluation/secondary/From%20Function%20to%20Repository.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

From Function to Repository: Towards Understanding and an
Agentic Approach for Repo-Level Directed Input Generation
Haoyu Wang∗†‡
Huazhong University of Science and
Technology
Wuhan, China
hy_wang@hust.edu.cn
Ming Wen∗†§
Huazhong University of Science and
Technology
Wuhan, China
mwenaa@hust.edu.cn
Haoran Yan∗†
Huazhong University of Science and
Technology
Wuhan, China
haoran_yan@hust.edu.cn
Jiayi Huang†
Huazhong University of Science and
Technology
Wuhan, China
u202312500@hust.edu.cn
Xuanhua Shi∗¶
Huazhong University of Science and
Technology
Wuhan, China
xhshi@hust.edu.cn
Hai Jin∗¶
Huazhong University of Science and
Technology
Wuhan, China
hjin@hust.edu.cn
Abstract
Directed Input Generation (DIG) aims to automatically construct an
input that reaches a specified target program location. Although
recent studies have shown promising results for Large Language
Models (LLMs) in function-level DIG, it remains unclear whether
such effectiveness generalizes to realistic repository-level testing
scenarios. Unlike function-level settings, repository-level DIG re-
quires reasoning over long call chains, project-specific input se-
mantics, and complex execution conditions distributed across real
software repositories. To address this gap, we present a comprehen-
sive empirical study of repository-level directed input generation
with LLMs. Specifically, we construct a benchmark, RepoEval, con-
taining hard-to-cover target lines across mainstream programming
languages, and evaluate multiple state-of-the-art LLMs under dif-
ferent context and output settings.
Our results show that repository-level DIG remains substantially
more challenging than prior simplified settings. While advanced
models can cover a portion of targets (from 16.02% to 37.35%), their
effectiveness is strongly compromised by repository-specific se-
mantic constraints, context settings, output formats, and external
execution conditions. Based on these findings, we design Agen-
ticDIG, an agentic workflow that integrates target-oriented analy-
sis, intention extraction, fault injection, and iterative feedback to
improve repository-level DIG. Evaluation shows that AgenticDIG
improves target coverage by 43.56% relative to the best baseline.
∗National Engineering Research Center for Big Data Technology and System, Ser-
vices Computing Technology and System Lab, Huazhong University of Science and
Technology (HUST), Wuhan, 430074, China.
†Hubei Engineering Research Center on Big Data Security, Hubei Key Laboratory of
Distributed System Security, School of Cyber Science and Engineering, HUST, Wuhan,
430074, China.
‡Zhongguancun Laboratory, Beijing, China.
§Corresponding author.
¶Cluster and Grid Computing Lab, School of Computer Science and Technology, HUST,
Wuhan, 430074, China.
This work is licensed under a Creative Commons Attribution 4.0 International License.
ASE ’26, Munich, Germany
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2882-2/2026/10
https://doi.org/10.1145/3832783.3837537
CCS Concepts
• Software and its engineering →Software testing and debug-
ging; Automatic programming.
Keywords
Repository-level Directed Input Generation, LLM, Agentic Work-
flows, Software Testing
ACM Reference Format:
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin.
2026. From Function to Repository: Towards Understanding and an Agentic
Approach for Repo-Level Directed Input Generation. In Proceedings of the
41st IEEE/ACM International Conference on Automated Software Engineering
(ASE ’26), October 12–16, 2026, Munich, Germany. ACM, New York, NY, USA,
13 pages. https://doi.org/10.1145/3832783.3837537
1
Introduction
Directed testing is particularly important when developers need to
exercise specific program locations in scenarios such as bug repro-
duction [19, 30, 37], patch testing [46, 54], and targeted vulnerability
analysis [5, 20, 29]. To support this task, a variety of directed test-
ing techniques, including directed greybox fuzzing [5, 19, 28, 54]
and directed symbolic execution [26, 33, 35], have been proposed
recently. The key challenge is to construct valid inputs that sat-
isfy project-specific data semantics, complex constraint conditions,
and execution contexts while still steering the execution toward
the target. This challenge motivates research on directed input
generation [16, 26] (a.k.a., target input generation), which aims to
synthesize inputs that can reach a specified target location.
In recent years, Large Language Models (LLMs) have shown re-
markable effectiveness in code understanding and generation [1, 3,
9, 17, 43, 49]. Recent studies have also explored the application of
LLMs to software testing tasks such as general fuzzing [8, 45, 51],
by leveraging their semantic understanding and code generation
capabilities together with the coverage-guided exploration para-
digm of fuzzing. These studies suggest that LLMs can generate valid
inputs and guide mutation strategies to improve test coverage.
However, Directed Input Generation (DIG) poses a more demand-
ing challenge: beyond producing valid inputs, it also requires guid-
ing execution toward specific target regions in the program. So far,
3062

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
several works have investigated whether LLMs are effective for
function-level DIG. Jiang et al. [16] presented the first systematic
study that compares LLMs against traditional constraint-based ap-
proaches on this task. It shows that LLMs can perform comparably
to, or even better than, traditional constraint-based techniques for
directed test input generation, and has further proposed a hybrid
approach that combines LLMs with constraint solvers to achieve
state-of-the-art performance. In parallel, Wang et al. [41] introduced
TESTEVAL, a benchmark for systematically evaluating LLMs on
targeted test generation tasks, including target code coverage and
target branch coverage. Their results show that, in single-function
test input generation, the best LLM achieves 80.97% targeted line
coverage on average, while most models still benefit only marginally
from explicit target information.
Although prior studies have shown promising results for LLMs
in function-level directed input generation, an open question re-
mains: whether such effectiveness can generalize to real-world
repository-level testing scenarios? In repository-level settings,
the target may only be reachable through long inter-procedural
paths, as illustrated by the target line in Listing 1, which requires
traversing a four-level call chain before entering the target function.
The input space is also more diverse and project-specific, as test
code may accept complex structured inputs such as audio/video
files, serialized objects, or project-specific binary layouts. Moreover,
target reachability is often guarded by multiple distributed con-
straints and affected by external interactions such as file I/O and
memory allocation. As a result, repository-level DIG requires not
only generating syntactically valid inputs, but also reasoning over
repository-wide execution context and target-relevant semantics.
However, the effectiveness of LLMs in addressing these challenges
has not been systematically investigated yet.
To bridge this gap, we first construct a new benchmark based on
OSS-Fuzz [11] testing scenarios to better reflect real-world testing
environments. To avoid trivially coverable targets, we select pro-
gram lines that libFuzzer [25] struggles to reach within a limited
time budget, specifically including lines covered within 12 to 24
hours, lines covered within 24 hours to 7 days, and lines that remain
uncovered after 7 days of fuzzing but are validated as reachable via
code-agent-assisted analysis. Based on this design, we build a new
dataset, RepoEval, which contains 422 target lines collected from
12 real-world repositories across four mainstream programming
languages, namely C, C++, Java, and Python. These target lines
are characterized by challenging constraints, diverse input formats,
and complex execution dependencies, making them suitable for
evaluating repository-level directed input generation. Based on the
dataset, we perform a systematic empirical evaluation of both com-
mercial LLMs (ChatGPT [31], Grok [44]) and open-source LLMs
(DeepSeek [7], Qwen [1]) across a range of prompt settings.
Evaluation results reveal that repository-level directed input
generation is a challenging yet feasible task for modern LLMs. In
particular, DeepSeek-R1 is able to cover 20.83%–37.35% of all target
lines within three attempts under different experimental settings.
Moreover, we find that the output format substantially affects LLM
effectiveness on repository-level directed input generation. In par-
ticular, prompting models to generate Python-based input gener-
ators is consistently more effective than asking them to directly
produce base64-encoded inputs. We also find that the choice of code
context plays a critical role. Among the three evaluated context
settings, call-chain context provides the most effective support over-
all, whereas agent-constructed context does not yield consistent
gains. A possible explanation is that agent-constructed context may
not always recover the target-relevant call chain accurately, which
can introduce irrelevant information or miss critical dependencies
needed to reach the target. We further analyze the performance un-
der different call-chain depths and different target difficulty levels.
Moreover, through a more in-depth failure analysis, we find that
the remaining hard cases stem from multiple sources. For instance,
some targets can only be triggered under external failure conditions,
such as file I/O errors or memory allocation failures, while others
require satisfying difficult numeric or structural constraints.
Based on the above findings, we propose AgenticDIG, an agentic
workflow for repository-level directed input generation. For targets
guarded by externally induced exceptional conditions, AgenticDIG
introduces a Fault Injection Agent to emulate scenarios such as
file I/O failures, resource exhaustion, and network disconnection
through source-code-level mock modules. For targets involving
complex semantic constraints, AgenticDIG uses an Intention Anal-
ysis Agent to summarize constraint intentions and derive actionable
input-generation guidance. AgenticDIG further includes a Gener-
ate & Verification Agent to synthesize and validate Python-based
input generators, and a Refinement Agent to diagnose path devi-
ations and guide subsequent attempts using execution feedback.
Together, these agents form a closed-loop workflow that addresses
the major failure modes identified in our empirical study. We further
evaluate AgenticDIG across different target characteristics and
component ablations, showing that its improvements are consistent
across call-chain depths and difficulty levels. More importantly, the
intention analysis, fault injection, and refinement all contribute to
the overall effectiveness. The main contributions of this work are
as follows:
• Extensive Study. We present a comprehensive empirical study
of repository-level directed input generation with large language
models, extending prior function-level studies to more realistic
repository-level testing scenarios.
• Benchmark. We construct a new benchmark from OSS-Fuzz
repositories and use it to systematically evaluate multiple state-
of-the-art LLMs under different context and output settings.
• Approach. Based on our empirical findings, we design an agentic
workflow, AgenticDIG, to better support repository-level DIG
through target-oriented analysis and iterative refinement, which
outperforms existing methods by at least 43.56% relatively.
• Open Science. We open-source our tool as well as the benchmark
at: https://github.com/CGCL-codes/RepoEval.
2
Background and Motivation
2.1
Existing Benchmarks
Directed Input Generation (DIG) [26] aims to automatically con-
struct an input that drives execution to a specified target location.
Compared with general valid-input generation, DIG is more de-
manding because it requires not only producing valid inputs, but
also satisfying target-reaching conditions. Existing studies have ex-
plored whether large language models (LLMs) are effective for this
task. For example, Jiang et al. [16] compared LLMs with traditional
3063

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
constraint-based techniques for function-level DIG, showing that
strong LLMs can be competitive in this setting. Wang et al. [41]
further introduced TESTEVAL for evaluating LLMs on targeted test
generation tasks and reported that the best model achieves 80.97%
targeted line coverage on average in single-function settings.
In addition to DIG-oriented benchmarks, the fuzzing commu-
nity has developed several mature benchmark platforms, such as
FuzzBench [27], Magma [12], and UNIFUZZ [22]. Although their
programs or bug locations could in principle be adapted into target-
reaching tasks, these benchmarks are primarily designed for eval-
uating fuzzer performance or bug-finding capability. Their bug-
oriented targets are limited in scale and diversity for systematically
studying repository-level DIG across languages, domains, call-chain
depths, and difficulty levels. Therefore, directly using them is insuf-
ficient for evaluating whether an input-generation method can syn-
thesize target-directed inputs by reasoning about repository-level
call chains, input semantics, and hard target-reaching conditions.
Beyond these general fuzzing benchmarks, existing DIG-specific
benchmarks also mainly focus on function-level, where target-
relevant constraints are local and easy to isolate. They therefore
cannot adequately capture repository-level challenges involving
long call chains, project-specific semantics, and cross-file depen-
dencies, motivating our study.
2.2
Motivation Example
Listing 1 shows a motivating example from sqlite3 [39]. The target
line (line 54) is located in sqlite3WhereCodeOneLoopStart() and
remains uncovered after seven days of continuous fuzzing with
libFuzzer [25], as a representative hard-to-cover repository-level
DIG target. Specifically, reaching the target requires a repository-
level data-flow chain that propagates information from the input
SQL statement to the target branch. First, sqlite3_prepare_v2()
parses the input SQL text and constructs the internal statement rep-
resentation (lines 4–7). For an UPDATE on a virtual table, the parsed
LIMIT/OFFSET expression is then passed to sqlite3Update() and
subsequently into the query-planning logic through the function in
Node 2 (i.e. sqlite3WhereBegin()). In sqlite3WhereAddLimit(),
the OFFSET expression flows through a series of structural checks
and is converted into a virtual-table constraint labeled SQLITE_INDEX
_CONSTRAINT_OFFSET (lines 25–38). This constraint is later repre-
sented by pTerm->eMatchOp in sqlite3WhereCodeOneLoopStart()
(Node 4). Meanwhile, the virtual-table planning process must mark
the constraint as omitted, which propagates to the statement pLoop->
u.vtab.bOmitOffset. The target branch is reached only when
both data-flow results meet: the current term represents the propa-
gated OFFSET constraint and bOmitOffset is set (lines 47–54).
This example illustrates why repository-level DIG is more chal-
lenging than function-level target reaching: the generated input
must not only be valid, but also cause input-derived values and prop-
erties to propagate through multiple intermediate representations
and functions until they satisfy the target predicate. Interestingly,
DeepSeek-V3.2 generates a target-reaching input in a single query:
CREATE VIRTUAL TABLE vt USING fts4(content);
INSERT INTO vt(content) VALUES('test');
UPDATE vt SET content='updated '
WHERE rowid MATCH 'test'
OFFSET 1;
1
// Node 1: src/prepare.c:937
sqlite3_prepare_v2 ()
2
int sqlite3_prepare_v2(sqlite3 *db, const char *zSql , ...,){
3
...
4
rc = sqlite3LockAndPrepare(db, zSql , nBytes ,
5
SQLITE_PREPARE_SAVESQL , 0,
6
ppStmt , pzTail);
7
/* input: must be valid SQL text , or all later stages are skipped */
8
return rc;
9
}
10
---------------------------------------------------------------
11
// Node 2: src/update.c:285
sqlite3Update ()
12
void sqlite3Update(
13
...,
14
SrcList
*pTabList ,
/* input: UPDATE target must be a virtual table */
15
Expr
*pLimit ,
/* input: LIMIT/OFFSET clause must be present */
16
){
17
...
18
pWInfo = sqlite3WhereBegin(pParse , pTabList , pWhere ,
19
0, 0, 0, flags , iIdxCur);
20
...
21
}
22
---------------------------------------------------------------
23
// Node 3: src/whereexpr.c:1650
sqlite3WhereAddLimit ()
24
void SQLITE_NOINLINE sqlite3WhereAddLimit(WhereClause *pWC , Select *p){
25
if( p->pGroupBy ==0
26
/* input: no GROUP BY */
27
&& (p->selFlags &
28
(SF_Distinct|SF_Aggregate))==0
29
/* input: not DISTINCT or aggregate */
30
&& (p->pSrc ->nSrc ==1
31
&& IsVirtual(p->pSrc ->a[0]. pSTab))
32
/* input: exactly one virtual -table source */
33
){
34
...,
35
whereAddLimitExpr(pWC , p->iOffset ,
36
p->pLimit ->pRight , iCsr ,
37
SQLITE_INDEX_CONSTRAINT_OFFSET);
38
/* only reached when all conditions hold */
39
}
40
}
41
---------------------------------------------------------------
42
// Node 4: bld/sqlite3.c:163977
sqlite3WhereCodeOneLoopStart ()
43
for(j=0; j<nConstraint; j++){
44
...
45
}else{
46
codeExprOrVector(pParse , pTerm ->pExpr ->pRight , iTarget , 1);
47
if( pTerm ->eMatchOp == SQLITE_INDEX_CONSTRAINT_OFFSET
48
/* current term is the OFFSET constraint (Node 3) */
49
&& pLoop ->u.vtab.bOmitOffset
50
// vtab declared it owns OFFSET (Node 4)
51
){
52
sqlite3VdbeAddOp2(v, OP_Integer , 0,
53
pWInfo ->pSelect ->iOffset);
54
VdbeComment ((v,"Zero OFFSET counter"));// <-- TARGET LINE
55
}
56
}
57
}
Listing 1: A motivating SQLite example with cross-function
constraints
Specifically, the above input reaches the target by creating a vir-
tual table, issuing an UPDATE statement, and introducing an OFFSET
clause that can be propagated into SQLite’s query-rewriting logic.
This suggests that the model can combine SQL prior knowledge
with repository-level cues, such as VIRTUAL TABLE, UPDATE, and
OFFSET, to form a coherent input pattern that satisfies distributed
constraints. While this case shows the potential of LLMs for repos-
itory level DIG, it also raises a broader question: whether such
capability can be systematically understood and generalized across
real repositories. This motivates our construction of RepoEval,
a benchmark designed to capture inter-procedural dependencies,
project-specific semantics, and complex target-reaching constraints
beyond simplified function-level settings.
3
Benchmark Construction
To comprehensively evaluate LLMs on repository-level directed
input generation, which requires reasoning about code semantics,
call-chain dependencies, and target-reaching constraints beyond
local snippets, we construct a benchmark through a two-stage se-
lection process. First, we select representative repositories from
OSS-Fuzz [11], which provides mature fuzzing harnesses, repro-
ducible build configurations, and diverse real-world projects across
3064

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
Table 1: Demographics of our benchmark. ‘Eligible’ denotes
the number of repositories after filtering
Language
Category
Eligible
Final Repo
Targets
Stars
C++
text
23
jansson
40
3.3k
codec
45
exiv2
40
1.1k
net
72
cpp-httplib
40
16.2k
database
9
sqlite3
42
9.2k
Java
text
18
jsoup
42
11.3k
codec
6
metadata-extractor
31
2.8k
net
10
async-http-client
42
6.4k
database
11
jedis
37
12.3k
Python
text
13
pycparser
21
3.5k
codec
7
mutagen
26
3.9k
net
12
scapy
30
12.1k
database
6
sqlparse
31
4.0k
Total
422
programming languages and application domains. Second, we iden-
tify challenging target lines in these repositories to cover different
difficulty levels and execution scenarios.
3.1
Repository Selection
To build a high-quality benchmark for repository-level directed
input generation, we select C/C++, Python, and Java projects from
OSS-Fuzz [11]. Our selection aims to balance practical relevance,
project quality, and cross-language representativeness. Specifically,
we apply five filtering criteria: (1) the project is integrated into
OSS-Fuzz with complete configuration files, and can be successfully
built; (2) it has been actively maintained within the last six months;
(3) it shows community adoption, e.g., at least 500 GitHub stars; (4)
the target language accounts for more than 70% of the codebase;
and (5) the project contains more than 10,000 code lines.
Following repo-selection principles used in prior fuzzing bench-
marks such as MAGMA [12], FuzzBench [27], and UNIFUZZ [22],
we explicitly consider cross-domain software diversity. We group
candidate repositories into four functional domains: text-based for-
mat parsers, codecs (i.e., libraries for encoding and decoding binary
data such as audio and video), network protocols, and databases.
The Eligible column in Table 1 reports the number of repositories
remaining after the initial filtering process.
We then select one representative repository for each language–
domain combination, resulting in 12 repositories in total. In this
step, we prioritize repositories that are representative within their
domains, exhibit sufficiently complex control flow and call-graph
structure, and show diverse input-dependent execution behaviors
so that different inputs can meaningfully affect reachability. We also
consider language-specific characteristics, such as manual memory
management in C/C++, dynamic features in Python, and object-
oriented programming patterns in Java.
3.2
Target Line Selection
To identify meaningful target lines at varying difficulty levels, we
employ a systematic approach based on empirical coverage analysis
as adopted in LibFuzzer [25], the default coverage-guided engine
in OSS-Fuzz [11]. Specifically, we focus on selecting lines that are
reachable yet difficult to cover, excluding dead code that cannot be
exercised through valid inputs.
Table 2: Distribution of RepoEval targets by fuzzing-based
difficulty and call-chain depth
Difficulty
Call depth
Total
1–2
3–5
6–8
9+
Medium
29
87
60
23
199
High
15
28
17
14
74
Exceptional
27
59
38
25
149
Total
71
174
115
62
422
3.2.1
Coverage-Based Analysis. For each selected repository, we
conduct fuzzing campaigns using LibFuzzer with three indepen-
dent 7-day runs to ensure statistical reliability. Following prior
studies [15, 23, 52], we record coverage snapshots at three repre-
sentative fuzzing time milestones: 12 hours, 24 hours, and 7 days.
The coverage results from the three independent runs were merged
to account for the stochastic nature of fuzzing. Based on these
measurements, we categorize target lines into three fuzzing-based
difficulty tiers: (1) medium-difficulty lines covered between 12 and
24 hours, (2) high-difficulty lines covered between 24 hours and
7 days, and (3) exceptional-difficulty lines that remain uncovered
after 7 days of continuous fuzzing. We use 7 days as the longest
fuzzing budget following the long-running fuzzing practice [24].
We do not impose an additional upper bound on the last tier, as
this would exclude valuable reachable targets that remain beyond
fuzzing’s capability under this extended budget.
3.2.2
Diversity-Oriented Selection. We further perform the follow-
ing selection. First, for the medium-difficulty and high-difficulty
tiers, candidate lines within each tier are grouped by conditional
branch since lines in the same branch often share similar reachabil-
ity conditions and input constraints. We therefore avoid selecting
multiple lines from the same branch. Second, after branch-level
clustering, we further stratify the remaining candidates by static
call-chain depth, i.e., the minimum number of function calls re-
quired to reach the target line from program entry points. For each
call-depth level, we randomly select 1-3 representative targets to
cover both shallow and deep execution paths.
As for the exceptional-difficulty tier (lines uncovered after 7 days),
we instead perform reachability validation. We prioritize uncovered
lines in partially covered functions. By contrast, lines in completely
uncovered functions were excluded, as they are more likely to
correspond to dead code or functionality requiring unavailable en-
vironmental support. To mitigate the risk of including unreachable
code in the exceptional-difficulty type, we further combine code-
agent-assisted analysis with manual inspection to check whether
feasible paths exist from the fuzz driver to the target line.
The above process ensures that the obtained target lines cover
various difficulty levels, control-flow locations, and call-chain depths.
Specifically, we collect a total of 422 target lines, each annotated
with a difficulty level and a call-chain depth (see Table 2). We fur-
ther provide target metadata, fuzzing logs, call-chain extraction
scripts, prompt templates, generated inputs, and execution scripts
to support reproducible benchmark construction.
3065

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
3.3
Evaluation Framework
We implement a prompt-based framework to evaluate large lan-
guage models on directed input generation. Given a benchmark
instance consisting of a fuzz driver and a target line, the frame-
work prompts the model to generate an input that drives execution
toward the specified target.
Each prompt contains four components: (1) a task descrip-
tion specifying the target function and line; (2) the fuzz driver as
the input entry point; (3) the code context, with the target line
explicitly marked; and (4) the required output format. Because
target files contain 3,847.58 lines on average, the file-level setting
includes up to 2,000 lines before and after the target to expose
nearby branch conditions and data dependencies. The model ei-
ther returns a Base64-encoded input or generates a Python input
generator, following prior LLM-enhanced fuzzing work [18, 51].
4
Evaluation Setup
Research Questions. In this study, we aim to understand the
effectiveness of LLMs on repository-level directed test input gen-
eration. More importantly, we seek to systematically characterize
the capability boundaries and limitations of LLMs and explore how
to improve their performance. To achieve this goal, we design four
research questions as follows:
RQ1: How effective are LLMs for repository-level directed
test input generation?
RQ2: How do different code context settings affect the effec-
tiveness of LLM-based directed input generation?
RQ3: What factors characterize the difficulty of repository-
level directed input generation?
RQ4: Why do LLMs fail on difficult directed input generation?
Evaluation Metric. We use the pass rate, Pass@K, as the eval-
uation metric in this study, following existing practices [16, 41].
It measures the proportion of target lines that can be reached by
LLM-generated inputs within a bounded number of queries.
Let 𝑁be the total number of target lines in the dataset. For each
target line 𝑡𝑖(where 𝑖= 1, 2, . . . , 𝑁), we query the LLM at most 𝐾
times. Each query produces one input 𝐼𝑖𝑗(where 𝑗= 1, 2, . . . , 𝐾),
which is then executed to test whether it reaches 𝑡𝑖. For each target
line, we define a boolean variable 𝑝𝑖: 𝑝𝑖= 1 if at least one of the
generated inputs reaches 𝑡𝑖, and 𝑝𝑖= 0 otherwise. The overall pass
rate is computed as: 𝑃𝑎𝑠𝑠@𝐾=
Í𝑁
𝑖=1 𝑝𝑖
𝑁
.
Studied LLMs. The LLMs evaluated in this study are selected
from those with strong performance on established code bench-
marks. Additionally, our selection process also considers several
practical factors, including computational and financial cost, com-
munity adoption, and prior usage in academic works [6, 13, 21, 42].
The final selection, as shown in Table 3, includes both open-source
and closed-source models with different specialization types. We se-
lect DeepSeek-V3.2 [7] and GPT-5-mini [31] as representative open-
source and commercial general-purpose LLMs, respectively. To
cover code-specialized models, we further include Qwen3-Coder-
Flash [1] and Grok-Code-Fast-1 [44], where Grok-Code-Fast-1 ad-
ditionally provides strong reasoning capabilities. Moreover, we
include DeepSeek-R1 [7] as a representative of reasoning LLMs.
Table 3: LLMs used in the empirical study
Access
Type
Model
Knowledge Cutoff
Open-source
Code
Qwen3-Coder-Flash
2024-10
Open-source
General
DeepSeek-V3.2
2025-05
Closed-source
General
GPT-5-mini
2024-05-30
Open-source
Reason
DeepSeek-R1
2025-05
Closed-source
Code&Reason
Grok-Code-Fast-1
2025-08-02*
* Indicates the model release date when the actual knowledge cutoff is unavailable.
5
Evaluation Result
5.1
RQ1: Effectiveness of LLMs
In this RQ, we evaluate each model on all RepoEval targets and
report Pass@1 and Pass@3 under the Base64 and Python-code
output settings.
5.1.1
Overall Performance. Table 4 summarizes the overall perfor-
mance of the five selected LLMs on our dataset. For each repository,
we report the pass rates achieved by each model under Pass@1 and
Pass@3, respectively, for both pycode and base64 output settings.
The results under the file-level context setting suggest that LLMs
already show strong potential for repository-level directed input
generation. Although the target lines in our benchmark are hard-
to-cover locations that are difficult for traditional fuzzing tools
to reach reliably, the best result can already cover up to 85.71%
of the target lines on a single project (e.g., Grok-Code-Fast-1 with
Pass@3 on sqlite3 under the pycode output setting). In terms of
overall performance, DeepSeek-R1 with the pycode output setting
achieves the best aggregate results, reaching 37.35% average target-
line coverage under Pass@3.
In contrast, Qwen3-Coder-Flash performs worse than the other
models, possibly due in part to weaker generation validity: it ap-
pears less effective at producing valid serialized inputs under the
base64 setting, and its generated Python code is often template-
driven, making it harder to satisfy repository-specific constraints.
Finding 1. LLMs show promising effectiveness on repository-level
directed input generation. The best-performing model achieves
37.35% average coverage, and repeated attempts further improve
success rates. Among the evaluated models, DeepSeek-R1 and
Grok-Code-Fast-1 achieve the best overall performance.
5.1.2
Output Perspective. The output setting has a substantial im-
pact on repository-level directed input generation. Overall, the
pycode setting consistently outperforms base64 across all five eval-
uated LLMs. Averaged across all models, pycode increases Pass@1
from 12.39% to 24.53% and Pass@3 from 15.95% to 30.13%, nearly
doubling the overall success rate. This advantage is observed for
every model: for example, Pass@3 improves from 22.80% to 36.28%
for GPT-5-mini, from 10.23% to 26.55% for DeepSeek-V3.2.
This advantage is especially pronounced when the desired inputs
are human-unreadable binary data. For example, averaged across
the five models, the Pass@3 rate rises from 13.00% to 34.00% on
exiv2, from 7.64% to 40.98% on mutagen, and from 5.41% to 28.65%
on metadata-extractor when switching from base64 to pycode. In
contrast, for repositories whose inputs are human-readable textual
3066

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
Table 4: Overall performance of LLMs on the benchmark
Language
C/C++
Java
Python
Models
Output Setting
project
cpp-*
exiv2
jansson
sqlite3
async-*
jedis
jsoup
metadata-*
mutagen
pycparser
scapy
sqlparse
Ave(Models)
Pass@1
15.00
17.50
20.00
23.81
9.52
19.35
9.52
10.81
4.80
0.00
0.00
58.06
15.70
Base64
Pass@3
17.50
32.50
22.50
28.57
9.52
70.97
11.90
10.81
4.80
0.00
0.00
64.52
22.80
Pass@1
27.50
45.00
25.00
47.62
9.52
19.35
11.90
37.84
42.90
0.00
3.30
64.52
27.87
GPT-5-mini
Python Code
Pass@3
27.50
47.50
25.00
52.38
23.81
70.97
14.29
56.76
42.90
0.00
3.30
70.97
36.28
Pass@1
12.50
2.50
0.00
2.38
0.00
19.35
9.52
0.00
4.80
0.00
0.00
54.84
8.82
Base64
Pass@3
12.50
2.50
0.00
9.52
0.00
19.35
9.52
0.00
4.80
0.00
0.00
64.52
10.23
Pass@1
27.50
25.00
17.50
35.71
26.19
16.13
16.67
24.32
19.00
0.00
0.00
54.84
21.91
DeepSeek-V3.2
Python Code
Pass@3
27.50
42.50
17.50
45.24
26.19
16.13
16.67
27.03
28.60
0.00
6.70
64.52
26.55
Pass@1
12.50
7.50
5.00
33.33
23.81
19.35
14.29
8.11
0.00
3.80
0.00
64.52
16.02
Base64
Pass@3
12.50
25.00
12.50
40.48
23.81
19.35
14.29
10.81
19.00
7.70
0.00
64.52
20.83
Pass@1
27.50
35.00
20.00
38.10
9.52
16.13
14.29
29.73
52.40
0.00
46.70
64.52
29.49
DeepSeek-R1
Python Code
Pass@3
57.50
45.00
20.00
47.62
26.19
19.35
16.67
29.73
61.90
0.00
50.00
74.20
37.35
Pass@1
17.50
2.50
5.00
11.90
26.19
70.97
11.90
5.41
4.80
0.00
0.00
58.06
17.85
Base64
Pass@3
17.50
2.50
7.50
47.62
26.19
70.97
14.29
5.41
4.80
0.00
0.00
67.74
22.04
Pass@1
22.50
27.50
22.50
73.81
9.52
67.74
16.67
24.32
38.10
0.00
6.70
61.29
30.89
Grok-Code-Fast-1
Python Code
Pass@3
27.50
35.00
25.00
85.71
23.81
70.97
16.67
27.03
42.90
0.00
13.30
67.74
36.30
Pass@1
0.00
2.50
0.00
0.00
0.00
16.13
0.00
0.00
4.80
0.00
0.00
19.35
3.57
Base64
Pass@3
0.00
2.50
0.00
0.00
0.00
16.13
0.00
0.00
4.80
0.00
0.00
22.58
3.83
Pass@1
0.00
0.00
0.00
0.00
0.00
67.74
0.00
0.00
23.80
0.00
3.30
54.84
12.47
Qwen3-Coder-Flash
Python Code
Pass@3
0.00
0.00
2.50
7.14
0.00
67.74
0.00
2.70
28.60
0.00
6.70
54.84
14.19
Pass@1
11.50
6.50
6.00
14.28
11.90
29.03
9.05
4.87
3.84
0.76
0.00
50.97
12.39
Base64
Pass@3
12.00
13.00
8.50
25.24
11.90
39.35
10.00
5.41
7.64
1.54
0.00
56.78
15.95
Pass@1
21.00
26.50
17.00
39.05
10.95
37.42
11.91
23.24
35.24
0.00
12.00
60.00
24.53
Ave(Repo)
Python Code
Pass@3
28.00
34.00
18.00
47.62
20.00
49.03
12.86
28.65
40.98
0.00
16.00
66.45
30.13
data, the gain is much smaller. For example, the average Pass@3
only changes from 10.00% to 12.86% on jsoup.
Finding 2. Overall, prompting LLMs to generate Python-based
input generators (python code) is consistently more effective than
asking them to directly output base64-encoded inputs, improving
the average Pass@3 from 15.95% to 30.13%.
5.2
RQ2: Impact of Context
Motivated by the performance variation observed in RQ1 under
the file-level context setting, we further investigate the role of code
context in repository-level directed input generation. To this end,
we compare three context settings, file-level context, call-chain con-
text, and agent context, under two output formulations, Base64 and
Python code. As shown in Figure 1, we evaluate all settings across
the selected models and three language groups, C/C++, Java, and
Python, to study how context and output setting affect Pass@3.
5.2.1
Context Settings. We compare three context settings with
different levels of target-relevant information. The file-level context
is the default setting used in RQ1, while call-chain context and
agent context are introduced in RQ2 to provide richer support for
repository-level directed input generation.
• File-level Context. This setting provides a local code window
centered on the target line within the target file, including 2,000
lines before and after the target line. It preserves rich local im-
plementation details, but may miss constraints distributed across
callers or other files.
• Call-chain Context. This setting augments the file-level context
with inter-procedural information derived from the call graph.
We use CodeQL [10], Soot [38], and PyCG [40] to extract call-
chain information for C/C++, Java, and Python, respectively.
Starting from the test entry point, we identify call chains that
can reach the target and collect the code of functions along the
selected chain as additional context. If multiple call chains exist,
we choose the shortest one; if none can be identified, we use only
the entry function and target function. This setting is designed to
expose how inputs are propagated and constrained across calls.
• Agent Context. This setting constructs context through an LLM-
based code agent. Built on top of OpenCode [32], the agent is
given the DIG task, fuzz driver, and target line, and then analyzes
the repository to trace relevant call chains and extract target-
relevant code fragments as context. To avoid conflating context-
construction ability with downstream input generation, we use
DeepSeek-R1, the best model in RQ 5.1, as model for this stage,
following prior benchmark practice [36].
These three context settings are designed as independent and
parallel configurations. On average, the resulting prompts contain
6.59M tokens for file-level context, 0.43M tokens for call-chain con-
text, and 2.32M tokens for agent context.
5.2.2
Context Impact. Figure 1 reports the Pass@3 results under
three context settings, namely file-level context, call-chain context,
and agent context. For each evaluated LLM, the figure further distin-
guishes two output settings, Base64 and Python Code, and reports
results separately for C/C++, Java, and Python repositories.
Overall, context construction has a substantial impact on perfor-
mance, and call-chain context achieves the best average results in
all three language groups. Specifically, when moving from file-level
context to call-chain context, the average Pass@3 increases from
20.65% to 22.91% on C/C++, from 18.44% to 22.57% on Java, and
from 23.14% to 35.51% on Python. The improvement is especially
pronounced on Python repositories, where call-chain context con-
sistently yields the strongest results across nearly all models and
output settings.
In contrast, agent context does not provide consistent gains. Its
average Pass@3 is only 14.26% on C/C++, 12.04% on Java, and
17.13% on Python, all substantially lower than call-chain context
(22.91%, 22.57%, and 35.51%) and also below file-level context (20.65%,
3067

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
GPT5m
DS-V3
DS-R1
GrokF
Q3F
0
10
20
30
40
50
Pass@3 Rate (%)
C/C++
GPT5m
DS-V3
DS-R1
GrokF
Q3F
0
10
20
30
40
Java
GPT5m
DS-V3
DS-R1
GrokF
Q3F
0
10
20
30
40
50
60
70
Python
File Level
Call Chain
Agent
Base64
Python Code
Figure 1: Performance under different context settings. Models are abbreviated as follows: GPT5m (GPT-5-mini), DS-V3
(DeepSeek-V3.2), DS-R1 (DeepSeek-R1), GrokF (Grok-Code-Fast-1), and Qw3F (Qwen3-Coder-Flash)
Table 5: Pass@3 under different call-chain depths
Depth Range
1-2
3-5
6-8
9+
Total Case
71
174
115
62
DeepSeek-V3.2
0.296
0.359
0.253
0.263
DeepSeek-R1
0.423
0.389
0.302
0.273
GPT-5-mini
0.493
0.364
0.290
0.273
Grok-Code-Fast-1
0.437
0.374
0.241
0.222
Qwen3-Coder-Flash
0.296
0.237
0.111
0.071
Average
0.389
0.345
0.239
0.221
18.44%, and 23.14%). Although agent context is occasionally com-
petitive in individual cases, such as some Java and Python settings,
its overall performance remains unstable and clearly inferior on
average. This result suggests that richer context is beneficial only
when the added information remains closely aligned with the actual
execution path to the target. A plausible explanation is that agent-
constructed context may not always recover the target-relevant
call chain with sufficient precision, thereby introducing irrelevant
information or missing critical dependencies needed to reach the
target. Importantly, such weaker performance should not be inter-
preted as a general limitation of agent-based context construction.
Rather, it reflects the limitation of our current OpenCode-based
context-construction strategy under the given prompt design and
inference budget: the agent may select plausible but path-irrelevant
snippets or miss critical input-propagation functions because its
context construction is not constrained by the recovered call path.
Finding 3. Call-chain context achieves the best overall perfor-
mance and consistently outperforms file-level context. The current
agent-context setting shows less stable improvements, suggesting
that LLMs benefit more when the provided context is explicitly
aligned with the actual execution path to the target.
5.3
RQ3: Target Difficulty Characterization
In this RQ, we investigate what factors characterize the difficulty
of repository-level directed input generation targets. We analyze
difficulty from two complementary perspectives. First, we examine
whether structural depth, measured by call-chain depth, is associ-
ated with target coverage. Second, we study fuzzing-based target
difficulty levels, i.e., targets covered within 12h–24h, covered within
24h–7d, and still uncovered after 7 days of fuzzing. Following the
12h-24h
24h-7d
7d uncover
56.28% 39.70% 45.23% 47.24% 10.05% 39.70%
41.89% 43.24% 44.59% 59.46% 12.16% 40.27%
20.81% 16.11% 14.77% 20.13% 6.71% 15.70%
12h-24h
24h-7d
7d uncover
48.24% 45.23% 49.75% 46.23% 26.13% 43.12%
59.46% 48.65% 55.41% 47.30% 16.22% 45.41%
27.52% 22.82% 27.52% 26.17% 14.09% 23.62%
GPT5m DS-V3
DS-R1
GrokF
Q3F
Avg
12h-24h
24h-7d
7d uncover
37.19% 25.13% 29.65% 28.14% 5.03% 25.03%
25.68% 27.03% 48.65% 43.24% 4.05% 29.73%
15.44% 10.07% 11.41% 11.41%
6.04% 10.87%
0.0
0.5
File Level
0.0
0.5
Call Chain
0.0
0.5
Agent
Figure 2: Performance (Pass@3) under different target diffi-
culty levels and context settings
strongest configuration identified earlier, we conduct this analysis
using DeepSeek-R1 with Python code as the output format. Our goal
is to determine whether repository-level DIG difficulty is mainly
explained by structural properties or by the intrinsic hardness of
the target-reaching constraints.
5.3.1
Impact of Call-Chain Depth. We further analyze whether
call-chain depth is associated with target coverage in repository-
level directed input generation. Table 5 groups all targets into four
depth ranges: 1–2, 3–5, 6–8, and 9+, containing 71, 174, 115, and
62 targets, respectively. On average, coverage decreases as depth
increases, from 0.389 for depth 1–2 to 0.345 for depth 3–5, 0.239 for
depth 6–8, and 0.221 for depth 9+.
An exception is DeepSeek-V3.2, which performs slightly better
at depth 3–5 than at depth 1–2. This non-monotonic result likely
reflects target composition and sample variation rather than an in-
herent advantage of medium-depth targets, as some shallow targets
may still contain restrictive local constraints.
Finding 4. Increasing call-chain depth generally reduces
repository-level DIG performance. However, this effect is not
strictly monotonic across all models.
5.3.2
Impact of Target Difficulty. We next analyze whether fuzzing-
based target difficulty is associated with repository-level directed
input generation performance. Specifically, we divide all targets into
3068

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
Table 6: Multi-label root cause taxonomy of failed cases
Category
Description
Ratio (%)
Domain-
specific
constraints
The generated input violates repository-
specific semantic requirements, such as
protocol or file-format rules.
35.23
Exception
handling
The target lies on an error-handling path
triggered by abnormal inputs, environment
failures, or resource constraints.
23.11
Structural
constraints
The generated input fails to satisfy required
properties of input-dependent internal data
structures, such as non-null fields.
21.21
Numeric
constraints
Target reachability depends on precise nu-
meric conditions, such as floats, or offsets.
18.56
Call-chain
recovery
Static analysis recovers the call chain im-
precisely, causing missing or misleading
context.
10.61
Other
Do not fit the above categories.
6.82
Sum
-
115.54
the three difficulty levels introduced in Section 3.2: targets covered
within 12h–24h, targets covered within 24h–7d, and targets still
uncovered after 7 days of fuzzing. Figure 2 shows the corresponding
pass rates of different models under three context settings.
Overall, the clearest pattern is that the 7d uncover group is sub-
stantially harder than the other two groups across almost all models
and context settings. For instance, under File Level, the average pass
rate drops from 39.70% and 40.27% on the first two groups to 15.70%
on the 7d uncover group. In contrast, the first two difficulty groups
do not show a stable monotonic trend. In several cases, targets
covered within 24h–7d are comparable to, or even easier than,
those covered within 12h–24h. For example, under File Level, Grok-
Code-Fast-1 increases from 47.24% to 59.46%, and under Call Chain
Context, DeepSeek-V3.2 rises from 45.23% to 48.65%. This suggests
that, within fuzzing-coverable targets, fuzzing difficulty does not
increase linearly with LLM difficulty.
Finding 5. Fuzzing-based target difficulty is strongly associated
with repository-level directed input generation performance. In
particular, targets uncovered after 7 days of fuzzing are consis-
tently much harder for LLMs, while the two fuzzing-coverable
groups show no stable monotonic difference.
5.4
RQ4: Failure Analysis
Building on the results of RQ2, we next examine why LLMs still fail
on repository-level directed input generation. To reduce confound-
ing effects from weaker models or less effective prompt settings,
we focus this analysis on the strongest configuration identified in
our evaluation, namely DeepSeek-R1 under the call-chain context
setting with Python-code output, measured at Pass@3. Specifically,
we analyze the target instances that remain uncovered after three
attempts under this configuration. Analyzing failures under the
best-performing setting allows us to more directly characterize the
remaining challenges of repository-level DIG, rather than artifacts
of weaker configurations.
5.4.1
Failure Taxonomy. To derive the failure taxonomy, we first
perform an inductive review of these unsuccessful instances and
1
// Context 1: layers/kerberos.py:2307
Protocol parser expects ASN.1 format
2
class Kerberos(ASN1_Packet):
/* Hint: ASN.1 encoded packet */
3
ASN1_codec = ASN1_Codecs.BER
/* Hint: BER encoding required */
4
ASN1_root = ASN1F_CHOICE (..., KRB_GSSAPI_Token , ...)
5
6
---------------------------------------------------------------
7
// Context 2: layers/kerberos.py:2145
InnerToken must be wrapped
8
class KRB_GSSAPI_Token(GSSAPI_BLOB):
9
ASN1_codec = ASN1_Codecs.BER
10
ASN1_root = ASN1F_SEQUENCE(
11
ASN1F_OID("MechType", "1.2.840.113554.1.2.2"),
12
ASN1F_PACKET("innerToken", KRB_InnerToken (), ...),
13
/* Hint: InnerToken is nested */
14
)
15
---------------------------------------------------------------
16
// Context 3: layers/kerberos.py:2137
Magic bytes for identification
17
if _pkt [2:13] == b"\x06\t*\x86H\x86\xf7\x12\x01\x02\x02":
18
/* Hint: GSSAPI Token signature */
19
return KRB_GSSAPI_Token
20
---------------------------------------------------------------
21
// Target: layers/kerberos.py:2128
Function to reach
22
class KRB_InnerToken(Packet):
23
def guess_payload_class(self , payload):
24
if self.TOK_ID in [b"\x01\x01",b"\x02\x01",b"\x04\x04",b"\x05\x04"]:
25
return conf.padding_layer
// <-- TARGET LINE 2130
26
return Kerberos
Listing 2: A fail case in Domain-specific constraints category
1
// com/drew/lang/StreamReader.java :76
2
public byte[] getBytes(int count) throws IOException
3
{
4
try {
5
byte[] bytes = new byte[count];
// Memory allocation
6
getBytes(bytes , 0, count);
7
return bytes;
8
} catch (OutOfMemoryError e) {
9
throw new EOFException("End of data reached.");// TARGET LINE 76
10
}
11
}
Listing 3: A fail case in Exception handling category
identify recurring failure patterns, which are then consolidated
into a set of candidate categories. After refining the category defini-
tions, we use them as explicit annotation criteria for the subsequent
labeling process. Two authors independently label each failed in-
stance with all applicable failure categories, based on observable
evidence from the target code, the associated fuzz driver, the gen-
erated Python script, and the coverage outcome. This multi-label
annotation allows a single failed case to be associated with mul-
tiple root causes when several constraints jointly prevent target
coverage. Disagreements were then resolved through discussion,
followed by an additional review from a third author. All three an-
notators have more than five years of experience in software testing.
This definition-guided and multi-stage review process yields a six-
category failure taxonomy, including structural constraints, domain-
specific constraints, numeric constraints, exception-handling code,
imprecise call-chain recovery, and others.
Table 6 summarizes the overall distribution of failure causes.
Domain-specific Constraints constitute the largest category (35.23%),
followed by Exception-handling (23.11%), Structural Constraints
(21.21%), and Numeric Constraints (18.56%). Call-chain Recovery con-
tributes 10.61%. These results indicate that the major challenge of
repository-level directed input generation lies not in producing su-
perficially plausible inputs, but in satisfying interacting repository-
specific semantic requirements and execution conditions. In par-
ticular, many failures arise because the generated input cannot si-
multaneously satisfy project-specific rules, trigger non-mainstream
execution paths, or meet precise numeric and structural conditions.
We next use two case studies to illustrate these failure modes.
5.4.2
Case Study I. Listing 2 presents a representative failure in the
Domain-specific Constraints category. The target is reachable only
3069

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
Input
Target Line
Fuzz Driver
Repo
Fault Injection Agent
Fault
Injection
Fault 
Injection
Analysis
Intention Analysis Agent
Intention
Analysis
Constraint
Extraction
Call Chain 
Analysis
Intention Report
Generate & Verification Agent
Input
Generation
Input
Refinement
Execution &
Verification
Coverage Report
Refinement Agent
Deviation 
Diagnosis
Coverage 
Analysis
Output
Output
Target Miss
Target Hit/
≥Max Iter
End
Feedback
Feedback
Figure 3: Overview of AgenticDIG
when the input satisfies a sequence of repository-specific packet-
format constraints. Concretely, the packet must be parsed as a
Kerberos-related message, follow BER-encoded ASN.1 formatting,
be wrapped as a valid KRB_GSSAPI_Token, contain the required
mechanism identifier and nested innerToken, and finally expose
one of the byte prefixes checked by the target branch. Thus, target
reachability depends on satisfying a highly specialized protocol
format rather than a simple local predicate.
Notably, the model is able to identify the relevant function con-
text behind this target, including the ASN.1 parser, the GSSAPI
token wrapper, and the nested innerToken structure. However,
such understanding remains coarse-grained. Although the model
can infer the general direction of the constraint, it fails to synthe-
size a concrete binary message that satisfies all protocol-specific
requirements simultaneously. This case shows that LLMs may rec-
ognize domain-specific constraints at a high level, yet still lack the
understanding needed to solve them precisely in repo-level DIG.
5.4.3
Case Study II. Listing 3 presents a representative Exception-
handling failure. The target, throw new EOFException("End of
data reached."), lies in the catch block (line 8). Although the
model is able to generate an input that reaches the try block and
exercises the normal data-reading logic, reaching the target re-
quires the execution to raise an OutOfMemoryError, for example,
during byte-array allocation. This condition depends on resource
exhaustion rather than input semantics alone.
Similar targets require external conditions such as memory ex-
haustion, network disconnection, file I/O failures, or unavailable
resources. Therefore, repository-level DIG must reason about and,
when possible, induce execution-environment failures. Simply in-
creasing the number of input-generation attempts is insufficient
for such environment-dependent targets.
Finding 6. The main failures in repository-level DIG arise from
hard-to-satisfy constraints and external execution conditions. In
particular, domain-specific, exception-handling, numeric, and
structural requirements play a major role in determining whether
target coverage can be achieved.
6
A New Agentic Framework
Based on the findings above, we develop an agentic workflow, called
AgenticDIG, for repository-level directed input generation.
6.1
AgenticDIG Workflow
Figure 3 illustrates the workflow of AgenticDIG, which is designed
with four major agents: a Fault Injection Agent, an Intention Analysis
Agent, a Generate & Verification Agent, and a Refinement Agent.
Guided by Finding 6, the workflow begins with the Fault Injec-
tion Agent. This agent examines the code surrounding the target
line to determine whether the target depends on such externally
induced exceptional scenarios. Fault injection is performed only for
these cases, including file I/O failures, system resource exhaustion,
and network disconnection. When needed, the agent constructs
source-code-level mock modules to emulate the corresponding fail-
ures and make the target-reaching path executable during testing.
The workflow then proceeds to the Intention Analysis Agent, which
serves as the main semantic analysis component based on Finding
3,6. This agent performs three closely related tasks: call-chain anal-
ysis, constraint extraction, and optional intention analysis. Starting
from the repository, fuzz driver, and target line, it first recovers the
target-relevant inter-procedural call chain by invoking static anal-
ysis tools and identifies the key constraints that govern whether
execution can reach the target. When constraints cannot be inferred
directly from local code context, such as when the agent identifies
factual errors in its previous constraint understanding or when a
generated input fails to resolve certain constraints as expected, it
further performs intention analysis to derive the semantic mean-
ing of these conditions and how they relate to the required input
properties based on Finding 6. The resulting analysis is organized
into an intention report, which summarizes the function, identified
constraints, their underlying intentions, and implications for test
input generation, and is stored as external knowledge for reuse in
later refinement rounds.
Guided by the extracted call-chain structure, target-relevant con-
straints, and the intention report, the Generate & Verification Agent
synthesizes a candidate input generator and executes the produced
input against the target program. Following Finding 2, this agent
generates inputs in the form of Python-based input generators
rather than directly serialized outputs. It further performs dynamic
execution and verification to determine whether the generated in-
put reaches the target line. The execution outcome is summarized
as a coverage report, which is also stored as external knowledge.
If the generated input fails to cover the target, the workflow en-
ters the Refinement Agent. Using the coverage report, this agent per-
forms coverage analysis and deviation diagnosis to identify why exe-
cution misses the target. It then produces feedback describing miss-
ing constraints, unsatisfied conditions, or incorrect path choices.
3070

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
Table 7: Overall performance of AgenticDIG
Lang.
Project
AgenticDIG
OpenCode Call Chain Agent
File-level
Pass@3𝑓𝑏Pass@3 Pass@3𝑓𝑏
Pass@3
Pass@3
Pass@3
C/C++
cpp-httplib
35.00
30.00
25.00
22.50
20.00
27.50
exiv2
52.50
37.50
47.50
30.00
20.00
42.50
jansson
37.50
25.00
30.00
22.50
15.00
17.50
sqlite3
85.71
61.90
38.10
76.19
35.71
45.24
Java
A.H.C
21.43
9.52
4.76
9.52
14.29
26.19
jedis
74.19
70.97
22.58
70.97
16.13
16.13
jsoup
38.09
35.71
19.05
11.90
11.90
16.67
M.E.
72.97
54.05
48.65
27.03
13.51
27.03
Python
mutagen
85.71
76.19
80.95
47.63
38.10
28.60
pycparser
92.31
92.31
76.92
42.32
3.80
0.00
scapy
86.67
76.67
56.67
40.00
26.70
6.70
sqlparse
83.87
80.65
83.30
76.67
53.30
66.67
Average
63.83
54.21
44.46
39.77
22.37
26.73
Table 8: Performance comparison of AgenticDIG and Open-
Code under different call depths and target difficulties
Category
Total
AgenticDIG
OpenCode
Pass@1
Pass@3𝑓𝑏
Pass@1
Pass@3𝑓𝑏
Call depth
1-2
71
35↑29.63%
48↑33.33%
27
36
3-5
174
78↑41.82%
103↑41.10%
55
73
6-8
115
51↑27.50%
66↑32.00%
40
50
9+
62
27↑125.0%
38↑171.4%
12
14
Difficulty
Medium
199
95↑37.68%
125↑35.87%
69
92
High
74
46↑39.39%
59↑47.50%
33
40
Exceptional
149
50↑56.25%
71↑73.17%
32
41
This feedback is sent back to the Intention Analysis Agent for the
next iteration. The workflow repeats this analysis–generation–
verification loop until the target is covered or the maximum it-
eration budget is reached.
6.2
Evaluation
As for baselines, we include the three LLM-based context settings
evaluated in RQ1–RQ2, i.e., file-level context, call-chain context, and
agent context. In addition, we introduce a stronger agent-based
baseline by directly using OpenCode [32] to handle the DIG task
through prompt-based end-to-end directed input generation. We
use DeepSeek-V3.2 as the backbone model for practical reasons, since
evaluating the full workflow incurs additional time and budget
costs. Our method targets the general challenges of repository-
level directed input generation, and DeepSeek-V3.2 serves here as a
representative backbone for controlled evaluation. We implement
the prototype system based on OpenCode and customized skills.
We use the same target-line coverage oracle as in the empiri-
cal study, but distinguish independent repeated generation from
feedback-guided agentic refinement. In the empirical study, Pass@3
refers to three independent queries, each producing one input, and
a target is considered covered if any of the three inputs reaches the
target line. For AgenticDIG and OpenCode, which both support
iterative refinement, we instead use Pass@3𝑓𝑏, where the super-
script denotes feedback-guided generation. Specifically, Pass@3𝑓𝑏
measures whether the target can be covered within at most three
generated inputs in an analysis-and-refinement process. For a fairer
comparison, we also report Pass@3 for AgenticDIG, where Agen-
ticDIG is run three times from scratch, each run generates one
input, and no refinement feedback is reused across runs.
Table 7 reports the performance of AgenticDIG and all base-
lines under their corresponding evaluation settings. Overall, Agen-
ticDIG achieves the best average result under Pass@3𝑓𝑏, reaching
63.83%, which represents a 43.56% relative improvement over Open-
Code under the same iterative setting (43.56% = (63.83-44.46)/44.46).
Moreover, the independent-run Pass@3 of AgenticDIG reaches
54.21%, which is also higher than OpenCode’s Pass@3𝑓𝑏result.
Additionally, we compute the p-value (0.001253), which further con-
firms that the improvement is statistically significant. At the project
level, AgenticDIG achieves the best result on 11 out of 12 reposi-
tories. The only exception is async-http-client, where AgenticDIG
reaches 21.43%, slightly below file-level context (26.19%). A possible
reason is that some AHC targets rely more on localized constraints
within the target file, while the additional analysis and refinement
steps in AgenticDIG may introduce extra noise rather than useful
guidance in such cases. We further compare the inference cost with
OpenCode to rule out the possibility that the improvement is due
to a larger inference budget. AgenticDIG costs $0.14 and 3.06M
tokens per target, compared with $0.22 and 3.38M for OpenCode.
6.3
Effectiveness across Target Characteristics
To examine whether AgenticDIG’s improvement generalizes across
target types, we further break down its performance by call-chain
depth and fuzzing-based difficulty in Table 8. AgenticDIG out-
performs OpenCode across all groups under both Pass@1 and
Pass@3𝑓𝑏. For call-chain depth, AgenticDIG improves Pass@3𝑓𝑏
by 33.33%, 41.10%, 32.00%, and 171.43% on depth ranges 1–2, 3–5,
6–8, and 9+, respectively. For difficulty, the improvements increase
from 35.87% on medium targets to 47.50% on high targets and 73.17%
on exceptional targets. These results indicate that AgenticDIG is
not only effective on average, but also provides stronger benefits
for deeper and harder targets.
6.4
Component Analysis
To quantify the contribution of each key component, we conduct an
ablation study by disabling one component at a time while keeping
the remaining workflow and generation budget unchanged. We
evaluate three variants: w/o Intention Analysis, where semantic
summaries of target constraints are not stored or reused; w/o Fault
Injection, where source-level mocks for external exceptional con-
ditions are disabled; and w/o Refinement Agent, where coverage
feedback is not used for iterative diagnosis. We report Pass@1 and
Pass@3𝑓𝑏, measuring the number of targets covered within one
generated input and within at most three feedback-guided inputs.
As shown in Table 9, all three components contribute to Agen-
ticDIG’s effectiveness. Removing Intention Analysis reduces Pass@1
and Pass@3𝑓𝑏from 191/255 to 143/196, showing the benefit of
reusable semantic constraint summaries. Removing Fault Injection
causes the largest drop, confirming its role in handling externally
guarded targets. Removing the Refinement Agent reduces perfor-
mance to 146/212, indicating the importance of feedback-driven
diagnosis. Overall, AgenticDIG’s gains come from the combination
of intention analysis, fault injection, and refinement.
3071

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
Table 9: Component contribution
Method
Performance
Pass@1
Pass@3𝑓𝑏
Full AgenticDIG
191
255
w/o-intention
143↓25.13%
196↓23.14%
w/o-fault injection
123↓35.60%
187↓26.67%
w/o-refinement*
146↓23.56%
212↓16.86%
* The Pass@3𝑓𝑏of w/o-refinement corresponds to Pass@3 without feedback,
following the same definition of Pass@3 in Table 7.
6.5
A Case Study
We use a SQLite target to illustrate how intention analysis helps
AgenticDIG refine input generation. The target is a boundary test-
case testcase(pIn1->u.i==-140737488355329LL). In the first
attempt, AgenticDIG generated a simple input that created a REAL
column and inserted the required boundary integer. Although it
captured the target value, it missed a key path constraint: SQLite
must actually generate and execute the OP_Affinity opcode so
that REAL affinity is applied to an integer register.
To diagnose this failure, the Intention Analysis Agent analyzed
the target condition and surrounding affinity-conversion logic. As
shown in Figure 4, the resulting intention report revealed that
the path is intended to test SQLite’s boundary handling when ap-
plying REAL affinity to an integer just below the 6-byte range,
which should force conversion from an integer representation to
a real value. It further translated this path intention into concrete
SQL-level guidance: use a REAL-typed column and trigger affin-
ity application through index operations, INSERT ... SELECT, or
typed-column comparison.
[Basic Information]
The following is the information of target location:
- File: /src/sqlite3/bld/sqlite3.c
- Line: 98583
- Code: testcase( pIn1->u.i==-140737488355329LL );
……
[Function / Constraint Intention]
OP_Affinity converts an integer to MEM_Real when it exceeds the 
6-byte range. The target checks the lower bound -140737488355329.
……
[Input Implication]
Requires: a REAL column with an index, INSERT ... SELECT of the 
boundary value, and a comparison to trigger OP_Affinity.
Intention Report
Figure 4: Brief intention report
Guided by this report, AgenticDIG generated an execution-path-
aware SQL sequence and successfully covered the target. This case
shows that intention analysis can identify a missed path-level se-
mantic constraint and convert it into actionable input-generation
guidance. By contrast, the baseline methods, including OpenCode
with automatic feedback iterations, failed to identify this key con-
straint OP_Affinity and thus could not reach the target line.
7
Threats to Validity
Internal: a) Data leakage. A potential threat is overlap between
benchmark repositories and LLM pretraining data. We mitigate this
risk by selecting diverse, actively maintained repositories across lan-
guages and domains. Moreover, repository-level DIG requires rea-
soning about project-specific semantics, call chains, and execution
conditions, making it unlikely that memorization alone explains
the results. b) Generalizability. Our study focuses on open-source
repositories in C/C++, Java, and Python. Although this improves di-
versity, the results may not fully generalize to industrial codebases,
additional languages, or tasks beyond repository-level DIG.
External: a) Testing setup. Our method is evaluated under a
fuzz-driver-based workflow, where each task is defined by a test
entry point, external input generation, and target-line coverage.
Nevertheless, the core challenges addressed by AgenticDIG, in-
cluding cross-function input propagation, constraint extraction,
path-deviation diagnosis, and feedback-driven refinement, are not
inherently tied to a specific fuzz driver. b) Efficiency. Compared
with direct prompting, AgenticDIG incurs additional time and
inference costs due to iterative analysis, generation, execution, and
refinement. Improving efficiency while preserving effectiveness
remains an important direction for future work.
8
Related Work
LLM-enhanced Directed Fuzzing: More recent studies [4, 8, 47, 48,
50, 53] incorporate LLMs to provide stronger semantic reasoning
and code-generation capabilities. HGFuzzer [47] leverages LLMs to
generate target harnesses, reachable seeds, and target-specific muta-
tors based on path-constraint and call-chain analysis. Locus [53] in-
troduces an agentic design that synthesizes intermediate predicates
to guide fuzzing toward local target-relevant states. PBFuzz [50]
further uses interacting LLM agents to extract constraints, generate
input generators, and iteratively refine PoV inputs with execution
feedback. Unlike prior work on LLM-enhanced directed fuzzing, we
systematically study repository-level DIG through a benchmark,
an empirical analysis, and an agentic workflow.
Targeted Test Generation: Recent work has explored targeted
test generation using both static analysis and LLMs. UnitCon [14]
uses static-analysis-guided synthesis to generate tests for target
exceptions, SymPrompt [34] combines static analysis with LLM
prompting to reach uncovered paths, and CoverUp [2] studies it-
erative coverage-guided test generation with execution feedback.
These studies focus on method-level or regression-style settings,
whereas our work targets repository-level DIG with cross-function
dependencies, complex semantics, and external runtime conditions.
9
Conclusion
We present the first systematic study of LLM-based repository-level
DIG and construct RepoEval with 422 hard-to-cover targets. Our
results show that effectiveness strongly depends on output format,
context construction, repository-specific semantics, and external
conditions. Based on these findings, AgenticDIG combines seman-
tic analysis, fault injection, and iterative refinement to substantially
improve target coverage. Our benchmark and findings provide a
foundation for future repository-level DIG research.
3072

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

ASE ’26, October 12–16, 2026, Munich, Germany
Haoyu Wang, Ming Wen, Haoran Yan, Jiayi Huang, Xuanhua Shi, and Hai Jin
Acknowledgments
We would like to thank the anonymous reviewers for their insightful
comments. This work was partially supported by the National Nat-
ural Science Foundation of China (No. U2436207 and No. 62372193),
the Major Program (JD) of Hubei Province (No. 2023BAA024), and
the Major Technological Innovation Program of Huazhong Univer-
sity of Science and Technology (No. 2025ZDKJCX05).
Data Availability Statement
All artifacts of this work, including the benchmark dataset, prompt
templates, experimental scripts, and tool implementation, are avail-
able at: https://doi.org/10.5281/zenodo.19347551.
References
[1] Alibaba Cloud Model Studio. 2025. Qwen3-Coder-Flash Model Information.
Retrieved July 31, 2026 from https://help.aliyun.com/en/model-studio/qwen3-
coder-flash
[2] Juan Altmayer Pizzorno and Emery D. Berger. 2025. CoverUp: Effective High
Coverage Test Generation for Python. Proc. ACM Softw. Eng. 2, FSE, Article
FSE128 (June 2025), 23 pages. doi:10.1145/3729398
[3] Anthropic. 2025. Claude 3.7 Sonnet and Claude Code. Retrieved March 18, 2026
from https://www.anthropic.com/news/claude-3-7-sonnet
[4] Asmita, Yaroslav Oliinyk, Michael Scott, Ryan Tsang, Chongzhou Fang, and
Houman Homayoun. 2024.
Fuzzing BusyBox: Leveraging LLM and Crash
Reuse for Embedded Bug Unearthing. In Proceedings of the 33rd USENIX Se-
curity Symposium, USENIX Security, Philadelphia, PA, USA, August 14-16, 2024,
Davide Balzarotti and Wenyuan Xu (Eds.). USENIX Association, 883–900. https:
//www.usenix.org/conference/usenixsecurity24/presentation/asmita
[5] Andrew Bao, Wenjia Zhao, Yanhao Wang, Yueqiang Cheng, Stephen McCamant,
and Pen-Chung Yew. 2025. From Alarms to Real Bugs: Multi-target Multi-step
Directed Greybox Fuzzing for Static Analysis Result Verification. In Proceedings of
the 34th USENIX Security Symposium, USENIX Security, Seattle, WA, USA, August
13-15, 2025, Lujo Bauer and Giancarlo Pellegrino (Eds.). USENIX Association,
6977–6997. https://www.usenix.org/conference/usenixsecurity25/presentation/
bao-andrew
[6] Jiawei Chen, Hongyu Lin, Xianpei Han, and Le Sun. 2024. Benchmarking Large
Language Models in Retrieval-Augmented Generation. In Proceedings of the
Thirty-Eighth AAAI Conference on Artificial Intelligence, AAAI, Thirty-Sixth Con-
ference on Innovative Applications of Artificial Intelligence, IAAI, Fourteenth Sym-
posium on Educational Advances in Artificial Intelligence, EAAI, February 20-27,
2024, Vancouver, Canada, Michael J. Wooldridge, Jennifer G. Dy, and Sriraam
Natarajan (Eds.). AAAI Press, 17754–17762. doi:10.1609/AAAI.V38I16.29728
[7] DeepSeek. 2025. DeepSeek-V3.2. Retrieved March 18, 2026 from https://chat.
deepseek.com/
[8] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming
Zhang. 2023. Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-
Learning Libraries via Large Language Models. In Proceedings of the 32nd ACM
SIGSOFT International Symposium on Software Testing and Analysis, ISSTA, Seattle,
WA, USA, July 17-21, 2023. ACM, 423–435. doi:10.1145/3597926.3598067
[9] Gregory Gay. 2023. Improving the Readability of Generated Tests Using GPT-4
and ChatGPT Code Interpreter. In Proceedings of the 15th International Symposium
on Search-Based Software Engineering, SSBSE, San Francisco, CA, USA, December
8, 2023, Proceedings (Lecture Notes in Computer Science, Vol. 14415), Paolo Arcaini,
Tao Yue, and Erik M. Fredericks (Eds.). Springer, 140–146. doi:10.1007/978-3-031-
48796-5_11
[10] GitHub. 2026. CodeQL. Retrieved March 18, 2026 from https://codeql.github.com/
[11] Google Open Source Security Team. 2026. OSS-Fuzz. Retrieved March 18, 2026
from https://google.github.io/oss-fuzz/
[12] Ahmad Hazimeh, Adrian Herrera, and Mathias Payer. 2020. Magma: A Ground-
Truth Fuzzing Benchmark. Proc. ACM Meas. Anal. Comput. Syst. 4, 3, Article 49
(Dec. 2020), 29 pages. doi:10.1145/3428334
[13] Wenhao Hu, Jinhao Duan, Chunchen Wei, Li Zhang, Yue Zhang, and Kaidi Xu.
2025. DynaCode: A Dynamic Complexity-Aware Code Benchmark for Evaluating
Large Language Models in Code Generation. In Proceedings of the Findings of the
Association for Computational Linguistics, ACL, Vienna, Austria, July 27 - August 1,
2025 (Findings of ACL, Vol. ACL 2025), Wanxiang Che, Joyce Nabende, Ekaterina
Shutova, and Mohammad Taher Pilehvar (Eds.). Association for Computational
Linguistics, 21980–21997. doi:10.18653/V1/2025.FINDINGS-ACL.1133
[14] Sujin Jang, Yeonhee Ryou, Heewon Lee, and Kihong Heo. 2025. UnitCon: Synthe-
sizing Targeted Unit Tests for Java Runtime Exceptions. Proc. ACM Softw. Eng. 2,
FSE (2025), 2053–2074. doi:10.1145/3729362
[15] Bokdeuk Jeong, Joonun Jang, Hayoon Yi, Jiin Moon, Junsik Kim, Intae Jeon,
Taesoo Kim, WooChul Shim, and Yong Ho Hwang. 2023. UTopia: Automatic
Generation of Fuzz Driver using Unit Tests. In Proceedings of the 44th IEEE
Symposium on Security and Privacy, SP, San Francisco, CA, USA, May 21-25, 2023.
IEEE, 2676–2692. doi:10.1109/SP46215.2023.10179394
[16] Zongze Jiang, Ming Wen, Jialun Cao, Xuanhua Shi, and Hai Jin. 2024. Towards
Understanding the Effectiveness of Large Language Models on Directed Test
Input Generation. In Proceedings of the 39th IEEE/ACM International Conference
on Automated Software Engineering, ASE, Sacramento, CA, USA, 2024. Association
for Computing Machinery, New York, NY, USA, 1408–1420. doi:10.1145/3691620.
3695513
[17] Zongze Jiang, Ming Wen, Ge Wen, and Hai Jin. 2025. Fact-Aligned and Template-
Constrained Static Analyzer Rule Enhancement with LLMs. In Proceedings of the
40th IEEE/ACM International Conference on Automated Software Engineering, ASE,
Seoul, Korea, Republic of, November 16-20, 2025. IEEE, 1642–1654. doi:10.1109/
ASE63991.2025.00138
[18] Taesoo Kim, HyungSeok Han, Soyeon Park, Dae R. Jeong, Dohyeok Kim, Dongk-
wan Kim, Eunsoo Kim, Jiho Kim, Joshua Wang, Kangsu Kim, Sangwoo Ji, Woosun
Song, Hanqing Zhao, Andrew Chin, Gyejin Lee, Kevin Stevens, Mansour Alharthi,
Yizhuo Zhai, Cen Zhang, Joonun Jang, Yeongjin Jang, Ammar Askar, Dongju Kim,
Fabian Fleischer, Jeongin Cho, Junsik Kim, Kyungjoon Ko, Insu Yun, Sangdon
Park, Dowoo Baik, Haein Lee, Hyeon Heo, Minjae Gwon, Minjae Lee, Minwoo
Baek, Seunggi Min, Wonyoung Kim, Yonghwi Jin, Younggi Park, Yunjae Choi,
Jinho Jung, Gwanhyun Lee, Junyoung Jang, Kyuheon Kim, Yeonghyeon Cha,
and Youngjoon Kim. 2025. ATLANTIS: AI-driven Threat Localization, Analysis,
and Triage Intelligence System. CoRR abs/2509.14589 (2025). arXiv:2509.14589
doi:10.48550/ARXIV.2509.14589
[19] Gwangmu Lee, Woochul Shim, and Byoungyoung Lee. 2021. Constraint-guided
Directed Greybox Fuzzing. In Proceedings of the 30th USENIX Security Symposium,
USENIX Security, August 11-13, 2021, Michael D. Bailey and Rachel Greenstadt
(Eds.). USENIX Association, 3559–3576. https://www.usenix.org/conference/
usenixsecurity21/presentation/lee-gwangmu
[20] Penghui Li, Wei Meng, and Chao Zhang. 2024. SDFuzz: Target States Driven Di-
rected Fuzzing. In Proceedings of the 33rd USENIX Security Symposium, USENIX Se-
curity, Philadelphia, PA, USA, August 14-16, 2024, Davide Balzarotti and Wenyuan
Xu (Eds.). USENIX Association, 2441–2457. https://www.usenix.org/conference/
usenixsecurity24/presentation/li-penghui
[21] Wei Li, Xin Zhang, Zhongxin Guo, Shaoguang Mao, Wen Luo, Guangyue Peng,
Yangyu Huang, Houfeng Wang, and Scarlett Li. 2025. FEA-Bench: A Benchmark
for Evaluating Repository-Level Code Generation for Feature Implementation.
In Proceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), ACL, Vienna, Austria, July 27 - August 1,
2025, Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher
Pilehvar (Eds.). Association for Computational Linguistics, 17160–17176. doi:10.
18653/V1/2025.ACL-LONG.839
[22] Yuwei Li, Shouling Ji, Yuan Chen, Sizhuang Liang, Wei-Han Lee, Yueyao Chen,
Chenyang Lyu, Chunming Wu, Raheem Beyah, Peng Cheng, Kangjie Lu, and
Ting Wang. 2021. UNIFUZZ: A Holistic and Pragmatic Metrics-Driven Platform
for Evaluating Fuzzers. In Proceedings of the 30th USENIX Security Symposium,
USENIX Security, August 11-13, 2021, Michael D. Bailey and Rachel Greenstadt
(Eds.). USENIX Association, 2777–2794. https://www.usenix.org/conference/
usenixsecurity21/presentation/li-yuwei
[23] Stephan Lipp, Daniel Elsner, Severin Kacianka, Alexander Pretschner, Marcel
Böhme, and Sebastian Banescu. 2023. Green Fuzzing: A Saturation-Based Stop-
ping Criterion using Vulnerability Prediction. In Proceedings of the 32nd ACM
SIGSOFT International Symposium on Software Testing and Analysis, ISSTA, Seat-
tle, WA, USA, 2023. Association for Computing Machinery, New York, NY, USA,
127–139. doi:10.1145/3597926.3598043
[24] Danushka Liyanage, Marcel Böhme, Chakkrit Tantithamthavorn, and Stephan
Lipp. 2023. Reachable Coverage: Estimating Saturation in Fuzzing. In Proceedings
of the 45th IEEE/ACM International Conference on Software Engineering, ICSE,
Melbourne, Australia, May 14-20, 2023. IEEE, 371–383. doi:10.1109/ICSE48619.
2023.00042
[25] LLVM Project. 2025. libFuzzer – a library for coverage-guided fuzz testing.
Retrieved March 18, 2026 from https://llvm.org/docs/LibFuzzer.html
[26] Kin-Keung Ma, Yit Phang Khoo, Jeffrey S. Foster, and Michael Hicks. 2011. Di-
rected Symbolic Execution. In Proceedings of the 18th International Symposium
on Static Analysis, SAS, Venice, Italy, September 14-16, 2011. Proceedings (Lecture
Notes in Computer Science, Vol. 6887). Springer, 95–111. doi:10.1007/978-3-642-
23702-7_11
[27] Jonathan Metzman, László Szekeres, Laurent Simon, Read Sprabery, and Abhishek
Arya. 2021. FuzzBench: an open fuzzer benchmarking platform and service. In
Proceedings of the 29th ACM Joint Meeting on European Software Engineering
Conference and Symposium on the Foundations of Software Engineering, ESEC/FSE,
Athens, Greece, 2021. Association for Computing Machinery, New York, NY, USA,
1393–1403. doi:10.1145/3468264.3473932
[28] Samit Shahnawaz Miftah, Amisha Srivastava, Hyunmin Kim, Shiyi Wei, and
Kanad Basu. 2025. SymbFuzz: Symbolic Execution Guided Hardware Fuzzing. In
Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture,
3073

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation
ASE ’26, October 12–16, 2026, Munich, Germany
MICRO, Seoul, Republic of Korea, October 18-22, 2025. ACM, 1477–1490. doi:10.
1145/3725843.3756131
[29] Aniruddhan Murali, Noble Saji Mathews, Mahmoud Alfadel, Meiyappan Nagap-
pan, and Meng Xu. 2024. FuzzSlice: Pruning False Positives in Static Analysis
Warnings through Function-Level Fuzzing. In Proceedings of the 46th IEEE/ACM
International Conference on Software Engineering, ICSE, Lisbon, Portugal, April
14-20, 2024. ACM, 65:1–65:13. doi:10.1145/3597503.3623321
[30] Manh-Dung Nguyen, Sébastien Bardin, Richard Bonichon, Roland Groz, and
Matthieu Lemerre. 2020. Binary-level Directed Fuzzing for Use-After-Free Vulner-
abilities. In Proceedings of the 23rd International Symposium on Research in Attacks,
Intrusions and Defenses, RAID, San Sebastian, Spain, October 14-15, 2020. USENIX
Association, 47–62. https://www.usenix.org/conference/raid2020/presentation/
nguyen
[31] OpenAI. 2025. GPT-5 mini. Retrieved March 18, 2026 from https://developers.
openai.com/api/docs/models/gpt-5-mini
[32] OpenCode. 2026. OpenCode: The Open Source AI Coding Agent. Retrieved
March 18, 2026 from https://opencode.ai/
[33] Suzette Person, Guowei Yang, Neha Rungta, and Sarfraz Khurshid. 2011. Directed
incremental symbolic execution. In Proceedings of the 32nd ACM SIGPLAN Con-
ference on Programming Language Design and Implementation, PLDI, San Jose,
California, USA, 2011. Association for Computing Machinery, New York, NY, USA,
504–515. doi:10.1145/1993498.1993558
[34] Gabriel Ryan, Siddhartha Jain, Mingyue Shang, Shiqi Wang, Xiaofei Ma, Mu-
rali Krishna Ramanathan, and Baishakhi Ray. 2024. Code-Aware Prompting: A
Study of Coverage-Guided Test Generation in Regression Setting using LLM.
Proc. ACM Softw. Eng. 1, FSE, Article 43 (July 2024), 21 pages. doi:10.1145/3643769
[35] Md Shafiuzzaman, Achintya Desai, Laboni Sarker, and Tevfik Bultan. 2024. STASE:
Static Analysis Guided Symbolic Execution for UEFI Vulnerability Signature
Generation. In Proceedings of the 39th IEEE/ACM International Conference on Au-
tomated Software Engineering, ASE, Sacramento, CA, USA, October 27 - November 1,
2024, Vladimir Filkov, Baishakhi Ray, and Minghui Zhou (Eds.). ACM, 1783–1794.
doi:10.1145/3691620.3695543
[36] Fan Shu, Yite Wang, Ruofan Wu, Boyi Liu, Zhewei Yao, Yuxiong He, and Feng
Yan. 2026. DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in
Data Science. CoRR abs/2602.24288 (2026). arXiv:2602.24288 doi:10.48550/ARXIV.
2602.24288
[37] Mozhan Soltani, Annibale Panichella, and Arie van Deursen. 2020. Search-Based
Crash Reproduction and Its Impact on Debugging. IEEE Trans. Software Eng. 46,
12 (2020), 1294–1317. doi:10.1109/TSE.2018.2877664
[38] Soot OSS Project. 2026. Soot: A Framework for Analyzing and Transforming
Java and Android Applications.
Retrieved March 18, 2026 from https://soot-
oss.github.io/soot/
[39] SQLite Project. 2026. SQLite Home Page.
Retrieved March 18, 2026 from
https://sqlite.org/
[40] Vitalis Salis and contributors. 2026. PyCG: Practical Python Call Graphs. Re-
trieved March 18, 2026 from https://github.com/vitsalis/PyCG
[41] Wenhan Wang, Chenyuan Yang, Zhijie Wang, Yuheng Huang, Zhaoyang Chu,
Da Song, Lingming Zhang, An Ran Chen, and Lei Ma. 2025. TESTEVAL: Bench-
marking Large Language Models for Test Case Generation. In Proceedings of the
Findings of the Association for Computational Linguistics: NAACL, Albuquerque,
New Mexico, USA, April 29 - May 4, 2025. Association for Computational Linguis-
tics, 3547–3562. doi:10.18653/V1/2025.FINDINGS-NAACL.197
[42] Zichao Wei, Jun Zeng, Ming Wen, Zeliang Yu, Kai Cheng, Yiding Zhu, Jingyi Guo,
Shiqi Zhou, Le Yin, Xiaodong Su, and Zhechao Ma. 2025. PATCHEVAL: A New
Benchmark for Evaluating LLMs on Patching Real-World Vulnerabilities. CoRR
abs/2511.11019 (2025). arXiv:2511.11019 doi:10.48550/ARXIV.2511.11019
[43] Yulun Wu, Ming Wen, Zeliang Yu, Xiaochen Guo, and Hai Jin. 2024. Effective
Vulnerable Function Identification based on CVE Description Empowered by
Large Language Models. In Proceedings of the 39th IEEE/ACM International Con-
ference on Automated Software Engineering, ASE, Sacramento, CA, USA, October
27 - November 1, 2024. ACM, 393–405. doi:10.1145/3691620.3695013
[44] xAI. 2025. Grok Code Fast 1. Retrieved March 18, 2026 from https://docs.x.ai/
docs/models/grok-code-fast-1
[45] Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian, Michael Pradel, and Lingming
Zhang. 2024. Fuzz4All: Universal Fuzzing with Large Language Models. In
Proceedings of the 46th IEEE/ACM International Conference on Software Engineering,
ICSE, Lisbon, Portugal, April 14-20, 2024. ACM, 126:1–126:13. doi:10.1145/3597503.
3639121
[46] Yi Xiang, Xuhong Zhang, Peiyu Liu, Shouling Ji, Xiao Xiao, Hong Liang, Jiacheng
Xu, and Wenhai Wang. 2024. Critical Code Guided Directed Greybox Fuzzing for
Commits. In Proceedings of the 33rd USENIX Security Symposium, USENIX Security,
Philadelphia, PA, USA, August 14-16, 2024, Davide Balzarotti and Wenyuan Xu
(Eds.). USENIX Association, 2459–2474. https://www.usenix.org/conference/
usenixsecurity24/presentation/xiang-yi
[47] Hanxiang Xu, Yanjie Zhao, and Haoyu Wang. 2025. Directed Greybox Fuzzing
via Large Language Model. CoRR abs/2505.03425 (2025). arXiv:2505.03425 doi:10.
48550/ARXIV.2505.03425
[48] Chenyuan Yang, Yinlin Deng, Runyu Lu, Jiayi Yao, Jiawei Liu, Reyhaneh Jab-
barvand, and Lingming Zhang. 2024. WhiteFox: White-Box Compiler Fuzzing
Empowered by Large Language Models. Proc. ACM Program. Lang. 8, OOPSLA2,
Article 296 (Oct. 2024), 27 pages. doi:10.1145/3689736
[49] Zhengmin Yu, Yuan Zhang, Ming Wen, Yinan Nie, Wenhui Zhang, and Min Yang.
2025. CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source
Software Building. Proc. ACM Softw. Eng. 2, FSE (2025), 2618–2640. doi:10.1145/
3729386
[50] Haochen Zeng, Andrew Bao, Jiajun Cheng, and Chengyu Song. 2025. PBFuzz:
Agentic Directed Fuzzing for PoV Generation.
CoRR abs/2512.04611 (2025).
arXiv:2512.04611 doi:10.48550/ARXIV.2512.04611
[51] Kunpeng Zhang, Zongjie Li, Daoyuan Wu, Shuai Wang, and Xin Xia. 2025. Low-
Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input
Generators. In Proceedings of the 34th USENIX Security Symposium, USENIX
Security, Seattle, WA, USA, August 13-15, 2025, Lujo Bauer and Giancarlo Pellegrino
(Eds.). USENIX Association, 6999–7018. https://www.usenix.org/conference/
usenixsecurity25/presentation/zhang-kunpeng
[52] Zenong Zhang, Zach Patterson, Michael Hicks, and Shiyi Wei. 2022. FIXRE-
VERTER: A Realistic Bug Injection Methodology for Benchmarking Fuzz Testing.
In Proceedings of the 31st USENIX Security Symposium, USENIX Security, Boston,
MA, USA, August 10-12, 2022, Kevin R. B. Butler and Kurt Thomas (Eds.). USENIX
Association, 3699–3715. https://www.usenix.org/conference/usenixsecurity22/
presentation/zhang-zenong
[53] Jie Zhu, Chihao Shen, Ziyang Li, Jiahao Yu, Yizheng Chen, and Kexin Pei. 2025.
Locus: Agentic Predicate Synthesis for Directed Fuzzing. CoRR abs/2508.21302
(2025). arXiv:2508.21302 doi:10.48550/ARXIV.2508.21302
[54] Xiaogang Zhu and Marcel Böhme. 2021. Regression Greybox Fuzzing. In Pro-
ceedings of the 2021 ACM SIGSAC Conference on Computer and Communications
Security, CCS, Virtual Event, Republic of Korea, 2021. Association for Computing
Machinery, New York, NY, USA, 2169–2182. doi:10.1145/3460120.3484596
Received 2026-03-26; accepted 2026-06-18
3074

[Vista original de la página 13](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-13.png)

![Página PDF 13, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/secondary/From%20Function%20to%20Repository/page-13.png)
