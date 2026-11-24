# A Hybrid Approach Combining Information Retrieval and Large Language Models for Traceability Link Recovery

- source_pdf: ../../../../../pdf/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

A Hybrid Approach Combining Information Retrieval and Large
Language Models for Traceability Link Recovery
Izumi Nagata
Kumamoto University
Kumamoto, Japan
nagata@st.cs.kumamoto-u.ac.jp
Israel Mendonça
Kumamoto University
Kumamoto, Japan
israel@cs.kumamoto-u.ac.jp
Kaito Utsunomiya
Akiba Republic Inc.
Tokyo, Japan
kaito.utsunomiya@akiba-
republic.com
Yuto Takaki
Akiba Republic Inc.
Tokyo, Japan
yuto.takaki@akiba-republic.com
Keisuke Sasaki
Nikkei Advanced Systems Inc.
Tokyo, Japan
keisuke.sasaki@nex.nikkei.com
Masayoshi Aritsugi
Kumamoto University
Kumamoto, Japan
aritsugi@cs.kumamoto-u.ac.jp
Abstract
Traceability information is essential for effective software main-
tenance and operation. In this study, we propose a traceability
link recovery approach that leverages the capabilities of LLMs for
linking requirements and source code. While LLMs demonstrate
powerful language comprehension, they still have limitations in
capturing domain-specific terminology. To overcome this limita-
tion, we combine the semantic similarity extracted by LLMs with
the textual similarity computed by an information retrieval (IR)-
based method. Experimental results demonstrate that our proposed
method improves the F1-score by up to 10.7 percentage points and
MAP by up to 9.1 percentage points compared to state-of-the-art
methods.
CCS Concepts
• Software and its engineering →Software maintenance tools;
• Information systems →Language models.
Keywords
Software Traceability, Requirements-to-Code, Textual Similarity,
Semantic Similarity
ACM Reference Format:
Izumi Nagata, Israel Mendonça, Kaito Utsunomiya, Yuto Takaki, Keisuke
Sasaki, and Masayoshi Aritsugi. 2026. A Hybrid Approach Combining Infor-
mation Retrieval and Large Language Models for Traceability Link Recov-
ery. In The 41st ACM/SIGAPP Symposium on Applied Computing (SAC ’26),
March 23–27, 2026, Thessaloniki, Greece. ACM, New York, NY, USA, 9 pages.
https://doi.org/10.1145/3748522.3779867
1
Introduction
Software traceability is the ability to relate artifacts created during
the development of a software system, enabling the system to be
described from different perspectives and levels of abstraction [30].
Traceability has been shown to improve software quality attributes
This work is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License.
SAC ’26, Thessaloniki, Greece
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2294-3/2026/03
https://doi.org/10.1145/3748522.3779867
and enhance the efficiency of maintenance tasks [7, 21]. However,
creating and maintaining traceability links becomes dramatically
more costly as the number of artifacts grows [12]. Moreover, man-
ually creating traceability links is prone to errors [4].
To address these challenges, many studies have explored auto-
mated or semi-automated traceability link recovery, often using
information retrieval (IR) [1, 3, 23] or machine learning (ML) [14, 19,
24, 25] techniques. IR-based methods leverage information retrieval
theory to recover traceability links based on textual similarity. De-
spite their effectiveness, they depend on the quality of the descrip-
tions in the artifacts, which can limit their performance. In contrast,
ML-based approaches have demonstrated superior performance,
but their reliance on costly annotated datasets [33] makes it hard
to apply them to unseen projects because each new project would
require creating annotations from scratch.
In this study, we develop a traceability link recovery method
applicable to unseen projects, reducing dependence on artifact
description quality. Unlike ML-based methods requiring training
data, our approach leverages LLMs to extract semantic informa-
tion without project-specific training. To address LLMs’ limita-
tions in capturing domain-specific terminology, we combine se-
mantic similarity—leveraging the language understanding capabili-
ties of LLMs—with textual similarity obtained through an IR-based
method. By generating candidate trace links based on the integrated
similarity, we can accurately capture artifact relationships across
semantic and textual dimensions. We explored two approaches to
unify the representation format: generating code from requirements
and generating natural language explanations from source code.
Preliminary experiments suggested that generating code from re-
quirements is more effective for recovering traceability links. Given
this observation, this paper focuses on discussing the approach of
generating code from requirements.
The key contributions of our study can be summarized as follows:
• We present a novel approach to recover traceability links
between requirements and source code using LLMs.
• We leverage an IR model to calculate textual similarity and
combine it with semantic similarity calculated by LLMs,
thereby capturing relationships between artifacts from both
semantic and textual perspectives.
• Experiments with multiple datasets demonstrate clearly the
effectiveness and limitations of our proposed method.

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

SAC ’26, March 23–27, 2026, Thessaloniki, Greece
I. Nagata et al.
The rest of this paper is organized as follows. Section 2 reviews
related work. Section 3 details the proposed approach. Section 4
presents the experimental setup. Section 5 discusses the experi-
mental results. Section 6 explains the threats to validity. Finally,
Section 7 concludes with a summary and a discussion of future
research directions.
2
Related Work
2.1
IR-Based Traceability Link Recovery
In the field of traceability link recovery, IR-based methods have been
widely adopted. These methods typically involve text preprocessing,
construction of a term-document matrix, and similarity calculation
using IR models such as the Vector Space Model (VSM) [3], Latent Se-
mantic Indexing (LSI) [23], and the Jensen–Shannon model (JS) [1].
While VSM represents documents as weighted term vectors com-
pared via cosine similarity, LSI extends VSM through dimensionality
reduction to capture latent semantics, and JS measures similarity
based on probabilistic distributions. We adopt the three models as
IR-based ones in this work.
IR-based methods rely on the words extracted from artifacts, and
their performance is highly influenced by the quality of artifact
descriptions. In this study, we address this limitation by integrating
semantic similarity with textual similarity, aiming to mitigate the
effect of description variations.
2.2
ML-Based Traceability Link Recovery
In recent years, there have been studies utilizing machine learning
for traceability link recovery. Mills et al. [25] proposed a learn-
ing approach for classification models, framing traceability link
recovery as a binary classification problem. Guo et al. [14] intro-
duced an approach that combines word embeddings with Recurrent
Neural Network (RNN) to incorporate semantic information of
artifacts and domain knowledge into traceability link generation.
Lin et al. [19] proposed Trace BERT (T-BERT), which leverages
pre-trained language models and transfer learning to address the
issue of performance degradation in deep learning models caused
by insufficient training data. Additionally, studies introducing ac-
tive learning have reported success in significantly reducing the
required amount of training data while maintaining comparable
performance [24].
These ML-based approaches demonstrate higher performance
than IR-based methods when some traceability links have been pre-
identified. However, their applicability to unseen projects where no
ground truth data is available has not been sufficiently validated. In
this study, we propose an approach that leverages LLMs, eliminating
the need for training and enabling applicability to systems where
traceability links are unspecified.
2.3
Utilization of LLMs for Traceability
Recently, there have been an increasing number of studies reporting
the use of LLMs in traceability-related tasks. Rodriguez et al. [29]
explored the process of prompt engineering for extracting trace link
predictions from LLMs. They examined several prompts, including
those with chain-of-thought, and demonstrated the potential of
LLMs in traceability. However, they also pointed out that achieving
Figure 1: Framework of the proposed method
high performance in each project requires careful prompt tuning,
which is time-consuming and may limit practical applicability.
North et al. [27] explored how to trace the relationship between
requirements and code during the code generation process, in the
context of the growing use of LLMs in software engineering for
code generation. Their findings suggest that it might be possible to
trace requirements to LLM-generated code by using the gradients
of the LLM output. While our research also utilizes code generation
using LLMs, it differs from their approach. They attempt to track
and maintain the traceability links during code generation, whereas
our research uses code generation to recover traceability links.
Fuchß et al. [11] proposed a novel traceability link recovery
approach that integrates LLMs with retrieval-augmented genera-
tion (RAG), demonstrating superior performance to state-of-the-
art methods in small-scale projects. Although our study does not
directly target the RAG framework, it aims to improve retrieval
performance, which can potentially contribute to enhancing the
retrieval component of RAG.
3
Methodology
Figure 1 illustrates the framework of our proposed method. The
following subsections explain it in detail.
3.1
Semantic Similarity Calculation
The calculation of semantic similarity consists of three steps: code
generation from the requirements, embeddings generation for both
the generated code and the source code, and calculation of similarity
between the generated embeddings.
3.1.1
Code Generation. While requirements describe system be-
havior conceptually, the source code defines concrete implemen-
tation procedures. This difference, along with the use of natural
versus programming languages, creates a significant semantic gap
between them [22]. To bridge this gap, we unify their representation
formats through code generation.
In this approach, the goal is not to produce executable code but
to reflect the intent of the requirement and assign meaningful iden-
tifiers. Maintaining the intent ensures semantic consistency, while
appropriate identifier naming contributes to better code understand-
ing and retrieval performance [20]. Based on these considerations,

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

A Hybrid Approach Combining IR and LLMs for Traceability Link Recovery
SAC ’26, March 23–27, 2026, Thessaloniki, Greece
we designed a prompt emphasizing these aspects. The prompt used
for code generation is shown as follows:
# Task Description
You are a software developer. Create {specific programming language}
code based on the following requirements.
# Requirements
{requirements}
# Notes
- Only implement the features described in the requirements. Avoid
adding unnecessary features or making assumptions.
- Ensure that variable names, function names, and class names are
appropriately named according to the requirements.
3.1.2
Embeddings Generation. Text embeddings in LLMs are typi-
cally generated through the following processes: (1) Tokenization:
The input text is split into tokens in order to convert it into a
format that can be processed by the LLM. (2) Encoding: The tok-
enized text is transformed into a high-dimensional vector repre-
sentation through the embedding layer of the LLM. (3) Contextual
Information Acquisition: Through the self-attention mechanism,
representations that consider the dependencies between tokens
are generated. This allows each token’s representation to reflect
the context, capturing complex relationships that cannot be repre-
sented at the word level. (4) Text Embedding Acquisition: From the
token-level contextual representations, a high-dimensional embed-
ding vector capturing the overall meaning of the text is generated
through methods such as the use of special tokens and aggregation
of the output.
The text embeddings generated by this process retain contextual
information, allowing for high-precision evaluation of the relation-
ship between texts through similarity calculations between the
embedding vectors.
3.1.3
Embeddings Similarity Calculation. Semantic similarity be-
tween the embeddings of both the generated code and the source
code is quantified using cosine similarity, which measures the angle
between vectors, as expressed in the following equation:
𝑠𝑖𝑚𝑠𝑒𝑚=
𝒗𝑇
𝑎𝒗𝑏
∥𝒗𝑎∥∥𝒗𝑏∥.
(1)
Here, 𝒗𝑎and 𝒗𝑏represent the embedding vectors of the generated
code and the source code, respectively.
3.2
Textual Similarity Calculation
In the calculation of semantic similarity mentioned in Section 3.1,
while the shared vocabulary between the artifacts is considered, it
is difficult to properly assess the importance of each vocabulary in
identifying traceability links. For instance, a match of frequently
occurring general words might be less significant than a match of
distinctive words that appear rarely in the document. The latter
is likely to be more important in identifying traceability links, but
simple semantic similarity cannot judge this difference in impor-
tance. In particular, since the extraction of semantic information
utilizes an LLM, it has the general ability to handle a wide range
of vocabulary and context, but it is not specialized in specific do-
main or system-specific terminology. Given this background, it is
essential to properly evaluate the significance of word matches
between the artifacts. By incorporating textual similarity, we can
reflect information based on the importance of words, leading to
more accurate identification of traceability links.
The textual similarity is calculated in three steps: (1) Corpus
Construction, where we preprocess textual data by removing stop
words, lemmatizing, and cleaning non-textual elements (with ad-
ditional camel case tokenization and language-specific stop word
removal for source code); (2) Corpus Indexing, where we build a
TF-IDF term-document matrix to emphasize distinctive terms and
down-weight common ones; and (3) Similarity Calculation, where
an IR model computes the textual similarity 𝑠𝑖𝑚𝑡𝑒𝑥based on the
TF-IDF representations.
3.3
Integration of Semantic and Textual
Similarities
The semantic and textual similarities are integrated to quantify the
overall similarity between the requirement and the source code. The
integration is defined as a linear combination of the two similarities,
as shown in the following equation:
𝑠𝑖𝑚𝑐𝑜𝑚𝑏= 𝜆𝑠𝑖𝑚𝑡𝑒𝑥+ (1 −𝜆)𝑠𝑖𝑚𝑠𝑒𝑚.
(2)
Here, 𝜆is a weighting coefficient between 0 and 1. Based on this
integrated similarity 𝑠𝑖𝑚𝑐𝑜𝑚𝑏, the ranking is performed in descend-
ing order, generating a ranking list of traceability link candidates.
Using 10% of the queries from each dataset (see Section 4.1) for
validation, we identified the 𝜆value that maximizes the F1-score for
each respective dataset, and then used the average as the uniform
weight in this study.
3.4
Two-Stage Filtering
In this study, we introduce a two-stage filtering approach designed
to reduce the search space, while maintaining Recall in traceability
link recovery, by excluding source code that is irrelevant to the re-
quirements. In challenging tasks within requirements engineering,
achieving high Recall is particularly important because the cost of
missing relevant items (false negatives) is high [5]. Therefore, our
filtering approach focuses on preserving Recall while effectively
reducing the number of candidate links.
3.4.1
Module-Level Filtering. In the first-stage filtering, we apply
clustering and LLM-based filtering to roughly eliminate irrelevant
modules while preserving potentially related ones. For clustering,
we adopt a simplified version of SARIF (Software Architecture
Recovery with Information Fusion) [35], which integrates multiple
types of information—code dependencies, textual data (e.g., method
names and comments), and folder structure—to classify source
code into semantically coherent modules. Specifically, to simplify
implementation, we use only call dependencies among the 13 types
originally considered in SARIF and replace the community detection
algorithm by Clauset et al. [8] with the Louvain algorithm [6].
After the source code is classified into modules, we perform
module-level filtering using an LLM. Functional descriptions of each
source file are first generated, and based on the file names and these
descriptions, the LLM evaluates whether each requirement is related
to a given module. Evaluating all possible combinations at the file
level results in an enormous number of input pairs, which increases
inference costs and computational resource consumption for the

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

SAC ’26, March 23–27, 2026, Thessaloniki, Greece
I. Nagata et al.
LLM. In contrast, the module-level approach substantially reduces
the number of requirement–module pairs, thereby lowering the
computational cost and enabling a more efficient filtering process.
The prompt employed in this filtering step is as follows:
You are a software architect. Your task is to identify any possible
connection between a software requirement and a source code module.
The default answer must always be "Yes".
Answer "No" only if it is absolutely clear that the requirement and
the module belong to completely different technical domains with no
conceivable overlap.
Guidelines for answering "Yes":
- Any overlap in keywords, concepts, functionality, or domain
- The module might indirectly support the requirement
- The requirement and module appear to be in the same subsystem or
could be connected through other code
3.4.2
Link-Level Filtering. In the second-stage, we perform link-
level filtering, which leverages the rank correlation between textual
similarity and semantic similarity to adjust the proportion of links
removed from the lower end of the integrated similarity list ac-
cording to its reliability. When the rank correlation is high, the
consistent evaluations between textual and semantic similarities
indicate higher reliability of the integrated similarity list, allowing
for more aggressive pruning of low-ranked candidates. Conversely,
when the correlation is low, the inconsistency suggests uncertainty,
and pruning is performed more conservatively to prevent the loss
of useful links. To achieve conservative filtering, the pruning ratio
𝑟is determined as a function of the rank correlation 𝜌as follows:
𝑟= ln 1 + ln(1 + 𝜌).
(3)
4
Experimental Setup
4.1
Evaluation System
We conducted our evaluation using four datasets from different
domains and scales: eTour, iTrust, SMOS, and eAnci. These datasets
are provided by the Center of Excellence for Software & Systems
Traceability (CoEST) [9] and are widely used in research on trace-
ability link recovery (e.g., [15, 16, 25]). Table 1 shows the statistics
for each dataset. iTrust consists of Java and JSP target artifacts; how-
ever, in this study, we only consider Java target artifacts and links.
The use cases in eTour, SMOS, and eAnci are structured according
to commonly used use case patterns, whereas the use cases in iTrust
consist only of event flows. eTour is primarily written in English,
but its source code identifiers and use case names are in Italian. In
contrast, SMOS is mainly written in Italian, but its identifiers are
in English. Artifact coverage represents the proportion of artifacts
linked. A low coverage may indicate issues with the requirements
or source code, or it could suggest problems with the quality of the
trace links.
4.2
Evaluation Metrics
To evaluate the performance, we use Precision, Recall, F1-score,
and Mean Average Precision (MAP). To fully automate traceability
link recovery, both Precision and Recall need to be high. However,
current unsupervised approaches do not achieve an F1-score suf-
ficient for full automation. Therefore, most existing methods are
used for semi-automated traceability link recovery rather than full
automation [28]. In semi-automated approaches, a ranked list of
candidate trace links is provided to developers, assisting them in
manually creating links. Thus, the quality of the ranking is crucial
for semi-automated traceability link recovery. MAP is calculated
over all candidate links without applying any filtering, providing a
comprehensive measure of the ranking quality.
4.3
Research Questions
We define the following four research questions:
RQ1: Does our approach of integrating semantic and textual
similarity demonstrate applicability across various IR models?
RQ2: Is our approach of generating code from requirements and
computing semantic similarity between generated and source code
embeddings effective for traceability recovery?
RQ3: Does two-stage filtering effectively reduce the search space
while maintaining Recall in traceability link recovery?
RQ4: How much does the proposed method improve perfor-
mance in traceability link recovery over state-of-the-art techniques?
To investigate RQ1, we evaluate the performance of an approach
that integrates semantic similarity using LLM embeddings with
three major IR models for computing textual similarity. Specif-
ically, we analyze the integration effects with the Vector Space
Model (VSM), Latent Semantic Indexing (LSI), and the probabilistic
Jensen and Shannon model (JS) distance. For the parameter 𝑘in LSI,
we set 𝑘= 30 based on values used in previous studies [26]. We use
the Wilcoxon signed-rank test [34] to evaluate the statistical signif-
icance of the performance differences between the integrated and
individual approaches, using F1-scores computed at Recall points
in 10% increments. According to [32], in information retrieval, lim-
ited query sizes and small performance differences result in low
statistical power. Therefore, for MAP, we report the 95% confidence
interval using the bootstrap method [10].
To investigate RQ2, we compare three approaches: Directly gen-
erating embeddings from requirements (DEM), generating code
from requirements and then computing embeddings (GEM), and
generating natural language explanations from source code and
then computing embeddings (NEM). Furthermore, to assess perfor-
mance variations across different LLMs, we conduct experiments
using both open-source and closed-source models.
Open-Source Models (OSM):
• Qwen2.5-Coder-7B-Instruct [17]: Used for code generation
and natural language description generation.
• jina-embeddings-v2-base-code [13]: Used for generating em-
beddings for DEM and GEM.
• jina-embeddings-v3 [31]: Used for generating embeddings
for NEM.
Closed-Source Models (CSM):
• GPT-4o [18]: Used for code generation and natural language
description generation.
• text-embedding-3-small1: Used for embedding generation.
These specific LLMs were selected primarily for their high reported
performance in relevant public benchmarks and their superior ca-
pacity for long context processing. We opted for models with large
input token capacity because accurately recovering traceability
links often requires the comprehensive analysis of lengthy software
1https://openai.com/index/new-embedding-models-and-api-updates

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

A Hybrid Approach Combining IR and LLMs for Traceability Link Recovery
SAC ’26, March 23–27, 2026, Thessaloniki, Greece
Table 1: Overview of the evaluated projects. All datasets consist of use cases as source artifacts and source code as target artifacts.
Project
Domain
Language
Source Code
Source Artifacts
Target Artifacts
Links
Covered Source
Covered Target
eTour
Tourism
EN/IT
Java
58
116
308
0.983
0.767
iTrust
Healthcare
EN
Java
131
226
286
0.802
0.385
SMOS
Education
IT/EN
Java
67
100
1044
1.000
0.680
eAnci
Governance
IT
Java
140
55
567
0.279
1.000
artifacts. jina-embeddings-v3 model supports both English and Ital-
ian, while jina-embeddings-v2-base-code supports only English. As
far as we know, the language support of Qwen2.5-Coder-7B-Instruct
remains unclear. CSM supports both English and Italian.
To investigate RQ3, we evaluate the impact of the proposed
two-stage filtering on the search space and Recall. For the filtering,
we only used Qwen2.5-Coder-7B-Instruct to reduce the API costs.
To investigate RQ4, we compare our results with three recent
unsupervised approaches: the first stage results of COMET [26],
FTLR [15], and LiSSA [11].
The first stage of COMET estimates the probability of trace-
ability links between artifacts by integrating information obtained
from multiple textual similarity measures through a hierarchical
Bayesian network model. The predictions generated by COMET
can be considered as a form of textual similarity. Therefore, we
choose to integrate COMET with semantic similarity and consider
this integrated model a form of our proposed approach. COMET
has three different versions, and we use the Maximum a Posteri-
ori (COMETMAP) version, which achieved the highest F1-score, for
comparison.
FTLR, on the other hand, is an approach that utilizes fine-grained
requirements-to-code relations for traceability link recovery. It cal-
culates similarity between artifact elements using word embeddings
and word mover’s distance. FTLR allows the selection of features
such as call dependencies (cd), method comments (mc), and use
case template structures (uct).
As described in Section 2.3, LiSSA is a RAG–based approach.
LiSSA provides several configurations; for comparison, we use the
configuration that achieved the best performance in the original
paper—specifically, the one without artifact preprocessing and with
the Chain-of-Thought prompting strategy. Since LiSSA is an ap-
proach that utilizes Top-k retrieval results (Top-k = 20 in the original
paper), a direct comparison based on MAP is not performed. Fur-
thermore, as Comet and LiSSA do not provide results on the eAnci
dataset, we do not include comparisons with them in this study.
5
Empirical Results
5.1
RQ1: Applicability of Integrated Similarity
Approach
Table 2 presents the experimental results for the four evaluated
systems, where the LLMs used in the experiments are CSM. Due
to page constraints, we only report the CSM results in this section,
although OSM demonstrated similar trends. In eTour, SMOS, and
eAnci, integrating semantic similarity with textual similarity im-
proved performance across all IR models compared to using either
semantic similarity or textual similarity alone.
On the other hand, in iTrust, while the integrated approach out-
performed textual similarity alone for all IR models, a performance
drop was observed compared to using semantic similarity alone.
This result may be partly attributed to the fact that the weight pa-
rameter used for integration was determined through preliminary
experiments on a subset of data and applied uniformly across all
datasets. In other words, the weighting may not have been optimal
for iTrust. A more detailed examination of the impact of different
weights will be provided in Section 5.2.
Moreover, the results observed with methods such as JS+GEM in
eTour and LSI+GEM in iTrust indicate that when the performance
of the textual similarity computed by the IR model is low, the
integrated performance also tends to be relatively low. This suggests
that if the IR model fails to capture textual similarity effectively,
the quality of the textual information provided for integration with
semantic similarity is reduced, thereby limiting the performance
gains achieved through integration.
5.2
RQ2: Effectiveness of Code Generation for
Traceability
Table 3 presents the performance comparison of IR+DEM, IR+GEM,
and IR+NEM for both OSM and CSM. Comparing OSM and CSM,
we observe that CSM tends to achieve better performance overall.
A noteworthy point is that in SMOS, the performance of IR+DEM
and IR+GEM in OSM is significantly lower than in CSM. A primary
reason for this performance gap is likely that SMOS is an Italian-
language dataset, while the embedding model used in OSM does
not support Italian. On the other hand, for IR+NEM, the embedding
model in OSM does support Italian, resulting in a smaller perfor-
mance gap compared to CSM, though OSM still performed worse.
This observation highlights the crucial importance of using models
that are compatible with the target language. Additionally, for the
eAnci dataset, despite being another Italian-language dataset, the
performance gap between OSM and CSM was relatively small. This
result may be attributed to the characteristics of the eAnci dataset,
which contains more than twice as many source artifacts as target
artifacts, and the coverage of source artifacts is only 0.279. This
means that over 70% of the source artifacts are not linked to any
correct target artifacts, suggesting potential issues with the quality
and completeness of the ground truth itself.
Comparing IR+DEM, IR+GEM, and IR+NEM in CSM, the aver-
age F1-score shows that IR+DEM and IR+GEM performed similarly,
while IR+NEM tends to perform slightly worse. In terms of the

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

SAC ’26, March 23–27, 2026, Thessaloniki, Greece
I. Nagata et al.
Table 2: Experimental results of each approach. The approaches that showed improved performance compared to the individual
approaches before integration are highlighted in bold. ∗indicates a statistically significant improvement (p-value < 0.05) over
the corresponding IR-ONLY, while † indicates statistical significance over the GEM-ONLY baseline. 95% confidence intervals (CI)
are reported for MAP.
eTour
iTrust
SMOS
eAnci
Approach
Pre
Rec
F1
MAP [95% CI]
Pre
Rec
F1
MAP [95% CI]
Pre
Rec
F1
MAP [95% CI]
Pre
Rec
F1
MAP [95% CI]
GEM-ONLY
0.333
0.419
0.371
0.508 [0.446, 0.569]
0.312
0.283
0.297
0.333 [0.277, 0.386]
0.309
0.609
0.410
0.439 [0.398, 0.484]
0.213
0.252
0.231
0.133 [0.097, 0.173]
VSM-ONLY
0.498
0.422
0.456
0.456 [0.388, 0.527]
0.197
0.301
0.238
0.216 [0.175, 0.258]
0.386
0.302
0.339
0.372 [0.338, 0.406]
0.255
0.312
0.281
0.123 [0.087, 0.159]
LSI-ONLY
0.506
0.422
0.460
0.439 [0.373, 0.507]
0.140
0.245
0.178
0.152 [0.120, 0.187]
0.296
0.393
0.338
0.341 [0.308, 0.374]
0.314
0.257
0.283
0.132 [0.094, 0.174]
JS-ONLY
0.435
0.295
0.352
0.368 [0.311, 0.437]
0.156
0.227
0.185
0.206 [0.165, 0.253]
0.245
0.563
0.342
0.297 [0.268, 0.324]
0.279
0.240
0.258
0.122 [0.088, 0.155]
VSM+GEM
0.541
0.432
0.480∗† 0.538 [0.472, 0.599]
0.274
0.325
0.297∗0.318 [0.265, 0.376]
0.388
0.471
0.426∗† 0.487 [0.449, 0.529]
0.311
0.275
0.292† 0.136 [0.098, 0.176]
LSI+GEM
0.561
0.464
0.508∗† 0.543 [0.474, 0.611]
0.256
0.224
0.239∗0.262 [0.220, 0.306]
0.383
0.471
0.423∗† 0.477 [0.438, 0.517]
0.404
0.235
0.297† 0.136 [0.097, 0.178]
JS+GEM
0.507
0.351
0.415∗† 0.512 [0.444, 0.582]
0.307
0.276
0.291∗0.319 [0.272, 0.374]
0.313
0.619
0.415∗† 0.482 [0.438, 0.525]
0.343
0.243
0.285
0.135 [0.098, 0.172]
(a) eTour
(b) iTrust
(c) SMOS
(d) eAnci
Figure 2: Trends in F1-score and MAP with changes in integration weights
average MAP score, IR+GEM achieves the highest score across all
datasets. The datasets used in this study have the characteristic of
having well-documented requirements. Therefore, in the IR+GEM
approach for generating code from requirements, it is assumed that
the LLMs are able to appropriately understand these clear require-
ments and generate code that reflects the intended meaning. In
the IR+NEM approach, which generates natural language descrip-
tions from source code, it is essential to accurately understand the
meanings of code elements such as variable names, method names,
and identifiers. If these elements are misunderstood, the generated
descriptions may deviate from the original intent of the code.
These results are based on integration weight 𝜆determined
through preliminary experiments. To examine its impact, we var-
ied 𝜆from 0 to 1 and observed changes in F1-score and MAP for
CSM (Figure 2). Based on the results of the preliminary experiments,
the value of 𝜆was set to 0.50 for VSM+DEM, 0.49 for VSM+GEM,
and 0.55 for VSM+NEM, respectively. From the analysis results, ex-
cept for eTour, F1-score shows that IR+DEM and IR+GEM perform
similarly, while in terms of MAP, IR+GEM achieves the highest
performance across all datasets. Additionally, across all datasets
and methods, as 𝜆gradually increases from 0, both F1-score and
MAP improve, but beyond a certain threshold, they begin to decline.
The same trend was observed with OSM only on all datasets ex-
cept SMOS due to language fit issues. This result demonstrates the
effectiveness of integrating semantic and textual similarity. Interest-
ingly, whether semantic similarity alone (𝜆=0) or textual similarity
alone (𝜆=1) achieves higher performance, the integration of both
can enhance overall results by leveraging the strengths of each ap-
proach. This suggests that semantic and textual similarities capture
different aspects of the relationships between artifacts. However,
it also indicates that, depending on the chosen weight, the perfor-
mance may be lower than when using either semantic or textual
similarity alone. In fact, in iTrust, the optimal lambda value for
VSM+DEM and VSM+GEM is around 0.3, and with the lambda
value set in this study, the performance is almost the same as that
of semantic similarity alone. The optimal weights vary by dataset,
and analyzing the characteristics of the dataset may help determine
the optimal weights. Determining the optimal weight remains an
important research challenge in the future.
5.3
RQ3: Effectiveness of Filtering
Table 4 shows the impact of the two-stage filtering process using
VSM on the number of candidate links and Recall across all datasets.
Overall, the first-stage filtering effectively reduced the search space
while maintaining high Recall, removing about 30% of the candi-
dates on average and preserving over 0.85 Recall for all projects.
The second-stage further decreased the number of candidate links,
achieving an overall reduction of about 50% compared to the unfil-
tered setting. For most projects, this additional filtering only caused
a marginal drop in Recall, indicating that the adaptive pruning strat-
egy successfully retained most relevant links. However, for eAnci,
the Recall decreased markedly after the second-stage filtering. This
suggests that the similarity list itself did not perform well for this
dataset, leading to removal of correct links from the lower-ranked

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

A Hybrid Approach Combining IR and LLMs for Traceability Link Recovery
SAC ’26, March 23–27, 2026, Thessaloniki, Greece
Table 3: Evaluation of each method (IR+DEM, IR+GEM, IR+NEM) and each model (OSM, CSM). For each dataset, the best-
performing approach combined with each IR model is highlighted in bold, as well as the one with the highest performance
averaged across all IR models.
VSM
LSI
JS
AVERAGE
Pre
Rec
F1
MAP
Pre
Rec
F1
MAP
Pre
Rec
F1
MAP
F1
MAP
eTour
O
S
M
IR+DEM
0.479
0.477
0.478
0.490
0.515
0.455
0.483
0.496
0.433
0.419
0.426
0.441
0.462
0.476
IR+GEM
0.495
0.477
0.486
0.501
0.536
0.464
0.497
0.511
0.410
0.451
0.430
0.463
0.471
0.492
IR+NEM
0.500
0.461
0.480
0.528
0.435
0.529
0.477
0.528
0.521
0.360
0.426
0.496
0.461
0.517
C
S
M
IR+DEM
0.410
0.529
0.462
0.515
0.515
0.435
0.472
0.529
0.463
0.390
0.423
0.494
0.452
0.513
IR+GEM
0.541
0.432
0.480
0.538
0.561
0.464
0.508
0.543
0.507
0.351
0.415
0.512
0.467
0.531
IR+NEM
0.516
0.474
0.494
0.536
0.406
0.617
0.490
0.547
0.358
0.581
0.443
0.499
0.476
0.527
iTrust
O
S
M
IR+DEM
0.269
0.255
0.262
0.268
0.174
0.304
0.221
0.221
0.202
0.346
0.255
0.292
0.246
0.260
IR+GEM
0.220
0.315
0.259
0.267
0.196
0.276
0.229
0.250
0.240
0.329
0.277
0.303
0.255
0.273
IR+NEM
0.237
0.290
0.261
0.280
0.225
0.213
0.219
0.226
0.305
0.213
0.251
0.284
0.243
0.263
C
S
M
IR+DEM
0.282
0.318
0.299
0.304
0.278
0.245
0.260
0.238
0.360
0.266
0.306
0.306
0.288
0.283
IR+GEM
0.274
0.325
0.297
0.318
0.256
0.224
0.239
0.262
0.307
0.276
0.291
0.319
0.276
0.300
IR+NEM
0.280
0.290
0.285
0.300
0.243
0.227
0.235
0.244
0.228
0.259
0.242
0.303
0.254
0.282
SMOS
O
S
M
IR+DEM
0.250
0.627
0.357
0.357
0.233
0.694
0.349
0.341
0.232
0.685
0.347
0.310
0.351
0.336
IR+GEM
0.305
0.435
0.359
0.399
0.276
0.470
0.348
0.378
0.241
0.632
0.348
0.349
0.352
0.375
IR+NEM
0.281
0.609
0.384
0.430
0.268
0.631
0.376
0.409
0.267
0.633
0.376
0.408
0.379
0.416
C
S
M
IR+DEM
0.298
0.721
0.421
0.476
0.347
0.530
0.419
0.466
0.320
0.603
0.418
0.454
0.419
0.465
IR+GEM
0.388
0.471
0.426
0.487
0.383
0.471
0.423
0.477
0.313
0.619
0.415
0.482
0.421
0.482
IR+NEM
0.297
0.596
0.396
0.463
0.381
0.399
0.390
0.450
0.295
0.557
0.386
0.440
0.390
0.451
eAnci
O
S
M
IR+DEM
0.292
0.303
0.297
0.128
0.369
0.259
0.305
0.130
0.279
0.226
0.250
0.130
0.284
0.129
IR+GEM
0.308
0.284
0.295
0.129
0.321
0.250
0.281
0.133
0.229
0.272
0.248
0.135
0.275
0.132
IR+NEM
0.307
0.275
0.290
0.130
0.365
0.243
0.292
0.132
0.371
0.206
0.265
0.130
0.282
0.131
C
S
M
IR+DEM
0.351
0.263
0.301
0.129
0.426
0.250
0.316
0.131
0.355
0.206
0.261
0.129
0.293
0.130
IR+GEM
0.311
0.275
0.292
0.136
0.404
0.235
0.297
0.136
0.343
0.243
0.285
0.135
0.291
0.136
IR+NEM
0.288
0.235
0.259
0.122
0.327
0.261
0.290
0.129
0.207
0.233
0.219
0.125
0.256
0.126
Table 4: Effect of Filtering on the Number of Candidate Links
and Recall
w/o Filtering
w/ 1st Filter
w/ 1st & 2nd Filters
Project
#Links
Recall
#Links
Recall
#Links
Recall
eTour
6,728
1.000
3,922
0.938
2,657
0.919
iTrust
29,606
1.000
22,738
0.927
15,632
0.874
SMOS
6,700
1.000
5,438
0.928
4,710
0.904
eAnci
7,700
1.000
5,011
0.868
3,624
0.628
portion during pruning. In other words, there may be elements
that were not captured by either the textual or semantic similarity
measures, indicating that additional similarity perspectives or new
metrics may be required to better capture the underlying relation-
ships.
5.4
RQ4: Comparison with State-of-the-Art
Methods
Table 5 presents a comparison of our approach against recent unsu-
pervised methods. We adopt VSM as the IR model in the comparison
because VSM offers stable performance, as shown in Table 2, and
does not require hyperparameter tuning. We define the baseline as
the original, non-integrated approaches (COMETMAP, FTLR, and
LiSSA). Our proposed approach is represented by VSM+GEM and
COMETMAP+GEM. For COMETMAP, the results correspond to the
threshold that maximized the F1-score when adjusted in increments
of 0.01. For FTLR, the majority threshold was set according to the
value specified in the original paper, while only the final threshold
was optimized. Additionally, the integration weight for combin-
ing COMETMAP with semantic similarity was determined through
preliminary experiments on a subset, as in previous cases.

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

SAC ’26, March 23–27, 2026, Thessaloniki, Greece
I. Nagata et al.
Table 5: Comparison results between our proposed method and state-of-the-art methods
eTour
iTrust
SMOS
eAnci
Approach
Pre
Rec
F1
MAP
Pre
Rec
F1
MAP
Pre
Rec
F1
MAP
Pre
Rec
F1
MAP
LiSSA[11]
0.409
0.734
0.526
-
0.199
0.451
0.276
-
0.590
0.195
0.294
-
-
-
-
-
FTLR+mc+cd [15]
0.268
0.610
0.372
0.277
0.180
0.322
0.231
0.258
0.337
0.427
0.377
0.418
0.191
0.347
0.247
0.149
FTLR+uct+mc+cd [15]
0.456
0.516
0.484
0.471
0.180
0.322
0.231
0.258
0.376
0.431
0.402
0.442
0.232
0.293
0.259
0.150
COMETMAP [26]
0.410
0.468
0.437
0.467
0.361
0.231
0.281
0.245
0.166
0.816
0.276
0.293
-
-
-
-
COMETMAP+GEM
0.448
0.445
0.446
0.519
0.331
0.346
0.338
0.349
0.314
0.569
0.405
0.448
-
-
-
-
VSM+GEM
0.541
0.432
0.480
0.538
0.274
0.325
0.297
0.318
0.388
0.471
0.426
0.487
0.311
0.275
0.292
0.136
The evaluation results reveal that the proposed method outper-
forms the baseline in all cases except for the F1-score in eTour and
the MAP in eAnci. In iTrust, COMETMAP+GEM demonstrates a sig-
nificant improvement over the FTLR, with the F1-score increasing
by 10.7 percentage points (= (0.338 −0.231) × 100) and MAP by 9.1
percentage points (= (0.349−0.258)×100). FTLR+uct+mc+cd shows
significant performance improvements over FTLR+mc+cd. How-
ever, in iTrust, which does not adhere to the use case template and
where the uct option is unavailable, no performance improvement
was observed, and the results remained low. In contrast, our pro-
posed method demonstrates stable performance across all datasets,
regardless of the requirements’ writing style.
It is worth noting that FTLR reported results on eTour and SMOS
using translated datasets, where identifiers and use case names
were converted into the primary language. We confirmed that ap-
plying our approach to the translated datasets slightly improved the
performance. However, because translation is not the main focus
of this study, our results are based on the original, untranslated
datasets.
Comparing COMETMAP with COMETMAP+GEM, it was con-
firmed that integrating with semantic similarity improves perfor-
mance across all datasets, including eTour, iTrust, and SMOS. This
result suggests that the integration approach with semantic simi-
larity was effective, as COMETMAP generates predictions based on
the results of multiple IR models.
While LiSSA achieved the highest performance on the eTour
dataset, our proposed approach demonstrated higher performance
on both the iTrust and SMOS datasets. This is likely because LiSSA
adopts an approach based on the Top-20 retrieval results. In eTour,
which has a relatively small project size and a limited number of
correct links, a large proportion of the correct links are likely to
be included within the Top-20 results. In contrast, for the larger
project iTrust, although recall remains relatively high, many false
positives are included in the Top-20 candidates. Although the LLM
determines whether each candidate constitutes a correct link, the
large number of false positives likely contributes to the low Preci-
sion, which in turn reduces the F1-score. For SMOS, which contains
a greater number of correct links, the Top-20 range is insufficient to
comprehensively cover them, also resulting in lower performance.
6
Threats to Validity
In this section, we present the main threats that may affect the
validity of the results of this study.
Internal validity: In this study, the integration weight 𝜆was
fixed across datasets based on preliminary experiments, rather than
optimized individually. While this ensured generalizability, it may
have limited performance on datasets with differing characteristics.
Additionally, code generation from requirements focused on cap-
turing semantic intent and appropriate identifier naming. Although
suitable for traceability link recovery, variability in the quality and
consistency of generated code—caused by ambiguous requirements
or inconsistent styles—may have influenced the results and intro-
duced uncertainty in performance evaluation.
External validity: In this study, we evaluated a limited number
of projects. These projects are standard datasets widely used in the
field of traceability link recovery research and cover various project
sizes and domains. However, caution is required when interpreting
whether the results obtained from these limited projects can be
applied to other software projects with different characteristics.
We also experimented with both open-source and closed-source
LLMs. However, since LLMs differ in architecture, training data, and
size, the models used in this study may not necessarily represent
the optimal choice for this task.
7
Conclusion
In this study, we proposed a novel approach utilizing LLMs and an
IR model for traceability link recovery between requirements and
source code. Our method combines semantic similarity—leveraging
the advanced language understanding capabilities of LLMs—with
textual similarity obtained through an IR-based method.
To evaluate the performance of the proposed approach, we con-
ducted an empirical study on four projects commonly used in the
community: eTour, iTrust, SMOS, and eAnci. The results demon-
strated the effectiveness of integrating semantic similarity with
textual similarity. Compared to state-of-the-art unsupervised trace-
ability link recovery methods, the proposed approach achieved up
to 10.7 percentage points higher F1-score and 9.1 percentage points
higher MAP.
In this study, we employed a linear combination to integrate
semantic and textual similarity. However, this simple approach may
not fully capture the complex interactions between the two sig-
nals. In future work, we plan to explore optimizing the integration
method itself, including nonlinear approaches, to better account
for these interactions. Furthermore, the current performance is not
sufficient to fully automate traceability link recovery, necessitating
further improvements including prompt optimization to enhance

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

A Hybrid Approach Combining IR and LLMs for Traceability Link Recovery
SAC ’26, March 23–27, 2026, Thessaloniki, Greece
its effectiveness. Recently, approaches leveraging requirements clas-
sification have attracted significant attention and have become a
promising trend in the field of traceability link recovery [16, 2].
Incorporating such approaches into this research has the potential
to greatly contribute to future performance improvements.
GenAI Disclosure Statement
We clearly wrote all the places where and the ways in which we
used generative AI software tools in this study in the body of this
paper; Otherwise we did not use generative AI software tools except
to refine the English grammar in this paper.
References
[1]
Aharon Abadi, Mordechai Nisenson, and Yahalomit Simionovici. 2008. A trace-
ability technique for specifications. In 2008 16th IEEE International Conference
on Program Comprehension, 103–112. doi:10.1109/ICPC.2008.30.
[2]
Waleed Abdeen, Michael Unterkalmsteiner, Krzysztof Wnuk, Alexandros Chir-
toglou, Christoph Schimanski, and Heja Goli. 2024. Multi-label requirements
classification with large taxonomies. In 2024 IEEE 32nd International Require-
ments Engineering Conference (RE), 264–274. doi:10.1109/RE59067.2024.00033.
[3]
Giuliano Antoniol, Gerardo Canfora, Gerardo Casazza, Andrea De Lucia, and
Ettore Merlo. 2002. Recovering traceability links between code and documen-
tation. IEEE Transactions on Software Engineering, 28, 10, 970–983. doi:10.1109
/TSE.2002.1041053.
[4]
Thazin Win Win Aung, Huan Huo, and Yulei Sui. 2020. A literature review
of automatic traceability links recovery for software change impact analysis.
In Proceedings of the 28th International Conference on Program Comprehension
(ICPC ’20). Association for Computing Machinery, Seoul, Republic of Korea,
14–24. isbn: 9781450379588. doi:10.1145/3387904.3389251.
[5]
Daniel M. Berry. 2021. Empirical evaluation of tools for hairy requirements
engineering tasks. Empirical Software Engineering, 26, 111. doi:10.1007/s10664-
021-09986-0.
[6]
Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne
Lefebvre. 2008. Fast unfolding of communities in large networks. Journal of
Statistical Mechanics: Theory and Experiment, 2008, 10, (Oct. 2008), P10008.
doi:10.1088/1742-5468/2008/10/P10008.
[7]
Sofia Charalampidou, Apostolos Ampatzoglou, Evangelos Karountzos, and
Paris Avgeriou. 2021. Empirical studies on software traceability: A mapping
study. Journal of Software: Evolution and Process, 33, 2, e2294. e2294 JSME-19-
0120.R2. eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/smr.2294.
doi:10.1002/smr.2294.
[8]
Aaron Clauset, M. E. J. Newman, and Cristopher Moore. 2004. Finding commu-
nity structure in very large networks. Phys. Rev. E, 70, 6, (Dec. 2004), 066111.
doi:10.1103/PhysRevE.70.066111.
[9]
Dataset. Center of Excellence for Software & Systems Traceability. Retrieved
Mar. 9, 2025 from http://sarec.nd.edu/coest/datasets.html.
[10]
Bradley Efron. 1979. Bootstrap methods: another look at the jackknife. The
Annals of Statistics, 7, 1, 1–26. doi:10.1214/aos/1176344552.
[11]
Dominik Fuchß, Tobias Hey, Jan Keim, Haoyu Liu, Niklas Ewald, Tobias Thirolf,
and Anne Koziolek. 2025. LiSSA: toward generic traceability link recovery
through retrieval-augmented generation. In 2025 IEEE/ACM 47th International
Conference on Software Engineering (ICSE), 1396–1408. doi:10.1109/ICSE55347.2
025.00186.
[12]
Achraf Ghabi and Alexander Egyed. 2015. Exploiting traceability uncertainty
among artifacts and code. Journal of Systems and Software, 108, 178–192. doi:1
0.1016/j.jss.2015.06.037.
[13]
Michael Günther et al. 2024. Jina embeddings 2: 8192-token general-purpose
text embeddings for long documents. https://arxiv.org/abs/2310.19923 arXiv:
2310.19923 [cs.CL].
[14]
Jin Guo, Jinghui Cheng, and Jane Cleland-Huang. 2017. Semantically enhanced
software traceability using deep learning techniques. In 2017 IEEE/ACM 39th
International Conference on Software Engineering (ICSE), 3–14. doi:10.1109
/ICSE.2017.9.
[15]
Tobias Hey, Fei Chen, Sebastian Weigelt, and Walter F. Tichy. 2021. Improving
traceability link recovery using fine-grained requirements-to-code relations.
In 2021 IEEE International Conference on Software Maintenance and Evolution
(ICSME), 12–22. doi:10.1109/ICSME52107.2021.00008.
[16]
Tobias Hey, Jan Keim, and Sophie Corallo. 2024. Requirements classification
for traceability link recovery. In 2024 IEEE 32nd International Requirements
Engineering Conference (RE), 155–167. doi:10.1109/RE59067.2024.00024.
[17]
Binyuan Hui et al. 2024. Qwen2.5-Coder technical report. https://arxiv.org/abs
/2409.12186 arXiv: 2409.12186 [cs.CL].
[18]
Aaron Hurst et al. 2024. GPT-4o system card. https://arxiv.org/abs/2410.21276
arXiv: 2410.21276 [cs.CL].
[19]
Jinfeng Lin, Yalin Liu, Qingkai Zeng, Meng Jiang, and Jane Cleland-Huang. 2021.
Traceability transformed: generating more accurate links with pre-trained
BERT models. In 2021 IEEE/ACM 43rd International Conference on Software
Engineering (ICSE), 324–335. doi:10.1109/ICSE43902.2021.00040.
[20]
Shuai Lu et al. 2021. CodeXGLUE: a machine learning benchmark dataset for
code understanding and generation. In Proceedings of the Neural Information
Processing Systems Track on Datasets and Benchmarks. J. Vanschoren and S.
Yeung, (Eds.) Vol. 1. https://datasets-benchmarks-proceedings.neurips.cc/pape
r_files/paper/2021/file/c16a5320fa475530d9583c34fd356ef5-Paper-round1.p
df.
[21]
Patrick Mäder and Alexander Egyed. 2015. Do developers benefit from re-
quirements traceability when evolving and maintaining a software system?
Empirical Software Engineering, 20, 2, 413–441. doi:10.1007/s10664-014-9314-z.
[22]
Junayed Mahmud, Fahim Faisal, Raihan Islam Arnob, Antonios Anastasopou-
los, and Kevin Moran. 2021. Code to comment translation: a comparative study
on model effectiveness & errors. In Proceedings of the 1st Workshop on Natural
Language Processing for Programming (NLP4Prog 2021). Association for Com-
putational Linguistics, Online, (Aug. 2021), 1–16. doi:10.18653/v1/2021.nlp4pro
g-1.1.
[23]
Andrian Marcus and Jonathan I. Maletic. 2003. Recovering documentation-
to-source-code traceability links using latent semantic indexing. In 25th In-
ternational Conference on Software Engineering, 2003. Proceedings. 125–135.
doi:10.1109/ICSE.2003.1201194.
[24]
Chris Mills, Javier Escobar-Avila, Aditya Bhattacharya, Grigoriy Kondyukov,
Shayok Chakraborty, and Sonia Haiduc. 2019. Tracing with less data: active
learning for classification-based traceability link recovery. In 2019 IEEE Inter-
national Conference on Software Maintenance and Evolution (ICSME), 103–113.
doi:10.1109/ICSME.2019.00020.
[25]
Chris Mills, Javier Escobar-Avila, and Sonia Haiduc. 2018. Automatic traceabil-
ity maintenance via machine learning classification. In 2018 IEEE International
Conference on Software Maintenance and Evolution (ICSME), 369–380. doi:10.11
09/ICSME.2018.00045.
[26]
Kevin Moran, David N. Palacio, Carlos Bernal-Cárdenas, Daniel McCrystal,
Denys Poshyvanyk, Chris Shenefiel, and Jeff Johnson. 2020. Improving the
effectiveness of traceability link recovery using hierarchical bayesian networks.
In Proceedings of the ACM/IEEE 42nd International Conference on Software
Engineering (ICSE ’20). Association for Computing Machinery, Seoul, South
Korea, 873–885. isbn: 9781450371216. doi:10.1145/3377811.3380418.
[27]
Marc North, Amir Atapour-Abarghouei, and Nelly Bencomo. 2024. Code gra-
dients: towards automated traceability of LLM-generated code. In 2024 IEEE
32nd International Requirements Engineering Conference (RE), 321–329. doi:10.1
109/RE59067.2024.00038.
[28]
Annibale Panichella, Andrea De Lucia, and Andy Zaidman. 2015. Adaptive user
feedback for IR-based traceability recovery. In 2015 IEEE/ACM 8th International
Symposium on Software and Systems Traceability, 15–21. doi:10.1109/SST.2015
.10.
[29]
Alberto D. Rodriguez, Katherine R. Dearstyne, and Jane Cleland-Huang. 2023.
Prompts matter: insights and strategies for prompt engineering in automated
software traceability. In 2023 IEEE 31st International Requirements Engineering
Conference Workshops (REW). IEEE Computer Society, Los Alamitos, CA, USA,
(Sept. 2023), 455–464. doi:10.1109/REW57809.2023.00087.
[30]
George Spanoudakis and Andrea Zisman. 2005. Software traceability: a roadmap.
In Handbook of Software Engineering and Knowledge Engineering. World Scien-
tific, (Aug. 2005), 395–428. eprint: https://www.worldscientific.com/doi/pdf/10
.1142/9789812775245_0014. doi:10.1142/9789812775245_0014.
[31]
Saba Sturua et al. 2024. Jina-embeddings-v3: multilingual embeddings with
task LoRA. https://arxiv.org/abs/2409.10173 arXiv: 2409.10173 [cs.CL].
[32]
Julián Urbano, Harlley Lima, and Alan Hanjalic. 2019. Statistical significance
testing in information retrieval: an empirical analysis of type I, type II and
type III errors. In Proceedings of the 42nd International ACM SIGIR Conference
on Research and Development in Information Retrieval (SIGIR’19). Association
for Computing Machinery, Paris, France, 505–514. isbn: 9781450361729. doi:10
.1145/3331184.3331259.
[33]
Bangchao Wang, Zhiyuan Zou, Hongyan Wan, Yuanbang Li, Yang Deng,
and Xingfu Li. 2024. An empirical study on the state-of-the-art methods for
requirement-to-code traceability link recovery. Journal of King Saud University
- Computer and Information Sciences, 36, 6, 102118. doi:10.1016/j.jksuci.2024.102
118.
[34]
Frank Wilcoxon. 1945. Individual comparisons by ranking methods. Biometrics
Bulletin, 1, 6, 80–83. doi:10.2307/3001968.
[35]
Yiran Zhang, Zhengzi Xu, Chengwei Liu, Hongxu Chen, Jianwen Sun, Dong
Qiu, and Yang Liu. 2023. Software architecture recovery with information
fusion. In Proceedings of the 31st ACM Joint European Software Engineering
Conference and Symposium on the Foundations of Software Engineering (ES-
EC/FSE 2023). Association for Computing Machinery, San Francisco, CA, USA,
1535–1547. isbn: 9798400703270. doi:10.1145/3611643.3616285.

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A%20Hybrid%20Approach%20Combining%20Information%20Retrieval%20and%20Large%20Language%20Models%20for%20Traceability%20Link%20Recovery/page-09.png)
