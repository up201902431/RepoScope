# CoderEval

- source_pdf: ../../../../../pdf/Evaluation/primary/CoderEval.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

CoderEval: A Benchmark of Pragmatic Code Generation with
Generative Pre-trained Models
Hao Yu
School of Software and
Microelectronics, Peking University
China
yh0315@pku.edu.cn
Bo Shen
Huawei Cloud Computing
Technologies Co., Ltd.
China
shenbo21@huawei.com
Dezhi Ran
Key Lab of HCST (PKU), MOE; SCS
Peking University
China
dezhiran@pku.edu.cn
Jiaxin Zhang
Huawei Cloud Computing
Technologies Co., Ltd.
China
zhangjiaxin35@huawei.com
Qi Zhang
Huawei Cloud Computing
Technologies Co., Ltd.
China
zhangqi98@huawei.com
Yuchi Ma
Huawei Cloud Computing
Technologies Co., Ltd.
China
mayuchi1@huawei.com
Guangtai Liang
Huawei Cloud Computing
Technologies Co., Ltd.
China
liangguangtai@huawei.com
Ying Li∗
School of Software and
Microelectronics, Peking University
China
li.ying@pku.edu.cn
Qianxiang Wang∗
Huawei Cloud Computing
Technologies Co., Ltd.
China
wangqianxiang@huawei.com
Tao Xie∗
Key Lab of HCST (PKU), MOE; SCS
Peking University
Beijing, China
taoxie@pku.edu.cn
ABSTRACT
Code generation models based on the pre-training and fine-tuning
paradigm have been increasingly attempted by both academia
and industry, resulting in well-known industrial models such as
Codex, CodeGen, and PanGu-Coder. To evaluate the effectiveness
of these models, multiple existing benchmarks (e.g., HumanEval
and AiXBench) are proposed, including only cases of generating a
standalone function, i.e., a function that may invoke or access only
built-in functions and standard libraries. However, non-standalone
functions, which typically are not included in the existing bench-
marks, constitute more than 70% of the functions in popular open-
source projects, and evaluating models’ effectiveness on standalone
functions cannot reflect these models’ effectiveness on pragmatic
code generation scenarios (i.e., code generation for real settings of
open source or proprietary code).
To help bridge the preceding gap, in this paper, we propose a
benchmark named CoderEval, consisting of 230 Python and 230
∗Corresponding author
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0217-4/24/04...$15.00
https://doi.org/10.1145/3597503.3623322
Java code generation problems carefully curated from popular real-
world open-source projects and a self-contained execution platform
to automatically assess the functional correctness of generated code.
CoderEval supports code generation problems from six levels of
context dependency, where context refers to code elements such as
types, APIs, variables, and consts defined outside the target func-
tion but within the dependent third-party libraries, current class,
file, or project. CoderEval can be used to evaluate the effectiveness
of models in generating code beyond only standalone functions.
By evaluating three state-of-the-art code generation models (Code-
Gen, PanGu-Coder, and ChatGPT) on CoderEval and HumanEval,
we find that the effectiveness of these models in generating stan-
dalone functions is substantially higher than that in generating non-
standalone functions. Our analysis highlights the current progress
and pinpoints future directions to further improve a model’s effec-
tiveness by leveraging contextual information for pragmatic code
generation.
CCS CONCEPTS
• Software and its engineering →Automatic programming.
KEYWORDS
Code Generation, Large Language Models, Benchmark
ACM Reference Format:
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai
Liang, Ying Li, Qianxiang Wang, and Tao Xie. 2024. CoderEval: A Benchmark
of Pragmatic Code Generation with Generative Pre-trained Models. In 2024
arXiv:2302.00288v3  [cs.SE]  23 Feb 2024

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
IEEE/ACM 46th International Conference on Software Engineering (ICSE ’24),
April 14–20, 2024, Lisbon, Portugal. ACM, New York, NY, USA, 12 pages.
https://doi.org/10.1145/3597503.3623322
1
INTRODUCTION
Recent years have seen a trend to tackle open-domain code gen-
eration tasks with machine learning techniques, especially large
generative pre-trained language models [3, 4, 20, 23] based on
Transformer [25], such as Codex [7], AlphaCode [18], InCoder [9],
CodeGen [21], PanGu-Coder [8], and ChatGPT [24]. Given natural
language descriptions specifying the functionalities of the target
function, these models can generate both standalone functions (i.e.,
functions that invoke or access only built-in functions and standard
libraries) and non-standalone functions.
To fairly and comprehensively evaluate the effectiveness of the
preceding models, representative benchmarks [2, 5–7, 11–13, 16, 26,
27] are required and widely used in the literature. Released along-
side Codex [7], HumanEval is a benchmark for Python to assess
the functional correctness of programs generated by code gener-
ation models. HumanEval consists of 164 hand-written problems,
each of which includes a function signature, a docstring, a canonical
reference function, and multiple unit tests. Recently, DS-1000 [16]
is proposed to evaluate the effectiveness of code generation models
in generating code that relies on third-party data science libraries. In
addition to Python, there are benchmarks for Java (AixBench [12])
and other programming languages (MultiPL-E [5]), facilitating
the understanding and development of code generation models for
these other languages.
Despite the importance and usefulness of these preceding bench-
marks, there exists a gap between these benchmarks and pragmatic
code generation scenarios (i.e., code generation for real settings
of open source or proprietary code). On one hand, standalone
functions are heavily focused by these benchmarks. In particular,
all the preceding benchmarks except DS-1000 include only stan-
dalone functions. Note that DS-1000 includes standalone functions
in addition to non-standalone functions that invoke API functions
from only seven specific widely used third-party libraries in data
science. On the other hand, non-standalone functions commonly
exist in pragmatic code generation scenarios. After analyzing the
100 most popular projects written in Java and Python, respectively,
on GitHub, we find that non-standalone functions account for more
than 70% functions1 of the open-source projects.
To help bridge the preceding gap, in this paper, we propose
CoderEval, a context-aware benchmark, which can be used to eval-
uate code generation models on pragmatic code generation. Accord-
ing to the source of dependency outside the target function, we cate-
gorize code generation problems into six levels (i.e., self_contained,
slib_runnable, plib_runnable, class_runnable, file_runnable, and
project_runnable), with details described in Section ??. Given that
the existing benchmarks such as HumanEval cover only the first
two levels, CoderEval can provide a more practical and representa-
tive evaluation of the effectiveness of code generation models in
tasks of pragmatic code generation. Note that functions belonging
to the first two levels correspond to standalone functions and the
others correspond to non-standalone functions.
1Detailed statistics are listed in our open-source repository [1].
To construct CoderEval as a representative and diverse bench-
mark for tasks of pragmatic code generation, we select and curate
code generation problems from real-world projects in three steps,
resulting in 230 problems from 43 Python projects and 230 prob-
lems from 10 Java projects. First, we select functions in open source
projects from the most frequent 14 tags and with high star counts on
GitHub. For each function2, we extract the original docstring (i.e.,
the natural language description of the function), the function name
and signature, the code implementation, and the corresponding test
code (if exists) to form one function-level code generation problem.
Additionally, we analyze the detailed contextual information (where
context refers to code elements such as types, APIs, variables, and
consts defined outside the target function, but within the dependent
third-party libraries, current class, file, or project) through program
dependence analysis and provide it as all-context (all accessible
context) and oracle_context (the actually used context), so as to
conduct a fine-grained evaluation about model effectiveness. Sec-
ond, to mitigate data leakage (i.e., the original docstring has a high
probability of being used as training data by large language models),
we recruit 13 experienced engineers to provide a human-labeled
version of description as the second docstring (i.e., human-labeled
docstring) to complement the original docstring. Third, to improve
the evaluation accuracy, we examine the test coverage of the ex-
isting tests provided by each project in CoderEval and manually
write additional tests to achieve high test coverage.
To automatically evaluate code generation models, we automati-
cally measure the Pass@K metric [7] and a newly proposed metric
named Acc@K (described in Section 4.3) to assess generated code.
Since CoderEval involves functions with contextual dependency
and non-primitive types, we build a project-level execution platform
to provide a ready runtime environment that can automatically as-
sess the functional correctness of generated code. We develop this
platform based on Docker, where we clone and set up environments
for all projects. Given multiple solutions generated by a model, the
platform can automatically place the generated code in the proper
location of the project under consideration.
We conduct a comprehensive evaluation of three state-of-the-
art code generation models (CodeGen [21], PanGu-Coder [8], and
ChatGPT [24]) on CoderEval and compare the difference with Hu-
manEval. In the evaluation, for each model, we analyze the overall
and level-wise effectiveness, the ability to correctly utilize contex-
tual information, and the effect of the two different natural lan-
guage descriptions (i.e., the original and human-labeled docstrings).
Furthermore, among these models, we compute the overlapping
and difference in terms of correctly solved functions. Through
the analysis and comparison, we provide a good understanding
of existing models and shed light on future directions and further
progress. Experimental results show that in CoderEval for Python
and CoderEval for Java, the effectiveness of the three models in
generating standalone functions is substantially higher than that in
generating non-standalone functions. Considering that more than
70% of functions in open-source projects belong to non-standalone
functions, improving a model’s ability to consider and use contex-
tual information is vital for the practical value of this technology.
2In this paper, we use the term of function to refer to both Python function and Java
method.

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
In summary, we make the following main contributions:
• We point out the limitation of the existing benchmarks through
an analysis of the 100 most popular open-source projects
written in Java and Python, respectively: the existing bench-
marks such as HumanEval typically include only standalone
functions, whereas non-standalone functions constitute more
than 70% of functions in the open-source projects.
• We introduce CoderEval, a benchmark of pragmatic code
generation. CoderEval originates from open-source projects
from various domains and considers non-primitive types,
third-party libraries, and project-specific contextual refer-
ences. In addition, CoderEval includes the human-labeled
docstring for the target function to complement the original
docstring.
• We evaluate and compare three state-of-the-art code gen-
eration models (CodeGen, PanGu-Coder, and ChatGPT) on
CoderEval. Experimental results indicate three important
findings: (1) these models do not work as well on non-standalone
functions as on standalone functions, (2) it is important yet
challenging for all these models to generate code with con-
textual dependency, even for ChatGPT (the most power-
ful model), and (3) the choice of using the human-labeled
docstring vs. the original docstring has an impact on code
generation effectiveness.
CoderEval and all the experimental results are open-sourced [1] to
continually evolve in the code generation community.
2
BACKGROUND
In this section, we first introduce existing large language models
for code generation. Then, we introduce the benchmarks used by
existing large language models.
2.1
Large Language Models for Code Generation
PanGu-Coder [8] is a pre-trained language model for the task of
text-to-code generation, which is based on the PanGu-𝛼architec-
ture [29] and a two-stage training strategy. CodeGen [21] is a series
of conversational text-to-code large language models trained on
natural language corpora, corpora of multilingual code (i.e., code
written in multiple programming languages), and datasets of Python
code. Codex [7] is the first work to use large generative pre-trained
models to generate complete functions from natural language. Al-
phaCode [18] specializes in programming contests and performs
on par with average human developers. InCoder [9] is a unified
generation model that can perform program synthesis (through
left to right generation) and editing (through padding). InCoder is
trained to generate code files from a large number of code bases
with specific friendly licenses, where code regions are randomly
masked and moved to the end of each file, allowing code to fill with
bidirectional context. In addition to the above-mentioned models,
some other models [2, 10, 17, 19, 28] have been proposed recently.
2.2
Benchmarks for Code Generation
Our proposed CoderEval is so far the only benchmark that sup-
ports project-level code generation and uses the evaluation metrics
with Pass@K, which can validate the functional correctness of the
generated code.
Benchmarks that contain project-level functions are important
and yet difficult to construct for two main reasons. First, it is nec-
essary to ensure that the selected projects can be compiled and
sandboxed to achieve successful execution of different projects.
However, it is difficult to successfully build and run many existing
open-source projects. Second, to speed up testing, for the target
function, the often large number of its covering test cases from
its belonging project needs to be desirably reduced but statically
determining whether a test case covers the target function requires
non-trivial construction of functional dependency diagrams and
coverage stub analysis. In addition, when the target function is not
covered by the test cases of its belonging project, the builders of
the benchmarks need to have a deep understanding of the often
complex logic of the belonging project before writing high-quality
test cases.
Most existing benchmarks (e.g., HumanEval [7], MulitPL-E [5],
DS-1000 [16], and AiXBench [12]) use Pass@K for validating the
correctness of a generated function and they contain only stan-
dalone functions. Although DS-1000 can validate the correctness
of generated non-standalone functions, these non-standalone func-
tions are limited to those that invoke API functions from only seven
specific widely used third-party libraries in data science.
Not being a benchmark, Concode [15] is a large dataset that con-
tains over 100,000 functions from approximately 33,000 open-source
Java repositories. In Concode, functions from the same repository
are split into training, validation, and test sets, so that a deep learn-
ing model can be trained based on the training and validation sets,
and then be tested on the test set. Each function included in Con-
code is in the form of a pair: its natural language annotation and
code implementation.
Although Concode can support validating the effectiveness of
code generation approaches on generating non-standalone func-
tions, there are five main differences between CoderEval and Con-
code for highlighting CoderEval’s advantages. (1) CoderEval val-
idates the correctness of the generated function by executing it,
whereas Concode does so based on the text similarity between the
generated function and the ground-truth function. (2) CoderEval
alleviates the problem of data leakage by providing human-labeled
docstrings whereas docstrings in Concode are likely “seen” by large
language models during the pre-training stage. (3) The functions
in CoderEval have been carefully selected by developers, whereas
the functions in Concode are automatically collected and have not
been carefully selected by developers. (4) CoderEval supports both
Java and Python languages, whereas Concode supports only Java.
(5) CoderEval contains latest code from the past five years, whereas
all functions in Concode come from open-source code before 2018.
2.3
Statistical Comparison with Different
Benchmarks
Table 1 shows the average value of cyclomatic complexity and
average number of lines of code in CoderEval, HumanEval, and
Concode. We find that the cyclomatic complexity of functions in
CoderEval is similar to HumanEval, and the average number of
lines of code in CoderEval is more than that in HumanEval.

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
Dataset Collection
Dataset Inspection
Runnable-level
Classification
Contextual
Dependency
Identification
Human Labeling
Evaluation Process
CoderEval
Data
Project 1
Project 2
...
Project n
Docker
Environments
Candidate
Projects
Candidate
Functions
CI Exec,
Test Trans
Filtering Projects
(Tags & Stars)
Selected
Projects
Filtering Functions
(Not Test, etc.)


Selected
Functions
Test
Generation
(         )
Solution Generation
By LLMs
Solutions
Results:
- Pass@K
    or
- Acc@K
Find Project for Each Solution
Replace the
Ground Truth
with the
Generated Solution
 
 
Manual Selection
(Code Quality)
Figure 1: Overview of CoderEval construction process
Table 1: Statistical comparison among CoderEval, Hu-
manEval, and Concode
Benchmark
Statistical
Cyclomatic Complexity
Line of Code
CoderEval-Python
4.71
32.0
CoderEval-Java
3.10
10.2
HumanEval
3.62
7.8
Concode
1.43
4.8
3
CODEREVAL BENCHMARK
In this section, we introduce CoderEval, whose construction process
is shown in Fig 1. The construction process of CoderEval includes
three phases: dataset collection, dataset inspection, and evaluation
process.
3.1
Dataset Collection
3.1.1
Problem Selection. To make CoderEval pragmatic and di-
verse, we select functions from various open-source projects by
four steps. (1) We select candidate projects by crawling the tags of
all projects on GitHub and selecting projects with the most frequent
14 tags and with high stars. For each tag, we select the projects
with the top five highest number of stars. The 14 types of tags are
“gson”, “music”, “logging”, “chat”, “websocket”, “mvc”, “leetcode”,
“microservices”, “jdbc”, “json”, “crud”, “datastructures”, “log4j”, and
“serialization”. (2) We extract all functions in the selected projects,
and keep only the ones that are not a test, interface, or deprecated
function, with a function-level comment in English, and can run
successfully in the verification platform (Section 3.3) and pass the
original test cases. (3) We select high-quality functions from the can-
didate functions through manual screening, whose main criterion is
whether a function often appears in real development scenarios. (4)
We attain projects according to the number of the selected functions
contained in each project. This process can help us compile fewer
projects with the same number of total selected functions. In the
end, we attain 230 problems from 10 projects in Java. To maintain
consistency with the number of problems in CoderEval for Java, we
also attain 230 problems for CoderEval for Python from 43 projects.
The reason why we select high-quality functions manually (the
third step described above) is that we want CoderEval to assess a
model’s ability to generate code that is helpful to developers. We
engage experienced developers to select functions that may be used
in real scenarios, following five rules. (1) Functions that contain
fewer than ten contextual tokens. Excessive contextual dependen-
cies make it difficult for a model to generate correct solutions. The
functions that are too difficult for all LLMs to generate correct im-
plementations are not suitable for the benchmark. (2) Functions that
are frequently used in real development scenarios judged by any of
the 13 experienced engineers recruited by us. The rationale behind
this rule is that different developers have various preferences over
frequently used functions. (3) Functions containing docstrings that
can reflect the implementations of the functions. (4) Functions that
have more than three lines of code implementation. (5) Functions
that are not test or deprecated functions.
3.1.2
Test Construction. For each project included CoderEval, we
first run the unit test cases contained in the original project and
measure the branch coverage of each function (from the project)
included in CoderEval. When a function’s branch coverage has not
achieved 100%, the first author of this paper has manually written
additional test cases for this function to aim to achieve 100% branch
coverage (if ever possible).
Based on the unit test cases in the original projects (in addition
to those manually written by the first author), we construct test
cases in CoderEval via two steps. (1) To obtain the corresponding
test cases of a function in CoderEval, we construct a static function
call graph from source code and then use the graph to select all
the test cases that can reach the function. In doing so, when we
assess the correctness of a function, we avoid the high cost of
executing all the test cases in the function’s belonging project.
(2) To unify and simplify the interface of invoking the test cases
in CoderEval, we automatically convert the corresponding test
cases (typically depending on test frameworks such as JUnit and
TestNG) of a function in CoderEval into non-test functions with
the “main” function in a new Python/Java file. We denote these new
Python/Java files as “NewTestFile”.
3.2
Dataset Inspection
3.2.1
Human-labeled Docstring. When large language models (LLMs)
are used for code generation, choosing what prompts to use can
have a great impact on the quality of the generated code. To study
the effect of different prompts, we recruit 13 experienced engineers
with at least 3 years experience of Python/Java, and let them provide
a human-labeled version for the description (named as docstring)
of each problem in CoderEval.
There are three main reasons for including human-labeled doc-
strings in CoderEval. (1) Including human-labeled docstrings helps
mitigate the memory effect (i.e., original docstrings have a high
probability of being seen by LLMs in the pre-training stage) of

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Table 2: Dependencies belonging to each contextual dependency type
Dependency Type
Dependencies
Examples in Python
Examples in Java
self-contained
built-in types/functions, no need to import
min(), print()
System.xxx
slib-runnable
standard libraries/modules, no need to install
os, subprocess, sys
Arrays.sort()
plib-runnable
publicly available libraries on pypi/maven
unittest2, requests
com.google.code.gson
class-runnable
code outside the function but within class
self.xxx, X.f()
this.f()
file-runnable
code outside the class but within the file
func(), URL, name
func()
project-runnable
code in the other source files
superclass, utils
superclass, utils
Each runnable level must depend on the dependencies defined at this level, must not depend on the
dependencies defined at its subsequent levels, and may or may not depend on dependencies defined at its previous levels.
LLMs and explore the impact of prompts with human labeling on
the quality of code generated by LLMs. (2) Including human-labeled
docstrings helps study how LLMs perform on different docstrings.
(3) Including human-labeled docstrings helps provide high-quality
docstrings for the functions in CoderEval. During our initial study,
we find that the original docstrings (from the selected open-source
projects) for the problems in CoderEval are highly diverse, well be-
yond describing functionalities, which are typically used as prompts
for LLMs. An original docstring can play multiple different roles,
such as explaining the internal logic, introducing the external usage
and behavior, declaring the effect and caution.
3.2.2
Contextual Dependency Identification. One of major differ-
ences between HumanEval [7] and CoderEval is that CoderEval
considers the target function’s contextual dependency, which refers
to code elements defined outside of the target function but required
by it in order to run. Table 2 shows the dependencies belonging to
each dependency type along with examples.
We identify the contextual dependencies of a function through
program analysis of its belonging project with three steps3. (1)
Before the analysis, we first build a knowledge base that helps
identify different references of Python/Java builtins and different
imports of standard or public libraries from the project-specific
code. To do so, we cache all built-in types/functions/variables/-
constants and standard library names for each Python version
from 3.0.0 to 3.10.0 and Java version from 1.8 to 17, as well as
all publicly available libraries on 𝑝𝑦𝑝𝑖.𝑜𝑟𝑔and the 𝑀𝑎𝑣𝑒𝑛central
repository. (2) With the knowledge base, given the function un-
der analysis, we parse the source file that contains the function to
get a list of type/function/variable/constant definitions. (3) We em-
ploy static program analysis to identify all the dependent elements
namely the external references and invocations whose definitions
are outside the function under analysis, and classify them into
three categories: type_reference, variable_reference, and API invo-
cation. More specifically, type_reference refers to a user-defined
class or a standard type (e.g., “List”, “subprocess”, and “os”). Vari-
able_reference refers to a user-defined variable or object. API invo-
cation refers to a user-defined function or function in a standard or
third-party library.
3Note that we also use the same three steps of identifying contextual dependencies
to calculate the proportions of standalone functions and non-standalone functions,
respectively, in the 100 most popular projects written in Java and Python on GitHub,
respectively (as reported in Section 1).
We use a function’s oracle_context information to denote its
contextual dependencies identified by the preceding three steps.
Oracle_context information not only can be used to evaluate the
accuracy of the contextual dependencies in the code generated by
an LLM (as done in our experiments) but also can be used as part of
the input to the LLM in the inference stage, to explore prompting the
LLM additionally with the oracle_context information to improve
code-generation effectiveness.
However, it is usually difficult for the users of an LLM to know
oracle_context information in advance, so CoderEval also includes a
function’s all_context information (i.e., all types, variables, and APIs
defined/imported in the function’s belonging file), which can be
additionally used to prompt the LLM to generate code incorporating
part or all of the all_context information. Note that we do not
use the all_context information in the inference stage during our
experiments; there we use only the original docstring, human-
labeled docstring, function name, and function signature of the
target function. We hope that the all_context information can be
valuable for the research community, and we plan to study the
impact of all_context information (as part of the used prompt) on
code-generation effectiveness in our future work.
3.2.3
Runnable Level Classification. As shown in Table 2, we clas-
sify the target function into six runnable levels, each of which refers
to the scope that the function can run successfully. These levels
include self-contained, slib-runnable, plib-runnable, class-runnable,
file-runnable, and project-runnable. Each runnable level must de-
pend on the dependencies defined at this level, must not depend
on the dependencies defined at its subsequent levels, and may or
may not depend on dependencies defined at its previous levels. For
example, a function at the plib-runnable level depends on public li-
braries, so it can run successfully outside its belonging class, source
file, and project, as long as the required Python version is used and
the libraries are installed and imported.
The left and right parts of Fig 2 show the distribution of runnable
levels on CoderEval for Python and Java, respectively. Most (84%)
of the problems collected in CoderEval for Python are file-runnable,
indicating that the oracle_context information in their respective
belonging file is necessary and critical for an LLM to generate the
target function correctly. The class-runnable functions account
for about half (54%) of all the functions; this result is not surpris-
ing considering the prevalence of object-oriented programming in

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
self_contained
project_runnable 
file_runnable 
55 (24%)
80 (35%)
85 (37%)
185 (80%)
186 (81%)
230 (100%)
35 (15%)
63 (27%)
84 (36%)
139 (60%)
207 (90%)
230 (100%)
Python
Java
class_runnable
plib_runnable
slib_runnable
Figure 2: Distribution of runnable levels in CoderEval
open-source non-trivial projects. On the contrary, the slib-runnable
functions account for only 17% of the functions in CoderEval for
Python but 100% in the case of HumanEval. This result shows
limitation of HumanEval when used for model optimization and
evaluation, especially in pragmatic code generation in real settings.
Similar to CoderEval for Python, the slib-runnable functions ac-
count for only 35% of the functions in CoderEval for Java.
3.3
Evaluation Process
To provide a ready runtime environment to automatically execute
and evaluate a function generated by a model, we construct an
evaluation platform based on a Linux Docker image, which can
provide a virtual sandbox to enable easy and safe distribution.
3.3.1
Evaluation for Python. To evaluate a generated Python func-
tion for the target function, we need to clone and set up environ-
ments for all the Python projects in CoderEval. To avoid conflicts of
Python/library versions, under each repository’s root directory, we
first use pyenv to set the local Python version to the latest version
specified in the CI configuration or document, and then use venv to
create an individual virtual environment for the target function’s
belonging project. After that, we use pip to install all the dependen-
cies and trigger execution of the test cases in the original belonging
project to ensure successful setup of the runtime environment.
After the runtime environment is successfully set up, our plat-
form automatically replaces the target function (in its belonging
project) with the generated function, invokes the generated func-
tion with the test inputs from the corresponding test cases of the
target function, and compares the actual test outputs with the ex-
pected outputs from the corresponding test cases to determine
whether all the corresponding test cases pass or not.
3.3.2
Evaluation for Java. Similar to the evaluation platform for
Python, the evaluation platform for Java also first clones all the
Java projects in CoderEval. We ensure that all Java projects in
CoderEval can be executed with the Java 17 version. Different from
Python code, Java code needs to be compiled before execution, so
the platform automatically compiles the test file (i.e., “NewTestFile”)
(including the corresponding test cases of the target function) in
advance, and then replaces the target function with the generated
function in the belonging project.
The platform then runs the “javac” command to incrementally
compile the changed files (whose changes are caused by the function
replacement), and runs the “java” command to execute the bytecode
of “NewTestFile”. The return value of the “java” command indicates
whether all the corresponding test cases of the target function pass
or not. Note that our platform uses the parameter “-cp” of both the
“javac” and “java” commands to import the class file of the given test
file and its dependent files/libraries. In addition, if the compilation
fails, our platform (without executing test cases) determines that
not all the corresponding test cases of the target function pass.
4
EXPERIMENTAL SETUP
In this section, we describe the setup of our experiment with three
models (CodeGen [21], PanGu-Coder [8], and ChatGPT [24]) on two
benchmarks (CoderEval and HumanEval [7]) in terms of research
questions, model settings, and evaluation metric. To alleviate the
randomness of a single run of experiment, we run each experiment
10 times and find that the standard deviation of the used evaluation
metric (namely Pass@K) for all models is about 1%. To better show
the experimental results (e.g., complementarity and overlapping of
different models in generating correct functions), in this section,
the discussed results focus on the median group of experiments
from 10 experiments according to the Pass@10 metric value. Our
experimental results and related artifacts are publicly available [1].
4.1
Research Questions
Our experiment intends to answer the following research questions:
• RQ1: How do the models of CodeGen, PanGu-Coder, and
ChatGPT perform, especially in generating standalone vs.
non-standalone functions?
• RQ2: How do these models perform in correctly incorporat-
ing the oracle_context information in the generated code?
• RQ3: How do different prompts impact the effectiveness of
these models?
4.2
Model Selection and Settings
4.2.1
Model selection. We focus on models that support code gen-
eration for both Python and Java. CodeGen, PanGu-Coder, and
ChatGPT all support both Java and Python. Specifically, we choose
CodeGen because CodeGen has specialized models for the Python
language (CodeGen-mono) and models that support multiple lan-
guages (CodeGen-multi). We choose PanGu-Coder because PanGu-
Coder has two models specifically designed for Python and Java,
respectively. We choose ChatGPT because ChatGPT is the most
effective and parameter-intensive multilingual model. Selecting
these models helps compare the effectiveness of single-language
generative models and multi-language generative models. The rea-
son why we do not select CodeGeex [30] is that its model is of 13B
size, being too large for us to complete the experiments due to our
limited computing resources at the time of the paper writing. We
plan to evaluate the effectiveness of CodeGeex and other recent
open-source models (e.g., StarCoder [17] and WizardCoder [19])
on CoderEval in future work.
4.2.2
Model settings. For PanGu-Coder, we use the 300M PanGu-
Coder model with the default settings. For CodeGen, we use the

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Table 3: Overall effectiveness of three models on two benchmarks
Benchmark
Model
Python
Java
Pass@1
Pass@5
Pass@10
Pass@1
Pass@5
Pass@10
CoderEval
CodeGen1
9.48%
19.58%
23.48%
13.91%
27.34%
33.48%
PanGu-Coder2
11.83%
20.93%
27.39%
25.43%
37.39%
43.04%
ChatGPT3
21.04%
27.31%
30.00%
35.39%
42.77%
46.09%
HumanEval
CodeGen1
10.20%
19.79%
22.80%
5.78%
9.00%
9.45%
PanGu-Coder2
13.42%
21.48%
22.73%
8.21%
15.88%
18.63%
ChatGPT3
39.21%
64.09%
72.96%
38.21%
59.35%
67.23%
1 We use the 350M CodeGen-Mono model with the default settings for Python. Since CodeGen does not have a monolingual
version of Java, on CoderEval for Java, we use the CodeGen-Multi model instead.
2 PanGu-Coder has two different models for Python and Java, and we use the 300M models with the default settings for Python
and Java.
3 We use the “gpt-3.5-turbo” for ChatGPT in our experiments.
350M CodeGen-Mono model with the default settings for Python.
Since CodeGen does not have a monolingual version of Java, on
CoderEval for Java, we use the CodeGen-Multi model instead. For
ChatGPT, we use the “gpt-3.5-turbo” in our experiments. ChatGPT’s
scale of model parameters is much larger than the other two models.
In the inference stage, for all models, we set the max window
length to 1024. We use nucleus sampling [14]: the number of sam-
ples is 10 (i.e., generating 10 codes per function), and the tempera-
ture is 0.8.
4.3
Evaluation Metric
Similar to HumanEval, we adopt the Pass@K metric for an LLM.
In particular, given the 230 problems in CoderEval, Pass@K for
an LLM measures the percentage of the problems (among the 230
problems) for which there is at least one correctly (judged based on
running the corresponding test cases) generated solution among
the top K samples (i.e., solutions) generated by the LLM. During
the experiments, we set the total number (denoted as n) of samples
generated by an LLM to 10, and then calculate Pass@K for the LLM
with K’s value of 1, 5, and 10, respectively. To avoid the issue of
high sampling variance, we use the unbiased estimator of Pass@K
implemented by ChatGPT in HumanEval4. Note that although n is
set to 200 in previous work on PanGu-Coder [8] and CodeGen [21],
we set n to 10 as what the Copilot plugin does because we con-
sider that sampling 10 times is more feasible and reasonable at an
acceptable cost and response time in practical settings.
Besides Pass@K, we also propose the Acc@K metric for an LLM
based on oracle_context tokens (i.e., dependent elements included
in the oracle_context information) to evaluate the LLM’s capability
of generating each individual oracle_context token among the top
K samples generated by the LLM. In particular, Acc@K for an LLM
measures the percentage of the target functions (among the 230
target functions as ground truth solutions for the 230 problems)
whose each oracle_context token is included by at least one of K
samples generated by the LLM. Note that other metrics can be for-
mulated to evaluate an LLM’s capability of generating a function
including all the oracle_context tokens in the target function (with
and without consideration of the tokens’ sequential order, respec-
tively). These metrics impose more challenging requirements for
4https://github.com/openai/human-eval/
an LLM to satisfy, and we plan to explore these and other metrics
in future work.
5
EXPERIMENTAL RESULTS
In this section, we detail the experimental results for CodeGen,
PanGu-Coder, and ChatGPT.
5.1
RQ1: How Do CodeGen, PanGu-Coder, and
ChatGPT Perform, Especially in Generating
Standalone vs. Non-Standalone Functions?
5.1.1
Overall effectiveness. Table 3 reports the overall effectiveness
of CodeGen, PanGu-Coder, and ChatGPT on CoderEval and Hu-
manEval. On HumanEval, the reported effectiveness of the three
models on HumanEval for Python is the effectiveness reported in
these models’ respective corresponding papers. These papers do
not report the effectiveness (being evaluated in our experiments)
of their models on HumanEval for Java. Since the problems in
CoderEval for Python and those in CoderEval for Java do not have
overlapping, we cannot directly compare the effectiveness of the
three models on CoderEval for Python and that on CoderEval for
Java. On both HumanEval and CoderEval (for both Python and
Java), ChatGPT consistently outperforms the other two models.
The reason is that ChatGPT’s parameter scale is much larger than
the other two models. CodeGen and PanGu-Coder perform worse
on HumanEval than on CoderEval because although the functions
in HumanEval are standalone functions (i.e., a function that may
invoke or access only built-in functions and standard libraries),
their complexity is higher than that of the standalone functions
in CoderEval. The functions in HumanEval tend to be more algo-
rithmic, while the standalone functions in CoderEval tend to be
more simple and practical (e.g., converting integer to string or float-
ing point number). The effectiveness of ChatGPT in HumanEval
is higher than that in CoderEval. ChatGPT’s powerful algorithmic
learning abilities make ChatGPT perform well on HumanEval. How-
ever, when generating code that relies on oracle_context tokens,
the prompts given to ChatGPT do not include all_context tokens,
resulting in poor effectiveness on CoderEval.
5.1.2
Complementarity and overlapping of three models. Fig 3 shows
the number of solved problems by the three models on CoderEval,

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
Table 4: Effectiveness comparison between the generation of standalone and non-standalone functions on CoderEval
Runnable-Level
Model
Python
Java
Pass@1
Pass@5
Pass@10
Pass@1
Pass@5
Pass@10
standalone:
CodeGen
18.10%
33.38%
38.10%
26.25%
46.40%
52.50%
PanGu-Coder
19.52%
31.30%
38.10%
43.88%
57.23%
62.50%
ChatGPT
35.87%
43.56%
47.62%
64.88%
68.65%
70.00%
- self-contained
CodeGen
22.57%
36.75%
40.00%
27.27%
49.37%
56.36%
PanGu-Coder
23.71%
34.93%
40.00%
48.36%
57.94%
61.82%
ChatGPT
52.29%
60.08%
82.86%
61.82%
66.21%
67.27%
- slib-runnable
CodeGen
12.50%
29.17%
35.71%
24.00%
39.87%
44.00%
PanGu-Coder
14.29%
26.76%
35.71%
34.00%
55.68%
64.00%
ChatGPT
15.36%
22.92%
28.57%
71.60%
74.00%
76.00%
non-standalone:
CodeGen
6.23%
14.38%
17.96%
7.33%
17.17%
23.33%
PanGu-Coder
8.92%
17.02%
23.35%
15.60%
26.81%
32.67%
ChatGPT
15.45%
21.18%
23.35%
19.67%
28.97%
33.33%
- plib-runnable
CodeGen
4.76%
16.16%
23.81%
0%
0%
0%
PanGu-Coder
13.33%
22.75%
28.57%
0%
0%
0%
ChatGPT
21.43%
28.06%
28.57%
0%
0%
0%
- class-runnable
CodeGen
5.82%
9.05%
10.91%
8.30%
19.21%
26.00%
PanGu-Coder
7.82%
15.04%
21.82%
19.90%
32.59%
40.00%
ChatGPT
8.73%
12.57%
14.55%
22.40%
31.49%
36.00%
- file-runnable
CodeGen
7.79%
20.19%
25.00%
0%
0%
0%
PanGu-Coder
9.41%
19.04%
26.47%
0%
0%
0%
ChatGPT
21.03%
29.09%
32.35%
0%
0%
0%
- project-runnable
CodeGen
3.91%
8.33%
8.70%
6.14%
14.89%
20.45%
PanGu-Coder
6.09%
10.51%
13.04%
7.95%
17.33%
20.45%
ChatGPT
9.57%
12.08%
13.04%
16.14%
27.20%
31.82%
!"
#
$%
$"
#
$"
&'()*)+
!
,-+*./&'()0
&1-2*,3
CE4Python
(a) CoderEval for Python
"#
""
!
&'()*)+
!
,-+*./&'()0
$7
&1-2*,3
CE4Java
!6
"8
(b) CoderEval for Java
Figure 3: Number of problems solved by CodeGen, PanGu-
Coder, and ChatGPT, respectively, on CoderEval
with the difference and overlapping. We use the median group of
experiments selected from 10 experiments with the Pass@10 value
to count the passing problems of each model. We consider a prob-
lem to be solved by a model if the model can generate at least one
solution (out of the 10 generated solutions) that passes all the test
cases. Among the 230 problems in CoderEval for Python, the total
number of functions solved by at least one of the three models is 91
(complementarity), while 32 problems (overlapping) can be solved
by any of the three models. On CoderEval for Java, the total number
of problems solved by at least one of the three models is 136 (com-
plementarity), while 56 problems (overlapping) can be solved by
any of the three models. The high complementarity indicates that
different models have their unique capabilities, and the high over-
lapping indicates that the ability of the three models to generate the
correct problem is consistent in some problems. We manually ana-
lyze the overlapping problems and find that more than half of them
belong to standalone functions. More specifically, the total number
of overlapping problems in CoderEval is 88, of which 52 belong to
standalone functions. Note that the standalone functions account
for only about 30% in CoderEval. Therefore, the three models are all
good at generating standalone functions (while ChatGPT performs
particularly well); extending the ability to non-standalone functions
and exploring how to combine the code generation capabilities of
different models are worthwhile research directions.
5.1.3
Effectiveness comparison between the generation of standalone
and non-standalone functions. Since all functions in HumanEval are
standalone functions, we further compare the effectiveness of three
models in generating the standalone functions in CoderEval with
the effectiveness of the non-standalone functions in CoderEval. The
standalone and non-standalone rows in Table 4 show that, in both
CoderEval for Python and CoderEval for Java, the effectiveness of
the three models in generating the standalone functions is substan-
tially higher than that of the non-standalone functions. Considering
that more than 70% of functions in open-source projects belong to
non-standalone functions, improving a model’s ability to correctly
generate oracle_context information is vital for pragmatic code
generation.

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Table 5: The similarity between the original docstring and
human-labeled docstring
Language
Metrics
BLEU-4
Jaccard Similarity
Python
54.7
55.2
Java
18.1
26.9
We evaluate both standalone and non-standalone functions at
detailed runnable levels. Standalone functions include two runnable
levels, self-contained and slib-runnable, and non-standalone func-
tions include four runnable levels, plib-runnable, class-runnable, file-
runnable, and project-runnable. From Table 4, we find that except for
the Pass@5 and Pass@10 of class-runnable on CoderEval for Java,
ChatGPT outperforms the other two models on all runnable levels.
As discussed in Section 5.1.1, the main reason is that ChatGPT’s
parameter scale is much larger than the other two models.
In summary, on both CoderEval for Python and CoderEval
for Java, the effectiveness of the three models in generating
standalone functions is substantially higher than that in gen-
erating non-standalone functions. Different models have their
unique capabilities in code generation, and how to combine
the code generation capabilities of different models is a worth-
while research direction.
5.2
RQ2: How Do These Models Perform in
Correctly Incorporating the Oracle_context
Information in the Generated Code?
To further study the ability of LLMs to generate oracle_context to-
kens, we analyze the oracle_context tokens in generated solutions
and focus on three categories of tokens: TypeReference, APIInvo-
cation, and VarReference (note that VarReference does not include
variables defined in the target function).
Fig 4 shows Acc@K of three models; the results shown in the
figure are the average values obtained from 10 experiments. We
find that the Acc@K value of the three models is consistent with
Pass@K (reflecting that the generated functions can pass test cases).
To further explore the ability of different models to generate differ-
ent types of oracle_context tokens, we divide the oracle_context
tokens into three categories: TypeReference, APIInvocation, and
VarReference. Tokens belonging to these three categories typically
form the most important part of the target function. As shown in
Fig 4, on CoderEval for Python, all models show poor effectiveness
in correctly generating the “VarReference” tokens, while the effec-
tiveness in correctly generating the “TypeReference” tokens is the
best. However, when it comes to Java, all models have poor effec-
tiveness in correctly generating the “TypeReference” tokens, while
the effectiveness in correctly generating “APIInvocation” tokens is
the best. The experimental results indicate that the ability of LLMs
to generate different types of oracle_context tokens varies across
different languages. Generating tokens of different categories for
different languages is an interesting future research direction.
In summary, as listed in Table 3 and Fig 4, the ability of LLMs
to generate the oracle_context tokens (reflected by Acc@K)
is consistent with that for generating correct code (reflected
by Pass@K). As shown in Fig 4, the ability of LLMs to gen-
erate different categories (i.e., TypeReference, APIInvocation,
and VariableReference) of oracle_context tokens varies across
different languages.
5.3
RQ3: How Do Different Prompts Impact the
Effectiveness of These Models?
We evaluate the three models with both the original docstrings
and the human-labeled docstrings, and show the results in Tables 5
and 6. Table 5 shows the similarity between the original docstrings
and human-labeled docstrings. From Table 5, we find that the BLEU-
4 [22] value and Jaccard similarity of the original docstring and
human-labeled docstring in a problem of CoderEval for Python
is higher than that of CoderEval for Java. Table 6 shows that for
all models, the Pass@K values of the code generated by using the
original docstrings and human-labeled docstrings of the three mod-
els are more similar on CoderEval for Python than on CoderEval
for Java. On CoderEval for Java, the effectiveness of CodeGen and
ChatGPT with the original docstrings is higher than their effec-
tiveness with the human-labeled docstrings, while the opposite
result is observed when the effectiveness of PanGu-Coder with
the original docstrings is compared with its effectiveness with the
human-labeled docstrings.
There are two main reasons for the preceding results. First, the
similarity between the original docstrings and human-labeled doc-
strings for Python is higher than the similarity between the original
docstrings and human-labeled docstrings for Java. Second, compar-
ing the generated code with two docstring versions, we find model
effectiveness is related to the proportion of the target-language
corpus in the whole training data. For Python, high model effective-
ness can be attributed to dedicated training or fine-tuning on the
Python-code corpus, while for Java, only PanGu-Coder undergoes
pre-training on the Java-code corpus. Therefore, while multilingual
pre-training can transfer knowledge and bring better generalization
across languages [17], monolingual pre-training or fine-tuning is
still necessary for the model effectiveness.
In summary, we find that the choice of using the human-
labeled docstring vs. the original docstring in a problem has
an impact on code generation effectiveness. In the task of
code generation for a single language, when given a docstring
with the same semantics but different expressions, the model
trained with a single-language corpus performs better than
the model trained with a multiple-language corpus.
6
RELATED WORK
HumanEval is a benchmark to evaluate code generation models on
the functional correctness of code generated from docstrings [7]. It

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
Figure 4: The three models’ accuracy of generating the oracle_context tokens
Table 6: Effectiveness with two prompt versions of CoderEval
Model
Prompt
Python
Java
Pass@1
Pass@5
Pass@10
Pass@1
Pass@5
Pass@10
CodeGen
Original
9.48%
19.58%
23.48%
13.87%
27.12%
33.04%
Human Label
12.26%
22.49%
25.65%
10.65%
21.36%
26.52%
PanGu-Coder
Original
11.83%
20.93%
27.39%
25.43%
37.39%
43.04%
Human Label
13.74%
21.14%
24.78%
26.70%
40.33%
46.09%
ChatGPT
Original
21.13%
27.31%
30.00%
35.39%
42.77%
46.09%
Human Label
26.61%
31.31%
32.61%
26.96%
34.85%
37.39%
consists of 164 hand-written programming problems (each prob-
lem’s functionality is reflected by a docstring) along with solutions
(in Python), each of which includes a function signature, body, and
multiple unit tests.
Following HumanEval, AiXBench [12] is proposed to benchmark
code generation models for Java. AiXBench contains 175 problems
for automated evaluation and 161 problems for manual evaluation.
The authors of AiXBench present a new metric for automatically
assessing the correctness of the generated code, and a set of criteria
to manually evaluate the overall quality of the generated code.
MultiPL-E [5] is the first multi-language parallel benchmark
for text-to-code generation. MultiPL-E extends HumanEval and
MBPP [2] to support 18 programming languages. MultiPL-E in-
cludes a suite of compilers and an evaluation framework for trans-
lating code generation benchmarks (including unit test cases, doc-
strings, Python-specific terminology, and type annotations) from
Python into other programming languages. MultiPL-E contains two
parallel benchmark portions (i.e., HumanEval and MBPP) for code
generation in 18 languages encompassing various programming
paradigms, language features, and popularity levels.
While all the preceding benchmarks contain only standalone
functions, another benchmark named DS-1000 [16] contains non-
standalone functions. In particular, DS-1000 contains 1000 problems,
covering seven widely used Python data science libraries: NumPy,
Pandas, TensorFlow, PyTorch, Scipy, Scikit-learn, and Matplotlib.
The authors of DS-1000 mitigate the problem of data leakage by
manually modifying functions while emphasizing the use of data
from real development scenarios to construct DS-1000.
Although DS-1000 contains non-standalone functions, DS-1000
has two major limitations. First, the functions in DS-1000 are col-
lected from only seven data science third-party libraries in Python.
Second, although some functions in DS-1000 have contextual depen-
dencies on third-party libraries, the development scenarios reflected
by DS-1000 are far from pragmatic code generation because no
function in DS-1000 has contextual dependencies on user-defined
functions outside of the target function.

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

CoderEval: A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models
ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Concode [15] is a new large dataset that contains over 100,000
problems of Java classes from open-source projects. From a public
Java project on GitHub, the authors of Concode collect each function
that has at least one contextual dependency as well as the tuple of
natural language (i.e., Javadoc-style method annotations) and code.
The authors of Concode collect Java functions from approximately
33,000 repositories and then split them into training, validation, and
test sets at the granularity of repositories, instead of the granularity
of functions. Although the functions in Concode contain contextual
dependencies, Concode uses only BLEU as its evaluation metric,
and does not evaluate the correctness of the generated functions,
given that each problem in Concode does not include test cases.
7
THREATS TO VALIDITY
A threat to validity includes the degree to which the models used in
our experiments are representative of true practice. All three mod-
els used in the experiments come from industry, and each model
achieved SOTA performance on HumanEval when it was first pro-
posed. Due to our limited computing resources at the time of the
paper writing, we do not conduct experiments with a number of
other recent models such as CodeGeex, StarCoder, and Wizard-
Coder on CoderEval. Such threat could be reduced by more experi-
ments on wider types of subjects in future work. Another threat
in our work comes from the accuracy of the statistics for the pro-
portion of standalone vs. non-standalone functions. Section 3.2.2
shows the way that we use to count the proportion of standalone
vs. non-standalone functions. To identify whether a function has a
contextual dependency on a third-party library, we collect all third-
party libraries from 𝑝𝑦𝑝𝑖for Python and 𝑚𝑎𝑣𝑒𝑛for Java. Due to
our inability to guarantee the collection of all third-party libraries,
there may be a slight deviation in the resulting statistics.
8
CONCLUSION
In this paper, we have presented a new benchmark named CoderEval
to evaluate a model’s effectiveness in pragmatic code generation
scenarios. Compared with the widely used HumanEval benchmark,
CoderEval includes carefully selected problems from various open-
source projects to evaluate the effectiveness of models in pragmatic
code generation. The experimental results show that CoderEval can
reveal the strengths and weaknesses of three LLMs, highlighting the
limitations of these existing code generation models in generating
non-standalone functions.
ACKNOWLEDGMENTS
This work was partially supported by National Key Research and
Development Program Project (2021YFF0704202), National Natural
Science Foundation of China under Grant No. 62161146003, a grant
from Huawei, and the Tencent Foundation/XPLORER PRIZE.
We would like to thank Jiaming Huang, Tianyu Chen, Ziyue
Hua, and Kun Zhou for their help with improving the quality of
unit test cases in CoderEval.
REFERENCES
[1] 2022. https://github.com/CoderEval/CoderEval.
[2] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk
Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le,
and Charles Sutton. 2021. Program Synthesis with Large Language Models.
arXiv:cs.PL/2108.07732
[3] Sid Black, Leo Gao, Phil Wang, Connor Leahy, and Stella Biderman. 2021. GPT-
Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow. https:
//doi.org/10.5281/zenodo.5297715
[4] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language Models Are Few-shot Learners. Advances in Neural
Information Processing Systems (2020), 1877–1901.
[5] Federico Cassano, John Gouwar, Daniel Nguyen, Sydney Nguyen, Luna Phipps-
Costin, Donald Pinckney, Ming-Ho Yee, Yangtian Zi, Carolyn Jane Anderson,
Molly Q Feldman, Arjun Guha, Michael Greenberg, and Abhinav Jangda. 2023.
MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code
Generation. IEEE Transactions on Software Engineering (2023), 3675–3691. https:
//doi.org/10.1109/TSE.2023.3267446
[6] Shubham Chandel, Colin B Clement, Guillermo Serrato, and Neel Sundaresan.
2022. Training and Evaluating a Jupyter Notebook Data Science Assistant. arXiv
preprint arXiv:2201.12901 (2022).
[7] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira
Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman,
et al. 2021. Evaluating Large Language Models Trained on Code. arXiv preprint
arXiv:2107.03374 (2021).
[8] Fenia Christopoulou, Gerasimos Lampouras, Milan Gritta, Guchun Zhang, Yin-
peng Guo, Zhongqi Li, Qi Zhang, Meng Xiao, Bo Shen, Lin Li, Hao Yu, Li Yan,
Pingyi Zhou, Xin Wang, Yuchi Ma, Ignacio Iacobacci, Yasheng Wang, Guangtai
Liang, Jiansheng Wei, Xin Jiang, Qianxiang Wang, and Qun Liu. 2022. PanGu-
Coder: Program Synthesis with Function-Level Language Modeling.
arXiv
preprint arXiv:2207.11280 (2022).
[9] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi,
Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2022. InCoder: A
Generative Model for Code Infilling and Synthesis. arXiv preprint arXiv:2204.05999
(2022).
[10] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang,
Guanting Chen, Xiao Bi, Y Wu, YK Li, et al. 2024. DeepSeek-Coder: When the
Large Language Model Meets Programming–The Rise of Code Intelligence. arXiv
preprint arXiv:2401.14196 (2024).
[11] Patrick Haluptzok, Matthew Bowers, and Adam Tauman Kalai. 2022. Language
Models Can Teach Themselves to Program Better. arXiv preprint arXiv:2207.14502
(2022).
[12] Yiyang Hao, Ge Li, Yongqiang Liu, Xiaowei Miao, He Zong, Siyuan Jiang, Yang
Liu, and He Wei. 2022. AixBench: A Code Generation Benchmark Dataset.
https://doi.org/10.48550/arXiv.2206.13179
[13] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora,
Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, and Jacob
Steinhardt. 2021. Measuring Coding Challenge Competence With APPS. In
Proceedings of the Neural Information Processing Systems Track on Datasets and
Benchmarks, Vol. 1.
[14] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 2019. The Curious
Case of Neural Text Degeneration. arXiv preprint arXiv:1904.09751 (2019).
[15] Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, and Luke Zettlemoyer. 2018.
Mapping Language to Code in Programmatic Context. arXiv:cs.CL/1808.09588
[16] Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettle-
moyer, Scott Wen tau Yih, Daniel Fried, Sida Wang, and Tao Yu. 2022. DS-
1000: A Natural and Reliable Benchmark for Data Science Code Generation.
arXiv:cs.SE/2211.11501
[17] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov,
Chenghao Mou, Marc Marone, Christopher Akiki, Jia Li, Jenny Chim, et al. 2023.
StarCoder: May the Source Be with You! arXiv preprint arXiv:2305.06161 (2023).
[18] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi
Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas
Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun
Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James
Molloy, Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando
de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. 2022. Competition-Level Code
Generation with AlphaCode. https://doi.org/10.48550/ARXIV.2203.07814
[19] Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu,
Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. 2023. WizardCoder:
Empowering Code Large Language Models with Evol-Instruct. arXiv preprint
arXiv:2306.08568 (2023).
[20] Naman Goyal Mike Lewis, Yinhan Liu. 2019. BART: Denoising Sequence-to-
Sequence Pre-training for Natural Language Generation, Translation, and Com-
prehension. https://doi.org/10.48550/arXiv.1910.13461
[21] Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Sil-
vio Savarese, and Caiming Xiong. 2022. A Conversational Paradigm for Program
Synthesis. arXiv preprint arXiv:2203.13474 (2022).
[22] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu:
a Method for Automatic Evaluation of Machine Translation. In Proceedings of
the 40th Annual Meeting of the Association for Computational Linguistics (ACL).
311–318. https://doi.org/10.3115/1073083.1073135

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

ICSE 2024, April 14–20, 2024, Lisbon, Portugal
Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie
[23] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. 2018. Im-
proving Language Understanding by Generative Pre-training. (2018).
[24] John Schulman, Barret Zoph, Christina Kim, Jacob Hilton, Jacob Menick, Jiayi
Weng, Juan Felipe Ceron Uribe, Liam Fedus, Luke Metz, Michael Pokorny, et al.
2022. ChatGPT: Optimizing Language Models for Dialogue. OpenAI blog (2022).
[25] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All
You Need. Advances in Neural Information Processing Systems 30 (2017).
[26] Thomas Wang, Adam Roberts, Daniel Hesslow, Teven Le Scao, Hyung Won
Chung, Iz Beltagy, Julien Launay, and Colin Raffel. 2022. What Language Model
Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?
arXiv preprint arXiv:2204.05832 (2022).
[27] Zhiruo Wang, Shuyan Zhou, Daniel Fried, and Graham Neubig. 2022. Execution-
Based Evaluation for Open-Domain Code Generation.
arXiv preprint
arXiv:2212.10481 (2022).
[28] Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. 2023.
Magicoder: Source code is all you need. arXiv preprint arXiv:2312.02120 (2023).
[29] Wei Zeng, Xiaozhe Ren, Teng Su, Hui Wang, Yi Liao, Zhiwei Wang, Xin Jiang,
ZhenZhang Yang, Kaisheng Wang, Xiaoda Zhang, Chen Li, Ziyan Gong, Yifan
Yao, Xinjing Huang, Jun Wang, Jianfeng Yu, Qi Guo, Yue Yu, Yan Zhang, Jin
Wang, Hengtao Tao, Dasen Yan, Zexuan Yi, Fang Peng, Fangqing Jiang, Han
Zhang, Lingfeng Deng, Yehong Zhang, Zhe Lin, Chao Zhang, Shaojie Zhang,
Mingyue Guo, Shanzhi Gu, Gaojun Fan, Yaowei Wang, Xuefeng Jin, Qun Liu, and
Yonghong Tian. 2021. PanGu-𝛼: Large-scale Autoregressive Pretrained Chinese
Language Models with Auto-parallel Computation. CoRR abs/2104.12369 (2021).
arXiv:2104.12369 https://arxiv.org/abs/2104.12369
[30] Qinkai Zheng, Xiao Xia, Xu Zou, Yuxiao Dong, Shan Wang, Yufei Xue, Lei Shen,
Zihan Wang, Andi Wang, Yang Li, et al. 2023. Codegeex: A pre-trained model for
code generation with multilingual benchmarking on humaneval-x. In Proceedings
of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining.
5673–5684.

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Evaluation/primary/CoderEval/page-12.png)
