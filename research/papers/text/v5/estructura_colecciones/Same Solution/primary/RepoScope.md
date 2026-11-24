# RepoScope

- source_pdf: ../../../../../pdf/Same%20Solution/primary/RepoScope.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RepoScope: Leveraging Call Chain-Aware Multi-View Context for
Repository-Level Code Generation
Yang Liu
Beihang University
Beijing, China
liuyang26@buaa.edu.cn
Li Zhang
Beihang University
Beijing, China
lily@buaa.edu.cn
Fang Liu∗
Beihang University
Beijing, China
fangliu@buaa.edu.cn
Zhuohang Wang
Beihang University
Beijing, China
wangzhuohang@buaa.edu.cn
Donglin Wei
Beihang University
Beijing, China
donglinwei@buaa.edu.cn
Zhishuo Yang
Beihang University
Beijing, China
yangzhishuo@buaa.edu.cn
Kechi Zhang
Peking University
Beijing, China
zhangkechi@pku.edu.cn
Jia Li
Peking University
Beijing, China
lijiaa@pku.edu.cn
Lin Shi
Beihang University
Beijing, China
shilin@buaa.edu.cn
Abstract
Repository-level code generation aims to generate code within
the context of a specified repository. Existing approaches typically
employ retrieval-augmented generation (RAG) techniques to pro-
vide LLMs with relevant contextual information extracted from
the repository. However, these approaches often struggle with ef-
fectively identifying truly relevant contexts that capture the rich
semantics of the repository, and their contextual perspectives re-
mains narrow. Moreover, most approaches fail to account for the
structural relationships in the retrieved code during prompt con-
struction, hindering the LLM’s ability to accurately interpret the
context. To address these issues, we propose RepoScope, which
leverages call chain-aware multi-view context for repository-level
code generation. RepoScope constructs a Repository Structural
Semantic Graph (RSSG) and retrieves a comprehensive four-view
context, integrating both structural and similarity-based contexts.
We propose a novel call chain prediction method that utilizes the
repository’s structural semantics to improve the identification of
callees in the target function. Additionally, we present a structure-
preserving serialization algorithm for prompt construction, ensur-
ing the coherence of the context for the LLM. Notably, RepoScope
relies solely on static analysis, eliminating the need for additional
training or multiple LLM queries, thus ensuring both efficiency and
generalizability. Evaluation on widely-used repository-level code
generation benchmarks (CoderEval and DevEval) demonstrates
that RepoScope outperforms state-of-the-art methods, achieving
up to a 36.35% relative improvement in pass@1 scores. Further
experiments emphasize RepoScope’s potential to improve code
∗corresponding author
This work is licensed under a Creative Commons Attribution 4.0 International License.
ICSE ’26, Rio de Janeiro, Brazil
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2025-3/26/04
https://doi.org/10.1145/3744916.3773211
generation across different tasks and its ability to integrate effec-
tively with existing approaches. We provide the replication package
at https://github.com/Lorien1128/RepoScope.
CCS Concepts
• Software and its engineering; • Computing methodologies
→Artificial intelligence;
Keywords
Repository-Level Code Generation, Call Chain Prediction, Large
Language Models, Retrieval-Augmented Generation
ACM Reference Format:
Yang Liu, Li Zhang, Fang Liu, Zhuohang Wang, Donglin Wei, Zhishuo Yang,
Kechi Zhang, Jia Li, and Lin Shi. 2026. RepoScope: Leveraging Call Chain-
Aware Multi-View Context for Repository-Level Code Generation. In 2026
IEEE/ACM 48th International Conference on Software Engineering (ICSE ’26),
April 12–18, 2026, Rio de Janeiro, Brazil. ACM, New York, NY, USA, 13 pages.
https://doi.org/10.1145/3744916.3773211
1
Introduction
Code generation can substantially reduce manual effort by automat-
ing repetitive and time-consuming programming tasks, offering
transformative potential for software engineering. In recent years,
Large Language Models (LLMs), such as DeepSeek-Coder [16],
QwenCoder [19], GPT-4o [1], etc., have demonstrated impressive
capabilities in code generation tasks. However, their performance
often degrades significantly when applied to repository-level code
generation tasks within complex, large-scale repositories. This chal-
lenge arises primarily from two factors: ❶constrained context
windows limiting the model’s access to the broader project con-
text needed to understand architecture and intricate dependencies,
and ❷a lack of repository-specific knowledge [39], including
details of internal APIs and domain-specific coding conventions
not captured within the immediate context window.
To mitigate the above challenge, retrieval-augmented generation
(RAG) [13] approaches have been introduced, aiming to provide
374

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
LLMs with relevant contextual information extracted from the
repository. Early approaches [37, 44] retrieve textually similar code
snippets from the repository using the code context as a query.
Recent methods have sought to refine retrieval through structural
and semantic augmentation, e.g., by incorporating imported def-
initions [26], performing dataflow analysis [8], or constructing
repository-level semantic graphs with GNNs for relevance scoring
[34]. Agent-based pipelines further extend these capabilities by
enabling iterative retrieval and LLM-guided evaluation of retrieval
targets [5, 30, 45]. Such advances have yielded notable performance
gains in repository-level code generation tasks. Nevertheless, exist-
ing approaches still exhibit critical limitations:
Insufficient Relevance of Retrieved Context. In RAG frame-
works, the quality of LLM-generated code hinges critically on iden-
tifying the highly relevant context. While similarity-based retrieval
approaches [10, 12, 28, 41, 44] can retrieve highly similar code, they
overlook the structural semantics embedded in the repository. This
often leads to the omission of critical context, potentially causing
generated code to conflict with repository-specific knowledge, such
as the usage of constants or APIs. To mitigate this issue, structural
augmentation approaches are proposed [5, 8, 26]. However, exist-
ing methods typically rely on shallow structural semantics, such
as basic dependency parsing or dataflow analysis. As a result, they
struggle to effectively assess and filter the relevance of retrieved
code, hindering the precise identification of truly relevant context.
Limited contextual perspectives. When encountering a new
project, human programmers typically analyze related code from
multiple perspectives to understand the behavior of a particular
snippet. For instance, they may examine where it is invoked, how
its return values are handled, which function it calls, and what struc-
turally similar code exists. In contrast, existing approaches often
rely on just one or two such perspectives, hindering accurately mod-
eling of rich semantics within repositories. The rapid advancement
in LLM capabilities now enables and demands repository-level code
generation to incorporate richer, more diverse contextual views.
Furthermore, existing approaches exhibit several additional limi-
tations. In terms of efficiency, approaches that depend on extensive
supervised training [34, 41] or on agent-based pipelines with multi-
ple LLM queries [30, 45] incur substantial computational/temporal
cost, and often struggle to adapt across diverse repositories. Regard-
ing prompt organization, existing approaches typically construct
prompts by simply concatenate the retrieved code elements, either
directly or in a predetermined order [8, 26, 34], overlooking the
inherent structural relationships between them (e.g., class-method
hierarchies). The lack of structural representation may hinder LLMs’
ability to accurately interpreting context semantics, potentially de-
grading code generation quality.
To this end, we propose RepoScope, a framework that leverages
call chain–aware multi-view context for repository-level code gen-
eration. For each repository, we construct a Repository Structural
Semantic Graph (RSSG). With the RSSG, RepoScope retrieves two
types of structure-based context for the target function: its direct
callers and its potential callees. These structure-based contexts are
then combined with two additional similarity-based contexts. To-
gether, they form a comprehensive four-view context, equipping
the LLM with rich background knowledge needed for code gener-
ation. Specifically, to identify potential callees, we propose a call
Table 1: Comparison between RepoScope and existing meth-
ods, including whether the method ranks retrieved code ele-
ments to reduce irrelevant context, utilizes more than two
contextual views, operates without additional training, and
performs code generation using only a single LLM query.
Method
Element
Ranking
Diverse
Views
Training-
Free
Single LLM
Query
RepoCoder[44]
✗
✗
✓
✗
RLCoder[41]
✗
✗
✗
✓
RepoFuse[26]
✗
✗
✓
✓
DRACO[8]
✗
✗
✓
✓
RepoHYPER[34]
✓
✗
✗
✓
CoCoGen[5]
✗
✗
✓
✗
CodeAgent[45]
✗
✓
✓
✗
LingmaAgent[30] ✓
✗
✓
✗
RepoScope
✓
✓
✓
✓
chain prediction method, fully exploiting the structural semantics
of the repository to predict entire call chains (i.e., a sequence of
callees connected via semantic relations, as defined in Section 2.2),
rather than just isolated callees. This method enhances the accuracy
of callee identification and thus provides context with stronger rele-
vance. When constructing the prompt with the retrieved four-view
context, we introduce a structure-preserving serialization algorithm
to convert the contexts into a coherent token sequence, preserving
their original hierarchical relationships within the repository. This
enables the LLM to accurately interpret context semantics, thus
enhancing code generation quality. Crucially, our approach relies
solely on static analysis, requiring no additional training or multiple
LLM queries, thereby ensuring both efficiency and generalizability.
Table 1 presents the comparison between RepoScope and several
representative repository-level code generation methods.
We evaluate RepoScope on widely-used repo-level code gener-
ation benchmarks, CoderEval [43] and DevEval [25], using four
advanced backbone LLMs and perform comprehensive comparisons
with state-of-the-art baselines. The evaluation results demonstrate
that RepoScope outperforms the best-performing baseline across
all backbone models, achieving up to 36.35% relative improvement
in pass@1 score. In addition, we further explored RepoScope’s gen-
eralization capability and its integration with existing approaches.
In summary, the contributions of this work are as follows:
• We propose RepoScope, a framework that utilizes call chain-
aware multi-view context for repository-level function gener-
ation. By integrating context from four distinct perspectives,
RepoScope enriches the LLM with a more comprehensive under-
standing of the repository’s semantics.
• We introduce Repository Structural Semantic Graph (RSSG), a
heterogeneous directed graph constructed via static analysis,
which captures various types of structural semantics within a
code repository and enables more precise context retrieval.
• We introduce a call chain prediction approach which deeply
leverages the structural semantics in the RSSG to predict the
potential callees of the target function, thereby improving the
relevance of the retrieved context. We further propose a structure-
preserving serialization algorithm that converts context into
coherent token sequences while preserving structural hierarchy.
375

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
• We conduct a comprehensive evaluation of RepoScope, and the
results demonstrate that it outperforms state-of-the-art methods,
exhibits strong generalizability across different tasks, and offers
potential for performance enhancement when integrated with
existing approaches.
2
Preliminaries
2.1
Motivating Example
In programming languages, the relationships between various code
elements (such as classes, methods/functions, and attributes) encode
rich structural semantics that are vital for understanding code [22,
31, 35]. These relationships include call relationships, structural and
type dependency relationships, and import relationships, etc. When
implementing a new function, the most direct, precise and relevant
information that can be obtained from these relationships typically
includes the callers and callees of the target function [17, 46]. The
callers reveal the function’s intended use, providing insights into
expected inputs and outputs, while the callees directly participate in
constructing the function body itself. Additionally, type information
for parameters and return values is crucial, which is often implicitly
reflected in caller usage patterns. Critically, while static analysis can
identify callers, callees present a distinct challenge. Since the target
function’s body is unknown during generation, we cannot directly
identify its callees from the repository. This necessitates predicting
the likelihood of each code element being called by the target function.
The goal is to select the code elements with the highest probability
to construct a highly relevant context for code generation. However,
this task is non-trivial, requiring comprehensive analysis of type
dependencies, code hierarchies, and cross-entity relations within
the repository.
Existing RAG based code generation methods lack targeted de-
sign and thus often struggle to accurately retrieve or predict these
code elements. As shown in Figure 1, a similarity-based retrieval
approach identifies the function _convert_non_cli_args, which
is similar to the target function. While its call chain appears rele-
vant, it erroneously terminates at get_option_spec instead of the
required iterate_option_specs. When supplied with this inac-
curate context, LLMs may hallucinate non-existent methods (e.g.,
get_parser_names and get_option_names), leading to incorrect
solution. In contrast, proactively identifying the target function’s
dependency on iterate_option_specs and incorporating this in-
formation into the prompt would enhance generation accuracy.
More importantly, these code elements typically form sequences
of interconnected calls, termed Call Chain (formally defined in
Section 2.2). A call chain connects different code elements through
type or structural relationships. As shown in Figure 1 and 2, a plau-
sible call chain within the target function get_deprecated_args
contains: ①The parent class SpecParser →②The attribute spec_
helper →③The attribute’s type SpecDictHelper →④The ter-
minal function iterate_option_specs. Compared to an isolated
callee, a call chain encodes richer behavioral information and pro-
vides a more coherent contextual representation. Accurately predict-
ing such chains is therefore highly beneficial for code generation.
It is also worth noting that, as shown in Figure 2, the correct
callee (iterate_option_specs) and the incorrectly retrieved one
(get_option_spec) also exhibit high similarity. This aligns with a
common phenomenon in software development: similar functions
within the same repository often exhibit similar calling behaviors.
Inspired by this insight, we propose a heuristic call chain predic-
tion method that leverages the calling patterns of similar, existing
functions to assist in predicting the call chain of the target function.
This method will be detailed in Section 3.3.
2.2
Definitions
This section formalizes key concepts foundational to our approach:
Call, Call Chain, and our constructed Repository Structural Semantic
Graph.
2.2.1
Call. In this paper, Call refers to the access or invocation
of code elements within the repository that are accessible across
scopes, including classes, functions/methods, attributes, etc.
2.2.2
Repository Structural Semantic Graph. The Repository Struc-
tural Semantic Graph (RSSG) is a multi-view heterogeneous directed
graph that represents semantic relationships among code elements
in the repository. Specifically, RSSG includes three types of entities:
• Class represents the classes defined in the code.
• Function represents various functions, including both standalone
functions and those bound to classes.
• Attribute represents variables bound to classes.
Relations are categorized into three semantic views comprising six
distinct types:
(1) Structural and Type Dependency relation defines the pos-
sible paths of a call chain. Entities involved in a sequence of
directly related call operations can be linked through such rela-
tions, forming a chained data structure that follows the dataflow.
Specifically, it includes four subtypes:
• Contains indicates that an entity 𝑒𝑡𝑜is a member of another
entity 𝑒𝑓𝑟𝑜𝑚, and can therefore be called from 𝑒𝑓𝑟𝑜𝑚using a
member access operator. Specifically, 𝑒from should be a Class,
while 𝑒to can be one of the following types: a Function, an
Attribute or a nested Class.
• Returns indicates that an instance of a Class 𝑒to can be ob-
tained by calling another entity 𝑒from. Specifically, 𝑒from can
be either a Function or an Attribute.
• As Parameter indicates that an entity 𝑒to relies on an in-
stance of a Class 𝑒from as a prerequisite for its call. Specifically,
𝑒to refers to a Function.
• Inherits indicates that a Class 𝑒from is a subclass of another
Class 𝑒to, and therefore 𝑒from can call the members of 𝑒to.
(2) Calls relation denotes that within the implementation of a
Function 𝑒from, another entity 𝑒to is called. Specifically, 𝑒to can
be a Function, an Attribute, or a Class.
(3) Imports relation denotes that a Function 𝑒from can directly call
another entity 𝑒to (excluding itself) within the current code
context. This encompasses two scenarios: 𝑒to has been imported
via an import statement and 𝑒to and 𝑒from reside within the
same module scope. Specifically, 𝑒to can be a Class or a Function.
Formally, RSSG can be described as 𝐺= {(ℎ,𝑟,𝑡) | ℎ,𝑡∈E, 𝑟∈
R𝑆𝑇∪R𝐶∪R𝐼}, where E denotes the set of entities, representing
the main code elements in the repository. R𝑆𝑇, R𝐶, R𝐼represent
the sets of structural semantic relations corresponding to the three
different views, i.e., Structural and Type Dependency, Calls, and
376

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
from infrared.core.inspector import helper
class SpecParser(object):
    def __init__(self, spec_dict, ...):
        self.spec_helper = helper.SpecDictHelper(spec_dict)
        ...
    def get_deprecated_args(self):
        """Returning dict with options which deprecate others."""
Task
# infrared/core/inspector/inspector.py, owning class: SpecParser
def _convert_non_cli_args(self, parser_name, values_dict):
    for opt_name, opt_value in values_dict.items():
        file_option_spec = self.spec_helper.get_option_spec(
            parser_name, opt_name)
        if file_option_spec.get('type', None) in ['int', ] or \
                file_option_spec.get('action', None) in ['count', ]:
            values_dict[opt_name] = int(opt_value)
...
Retrieved Similar
Functions
Retrieve
def get_deprecated_args(self):
    deprecated_args = {}
    for parser_name in self.spec_helper.get_parser_names():
        for opt_name in self.spec_helper.get_option_names(parser_name):
            option_spec = self.spec_helper.get_option_spec(
                                               parser_name, opt_name)
            deprecated_list = option_spec.get('deprecated_opts', [])
            if deprecated_list:
                deprecated_args[opt_name] = deprecated_list
    return deprecated_args
Generated
Solution
def get_deprecated_args(self):
    result = collections.defaultdict(dict)
    for parser, option in self.spec_helper.iterate_option_specs():
        if option.get('deprecates') is not None:
            result[option.get('deprecates')] = option.get('name')
    return result
Ground-truth
Solution
Bad Solution
Inaccurate Callee
LLM 
Generate
Cause
Figure 1: A motivating example. Similarity-based retrieval methods often struggle to accurately capture call-related information.
Spec
Parser
get_
deprecated
_args
_convert
_non_cli
_args
spec_
helper
SpecDict
Helper
iterate
_option
_specs
get_
option
_spec
A Call Chain
Contains
TypeOf
Class
Function
Attribute
Target
Function
Calls
Imports
Figure 2: The RSSG derived from the code shown in Figure 1.
Imports. In each triplet (ℎ,𝑟,𝑡), the head entity ℎpoints to the tail
entity 𝑡via the relation 𝑟. The RSSG serves as a crucial foundation
for our retrieval and call chain prediction. Unless otherwise speci-
fied, all mentions of entities and relations in the following text refer
to those defined in the RSSG.
2.2.3
Call Chain. Based on RSSG, we define a call chain as C =
(𝑒1,𝑟1,𝑒2, . . . ,𝑟𝑛−1,𝑒𝑛), where ∀1 ≤𝑖< 𝑛, (𝑒𝑖,𝑟𝑖,𝑒𝑖+1) ∈𝐺,𝑟𝑖∈
R𝑆𝑇. Unlike conventional call chains, the call chains in our
work focus on the static entity relationships within call state-
ment(s) under the same scope. Intuitively, in source code, a
single call often explicitly or implicitly involves multiple entities.
For example, consider a call c.f(d), where c is an instance of class
C, d is an instance of class D, and the return type of f is E. This call
involves four entities: C, D, E, and f, which can be further organized
into two chains along the direction of dataflow: C →f →E and
D →f →E. The relationships among these entities are encoded
in the structural and Type dependency relations. If there are other
calls in the context that are directly related to this call—such as a
call used to obtain the instance d of D—the call chain can be further
extended. In other words, a sequence of directly related calls can
be jointly represented using a call chain.
3
Approach
3.1
Overview
With the observation in Section 2.1, we proposed RepoScope, a
framework leveraging call chain-aware multi-view context for
repository-level function generation. As illustrated in Figure 3 (a),
RepoScope incorporates both the callers and the predicted callees
of the target function into the LLM’s prompt. It follows the standard
RAG paradigm, which consists of three stages: indexing, retrieval,
and generation. In the indexing stage, we construct a unified RSSG
that captures the semantic relationships among three types of code
elements in the repository. This graph forms the foundation for
retrieving both callers and callees. Additionally, we employ the
sliding window algorithm [44] to segment the repository code into
fragments, which are used for similarity-based retrieval. In the
retrieval stage, we perform both retrieval and call chain predic-
tion to obtain two types of contextual information from the index:
structural semantic context and similarity-based context. The
former comprises ①function’s callers and ②predicted call chain,
while the latter includes ③functions and ④code fragments most
similar to the unimplemented target function. Together, these form
a four-view context representation. In the generation stage, we de-
sign a serialization algorithm to reconstruct the call chain into a
valid code structure while ensuring the elimination of duplicate
nodes. Then we propose an iterative prompt construction strategy
to systematically integrate the four context types into the prompt.
The final prompt is fed into the LLM to produce the function.
3.2
RSSG Construction
For each repository, we parse it using static code analysis tools
to construct a RSSG. To support retrieval, we further process the
RSSG accordingly. Specifically, for each relation 𝑟∈R𝐶, a weight
𝑤𝑟is assigned to represent the number of times the head entity
calls the tail entity. In addition, we compute an embedding vector
𝑉𝑒for each entity 𝑒using a sentence embedding model:
𝑉𝑒= Embedder(
< name > 𝑒name < /name >< signature > 𝑒sig < /signature >
< description > 𝑒docs < /description >< path > 𝑒path < /path >
)
where 𝑒name, 𝑒sig, 𝑒docs, and 𝑒path represent the entity’s name, sig-
nature, docstring, and path, respectively. For example, for the target
function in Figure 1, these values are:
• 𝑒name: get_deprecated_args
• 𝑒sig: def get_deprecated_args(self) -> collections.
defaultdict
• 𝑒docs: Returning dict with options which deprecate others
• 𝑒path: infrared/core/inspector/inspector/SpecParser/
get_deprecated_args
377

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Call Chains
Construct RSSG
Split Code Fragments
Contains
 Returns
As 
Parameter
Inherits
Calls
Imports
Structural and Type Dependency
Relations
Class
Function
Attribute
Entities
Target
Function
Callers
Similar Functions
Similar Fragments
Multi-view Contexts
Similarity-based
Structual Semantic
Call Chain 
Prediction
Structure-
Preserving
Serialization
① Indexing
② Retrieval
③ Generation
Target
Function
Repo
Prompt
...
(a) Overview
RSSG
Identify 
Imported Entities
0.6
0.9
2.7
0.5
0.2
1.2
0.8
0.7
0.3
1.8
1.3
Depth First Search
2.7
0.5
0.8
1.8
1.2
1.4
1.3
...
Extend & Rank
2.7
0.5
0.8
1.2
0.9
0.8
0.6
0.7
0.5
0.4
0.3
0.4
Calculate Entity Scores
0.9
0.9
descend
All Scores
+1
All Scores
+2
A Call Chain
(b) Detailed steps of call chain prediction
Figure 3: Workflow of RepoScope.
If 𝑒does not have a docstring, then 𝑒docs is set to an empty string.
3.3
Call Chain Prediction
Given the signature and docstring of an unimplemented target
function 𝑓, we propose a heuristic method to predict the potential
call chains that may appear in its function body based on RSSG.
The core idea involves starting with the entities imported by the
target function and performing a depth-first search on the RSSG
to generate call chains from each search path. Each entity is then
assigned a score based on the call patterns within the repository.
These scores are aggregated to compute the score for each call chain,
and the top-ranked call chains are selected as the final output. As
illustrated in Figure 3 (b), this method consists of four steps.
(1) Identify Imported Entities. First, we identify all entities
(i.e., classes and functions) accessible directly from target func-
tion 𝑓, which can be directly extracted from RSSG: Eimp(𝑓) = {𝑒|
(𝑓,𝑟,𝑒) ∈𝐺, 𝑟∈R𝐼}. These imported entities serve as initial start-
ing points for call chain prediction. In the example from Figure 1,
the sole imported entity identified is the SpecParser class.
(2) Calculate Entity Scores. Second, we compute entity scores
using the call relation set R𝐶in the RSSG, where higher values
indicate greater likelihood of being called. As mentioned in 2.1, we
could leverage the callees of similar functions to identify entities
that are more likely to be called by the target function. To achieve
this, we first apply the K-means clustering algorithm to partition
all entities into clusters, each containing approximately 𝑀entities
on average, with the cluster containing entity 𝑒denoted as 𝐶𝑒. We
then compute a weighted score 𝑆𝑒for each entity:
𝑆𝑒= 𝛼1 · sim(𝑉𝑓,𝑉𝑒) + 𝛼2 · 𝜙
©­­­­
«
∑︁
(ℎ,𝑟,𝑡)∈𝐺, 𝑟∈R𝐶,
ℎ∈𝐶𝑓\{𝑓}, 𝑡∈𝐶𝑒
𝛼3𝑤𝑟
ª®®®®
¬
where sim(·) is vector similarity (cosine similarity), 𝛼𝑖(𝑖= 1, 2, 3)
are weighting coefficients, and the function 𝜙(·) is a monotonically
increasing concave function that mitigates sensitivity to large input.
For illustration, consider the top-right subfigure of Figure 3 (b),
where the number in each entity represents its similarity with the
target function 𝑓. Ignoring 𝛼𝑖and 𝜙(·), each call of an entity 𝑒by
a function from 𝐶𝑓increments the scores of all entities in 𝐶𝑒by
1, added to their similarity with 𝑓. Thus, an attribute entity with
similarity 0.6 (as shown) would receive a final score of 1.6.
In summary, this algorithm computes entity scores by leveraging
both repository call patterns and embedding similarity. Moreover,
it enhances robustness by allowing entities within the same cluster
to share call values (i.e. the input of 𝜙(·)). For example, in Figure 1,
if only _convert_non_cli_args or its callees were provided to the
LLM, the model would struggle to infer that iterate_option_specs
is a valid callee of the target function. However, because iterate_
option_specs and get_option_spec reside in the same cluster,
the former inherits the latter’s call value, thereby boosting its re-
trieval probability. It is important to note that, function embedding
vectors (𝑉𝑒) are computed without dependency on function bodies,
which remain unavailable prior to code generation.
(3) Depth First Search. Third, we perform a depth-first search
(DFS) traversal on the R𝑆𝑇relation set of RSSG starting from each
entity in Eimp(𝑓), collecting all possible call chains. By controlling
the maximum chain length 𝑙max, we can balance the breadth of
retrieval with retrieval efficiency and precision. The algorithm
pseudocode can be found in our replication package.
(4) Extend & Rank. Finally, to enhance the LLM’s understanding
of each entity within the call chain, we extend the chain to include
three key entities types (if exists):
• The constructor Function entity for each Class entity in the chain
(using Contains relation).
• The parameter and return type Class entities for each Function en-
tity in the chain, as well as the type Class entity of each Attribute
entity in the chain (using As Parameter and Returns relation).
• The Class entity to which each Function or Attribute entity in the
chain belong (using Contains relation).
We then compute each chain’s overall score as the average score of
its constituent entities, and the top 𝐾chain highest-scoring chains
(Cchain) are selected. Since different call chains may contain each
378

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
other—as seen in the first two call chains in Figure 3 (b)—we dedupli-
cate the chains during the ranking. To further enhance diversity, we
select a maximum of 𝜏chains starting from each entity in Eimp(𝑓).
3.4
Structure-Preserving Prompt Construction
In addition to call chain prediction, we also retrieve three addi-
tional context types: (1) 𝐾𝑐𝑎𝑙𝑙𝑒𝑟caller entities of 𝑓(C𝑐𝑎𝑙𝑙𝑒𝑟) with
the minimum distances1; (2) the top 𝐾𝑠𝑖𝑚_𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛function en-
tities (C𝑠𝑖𝑚_𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛) most similar2 to 𝑓from RSSG; (3) the top
𝐾𝑠𝑖𝑚_𝑓𝑟𝑎𝑔𝑚𝑒𝑛𝑡code fragments (C𝑠𝑖𝑚_𝑓𝑟𝑎𝑔𝑚𝑒𝑛𝑡) most similar to 𝑓
from all code fragments. These contexts provide the LLM with
relevant information for implementing the target function from
both the perspectives of code similarity and structural semantics,
forming a four-view context. Notably, C𝑠𝑖𝑚_𝑓𝑟𝑎𝑔𝑚𝑒𝑛𝑡complements
C𝑠𝑖𝑚_𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛by capturing similar code that may not reside within
function definitions, thus preventing potential omissions.
Since entities within call chains may exhibit hierarchical rela-
tionships in the repository, we present a structure-preserving
serialization algorithm to preserve their original structural orga-
nization during prompt construction, enabling the LLM to better
capture these relationships and, as a result, improve its interpreta-
tion of the context. Additionally, because different call chains may
contain overlapping entities, deduplication is necessary. Specifi-
cally, we traverse all the call chains to construct a structural tree,
where each node’s children are entities that share a Contains rela-
tion with it. We then perform a preorder traversal to sequentially
output all entities, using indentation to reconstruct their hierarchi-
cal structure. The detailed algorithm of the serialization strategy
can be found in the replication package.
Considering the limited input token length of LLMs, we need
to allocate the input budget reasonably across the four types of
context. To achieve this, we propose a two-stage iterative prompt
construction strategy. Its basic idea aligns with the dynamic context
allocation strategy [39] but is more extensible. In short, each type
of context is first allocated an equal token budget, after which each
type “claims” any remaining tokens from the others according to
a fixed priority order. Specifically, given a maximum input length
ℓ(after subtracting the length occupied by the task description
and instructions) and 𝑁types of context 𝐶1, . . . ,𝐶𝑁, our strategy
proceeds as follows:
Stage 1: Pre-allocation. We first allocate a uniform budget of
¯ℓ=
 ℓ
𝑁
 to each context type 𝐶𝑖to balance the inclusion of dif-
ferent types of context. This averaged initialization strategy has
been proven optimal in our preliminary experiments. Then, 𝐶𝑖fills
¯ℓtokens with its context units according to its internal ranking
strategy. If the shortest unit exceeds ¯ℓ, the corresponding prompt
is set to empty. Let ℓ𝑖denote the actual number of tokens used by
𝐶𝑖after this step.
Stage 2: Re-allocation. Through preliminary experiments, we
determined a fixed priority order over context types 𝐶𝑡1, . . . ,𝐶𝑡𝑁.
For each context 𝐶𝑡𝑖in order 𝑖= 1, . . . , 𝑁, ①we allocate ℓ−
Í
1≤𝑗≤𝑁∧𝑗≠𝑖ℓ𝑡𝑗tokens, allowing 𝐶𝑡𝑖to claim remaining space of
1If two entities reside in different files from 𝑓, the one with the shorter path length to
𝑓in the file system tree is considered closer. Otherwise, the entity with a smaller line
number difference from 𝑓is considered closer.
2All similarity computations use the same embedding model and similarity function
as those employed in call chain prediction.
Prompt
You need to implement the function located at the end of
the instruction based on relevant repository information.
1. Here are some relevant code fragments from the repo:


1
# infrared/common/library/virt_util.py
2
COMMANDS.setdefault(
3
cmd_name, {'call': func, 'args': kwargs.keys()}
4
)
5
...
6
7
# infrared/__init__.py
8
...


2. Here are some functions in the repo that invoke the target func-
tion:


1
# filepath: infrared/core/inspector/inspector.py, owning class: SpecParser
2
def validate_arg_deprecation(self, cli_args, answer_file_args):
3
...
4
for deprecated , deprecates in self.get_deprecated_args().items():
5
...
6
...


3.
Here are some relevant classes, functions, or attributes in the
repo that you might use in the target function:


1
# infrared/core/inspector/helper.py
2
class SpecDictHelper:
3
"""Controls the spec dicts and provides useful methods to get spec
info."""
4
...
5
def get_option_spec(self, command_name , argument_name) -> Any:
6
"""Gets the specification for the specified option name. """
7
8
def iterate_option_specs(self) -> Generator[Tuple[dict, dict], Any,
None]:
9
...
10
...
11
...


4. Here are some functions in the repo that are similar to the target
function:


1
# filepath: infrared/common/library/virt_util.py, owning class: Util
2
def _validate_args(self, *args):
3
...
4
absent = []
5
...
6
...


Please implement the following function:


1
from infrared.core.cli.cli import CliParser
2
from infrared.core.inspector import helper
3
...
4
5
# filepath: infrared/core/inspector/inspector.py, owning class: SpecParser
6
def get_deprecated_args(self):
7
"""
8
Returning dict with options which deprecate others.
9
"""


Figure 4: The prompt corresponding to the target function
in Figure 1 (with omissions).
other contexts; ②similar to the first stage, 𝐶𝑡𝑖refills the updated
length with its context units; ③we then update ℓ𝑡𝑖accordingly.
Finally, the four types of context, together with the task de-
scription and generation instruction, are combined into a well-
structured and properly formatted prompt, which is used to query
the LLM for generating the target function. An example prompt is
shown in Figure 4. The 1st, 2nd, 3rd, and 4th contexts in the prompt
correspond to the four contextual perspectives: similar code frag-
ments, callers, call chains, and similar functions. Regarding call
chains (3rd context), we can observe that entities retrieved via call
chain prediction, such as SpecDictHelper, get_option_spec, and
iterate_option_specs, are serialized in accordance with their
structural organization in the repository code.
379

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
4
Evaluation
4.1
Research Questions
In this work, we aim to answer the following research questions:
• RQ1: Overall Performance. How does RepoScope perform on
the task of repository-level function generation?
• RQ2: Ablation Study. To what extent do the key components
and strategies of RepoScope contribute to its performance?
• RQ3: Generalization Capability. How generalizable is Repo-
Scope to other repository-level code generation tasks?
• RQ4: Integration with Existing Approaches. Can RepoScope
be integrated with existing repository-level code generation ap-
proaches to achieve further performance improvements?
4.2
Baselines
We selected several representative repository-level code genera-
tion methods, including the current state-of-the-art, to conduct a
performance comparison against RepoScope.
• Direct refers to generating code solely based on the local context
without incorporating any retrieval.
• SimpleRAG retrieves a fixed set of similar code snippets based
on similarity and directly appends them to the prompt for one-
shot generation.
• RepoCoder [44] is a retrieval-augmented framework for repository-
level code completion that combines a similarity-based retriever
with a LLM in an iterative retrieval-generation pipeline.
• DRACO [8] is a repository-level code completion method that
leverages extended dataflow analysis to construct a repo-specific
context graph and enhances prompt by integrating structurally
relevant background knowledge.
• CodeAgent [45] is an agent-based framework that equips LLMs
with external programming tools to enable effective repository-
level code generation.
• RLCoder [41] is a reinforcement learning–based framework
for repository-level code completion that optimizes retriever
behavior through perplexity feedback.
For RepoScope and each baseline, we evaluate their performance
on four advanced backbone LLMs: GPT-4o mini3 [20], Claude-3.5-
Haiku4 [2], Qwen3-235B-A22B5 [42] and DeepSeek-V36 [27].
4.3
Datasets and Metrics
We evaluate the effectiveness of RepoScope in repo-level function
generation tasks using two widely adopted benchmarks: CoderEval
[43] and DevEval [25]. In addition, to assess the generalizability of
RepoScope, we further evaluate its performance on repo-level API
generation tasks using RepoEval [44] in Section 5.3. The detailed
information of the benchmarks are as follows:
• CoderEval [43] consists of 460 real-world Python and Java tasks
(half for each language) designed to evaluate code generation
across six levels of context dependency. We use its Python sub-
set. Due to incorrect file_path entries in some samples, which
prevent us from locating the corresponding RSSG entities of the
3We use its latest model snapshot gpt-4o-mini-2024-07-18
4We use its latest model snapshot claude-3-5-haiku-20241022
5We use its “non-thinking” mode
6We use its latest version DeepSeek-V3-0324
target functions, we exclude those samples, resulting in a total
of 207 samples.
• DevEval [25] is a developer-annotated benchmark designed to
evaluate LLMs’ coding abilities in real-world repositories, featur-
ing 1,825 samples from 117 repos. Due to the presence of samples
whose reference solutions fail to pass the provided test suites, as
well as samples with incorrect lineno annotations, we exclude
those instances, resulting in a final dataset of 1,742 samples. The
specific details of the excluded samples for the above two datasets
can be found in our replication package.
• RepoEval [44] is a repository-level benchmark covering line-,
API-, and function-level code completion tasks across real-world
repositories. In Section 5.3, we use its API-level subset, which
contains 1,600 samples.
For CoderEval and DevEval, since they provide test suites, we
evaluate the correctness of the generated code using the pass@k
metric [7]. For RepoEval, we employ EM (Exact Match) and ES
(Edit Similarity) [23] metrics to assess the similarity between the
generated code and reference solution. These benchmarks include
repositories of various scales. Among the 158 repositories involved
in CodeEval and DevEval, 17 repositories (10.76%) contain more
than 100,000 lines of code, which are typically classified as large-
scale repositories. Tasks associated with these repositories account
for 320 out of the total 1,949 tasks (16.42%).
4.4
Implementation Details
We construct the RSSG with the assistance of the Pytype7 library
and Tree-sitter8. Except for RLCoder, which uses a custom fine-
tuned version of UnixCoder9 [15] (126M parameters) as its retriever
(embedder), all other methods employ bge-small-en-v1.510 [6]
(33.4M parameters) as the embedding model. It is worth noting
that preliminary experiments have shown that different advanced
embedding models have no significant impact on the performance
of our method. For call chain prediction, the average cluster size
𝑀is set to 5. The weighting coefficients 𝛼1, 𝛼2, 𝛼3 of 𝑆𝑒are set
to 1.0, 2.0, and 2.0, respectively. The call value mapping function
𝜙(·) is defined as 𝜙(𝑥) = log2(𝑥+ 1). The maximum call chain
length 𝑙max is set to 5, and the maximum number of call chains per
starting point 𝜏is set to 4. The number of retrieved items for the
four contexts—𝐾𝑐ℎ𝑎𝑖𝑛, 𝐾𝑐𝑎𝑙𝑙𝑒𝑟, 𝐾𝑠𝑖𝑚_𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛, 𝐾𝑠𝑖𝑚_𝑓𝑟𝑎𝑔𝑚𝑒𝑛𝑡—are
all set to 5. All the above parameters were determined through
preliminary experiments. The maximum prompt token length ℓis
set to 4096.
All LLMs used in our experiments are accessed via their online
APIs. Except for the temperature parameter, which is set to 0, all
other decoding parameters are kept at their default values. Tem-
perature controls the randomness of LLM outputs, and setting it to
0 reduces decoding to greedy decoding, resulting in deterministic
outputs. We set 𝑘= 1 in the pass@k. To minimize the impact of
prompt token length—a extraneous variable—on the results and
allow us to focus on the quality and accuracy of the prompt, we
adjusted parameters in baselines during evaluation to make sure
7https://github.com/google/pytype
8https://tree-sitter.github.io/py-tree-sitter
9https://huggingface.co/microsoft/unixcoder-base
10https://huggingface.co/BAAI/bge-small-en-v1.5
380

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
Table 2: Pass@1 scores across datasets and backbone models, along with the average length of input tokens in each method. The
percentages indicate the relative improvement compared to the best-performing baseline (underlined) under the same setting.
Dataset
Method
Backbone Model
Avg. # Token
GPT-4o mini
Claude-3.5-Haiku
Qwen3-235B-A22B
DeepSeek-V3
CoderEval
Direct
20.29
26.09
23.19
28.02
97
SimpleRAG
39.13
43.96
43.00
48.79
3824
RepoCoder
37.68
44.93
44.44
50.72
7661*
DRACO
40.10
47.34
41.06
47.34
3837
CodeAgent
27.54
28.99
33.82
39.13
5884*
RLCoder
38.16
49.28
40.58
46.86
3576
RepoScope
44.93 ↑12.04%
55.07 ↑11.75%
49.28 ↑10.89%
59.42 ↑17.15%
3679
DevEval
Direct
7.69
11.71
10.56
12.40
90
SimpleRAG
22.61
28.42
21.81
28.53
3803
RepoCoder
20.84
29.28
22.96
28.93
7613*
DRACO
25.26
30.48
29.39
32.09
3804
CodeAgent
15.33
23.13
21.70
25.89
5649*
RLCoder
19.69
26.35
22.39
27.90
3668
RepoScope
26.18 ↑3.64%
41.56 ↑36.35%
30.02 ↑2.14%
35.82 ↑11.62%
3679
* The input token lengths for the RepoCoder and CodeAgent method are calculated as the sum of the input token lengths across all dialogue rounds.
their average prompt token lengths were approximately at the same
level. The RepoCoder [44] and CodeAgent [45] are exceptions, as
their multi-turn dynamic interaction with the LLM makes it difficult
to control the overall prompt length. Nevertheless, we tried to align
the final-turn (i.e., the final code generation turn) prompt length
with that of other methods.
5
Results and Analysis
5.1
RQ1: Overall Performance
To evaluate the effectiveness of RepoScope, we compare it against
baselines using four backbone models on the CoderEval and De-
vEval datasets. The pass@1 scores and the average input token
length are presented in Table 2. As seen in the results, RepoScope
consistently achieves the highest pass@1 scores in all backbone
models, with comparable or fewer input tokens, showing substan-
tial improvements over the best-performing baselines, while main-
taining high efficiency. Notably, the most prominent gain is ob-
served on DevEval with the Claude-3.5-Haiku backbone model,
where RepoScope outperforms the best baseline DRACO by 36.35%.
The second-best result is achieved on the CoderEval dataset with
DeepSeek-V3, showing a 17.15% improvement. We validated the
improvements statistically by comparing RepoScope against the
best baseline DRACO across all backbone LLMs and benchmarks.
A two-tailed test yields 𝑝= 2.11 × 10−9 ≪0.05, confirming that
RepoScope’s gains are statistically significant. These results demon-
strate that RepoScope, by offering more relevant, comprehensive,
and well-structured contextual information, effectively enhances
the performance of LLMs in repository-level code generation tasks.
Additionally, we observe that, in most cases, the best-performing
baseline is DRACO, which retrieves context via dataflow analysis.
This further underscores the importance of leveraging repository
structural semantics for code generation. Interestingly, despite hav-
ing the second-highest average input token length, the agent-based
approach CodeAgent performs poorly, even falling behind Sim-
pleRAG. This is primarily due to the large scale and logical com-
plexity of the repositories used in the experiments, which makes it
challenging for the LLM agent to effectively identify truly relevant
content from the vast array of potential classes or modules using
integrated tools. This suggests that, compared to static analysis or
similarity-based retrieval, LLM-driven retrieval may still face con-
siderable limitations when dealing with complex repository-level
tasks.
Answer to RQ1: RepoScope consistently outperforms all baseline
methods across all backbone models with comparable or fewer
input tokens, achieving a relative improvement of up to 36.35% in
pass@1 score. This superior performance validates the effective-
ness and robustness of the contextual information provided by
RepoScope, highlighting its ability to enhance code generation
tasks at the repository level.
5.2
RQ2: Ablation Study
To assess the effectiveness of each key component and strategy in
RepoScope, we conduct an ablation study on the CoderEval dataset
using two best-performing backbone models overall (Claude-3.5-
Haiku and DeepSeek-V3). Specifically, the ablation experiments are
divided into three parts. First, we evaluate the contribution of each
of the four context views in the prompt to the overall performance.
We individually remove (1) the callers (w/o Ca), (2) the call chains
(w/o CC), (3) the similar functions (w/o SF), and (4) the similar code
fragments (w/o SCF), and then assess the impact on code generation
performance. Second, we validate the necessity of three key strate-
gies in call chain prediction: weighted entity scoring, depth-first
search, and call chain extension. We construct three corresponding
variants by removing each strategy: (1) scoring entities solely based
on similarity (w/o WES), (2) using only directly imported entities (w/o
DFS), and (3) disabling call chain extension (w/o CCE). Finally, to
evaluate the effectiveness of our structure-preserving serialization
algorithm for prompt construction, we replace the algorithm with a
baseline that simply exports each entity in the call chain sequentially
without preserving structural relationships (w/o SS).
381

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Table 3: Ablation study results on CoderEval.
Method
Model
Avg. # Token
Claude-3.5-Haiku
DeepSeek-V3
RepoScope
55.07
59.42
3679
w/o Ca
52.66 ↓4.38%
55.56 ↓6.50%
3281 ↓10.82%
w/o CC
51.20 ↓7.03%
55.07 ↓7.32%
3245 ↓11.80%
w/o SF
52.17 ↓5.27%
52.66 ↓11.38%
2797 ↓23.97%
w/o SCF
51.20 ↓7.03%
57.00 ↓4.07%
2542 ↓30.91%
w/o WES
53.14 ↓3.50%
57.49 ↓3.25%
3645 ↓0.92%
w/o DFS
52.66 ↓4.38%
57.00 ↓4.07%
3669 ↓0.27%
w/o CCE
55.07 ↓0.00%
57.00 ↓4.07%
3665 ↓0.38%
w/o SS
54.11 ↓1.74%
56.04 ↓5.69%
3728 ↑1.33%
As shown in Table 3, the results show that, except for the removal
of the call chain extension strategy with Claude-3.5-Haiku, elimi-
nating any key component or strategy leads to a decrease in pass@1
score, confirming their effectiveness. Among them, removing the
similar function context (SF) when using the DeepSeek-V3 model
results in the largest performance degradation, with a decrease
of 11.38%. However, when factoring in changes in prompt token
length, the caller (Ca) and call chain (CC) contexts contribute the
highest utility per token consumed among the four context types
under our experimental settings, while similar code fragments (SCF)
contribute the lowest. Additionally, when the structure-preserving
serialization algorithm is removed (w/o SS), the pass@1 score drops
despite a slight increase in prompt length. This highlights the impor-
tance of this algorithm in both reducing token usage and improving
generation quality.
Furthermore, to examine the quality of the predicted call chains,
we compute the F1 scores for the predicted callees from our strategy
and a baseline that predicts callees solely based on similarity, under
the same average number of predicted callees. The results show
that our method (F1=0.603) outperforms the baseline (F1=0.4352)
by 38.56%, providing strong evidence for the effectiveness of our
call chain prediction strategy. Notably, accurately predicting the
callees of a target function is inherently challenging, since similar
functions can only provide guidance rather than deterministically
dictate which calls should appear. While the current error rate may
still seem high in absolute terms, it already represents a substantial
improvement over baselines, thereby yielding stronger contextual
relevance overall.
Answer to RQ2: Each proposed key component and strategy
in RepoScope positively contributes to the overall performance.
Considering the variation in token length, callers and call chains
are the most important among the four types of context, and the
structure-preserving serialization contributes to both generation
quality and token efficiency. Compared to the baseline, our call
chain prediction strategy is able to retrieve more accurate callees.
5.3
RQ3: Generalization Capability
Although RepoScope is designed for repository-level function gen-
eration, it can be easily adapted to other repository-level generation
tasks, such as API-level generation. In the case of API-level genera-
tion, given a code snippet 𝑐from the repository, the model needs
Table 4: Generalization experiment results on RepoEval.
Method
EM
ES
Avg. # Token
Direct
22.06
51.20
1505
SimpleRAG
34.25
61.02
3965
RepoCoder
32.94
59.60
7930
DRACO
33.19
64.36
4073
CodeAgent
36.13
60.86
14153
RLCoder
37.50
66.59
4081
RepoScope
40.25 ↑7.33%
67.74 ↑1.73%
4055
to generate a complete API call 𝑑that directly follows 𝑐. To address
this, we consider two cases for the location of 𝑑: (1) if 𝑑resides
within a function 𝑓, we can reuse the logic of function-level gen-
eration; (2) otherwise, we treat 𝑐as a function entity 𝑓and use it
for retrieval. Moreover, considering that the contextual code 𝑐in
API-level generation may already contain some API calls, we can
leverage this information. As previously mentioned, programming
experience suggests that similar functions tend to exhibit similar
call patterns. Similarly, calls that follows similar call sequences
are also often similar. Inspired by this, we extend our call chain
prediction method to incorporate this sequential pattern in the
repository. Specifically, We add a “sequence value” term into 𝜙(·),
which represents the degree of matching between the sequence
formed by entity 𝑒and the entities involved in existing calls within
𝑐, and the sequence patterns observed in the repository.
We conduct experiments on the API-level subset of RepoEval
using DeepSeek-V3 as the backbone, comparing RepoScope with
baseline methods. The results, shown in Table 4, reveal that Re-
poScope still demonstrates a notable improvement over the best-
performing baseline in both EM and ES metrics, with fewer input
tokens. In particular, for the Exact Match score, it achieves a relative
gain of 7.33%, indicating that RepoScope also holds considerable
potential for other repository-level code generation tasks beyond
function-level generation.
Answer to RQ3: RepoScope generalizes effectively to other
repository-level code generation tasks, achieving a 7.33% rela-
tive improvement in EM over the best baseline on the API-level
generation task. This demonstrates its potential to extend beyond
function-level generation and tackle a broader range of repository-
level code generation challenges.
5.4
RQ4: Integration with Existing Approaches
Due to the low coupling between the contextual views in Repo-
Scope, it can be seamlessly integrated with other repository-level
code generation methods to achieve better performance. To this
end, we experimented with integrating RepoScope with RLCoder
[41] and RepoCoder [44]. Specifically, since both RLCoder and Re-
poCoder focus on similarity-based full-text retrieval, we replaced
the similar code fragment context in RepoScope with the code re-
trieved by these two methods. To construct more discriminative
comparative experiments, we removed the similar function con-
text from RepoScope as a baseline and appropriately increased the
number of similar code fragments. We denote this variant as Repo-
Scope*. We conduct experiments on the CoderEval dataset using the
DeepSeek-V3 backbone model, and the results are shown in Table 5.
382

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
# infrared/core/inspector/helper.py
class SpecDictHelper:
    """Controls the spec dicts and provides useful methods to get spec info."""
    def get_option_spec(self, command_name, argument_name) -> Any
        """Gets the specification for the specified option name. """
    def iterate_option_specs(self) -> Generator[Tuple[dict, dict], Any, None]
        """Iterates over all the option specs. 
        Returns pair of parser and option on every iteration. """
    (2 methods omitted)
(3 classes/functions omitted)
Concise and relevant context
RepoScope
def _convert_non_cli_args(self, parser_name, values_dict):
    """Casts arguments to correct types by modifying values_dict param.
    By default all the values are strings.
    :param parser_name: The command name, e.g. main, virsh, ospd, etc
    :param values_dict: The dict of with arguments"""
    for opt_name, opt_value in values_dict.items():
        file_option_spec = self.spec_helper.get_option_spec(parser_name, opt_name)
        if file_option_spec.get('type', None) in ['int', ] or \
                file_option_spec.get('action', None) in ['count', ]:
            values_dict[opt_name] = int(opt_value)
(15 blocks omitted)
RLCoder
Target callee not retrieved
class SpecDictHelper(object):
    """Controls the spec dicts and provides useful methods to get spec info."""
    def iterate_option_specs(self):
        """Iterates over all the option specs.
        Returns pair of parser and option on every iteration."""
        for parser in self.iterate_parsers():
            for spec_option in self._get_all_options_spec(parser):
                yield parser, spec_option
    (8 methods omitted)
(7 classes/functions omitted)
Excessive irrelevant context
DRACO
Figure 5: An example of the code snippets retrieved by Re-
poScope and two baseline methods. The target function is
the same as the one in Figure 1.
As observed, RepoScope achieved consistent performance improve-
ments when integrated with both two approaches. Notably, the
integration with RepoCoder resulted in a 5.46% increase in pass@1
score. This result further highlights the broad applicability and
enhancement potential of RepoScope. Meanwhile, this indicates
that RepoScope still faces limitations in similarity-based context
retrieval, which presents an opportunity for further optimization
in future work.
Answer to RQ4: RepoScope can be effectively integrated with
existing repository-level code generation methods to achieve per-
formance improvements. This demonstrates the broad applicabil-
ity and enhancement potential of RepoScope, offering promising
directions for future optimization.
Table 5: Results of integrating RepoScope with RLCoder and
RepoCoder on CoderEval.
Method
Pass@1
Avg. # Token
RepoScope*
53.14
3962
+RLCoder
54.11 ↑1.83%
3975
+RepoCoder
56.04 ↑5.46%
7927
6
Discussion
6.1
Case Study
To intuitively illustrate the effectiveness of RepoScope, we present
an example in Figure 5, highlighting the differences in the retrieved
context between RepoScope and two baseline methods, RLCoder
and DRACO. RLCoder, using a reinforcement-learned retriever,
effectively retrieved a similar function _convert_non_cli_args.
However, due to slight differences in the callees used by the tar-
get function and the retrieved one, _convert_non_cli_args fails
to provide LLM with the complete set of relevant call informa-
tion. DRACO, on the other hand, employs dataflow analysis and
successfully locates the class SpecDictHelper and the method
iterate_option_specs, both of which are called by the target
function. However, it lacks a filtering mechanism for the retrieved
code elements, leading to excessive irrelevant code being included
in the context. For instance, the SpecDictHelper class alone intro-
duces eight unused methods, which may obscure the truly relevant
code and hinder the LLM’s focus. In contrast, RepoScope accu-
rately predicts the callees of the target function by conducting
in-depth static analysis and leveraging structural semantic infor-
mation within the repository, while minimizing irrelevant context.
This distinction largely explains why RepoScope achieves superior
performance in repository-level code generation tasks.
6.2
Threats to Validity
Threats to internal validity arise from the hyperparameter set-
tings used during the call chain prediction and the prompt con-
struction process. We performed a small-range grid search over
RepoScope’s hyperparameters on a small subset of data, selecting
the coefficients based on the best performance observed. It is antic-
ipated that alternative hyperparameter configurations may lead to
further improvements. Additionally, due to budget constraints, our
evaluation was restricted to a set of representative and advanced
LLMs as the backbone models. Given the rapid progress in the field
of LLMs, some models not included in this study may outperform
those we evaluated. We will continue to monitor developments in
this area and remain open to incorporating additional models in
future work. Besides, the current use of pass@1 as the sole eval-
uation metric limits a comprehensive assessment of code quality,
overlooking important attributes such as readability and maintain-
ability. We plan to introduce LLM-as-Judge in the future to evaluate
these attributes, providing a more comprehensive reflection of code
quality.
Threats to external validity relate to the generalizability of our
approach and findings. Given the widespread adoption of Python
language and the fact that most existing repository-level code gen-
eration benchmarks [11, 21, 24, 25, 43, 44] are built using Python, we
currently systematically evaluate our method only on this language.
Nevertheless, compared to Python, statically typed languages (e.g.,
Java or C++) offer more explicit and easily extractable type relation-
ships, which may make them even more amenable to our approach.
We conducted preliminary experiments on Java to validate this.
Using the Java subset of CoderEval (229 tasks after excluding one
faulty case) with GPT-4o-mini, RepoScope outperformed all base-
lines that can run on Java despite only a basic adaptation (e.g.,
polymorphism not well-handled). Specifically, RepoScope achieved
383

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
a pass@1 of 58.95%, whereas the best baseline, RLCoder, achieved
only 57.64%. We are willing to conduct a more systematic study of
RepoScope’s performance on such languages in future work.
Moreover, our call chain prediction relies on the assumption that
the call behavior of the target function can be inferred by similar
functions within the same repository. While this assumption holds
in most cases, the prediction performance may degrade if the target
function lacks similar counterparts (e.g., for small-scale repository),
if similar functions do not exhibit similar calling behaviors, or if the
calling behaviors are sparse. Nevertheless, these issues generally do
not occur in well-structured medium- to large-scale repositories. Ad-
ditionally, even when call chain prediction is suboptimal, contexts
from other perspectives can still provide valuable semantic infor-
mation to enhance code generation. To support this, we conducted
a validation on the 30% most dissimilar tasks On CoderEval and
DevEval benchmarks, determined by the similarity between each
target function and its most similar counterpart in the repository. In
these tasks across all four LLMs, RepoScope still outperformed the
best baseline DRACO with a 17.97% relative gain, even higher than
the 14.67% improvement in all tasks, demonstrating robustness of
RepoScope.
7
Related Work
Since the advent of programming languages, automated code gener-
ation has consistently attracted the attention of researchers [3, 4, 32,
33, 36, 40]. With the rapid advancement of large language models
(LLMs), many studies [14, 18, 29, 47, 48] have leveraged LLMs to
generate code for programming exercises or competitive program-
ming tasks, achieving remarkable performance. In recent years,
repository-level code generation has garnered increasing attention
due to its closer alignment with real-world software development
scenarios. This growing interest has led to the introduction of vari-
ous datasets, such as RepoEval [44], CoderEval [43], DevEval [25],
SWE-Bench [21], etc., further advancing the field.
To address the challenge of incorporating extensive repository
knowledge within the limited context window of LLMs, RAG tech-
niques [13] have been introduced into repository-level code gener-
ation. Early approaches [37, 44] treated code repositories as natural
language corpora, employing retrievers to identify a set of code
snippets that are most similar to the generation context. These
snippets then serve as relevant background knowledge for the LLM.
Building on this foundation, subsequent research has focused pri-
marily on three aspects: improving the accuracy of retrieving useful
information [9, 12, 28, 41], reducing unnecessary retrieval [10, 41],
and transforming the retrieved code snippets to make them more
interpretable for the LLM [12, 38].
However, similarity-based retrieval methods do not always suc-
ceed in identifying the most relevant information. Due to the formal
and structured nature of programming languages, code reposito-
ries contain rich program structural semantics which can serve as
valuable signals for retrieval. To address this, some research has
extended pure similarity-based retrieval. Among them, RepoFuse
[26] enriches the LLM context by including the code of imported
classes and functions. DRACO [8] goes further by performing data
flow analysis to identify local import information. Repohyper [34]
constructs a Repo-level Semantic Graph and uses a Graph Neural
Network (GNN) to compute node relevance scores for retrieval.
Different from these approaches, CoCoGen [5] adopts an iterative
generation strategy, where it uses feedback from the interpreter to
determine which code elements to retrieve. While these methods
improve generation performance to varying degrees, they still fall
short in fully leveraging program structural semantics. As a result,
①they may retrieve a large number of irrelevant codes [8, 26], or
②they have to rely on annotated data for training [34], which can
reduce performance and efficiency.
Recently, agent-based approaches have gained increasing atten-
tion for their strong performance in repository-level code genera-
tion. CodeAgent [45] integrates five programming tools and imple-
ments four agent strategies, enabling the LLM to determine retrieval
targets autonomously. LingmaAgent [30] constructs a knowledge
graph for the repository and combines Monte Carlo Tree Search
with LLM-based evaluation to identify the most relevant code snip-
pets. These snippets are then integrated into the agent’s pipeline.
However, these approaches face notable limitations in terms of cost
and efficiency due to the need for multiple LLM invocations.
Compared to existing approaches, RepoScope leverages in-depth
analysis of repository structural semantics to obtain more relevant
and diverse contextual information. Specifically, the core novelty
of our approach lies in the call-chain prediction module. This mod-
ule is the first to explicitly focus on potential callees of the target
function as a distinct context type and achieves relatively accurate
retrieval of such entities. More fundamentally, our method is the
first to leverage the entire repository’s structural information to
enhance structure-based retrieval. Existing approaches only con-
sider local information around the target function. For instance,
DRACO restricts retrieval to code elements directly accessible at
the completion site, overlooking non-local but potentially crucial el-
ements (e.g., structurally similar functions). In contrast, our method
expands the horizon: in the second step of call-chain prediction,
we incorporate the call behavior of similar functions across the
repository to compute entity scores. This design makes our re-
trieval both broader in scope and more robust than prior methods.
Moreover, RepoScope relies solely on static analysis, requires no
training, and each function generation only invokes the LLM once
after RSSG construction, making it more advantageous in terms of
cost and time efficiency. This contrasts with training-based meth-
ods, which may need full retraining when components change, and
agent-based methods, which repeatedly query LLMs at runtime,
incurring higher cost and latency.
8
Conclusion and Future Work
In this paper, we propose RepoScope, a novel framework leverag-
ing call chain-aware multi-view context for repository-level code
generation. RepoScope retrieves context from four distinct perspec-
tives, providing LLMs with comprehensive repository background
knowledge. Building upon our constructed Repository Structural Se-
mantic Graph, we propose an effective call chain prediction method
that enables the retrieval of more relevant contextual information.
We further introduce a structure-preserving serialization algorithm
to preserve hierarchical organization in prompts, making them
more interpretable to LLMs. Our training-free, single-query ap-
proach is highly efficient. Extensive evaluation results demonstrate
384

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
Liu et al.
that RepoScope substantially outperforms state-of-the-art baselines
on repository-level code generation benchmarks, while exhibiting
strong generalization and integration capabilities.
In addition to those mentioned in Section 6.2, we also plan to
pursue the following directions in future work: ①Investigate how
to infer specific user intentions from broader repository contexts
when only vague requirements are provided. ②Explore alternative
code snippet segmentation strategies (e.g., syntax-based segmen-
tation) and study their impact. ③Investigate more fine-grained
call-chain prediction techniques to further enhance accuracy. ④
Explore deeper integrations with agent-based frameworks, such as
enabling an agent to dynamically decide which contextual views
to retrieve for a given target function, or exposing the call-chain
prediction module as a callable tool for agents.
Acknowledgments
This research is supported by the National Natural Science Founda-
tion of China Grants Nos. 62302021 and 62177003.
References
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Floren-
cia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal
Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774
(2023).
[2] Anthropic. 2024. Claude Models Overview. https://docs.anthropic.com/en/docs/
about-claude/models/overview. Accessed: 2025-06-25.
[3] Antonio Valerio Miceli Barone and Rico Sennrich. 2017. A parallel corpus of
python functions and documentation strings for automated code documentation
and code generation. arXiv preprint arXiv:1707.02275 (2017).
[4] Brett A Becker, Paul Denny, James Finnie-Ansley, Andrew Luxton-Reilly, James
Prather, and Eddie Antonio Santos. 2023. Programming is hard-or at least it
used to be: Educational opportunities and challenges of ai code generation. In
Proceedings of the 54th ACM Technical Symposium on Computer Science Education
V. 1. 500–506.
[5] Zhangqian Bi, Yao Wan, Zheng Wang, Hongyu Zhang, Batu Guan, Fangxin Lu,
Zili Zhang, Yulei Sui, Hai Jin, and Xuanhua Shi. 2024. Iterative refinement of
project-level code context for precise code generation with compiler feedback.
arXiv preprint arXiv:2403.16792 (2024).
[6] Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu. 2024.
Bge m3-embedding: Multi-lingual, multi-functionality, multi-granularity text
embeddings through self-knowledge distillation. arXiv preprint arXiv:2402.03216
(2024).
[7] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde
De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, et al. 2021. Evaluating large language models trained on code.
arXiv preprint arXiv:2107.03374 (2021).
[8] Wei Cheng, Yuhan Wu, and Wei Hu. 2024. Dataflow-guided retrieval augmen-
tation for repository-level code completion. arXiv preprint arXiv:2405.19782
(2024).
[9] Ken Deng, Jiaheng Liu, He Zhu, Congnan Liu, Jingxin Li, Jiakai Wang, Peng Zhao,
Chenchen Zhang, Yanan Wu, Xueqiao Yin, et al. 2024. R2c2-coder: Enhancing
and benchmarking real-world repository-level code completion abilities of code
large language models. arXiv preprint arXiv:2406.01359 (2024).
[10] Wasi Uddin Ahmad Di Wu, Dejiao Zhang, Murali Krishna Ramanathan, and
Xiaofei Ma. [n. d.]. Repoformer: Selective retrieval for repository-level code
completion, 2024. URL https://arxiv. org/abs/2403.10059 ([n. d.]).
[11] Yangruibo Ding, Zijian Wang, Wasi Ahmad, Hantian Ding, Ming Tan, Nihal Jain,
Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth,
et al. 2023. Crosscodeeval: A diverse and multilingual benchmark for cross-file
code completion. Advances in Neural Information Processing Systems 36 (2023),
46701–46723.
[12] Xinyu Gao, Yun Xiong, Deze Wang, Zhenhan Guan, Zejian Shi, Haofen Wang,
and Shanshan Li. 2024. Preference-Guided Refactored Tuning for Retrieval
Augmented Code Generation. In Proceedings of the 39th IEEE/ACM International
Conference on Automated Software Engineering. 65–77.
[13] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yixin
Dai, Jiawei Sun, Haofen Wang, and Haofen Wang. 2023. Retrieval-augmented
generation for large language models: A survey. arXiv preprint arXiv:2312.10997
2, 1 (2023).
[14] Leonidas Gee, Milan Gritta, Gerasimos Lampouras, and Ignacio Iacobacci. 2024.
Code-optimise: Self-generated preference data for correctness and efficiency.
arXiv preprint arXiv:2406.12502 (2024).
[15] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. 2022.
Unixcoder: Unified cross-modal pre-training for code representation. arXiv
preprint arXiv:2203.03850 (2022).
[16] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang,
Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. 2024. DeepSeek-Coder: When the
Large Language Model Meets Programming–The Rise of Code Intelligence. arXiv
preprint arXiv:2401.14196 (2024).
[17] Mehadi Hassen and Philip K Chan. 2017. Scalable function call graph-based
malware classification. In Proceedings of the Seventh ACM on Conference on Data
and Application Security and Privacy. 239–248.
[18] Baizhou Huang, Shuai Lu, Weizhu Chen, Xiaojun Wan, and Nan Duan. 2023.
Enhancing large language models in coding through multi-perspective self-
consistency. arXiv preprint arXiv:2309.17272 (2023).
[19] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu
Liu, Jiajun Zhang, Bowen Yu, Keming Lu, Kai Dang, Yang Fan, Yichang Zhang,
An Yang, Rui Men, Fei Huang, Bo Zheng, Yibo Miao, Shanghaoran Quan, Yunlong
Feng, Xingzhang Ren, Xuancheng Ren, Jingren Zhou, and Junyang Lin. 2024.
Qwen2.5-Coder Technical Report. arXiv:2409.12186 [cs.CL] https://arxiv.org/
abs/2409.12186
[20] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh,
Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. 2024.
Gpt-4o system card. arXiv preprint arXiv:2410.21276 (2024).
[21] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir
Press, and Karthik Narasimhan. 2023. Swe-bench: Can language models resolve
real-world github issues? arXiv preprint arXiv:2310.06770 (2023).
[22] Daniel Le Métayer and David Schmidt. 1996. Structural operational semantics as
a basis for static program analysis. ACM Computing Surveys (CSUR) 28, 2 (1996),
340–343.
[23] Vladimir I Levenshtein et al. 1966. Binary codes capable of correcting deletions,
insertions, and reversals. In Soviet physics doklady, Vol. 10. Soviet Union, 707–710.
[24] Jia Li, Ge Li, Xuanming Zhang, Yihong Dong, and Zhi Jin. 2024. Evocodebench: An
evolving code generation benchmark aligned with real-world code repositories.
arXiv preprint arXiv:2404.00599 (2024).
[25] Jia Li, Ge Li, Yunfei Zhao, Yongmin Li, Huanyu Liu, Hao Zhu, Lecheng Wang,
Kaibo Liu, Zheng Fang, Lanshen Wang, et al. 2024.
Deveval: A manually-
annotated code generation benchmark aligned with real-world code repositories.
arXiv preprint arXiv:2405.19856 (2024).
[26] Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Peng Di, Hongwei
Chen, Chengpeng Wang, Gang Fan, et al. 2024. Repofuse: Repository-level code
completion with fused dual context. arXiv preprint arXiv:2402.14323 (2024).
[27] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Cheng-
gang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. 2024. Deepseek-v3
technical report. arXiv preprint arXiv:2412.19437 (2024).
[28] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and
Qianxiang Wang. 2024. Graphcoder: Enhancing repository-level code completion
via code context graph-based retrieval and language model. arXiv preprint
arXiv:2406.07003 (2024).
[29] Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu,
Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. 2023. Wizardcoder:
Empowering code large language models with evol-instruct. arXiv preprint
arXiv:2306.08568 (2023).
[30] Yingwei Ma, Qingping Yang, Rongyu Cao, Binhua Li, Fei Huang, and Yongbin
Li. 2024. Alibaba LingmaAgent: Improving Automated Issue Resolution via
Comprehensive Repository Exploration. arXiv preprint arXiv:2406.01422 (2024).
[31] Jonathan I Maletic and Andrian Marcus. 2001. Supporting program compre-
hension using semantic and structural information. In Proceedings of the 23rd
International Conference on Software Engineering. ICSE 2001. IEEE, 103–112.
[32] Kristian B Ølgaard, Anders Logg, and Garth N Wells. 2009. Automated code
generation for discontinuous Galerkin methods. SIAM Journal on Scientific
Computing 31, 2 (2009), 849–864.
[33] Kristian B Ølgaard and Garth N Wells. 2010. Optimizations for quadrature
representations of finite element tensors through automated code generation.
ACM Transactions on Mathematical Software (TOMS) 37, 1 (2010), 1–23.
[34] Huy Nhat Phan, Hoang Nhat Phan, Tien N Nguyen, and Nghi DQ Bui. 2024.
Repohyper: Better context retrieval is all you need for repository-level code
completion. CoRR (2024).
[35] Gordon D Plotkin. 2004. The origins of structural operational semantics. The
Journal of Logic and Algebraic Programming 60 (2004), 3–15.
[36] Saurabh Pujar, Luca Buratti, Xiaojie Guo, Nicolas Dupuis, Burn Lewis, Sahil
Suneja, Atin Sood, Ganesh Nalawade, Matt Jones, Alessandro Morari, et al. 2023.
Automated code generation for information technology tasks in yaml through
large language models. In 2023 60th ACM/IEEE Design Automation Conference
(DAC). IEEE, 1–4.
[37] Anton Shapkin, Denis Litvinov, Yaroslav Zharov, Egor Bogomolov, Timur Gal-
imzyanov, and Timofey Bryksin. 2023. Dynamic Retrieval-Augmented Generation.
385

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation
ICSE ’26, April 12–18, 2026, Rio de Janeiro, Brazil
arXiv preprint arXiv:2312.08976 (2023).
[38] Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, and
Torsten Scholak. 2023. Repofusion: Training code models to understand your
repository. arXiv preprint arXiv:2306.10998 (2023).
[39] Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2023. Repository-level
prompt generation for large language models of code. In International Conference
on Machine Learning. PMLR, 31693–31715.
[40] Rahul Vadisetty, Anand Polamarasetti, Sameerkumar Prajapati, Jinal Bhanubhai
Butani, et al. 2023. Leveraging Generative AI for Automated Code Generation
and Security Compliance in Cloud-Based DevOps Pipelines: A Review. Available
at SSRN 5218298 (2023).
[41] Yanlin Wang, Yanli Wang, Daya Guo, Jiachi Chen, Ruikai Zhang, Yuchi Ma, and
Zibin Zheng. 2024. Rlcoder: Reinforcement learning for repository-level code
completion. arXiv preprint arXiv:2407.19487 (2024).
[42] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. 2025. Qwen3 technical
report. arXiv preprint arXiv:2505.09388 (2025).
[43] Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang,
Ying Li, Qianxiang Wang, and Tao Xie. 2024. Codereval: A benchmark of prag-
matic code generation with generative pre-trained models. In Proceedings of the
46th IEEE/ACM International Conference on Software Engineering. 1–12.
[44] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao,
Jian-Guang Lou, and Weizhu Chen. 2023. Repocoder: Repository-level code com-
pletion through iterative retrieval and generation. arXiv preprint arXiv:2303.12570
(2023).
[45] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024. Codeagent: Enhancing
code generation with tool-integrated agent systems for real-world repo-level
coding challenges. arXiv preprint arXiv:2401.07339 (2024).
[46] Dan Zhao, Li Miao, Dafang Zhang, et al. 2015. Reusable function discovery by
call-graph analysis. Journal of Software Engineering and Applications 8, 04 (2015),
184.
[47] Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu,
Wenhu Chen, and Xiang Yue. 2024. Opencodeinterpreter: Integrating code gen-
eration with execution and refinement. arXiv preprint arXiv:2402.14658 (2024).
[48] Li Zhong, Zilong Wang, and Jingbo Shang. 2024. Debug like a human: A large
language model debugger via verifying runtime execution step-by-step. arXiv
preprint arXiv:2402.16906 (2024).
386

[Vista original de la página 13](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-13.png)

![Página PDF 13, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoScope/page-13.png)
