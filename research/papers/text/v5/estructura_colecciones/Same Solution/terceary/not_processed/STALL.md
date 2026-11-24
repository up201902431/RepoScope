# STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis

- source_pdf: ../../../../../../pdf/Same%20Solution/terceary/not_processed/STALL.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

STALL+: Boosting LLM-based Repository-level Code Completion with
Static Analysis
JUNWEI LIU, Fudan University, China
YIXUAN CHEN, Fudan University, China
MINGWEI LIU, Sun Yat-sen University, China
XIN PENG∗, Fudan University, China and Shandong Key Laboratory of Complex Network Software Automatic
Construction Technology, China
YILING LOU, University of Illinois Urbana-Champaign, USA
Repository-level code completion refers to the challenging completion scenario involving complicated contexts from multiple
files in a repository. To date, researchers have proposed two technical categories to enhance LLM-based repository-level
code completion: retrieval-augmented generation (RAG) and static analysis integration. This work performs the first study
on static analysis integration in LLM-based repository-level code completion by investigating integration strategies across
different phases. We first implement a framework STALL+, which supports extensible, customizable integration of multiple
static analysis strategies into the full pipeline of LLM-based repository-level code completion. Based on STALL+, we conduct
extensive experiments including different LLMs on the latest repository-level code completion benchmark CrossCodeEval.
Our findings show that integrating file-level dependencies in the prompting phase performs best, while post-processing phase
integration performs worst. Additionally, we observe different improvements between dynamic and static languages, i.e., the
best combination is prompting-phase with decoding-phase integration for Java, and prompting-phase with post-processing-
phase integration for Python due to limitations in statically analyzing dynamic languages. We also find complementarity
between RAG and static analysis integration, and that prompting-phase integration is more cost-effective than RAG.
CCS Concepts: • Software and its engineering; • Computing methodologies →Machine learning;
Additional Key Words and Phrases: Large Language Model, Repository-level Code Completion, Static Analysis, Retrieval-
Augmented Generation
1
Introduction
Code completion techniques generate code for the given contexts (e.g., natural language descriptions or incomplete
code snippets), which have been widely adopted in practical programming activities and substantially increase
development productivity [39, 70, 71]. Recent advances in large language models (LLMs), further boost the
progress in this domain [26, 32, 44, 87]. Having been pre-trained on massive code corpora, code LLMs exhibit
strong effectiveness in code completion.
∗Corresponding author
Authors’ Contact Information: Junwei Liu, jwliu24@m.fudan.edu.cn, Fudan University, Shanghai, China; Yixuan Chen, yixuanchen23@m.fu-
dan.edu.cn, Fudan University, Shanghai, China; Mingwei Liu, liumw26@mail.sysu.edu.cn, Sun Yat-sen University, Guangzhou, China; Xin
Peng, pengxin@fudan.edu.cn, Fudan University, Shanghai, China and Shandong Key Laboratory of Complex Network Software Automatic
Construction Technology, Shandong, China; Yiling Lou, yilingl@illinois.edu, University of Illinois Urbana-Champaign, Illinois, USA.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that
copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy
otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org.
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1557-7392/2026/9-ART
https://doi.org/10.1145/3846180
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 1](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-01.png)

![Página PDF 1, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

2
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Previously, the majority of code completion work [24, 30, 54] focuses on code completion within a small-
scale and isolated context (i.e., a single file). For example, coding tasks in widely-used benchmarks (such as
HumanEval [17] and MBPP [11]) expect to generate code mainly based on the context of the current file. However,
real-world code completion is often associated with a broader repository-level context [81]. In such scenarios
(i.e., repository-level code completion), the code in the target file (i.e., the file with unfinished code for completion)
may depend on code contexts (e.g., classes or methods) declared in other files of the repository. Unlike previous
code completion only taking the target file as input, repository-level code completion takes not only the target
file but also the entire repository as input.
Compared to code completion within a single file, applying LLMs for repository-level code completion is more
challenging. First, generating code dependent on other files of the repository is a more restricted task for LLMs.
While most LLMs are pre-trained on public code corpora, they are less aware of infrequent token distributions
within certain repositories. Therefore, LLMs are more likely to exhibit hallucinations when generating tokens that
are less commonly seen in their pre-training data [58]. Previous work [21] shows that state-of-the-art code LLMs
perform much poorer when generating code dependent on other local files. Second, the overwhelming scale of
the repository makes it infeasible to feed the complete repository-level context into LLMs due to their limited
input length and poorer performance with longer inputs [46]. As a result, only a portion of repository-level
context can be utilized by LLMs, potentially leading to non-optimal effectiveness.
To address the issues above, researchers have proposed two categories of techniques to boost LLM-based
repository-level code completion. The first category is to enhance LLM-based repository-level code completion
via Retrieval-Augmented Generation (RAG) techniques [79, 85]. In particular, RAG-based techniques first leverage
a retrieval mechanism to fetch similar code snippets from the repository, and then include the retrieved code
snippets in the input prompt. The prompts augmented with similar code examples facilitate more accurate
LLM-based code completion via few-shot learning and in-context learning [14]. The second category is to
enhance LLM-based repository-level code completion with static analysis. In particular, existing techniques
mainly integrate static analysis in two phases, i.e., (i) integrating static analysis in the prompting phase by
extracting useful code contexts from other files via static analysis [22, 47] and (ii) integrating static analysis in
the decoding phase by adjusting the model-predicted token probabilities guided by static analysis [9, 74]. While
the RAG category enhances LLMs with similar code in the repository, static analysis equips LLMs with additional
capabilities of code analysis.
Although showing promise in existing work, the effectiveness of static analysis on boosting LLM-based
repository-level code completion has not been systematically explored. First, the effectiveness and efficiency of
existing static analysis integration strategies have not been compared, leaving it unclear which strategy performs
the best. Second, existing integration strategies have not covered the complete pipeline of code completion, only
including the prompting phase and the decoding phase without including the phase after the model inference
(i.e., the post-processing phase), leaving it unclear how integrating static analysis in different inference phases
performs. Third, existing work only focuses on the effectiveness of individual integration strategy, leaving it
unclear how the different integration strategies are complementary to each other. Fourth, it is still unclear how
the two mainstream enhancement categories in LLM-based repository-level code completion (i.e., static analysis
integration versus RAG) perform compared to each other and whether they are complementary. In summary, it
still lacks a comprehensive evaluation on the existing progress and the potential of integrating static analysis
into LLM-based repository-level code completion.
To fill such a knowledge gap, in this work, we perform the first study on the static analysis integration
in LLM-based repository-level code completion by investigating static analysis integration strategies across
different phases of code completion. In particular, we make the first attempt to explore (i) the effectiveness and
efficiency of each individual integration strategy, (ii) the complementarity among different strategies based on
their combination, and (iii) the comparison and combination with existing RAG techniques.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 2](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-02.png)

![Página PDF 2, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
3
To facilitate a comprehensive evaluation, we first examine existing approaches that integrate static analysis
with code completion, which mainly follow two strategies: retrieving APIs from imported modules and removing
non-existent API tokens during decoding. To further push the boundaries of this research area, we additionally
propose a prompting strategy that directly inserts candidate APIs into the code context, as well as a post-processing
strategy that determines the final output through static checking after code generation. Finally, we propose
a framework STALL+, which supports an extensible and customizable integration of multiple static analysis
strategies into the complete pipeline of LLM-based repository-level code completion. In particular, STALL+ can
integrate static analysis along the prompting phase (before model inference), the decoding phase (during model
inference), and the post-processing phase (after model inference). Additionally, STALL+ is not only extensible for
different static analysis strategies and their combination, but also compatible with RAG techniques.
Based on our framework STALL+, we perform extensive experiments by including three state-of-the-art code
LLMs (i.e., DeepSeek-Coder-6.7B, StarCoderBase-7B, and CodeLlama-7B) and several general-purpose LLMs (i.e.,
Claude-Sonnet-4.5, Qwen3-Coder-30B-A3B-Instruct, DeepSeek-7B, Llama2-7B) on the latest repository-level code
completion benchmark CrossCodeEval, which includes 2,075/2,460 code completion tasks of both static language
Java and dynamic language Python. Based on our experimental results, we have the following main findings. First,
integrating static analysis in any phase of code completion can improve repository-level code completion, while
the prompting phase with file-level dependencies performs the best and the post-processing phase performs
the worst. Second, combining multiple integration strategies can bring further improvements, and different
strategies exhibit different complementarity (e.g., the prompting phase with token-level dependencies shares the
smallest complementarity with decoding-phase integration). In particular, integrating static analysis for dynamic
language or static language exhibits different improvements, e.g., the best combination is prompting-phase with
decoding-phase for Java, while the best combination is prompting-phase with post-processing-phase for Python
given the limitations of statically analyzing dynamic languages. Third, in our evaluation settings, static analysis
integration in the prompting phase is overall more efficient and effective than existing RAG-based strategies in
repository-level code completion, and combining them can further achieve the best accuracy. Finally, we provide
practical discussions informed by the experimental results, including: (i) we explore strategies for mitigating the
negative impact of static analysis errors on dynamic languages and propose a lightweight approach by training a
logistic regression model to decide whether to trust static analysis outputs; (ii) we analyze language features that
may influence static analysis integration strategies; (iii) we summarize practical implications for future work,
such as designing more flexible integration strategies. In summary, this work makes the following contributions:
• We perform the first study on the static analysis integration strategies across different phases of LLM-based
repository-level code completion.
• We propose and implement a framework, STALL+, which incorporates both existing static-analysis integration
strategies and two novel strategies, providing an extensible and customizable pipeline for integrating multiple
static analysis techniques into LLM-based repository-level code completion.
• Our study reveals insightful findings and practical implications on static analysis integration, including the
most effective strategy, the most efficient strategy, the combination and complementarity between static
analysis and RAG, the potential to mitigate the impact of inaccurate static analysis, and the future directions
for designing more powerful static analysis integration strategies. Our replication package is at [7].
2
Background
2.1
Code LLMs
Large language models (LLMs) such as Llama [68] and ChatGPT [2], are large-scale Transformer models with
hundreds of billions of parameters. Recently LLMs have made significant progress and been applied across various
domains [44, 45, 73]. Code LLMs are specifically trained on code corpus, showcasing strong capabilities in code
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 3](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-03.png)

![Página PDF 3, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

4
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
generation and code comprehension. Many LLMs (e.g., CodeGen [56], StarCoder [41], and Code Llama [60]),
have been widely applied in code-related tasks, such as code completion [23, 24, 82], test generation [20, 37], and
program repair [12, 18, 53, 59].
2.2
Repository-level Code Completion
Repository-level code completion [9, 21, 85] focuses on completing unfinished code based on the context of
the entire repository. Unlike traditional code completion tasks that consider only the target file (i.e., the file
with unfinished code to be completed), repository-level code completion takes the entire repository as input.
The output typically consists of completed code that may depend on other files within the repository, such
as invoking methods declared in other files. Compared to code completion within a small-scale and isolated
context (e.g., within a single file [11, 17, 24]), repository-level code completion is considered a more realistic
scenario, as files in real-world software development often depend on each other. However, repository-level
code completion has shown to be more challenging than code completion within the single-file context [21].
Researchers have proposed various techniques to enhance LLMs performance in repository-level code completion,
which broadly fall into two categories: (i) Retrieval-Augmented Generation (RAG) [79, 85] and (ii) static analysis
integration [9, 74].
RAG-based techniques focus on the prompting phase of LLM-based code completion. They retrieve code snippets
that are similar to the unfinished one from the repository and include them in the input prompt. The main insight
of RAG-based techniques is to leverage the few-shot learning and in-context learning capabilities of models
by providing similar code examples as hints [14]. However, when no similar code snippets are available in the
repository (i.e., the code to be complete is almost unique), RAG-based techniques can become less effective [21].
Static analysis integration techniques enhance LLMs with the code analyzing and checking capabilities of static
analysis. Existing techniques mainly integrate static analysis in two phases: (i) the prompting phase (before the
model inference), which utilizes static analysis to extract useful/dependent code contexts from other files and
then prepends them into the current context [22, 47]; (ii) the decoding phase (during the model inference), which
utilizes static analysis to extract valid tokens (e.g., method names) on the fly and then based on them adjusts the
model-predicted token probabilities [9, 74]. This category enhances LLMs by equipping them with additional
capabilities from external tools (i.e., static analyzers).
3
Integration Framework for Static Analysis
In this section, we present our framework, STALL+, which enables an extensible and customizable integration of
static analysis throughout the pipeline of LLM-based repository-level code completion. As shown in Figure 1,
STALL+ can individually or simultaneously integrate static analysis into the following three phases along the
pipeline of model inference.
• Prompting Phase. Before model inference, static analysis can be integrated to provide relevant code contexts
(e.g., extracting code dependencies) for the input prompt.
• Decoding Phase. During model inference, static analysis can be integrated to adjust the probability of tokens
predicted by models on the fly.
• Post-processing Phase. After model inference, static analysis can be integrated to filter and re-rank the
model-generated code candidates.
The integration in these three phases is theoretically orthogonal and can be combined with each other by
simultaneously applying them during code completion. In particular, STALL+ is customizable for selectively
activating one or multiple specified integration strategies, and it is also extensible as new integration strategies
of these three phases can be easily plugged into the framework. We then explain the integration strategies of
each phase in detail.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 4](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-04.png)

![Página PDF 4, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
5
Fig. 1. Overview of the STALL+ static analysis integration framework.
3.1
Integration in Prompting Phase
One key challenge of repository-level code completion is that the unfinished code might depend on code located
beyond the current file (e.g., method invocations declared in other files of the repository) [9, 21]. Therefore, given
the unfinished code, static analysis can extract code dependencies from other files of the repository. The extracted
cross-file code contexts can then be prepended to the current file context in the prompt, providing hints to LLMs
with potentially relevant code ingredients. Specifically, our framework currently includes two granularities of
code dependencies extracted by static analysis: file-level or token-level dependencies.
• File-level Dependency Analysis. This coarse-grained strategy focuses on file-level dependencies by analyzing
the import statements of the current file. It is also a common strategy used in existing repository-level code
completion techniques (e.g., RLPG [64] and CoCoMIC [22]). Specifically, given the unfinished code, we first
leverage static analysis to extract the import statements in its current file and then extract all the classes and
methods from these imported files. Given the limited input length of LLMs and to avoid overwhelming LLMs
with massive contexts, we organize the key information hierarchically, i.e., (i) for each module, we include its
classes, methods, and variables, (ii) for each class, we include its class signature, member variable names, and
member methods, and (iii) for each method, we include its method signature. The “File-level Dependency” in
Figure 1 provides an example.
• Token-level Dependency Analysis. File-level dependency collects information from imported modules
without filtering. However, in practice, programmers in an IDE typically receive candidate APIs only at the
current completion position via the language server. To better simulate this realistic scenario, we propose a novel
prompting-phase integration strategy based on token-level dependency. In particular, given the unfinished
code, we leverage static analysis to extract the list of method names and variable names that are valid at the
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 5](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-05.png)

![Página PDF 5, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

6
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
completion position and insert them before the target line. The “Token-level Dependency” in Figure 1 presents
an example.
3.2
Integration in Decoding Phase
Static analysis can be integrated into the auto-regressive decoding procedure by on-the-fly restricting the model’s
output to only valid tokens with static checking. We define a binary mask over the vocabulary indicating which
tokens are allowed. The original logits are modified by setting the logits of invalid tokens to -inf, ensuring
they receive zero probability after softmax. The next token is then selected based on this masked probability
distribution. The detailed process is formulated as follows.
Given the input token sequence in the current iteration (𝑥1, 𝑥2, … , 𝑥𝑛), the model generates a vector of
𝑙𝑜𝑔𝑖𝑡𝑠= (𝑙1, 𝑙2, … , 𝑙𝐾) for 𝐾potential next tokens, where 𝐾is the size of the vocabulary. In the auto-regressive
greedy decoding procedure, the next token 𝑥𝑛+1 is decoded based on the Top-1 probability computed with the
softmax and 𝑎𝑟𝑔𝑚𝑎𝑥function:
𝑥𝑛+1 = arg max
𝑘(softmax(𝑙𝑜𝑔𝑖𝑡𝑠))
(1)
To incorporate static analysis into this procedure, we leverage static analysis to obtain all available variables
and APIs (e.g., the method names, variable names, and parameter names that have been defined) at the current
position, and the token which is a subsequent token of any returned variables or APIs would be considered as
valid. For example, if setUser and getUser are available APIs, then set and get are considered valid tokens in
the first turn, and User becomes the only valid token in the second turn. In particular, for cases that static analysis
returns nothing, all tokens would be judged as valid in this iteration. The vector 𝑣𝑎𝑙𝑖𝑑= (𝑣1, 𝑣2, … , 𝑣𝐾) indicates
whether each token in the vocabulary is valid, where 𝑣𝑘= 1 if the 𝑘-th token is valid and 𝑣𝑘= 0 otherwise.
Subsequently, the original logits vector 𝑙𝑜𝑔𝑖𝑡𝑠can be adjusted into 𝑙𝑜𝑔𝑖𝑡𝑠+, where
𝑙𝑜𝑔𝑖𝑡𝑠+ = (𝑙′
1, 𝑙′
2, … , 𝑙′
𝐾) = 𝑙𝑜𝑔𝑖𝑡𝑠⊕𝑣𝑎𝑙𝑖𝑑= (𝑙1, 𝑙2, … , 𝑙𝑘) ⊕(𝑣1, 𝑣2, … , 𝑣𝑘)
(2)
⊕defines element-wise for vectors 𝑙𝑜𝑔𝑖𝑡𝑠and 𝑣𝑎𝑙𝑖𝑑, where 𝑙′
𝑘= 𝑙𝑘if 𝑣𝑘= 1 and 𝑙′
𝑘= −𝑖𝑛𝑓otherwise.
Equation 1 is then updated by replacing 𝑙𝑜𝑔𝑖𝑡𝑠with 𝑙𝑜𝑔𝑖𝑡𝑠+:
𝑥𝑛+1 = arg max
𝑘(softmax(𝑙𝑜𝑔𝑖𝑡𝑠+))
(3)
After being processed by softmax function, the probability of all invalid tokens is set as zero, thus being
excluded in the current iteration of token generation.
Figure 1 shows how this integration strategy works. Compared to the prompting phase, integration in decoding
assigns more dominance to static analysis, as its returned information directly changes the generating probabilities
of tokens. Although previous work (i.e., MGD [9]) has explored the similar integration strategy in the decoding
phase, they are only applied in selective positions (e.g., API invocations); STALL+ further extends the strategy to
all token positions during generation.
3.3
Integration in Post-processing Phase
Incorporating static analysis in the prompting and decoding phases cannot fully ensure the correctness of the
output due to the nondeterministic nature and the limited interpretability of model inference. A potential solution
is to check whether the generated code passes syntactic validation during the post-processing phase. However,
to the best of our knowledge, there is no existing work that integrates static analysis into the post-processing
phase in the repository-level code completion scenario. To address this gap, we propose a straightforward
post-processing integration strategy. In particular, given unfinished code, we first collect a ranked list of code
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 6](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-06.png)

![Página PDF 6, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
7
candidates generated by LLMs using beam search (i.e., asking LLMs to generate the top-k most likely code
candidates); then for each generated code candidate, we put it back to the unfinished code and check whether
the concatenated code can pass the static checking within the repository context, i.e., no syntactical errors are
reported by the static analyzer; lastly, the invalid code candidates are removed from the list and the first code
candidate that can pass the static checking is returned as the final output. In addition, if all the code candidates
fail the static checking, we return the original Top-1 candidate generated by LLMs. Figure 1 shows how this
integration strategy works.
4
Experiment Setup
Based on our framework STALL+, we aim to investigate to what extent static analysis integration strategies can
improve the accuracy of repository-level code completion, and compare the effectiveness and efficiency of static
analysis integration strategies with the RAG strategy. The study begins with a formulation of the primary research
questions, followed by a detailed introduction of the studied benchmark, code LLMs, baseline approaches, and
the evaluation metrics for assessing repository-level code completion performance. Finally, we introduce the
detail for prompt construction, static analysis, and our experimental environment.
4.1
Research Questions
We design the following research questions to explore the effectiveness and efficiency of integrating static analysis
strategies in repository-level code completion.
• RQ1 (Individual Integration Strategy): How does each static analysis integration strategy perform
in LLM-based repository-level code completion? To answer RQ1, we separately test the static analysis
integration strategies mentioned in Section 3 and compare their performance with the basic prompting strategy
that includes merely in-file context.
• RQ2 (Combined Integration Strategies): How do different combinations of integration strategies
affect LLM-based repository-level code completion? Since the static analysis integration strategies across
different phases are orthogonal to each other, we explore the complementarity between them by combining
static analysis integration strategies across different phases, and compare the performance of the combined
approach with that of the better-performing individual strategy within the combination.
• RQ3 (Compared with RAG): How do static analysis integration strategies perform compared to RAG
in LLM-based repository-level code completion?
– RQ3.a (Effectiveness) How is the accuracy of static analysis integration compared to RAG? We
compare the performance of static analysis integration strategies (both individual and combined integration
strategies) with the RAG strategy. To explore the potential compatibility between these two distinct strategies,
we also combine static analysis integration strategies and the RAG strategy.
– RQ3.b (Efficiency) How are the online costs of static analysis integration compared to RAG? To
answer RQ3.b, we measure and compare the inference overhead of all static analysis integration strategies
and RAG to explore their efficiency.
• RQ4 (Generalization): How do static analysis integration strategies and RAG-based strategies perform
in LLM-based repository-level code completion on larger-scale and general-purpose LLMs? To answer
RQ4, we separately test the static analysis integration strategies and RAG-based strategies using larger-scale
and general-purpose LLMs and compare their performance with the baseline that includes merely the in-file
context.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 7](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-07.png)

![Página PDF 7, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

8
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
4.2
Benchmark
We choose the CrossCodeEval [21] benchmark for the following reasons. First, it is the latest repository-level
code completion benchmark, constructed from GitHub projects spanning from March 5, 2023, to June 15, 2023.
This timeframe helps mitigate data leakage issues by excluding training data from many existing code LLMs
released before mid-2023. Second, CrossCodeEval is a more challenging benchmark exclusively focusing on
code completion with cross-file dependencies. As shown in previous work [21], LLMs exhibit much poorer
performance on CrossCodeEval than on other benchmarks such as RepoEval [85]. Third, CrossCodeEval is
broadly collected across diverse repositories and programming languages, reducing selection bias and enhancing
its representativeness for real-world code completion tasks. In particular, the granularity of code completion tasks
in CrossCodeEval is line level, i.e., completing the current unfinished line within the repository-level context.
Line completion is one of the most frequent code completion scenarios expected by developers in practice [72],
and has been widely studied in previous repository-level code completion work [21, 22, 47, 64].
Studied Programming Languages. We focus on repository-level code completion for two languages, i.e., Java
and Python, to cover representative static and dynamic languages and explore the potentially different impacts
of static analysis on different types of programming languages. Besides, these languages have been widely used
and studied in previous repository-level code completion work [21, 47, 64, 85]. Specifically, we adopt the Java
and Python repository-level code completion tasks in the CrossCodeEval benchmark. Detailed statistics of the
benchmark are provided in Table 1. Note that the scale of the benchmark slightly reduces compared to the original
CrossCodeEval (e.g., from 239 Java repositories to 230 Java repositories) due to the removal of invalid data items
from non-existent repositories or with non-existent modules imported.
Table 1. Benchmark statistics
Language
Python
Java
# Repo.
450
230
# Examples
2,460
2,075
Avg. # prompt lines
92
107
Avg. # prompt tokens
1,119
1,194
Avg. # reference tokens
14
16
4.3
Studied LLMs
We select three state-of-the-art code LLMs in our main experiments, i.e., StarCoderBase-7B [41], CodeLlama-
7B [60], and DeepSeek-Coder-6.7B [31], for the following reasons. First, they are trained on data predating March
2023 and the repositories in CrossCodeEval are created between March 5 and June 15, 2023 [21], which can
mitigate data leakage issues. Second, their input window size is at least 8,000 tokens, which can support the
massive cross-file code contexts involved in repository-level code completion. Third, these code LLMs have been
widely used in previous repository-level code completion work [21, 31, 74, 79] and shown advanced effectiveness.
In particular, we mainly focus on the 6B-7B versions of these models given the cost-effectiveness balance. For
generalization experiments, we select larger-scale and general-purpose LLMs including Claude-Sonnet-4.5,
Qwen3-Coder-30B-A3B-Instruct, DeepSeek-7B, and Llama2-7B.
4.4
Studied Baselines
According to previous work [21], we include the following two repository-level code completion baselines:
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 8](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-08.png)

![Página PDF 8, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
9
• In-file Generation is a default strategy including only the code preceding to the unfinished code into the
prompt, which is the most common baseline widely included in repository-level code completion studies [21,
22, 47, 63, 85].
• RAG is another mainstream approach for enhancing LLM-based repository-level code completion [79, 85]. We
select three RAG based approaches as baselines, including Naive RAG, RepoCoder [85], and Repoformer [79].
Naive RAG performs single-round retrieval augmented generation. RepoCoder conducts an additional round of
retrieval and generation based on the code produced by Naive RAG. Repoformer is a selective RAG framework
to enable a code LM to accurately self-evaluate whether to conduct retrieval by self-supervised learning.
As for the existing techniques that leverage static analysis for LLM-based repository-level code completion
(e.g., MGD [9] and ToolGen [74]), they are actually embraced (or even extended) in our framework. Thus, we do
not list them as separate baselines here. Additionally, we do not include CoCoMIC [22] or RLPG [64] due to the
unreleased implementation or expensive adaption to the new language (missing training data of new language
for RLPG).
4.5
Metrics
In code completion scenarios, the generated code is often incomplete and cannot undergo testing. Therefore,
similarity-based metrics, rather than test-based ones (e.g., pass@k), are most commonly used for evaluation.
Following previous work [21, 85], we adopt the following four similarity-based metrics to evaluate the effectiveness
of different repository-level code completion techniques.
• Code Match. These metrics evaluate the similarity between the entire generated code and the ground truth:
– Line Exact Match (Line EM) measures the percentage of generated code that exactly matches the ground
truth.
– Line Edit Similarity (Line ES) calculates the Levenshtein distance between the generated code and ground
truth [38].
• Identifier Match. These metrics assess the accuracy of generating correct APIs by comparing identifiers in
the generated code with those in the ground truth.
– Identifier Exact Match (ID EM) measures the percentage of generated code with the same identifiers as
ground truth.
– Identifier F1 (ID F1) is the F1 score of the identifiers in the generated code against the ground truth.
In addition, to avoid merely relying on similarity-based metrics, we included a Compilation Rate metric for
the Java subset, by calculating the ratio of predictions that can lead to a successful compilation in the original
repository.
4.6
Implementations
Prompt Construction. The static analysis contexts are detailed in Section 3.1. For constructing retrieval
contexts, we follow the settings in prior RAG-based code completion [85], which partitions the repository code
using a sliding window with a line length of 20 and a sliding size of 10. We adopt lexical-based similarity,
specifically Jaccard similarity [35], to calculate the similarity between different code snippets during retrieval.
We do not use deep learning-based retrievers (e.g., CodeBERT [27]), as previous studies [21, 85] show no
significant effectiveness difference between lexical-based and deep learning-based retrievers in repository-level
code completion. Furthermore, we include 3 retrieved code snippets into the prompt, as recent research [16]
indicates that 1 or 2 shots can already yield notable improvement, while 4 or more shots lead to limited increases
or even decreases in performance. Given the limited input size of 8,000 tokens and the average prompt token
length in the benchmark being less than 2,000 (i.e., 1,194/1,119 for Java/Python), we truncate the in-file context
to 2,000 tokens and truncate each cross-file context to 3,000 tokens. This ensures adequately and equally sized
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 9](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-09.png)

![Página PDF 9, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

10
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Table 2. Results of individual integration strategies. “Prompt-F”/“Prompt-T” denotes the prompting-phase integration with
file-level/token-level dependencies, “Decode” denotes the decoding-phase integration, and “Post” denotes the post-processing-
phase integration. The numbers in parentheses show the relative improvement over in-file generation.
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
DeepSeek-Coder
6.7B
In-file
9.02
62.51
15.45
48.00
26.7
73.38
34.36
58.62
63.18
Prompt-F 27.80(↑208.2%)§0.19 72.64(↑16.2%)§0.25 36.75(↑137.9%)§0.21 64.94(↑35.3%)§0.27 44.24(↑65.7%)§0.18 80.33(↑9.5%)§0.20 53.25(↑55.0%)§0.19 73.19(↑24.9%) §0.22 84.82(↑34.3%)§0.22
Prompt-T 24.84(↑175.4%)§0.16
69.89(↑11.8%)§0.18
33.94(↑119.7%)§0.19
61.70(↑28.5%)§0.22
38.65(↑44.8%)§0.12
76.95(↑4.9%)§0.11
47.18(↑37.3%)§0.13
68.42(↑16.7%)§0.15
75.23(↑19.1%)§0.12
Decode
16.02(↑77.6%)§0.07
63.92(↑2.3%)§0.03
23.37(↑51.3%)§0.08
54.30(↑13.1%)§0.10
33.11(↑24.0%)§0.07
74.34(↑1.3%)§0.04
41.45(↑20.6%)§0.07
64.49(↑10.0%)§0.09
74.17(↑17.4%)§0.11
Post
11.54(↑27.9%)§0.03
63.39(↑1.4%)§0.02
17.36(↑12.4%)§0.02
49.44(↑3.0%)§0.02
30.36(↑13.7%)§0.04
73.63(↑0.3%)†0.02
38.07(↑10.8%)§0.04
60.96(↑4.0%)§0.04
70.80(↑12.1%)§0.08
StarCoderBase
7B
In-file
6.38
60.82
13.17
45.53
23.61
72.22
32.24
56.95
62.12
Prompt-F 23.58(↑269.6%)§0.17 69.78(↑14.7%)§0.22 32.20(↑144.5%)§0.19 61.35(↑34.7%)§0.25 40.19(↑70.2%)§0.17 78.90(↑9.2%)§0.19 50.60(↑57.0%)§0.19 71.23(↑25.1%)§0.22 82.65(↑33.0%)§0.21
Prompt-T 20.28(↑217.9%)§0.14
66.31(↑9.0%)§0.13
28.62(↑117.3%)§0.15
56.49(↑24.1%)§0.17
34.51(↑46.2%)§0.11
75.72(↑4.8%)§0.11
44.19(↑37.1%)§0.12
66.09(↑16.0%)§0.14
74.65(↑20.2%)§0.13
Decode
13.09(↑105.2%)§0.07
62.21(↑2.3%)§0.03
20.73(↑57.4%)§0.08
52.13(↑14.5%)§0.11
30.89(↑30.8%)§0.08
73.75(↑2.1%)§0.05
39.90(↑23.8%)§0.08
63.37(↑11.3%)§0.10
72.87(↑17.3%)§0.11
Post
7.73(↑21.2%)§0.01
60.32(↓0.8%)†0.01
13.70(↑4.0%)𝑛𝑠0.01
45.78(↑0.5%)𝑛𝑠0.00
26.12(↑10.6%)§0.03
72.46(↑0.3%)†0.02
34.89(↑8.2%)§0.03
58.20(↑2.2%)§0.02
67.57(↑8.8%)§0.05
CodeLlama
7B
In-file
7.20
60.69
13.94
45.62
25.59
72.85
33.45
57.97
62.89
Prompt-F 23.94(↑232.5%)§0.17 69.77(↑15.0%)§0.22 33.01(↑136.8%)§0.19 61.18(↑34.1%)§0.24 41.25(↑61.2%)§0.16 78.79(↑8.2%)§0.17 50.99(↑52.4%)§0.18 71.12(↑22.7%)§0.20 82.89(↑31.8%)§0.20
Prompt-T 21.46(↑198.1%)§0.15
67.34(↑11.0%)§0.16
30.33(↑117.6%)§0.16
58.11(↑27.4%)§0.20
33.35(↑30.3%)§0.08
74.95(↑2.9%)§0.07
42.46(↑26.9%)§0.09
64.82(↑11.8%)§0.10
73.78(↑17.3%)§0.11
Post
8.87(↑23.2%)§0.02
60.47(↓0.4%)𝑛𝑠0.00
14.92(↑7.0%)†0.01
45.84(↑0.5%)𝑛𝑠0.00
27.66(↑8.1%)§0.02
72.63(↓0.3%)𝑛𝑠0.01
35.47(↑6.0%)§0.02
58.73(↑1.3%)†0.02
67.08(↑6.7%)§0.04
Note: Superscripts indicate statistical significance and effect size. § (p < 0.001), ‡ (p < 0.01), † (p < 0.05), 𝑛𝑠(not significant). (Wilcoxon test). The
number following the 𝑝-value symbol is the Cliff’s 𝛿value. The same notation is used for following tables.
input windows for different prompting-phase integration techniques, facilitating fair comparison among different
strategies. All contexts are subsequently combined into the prompt, as depicted in Figure 1.
Static Analysis Details. In the prompting phase, we adopt the widely-used toolkit tree-sitter [8] for Java and
the internal ast module for Python to parse the code into abstract syntax trees (AST) for import statement
identification. We adopt well-established language servers (i.e., Jedi [4] for Python and Eclipse JDT [3] for Java) to
extract code elements and obtain the list of valid tokens. To reduce the online costs during code completion, we
initially parse each repository to index dependencies in advance. This list of valid tokens will also be utilized to
adjust the probability of LLM-predicted tokens in the decoding phase as shown in Figure 1. In the post-processing
phase, we adopt the static analyzers (e.g., Pylint [5] for Python and native javac for Java) to check the correctness
of the generated code. For efficiency, we only perform incremental compilation (i.e., only the modified file
associated with its imported files would be compiled rather than the entire project), taking less than one second.
Note that the implementation of STALL+ is not language-specific as different language features are directly
handled by these adopted static analysis tools.
Experimental Details. We acquire all models directly from their official open-source repositories. We employ
the default greedy-decoding strategy without sampling since previous work [21] has illustrated the marginal
differences between them in similar repository-level line completion scenarios. In the post-processing phase,
we employ beam search to generate multiple candidate predictions, with a beam size of 3. This setting follows
common practices in prior work [25, 33] and is further supported by our preliminary experiments, striking a
balance between prediction accuracy and computational efficiency. Furthermore, dataset statistics indicate that
the maximum ground-truth sequence length is 51 tokens for Python and 87 tokens for Java, with 99% of Java
samples containing no more than 35 tokens. In addition, we consider hardware efficiency: modern GPUs achieve
higher throughput when tensor dimensions are aligned with powers of two, leading to improved parallelism
and resource utilization [43, 57]. Based on these observations, we set max_new_tokens to 64, which sufficiently
covers nearly all cases while avoiding unnecessary computational overhead. Finally, we define the termination
condition of the generation process as the emission of the first newline token, which prevents excessively long
outputs and enables accurate measurement of the time required to complete the target line. All experiments are
conducted on a server with the Ubuntu 20.04.6 LTS operating system and equipped with eight A800-80G GPUs.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 10](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-10.png)

![Página PDF 10, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
11
5
Results
5.1
RQ1: Individual Integration Strategy
Table 2 presents the effectiveness of each individual integration strategy. In particular, we skip the decoding-phase
integration on CodeLlama-7B, as its SentencePiece [6] tokenizer escapes whitespace and the beginning of each
word with a meta symbol “_”(U+2581). Therefore, each token is encoded with the meta symbol before it (e.g., the
first token of “sendMessage” will be “_send” instead of “send”); As only “_send” is reserved during decoding,
there will be a whitespace before each token after detokenization (e.g., “ send Message”). The whitespace cannot
be directly removed as it is hard to distinguish whether it is a whitespace or the beginning of a word. From the
table, we have the following observations.
Comparison among different strategies. Overall, we find that all the static analysis integration strategies
can individually improve the basic capabilities of three studied LLMs in repository-level code completion. For
example, compared to in-file generation, the studied LLMs achieve 21.2% - 269.6% line EM improvements in
Python and 8.1% - 70.2% line EM improvements in Java, which aligns with the reported improvements in prior
work [9, 22, 64, 74]. In addition, all improvements for line EM are statistically significant (p <0.001).
In particular, we find that integrating static analysis in the prompting phase (both file-level dependency
analysis and token-level dependency analysis) can achieve much larger improvements than integration in other
phases; meanwhile integrating in the post-processing phase achieves the smallest improvements. For example,
for DeepSeek-Coder-6.7B on Python, integrating static analysis in the prompting phase leads to 208.2%/175.4%
improvements (file-level/token-level dependency analysis) in line EM, while integration in decoding or post-
processing phases only has 77.6% or 27.9% improvements in line EM. One reason might be that including the
relevant tokens before inference can better guide LLMs to be aware of these tokens and assign higher probabilities
to them during the following inference. Figure ⁇ shows an example that the prompting-phase integration
can help DeepSeek-Coder generate the correct code with the API name, but the decoding-phase integration
or the post-processing integration cannot. When prompted with only the in-file context, the model tends to
predict the local API “normalize”. When utilizing the decoding-phase integration strategy, although it retains
the “strip” token, the model does not assign enough probability (only 0.06) to it, which is still surpassed by the
token “normalize” as it is also valid and with higher probability. Unlike previous work [9, 22, 64, 74], which only
reported the improvements from integrating static analysis at an individual phase, our study benefits from the
STALL+ framework, which supports multi-phase static analysis integration and enables a more comprehensive
comparison of the improvements of different static analysis integration strategies. As a result, we are able to
conclude that prompting-phase integration strategies yield greater improvements than strategies that integrate
static analysis at other phases.
From the perspective of Compilation Rate, all integration strategies exhibit similar differences to those observed
with similarity metrics. Notably, although prompting-phase integration with token-level dependencies achieves a
significantly higher line EM than decoding-phase integration, their Compilation Rates remain very close (e.g.,
74.17 vs. 75.23 for DeepSeek-Coder), since decoding-phase integration only generates APIs that already exist in
the repository, increasing the likelihood of successful compilation.
In addition, the prompting phase with file-level dependency analysis is the best individual integration strategy.
The main reason why file-level dependencies outperform token-level dependencies might be that (i) the file-level
contains more comprehensive contexts regarding the usage of APIs, and (ii) putting the cross-file context of
the original code hierarchies at the beginning of the current file, aligns better with the data layout during
LLM pre-training. Therefore, although file-level dependencies and token-level dependencies can both provide
the correct APIs in the prompt, it is easier for LLMs to utilize the relevant tokens displayed within file-level
dependencies.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 11](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-11.png)

![Página PDF 11, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

12
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Fig. 2. Comparison case of Prompt-F, Decode and Post
Generalization on different languages and LLMs. The observations above can be generalized on different
languages and LLMs, as we observe consistent trends in all studied languages and LLMs. For both static and
dynamic languages, integrating static analysis into any phase of code completion can improve LLM-based
repository-level code completion, while the prompting phase with file-level dependency analysis is always the
best one with the highest improvements.
Answer to RQ1: Integrating static analysis in any phase can improve repository-level code completion for
all studied LLMs on both static and dynamic languages. Among them, integration in the prompting phase
(especially with file-level dependencies) can achieve substantially larger improvements than other phases,
while integration in the post-processing phase achieves the smallest improvements.
5.2
RQ2: Combined Integration Strategies
Table 3 presents the effectiveness when two-phase integration strategies are combined. Although STALL+
theoretically supports the combination between any two strategies, our experiments skip the combination of
decoding-phase integration and post-processing-phase integration, given the expensive time and memory costs
of their combination, which will be discussed in RQ3.b. Based on the results, we have the following observations.
Improvements from two-phase combined strategies. As presented in Table 3, combining any prompting-
phase integration strategies with a non-prompting strategy can further improve the accuracy of LLM-based
code completion. For example, combining prompting-phase integration (with file-level dependency) with either
decoding-phase or post-processing-phase integration can both improve the original prompting-phase integration
with 0.8% and 3.4% relative increase in line EM. The only exception occurs when combining the decoding-phase
integration with the prompting-phase integration on Python, where there is even a marginal decrease (e.g., for
DeepSeek-Coder on Python). The reason might be the limitations in analyzing dynamic language, which we
further discuss in the later paragraph “Different results on different languages”.
Complementarity between different strategies. The improvements of combining different integration strategies
actually vary, indicating the different complementarity between integration strategies. In particular, we can
observe the smallest complementarity between the prompting-phase integration with token-level dependencies
and the decoding-phase integration, as their combination leads to at most 2.6% improvements in line EM. The
main reason might be that both token-level dependencies and the decoding-phase integration are built on the
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 12](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-12.png)

![Página PDF 12, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
13
Table 3. Results of two-phase combined integration strategies. Numbers in the parentheses show the relative improvement
over the prompting-phase integration strategy in each combination.
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
DeepSeek-Coder
6.7B
Prompt-F + Decode 28.01(↑0.8%)𝑛𝑠0.00
70.83(↓2.5%)§0.03
36.38(↓1.0%)𝑛𝑠0.00
63.98(↓1.5%)‡0.01
46.46(↑5.0%)§0.02 80.68(↑0.4%)†0.02 55.37(↑4.0%)§0.02 75.18(↑2.7%)§0.03 86.94(↑2.5%) §0.02
Prompt-F + Post
28.74(↑3.4%)†0.01 72.40(↓0.3%)𝑛𝑠0.00 36.91(↑0.4%)𝑛𝑠0.00 65.04(↑0.2%)𝑛𝑠0.00 45.93(↑3.8%)§0.02
80.49(↑0.2%)‡0.02
54.80(↑2.9%)§0.02
73.79(↑0.8%)‡0.02 87.52(↑3.2%)§0.03
Prompt-T + Decode 24.51(↓1.3%)𝑛𝑠0.00
68.08(↓2.6%)§0.03
32.80(↓3.4%)†0.01
60.55(↓1.9%)‡0.02
39.04(↑1.0%)†0.01
76.53(↓0.6%)†0.00
47.47(↑0.6%)𝑛𝑠0.00 68.44(↑0.0%)𝑛𝑠0.00
77.54(↑3.1%)§0.02
Prompt-T + Post
26.95(↑8.5%)§0.02
70.05(↑0.2%)𝑛𝑠0.01
35.45(↑4.5%)‡0.01
61.99(↑0.5%)𝑛𝑠0.01
40.34(↑4.4%)§0.02
76.97(↑0.0%)𝑛𝑠0.01
48.48(↑2.8%)‡0.01
69.01(↑0.9%)†0.01
80.72(↑7.3%)§0.05
StarCoderBase
7B
Prompt-F + Decode 23.98(↑1.7%)𝑛𝑠0.00
68.20(↓2.3%)§0.03
31.42(↓2.4%)†0.01
60.40(↓1.5%)‡0.01
42.89(↑6.7%)§0.03 79.24(↑0.4%)𝑛𝑠0.02 53.25(↑5.2%)§0.03 73.56(↑3.3%)§0.03
85.45(↑3.4%)§0.03
Prompt-F + Post
25.09(↑6.4%)§0.02 70.10(↑0.5%)𝑛𝑠0.01 32.94(↑2.3%)𝑛𝑠0.01 61.92(↑0.9%)𝑛𝑠0.01 41.73(↑3.8%)§0.02
78.89(↓0.0%)†0.02
51.76(↑2.3%)§0.02
71.20(↓0.0%)𝑛𝑠0.01 85.54(↑3.5%)§0.03
Prompt-T + Decode 20.81(↑2.6%)𝑛𝑠0.01
64.62(↓2.5%)§0.03
28.53(↓0.3%)𝑛𝑠0.00
55.57(↓1.6%)‡0.01
35.04(↑1.5%) †0.01
75.46(↓0.3%)†0.00
44.82(↑1.4%)†0.01
66.38(↑0.4%)†0.01
76.87(↑3.0%)§0.02
Prompt-T + Post
22.34(↑10.2%)§0.02 66.53(↑0.3%)𝑛𝑠0.01
29.58(↑3.4%)†0.01
56.54(↑0.1%)𝑛𝑠0.00
37.11(↑7.5%)§0.03
76.42(↑0.9%)‡0.03
46.41(↑5.0%)§0.03
67.49(↑2.1%)§0.02
78.99(↑5.8%)§0.04
CodeLlama
7B
Prompt-F + Post
25.22(↑5.3%)‡0.01 69.27(↓0.7%)𝑛𝑠0.00 33.31(↑0.9%)𝑛𝑠0.00 60.39(↓1.3%)𝑛𝑠0.00 43.28(↑4.9%)§0.02 79.05(↑0.3%)‡0.02 52.58(↑3.1%)§0.02 71.84(↑1.0%)‡0.02 85.40(↑3.0%)§0.03
Prompt-T + Post
24.09(↑12.3%)§0.03 67.76(↑0.6%)𝑛𝑠0.01
32.03(↑5.6%)‡0.02
58.75(↑1.1%)𝑛𝑠0.01
36.14(↑8.4%)§0.03
75.45(↑0.7%)†0.03
44.82(↑5.6%)§0.03
66.11(↑2.0%)‡0.02
77.73(↑5.4%)§0.04
Fig. 3. Bad cases in decoding-phase integration ( prompt , ground truth , model prediction , explanation )
list of valid tokens (e.g., the active method names or variable names), which share quite overlapping hints to
the models. As a result, the benefits from combining them can be limited. In addition, we observe a relatively
stable complementarity between post-processing integration and other phases. Although it performs worse than
strategies combined with decoding-phase integration on Java in terms of similarity metrics, post-processing
integration achieves higher Compilation Rates, as it selects results based on syntactic correctness, making the
outputs more likely to pass compilation checks.
Different results on different languages. Interestingly, we can observe that the complementarity between
integration strategies is different for static language (Java) and dynamic language (Python). Especially for
the decoding-phase integration, it exhibits larger improvements when combined with other strategies in Java
than in Python. Moreover, on Python subsets, the combination with decoding-phase integration might achieve
improvements in line EM, but all improvements are not statistically significant (p>0.05). In particular, for DeepSeek-
Coder-6.7B on Python, line EM of the token-level dependencies even drops (i.e., decreasing from 24.84 to 24.51)
after being combined with the decoding-phase integration.
Bad cases caused by imprecise static analysis. We further perform qualitative and quantitative analysis by man-
ually inspecting bad cases and find that the observed performance degradation mainly stems from the inherent
challenges of statically analyzing dynamic languages, which are common in dynamic languages. Figure 3 and
Figure 4 present representative bad cases and their distribution over Python subsets for DeepSeek-Coder-6.7B +
Prompt-T + Decode. These dynamic language characteristics pose significant challenges to static analysis, leading
it to either miss correct tokens or introduce irrelevant candidates during decoding, thereby misleading the model-
predicted results by incorrectly adjusting the decoding logits. To the best of our knowledge, prior work [9, 74]
mainly reports the benefits of decoding-phase integration, while we are the first to systematically reveal its
potential negative effects caused by imprecise static analysis through both qualitative and quantitative analysis.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 13](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-13.png)

![Página PDF 13, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-13.png)


<!-- PDF page 14 -->

## Página PDF 14

14
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Fig. 4. Distribution of bad cases in decoding-phase integration (Deepseek-Coder-6.7B + Prompt-T + Decode)
Different sensitivities of metrics to failures. In addition, the combination of the prompting-phase with
decoding-phase or post-processing-phase integration strategies sometimes leads to an increase in line EM, while
other similarity-based metrics decline (e.g., for DeepSeek-Coder on Python), which has also been reported in
prior work [74]. While prior work attributes this to the granularity mismatch between tokens and strings, our
further analysis reveals that this phenomenon also stems from the different sensitivities of the used metrics to
failure cases. For example, line EM is a discrete metric and yields a value of 0 regardless of how far the prediction
deviates from the ground truth. In contrast, other continuous metrics (e.g., Line ES, ID EM, and ID F1) may
decrease substantially as the textual difference between the prediction and the ground truth increases. For the
decoding-phase integration strategy, imprecise static analysis can lead the LLM to generate excessively long
erroneous outputs, which significantly degrade continuous metrics based on syntactic similarity. Figure 5(a)
presents an example in which the LLM incorrectly predicts a Python keyword, memoryview, ultimately causing a
generation loop that fills the entire output window. For the post-processing integration strategy, the LLM may
sometimes generate APIs that are lexically similar to the ground truth but are hallucinated. These APIs tend to
receive relatively high similarity scores; however, they fail the syntactic checks in the post-processing phase. In
contrast, APIs that differ entirely from the ground truth but pass the checks are retained. Figure 5(b) illustrates a
case. Therefore, although decoding-phase and post-processing-phase integration can improve line EM, they may
lead to the degradation of other similarity-based metrics.
Performance of three-phase combined strategies. Finally, given the potential gains from the combination of all
three-phase integration strategies, we conduct experiments on 200 tasks and report the results in Table 4. Unlike
the consistent improvements observed with the two-phase integration strategies, the three-phase integration
strategy generally leads to performance degradation compared with the two-phase strategy without the decoding-
phase integration strategy. This degradation is primarily attributed to the negative impact of the imprecise static
analysis. Specifically, if the static analysis is incorrect, decoding-phase integration will mask the correct paths
that post-processing might generate, ultimately causing the positive improvements from post-processing to
also be suppressed. Furthermore, incorporating both file-level dependencies and token-level dependencies in
the prompt achieves better performance than using token-level dependencies alone, but performs worse than
incorporating only file-level dependencies. A possible explanation is that simultaneously including both types of
information increases prompt complexity and introduces additional ambiguity for LLMs, thereby preventing the
combined information from yielding the expected synergistic benefit.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 14](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-14.png)

![Página PDF 14, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-14.png)


<!-- PDF page 15 -->

## Página PDF 15

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
15
Fig. 5. Predictions with low lexical similarity when integrating decoding-phase and post-processing-phase static analysis
strategies.
Table 4. Results of three-phase combined integration strategies in 200 samples. Numbers in the parentheses show the relative
improvement over the corresponding two-phase combinations without Decode (Prompt-F/ Prompt-T + Post). For Prompt-F +
Prompt-T + Decode + Post, improvements are measured against Prompt-F + Post.
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
DeepSeek-Coder
6.7B
Prompt-F + Decode + Post
29.50(↑1.7%)𝑛𝑠0.01 69.63(↓4.4%)‡0.05 33.50(↓2.9%)𝑛𝑠0.01 65.26(↓2.8%)𝑛𝑠0.03 53.00(↑1.9%)𝑛𝑠0.01 84.27(↓0.9%)𝑛𝑠0.01 60.00(↑0.8%)𝑛𝑠0.01 78.65(↑2.3%)𝑛𝑠0.02 86.50(↓1.7%)𝑛𝑠0.01
Prompt-T + Decode + Post
25.50(-0.0%)𝑛𝑠0.00
65.91(↓4.0%)‡0.05
30.50(↓3.2%)𝑛𝑠0.01
58.88(↓3.8%)†0.03
45.00(↓7.2%)𝑛𝑠0.04
80.61(↓1.1%)𝑛𝑠0.03
50.00(↓9.1%)†0.05
71.76(↓2.4%)𝑛𝑠0.04
87.52(↓1.7%)𝑛𝑠0.01
Prompt-F + Prompt-T + Decode + Post 26.50(↓8.6%)𝑛𝑠0.03
68.06(↓6.6%)‡0.09
33.50(↓2.9%)𝑛𝑠0.01
62.05(↓7.5%)†0.07
53.50(↑2.9%)𝑛𝑠0.01 83.82(↓1.4%)𝑛𝑠0.00 60.00(↑0.8%)𝑛𝑠0.01 77.62(↑0.9%)𝑛𝑠0.01
90.50(↑2.8%)𝑛𝑠0.03
StarCoderBase
7B
Prompt-F + Decode + Post
27.50(↓5.2%)𝑛𝑠0.01 69.14(↓3.2%)†0.05 30.50(↓9.0%)𝑛𝑠0.03 63.19(↓1.2%)𝑛𝑠0.02 52.50(↑5.0%)𝑛𝑠0.03 83.91(↑0.7%)𝑛𝑠0.02 59.00(↑2.6%)𝑛𝑠0.01 76.70(↑4.2%)𝑛𝑠0.03 90.00(↑4.0%)†0.04
Prompt-T + Decode + Post
22.50(↓2.2%)𝑛𝑠0.01
66.39(-0.0%)𝑛𝑠0.00
30.00(-0.0%)𝑛𝑠0.00
57.49(↑3.4%)𝑛𝑠0.02
43.00(↓6.5%)𝑛𝑠0.03
79.80(↓3.5%)‡0.06
49.00(↓7.5%)†0.04
70.05(↓4.9%)‡0.05
82.00(↓1.20%)𝑛𝑠0.01
Prompt-F + Prompt-T + Decode + Post 23.50(↓19.0%)†0.06 67.27(↓5.8%)‡0.08
28.50(↓14.9%)†0.05
58.74(↓8.2%)†0.08
52.50(↑5.0%)𝑛𝑠0.03 83.22(↓0.2%)𝑛𝑠−0.01 58.50(↑1.7%)𝑛𝑠0.01
75.65(↑2.8%)𝑛𝑠0.02
90.00(↑4.0%)†0.04
Answer to RQ2:
Combining prompting-phase integration strategies with decoding-phase and post-
processing-phase integration strategies can further improve LLM-based repository-level code completion.
The complementarity between integration strategies varies: (i) the decoding phase and prompting phase with
token-level dependencies share the smallest complementarity as they share similar information; (ii) improve-
ments from combining with decoding-phase integration are large for Java, but remain small and statistically
insignificant for Python, given difficulties in statically analyzing dynamic languages; (iii) the combination
with post-processing-phase integration achieves consistent statistically significant improvements. Combining
three-phase strategies leads to performance degradation on Python, due to the compounded side effects of
the decoding phase and the post-processing phase integration.
5.3
RQ3: Compared with RAG
Retrieval-Augmented Generation (RAG) is another mainstream category for enhancing LLM-based repository-
level code completion. In RQ3, we compare both the effectiveness and efficiency between static analysis integration
and RAG.
5.3.1
RQ3.a Effectiveness. Table 5 shows the experimental results of RAG-based strategies (i.e., Naive RAG,
RepoCoder and Repoformer) and the combination of Naive RAG with other static analysis-integrated strategies.
We merely include Repoformer with StarCoderBase-7B since only this model is open-sourced.
Compared with RAG. First, compared with the individual static analysis integration strategies in Table 2,
enhancing LLMs with static analysis in the prompting phase (with either file-level dependencies or token-level
dependencies) substantially outperforms enhancing LLMs with Naive RAG and Repoformer. However, Naive RAG
is more effective than integration strategies in decoding or post-processing phases. RepoCoder improves line EM
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 15](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-15.png)

![Página PDF 15, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-15.png)


<!-- PDF page 16 -->

## Página PDF 16

16
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Table 5. Results of RAG-based strategies and the combination of Naive RAG and static analysis-integrated strategies.
Numbers in the parentheses show the relative improvement over the Naive RAG (for RepoCoder and Repoformer) or the
pure static analysis-integrated strategies without Naive RAG (for combinations).
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
DeepSeek-Coder
6.7B
Naive RAG
20.33
69.50
29.27
59.16
38.27
78.04
47.13
67.81
73.73
RepoCoder
22.93 (↑1.8%)§0.03
70.76 (↑1.8%)§0.03
32.20 (↑10.0%)§0.03
61.05 (↑3.2%)§0.03
40.19 (↑5.0%)𝑛𝑠0.01
79.50 (↑1.9%)†0.01
48.82 (↑3.6%)𝑛𝑠0.01
68.32 (↑0.8%)†0.01
72.77 (↓1.3%)†0.01
+ Prompt-F
33.66 (↑21.1%)§0.06
75.94 (↑4.5%)§0.08
44.02 (↑19.8%)§0.07
70.06 (↑7.9%)§0.08
50.70 (↑14.6%)§0.07
82.71 (↑3.0%)§0.07
60.29 (↑13.2%)§0.07
77.54 (↑5.9%)§0.08
87.61 (↑3.3%)§0.03
+ Prompt-T
30.61 (↑23.2%)§0.06
73.67 (↑5.4%)§0.09
41.18 (↑21.3%)§0.07
67.38 (↑9.2%)§0.09
45.16 (↑16.8%) §0.07
80.23 (↑4.3%)§0.09
54.65 (↑15.8%)§0.08
73.77 (↑7.8%)§0.09
81.69 (↑8.6%)§0.06
+ Decode
24.02 (↑49.9%)§0.08
68.45 (↑7.1%)§0.11
32.89 (↑40.7%)§0.10
61.25 (↑12.8%)§0.11
42.80 (↑29.3%)§0.10
78.71 (↑5.9%)§0.12
51.56 (↑24.4%)§0.10
71.48 (↑10.8%)§0.11
80.92 (↑9.1%)§0.07
+ Post
22.93 (↑98.7%)§0.11
70.29 (↑10.9%)§0.17
31.06 (↑78.9%)§0.14
60.08 (↑21.5%)§0.17
40.92 (↑34.8%)§0.11
78.15 (↑6.1%)§0.13
49.35 (↑29.6%)§0.12
68.98 (↑13.2%)§0.13 78.17 (↑10.4%)§0.07
+ Prompt-F + Decode
32.32 (↑15.4%)§0.04
73.32 (↑3.5%)§0.06
41.30 (↑13.5%) §0.05
67.49 (↑5.5%)§0.06
52.05 (↑12.0%)§0.06 82.96 (↑2.8%)§0.07 61.40 (↑10.9%)§0.07 78.81 (↑4.8%)§0.07
89.45 (↑2.9%)§0.03
+ Prompt-F + Post
34.67 (↑20.6%)‡0.07 76.51 (↑5.7%)§0.12 45.00 (↑21.9%)§0.10 70.55 (↑8.5%)§0.11 52.05 (↑13.3%)§0.09 82.41 (↑2.4%)§0.08
60.87 (↑11.1%)§0.07
77.48 (↑5.0%)§0.07
89.93 (↑2.8%)§0.02
+ Prompt-T + Decode
29.31 (↑19.6%)§0.05
71.21 (↑4.6%)§0.07
38.54 (↑17.5%)§0.06
64.87 (↑7.1%)§0.07
45.20 (↑15.8%)§0.07
79.93 (↑4.4%)§0.09
54.46 (↑14.7%)§0.08
73.68 (↑7.7%)§0.09
82.65 (↑6.6%)§0.05
+ Prompt-T + Post
32.36 (↑20.1%)‡0.06
74.00 (↑5.6%)§0.11
42.11 (↑18.8%)§0.07
67.58 (↑9.0%)§0.11
46.75 (↑15.9%)‡0.08
80.54 (↑4.6%)§0.10
56.29 (↑16.1%)‡0.09
74.76 (↑8.3%)‡0.09
84.53 (↑4.7%)§0.04
StarCoderBase
7B
Naive RAG
16.06
67.07
25.28
55.84
34.12
76.42
44.00
65.81
72.14
RepoCoder
19.23 (↑19.7%)§0.03
68.70 (↑2.4%)§0.04
28.86 (↑14.2%)§0.04
58.19 (↑4.2%)§0.04
36.72 (↑7.6%)𝑛𝑠0.00
78.30 (↑2.5%)𝑛𝑠0.00
45.30 (↑3.0%)‡0.01
66.27 (↑0.7%)†0.01
71.23 (↓1.3%)†0.01
Repoformer
16.38 (↑2.0%)𝑛𝑠0.00
66.79 (↓0.4%)𝑛𝑠0.00
24.80 (↓1.9%)𝑛𝑠0.01
55.51 (↓0.6%)𝑛𝑠0.00
21.45 (↓37.1%)§0.15 64.81 (↓15.2%)§0.28
28.19 (↓35.9%)§0.18
51.90 (↓21.1%)§0.22 46.89 (↓35.0%)§0.25
+ Prompt-F
28.74 (↑21.9%)§0.05
73.68 (↑5.6%)§0.09
39.31 (↑22.1%)§0.07
66.81 (↑8.9%)§0.09
45.83 (↑14.0%)§0.06
81.26 (↑3.0%)§0.07
56.92 (↑12.5%)§0.07
75.73 (↑6.3%)§0.07
86.17 (↑4.3%)§0.04
+ Prompt-T
26.83 (↑32.3%)§0.07
71.07 (↑7.2%)§0.11
37.64 (↑31.5%)§0.09
63.80 (↑12.9%)§0.11
40.77 (↑18.1%)§0.07
78.36 (↑3.5%)§0.07
50.84 (↑15.0%)§0.07
71.07 (↑7.5%)§0.08
79.42 (↑6.4%)§0.05
+ Decode
19.67 (↑50.3%)§0.07
66.66 (↑7.2%) §0.10
28.78 (↑38.8%) §0.08 58.65 (↑12.5%) §0.10 38.94 (↑26.1%)§0.09
77.38 (↑4.9%)§0.10
48.82 (↑22.4%)§0.09
70.21 (↑10.8%) §0.11
79.81 (↑9.5%)§0.07
+ Post
18.14 (↑134.7%)§0.10 67.18 (↑11.4%)§0.16
26.47 (↑93.2%)§0.13
56.38 (↑23.2%)§0.17
36.67 (↑40.4%)§0.11
76.81 (↑6.0%)§0.12
46.41 (↑33.0%)§0.12
66.76 (↑14.7%)§0.13 76.34 (↑13.0%)§0.09
+ Prompt-F + Decode
27.60 (↑15.1%)§0.04
71.29 (↑4.5%)§0.07
36.54 (↑16.3%)§0.05
64.93 (↑7.5%)§0.07
47.61 (↑11.0%)§0.05
81.43 (↑2.8%)§0.06
58.60 (↑10.0%)§0.06
77.14 (↑4.9%)§0.06
87.86 (↑2.8%)§0.02
+ Prompt-F + Post
30.26 (↑20.6%)‡0.07 73.81 (↑5.3%)§0.13 40.30 (↑22.3%)§0.08 67.47 (↑9.0%)§0.12 48.24 (↑15.6%)§0.07 81.80 (↑3.7%)§0.07 58.89 (↑13.8%)§0.07
76.25 (↑7.1%)§0.08
88.72 (↑3.7%)§0.03
+ Prompt-T + Decode
25.80 (↑24.0%)§0.05
68.55 (↑6.1%)§0.08
34.95 (↑22.5%)§0.07
61.36 (↑10.4%)§0.09
41.16 (↑17.5%)§0.07
78.20 (↑3.6%)§0.07
51.18 (↑14.2%)§0.07
71.29 (↑7.4%)§0.08
81.45 (↑6.0%)§0.05
+ Prompt-T + Post
27.94 (↑25.1%)†0.04
70.77 (↑6.4%)§0.11
37.62 (↑27.2%)†0.06
63.16 (↑11.7%)§0.12
44.05 (↑18.7%)†0.06
78.92 (↑3.3%)†0.04
53.64 (↑15.6%)†0.06
72.11 (↑6.8%)†0.05
84.10 (↑6.5%)§0.05
CodeLlama
7B
Naive RAG
17.52
67.71
26.22
56.41
35.90
76.91
44.58
66.15
71.86
RepoCoder
20.04 (↑14.4%)§0.02
69.01 (↑1.9%)§0.03
29.07 (↑10.9%)§0.03
58.70 (↑4.1%)§0.04
37.98 (↑5.8%)†0.01
78.53 (↑2.1%)𝑛𝑠0.01
46.07 (↑3.3%)†0.01
66.72 (↑0.9%)𝑛𝑠0.01
71.52 (↓0.5%)𝑛𝑠0.00
+ Prompt-F
29.55 (↑23.4%)§0.06
73.86 (↑5.9%)§0.09 40.49 (↑22.7%) §0.08
67.23 (↑9.9%)§0.10
47.61 (↑15.4%)§0.07
81.30 (↑3.2%)§0.08
57.45 (↑12.7%)§0.07
75.58 (↑6.3%)§0.07
86.22 (↑4.0%)§0.03
+ Prompt-T
27.32 (↑27.3%)§0.06
70.93 (↑5.3%)§0.08
37.64 (↑24.1%)§0.07
63.56 (↑9.4%)§0.08
41.98 (↑25.9%)§0.09
78.59 (↑4.9%)§0.10
51.33 (↑20.9%)§0.09
70.81 (↑9.2%)§0.09
79.18 (↑7.3%)§0.05
+ Post
19.59 (↑120.9%) §0.11 68.16 (↑12.7%)§0.18
27.52 (↑84.5%)§0.13
56.83 (↑24.0%)§0.17
38.36 (↑38.7%)§0.12
77.39 (↑6.6%)§0.13
46.89 (↑32.2%)§0.12
67.37 (↑14.7%)§0.13 75.61 (↑12.7%)§0.09
+ Prompt-F + Post
31.34 (↑24.3%)‡0.07
73.48 (↑6.1%)§0.12 40.93 (↑22.9%)‡0.07 66.58 (↑10.3%)§0.10 48.72 (↑12.6%)§0.09 81.46 (↑3.0%)‡0.08 58.22 (↑10.7%)‡0.07 75.86 (↑5.6%)‡0.07 88.19 (↑3.3%)§0.03
+ Prompt-T + Post
29.07 (↑20.7%)‡0.07
70.86 (↑4.6%)§0.10
38.62 (↑20.6%)§0.04
63.34 (↑7.8%)§0.06
43.90 (↑21.5%)§0.09
78.92 (↑4.6%)‡0.10
52.63 (↑17.4%)§0.10
71.89 (↑8.7%)§0.10
82.31 (↑5.9%)§0.05
over Naive RAG by 12.8%–19.7% on Python and 5.0%–7.6% on Java, slightly outperforming the prompting-phase
integration with token-level dependencies on Java (e.g., 40.19 vs. 38.65 for DeepSeek-Coder) but still lagging
behind it on Python (e.g., 22.93 vs. 24.84 for DeepSeek-Coder). Repoformer yields only marginal improvements
over Naive RAG, achieving about 2% line EM gain (not statistically significant) on Python and even showing
a clear decline on Java. This may stem from the fact that Repoformer is trained with a fill-in-the-middle (FIM)
objective, which makes it less compatible with our prefix-only completion setting. In addition, Repoformer is
only fine-tuned on Python data, which may lead to negative results on Java. Consequently, Repoformer performs
worse than all static analysis integration strategies on both languages.
Second, compared with the results in Table 3, the combination of any two static analysis integration strategies
substantially outperforms Naive RAG and generally surpasses RepoCoder. A few exceptions appear in Java; for
instance, the least effective combination, Prompt-T + Decode, underperforms RepoCoder (the line EM is 39.04 vs.
40.19 for DeepSeek-Coder).
In summary, prior RAG work has contributed by revealing the effectiveness of diverse RAG-based strategies in
code completion, including single-round RAG [21, 49], multi-round RAG [85], and selective RAG [79]. However,
these approaches largely adopt RAG strategies developed for general-purpose QA tasks, overlooking the unique
characteristics of code, i.e., static analysis provides a more precise and effective way to identify relevant context
than general-purpose retrieval. For example, for the completion of method invocation, the previous work [21]
shows that including the ground-truth method invocation in prompts is beneficial for repository-level code
completion. Based on our statistics, RAG correctly retrieves the code containing the ground-truth method
invocation only for 17.87%/19.08% of cases in Python/Java (it is hard for RAG to retrieve such code especially
when the method is seldom used in other files or used in very different contexts); while static analysis can get
such information for many more cases by dependency analysis (i.e., 58.16%/55.32% in Python/Java). Our work
fills the gap of a systematic comparison between static analysis strategies and RAG strategies, and offers the first
empirical evidence that integrating static analysis can outperform RAG. This is also supported by the results
from prior RAG-based studies [21], with the highest line EM scores on CrossCodeEval being 21.35/21.69 for
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 16](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-16.png)

![Página PDF 16, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-16.png)


<!-- PDF page 17 -->

## Página PDF 17

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
17
Python/Java using StarCoder-15.5B, which are notably lower than the results of the combined static analysis
integration strategies with the smaller StarCoder-7B model (25.09/41.3 for Python/Java).
Combined with RAG. Overall, we can find that combining RAG with individual or multiple integration strategies
can further substantially improve LLM-based repository-level code completion with statistical significance, to
the best of our knowledge, even leading to the best accuracy on CrossCodeEval so far. For example, combin-
ing RAG with file-level dependencies and post-processing-phase integration achieves 34.67/52.05 line EM for
DeepSeek-Coder-6.7B on Python/Java, which is the highest accuracy on the CrossCodeEval benchmark (i.e.,
than the highest reported line EM with larger-scale models on CrossCodeEval is 21.35/21.69 [21]). In addition, in
most cases, combining RAG with file-level dependencies and post-processing integration can achieve the best
effectiveness. The results reveal the complementarity between static analysis and RAG, indicating that combining
both techniques can enable more powerful LLM-based repository-level code completion.
5.3.2
RQ3.b Efficiency. Table 6 compares the online latency, GPU utilization, and TFLOPs (Tera Floating Point
Operations Per Second) of different static analysis integration strategies and RAG-based strategies (i.e., Naive
RAG and RepoCoder).
From the latency perspective, we summarize the following findings. First, for individual-phase integration
strategies, the prompting-phase integration (i.e., Prompt-F and Prompt-T) is more efficient than Naive RAG.
For example, the latency for generating 20 tokens drops from 2.00 to 1.81 (9.5%) and 1.52 (24%), respectively.
Besides, they both achieve higher completion accuracy than Naive RAG (as shown in RQ3.a). Furthermore,
Prompt-T is the most efficient among all studied strategies, with the lowest latency, nearly full GPU utilization
(98.64%), and the second-lowest TFLOPs. This efficiency gain mainly comes from two factors: (1) Prompt-T
introduces a substantially smaller context compared to file-level dependency prompting and Naive RAG. On
Python tasks, the average number of tokens introduced by Promopt-T is 429 per task, which is 42.2% fewer than
file-level dependency prompting (742 tokens) and 50.6% fewer than Naive RAG (868 tokens), thereby reducing
decoding overhead; and (2) it provides more focused API-level dependency information that is highly relevant
to the current target object, which reduces the model’s reasoning burden over irrelevant context and improves
autoregressive generation efficiency. Given that Prompt-T ranks second only to Prompt-F in completion accuracy,
it provides a practical, efficiency-oriented alternative for the latency-sensitive code completion tasks. Second, the
latency of the combined strategies mainly arises from the decoding-phase and post-processing-phase integration
strategy. In the two-phase static analysis integration strategies, the former contributes 25.8% to 61.3% of the
latency, while the latter causes an even larger latency increase, ranging from 161.8% to 208.8%. Third, the multi-
turn generation strategy of RepoCoder incurs significant latency. Compared with the two-phase static analysis
integration strategies, its latency is merely lower than the most expensive Prompt-F + Post combination. However,
as shown in Tables 3 and 5, its performance is substantially lower than most two-phase static analysis integration
strategies, further highlighting the advantage of static analysis over RAG-based strategies in both effectiveness
and efficiency for repository-level code completion tasks. Finally, the three-phase combined integration strategies
incur significant latency and computational overhead. For instance, predicting five tokens with Prompt-F +
Decode + Post takes 5.25 seconds, which limits its usage in practical development scenarios.
From the perspective of GPU utilization and TFLOPs, it can be observed that the decoding-phase integration
strategy significantly reduces GPU utilization to around 20% due to the need to interrupt generation for static
analysis and completion. However, since it does not increase computation during inference, its TFLOPs are the
smallest. In contrast, under the post-processing integration strategy, the additional sequence reranking steps
reduce GPU utilization to below 90%. Moreover, the TFLOPs are the highest due to simultaneously generating
multiple sequences. RepoCoder also incurs a noticeable increase in TFLOPs due to performing two rounds of
generation.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 17](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-17.png)

![Página PDF 17, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-17.png)


<!-- PDF page 18 -->

## Página PDF 18

18
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Table 6. Efficiency comparison of the static analysis integration strategies with the RAG-based strategies. Numbers in the
parentheses show the relative improvement with the In-file strategy (for individual-phase strategies), the corresponding
prompting-phase integration strategy (for two-phase integration strategies) or Naive RAG (for Repocoder), and the two-phase
integration strategies without Post (for three-phase integration strategies).
Strategy
Latency (s/k tokens)
GPU Util. (%)
TFLOPs
k=5
k=10
k=15
k=20
In-file
0.98
1.12
1.22
1.24
98.36
15.63
Naive RAG
1.64(↑67.3%)
1.81(↑61.6%)
1.97(↑61.5%)
2.00(↑61.3%)
98.75(↑0.4%)
26.53(↑69.7%)
Prompt-F
1.63(↑66.3%)
1.79(↑59.8%)
1.81(↑48.4%)
1.81(↑46.0%)
98.91(↑0.6%)
27.53(↑76.1%)
Prompt-T
1.17(↑19.4%)
1.31(↑17.0%)
1.36(↑11.5%)
1.52(↑22.6%)
98.64(↑0.3%)
18.10(↑15.8%)
Decode
1.46(↑49.0%)
1.79(↑59.8%)
2.20(↑80.3%)
2.29(↑84.7%)
16.43(↓83.3%)
15.64(↑0.1%)
Post
2.67(↑172.4%)
2.96(↑164.3%)
3.23(↑164.8%)
3.40(↑174.2%)
82.41(↓16.2%)
46.94(↑200.3%)
RepoCoder
3.28(↑100.0%)
3.61(↑99.4%)
3.90(↑98.0%)
3.90(↑95.0%)
98.68(↓0.1%)
46.95(↑76.9%)
Prompt-F + Decode
2.05(↑25.8%)
2.38(↑33.0%)
2.66(↑47.0%)
2.92(↑61.3%)
24.63(↓75.1%)
27.52(↓0.0%)
Prompt-F + Post
4.62(↑183.4%)
4.98(↑178.2%)
5.48(↑202.8%)
5.59(↑208.8%)
88.38(↓10.6%)
82.65(↑200.3%)
Prompt-T + Decode
1.62(↑38.5%)
1.93(↑47.3%)
2.15(↑58.1%)
2.43(↑59.9%)
19.64(↓80.1%)
18.10(-0.0%)
Prompt-T + Post
3.23(↑176.1%)
3.54(↑170.2%)
3.80(↑179.4%)
3.98(↑161.8%)
84.80(↓14.0%)
54.36(↑200.4%)
Prompt-F + Decode + Post
5.25(↑156.1%)
5.88(↑147.1%)
6.68(↑151.1%)
7.02(↑140.4%)
41.65(↑69.1%)
82.62(↑200.2%)
Prompt-T + Decode + Post
3.74(↑130.9%)
4.40(↑128.0%)
4.79(↑122.8%)
5.21(↑114.4%)
33.01(↑68.1%)
54.32(↑200.2%)
·
Table 7. Results of individual integration strategies on larger-scale LLMs on 200 samples. Numbers in parentheses show the
relative improvement over in-file generation.
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
Claude-Sonnet
4.5
In-file
20.50
68.95
29.00
59.18
38.00
80.50
43.50
68.29
70.00
Naive RAG
34.00(↑65.9%)§0.14
75.15(↑9.0%)§0.16
44.00(↑51.7%)§0.15
69.81(↑18.0%)§0.17
49.00(↑28.9%)§0.11
83.46(↑3.7%)‡0.10
54.50(↑25.3%)§0.11
74.52(↑9.1%)§0.11
75.00(↑7.1%)†0.05
RepoCoder
35.50(↑73.2%)§0.15
76.84(↑11.4%)§0.20
45.50(↑56.9%)§0.17
70.61(↑19.3%)§0.18
46.50(↑22.4%)§0.09
82.94(↑3.0%)‡0.09
52.00(↑19.5%)‡0.09
73.81(↑8.1%)‡0.09
73.00(↑4.3%)𝑛𝑠0.03
Prompt-F
39.50(↑92.7%)§0.19 77.69(↑12.7%)§0.22 49.00(↑69.0%)§0.20
75.03(↑26.8%)§0.26
57.00(↑50.0%)§0.19
87.27(↑8.4%)§0.21 63.50(↑46.0%)§0.20 81.75(↑19.7%)§0.22 90.00(↑28.6%)§0.20
Prompt-T
38.50(↑87.8%)§0.18
76.17(↑10.5%)§0.19
47.50(↑63.8%)§0.18
71.90(↑21.5%)§0.21
53.50(↑40.8%)§0.15
85.53(↑6.2%)§0.17
61.00(↑40.2%)§0.17
79.52(↑16.4%)§0.18
81.00(↑15.7%)§0.11
Qwen3-Coder
30B-A3B-Instruct
In-file
9.00
59.86
13.50
45.20
16.50
65.99
21.00
43.33
49.00
Naive RAG
21.00(↑133.3%)§0.12
66.04(↑10.3%)§0.14 31.00(↑129.6%)§0.17
58.31(↑29.0%)§0.20
23.50(↑42.4%)‡0.07
71.03(↑7.6%)§0.11
28.50(↑35.7%)§0.07
50.86(↑17.4%)§0.10
52.50(↑7.1%)†0.04
RepoCoder 24.50(↑172.2%)§0.15
67.08(↑12.1%)§0.18 33.00(↑144.4%)§0.20
61.00(↑35.0%)§0.24
24.50(↑48.5%)‡0.07
72.03(↑9.2%)§0.13
29.00(↑38.1%)‡0.08
50.85(↑17.4%)§0.10
51.50(↑5.1%)𝑛𝑠0.03
Prompt-F
25.00(↑177.8%)§0.16 68.89(↑15.1%)§0.21 34.00(↑41.1%)§0.20 63.78(↑118.2%)§0.30 36.00(↑118.2%)§0.19 75.86(↑15%)§0.23
42.00(↑100%)§0.21 60.70(↑40.1%)§0.24 71.00(↑44.9%)§0.22
Prompt-T
24.50(↑172.2%)§0.15
66.73(↑11.5%)§0.15 33.00(↑144.4%)§0.20
60.26(↑33.3%)§0.24
24.50(↑48.5%)‡0.07
67.75(↑2.7%) 𝑛𝑠0.06
31.50(↑50%)§0.10
52.21(↑20.5%)§0.12
50.50(↑3.1%)𝑛𝑠0.01
Decode
11.00(↑22.2%)†0.02
60.12(↑0.4%)𝑛𝑠−0.01
19.50(↑44.4%)†0.06
47.98(↑6.2%)𝑛𝑠0.04
29.00(↑75.8%)§0.12
71.69(↑8.6%)§0.14
33.50(↑59.5%)§0.12
55.60(↑28.3%)§0.17
64.00(↑30.6%)§0.15
Post
10.00(↑11.1%)†0.01
61.13(↑2.1%)𝑛𝑠0.02
16.00(↑18.5%)†0.03
47.78(↑5.7%)†0.04
22.00(↑33.3%)‡0.05
68.23(↑3.4%)†0.05
27.00(↑28.6%)‡0.06
48.99(↑13.1%)§0.08
54.50(↑11.2%)‡0.06
Answer to RQ3: Overall, enhancing LLMs with static analysis achieves better effectiveness in repository-level
code completion than enhancing LLMs with RAG. In addition, static analysis and RAG are complementary,
and combining them can further make a better repository-level code completion technique. For efficiency,
prompting-phase integration is more cost-effective than Naive RAG, especially for the token-level dependency,
which achieves the best efficiency performance. In addition, all two-phase combination strategies without
beam search are more cost-effective than RepoCoder.
5.4
RQ4: Generalization
In this section, we studied whether our findings about the performance differences among different static analysis
integration strategies and RAG-based strategies can be generalized to other LLMs.
5.4.1
Generalization on larger-scale LLMs. Table 7 presents the effectiveness of individual static analysis integra-
tion strategies and RAG-based strategies on 200 random samples for two larger-scale LLMs (i.e., Claude-4.5-
Sonnet and Qwen3-Coder-30B-A3B-Instrunct). The decoding-phase and post-processing-phase integration
strategies are not allowed for Claude-4.5-Sonnet due to its closed-source nature, and therefore are excluded. Over-
all, for larger-scale LLMs, the prompting-phase static analysis integration strategy still significantly outperforms
decoding-phase and post-processing-phase integration strategies, which is consistent with our findings in RQ1.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 18](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-18.png)

![Página PDF 18, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-18.png)


<!-- PDF page 19 -->

## Página PDF 19

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
19
Table 8. Results of individual integration strategies on 7B-scale general-purpose LLMs on 200 samples. Numbers in parentheses
show the relative improvement over in-file generation.
LLM
Strategy
Python
Java
Code Match
Identifier Match
Code Match
Identifier Match
Compilation
Rate
Line EM
Line ES
EM
F1
Line EM
Line ES
EM
F1
DeepSeek
7B
In-file
4.00
55.77
9.00
40.15
17.00
71.33
23.50
50.31
54.50
Naive RAG
13.00(↑225.0%)§0.09
63.70§0.19
21.00(↑133.3%)§0.12
51.26(↑27.7%)§0.17
29.00(↑70.6%)§0.12
75.72(↑6.2%)§0.12
34.50(↑46.8%)§0.11
58.61(↑16.5%)§0.13
62.50(↑14.7%)§0.08
RepoCoder 15.00(↑275.0%)§0.11 66.73(↑19.7%) §0.27 22.50(↑150.0%)§0.14 55.14(↑37.3%)§0.24
29.00(↑70.6%)§0.12
75.83(↑6.3%)§0.13
34.50(↑46.8%)§0.11
58.61(↑16.5%)§0.13
62.50(↑14.7%)§0.08
Prompt-F
15.50(↑287.5%)§0.12
61.93(↑11.0%)§0.13
21.50(↑138.9%)§0.12
51.28(↑27.7%)§0.17 37.00(↑117.6%)§0.20 78.97(↑10.7%)§0.22 43.00(↑83.0%)§0.20 65.89(↑31.0%)§0.24 76.00(↑39.4%)§0.21
Prompt-T
14.50(↑262.5%)§0.10
57.19(↑2.5%)𝑛𝑠0.01
18.00(↑100.0%)§0.09
44.28(↑10.3%)𝑛𝑠0.06
33.00(↑94.1%)§0.16
76.02(↑6.6%)§0.14
38.50(↑63.8%)§0.15
61.77(↑22.8%)§0.17
67.00(↑22.9%)§0.12
Decode
11.00(↑175.0%)§0.07
59.20(↑6.2%)‡0.08
18.50(↑105.6%)§0.10
49.20(↑22.5%)§0.14
27.50(↑61.8%)§0.10
73.52(↑3.1%)§0.07
34.00(↑44.7%)§0.10
60.03(↑19.3%)§0.15
69.50(↑27.5%)§0.15
Post
6.50(↑62.5%)†0.03
55.21(↓1.0%)𝑛𝑠0.02
10.00(↑11.1%)𝑛𝑠0.01
40.56(↑1.0%)𝑛𝑠0.01
24.00(↑41.2%)§0.07
73.38(↑2.9%)§0.06
30.50(↑29.8%)§0.07
55.56(↑10.4%)§0.08
69.00(↑26.6%)§0.14
Llama2
7B
In-file
1.50
55.05
6.00
37.64
19.00
71.56
27.00
51.58
58.50
Naive RAG
13.50(↑800.0%)§0.12
63.20(↑14.8%)§0.19
22.00(↑266.7%)§0.16
50.72(↑34.8%)§0.20
28.50(↑50.0%)§0.10
77.23(↑7.9%)§0.15
36.50(↑35.2%)§0.10
61.26(↑18.8%)§0.14
63.50(↑8.5%)†0.05
RepoCoder 13.50(↑800.0%)§0.12
65.86(↑19.6%)§0.26 22.50(↑275.0%)§0.17 54.92(↑45.9%)§0.27
27.50(↑44.7%)‡0.09
76.46(↑6.8%)§0.13
34.50(↑27.8%)‡0.07
59.99(↑16.3%)§0.12
62.50(↑6.8%)†0.04
Prompt-F
15.00(↑900.0%)§0.14
61.18(↑11.1%)§0.13
20.00(↑233.3%)§0.14
49.72(↑32.1%)§0.19
34.50(↑81.6%)§0.15
77.24(↑7.9%)§0.16
43.00(↑59.3%)§0.16 64.77(↑25.6%)§0.19 77.00(↑31.6%)§0.18
Prompt-T
9.50(↑533.3%)§0.08
56.77(↑3.1%)§0.04
13.50(↑125.0%)§0.07
41.79(↑11.0%)§0.06
34.00(↑78.9%)§0.15
77.06(↑7.7%)§0.15
41.00(↑51.9%)§0.14
63.51(↑23.1%)§0.18
70.50(↑20.5%)§0.12
Post
4.00(↑166.7%)†0.03
53.56(↓2.7%)𝑛𝑠0.04
7.50(↑25.0%)𝑛𝑠0.01
37.22(↓1.1%)𝑛𝑠0.01
25.00(↑31.6%)‡0.06
73.93(↑3.3%)‡0.06
32.00(↑18.5%)†0.05
55.21(↑7.0%)†0.05
70.00(↑19.7%)§0.12
Furthermore, in comparison with RAG-based approaches, for the Claude-Sonnet-4.5 model, the prompting-phase
integration strategy generally outperforms both RAG-based strategies (i.e., Naive RAG and RepoCoder). However,
for the Qwen3-Coder-30B-A3B-Instruct model, although both prompting-phase integration strategies outperform
Naive RAG, the completion performance of RepoCoder and the prompting-phase integration strategy with
token-level dependencies is comparable (e.g., the line EM is 24.5 for both strategies on Python and Java subsets).
However, as presented in Table 6, the overall latency of RepoCoder is 156.6%–186.8% higher than that of the
prompting-phase strategy with token-level dependencies. Therefore, static analysis still demonstrates greater
practical value than RAG-based strategies in repository-level code completion.
5.4.2
Generalization on equal-scale general-purpose LLMs. Table 8 presents the effectiveness of individual static
analysis integration strategies and RAG-based strategies on 200 random samples for two general-purpose LLMs
(i.e., DeepDeek-7B and Llama-2-7B). Overall, the performance of general-purpose LLMs is significantly lower
than that of corresponding coding LLMs. For example, Llama-2-7B achieves the lowest line EM (1.50) in the In-file
setting in Python subsets. In addition, the prompting-phase integration strategy with file-level dependencies
still outperforms Naive RAG and even surpasses RepoCoder. Meanwhile, RAG-based strategies outperform the
decoding-phase and post-processing-phase integration strategies. However, similar to our findings on larger-scale
LLMs, RepoCoder achieves better results than the prompting-phase integration with token-level dependencies.
Specifically, on the Llama-2-7B model, RepoCoder achieves a line EM of 13.5, whereas Prompt-T only reaches
9.5. This might be attributed to the fact that general-purpose LLMs have been trained more extensively on RAG
scenarios and therefore adapt better to RAG. However, this improvement is at the cost of a 156.6%–186.8% increase
in latency.
Answer to RQ4: For larger-scale LLMs and general-purpose LLMs, the prompting-phase integration strategies
still achieve an overall better performance than Naive RAG and RepoCoder, and all RAG-based strategies still
outperform the decoding-phase and post-processing-phase strategies. However, in Python code completion
tasks, RepoCoder can achieve comparable or even better performance than the prompting-phase integration
with token-level dependencies, which might be attributed to the better adaptation of general-purpose LLMs
in RAG scenarios.
6
Discussion
In this section, we further discuss the potential to mitigate the negative effects of imprecise static analysis,
language features that might impact the practical applicability, and the implications of our findings.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 19](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-19.png)

![Página PDF 19, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-19.png)


<!-- PDF page 20 -->

## Página PDF 20

20
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Fig. 6. Completion performance of Deepseek-Coder-6.7B under the decoding-phase integration strategy as the probability
threshold varies on 200 samples.
6.1
Robustness Enhancement for Imprecise Static Analysis
In this section, we explore strategies to mitigate the impact of imprecise static analysis in dynamic languages.
As discussed in RQ2, some bad cases degrade the performance of decoding-phase integration strategies, causing
line EM to drop when combined with other strategies. Although fully resolving the challenge of imprecise static
analysis in dynamic languages remains open, we explore strategies to mitigate its negative impact on integration
approaches and enhance the robustness of our framework.
Probability Threshold. The naive strategy is to skip static-analysis-based decoding intervention when the
model predicts a high-probability token. As an initial attempt, we introduced a simple probability threshold: if the
LLM’s top-1 token probability exceeds a predefined threshold, the intervention is skipped. We randomly sampled
200 tasks and tested thresholds ranging from 0.1 to 0.9 with a step size of 0.1. We also added a baseline with a
threshold of 0.99 to examine whether removing the decoding intervention when the LLM is highly confident
will lead to any improvement. Figure 6 illustrates that all configurations with a threshold led to performance
degradation. When the LLM is uncertain, the top-1 probability is mainly distributed around 0.5. Therefore,
introducing decoding intervention around 0.5 yields a suboptimal value. However, the suboptimal value is still
significantly lower than the result without a threshold (line EM dropped by 21.6%). This indicates that high
model confidence does not reliably correspond to correct API usage. In fact, the largest performance gain occurs
between 0.99 and 1 (w/o threshold), indicating that the LLM tends to produce highly confident outputs that
are still hallucinations. This reinforces the value of decoding-phase integration strategies, which correct model
hallucinations using objectively available APIs. This reinforces the value of decoding-phase integration strategies,
which correct model hallucinations using objectively existing APIs.
Characteristics-based Classifier. The experimental results from the initial attempt, along with the distribution
shown in Figure 4, indicate that a more flexible approach is required to mitigate the negative effects of static
analysis errors while minimizing interference with correct completions. Therefore, inspired by prior studies [29,
52, 80], we adopt a lightweight strategy by training a logistic regression classifier to identify imprecise static
analysis scenarios based on the characteristics of bad cases.
In particular, in scenarios involving Global Variables, the API to be called does not appear in the preceding code
context, which cannot be resolved when only the prior code context is provided. We therefore adopt a heuristic:
if the API caller is defined via the global keyword, the intervention is skipped. In scenarios involving String
Prefixes or List/Tuple Comprehensions, the system may bias correct completions toward APIs defined in the prior
context, keywords, or built-in functions. This can be partially mitigated by checking whether all language-server
candidates belong to these categories. For cases with Dynamic Parameters, the language server fails to resolve
accurate completions and instead returns numerous “magic methods.” For instance, if concrete arguments cannot
be inferred (e.g., from args), the server may suggest methods like __dict__, leading to completion errors.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 20](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-20.png)

![Página PDF 20, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-20.png)


<!-- PDF page 21 -->

## Página PDF 21

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
21
Table 9. Results of decoding-phase integration strategy by incorporating the classifier (Decode*). Numbers in the parentheses
show the relative improvement over the strategy without the classifier.
LLM
Strategy
Python
Code Match
Identifier Match
Line EM
Line ES
EM
F1
DeepSeek-Coder
6.7B
Decode*
17.11(↑6.8%)§0.01
65.15(↑1.9%)§0.03
25.85(↑10.6%)§0.02
56.49(↑4.0%)§0.03
Prompt-F + Decode*
29.31(↑4.6%)§0.01
72.50(↑2.4%)§0.03
39.23(↑6.3%)§0.03
66.46(↑3.9%)§0.04
Prompt-T + Decode*
25.37(↑3.5%)§0.01
69.58(↑2.2%)§0.03
34.96(↑6.6%)§0.02
62.69(↑3.5%)§0.03
StarCoderBase
7B
Decode*
14.11(↑7.8%)§0.01
63.58(↑2.2%)§0.03
23.13(↑11.6%)§0.02
54.35(↑4.3%)§0.03
Prompt-F + Decode*
25.00(↑4.2%)§0.01
69.62(↑2.1%)§0.03
34.19(↑8.8%)§0.03
62.56(↑3.6%)§0.03
Prompt-T + Decode*
21.79(↑4.7%)§0.01
66.37(↑2.7%)§0.04
30.57(↑7.1%)§0.02
57.87(↑4.1%)§0.03
However, these characteristics alone are insufficient to reliably identify erroneous completions. For example, a
String-type API caller may legitimately return many built-in APIs, but static analysis may still be useful if the
LLM cannot infer the type from context. Conversely, many built-in APIs for a non-built-in caller may indicate
guesswork rather than accurate predictions. Similarly, predicting a magic method does not always indicate an
error. Based on these observations, we define four features that jointly capture information from the prompt,
language server, and model prediction behavior:
• Whether the API Caller is of a built-in type (e.g., String).
• Whether each API candidate returned from the language server satisfies at least one of: (1) is defined in
the prior context, (2) is a built-in API, or (3) is a language keyword.
• Whether the top-1 prediction is a magic method before intervention.
• Whether the top-1 prediction is a magic method after intervention.
Based on these features, we train a logistic regression classifier to predict whether the correct API is included
in the language server’s completion list. The classifier leverages the prompt information, the completion list
from the language server, and model predictions to decide whether to apply static-analysis-based intervention,
enabling tighter and more adaptive integration.
We evaluate this approach with the widely-adopted 10-fold cross-validation [10, 51, 67], partitioning the
dataset into ten subsets. Each subset serves as the test set once, with results aggregated across folds. As shown
in Table 9, our method consistently improves performance for decoding-phase integration alone and when
combined with prompting-phase integration, achieving 3.5%-7.8% relative improvement of line EM. Notably,
after using the classifier, the combinations of prompting-phase integration with file-level dependency and the
decoding-phase integration strategy achieve superior or comparable performance to that of the combination
with the post-processing integration strategy (i.e., the line EM is 29.31 vs. 28.74 for DeepSeek-Coder and 25.00 vs.
25.09 for StarCoderBase). This indicates that our approach has substantially mitigated the negative impact of
imprecise static analysis on both individual and combined integration strategies. Although we use DeepSeek-
Coder to obtain top-1 predictions before and after intervention during training, the proposed method does not
rely on specific probability values, but rather on general prediction patterns (e.g., the tendency to predict magic
methods). Therefore, it is not model-specific, evidenced by consistent improvements when applying this approach
to StarCoderBase. Finally, our approach introduces negligible computational overhead. Both the language server
outputs and model prediction probabilities are readily available, and the logistic regression classifier is lightweight.
As such, the method is efficient and practical for real-world deployment.
6.2
Cross-Language Applicability
While we propose a lightweight strategy to mitigate the negative effects of imprecise static analysis, the
effectiveness of static-analysis-integration strategies is inherently influenced by the precision and completeness
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 21](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-21.png)

![Página PDF 21, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-21.png)


<!-- PDF page 22 -->

## Página PDF 22

22
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
of static analysis, which can vary depending on language features. In this section, we discuss language features
that might affect the completion performance and provide guidance on the practical usage of STALL+.
Type system strength and explicitness. Languages with strong and explicit static typing generally enable
more accurate static analysis, since types and API usage can be resolved more reliably. For example, Java and
Go explicitly declare most types, which helps tools precisely identify API definitions and call sites. Rust also
benefits from a strong type system and explicit module structure. In contrast, dynamically typed languages such
as JavaScript make it more difficult to statically infer object structures or available APIs, especially when variable
types change across contexts.
Dynamic language features and runtime code generation. Features that allow program behavior to
be modified at runtime can significantly reduce static analysis accuracy. JavaScript is a typical example, with
mechanisms such as dynamic property access, prototype manipulation, and dynamically generated imports. These
features make it difficult to statically determine which APIs are available at a given point, which can weaken the
effectiveness of prompt augmentation and decoding constraints.
Metaprogramming and macro systems. Languages that heavily rely on macros or metaprogramming can
implicitly generate code that is not directly visible in the source, complicating static analysis. For example, C++
uses extensive preprocessor macros and template metaprogramming, which may generate large amounts of
implicit code during compilation. Similarly, Rust supports powerful macro systems (e.g., procedural macros) that
expand into additional code, which static analyzers must resolve before accurate API extraction is possible.
Advanced abstraction mechanisms (e.g., generics and interfaces). Some language features introduce
additional complexity in resolving concrete APIs. For example, C++ templates and Rust generics may require
complex type instantiation during compilation, making it harder to identify concrete API instances statically. In
Go, interfaces are widely used and implemented implicitly, which may create ambiguity when determining the
concrete type behind an interface variable.
Overall, although the effectiveness of our approach may be influenced by the aforementioned language
features, our experiments show that even simple integration of statically extracted contextual information (e.g.,
API definitions) already leads to code completion performance that significantly surpasses RAG-based approaches
for both static languages (e.g., Java) and dynamic languages (e.g., Python). The advances of mature language
servers in modern language ecosystems will increasingly improve the applicability and performance of our
approach in more languages. Moreover, STALL+ is designed to flexibly integrate static analysis at multiple
phases, including the prompting phase, decoding phase, and post-processing phase. These components can
be used independently or combined, allowing users to tailor the integration strategy to the characteristics of
different languages. For example, for dynamically typed languages where static analysis may be less precise (e.g.,
JavaScript), users may prefer integrating static analysis in the prompting and post-processing phases to obtain
stable improvements without overly restricting generation. Moreover, our exploration on using heuristic rules
and simple classifiers to mitigate the language-specific issues in Python also serve as a practical reference. In
contrast, for statically typed languages with more accurate static analysis (e.g., Go or Rust), users can further
incorporate decoding-time constraints to guide token generation more aggressively and potentially achieve
stronger completion performance.
6.3
Implications
We then discuss the implications for practition and future research.
Customize enhancement strategies for different scenarios. STALL+ enables flexible integration of RAG
and static analysis strategies across different phases of LLM-based repository-level code completion, offering
adaptable solutions for diverse practical scenarios. In cost-sensitive settings, integrating file-level dependencies
during the prompting stage provides a cost-effective enhancement. In contrast, for effectiveness-sensitive scenar-
ios, further combining RAG and static analysis in the decoding and post-processing stages yields state-of-the-art
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 22](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-22.png)

![Página PDF 22, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-22.png)


<!-- PDF page 23 -->

## Página PDF 23

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
23
performance. Strategy combination can also be tailored to programming language characteristics. As shown
in Table 3, static languages (e.g., Java) benefit from integrating static analysis during both the prompting and
decoding phases, whereas dynamic languages (e.g., Python) achieve optimal results when static analysis is applied
during the prompting and post-processing phases. By supporting customizable integration of multiple enhance-
ment strategies, STALL+ adapts to diverse practical scenarios and provides extensibility for the development of
novel static analysis methods.
More flexible integration strategies for static analysis to address its precision limitations. Our findings
reveal that the imprecise analysis results returned by static analysis (especially for dynamic language) sometimes
can restrict the improvements from static analysis on LLM-based repository-level code completion. However, the
current integration strategies in the decoding phase assign the dominant importance to the static analysis (e.g.,
the tokens or statements that are identified as invalid would be directly filtered out). This dominance might lead
to errors, particularly when static analysis is not sufficiently accurate (e.g., for dynamic languages like Python).
Therefore, to address this issue, it is important to design more flexible integration strategies that can tolerate the
imprecise analysis results of static analysis. In our work, we propose a simple yet effective machine learning
classification strategy. However, developing more effective integration strategies remains an important research
area.
Self-admitted static analysis errors for language servers. Language servers (e.g., Jedi[4]) often attempt
to provide incomplete or speculative recommendations when analysis encounters unresolved obstacles. In
collaboration with human developers, such recommendations can be filtered based on developers’ experience.
However, in interactions with LLMs, providing incomplete or inaccurate completions may be more harmful
than explicitly throwing a warning or error, as it risks misleading the LLM. As increasing research focuses
on leveraging language servers to provide static analysis support for LLM-based agents [9, 28, 65, 74, 86], the
negative effects of imprecise static analysis may be amplified. Explicitly marking self-admitted static analysis
warnings or errors can allow LLMs to better evaluate the reliability of the analysis, thereby enabling a more
precise integration.
More advanced baselines for future evaluation. Our findings demonstrate that combining multiple static
analysis integration strategies with an RAG-based approach achieves the best accuracy for repository-level code
completion, which can serve as the new state-of-the-art baseline for LLM-based repository-level code completion.
In addition, our findings also recommend different integration strategies for the application scenarios with
different latency requirements, i.e., prompting-phase integration strategies for the best cost-effectiveness whereas
prompting-phase with post-processing-phase for the best accuracy but less efficiency.
More diverse representation of dependencies in the prompt. Given the superiority of file-level dependen-
cies over token-level dependencies in our findings, we believe that how to represent the dependencies extracted
by static analysis in the prompt is essential for the accuracy of the code completion. In addition, the impact of
dependency representation might also be associated with how the dependencies are organized in the model
pre-training phase. Currently, there is a rather limited exploration of how to represent the dependencies of
static analysis in the prompt, which can be very important future work to systematically explore more diverse
dependency representations for repository-level code completion.
7
Threats to Validity and Limitations
In this section, we discuss some threats to the validity of our framework and findings.
Biases of Static Analysis Tools. This work explores the enhancement of static analysis in LLM-based
repository-level code completion. However, the enhancement is impacted by the implementation of the static
analysis tools, and it is still an open challenge to conduct precise static analysis in dynamically typed languages
due to their dynamic nature. To mitigate this threat to the validity of our findings, we build our framework
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 23](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-23.png)

![Página PDF 23, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-23.png)


<!-- PDF page 24 -->

## Página PDF 24

24
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
on top of a well-established and widely-used static analysis toolkit such as tree-sitter [8], Jedi [4], and Eclipse
JDT [3]. We also explore a lightweight approach to mitigate the negative effects of imprecise static analysis by
training a classifier. However, employing static analysis tools that are less established or applying this framework
to programming languages lacking precise static analysis tools might still introduce performance biases in the
results.
Data and Model Generalizability. In our experiments, we utilize various state-of-the-art LLMs and test them
on both statically and dynamically typed languages. However, due to the varying complexities of static analysis
across different programming languages and the differences in model capabilities for context understanding, the
experimental findings might be specific to the benchmarks and code LLMs employed in our study.
Biases of Evaluation Metrics. Although similarity-based metrics are currently the most widely used evalua-
tion metrics for repository-level code completion tasks, they do not accurately assess the correctness of generated
code. For instance, they cannot distinguish between semantically similar but syntactically different code. To
mitigate this, we introduce a new metric, Compilation Rates, which measures whether the generated code can be
successfully compiled in its target environment. This metric provides a more practical indication of code usability
by directly evaluating syntactic correctness and integration feasibility within the repository context. A more
accurate metric would be the test pass rate. However, for line-level code completion, it is difficult to ensure that
the generated code is actually tested by oracle assertions. Moreover, most existing datasets do not guarantee the
testability of tasks. Addressing this limitation remains an important research direction for future work.
Efficiency of Combined Strategies. Although our framework supports customizable integration of static
analysis strategies in different phases, applying static analysis strategies in the decoding and post-processing
phases simultaneously might be time-consuming for the code completion task, as we mentioned in Section 5.2.
To mitigate this limitation, we aim to reduce the overhead of online static analysis by caching the available API
context of active objects in the current line offline. In addition, we aim to propose new decoding algorithms to
accelerate the process of masking output tokens with static analysis.
Integration with Closed-source LLMs. Our framework is model-agnostic and can be applied to any LLM.
However, for closed-source models like GPT-3.5 and GPT-4, their closed-source nature prevents integration
during the decoding stage. Nonetheless, our framework remains compatible with closed-sourced models at the
prompting and post-processing stages, which suffices for most practical use cases.
8
Related Work
8.1
Synergy between Static Analysis and LLM
To mitigate the hallucination of LLM-based generation, there is an increasing body of research combining LLMs
with static analysis techniques/tools to facilitate more powerful LLM-based solutions for software engineering
tasks. For example, in automated program repair [13], RepairAgent [12] leverages static analysis to extract
information for LLM-based repair; PyTy [18] utilizes the type checker to verify whether each LLM-generated
candidate accurately fixes static type errors. For bug detection, SkipAnalyzer [53] filters warnings from both LLM
and static detection Infer; and GPTScan [66] employs static analysis to validate crucial variables and statements
recognized by LLM, which allows to determine the existence of vulnerabilities with confidence. In addition, in
software testing [42, 75], CodaMosa [37] combines traditional search-based test generation with LLM-based test
generation; TECO [55] trains transformer for test completion based on the semantic features extracted by static
analysis; ChatTester [83] and TestPilot [61] leverage static analysis to prepare context information for the iterative
LLM-based test code repair. The work above demonstrates the promise of combining static analysis and LLMs in
different tasks. In contrast, our work systematically investigates the use of static analysis on repository-level
code completion tasks and offers practical implications for future research.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 24](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-24.png)

![Página PDF 24, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-24.png)


<!-- PDF page 25 -->

## Página PDF 25

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
25
8.2
LLM-based Code Completion
To date, many efforts have been dedicated to the LLM-based code completion [84, 88], including code LLM
training [1, 31, 41, 48, 56, 60, 78], prompting engineering [40, 77, 89], benchmarks [11, 15, 17, 21, 24, 47, 50],
and empirical studies [19, 19, 34, 36, 62, 69, 76]. In particular, repository-level code completion is a practical
and challenging code completion scenario, while RAG-based and static analysis-integrated techniques are two
mainstream LLM-based repository-level code completion techniques. For RAG-based techniques [49, 79, 85],
researchers enhance LLMs by prompting with similar code in the repository, mainly through designing different
retrieval strategies (e.g., dual-encoder model [49]) with different pipelines (e.g., selectively or iteratively triggering
RAG [79, 85]). In contrast, our work focuses on the static analysis-integrated techniques, which are orthogonal
to these RAG-based techniques; in addition, our framework is compatible with further combining RAG-based
techniques, which has demonstrated promising effectiveness in our experiments. For static analysis-integrated
techniques [9, 22, 63, 74], researchers focus on integrating static analysis into different phases (e.g., prompting
phase or decoding phase) of LLM-based repository-level code completion. In particular, CoCoMIC and RLPG
propose to extract dependent code from the repository and then include the extracted contexts during prompting.
MGD [9] and ToolGen [74] adjust the token probabilities based on the results returned by static analysis during
decoding. Compared with existing work that integrates static analysis, our work extends the boundary of this
research area in the following aspects. First, we present the first empirical study that systematically compares the
effectiveness and efficiency of integration strategies across different phases, and further analyzes the differences
and complementarity between the static-analysis–integrated category and the RAG-based category. Second,
we propose two novel static-analysis integration strategies: the prompting-phase integration with token-level
dependencies and the post-processing-phase integration strategy. The integration with token-level dependencies
overall outperforms RAG-based strategies and decoding-phase integration strategy, and is the most efficient
strategy. The post-processing-phase integration achieves consistent and significant combined improvements
compared with decoding-phase integration. Third, to address bad cases observed in decoding-phase strategies, we
design a lightweight logistic regression classifier that enables the model to selectively apply the decoding-phase
integration strategy and significantly improve the effectiveness.
In addition, from the perspective of integration level, STALL+ also differs from traditional language server–based
completion and existing tool-augmented methods in that it forms a unified inference pipeline spanning three
phases of LLM inference, including prompting, decoding, and post-processing, whereas prior approaches typically
treat static analysis as a single-phase auxiliary component or an external tool.
9
Conclusion
This work proposes the framework STALL+, which supports customizable integration of multiple static analysis
strategies into different phases of LLM-based repository-level code completion. Based on STALL+, we conduct the
first systematic study of static analysis integration for repository-level code completion with LLMs. Experiments
across three code LLMs and the CrossCodeEval benchmark show that all static-analysis-based approaches consis-
tently outperform in-file baselines on repository-level completion tasks. Among these approaches, integrating
file-level dependencies during the prompting phase consistently achieves the best completion effectiveness, while
integrating token-level dependencies provides the highest efficiency. Moreover, different integration strategies
also exhibit complementarity, and combining them can further improve completion accuracy. However, the effec-
tiveness of static-analysis integration is inherently constrained by the precision of the underlying static analysis.
Consequently, performance is less stable on dynamic languages such as Python, especially for decoding-phase
integration, where inaccurate analysis may even degrade completion performance. Based on failure-case analysis,
we conduct an exploratory experiment to investigate a lightweight classifier-based enhancement approach, which
demonstrates promising potential for improving the robustness of static-analysis integration in the decoding
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 25](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-25.png)

![Página PDF 25, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-25.png)


<!-- PDF page 26 -->

## Página PDF 26

26
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
phase. We also compare static-analysis integration strategies with RAG-based strategies under the prefix-only
setting. Overall, the evaluated RAG-based approaches perform worse than prompting-phase static-analysis
integration, but outperform decoding-phase and post-processing-phase integration strategies. In some sampled
experiments involving larger-scale LLMs and general-purpose LLMs, RepoCoder remains competitive with
the token-level dependency integration strategy. Nevertheless, given the substantial overhead introduced by
RepoCoder’s two-round generation process, prompting-phase integration with token-level dependencies remains
a more practical and efficient choice. Finally, by combining RAG and static analysis integration strategies, we
achieve state-of-the-art performance on CrossCodeEval, demonstrating the strong complementarity between
these two mainstream approaches for repository-level code completion.
Acknowledgments
This work was supported by the Key R&D Program of Shandong Province, China (Project No. 2025CXPT073).
References
[1] 2021. Codex. https://openai.com/blog/openai-codex.
[2] 2022. OpenAI: Introducing ChatGPT. https://openai.com/blog/chatgpt/.
[3] 2024. eclipse.jdt.ls. https://github.com/eclipse-jdtls/eclipse.jdt.ls.
[4] 2024. jedi-language-server. https://github.com/pappasam/jedi-language-server.
[5] 2024. pylint. https://github.com/pylint-dev/pylint.
[6] 2024. sentencepiece. https://github.com/google/sentencepiece.
[7] 2024. stall+. https://anonymous.4open.science/r/STALL.
[8] 2024. tree-sitter. https://github.com/tree-sitter/tree-sitter.
[9] Lakshya A Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K. Lahiri, and Sriram K. Rajamani. 2023. Guiding Language Models of
Code with Global Context using Monitors. CoRR abs/2306.10763 (2023). https://doi.org/10.48550/ARXIV.2306.10763 arXiv:2306.10763
[10] Abdullah Alsaeedi and Mohammad Zubair Khan. 2019. Software defect prediction using supervised machine learning and ensemble
techniques: a comparative study. Journal of Software Engineering and Applications 12, 5 (2019), 85–100.
[11] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, and David Dohan et al. 2021. Program Synthesis
with Large Language Models. ArXiv abs/2108.07732 (2021). https://api.semanticscholar.org/CorpusID:237142385
[12] Islem Bouzenia, Prem Devanbu, and Michael Pradel. 2024. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair.
https://api.semanticscholar.org/CorpusID:268692056
[13] Islem Bouzenia, Yangruibo Ding, Kexin Pei, Baishakhi Ray, and Michael Pradel. 2023. TraceFixer: Execution Trace-Driven Program
Repair. CoRR abs/2304.12743 (2023). https://doi.org/10.48550/ARXIV.2304.12743 arXiv:2304.12743
[14] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, Sandhini Agarwal, and Ariel Herbert-Voss et al. 2020. Language Models are Few-Shot Learners. ArXiv
abs/2005.14165 (2020). https://api.semanticscholar.org/CorpusID:218971783
[15] Federico Cassano, John Gouwar, Daniel Nguyen, Sydney Nguyen, and Phipps-Costin et al. 2023. MultiPL-E: A Scalable and Polyglot
Approach to Benchmarking Neural Code Generation. IEEE Transactions on Software Engineering 49, 7 (July 2023), 3675–3691. https:
//doi.org/10.1109/TSE.2023.3267446
[16] J. Chen, X. Hu, Z. Li, C. Gao, X. Xia, and D. Lo. 2024. Code Search Is All You Need? Improving Code Suggestions With Code Search. In
2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE). IEEE Computer Society, Los Alamitos, CA, USA, 857–857.
https://doi.ieeecomputersociety.org/
[17] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde, Jared Kaplan, Harrison Edwards, Yura Burda, Nicholas Joseph,
Greg Brockman, Alex Ray, Raul Puri, and Gretchen Krueger et.al. 2021. Evaluating Large Language Models Trained on Code. ArXiv
abs/2107.03374 (2021). https://api.semanticscholar.org/CorpusID:235755472
[18] Yiu Wai Chow, Luca Di Grazia, and Michael Pradel. 2024. PyTy: Repairing Static Type Errors in Python. ArXiv abs/2401.06619 (2024).
https://api.semanticscholar.org/CorpusID:266977080
[19] Matteo Ciniselli, Nathan Cooper, and Luca Pascarella et al. 2021. An Empirical Study on the Usage of Transformer Models for Code
Completion. IEEE Transactions on Software Engineering 48 (2021), 4818–4837. https://api.semanticscholar.org/CorpusID:236881348
[20] Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming Zhang. 2023. Large Language Models Are Zero-Shot
Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models. In Proceedings of the 32nd ACM SIGSOFT International Symposium
on Software Testing and Analysis (<conf-loc>, <city>Seattle</city>, <state>WA</state>, <country>USA</country>, </conf-loc>) (ISSTA
2023). Association for Computing Machinery, New York, NY, USA, 423–435. https://doi.org/10.1145/3597926.3598067
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 26](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-26.png)

![Página PDF 26, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-26.png)


<!-- PDF page 27 -->

## Página PDF 27

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
27
[21] Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, and Nihal Jain et al. 2023. CrossCodeEval: A Diverse and
Multilingual Benchmark for Cross-File Code Completion. In Advances in Neural Information Processing Systems 36: Annual Conference
on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023, Alice Oh, Tristan Naumann,
Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine (Eds.).
[22] Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth,
and Bing Xiang. 2022. CoCoMIC: Code Completion By Jointly Modeling In-file and Cross-file Context. CoRR abs/2212.10007 (2022).
https://doi.org/10.48550/ARXIV.2212.10007 arXiv:2212.10007
[23] Shihan Dou, Yan Liu, Haoxiang Jia, Limao Xiong, Enyu Zhou, Junjie Shan, Caishuang Huang, Wei Shen, Xiaoran Fan, Zhiheng Xi, et al.
2024. StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback. arXiv preprint arXiv:2402.01391
(2024).
[24] Xueying Du, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, Yixuan Chen, Jiayi Feng, Chaofeng Sha, Xin Peng, and Yiling Lou.
2024. Evaluating Large Language Models in Class-Level Code Generation. In 2024 IEEE/ACM 46th International Conference on Software
Engineering (ICSE). IEEE Computer Society, 865–865.
[25] Hasan Ferit Eniser, Valentin Wüstholz, and Maria Christakis. 2024. Automatically testing functional properties of code translation
models. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38. 21055–21062.
[26] Angela Fan, Beliz Gokkaya, Mark Harman, Mitya Lyubarskiy, Shubho Sengupta, Shin Yoo, and Jie M. Zhang. 2023. Large Language Models
for Software Engineering: Survey and Open Problems. In IEEE/ACM International Conference on Software Engineering: Future of Software
Engineering, ICSE-FoSE 2023, Melbourne, Australia, May 14-20, 2023. IEEE, 31–53. https://doi.org/10.1109/ICSE-FOSE59343.2023.00008
[27] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, and Ming Gong et al. 2020. CodeBERT: A Pre-Trained Model
for Programming and Natural Languages. In Findings of the Association for Computational Linguistics: EMNLP 2020, Online Event,
16-20 November 2020 (Findings of ACL, Vol. EMNLP 2020), Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association for Computational
Linguistics, 1536–1547. https://doi.org/10.18653/V1/2020.FINDINGS-EMNLP.139
[28] Gwihwan Go, Chijin Zhou, Quan Zhang, Yu Jiang, and Zhao Wei. 2025. LSPAI: An IDE Plugin for LLM-Powered Multi-Language Unit
Test Generation with Language Server Protocol. In Proceedings of the 33rd ACM International Conference on the Foundations of Software
Engineering. 144–149.
[29] Sai Krishna Gunda. 2024. Comparative analysis of machine learning models for software defect prediction. In 2024 International
Conference on Power, Energy, Control and Transmission Systems (ICPECTS). IEEE, 1–6.
[30] Daya Guo, Canwen Xu, Nan Duan, Jian Yin, and Julian Mcauley. 2023. LongCoder: A Long-Range Pre-trained Language Model for Code
Completion. In Proceedings of the 40th International Conference on Machine Learning (Proceedings of Machine Learning Research, Vol. 202),
Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett (Eds.). PMLR, 12098–12107.
https://proceedings.mlr.press/v202/guo23j.html
[31] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Y. Wu, Y. K. Li, Fuli Luo, Yingfei
Xiong, and Wenfeng Liang. 2024. DeepSeek-Coder: When the Large Language Model Meets Programming - The Rise of Code Intelligence.
CoRR abs/2401.14196 (2024). https://doi.org/10.48550/ARXIV.2401.14196 arXiv:2401.14196
[32] Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John C. Grundy, and Haoyu Wang. 2023. Large
Language Models for Software Engineering: A Systematic Literature Review. CoRR abs/2308.10620 (2023). https://doi.org/10.48550/
ARXIV.2308.10620 arXiv:2308.10620
[33] Tao Huang, Zhihong Sun, Zhi Jin, Ge Li, and Chen Lyu. 2024. Knowledge-aware code generation with large language models. In
Proceedings of the 32nd IEEE/ACM International Conference on Program Comprehension. 52–63.
[34] Maliheh Izadi, Jonathan Katzy, Tim van Dam, Marc Otten, Razvan Mihai Popescu, and Arie van Deursen. 2024. Language Models for
Code Completion: A Practical Evaluation. arXiv preprint arXiv:2402.16197 (2024).
[35] Paul Jaccard. 1912. The distribution of the flora in the alpine zone. 1. New phytologist 11, 2 (1912), 37–50.
[36] Xing Hu Junkai Che and, Zhenhao Li, Cuiyun Gao, Xin Xia, and David Lo. 2024. Code Search is All You Need? Improving Code
Suggestions with Code Search. In 2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE).
[37] Caroline Lemieux, Jeevana Priya Inala, Shuvendu K Lahiri, and Siddhartha Sen. 2023. Codamosa: Escaping coverage plateaus in test
generation with pre-trained large language models. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE).
IEEE, 919–931.
[38] Vladimir I Levenshtein et al. 1966. Binary codes capable of correcting deletions, insertions, and reversals. In Soviet physics doklady,
Vol. 10. Soviet Union, 707–710.
[39] Jingxuan Li, Rui Huang, Wei Li, Kai Yao, and Weiguo Tan. 2021. Toward less hidden cost of code completion with acceptance and
ranking models. In 2021 IEEE International Conference on Software Maintenance and Evolution (ICSME). IEEE, 195–205.
[40] Jia Li, Ge Li, Yongming Li, and Zhi Jin. 2023. Structured Chain-of-Thought Prompting for Code Generation. https://api.semanticscholar.
org/CorpusID:258615421
[41] Raymond Li, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov, Chenghao Mou, Marc Marone, Christopher Akiki, Jia
Li, Jenny Chim, Qian Liu, Evgenii Zheltonozhskii, Terry Yue Zhuo, Thomas Wang, and Olivier Dehaene et al. 2023. StarCoder: may the
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 27](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-27.png)

![Página PDF 27, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-27.png)


<!-- PDF page 28 -->

## Página PDF 28

28
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
source be with you! CoRR abs/2305.06161 (2023). https://doi.org/10.48550/ARXIV.2305.06161 arXiv:2305.06161
[42] Tsz On Li, Wenxi Zong, Yibo Wang, Haoye Tian, and Ying Wang et al. 2023. Finding Failure-Inducing Test Cases with ChatGPT. CoRR
abs/2304.11686 (2023). https://doi.org/10.48550/ARXIV.2304.11686 arXiv:2304.11686
[43] Zhan Li, Yongtao Wu, Yihang Chen, Francesco Tonin, Elias Abad Rocamora, and Volkan Cevher. 2024. Membership inference attacks
against large vision-language models. Advances in Neural Information Processing Systems 37 (2024), 98645–98674.
[44] Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, Zhenpeng Chen, Lingming Zhang, and Yiling Lou. 2024. Large language model-based
agents for software engineering: A survey. ACM Transactions on Software Engineering and Methodology (2024).
[45] Junwei Liu, Chen Xu, Chong Wang, Tong Bai, Weitong Chen, Kaseng Wong, Yiling Lou, and Xin Peng. 2025. EvoDev: An Iterative
Feature-Driven Framework for End-to-End Software Development with LLM-based Agents. arXiv preprint arXiv:2511.02399 (2025).
[46] Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the middle:
How language models use long contexts. Transactions of the Association for Computational Linguistics 12 (2024), 157–173.
[47] Tianyang Liu, Canwen Xu, and Julian McAuley. 2023. RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems.
ArXiv abs/2306.03091 (2023). https://api.semanticscholar.org/CorpusID:259075246
[48] Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi, Ao Tang, Dmytro Pykhtar,
Jiawei Liu, and Yuxiang Wei et al. 2024. StarCoder 2 and The Stack v2: The Next Generation. ArXiv abs/2402.19173 (2024). https:
//api.semanticscholar.org/CorpusID:268063676
[49] Shuai Lu, Nan Duan, Hojae Han, Daya Guo, Seung won Hwang, and Alexey Svyatkovskiy. 2022. ReACC: A Retrieval-Augmented Code
Completion Framework. ArXiv abs/2203.07722 (2022). https://api.semanticscholar.org/CorpusID:247450969
[50] Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, and Ambrosio Blanco et al. 2021. CodeXGLUE: A Machine Learning
Benchmark Dataset for Code Understanding and Generation. ArXiv abs/2102.04664 (2021). https://api.semanticscholar.org/CorpusID:
231855531
[51] Ruchika Malhotra and Shweta Meena. 2021. Empirical Validation of cross-version and 10-fold cross-validation for Defect Prediction. In
2021 Second International Conference on Electronics and Sustainable Communication Systems (ICESC). 431–438. https://doi.org/10.1109/
ICESC51422.2021.9533030
[52] Iqra Mehmood, Sidra Shahid, Hameed Hussain, Inayat Khan, Shafiq Ahmad, Shahid Rahman, Najeeb Ullah, and Shamsul Huda. 2023. A
novel approach to improve software defect prediction accuracy using machine learning. IEEE Access 11 (2023), 63579–63597.
[53] Mohammad Mahdi Mohajer, Reem Aleithan, Nima Shiri Harzevili, Moshi Wei, Alvine Boaye Belle, Hung Viet Pham, and Song Wang.
2023. SkipAnalyzer: A Tool for Static Code Analysis with Large Language Models. https://api.semanticscholar.org/CorpusID:264590515
[54] Ansong Ni, Srini Iyer, Dragomir Radev, Veselin Stoyanov, Wen-Tau Yih, Sida I. Wang, and Xi Victoria Lin. 2023. LEVER: Learning to
Verify Language-to-Code Generation with Execution. In International Conference on Machine Learning, ICML 2023, 23-29 July 2023,
Honolulu, Hawaii, USA (Proceedings of Machine Learning Research, Vol. 202), Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara
Engelhardt, Sivan Sabato, and Jonathan Scarlett (Eds.). PMLR, 26106–26128. https://proceedings.mlr.press/v202/ni23b.html
[55] Pengyu Nie, Rahul Banerjee, Junyi Jessy Li, Raymond J. Mooney, and Milos Gligoric. 2023. Learning Deep Semantics for Test Completion.
In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE). 2111–2123. https://doi.org/10.1109/ICSE48619.2023.00178
[56] Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023. CodeGen:
An Open Large Language Model for Code with Multi-Turn Program Synthesis. In The Eleventh International Conference on Learning
Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net. https://openreview.net/pdf?id=iaYcJKpY2B_
[57] NVIDIA Corporation. 2023. Deep Learning Performance Guide: Getting Started. https://docs.nvidia.com/deeplearning/performance/dl-
performance-getting-started/index.html Accessed: March 17, 2026.
[58] Xin Peng and Chong Wang. 2025. Code Digital Twin: Empowering LLMs with Tacit Knowledge for Complex Software Development.
arXiv preprint arXiv:2503.07967 (2025).
[59] Alfin Wijaya Rahardja, Junwei Liu, Weitong Chen, Zhenpeng Chen, and Yiling Lou. 2026. Can Agent Fix Agent Issues? Advances in
Neural Information Processing Systems 38 (2026), 49002–49028.
[60] Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, and Tal Remez et
al. 2023. Code Llama: Open Foundation Models for Code. CoRR abs/2308.12950 (2023). https://doi.org/10.48550/ARXIV.2308.12950
arXiv:2308.12950
[61] Max Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2023. Adaptive Test Generation Using a Large Language Model. CoRR
abs/2302.06527 (2023). https://doi.org/10.48550/ARXIV.2302.06527 arXiv:2302.06527
[62] Ensheng Shi, Yanlin Wang, Hongyu Zhang, Lun Du, Shi Han, Dongmei Zhang, and Hongbin Sun. 2023. Towards Efficient Fine-Tuning
of Pre-trained Code Models: An Experimental Study and Beyond. In Proceedings of the 32nd ACM SIGSOFT International Symposium
on Software Testing and Analysis, ISSTA 2023, Seattle, WA, USA, July 17-21, 2023, René Just and Gordon Fraser (Eds.). ACM, 39–51.
https://doi.org/10.1145/3597926.3598036
[63] Disha Shrivastava, Denis Kocetkov, and Harm de Vries et al. 2023. RepoFusion: Training Code Models to Understand Your Repository.
CoRR abs/2306.10998 (2023). https://doi.org/10.48550/ARXIV.2306.10998 arXiv:2306.10998
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 28](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-28.png)

![Página PDF 28, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-28.png)


<!-- PDF page 29 -->

## Página PDF 29

STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis
•
29
[64] Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2023. Repository-Level Prompt Generation for Large Language Models of
Code. In Proceedings of the 40th International Conference on Machine Learning (Proceedings of Machine Learning Research, Vol. 202),
Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett (Eds.). PMLR, 31693–31715.
https://proceedings.mlr.press/v202/shrivastava23a.html
[65] David Sounthiraraj, Jared Hancock, Yassin Kortam, Ashok Javvaji, Prabhat Singh, and Shaila Shankar. 2025. Code-Craft: Hierarchical
Graph-Based Code Summarization for Enhanced Context Retrieval. arXiv preprint arXiv:2504.08975 (2025).
[66] Yuqiang Sun, Daoyuan Wu, Yue Xue, and Hangbo Liu et al. 2023. GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by
Combining GPT with Program Analysis. https://api.semanticscholar.org/CorpusID:260682978
[67] Touseef Tahir, Cigdem Gencel, Ghulam Rasool, Tariq Umer, Jawad Rasheed, Sook Fern Yeo, and Taner Cevik. 2023. Early software
defects density prediction: training the international software benchmarking cross projects data using supervised learning. Ieee Access
11 (2023), 141965–141986.
[68] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman
Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. LLaMA: Open and
Efficient Foundation Language Models. ArXiv abs/2302.13971 (2023). https://api.semanticscholar.org/CorpusID:257219404
[69] Tim van Dam, Maliheh Izadi, and Arie van Deursen. 2023. Enriching Source Code with Contextual Data for Code Completion
Models: An Empirical Study. 2023 IEEE/ACM 20th International Conference on Mining Software Repositories (MSR) (2023), 170–182.
https://api.semanticscholar.org/CorpusID:258298223
[70] Yao Wan, Yang He, Zhangqian Bi, Jianguo Zhang, Hongyu Zhang, Yulei Sui, Guandong Xu, Hai Jin, and Philip S. Yu. 2024. Deep
Learning for Code Intelligence: Survey, Benchmark and Toolkit. CoRR abs/2401.00288 (2024). https://doi.org/10.48550/ARXIV.2401.00288
arXiv:2401.00288
[71] Chaozheng Wang, Junhao Hu, Cuiyun Gao, Yu Jin, Tao Xie, Hailiang Huang, Zhenyu Lei, and Yuetang Deng. 2023. Practitioners’
expectations on code completion. arXiv preprint arXiv:2301.03846 (2023).
[72] Chaozheng Wang, Junhao Hu, Cuiyun Gao, Yu Jin, Tao Xie, Hailiang Huang, Zhenyu Lei, and Yuetang Deng. 2023. Practitioners’
Expectations on Code Completion. CoRR abs/2301.03846 (2023). https://doi.org/10.48550/ARXIV.2301.03846 arXiv:2301.03846
[73] Chong Wang, Yiling Lou, Junwei Liu, and Xin Peng. 2023. Generating variable explanations via zero-shot prompt learning. In 2023 38th
IEEE/ACM International Conference on Automated Software Engineering (ASE). IEEE, 748–760.
[74] Chong Wang, Jian Zhang, Yebo Feng, Tianlin Li, Weisong Sun, Yang Liu, and Xin Peng. 2024. Teaching Code LLMs to Use Autocompletion
Tools in Repository-Level Code Generation. CoRR abs/2401.06391 (2024). https://doi.org/10.48550/ARXIV.2401.06391 arXiv:2401.06391
[75] Junjie Wang, Yuchao Huang, Chunyang Chen, Zhe Liu, Song Wang, and Qing Wang. 2024. Software Testing with Large Language
Models: Survey, Landscape, and Vision. arXiv:2307.07221 [cs.SE]
[76] Xinchen Wang, Ruida Hu, Cuiyun Gao, Xinjie Wen, Yujia Chen, and Qing Liao. 2024. ReposVul: A Repository-Level High-Quality
Vulnerability Dataset. https://api.semanticscholar.org/CorpusID:267200063
[77] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Huai hsin Chi, F. Xia, Quoc Le, and Denny Zhou. 2022. Chain of Thought
Prompting Elicits Reasoning in Large Language Models. ArXiv abs/2201.11903 (2022).
https://api.semanticscholar.org/CorpusID:
246411621
[78] Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. 2023. Magicoder: Source Code Is All You Need. ArXiv
abs/2312.02120 (2023). https://api.semanticscholar.org/CorpusID:265609970
[79] Di Wu, Wasi Uddin Ahmad, Dejiao Zhang, Murali Krishna Ramanathan, and Xiaofei Ma. 2024. Repoformer: Selective Retrieval for
Repository-Level Code Completion. arXiv preprint arXiv:2403.10059 (2024).
[80] Yanming Yang, Xin Xia, David Lo, Tingting Bi, John Grundy, and Xiaohu Yang. 2022. Predictive models in software engineering:
Challenges and opportunities. ACM Transactions on Software Engineering and Methodology (TOSEM) 31, 3 (2022), 1–72.
[81] Kai Yu, Zhenhao Zhou, Junhao Zeng, Ying Wang, Xueying Du, Zhiqiang Yuan, Junwei Liu, Ziyu Zhou, Yujia Wang, Chong Wang, et al.
2026. Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution. arXiv preprint
arXiv:2604.05955 (2026).
[82] Zhiqiang Yuan, Junwei Liu, Qiancheng Zi, Mingwei Liu, Xin Peng, and Yiling Lou. 2023. Evaluating Instruction-Tuned Large Lan-
guage Models on Code Comprehension and Generation. CoRR abs/2308.01240 (2023). https://doi.org/10.48550/ARXIV.2308.01240
arXiv:2308.01240
[83] Zhiqiang Yuan, Yiling Lou, Mingwei Liu, Shiji Ding, Kaixin Wang, Yixuan Chen, and Xin Peng. 2023. No More Manual Tests?
Evaluating and Improving ChatGPT for Unit Test Generation. CoRR abs/2305.04207 (2023). https://doi.org/10.48550/ARXIV.2305.04207
arXiv:2305.04207
[84] Daoguang Zan, B. Chen, Fengji Zhang, Di Lu, Bingchao Wu, Bei Guan, Yongji Wang, and Jian-Guang Lou. 2022. Large Language Models
Meet NL2Code: A Survey. In Annual Meeting of the Association for Computational Linguistics. https://api.semanticscholar.org/CorpusID:
258557362
[85] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen. 2023. RepoCoder:
Repository-Level Code Completion Through Iterative Retrieval and Generation. In Proceedings of the 2023 Conference on Empirical
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 29](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-29.png)

![Página PDF 29, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-29.png)


<!-- PDF page 30 -->

## Página PDF 30

30
•
Junwei Liu, Yixuan Chen, Mingwei Liu, Xin Peng, and Yiling Lou
Methods in Natural Language Processing, EMNLP 2023, Singapore, December 6-10, 2023, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.).
Association for Computational Linguistics, 2471–2484. https://aclanthology.org/2023.emnlp-main.151
[86] Mingming Zhang, Xu Wang, Jian Zhang, Xiangxin Meng, Jiayi Zhang, and Chunming Hu. 2026. VulnResolver: A Hybrid Agent
Framework for LLM-Based Automated Vulnerability Issue Resolution. arXiv preprint arXiv:2601.13933 (2026).
[87] Quanjun Zhang, Chunrong Fang, Yang Xie, Yaxin Zhang, Yun Yang, Weisong Sun, Shengcheng Yu, and Zhenyu Chen. 2023. A
Survey on Large Language Models for Software Engineering. CoRR abs/2312.15223 (2023). https://doi.org/10.48550/ARXIV.2312.15223
arXiv:2312.15223
[88] Zibin Zheng, Kaiwen Ning, Yanlin Wang, Jingwen Zhang, Dewu Zheng, Mingxi Ye, and Jiachi Chen. 2023. A survey of large language
models for code: Evolution, benchmarking, and future trends. arXiv preprint arXiv:2311.10372 (2023).
[89] Denny Zhou, Nathanael Scharli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Olivier Bousquet, Quoc Le, and
Ed Huai hsin Chi. 2022. Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. ArXiv abs/2205.10625 (2022).
https://api.semanticscholar.org/CorpusID:248986239
Received 24 June 2025; revised 11 May 2026; accepted 2 June 2026
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 30](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-30.png)

![Página PDF 30, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/STALL/page-30.png)
