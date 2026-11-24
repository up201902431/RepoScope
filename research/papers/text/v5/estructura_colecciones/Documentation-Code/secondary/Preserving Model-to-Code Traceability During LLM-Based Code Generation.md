# Preserving Model-to-Code Traceability During LLM-Based Code Generation

- source_pdf: ../../../../../pdf/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

Preserving Model-to-Code Traceability During LLM-Based Code
Generation
Marc North
Computer Science
Durham University
Durham, United Kingdom
marc.north@durham.ac.uk
Nelly Bencomo
Computer Science
Durham University
Durham, United Kingdom
nelly.bencomo@durham.ac.uk
Amir Atapour-Abarghouei
Computer Science
Durham University
Durham, United Kingdom
amir.atapour-
abarghouei@durham.ac.uk
Abstract
Large language models (LLMs) are increasingly used for model-
to-code generation, but they weaken one of the central properties
of model-driven engineering: traceability between design models
and generated implementation artefacts. Existing approaches ei-
ther rely on deterministic transformations, where trace links can
be produced by construction, or treat traceability as a post-hoc
recovery problem, where links are reconstructed after code has al-
ready been generated. This paper investigates a different possibility:
preserving model-to-code traceability during LLM-based code gen-
eration. We study generation from UML class diagrams, represented
in XMI, to Java and Python code. During generation, we capture
token-level attribution between the model input and generated
code output, and aggregate these signals into trace links between
model elements and code features. We evaluate input masking,
gradient-based attribution, and internal intervention techniques as
mechanisms for preserving traceability during generation. Across
open-weight LLMs of different sizes, value zeroing performs best,
identifying the correct trace link with 90% top-1 accuracy and more
than 95% top-5 accuracy. The results suggest that generating LLMs
contain signals that can support meaningful model-to-code trace-
ability, without requiring trace links to be reconstructed only after
generation. This paper therefore reframes LLM-based model-to-
code generation as a traceability-preservation problem. This opens
a research direction for AI-supported MDE in which trace links
are treated as engineering artefacts produced alongside generated
code, rather than as evidence recovered afterwards.
ACM Reference Format:
Marc North, Nelly Bencomo, and Amir Atapour-Abarghouei. 2026. Pre-
serving Model-to-Code Traceability During LLM-Based Code Generation.
In ACM/IEEE 29th International Conference on Model Driven Engineering
Languages and Systems (MODELS 2026), October 04–09, 2026, Málaga, Spain.
ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3822455.3838762
1
Introduction
Traceability is central to model-driven engineering (MDE), where
transformations create implementation artefacts from higher-level
models. Trace links relate artefacts across abstraction levels, such
This work is licensed under a Creative Commons Attribution 4.0 International License.
MODELS 2026, Málaga, Spain
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2809-9/26/10
https://doi.org/10.1145/3822455.3838762
as UML classes to generated source-code classes, supporting under-
standing, impact analysis, consistency maintenance, and validation
[9]. Without them, engineers lose evidence of how generated arte-
facts relate to their originating models and requirements.
In this paper, we investigate whether model-to-code traceability
can be preserved during LLM-based code generation. To do so, we
exploit attribution signals from the generating Large Lan-
guage Model (LLM) itself, using AI explainability techniques
to preserve trace links as code is produced.
Despite the value of trace links, maintaining them as projects
grow and requirements change is difficult. Manual traceability
is costly, time-consuming, and error-prone, especially when arte-
facts evolve independently, span different domains, or are main-
tained using different tools [27]. Traditional MDE partly addresses
this through deterministic model-to-code transformations, where
known transformation rules allow trace links to be generated or
reconstructed as part of the engineering workflow. However, this
approach is not possible with LLM-based code generation. Develop-
ers increasingly use LLMs to generate code from prompts, design
descriptions, examples, and structured models, but LLMs do not
provide explicit trace links between generated code and the input
artefacts that influenced it. This risks widening the traceability gap
that MDE has traditionally sought to control.
Existing work largely treats traceability as a post-hoc recovery
problem. In contrast, our approach preserves trace links during
generation by exploiting attribution signals within the generating
LLM itself. This shifts the focus from recovering traceability after
generation to preserving it as an integral part of the generation
process.
1.1
Contributions
This paper makes the following contributions:
(1) We frame LLM-based model-to-code generation as a
traceability-preservation problem, arguing that traceability
should be preserved during generation rather than recovered
post hoc, as in existing LLM-based traceability approaches.
(2) We introduce an aggregation pipeline that transforms raw at-
tribution signals into meaningful trace links between model
elements and generated code features.
(3) We evaluate multiple attribution mechanisms for preserving
traceability across open-weight LLMs, analysing both overall
accuracy and the effect of model size and code feature type.
(4) We release our ground-truth dataset, evaluation framework,
and implementation to support reproducibility and future
358

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

MODELS 2026, October 04–09, 2026, Málaga, Spain
Marc North, Nelly Bencomo, and Amir Atapour-Abarghouei
research on preserving model-to-code traceability during
LLM-based code generation 1.
Two long-standing goals of model-driven engineering are (i)
generating implementations from higher-level abstractions and (ii)
preserving traceability across those abstractions. LLMs represent
an important new mechanism for achieving the first goal, but they
currently undermine the second because their generation process
does not expose explicit relationships between input models and
generated code. Our results suggests that these two goals may be
reconcilable. If traceability can be preserved during generation,
AI-assisted model transformations can retain one of the defining
engineering properties of model-driven development.
2
Background and Related Work
2.1
LLM Explainability for Traceability
Preservation
The rapid adoption of LLMs has begun to reshape software en-
gineering practice, with AI systems increasingly integrated into
everyday development workflows, with Anthropic, for example,
stating that 80% of their code is now written by AI [4]. While the
effect of AI on developer productivity is still unclear [6], AI has
undeniably had a wide-reaching impact on software engineering,
including testing [37], code generation [18], and documentation
[34]. Within Model-Driven Engineering (MDE), recent work has
seen AI applied to model generation [40], using Domain-Specific
Languages [26], and LLMs being used to facilitate dialogue between
domain experts and engineers during model development [33].
In spite of these recent advances and diverse uses of LLMs in
software engineering, explaining why LLMs give the outputs they
do remains an open challenge. LLMs’ own explanations for their
outputs can be misleading [36] or missing [14], making it unclear
whether the LLM’s output has been shaped by some feature in the
input, its training data, or a hallucination.
Various techniques exist for explaining LLM behaviour, includ-
ing attribution methods, post-hoc rationales, and natural-language
explanations, but these explanations can themselves be incomplete
or misleading [1]. Chain-of-thought prompting is often presented
as a route to interpretability, yet chain-of-thought has been found
not to be equivalent to explainability [39]; the reasoning text pro-
duced by an LLM is still an output of the LLM and does not always
adequately correlate with or explain that output. Moreover, recent
work has shown that the ‘thoughts’ generated by reasoning models
do not always match the factors that determine their final outputs
[11], and that explicit reasoning is not always beneficial for model
performance [32].
LLM explainability is an active area of research; since training-
data memorisation [38] and hallucinations [19] are still major issues
for LLMs, being able to reliably attribute an LLM’s output to spe-
cific inputs is important for reliability and user trust. Research has
explored attributing LLM responses to specific artefacts in their
training data [28] or input context via calculating gradients [3], per-
turbing the input [21], or examining the LLM’s internal state, for
example by examining the residual stream [12], or editing attention-
head weights during generation [25]. While most explainability
1https://github.com/marcnorth/attribution-traceability
research aims to improve the transparency or trustworthiness of
LLMs, this paper instead investigates whether attribution signals
can be exploited to preserve engineering traceability during AI-
assisted model transformations.
2.2
Traceability
Traceability in model-driven engineering is the process of identi-
fying, recording, and linking relationships between the artifacts
produced during software or system development [16]. A traceabil-
ity link explains how one artifact relates to another, such as which
requirement is fulfilled by a model element, which model element
generated a piece of code, or which test validates a particular re-
quirement. Modern approaches to traceability address semantically
meaningful trace links, traceability-aware model transformations,
and, more recently, AI-assisted trace recovery and explanation [22].
Traceability helps engineers understand the origin, purpose, and
impact of each model artefact. However, despite the theoretical
benefits, traceability in practice is a challenge, with manual main-
tenance of tracing often being very time-consuming or infeasible
[31]. While work has been done to automatically propagate changes
across different models and different tools [30], this remains a chal-
lenge. These difficulties are not only theoretical. Research into soft-
ware modelling in open-source projects has found that although the
use of UML model diagrams in these projects has grown, model evo-
lution and maintenance rarely aligns with changing requirements
and code [27].
Attempting to address this, recent work has explored the use of
LLMs to recover trace links between development artefacts. Rather
than relying only on manually defined rules or traditional informa-
tion retrieval techniques, LLM-based approaches use their language
and code understanding capabilities to identify semantic relation-
ships between artefacts and infer trace links between them [13].
One family of AI-based approaches to traceability uses prompt
engineering to guide an LLM towards identifying relevant trace
links. This has been applied in work on recovering links between
security requirements and goal models, where the LLM is used di-
rectly as the mechanism for assessing whether artefacts are related
[17]. Other approaches use LLMs together with similarity-based or
retrieval-based techniques. Vector-based similarity methods rep-
resent artefacts as embeddings (vectors in the LLM’s latent vector
space) and compare them in a shared semantic space, allowing
candidate trace links to be identified even when the artefacts use
different wording or domain language [8]. Related work also com-
bines LLMs with knowledge graphs, where structured relationships
between artefacts are used alongside retrieved contextual informa-
tion to support link recovery [2].
A further line of work focuses on improving the interpretability
of LLM-based trace recovery. Some approaches train separate mod-
els to learn input masks, identifying which parts of an input are
most influential for the model’s output [5]. Others use prompt attri-
bution or counterfactual methods to examine how changes to the
input affect the generated response, helping to assess whether the
model’s decision is based on relevant evidence [10] [20]. In trace-
ability recovery, these techniques can support more transparent
link generation by showing which artefact fragments contributed
359

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

Preserving Model-to-Code Traceability During LLM-Based Code Generation
MODELS 2026, October 04–09, 2026, Málaga, Spain
to a proposed trace link and by helping users judge the reliability
of the AI-generated result.
These existing approaches recover trace links after code has been
generated. In contrast, our work investigates whether traceability
can be preserved during AI-assisted model transformations by ex-
ploiting attribution signals from the generating LLM itself. Rather
than reconstructing traceability as a separate activity, our goal is
to preserve traceability alongside the generated implementation.
3
Methods
Our objective is to preserve model-to-code traceability during AI-
assisted model transformations. To achieve this, we investigate
whether attribution signals produced by the generating LLM can be
transformed into meaningful trace links between model elements
and generated code. We evaluate several AI explainability tech-
niques as alternative mechanisms for preserving traceability and
compare their ability to preserve traceability against a determinis-
tically generated ground truth.
Our dataset consists of 128 XML class models from different
domains. From these models, we use a custom deterministic code
generator to produce Python and Java classes, together with de-
terministic traceability maps linking each generated code feature
to the model element from which it was generated. These maps
contain 3,707 trace links and serve as the ground truth for our ex-
periments. We then use teacher-forcing generation [7] to compare
each trace-preservation strategy against this ground truth: rather
than sampling or greedily generating code, we evaluate attribution
scores at the ground-truth output tokens.
We evaluate five attribution mechanisms for preserving trace-
ability between model elements and generated code. Given an LLM
input of 𝑚tokens and output code of 𝑛tokens, each explainability
technique outputs an 𝑚× 𝑛matrix representing the trace scores of
each input token for each output token. I.e., for each input-output
token pair we first capture how important that input token is in the
generation of that output token. The five explainability techniques
to evaluate are:
(1) Individual Token Masking: We run multiple forward
passes through the LLM, masking a different input token on
each forward pass to explore how the LLM’s output changes
when it can no longer ‘see’ each part of the input UML model.
We measure the difference in logit value at each output token
position when the LLM can and can’t see each input token.
This give the trace score for that input-output pair. Causal
LLMs don’t have a dedicated [MASK] token like masked-
language-trained models like BERT, and so we tried different
masking values, such as 0-vector and dedicated [PAD] tokens,
but these replacements gave unstable outputs. Instead, we
mask an input token at the embedding level by replacing its
actual embedding with the average of the LLM’s embedding
matrix.
(2) XML Element Masking: Similar to individual token mask-
ing, however instead of masking individual tokens one at
a time, we mask whole XML element tags. As above, we
measure the difference in logit value at each output token
position when the LLM can and can’t see each XML tag. Note
that we only mask the tokens in the XML element opening
tag; the LLM can still see the tags child elements. Tokens
that are not part of an XML tag are masked individually.
(3) Gradients × Embedding: For each output token position,
we calculate the gradient of the logit of the target output
token with respect to each input token embedding dimension
and multiply this by the input token’s embedding [3]. We
then calculate the 𝐿2-norms across the embedding dimension
to give us a trace score for each output-input token pair.
(4) Integrated Gradients: We calculate integrated gradients to
measure the contribution of each input token to each target
output token. Unlike the previous gradient-based method,
which uses only the local gradient evaluated at the actual in-
put embedding, integrated gradients accumulates gradients
along a path from a baseline input to the actual input [35];
we use the embedding of each LLM’s tokenizer’s unknown
token, or its padding token where no unknown token is de-
fined by the tokenizer. As with Gradients × Embedding, we
calculate the 𝐿2-norm of each attribution vector to obtain a
scalar trace score for each output-input token pair.
(5) Value Zeroing: Like token masking, Value Zeroing [25] also
aims to ‘hide’ parts of the input from the LLM. We set the
value vector of every attention head of every layer in the
LLM at the source token position to zero, thus preventing the
LLM from moving any information from the token position
to other token positions. Measuring the difference in output
token logit gives us the source token’s trace score for each
output token. We do this for each token in the input to give
us trace scores for each input-output token pair.
3.1
From Token Attribution to Model-to-Code
Trace Links
The attribution mechanisms described above produce fine-grained
attribution signals at different levels of granularity, including token-
to-token, embedding-dimension-to-token, and per-layer residual-
stream positions. However, engineering traceability is defined be-
tween meaningful model elements and generated code features
rather than individual tokens. Our aggregation pipeline bridges
this gap by transforming raw attribution signals into meaningful
model-to-code trace links.
3.1.1
Resolving Prior Output Token Attribution. All of the tracing
methods described above operate autoregressively; when comput-
ing the attribution of output token𝑦𝑗, the visible context consists of
both the 𝑚input tokens x = (𝑥1, . . . ,𝑥𝑚) and the 𝑗−1 prior output
tokens (𝑦1, . . . ,𝑦𝑗−1). Consequently, after embedding-dimension
reduction, the trace scores matrix 𝐴∈R𝑛×(𝑚+𝑛−1) assigns scores
to prior output tokens as well as to input tokens.
We are tracing input features to output features, we don’t want
to attribute later output tokens to earlier output tokens. However,
in reality some output tokens will strongly influence later output
tokens. However, simply slicing the trace scores to remove prior
output token attributions would lose potentially meaningful infor-
mation, and so we resolve these trace scores by redistributing the
credit that each output token assigns to earlier output tokens as
follows:
(1) Apply a causal mask to give masked trace-score matrix ˜𝐴by
setting the trace scores of every subsequent output token to
−∞.
360

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

MODELS 2026, October 04–09, 2026, Málaga, Spain
Marc North, Nelly Bencomo, and Amir Atapour-Abarghouei
(2) Calculate the attribution weight matrix 𝑊by normalising
each row of ˜𝐴with a softmax function to obtain a probability
distribution over the visible context (𝑥0, . . . 𝑥𝑚,𝑦0, . . .𝑦𝑗−1)
for each output token. Each row then tells us what fraction
of output token 𝑦𝑗’s total attribution it assigns to each prior
token.
(3) Initialise the resolved input-only attribution matrix 𝑆∈
R𝑛×𝑚by slicing the initial attribution matrix 𝐴.
(4) For each prior output token 𝑦𝑘in chronological order 𝑘=
1, . . . ,𝑛−1, distribute its resolved input attribution to all
subsequent output tokens weighted by how strongly those
tokens attribute to 𝑦𝑘:
𝑆𝑗←𝑆𝑗+ 𝑊𝑗,𝑚+𝑘· 𝑆𝑘,
for all 𝑗> 𝑘.
For example, if output token 𝑦2 attributes 20% of its score to
prior output token 𝑦0 and 30% to 𝑦1, its resolved score will
become 𝑆2 = 0.2𝑆0 + 0.3𝑆1 + 0.5𝑆′
2, where 𝑆′
2 is 𝑦2’s initial
input-token-only attribution scores.
Note that this iterative resolving means that multi-hop attribu-
tion is resolved correctly. A three-token attribution chain 𝑦𝑗→
𝑦𝑘→𝑦𝑘′ with 𝑘′ < 𝑘< 𝑗, for example, is resolved because 𝑆𝑘has
already absorbed the 𝑦𝑘′ contribution before it is used to update 𝑆𝑗.
3.1.2
Feature Grouping and XML Aggregation. The resolved scores
assign an attribution to every individual input token, but our unit
of ground truth is the XMI element, and the unit we wish to predict
is a span of generated code rather than a single output token. We
therefore reduce the token-level scores in two steps: we group
output tokens into output features aligned with the ground truth,
and we aggregate input-token scores onto the candidate source
elements they belong to. Let 𝑆∈R𝑛×𝑚denote the resolved input-
token attribution scores from the previous step.
(1) Output-feature grouping. The ground-truth trace parti-
tions the generated code into contiguous spans, each mapped
to a single XMI element. We assign each output token 𝑦𝑗to
the span it falls within, so that the tokens belonging to one
span are merged into a single output feature, and take the
element-wise maximum over the group as the features trace
score. This yields 𝐹≤𝑛output features and feature trace
scores 𝑆′ ∈R𝐹×𝑚.
(2) Input aggregation onto source elements. The input is the
XMI model serialised as XML; the candidate source elements
are its opening tags 𝑒1, . . . ,𝑒𝐸, each spanning a contiguous
range of input tokens𝑇𝑒. For each output feature 𝑓we reduce
the per-token scores over each element to a single relative-
average score. We first average over the element’s tokens and
then make this relative by subtracting the mean attribution
that element receives from all other output features,
˜𝑎𝑓,𝑒=
1
|𝑇𝑒|
∑︁
𝑖∈𝑇𝑒
𝑆′
𝑓,𝑒−
1
𝐹−1
∑︁
𝑓′≠𝑓
𝑎𝑓′,𝑒.
The relative step controls for elements that are broadly salient to
every output feature. For example, masking beginning-of-sequence
or chat-template tokens has a large impact on all output logits, since
it breaks the input structure that the LLM was trained on. Attribut-
ing every code feature to these tokens would be meaningless, and
so we calculate relative trace scores to answer the question “how
Figure 1: Trace strategy comparison: top-1 attribution
accuracy per tracing strategy, by LLM. Each strategy shows
one point per LLM, with 95% bootstrap confidence intervals.
Value zeroing is the strongest and by far the most consistent
strategy, achieving the highest accuracy for every LLM.
much more influential was each input feature to a code feature than
it was to every other code feature?”
This gives us the final trace scores from which we compute
accuracy and mean reciprocal rank.
4
Results and Discussion
We evaluate five attribution-based mechanisms for preserving
model-to-code traceability in Python and Java across four LLMs:
CodeLlama-7b [23], Phi-4-mini [24], Gemma-3-4b-it [15], and
Qwen2-0.5B [29]. Each predicted trace link is compared against the
ground-truth XMI trace using top-1 and top-5 accuracy, mean rank,
and mean reciprocal rank (MRR). We find that value zeroing is the
most effective mechanism for preserving traceability, remaining re-
liable across all evaluated LLMs, while return types are consistently
the hardest features to trace and class attributes the easiest.
4.1
Comparison of Attribution Techniques
Figure 1 shows the top-1 accuracy of each tracing strategy for each
LLM. Value zeroing was the most accurate mechanism for preserv-
ing traceability during generation, achieving approximately 90%
top-1 accuracy and more than 95% top-5 accuracy. When consid-
ering only the Python code outputs, this rises to approximately
97% top-1 accuracy and 100% top-5 accuracy. Value zeroing out-
performed the other tracing techniques across all LLMs and all
evaluated metrics: top-1 accuracy, top-5 accuracy, mean rank, and
mean reciprocal rank (MRR).
Value zeroing is a more disruptive intervention than the token-
masking approaches, as it masks all movement from the target
token position in every layer of the LLM, not just the embed-
dings. Any activation path, therefore, that uses the zeroed token
position as an intermediate, before using it as input in later lay-
ers, will also be disrupted. This perhaps also explains its superior
traceability-preservation performance, especially for larger LLMs
(see Section 4.2).
Of the two masking-based strategies, individual token masks
outperformed XML element masking. This is perhaps surprising, as
it might be expected that element masking’s knowledge of the input
structure would give it an advantage over simple individual-token
masking. It is possible that masking full XML element tags disrupts
361

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

Preserving Model-to-Code Traceability During LLM-Based Code Generation
MODELS 2026, October 04–09, 2026, Málaga, Spain
Figure 2: Tracing accuracy by LLM size. Points are the mean
over those all input models and shaded bands are 95%
bootstrap confidence intervals over input models.
the input structure too much, leading the models’ understanding of
its input to collapse; future work could test this by replacing target
XML elements with valid XML counterfactuals instead of masking
embeddings. It should be noted that, since it runs fewer masked
forward passes, XML element masking is faster than individual
token masking, and so may still be a more practical choice.
For the gradient-based techniques, integrated gradients performs
on average slightly better than input × gradient, though this is not
consistent across all LLMs. Integrated gradients has a much larger
computation cost than input × gradient for only slightly improved
performance, which must also be considered for future practical
use. For some tracing techniques, there is significant variation in
performance for different LLMs and on different code features, these
are discussed below.
4.2
Performance Across LLMs
Broadly, the performance of traceability-preservation mecha-
nisms correlates negatively with LLM size, as shown in Figure 2.
That is, most traceability-preservation mechanisms perform worse
on larger LLMs. It is, however, important to note that our results do
not give a clean comparison between LLM sizes, as the evaluated
LLMs are from different model families and it is possible that any
differences we find are a result of LLM architecture rather than
number of parameters.
The exception to the general trend is value zeroing, which main-
tains high performance across all LLM sizes. There is a plausible
explanation for why this might be. For the masking-based tech-
niques, we mask only after the embedding layer, before the first
transformer block. The distance between our intervention and the
output we are measuring therefore grows as the number of LLM
layers increases; the LLMs have more components to compensate
for the masked input, lowering the impact of the masking. Similarly
for the gradient-based approaches, as LLM size grows the distance
between the output and the variables we are differentiating with
respect to (the embedding dimensions) grows; it is reasonable to ex-
pect this signal to weaken as LLM size increases. Value zeroing, on
the other hand, is an intervention that applies at every LLM
Figure 3: Tracing difficulty by UML feature type, per
strategy (top-1). For each strategy, top-1 attribution accuracy
is shown for the five feature types, with 95% bootstrap
confidence intervals. The ordering is consistent across all
strategies: attributes, parameters, and operations are traced
most reliably, the class declaration is harder, and return
types are by far the hardest.
layer. Its effect therefore scales with LLM size and it does not suffer
from the same long-distance problem that the other techniques do.
4.3
Performance by Traceability Link Type
Figure 3 shows the performance of each trace strategy on different
model feature classes. As can be seen, class attributes are the easiest
features to trace — value zeroing correctly links 100% of them —
while return types are the most difficult. Return types are not just
the most difficult to trace on average, they are consistently the most
difficult feature type to trace for every tracing strategy. This result
is confirmed by mean rank and MRR metrics as well.
There is a mechanistic reason why return types are the most
difficult feature class to trace: they are often non-distinctive tokens.
60.3% of return spans in our dataset are non-unique within their
class, versus 12% for parameters and less than 3% for attributes,
operations, and classes.
5
Threats to Validity
There are a number of potential factors we must consider when
discussing the validity, reliability, and generalisability of our results:
5.1
Construction Validity
• Ground-truth trace links may be an imperfect proxy for
meaningful traceability that our deterministic generators
don’t capture.
• Since the inputs are structured XML, masking tokens poten-
tially breaks the input structure, and any change in output
may therefore reflect sensitivity to malformed input rather
than meaningful trace links.
• In our experiment, attribution was calculated while the LLMs
were conditioned on reference output, which may not reflect
real-world usage attribution.
5.2
Internal Validity
• Our LLM size comparison does not account for architecture
differences between the LLMs.
• The different LLMs used have different tokenizers, which in
some cases tokenize input slightly differently. While this does
362

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

MODELS 2026, October 04–09, 2026, Málaga, Spain
Marc North, Nelly Bencomo, and Amir Atapour-Abarghouei
reflect how each LLM works, it means that how we aggregate
tokens into meaningful trace features varies slightly between
LLMs, potentially affecting results.
• Results may depend on specific input formatting we used,
such as prompting template, XMI serialization, or output
coding styles.
5.3
External Validity
• In terms of generalisability and applicability to practical de-
velopment environments, real projects involve larger models,
more relationships and more generated files.
• We focus on open-weight models; our results may not gen-
eralise to closed-source models or other LLM architectures.
6
Future Work
The results presented in this paper suggest that attribution signals
from the generating LLM can provide a useful basis for preserv-
ing traceability during model-to-code generation. Our evaluation
deliberately uses a controlled setting: UML class diagrams are rep-
resented in structured XMI, reference code is produced through
deterministic generation, and teacher forcing aligns the LLM with
that reference output. These design choices provide reliable ground
truth for evaluating traceability preservation. The next stage of
this research is therefore to move beyond controlled evaluation
and explore how traceability preservation can support AI-assisted
model transformations in realistic software engineering workflows.
6.1
Beyond Controlled Evaluation
A natural next step is to evaluate traceability preservation during
free code generation. Teacher forcing enables rigorous comparison
against deterministic ground truth, but practical development re-
quires models to generate code autonomously. Future work should
therefore investigate whether attribution-based trace links remain
reliable under realistic decoding strategies, different prompting
styles, and repeated generations from the same input.
Evaluation will also need to extend beyond deterministic trace-
ability maps. Expert software engineers and modelling practition-
ers could assess whether inferred trace links are meaningful and
useful during development, potentially supported by AI-assisted
evaluation methods [41]. Richer modelling artefacts, including be-
havioural models, requirements, and natural-language specifica-
tions, should also be considered alongside larger systems and ad-
ditional programming languages to evaluate how well traceability
preservation generalises beyond the controlled setting explored in
this paper.
6.2
Traceability-Aware AI-Assisted Model
Transformations
Preserving traceability during generation opens possibilities be-
yond recovering links after software has already been produced.
Future development environments could preserve traceability as
a first-class engineering artefact throughout AI-assisted software
development, allowing engineers to navigate directly between re-
quirements, models, generated implementations, tests, and other
software artefacts.
Such capabilities could support impact analysis, change propa-
gation, model evolution, debugging, validation, and maintenance
within AI-assisted development environments. Rather than requir-
ing separate trace-recovery tools after generation, traceability could
become an integral part of AI-assisted model transformations them-
selves.
6.3
Faithful Traceability
An equally important research direction concerns the faithfulness
of attribution-based traceability. While this paper demonstrates
that attribution signals can preserve meaningful trace links, an
important open question is when these signals faithfully represent
the generation process itself.
Future work should therefore investigate alternative attribution
mechanisms, aggregation strategies, perturbation methods, and
counterfactual inputs to better understand when attribution reflects
genuine causal influence rather than model priors or artefacts of
the attribution technique. Understanding failure cases, including
boilerplate code, language-specific syntax, and code generated from
multiple interacting model elements, will be equally important for
improving both the reliability and interpretability of preserved
trace links.
Overall, we believe this work points towards a new generation
of AI-assisted model-driven engineering environments in which
traceability is preserved as software is generated rather than re-
constructed afterwards. If successful, this would allow traceability
to remain a first-class engineering artefact throughout AI-assisted
software engineering.
7
Conclusions
Model-driven engineering has long emphasised structure, explicit
relationships between artefacts, and traceability from design deci-
sions to implementation. LLM-based code generation, by contrast,
is often opaque and unstructured: code is produced from a prompt,
but the relationship between the generated implementation and
the input artefacts is lost. The aim of this work has been to begin
bridging that gap by using AI explainability to bring the trace-
ability discipline of MDE into LLM-based code generation. Our
results provide encouraging evidence for this approach. The best-
performing tracing technique, value zeroing, identified the correct
input element with 90% top-1 accuracy and more than 95% top-5
accuracy.
These findings support the central claim of this paper. Rather
than treating traceability as something to recover after AI-assisted
model transformations, our results suggest that it can instead be
preserved during generation. In this way, attribution-based trace-
ability offers a path towards combining the flexibility and speed
of LLM code generation with the structure, accountability, and
engineering discipline of model-driven engineering.
References
[1] Rohan Ajwani, Shashidhar Reddy Javaji, Frank Rudzicz, and Zining Zhu.
2024.
LLM-Generated Black-box Explanations Can Be Adversarially Help-
ful. arXiv:2405.06800 (Oct. 2024).
https://doi.org/10.48550/arXiv.2405.06800
arXiv:2405.06800 [cs.CL].
[2] Syed Juned Ali, Varun Naganathan, and Dominik Bork. 2025.
Establishing
Traceability Between Natural Language Requirements and Software Artifacts
by Combining RAG and LLMs. In Conceptual Modeling, Wolfgang Maass, Hyoil
Han, Hasan Yasar, and Nick Multari (Eds.). Springer Nature Switzerland, Cham,
295–314. https://doi.org/10.1007/978-3-031-75872-0_16
363

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

Preserving Model-to-Code Traceability During LLM-Based Code Generation
MODELS 2026, October 04–09, 2026, Málaga, Spain
[3] Marco Ancona, Enea Ceolini, Cengiz Öztireli, and Markus Gross. 2017. Towards
better understanding of gradient-based attribution methods for Deep Neural
Networks. https://arxiv.org/abs/1711.06104v4
[4] Anthropic. [n. d.]. When AI builds itself. https://www.anthropic.com/institute/
recursive-self-improvement
[5] Oren Barkan, Yonatan Toib, Yehonatan Elisha, Jonathan Weill, and Noam Koenig-
stein. 2024. LLM Explainability via Attributive Masking Learning. In Findings
of the Association for Computational Linguistics: EMNLP 2024, Yaser Al-Onaizan,
Mohit Bansal, and Yun-Nung Chen (Eds.). Association for Computational Linguis-
tics, Miami, Florida, USA, 9522–9537. https://doi.org/10.18653/v1/2024.findings-
emnlp.556
[6] Joel Becker, Nate Rush, Tom Cunningham, David Rein, and Khalid Mahamud.
2026. We are Changing our Developer Productivity Experiment Design. METR
Blog (Feb. 2026). https://metr.org/blog/2026-02-24-uplift-update/
[7] Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. 2015.
Scheduled Sampling for Sequence Prediction with Recurrent Neural Net-
works. In Advances in Neural Information Processing Systems, Vol. 28. Cur-
ran Associates, Inc.
https://papers.nips.cc/paper_files/paper/2015/hash/
e995f98d56967d946471af29d7bf99f1-Abstract.html
[8] Maria Bonner, Marc Zeller, Gabor Schulz, and Ana Savu. 2024. LLM-based
Approach to Automatically Establish Traceability between Requirements and
MBSE. INCOSE International Symposium 34, 1 (2024), 2542–2560.
https://doi.
org/10.1002/iis2.13285
[9] Artur Boronat, José Á. Carsí, and Isidro Ramos. 2005. Automatic Support for
Traceability in a Generic Model Management Framework. In Model Driven Archi-
tecture – Foundations and Applications, Alan Hartman and David Kreische (Eds.).
Springer, Berlin, Heidelberg, 316–330. https://doi.org/10.1007/11581741_23
[10] Yurui Chang, Bochuan Cao, Yujia Wang, Jinghui Chen, and Lu Lin. 2025. JoPA:
Explaining Large Language Model’s Generation via Joint Prompt Attribution.
In Proceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Wanxiang Che, Joyce Nabende, Ekaterina
Shutova, and Mohammad Taher Pilehvar (Eds.). Association for Computational
Linguistics, Vienna, Austria, 22106–22122. https://doi.org/10.18653/v1/2025.acl-
long.1074
[11] Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison,
John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad
Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, and Ethan Perez. 2025.
Reasoning Models Don’t Always Say What They Think. https://arxiv.org/abs/
2505.05410v1
[12] Javier Ferrando, Gerard I. Gállego, Ioannis Tsiamas, and Marta R. Costa-jussà.
2023. Explaining How Transformers Use Context to Build Predictions. In Proceed-
ings of the 61st Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki
(Eds.). Association for Computational Linguistics, Toronto, Canada, 5486–5513.
https://doi.org/10.18653/v1/2023.acl-long.301
[13] Dominik Fuchß, Haoyu Liu, Sophie Corallo, Tobias Hey, Jan Keim, Johannes von
Geisau, and Anne Koziolek. 2026. Who’s Who? LLM-assisted Software Trace-
ability with Architecture Entity Recognition. ACM Transactions on Autonomous
and Adaptive Systems (April 2026), 3807453.
https://doi.org/10.1145/3807453
arXiv:2511.02434 [cs.SE].
[14] Tianyu Gao, Howard Yen, Jiatong Yu, and Danqi Chen. 2023. Enabling Large
Language Models to Generate Text with Citations. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing, Houda Bouamor,
Juan Pino, and Kalika Bali (Eds.). Association for Computational Linguistics,
Singapore, 6465–6488. https://doi.org/10.18653/v1/2023.emnlp-main.398
[15] Google. 2026. Hugging face - Gemma 3. https://huggingface.co/google/gemma-
3-4b-it
[16] O.C.Z. Gotel and C.W. Finkelstein. 1994. An analysis of the requirements trace-
ability problem. In Proceedings of IEEE International Conference on Requirements
Engineering. IEEE Comput. Soc. Press, Colorado Springs, CO, USA, 94–101.
https://doi.org/10.1109/ICRE.1994.292398
[17] Jameleddine Hassine. 2024. An LLM-based Approach to Recover Traceability
Links between Security Requirements and Goal Models: 28th International Con-
ference on Evaluation and Assessment in Software Engineering, EASE 2024.
Proceedings of 2024 28th International Conference on Evaluation and Assessment
in Software Engineering, EASE 2024 (2024), 643–651.
https://doi.org/10.1145/
3661167.3661261
[18] Nam Huynh and Beiyu Lin. 2025. Large Language Models for Code Generation: A
Comprehensive Survey of Challenges, Techniques, Evaluation, and Applications.
arXiv:2503.01245 (April 2025). https://doi.org/10.48550/arXiv.2503.01245
[19] Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang. 2025.
Why Language Models Hallucinate. arXiv:2509.04664 (2025). https://doi.org/10.
48550/arXiv.2509.04664 arXiv:2509.04664 [cs.CL].
[20] Sepehr Kamahi and Yadollah Yaghoobzadeh. 2024. Counterfactuals As a Means
for Evaluating Faithfulness of Attribution Methods in Autoregressive Language
Models. In Proceedings of the 7th BlackboxNLP Workshop: Analyzing and Interpret-
ing Neural Networks for NLP. Association for Computational Linguistics, Miami,
Florida, US, 452–468. https://doi.org/10.18653/v1/2024.blackboxnlp-1.28
[21] Jiwei Li, Will Monroe, and Dan Jurafsky. 2017. Understanding Neural Networks
through Representation Erasure. arXiv:1612.08220 (Jan. 2017). https://doi.org/
10.48550/arXiv.1612.08220 arXiv:1612.08220 [cs.CL].
[22] Jinfeng Lin, Yalin Liu, Qingkai Zeng, Meng Jiang, and Jane Cleland-Huang. 2021.
Traceability Transformed: Generating more Accurate Links with Pre-Trained
BERT Models. arXiv:2102.04411 (Feb. 2021). https://doi.org/10.48550/arXiv.2102.
04411 arXiv:2102.04411 [cs.SE].
[23] Meta. 2023. Hugging face - CodeLlama.
https://huggingface.co/codellama/
CodeLlama-7b-hf
[24] Microsoft. 2025. Hugging face - Phi-4. https://huggingface.co/microsoft/Phi-4-
mini-instruct
[25] Hosein Mohebbi, Willem Zuidema, Grzegorz Chrupała, and Afra Alishahi. 2023.
Quantifying Context Mixing in Transformers. In Proceedings of the 17th Confer-
ence of the European Chapter of the Association for Computational Linguistics, An-
dreas Vlachos and Isabelle Augenstein (Eds.). Association for Computational Lin-
guistics, Dubrovnik, Croatia, 3378–3400. https://doi.org/10.18653/v1/2023.eacl-
main.245
[26] Lukas Netz, Judith Michael, and Bernhard Rumpe. [n. d.]. From Natural Language
to Web Applications: Using Large Language Models for Model-Driven Software
Engineering. ([n. d.]).
[27] Zaki Pauzi and Andrea Capiluppi. 2025. Using Concept Traceability to Investigate
UML Class Diagram Evolution in Long-Existing FOSS Projects. 432–438. https:
//doi.org/10.1109/MODELS-C68889.2025.00062
[28] Garima Pruthi, Frederick Liu, Satyen Kale, and Mukund Sundararajan. 2020.
Estimating Training Data Influence by Tracing Gradient Descent. Advances in
Neural Information Processing Systems 33 (2020), 19920–19930.
[29] Qwen. 2026. Hugging face - Qwen 2. https://huggingface.co/Qwen/Qwen2-0.5B
[30] Cosmina-Cristina Raţiu, Wesley K. G. Assunção, Edvin Herac, Rainer Haas,
Christophe Lauwerys, and Alexander Egyed. 2025. Using reactive links to propa-
gate changes across engineering models. Software and Systems Modeling 24, 4
(Aug. 2025), 1213–1239. https://doi.org/10.1007/s10270-024-01186-w
[31] Cosmina Cristina Raţiu, Christoph Mayr-Dorn, Wesley K. G. Assunção, and
Alexander Egyed. 2023. Taming Cross-Tool Traceability in the Wild. In 2023 IEEE
31st International Requirements Engineering Conference (RE). 233–243.
https:
//doi.org/10.1109/RE57278.2023.00031 ISSN: 2332-6441.
[32] Parshin Shojaee, Iman Mirzadeh, Keivan Alizadeh, Maxwell Horton, Samy Ben-
gio, and Mehrdad Farajtabar. [n. d.]. The Illusion of Thinking: Understanding
the Strengths and Limitations of Reasoning Models via the Lens of Problem
Complexity. In Apple Machine Learning Research. https://machinelearning.apple.
com/research/illusion-of-thinking
[33] Jonathan Silva Mercado. 2024. AI Assisted Domain Modeling Explainability and
Traceability. https://doi.org/10.1145/3652620.3688197
[34] Weisong Sun, Yun Miao, Yuekang Li, Hongyu Zhang, Chunrong Fang, Yi Liu,
Gelei Deng, Yang Liu, and Zhenyu Chen. 2025. Source Code Summarization
in the Era of Large Language Models. arXiv:2407.07959 (Aug. 2025).
https:
//doi.org/10.48550/arXiv.2407.07959 arXiv:2407.07959 [cs.SE].
[35] Mukund Sundararajan, Ankur Taly, and Qiqi Yan. 2017. Axiomatic Attribution
for Deep Networks. https://arxiv.org/abs/1703.01365v2
[36] Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. 2023. Lan-
guage Models Don’t Always Say What They Think: Unfaithful Explanations in
Chain-of-Thought Prompting. https://arxiv.org/abs/2305.04388v2
[37] Wenhan Wang, Chenyuan Yang, Zhijie Wang, Yuheng Huang, Zhaoyang Chu,
Da Song, Lingming Zhang, An Ran Chen, and Lei Ma. 2025. TESTEVAL: Bench-
marking Large Language Models for Test Case Generation. arXiv:2406.04531
(Feb. 2025). https://doi.org/10.48550/arXiv.2406.04531 arXiv:2406.04531 [cs.SE].
[38] Alexander Xiong, Xuandong Zhao, Aneesh Pappu, and Dawn Song. 2025. The
Landscape of Memorization in LLMs: Mechanisms, Measurement, and Mitigation.
arXiv:2507.05578 (Dec. 2025). https://doi.org/10.48550/arXiv.2507.05578
[39] Kerem Zaman and Shashank Srivastava. 2025. Is Chain-of-Thought Really Not
Explainability? Chain-of-Thought Can Be Faithful without Hint Verbalization.
https://arxiv.org/abs/2512.23032v2
[40] Weixing Zhang, Jiang Bowen, Fu Yuhong, Cheng Haowei, Maximilian Hummel,
Vincenzo Scotti, Nathan Hagel, Jialong Li, Georg Grossmann, Markus Stumptner,
Regina Hebig, Daniel Strüber, and Anne Koziolek. 2026. Large Language Models
in Model-Driven Engineering: A Systematic Mapping Study. https://doi.org/10.
5281/zenodo.20064398 DOI: 10.5281/zenodo.20064398.
[41] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu,
Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph
Gonzalez, and Ion Stoica. 2023. Judging LLM-as-a-Judge with MT-Bench and
Chatbot Arena. Advances in Neural Information Processing Systems 36 (Dec. 2023),
46595–46623.
364

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Documentation-Code/secondary/Preserving%20Model-to-Code%20Traceability%20During%20LLM-Based%20Code%20Generation/page-07.png)
