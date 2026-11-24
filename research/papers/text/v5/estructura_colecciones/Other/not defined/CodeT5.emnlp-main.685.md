# CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation

- source_pdf: ../../../../../pdf/Other/not%20defined/CodeT5.emnlp-main.685.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 8696–8708
November 7–11, 2021. c⃝2021 Association for Computational Linguistics
8696
CodeT5: Identiﬁer-aware Uniﬁed Pre-trained Encoder-Decoder Models
for Code Understanding and Generation
Yue Wang1, Weishi Wang12, Shaﬁq Joty12, and Steven C.H. Hoi1
1 Salesforce Research Asia
2 Nanyang Technological University, Singapore
{wang.y,weishi.wang,sjoty,shoi}@salesforce.com
Abstract
Pre-trained models for Natural Languages
(NL) like BERT and GPT have been recently
shown to transfer well to Programming Lan-
guages (PL) and largely beneﬁt a broad set of
code-related tasks. Despite their success, most
current methods either rely on an encoder-only
(or decoder-only) pre-training that is subopti-
mal for generation (resp. understanding) tasks
or process the code snippet in the same way
as NL, neglecting the special characteristics of
PL such as token types. We present CodeT5,
a uniﬁed pre-trained encoder-decoder Trans-
former model that better leverages the code se-
mantics conveyed from the developer-assigned
identiﬁers.
Our model employs a uniﬁed
framework to seamlessly support both code un-
derstanding and generation tasks and allows
for multi-task learning. Besides, we propose a
novel identiﬁer-aware pre-training task that en-
ables the model to distinguish which code to-
kens are identiﬁers and to recover them when
they are masked. Furthermore, we propose to
exploit the user-written code comments with a
bimodal dual generation task for better NL-PL
alignment. Comprehensive experiments show
that CodeT5 signiﬁcantly outperforms prior
methods on understanding tasks such as code
defect detection and clone detection, and gen-
eration tasks across various directions includ-
ing PL-NL, NL-PL, and PL-PL. Further analy-
sis reveals that our model can better capture
semantic information from code.
Our code
and pre-trained models are released at https:
//github.com/salesforce/CodeT5.
1
Introduction
Pre-trained language models such as BERT (De-
vlin et al., 2019), GPT (Radford et al., 2019), and
T5 (Raffel et al., 2020) have greatly boosted per-
formance in a wide spectrum of natural language
processing (NLP) tasks. They typically employ
a pre-train then ﬁne-tune paradigm that aims to
derive generic language representations by self-
supervised training on large-scale unlabeled data,
which can be transferred to beneﬁt multiple down-
stream tasks, especially those with limited data an-
notation. Inspired by their success, there are many
recent attempts to adapt these pre-training meth-
ods for programming language (PL) (Svyatkovskiy
et al., 2020; Kanade et al., 2020; Feng et al., 2020),
showing promising results on code-related tasks.
However, despite their success, most of these
models rely on either an encoder-only model simi-
lar to BERT (Svyatkovskiy et al., 2020; Feng et al.,
2020) or a decoder-only model like GPT (Kanade
et al., 2020), which is suboptimal for generation
and understanding tasks, respectively. For exam-
ple, CodeBERT (Feng et al., 2020) requires an
additional decoder when applied for the code sum-
marization task, where this decoder cannot bene-
ﬁt from the pre-training. Besides, most existing
methods simply employ the conventional NLP pre-
training techniques on source code by regarding it
as a sequence of tokens like NL. This largely ig-
nores the rich structural information in code, which
is vital to fully comprehend the code semantics.
In this work, we present CodeT5, a pre-trained
encoder-decoder model that considers the token
type information in code. Our CodeT5 builds on
the T5 architecture (Raffel et al., 2020) that em-
ploys denoising sequence-to-sequence (Seq2Seq)
pre-training and has been shown to beneﬁt both
understanding and generation tasks in natural lan-
guage. In addition, we propose to leverage the
developer-assigned identiﬁers in code. When writ-
ing programs, developers tend to employ informa-
tive identiﬁers to make the code more understand-
able, so that these identiﬁers would generally pre-
serve rich code semantics, e.g., the “binarySearch”
identiﬁer in Figure 2 directly indicates its func-
tionality. To fuse such code-speciﬁc knowledge,
we propose a novel identiﬁer-aware objective that
trains the model to distinguish which tokens are
identiﬁers and recover them when they are masked.
Furthermore, we propose to leverage the code

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

8697
CodeT5
"Summarize Python: def inc_value(x):..."
"Generate Python: increment value"
"Defect: if x=0: x += 1"
"Refine: if x=0: x += 1"
"Translate Python to C: if x==0: x += 1"
"increment value"
"def inc_value(x):..."
"true"
"if x == 0: x += 1"
"if (x==0) {x += 1;}"
Figure 1: Illustration of our CodeT5 for code-related understanding and generation tasks.
and its accompanying comments to learn a better
NL-PL alignment. Developers often provide docu-
mentation for programs to facilitate better software
maintenance (de Souza et al., 2005), so that such
PL-NL pairs are widely available in most source
code. Speciﬁcally, we regard the NL→PL gener-
ation and PL→NL generation as dual tasks and
simultaneously optimize the model on them.
We pre-train CodeT5 on the CodeSearchNet
data (Husain et al., 2019) following (Feng et al.,
2020) that consists of both unimodal (PL-only)
and bimodal (PL-NL) data on six PLs. In addi-
tion to that, we further collect extra data of C/C#
from open-source Github repositories. We ﬁne-
tune CodeT5 on most tasks in the CodeXGLUE
benchmark (Lu et al., 2021), including two under-
standing tasks: code defect detection and clone
detection, and generation tasks such as code sum-
marization, generation, translation, and reﬁnement.
As shown in Figure 1, we also explore multi-task
learning to ﬁne-tune CodeT5 on multiple tasks at a
time using a task control code as the source prompt.
In summary, we make the following contributions:
• We present one of the ﬁrst uniﬁed encoder-
decoder models CodeT5 to support both code-
related understanding and generation tasks,
and also allows for multi-task learning.
• We propose a novel identiﬁer-aware pre-
training objective that considers the crucial
token type information (identiﬁers) from code.
Besides, we propose to leverage the NL-PL
pairs that are naturally available in source
code to learn a better cross-modal alignment.
• Extensive experiments show that CodeT5
yields state-of-the-art results on the fourteen
sub-tasks in CodeXGLUE. Further analysis
shows our CodeT5 can better capture the code
semantics with the proposed identiﬁer-aware
pre-training and bimodal dual generation pri-
marily beneﬁts NL↔PL tasks.
2
Related Work
Pre-training
on
Natural
Language.
Pre-
trained models based on Transformer archi-
tectures (Vaswani et al., 2017) have led to
state-of-the-art performance on a broad set of
NLP tasks. They can be generally categorized
into three groups:
encoder-only models such
as BERT (Devlin et al., 2019), RoBERTa (Liu
et al., 2019b), and ELECTRA (Clark et al., 2020),
decoder-only models like GPT (Radford et al.,
2019), and encoder-decoder models such as
MASS (Song et al., 2019), BART (Lewis et al.,
2020), and T5 (Raffel et al., 2020). Compared
to encoder-only and decoder-only models that
respectively favor understanding and generation
tasks, encoder-decoder models can well support
both types of tasks. They often employ denoising
sequence-to-sequence pre-training objectives that
corrupt the source input and require the decoder
to recover them. In this work, we extend T5 to
the programming language and propose a novel
identiﬁer-aware denoising objective that enables
the model to better comprehend the code.
Pre-training on Programming Language.
Pre-
training on the programming language is a nascent
ﬁeld where much recent work attempts to extend
the NLP pre-training methods to source code. Cu-
BERT (Kanade et al., 2020) and CodeBERT (Feng
et al., 2020) are the two pioneer models. CuBERT
employs BERT’s powerful masked language mod-
eling objective to derive generic code-speciﬁc rep-
resentation, and CodeBERT further adds a replaced
token detection (Clark et al., 2020) task to learn
NL-PL cross-modal representation. Besides the
BERT-style models, Svyatkovskiy et al. (2020) and
Liu et al. (2020) respectively employ GPT and
UniLM (Dong et al., 2019) for the code completion
task. Transcoder (Rozière et al., 2020) explores
programming language translation in an unsuper-
vised setting. Different from them, we explore

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

8698
# recursive binary search
def binarySearch(arr, left, right, x):
mid = (left + right) // 2
if arr[mid] == x:
return mid
...
Bimodal Input
if arr [ mid ] == x : return mid
0
1
0
1
0 0 1 0
0
1
# recursive binary search
def binarySearch(arr, left, right, x):
mid = (left + right) // 2
if arr[mid] == x:
return mid
(d) Bimodal Dual Generation
(b) Identifier Tagging
(c) Masked Identifier Prediction
# recursive binary search
def MASK0(MASK1, MASK2, MASK3, MASK4):
MASK5 = (MASK2 + MASK3) // 2
if MASK1[MASK5] == MASK4:
return MASK5
MASK0 binarySearch MASK1 arr MASK2 
left MASK3 right MASK4 x MASK5 mid
Masked Input
Output
# recursive MASK0
def binarySearch(arr, left, right, x):
mid = (left + MASK1
if arr MASK2 == x:
return mid
MASK0 binary search MASK1 right ) // 2 
MASK2 [ mid ]
Masked Input
Output
(a) Masked Span Prediction
Figure 2: Pre-training tasks of CodeT5. We ﬁrst alternately train span prediction, identiﬁer prediction, and identi-
ﬁer tagging on both unimodal and bimodal data, and then leverage the bimodal data for dual generation training.
encoder-decoder models based on T5 for program-
ming language pre-training and support a more
comprehensive set of tasks.
Some emerging work (Clement et al., 2020; Mas-
tropaolo et al., 2021; Elnaggar et al., 2021) in the
recent literature also explore the T5 framework on
code, but they only focus on a limited subset of
generation tasks and do not support understand-
ing tasks like us. Apart from these, PLBART (Ah-
mad et al., 2021) based on another encoder-decoder
model BART can also support both understanding
and generation tasks. However, all the above prior
work simply processes code in the same way as nat-
ural language and largely ignores the code-speciﬁc
characteristics. Instead, we propose to leverage the
identiﬁer information in code for pre-training.
Recently, GraphCodeBERT (Guo et al., 2021)
incorporates the data ﬂow extracted from the code
structure into CodeBERT, while Rozière et al.
(2021) propose a deobfuscation objective to lever-
age the structural aspect of PL. These models only
focus on training a better code-speciﬁc encoder.
Zügner et al. (2021) proposes to capture the rela-
tive distances between code tokens over the code
structure. By contrast, we speciﬁcally focus on
the identiﬁers that reserve rich code semantics and
fuse such information into a Seq2Seq model via
two novel identiﬁer tagging and prediction tasks.
3
CodeT5
Our CodeT5 builds on an encoder-decoder frame-
work with the same architecture as T5 (Raffel et al.,
2020). It aims to derive generic representations
for programming language (PL) and natural lan-
guage (NL) via pre-training on unlabeled source
code. As illustrated in Figure 2, we extend the de-
noising Seq2Seq objective in T5 by proposing two
identiﬁer tagging and prediction tasks to enable the
model to better leverage the token type informa-
tion from PL, which are the identiﬁers assigned by
developers. To improve the NL-PL alignment, we
further propose a bimodal dual learning objective
for a bidirectional conversion between NL and PL.
In the following, we introduce how CodeT5 en-
codes PL and NL inputs (§3.1) and our proposed
identiﬁer-aware pre-training tasks (§3.2), followed
by the ﬁne-tuning with task-speciﬁc transfer learn-
ing and multi-task training (§3.3).
3.1
Encoding NL and PL
At the pre-training stage, our model would receive
either PL-only or NL-PL as inputs depending on
whether the code snippet has accompanying NL
descriptions or not. For the NL-PL bimodal in-
puts, we concatenate them into a sequence with
a delimiter token [SEP] and represent the whole
input sequence into the format as x = ([CLS],
w1, ..., wn, [SEP], c1, ..., cm, [SEP]), where n
and m denote the number of NL word tokens and
PL code tokens, respectively. The NL word se-
quence will be empty for PL-only unimodal inputs.
In order to capture more code-speciﬁc features,
we propose to leverage token type information from
code. We focus on the type of identiﬁers (e.g., func-
tion names and variables) as they are one of the
most PL-agnostic features and reserve rich code
semantics. Speciﬁcally, we convert the PL segment
into an Abstract Syntax Tree (AST) and extract the
node types for each code token. Finally, we con-
struct a sequence of binary labels y ∈{0, 1}m for
the PL segment, where each yi ∈{0, 1} represents
whether the code token ci is an identiﬁer or not.

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

8699
3.2
Pre-training Tasks
We now introduce our proposed pre-training tasks
that enable CodeT5 to learn useful patterns from
either PL-only or NL-PL bimodal data.
Identiﬁer-aware Denoising Pre-training.
De-
noising Sequence-to-Sequence (Seq2Seq) pre-
training has been shown to be quite effective in
a broad set of NLP tasks (Song et al., 2019; Raf-
fel et al., 2020; Lewis et al., 2020). This denois-
ing objective typically ﬁrst corrupts the source se-
quence with some noising functions and then re-
quires the decoder to recover the original texts. In
this work, we utilize a span masking objective sim-
ilar to T5 (Raffel et al., 2020) that randomly masks
spans with arbitrary lengths and then predicts these
masked spans combined with some sentinel tokens
at the decoder. We refer this task to Masked Span
Prediction (MSP), as illustrated in Figure 2 (a).
Speciﬁcally, we employ the same 15% corrup-
tion rate as T5 and ensure the average span length
to be 3 by uniformly sampling spans of from 1 to
5 tokens. Moreover, we employ the whole word
masking by sampling spans before subword tok-
enization, which aims to avoid masking partial sub-
tokens and is shown to be helpful (Sun et al., 2019).
Notably, we pre-train a shared model for various
PLs to learn robust cross-lingual representations.
We describe the masked span prediction loss as:
LMSP (θ) =
k
X
t=1
−log Pθ(xmask
t
|x\mask, xmask
<t ),
(1)
where θ are the model parameters, x\mask is the
masked input, xmask is the masked sequence to pre-
dict from the decoder with k denoting the number
of tokens in xmask, and xmask
<t
is the span sequence
generated so far.
To fuse more code-speciﬁc structural informa-
tion (the identiﬁer node type in AST) into the
model, we propose two additional tasks: Identi-
ﬁer Tagging (IT) and Masked Identiﬁer Prediction
(MIP) to complement the denoising pre-training. .
• Identiﬁer Tagging (IT)
It aims to notify the
model with the knowledge of whether this code
token is an identiﬁer or not, which shares a similar
spirit of syntax highlighting in some developer-
aided tools. As shown in Figure 2 (b), we map
the ﬁnal hidden states of the PL segment at the
CodeT5 encoder into a sequence of probabilities
p = (p1, ..., pm), and compute a binary cross en-
tropy loss for sequence labeling:
LIT (θe) =
m
X
i=1
−[yi log pi + (1 −yi) log(1 −pi)],
(2)
where θe are the encoder parameters. Note that by
casting the task as a sequence labeling problem, the
model is expected to capture the code syntax and
the data ﬂow structures of the code.
• Masked Identiﬁer Prediction (MIP)
Differ-
ent from the random span masking in MSP, we
mask all identiﬁers in the PL segment and employ
a unique sentinel token for all occurrences of one
speciﬁc identiﬁer. In the ﬁeld of software engi-
neering, this is called obfuscation where changing
identiﬁer names does not impact the code seman-
tics. Inspired by Rozière et al. (2021), we arrange
the unique identiﬁers with the sentinel tokens into
a target sequence I as shown in Figure 2 (c). We
then predict it in an auto-regressive manner:
LMIP (θ) =
|I|
X
j=1
−log Pθ(Ij|x\I, I<j),
(3)
where x\I is the masked input. Note that deobfus-
cation is a more challenging task that requires the
model to comprehend the code semantics based on
obfuscated code and link the occurrences of the
same identiﬁers together.
We alternately optimize these three losses with
an equal probability, which constitutes our pro-
posed identiﬁer-aware denoising pre-training.
Bimodal Dual Generation.
In the pre-training
phase, the decoder only sees discrete masked spans
and identiﬁers, which is disparate from the down-
stream tasks where the decoder needs to gener-
ate either ﬂuent NL texts or syntactically correct
code snippets. To close the gap between the pre-
training and ﬁne-tuning, we propose to leverage
the NL-PL bimodal data to train the model for a
bidirectional conversion as shown in Figure 2 (d).
Speciﬁcally, we regard the NL→PL generation and
PL→NL generation as dual tasks and simultane-
ously optimize the model on them. For each NL-
PL bimodal datapoint, we construct two training
instances with reverse directions and add language
ids (e.g., <java> and <en> for Java PL and En-
glish NL, respectively). This operation can be also
seen as a special case of T5’s span masking by
either masking the full NL or PL segment from
the bimodal inputs. This task aims to improve the
alignment between the NL and PL counterparts.

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

8700
3.3
Fine-tuning CodeT5
After pre-training on large-scale unlabeled data, we
adapt CodeT5 to downstream tasks via either task-
speciﬁc transfer learning or multi-task learning.
Task-speciﬁc Transfer Learning: Generation
vs. Understanding Tasks.
Code-related tasks
can be categorized into generation and understand-
ing tasks. For the former one, our CodeT5 can
be naturally adapted with its Seq2Seq framework.
For understanding tasks, we investigate two ways
of either generating the label as a unigram target
sequence (Raffel et al., 2020), or predicting it from
the vocabulary of class labels based on the last
decoder hidden state following Lewis et al. (2020).
Multi-task Learning.
We also explore a multi-
task learning setting by training a shared model
on multiple tasks at a time. Multi-task learning
is able to reduce computation cost by reusing the
most of model weights for many tasks and has
been shown to improve the model generalization
capability in NL pre-training (Liu et al., 2019a).
We follow Raffel et al. (2020) to employ the same
uniﬁed model for all tasks without adding any task-
speciﬁc networks but allow to select different best
checkpoints for different tasks. To notify the model
with which task it is dealing with, we design a
uniﬁed format of task control codes and prepend
it into the source inputs as shown in Figure 1. For
instance, we employ “Translate Java to CSharp:” as
the source prompt for the code-to-code translation
task from Java to CSharp.
As different tasks have different dataset sizes,
we follow Conneau and Lample (2019) to employ
a balanced sampling strategy. For N number of
datasets (or tasks), with probabilities {qi}N
i=1, we
deﬁne the following multinomial distribution to
sample from:
qi =
rα
i
PN
j=1 rα
j
, where ri =
ni
PN
k=1 nk
,
(4)
where ni is number of examples for i-th task and
α is set to 0.7. This balanced sampling aims to
alleviate the bias towards high-resource tasks.
4
Experimental Setup
4.1
Pre-training Dataset
We follow Feng et al. (2020) to employ Code-
SearchNet (Husain et al., 2019) to pre-train
PLs
W/ NL
W/o NL
Identiﬁer
CodeSearchNet















Ruby
49,009
110,551
32.08%
JavaScript
125,166
1,717,933
19.82%
Go
319,132
379,103
19.32%
Python
453,772
657,030
30.02%
Java
457,381
1,070,271
25.76%
PHP
525,357
398,058
23.44%
Our
 C
1M
-
24.94%
CSharp
228,496
856,375
27.85%
Total
3,158,313
5,189,321
8,347,634
Table 1: Dataset statistics. “Identiﬁer” denotes the pro-
portion of identiﬁers over all code tokens for each PL.
CodeT5, which consists of six PLs with both uni-
modal and bimodal data. Apart from that, we ad-
ditionally collect two datasets of C/CSharp from
BigQuery1 to ensure that all downstream tasks have
overlapped PLs with the pre-training data. In total,
we employ around 8.35 million instances for pre-
training. Table 1 shows some basic statistics. To
obtain the identiﬁer labels from code, we leverage
the tree-sitter2 to convert the PL into an abstract
syntax tree and then extract its node type informa-
tion. We ﬁlter out reserved keywords for each PL
from its identiﬁer list. We observe that PLs have
different identiﬁer rates, where Go has the least
rate of 19% and Ruby has the highest rate of 32%.
4.2
Code-speciﬁc Tokenizer
Tokenization is a key ingredient for the success of
pre-trained language models like BERT and GPT.
They often employ a Byte-Pair Encoding (BPE) to-
kenizer (Sennrich et al., 2016) to alleviate the Out-
of-Vocabulary (OoV) issues. Speciﬁcally, we train
a Byte-level BPE tokenizer following Radford et al.
(2019) and set the vocabulary size to 32,000 as T5.
We add additional special tokens ([PAD], [CLS],
[SEP], [MASK0], ..., [MASK99]). This token-
zier is trained on all of our pre-training data with
non-printable characters and low-frequent tokens
(occurring <3 times) ﬁltered. We compare it with
T5’s default tokenizer and ﬁnd that our tokenizer
largely reduces the length of tokenized code se-
quence by 30% - 45% on downstream tasks. This
will accelerate the training and especially beneﬁt
generation tasks due to the shorter sequence to pre-
dict. We also spot a severe problem for applying
the T5’s default tokenizer on source code, where it
would encode some common code tokens such as
brackets [‘{’, ‘}’] into unknown tokens.
1https://console.cloud.google.com/
marketplace/details/github/github-repos
2https://tree-sitter.github.io/
tree-sitter/

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

8701
Methods
Ruby
JavaScript
Go
Python
Java
PHP
Overall
RoBERTa
11.17
11.90
17.72
18.14
16.47
24.02
16.57
CodeBERT
12.16
14.90
18.07
19.06
17.65
25.16
17.83
DOBF
-
-
-
18.24
19.05
-
-
PLBART
14.11
15.56
18.91
19.30
18.45
23.58
18.32
CodeT5-small
14.87
15.32
19.25
20.04
19.92
25.46
19.14
+dual-gen
15.30
15.61
19.74
19.94
19.78
26.48
19.48
+multi-task
15.50
15.52
19.62
20.10
19.59
25.69
19.37
CodeT5-base
15.24
16.16
19.56
20.01
20.31
26.03
19.55
+dual-gen
15.73
16.00
19.71
20.11
20.41
26.53
19.75
+multi-task
15.69
16.24
19.76
20.36
20.46
26.09
19.77
Table 2: Smoothed BLEU-4 scores on the code summarization task. The “Overall”
column shows the average scores over six PLs. Best results are in bold.
Methods
EM
BLEU
CodeBLEU
GPT-2
17.35
25.37
29.69
CodeGPT-2
18.25
28.69
32.71
CodeGPT-adapted
20.10
32.79
35.98
PLBART
18.75
36.69
38.52
CodeT5-small
21.55
38.13
41.39
+dual-gen
19.95
39.02
42.21
+multi-task
20.15
35.89
38.83
CodeT5-base
22.30
40.73
43.20
+dual-gen
22.70
41.48
44.10
+multi-task
21.15
37.54
40.01
Table 3: Results on the code generation task. EM de-
notes the exact match.
4.3
Downstream Tasks and Metrics
We cover most generation and understanding tasks
in the CodeXGLUE benchmark (Lu et al., 2021)
and employ the provided public datasets and the
same data splits following it for all these tasks.
We ﬁrst consider two cross-modal generation
tasks. Code summarization aims to summarize a
function-level code snippet into English descrip-
tions. The dataset consists of six PLs including
Ruby, JavaScript, Go, Python, Java, and PHP from
CodeSearchNet (Husain et al., 2019). We employ
the smoothed BLEU-4 (Lin and Och, 2004) to eval-
uate this task. Code generation is the task to gen-
erate a code snippet based on NL descriptions. We
employ the Concode data (Iyer et al., 2018) in Java
where the input contains both NL texts and class
environment contexts, and the output is a function.
We evaluate it with BLEU-4, exact match (EM)
accuracy, and CodeBLEU (Ren et al., 2020) that
considers syntactic and semantic matches based on
the code structure in addition to the n-gram match.
Besides, we consider two code-to-code gener-
ation tasks.
Code translation aims to migrate
legacy software from one PL to another, where we
focus on translating functions from Java to CSharp
and vice versa. Code reﬁnement aims to convert
a buggy function into a correct one. We employ
two Java datasets provided by Tufano et al. (2019)
with various function lengths: small (fewer than
50 tokens) and medium (50-100 tokens). We use
BLEU-4 and exact match to evaluate them.
We also investigate how CodeT5 performs on
two understanding-based tasks. The ﬁrst one is
defect detection that aims to predict whether a
code is vulnerable to software systems or not. We
use the C dataset provided by Zhou et al. (2019)
for experiment. The second task is clone detection
which aims to measure the similarity between two
code snippets and predict whether they have the
same functionality. We experiment with the Java
data provided by Wang et al. (2020). We employ
F1 score and accuracy for evaluating these two
tasks respectively. In total, our CodeT5 supports
six tasks and fourteen sub-tasks in CodeXGLUE
with a uniﬁed encoder-decoder model.
4.4
Comparison Models
We compare CodeT5 with state-of-the-art (SOTA)
pre-trained models that can be categorized into
three types:
encoder-only, decoder-only, and
encoder-decoder models. As encoder-only mod-
els, we consider RoBERTa (Liu et al., 2019b),
RoBERTa (code) trained with masked language
modeling (MLM) on code, CodeBERT (Feng et al.,
2020) trained with both MLM and replaced to-
ken detection (Clark et al., 2020), GraphCode-
BERT (Guo et al., 2021) using data ﬂow from code,
and DOBF (Rozière et al., 2021) trained with the
identiﬁer deobfuscation objective. Note that al-
though DOBF employs a Seq2Seq model during
pre-training, it only aims to train a better encoder
for downstream tasks without exploring the poten-
tial beneﬁt of the pre-trained decoder.
For decoder-only models, we compare GPT-
2 (Radford et al., 2019) and its adaptations on
code domain including CodeGPT-2, and CodeGPT-
adapted. The difference is that the latter one uti-
lizes a GPT-2 checkpoint for model initialization
while the former one is trained from scratch. As
encoder-decoder models, the current SOTA model
for the CodeXGLUE benchmark is PLBART (Ah-
mad et al., 2021) based on BART (Lewis et al.,
2020) architecture. For pre-training data, most of
these models employ CodeSearchNet (Husain et al.,
2019) except DOBF and PLBART. DOBF is pre-
trained on 7.9M Java and 3.6M Python ﬁles from
BigQuery while PLBART employs a much larger
data with 470M Python and 210M Java functions,
and 47M NL posts from StackOverﬂow.

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

8702
Methods
Java to C#
C# to Java
Reﬁne Small
Reﬁne Medium
BLEU
EM
BLEU
EM
BLEU
EM
BLEU
EM
Naive Copy
18.54
0
18.69
0
78.06
0
90.91
0
RoBERTa (code)
77.46
56.10
71.99
57.90
77.30
15.90
90.07
4.10
CodeBERT
79.92
59.00
72.14
58.80
77.42
16.40
91.07
5.20
GraphCodeBERT
80.58
59.40
72.64
58.80
80.02
17.30
91.31
9.10
PLBART
83.02
64.60
78.35
65.00
77.02
19.21
88.50
8.98
CodeT5-small
82.98
64.10
79.10
65.60
76.23
19.06
89.20
10.92
+dual-gen
82.24
63.20
78.10
63.40
77.03
17.50
88.99
10.28
+multi-task
83.49
64.30
78.56
65.40
77.03
20.94
87.51
11.11
CodeT5-base
84.03
65.90
79.87
66.90
77.43
21.61
87.64
13.96
+dual-gen
81.84
62.00
77.83
63.20
77.66
19.43
90.43
11.69
+multi-task
82.31
63.40
78.01
64.00
78.06
22.59
88.90
14.18
Table 4: BLEU-4 scores and exact match (EM) accuracies for code translation (Java to
C# and C# to Java) and code reﬁnement (small and medium) tasks.
Methods
Defect
Clone
Accuracy
F1
RoBERTa
61.05
94.9
CodeBERT
62.08
96.5
DOBF
-
96.5
GraphCodeBERT
-
97.1
PLBART
63.18
97.2
CodeT5-small
63.40
97.1
+dual-gen
63.47
97.0
+multi-task
63.58
-
CodeT5-base
65.78
97.2
+dual-gen
62.88
97.0
+multi-task
65.02
-
Table 5: Results on the code defect detec-
tion and clone detection tasks.
4.5
Model Conﬁgurations
We build CodeT5 based on Huggingface’s T5 (Raf-
fel et al., 2020) PyTorch implementation3 and
employ two sizes of CodeT5-small (60M) and
CodeT5-base (220M). We set the maximum source
and target sequence lengths to be 512 and 256, re-
spectively. We use the mixed precision of FP16 to
accelerate the pre-training. We set the batch size
to 1024 and employ the peak learning rate of 2e-4
with linear decay. We pre-train the model with the
denoising objective for 100 epochs and bimodal
dual training for further 50 epochs on a cluster of
16 NVIDIA A100 GPUs with 40G memory. The
total training time for CodeT5-small and CodeT5-
base is 5 and 12 days, respectively.
In the ﬁne-tuning phase, we ﬁnd that the tasks in
CodeXGLUE (Lu et al., 2021) are quite sensitive
to some hyper parameters such as learning rate,
training steps, and batch size. We conduct a grid
search and select the best parameters based on the
validation set. In multi-task learning, we cover all
downstream tasks except clone detection.
5
Results and Analysis
In this section, we compare CodeT5 with SOTA
models on a broad set of CodeXGLUE downstream
tasks (§5.1), and investigate the effects of our
bimodal dual generation and multi-task learning
(§5.2), followed by a detailed analysis on the pro-
posed identiﬁer-aware pre-training (§5.3).
5.1
CodeXGLUE Downstream Tasks
We evaluate two sizes of our model: CodeT5-
small and CodeT5-base that are pre-trained with
identiﬁer-aware denoising. In addition, we consider
the model that continues to train with bimodal dual
3https://huggingface.co/
generation (dual-gen) and show the results with
multi-task ﬁne-tuning. The results of all compari-
son models are obtained from their original papers
and also the CodeXGLUE paper (Lu et al., 2021).
Code Summarization.
We show code summa-
rization results of smoothed BLEU-4 on six PL
data in Table 2. We observe all our model vari-
ants signiﬁcantly outperform prior work with either
an encode-only (RoBERTa, CodeBERT, DOBF)
or encoder-decoder framework (PLBART). More-
over, the salient performance gap between these
two groups of models conﬁrms that encode-only
frameworks are suboptimal for generation tasks.
Compared to the SOTA encoder-decoder model
PLBART, we ﬁnd that even our CodeT5-small
yields better overall scores (also on Python and
Java) given that our model is much smaller (60M
vs. 140M) and PLBART is pre-trained with much
larger Python and Java data (> 100 times). We at-
tribute such improvement to our identiﬁer-aware
denoising pre-training and better employment of bi-
modal training data4. By increasing the model size,
our CodeT5-base boosts the overall performance
by over 1.2 absolute points over PLBART.
Code Generation.
We compare CodeT5 with
GPT-style models and PLBART in Table 3. Our
CodeT5-small outperforms all decoder-only mod-
els and also the SOTA PLBART, which again
conﬁrms the superiority of encoder-decoder mod-
els at generating code snippets. Moreover, our
CodeT5-base further signiﬁcantly pushes the SOTA
results across three metrics. Particularly, it achieves
around 4.7 points improvement on CodeBLEU over
PLBART, indicating our CodeT5 can better com-
prehend the code syntax and semantics with the
help of identiﬁer-aware pre-training.
4Apart from bimodal dual generation, we concatenate NL
and PL for training while PLBART deals with them separately.

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

8703
Type
Code
Target
public long ramBytesUsed(){
return BASE_RAM_BYTES_USED+((index!=null)?
index.ramBytesUsed() : 0);}
CodeT5
public long ramBytesUsed(){
long sizeInBytes = BASE_RAM_BYTES_USED;
if (index != null){
sizeInBytes += index.ramBytesUsed();}
return sizeInBytes;}
Figure 3: One translation (C# to Java) example that is seman-
tically correct but with a 50.23% BLEU-4 score.
Code-to-Code Generation Tasks.
We compare
two code-to-code generation tasks: code translation
and code reﬁnement in Table 4 and further consider
one naive copy baseline by copying the source in-
put as the target prediction. In the code translation
task, our CodeT5-small outperforms most of base-
lines and obtains comparable results with PLBART,
which shows the advantages of encoder-decoder
models in the code-to-code generation setting. Our
CodeT5-base further achieves consistent improve-
ments over PLBART across various metrics for
translating from Java to C# and vice versa.
Here we show one CodeT5’s output of translat-
ing C# to Java in Figure 3. In this case, despite
the poor BLEU score, CodeT5 is able to gener-
ate a function that reserves the same functionality
and even has better readability compared to the
ground-truth. This reveals that CodeT5 has a good
generalization ability instead of memorizing and re-
peating what it has seen before. On the other hand,
it also suggests that BLEU score is not a perfect
evaluation metric for code generation tasks, where
sometimes a higher score can instead reﬂect the
problematic copy issues of neural models.
Another code-to-code generation task is code
reﬁnement, a challenging task that requires to de-
tect which parts of code are buggy and ﬁx them
via generating a bug-free code sequence. Due to
the large overlap of source and target code, even
the naive copy approach yields very high BLEU
scores but zero exact matches. Therefore, we fo-
cus on the exact match (EM) metric to evaluate
on this task. As shown in Table 4, we observe
that EM scores for the small data are consistently
higher than the medium one, indicating that it is
harder to ﬁx bugs for a longer code snippet. Our
CodeT5-base signiﬁcantly outperforms all base-
lines on EM and especially boosts over 4.8 points
for the more challenging medium task (13.96 vs.
GraphCodeBERT’s 9.10), reﬂecting its strong code
understanding capability.
Understanding Tasks.
We compare with two un-
derstanding tasks of defect detection and clone de-
Methods
Sum-PY
Code-Gen
Reﬁne Small
Defect
(BLEU)
(CodeBLEU)
(EM)
(Acc)
CodeT5
20.04
41.39
19.06
63.40
-MSP
18.93
37.44
15.92
64.02
-IT
19.73
39.21
18.65
63.29
-MIP
19.81
38.25
18.32
62.92
Table 6: Ablation study with CodeT5-small on four se-
lected tasks. “Sum-PY” denotes code summarization
on Python and “Code-Gen” denotes code generation.
tection in Table 5. Speciﬁcally, we generate the
binary labels as a unigram sequence from the de-
coder for the defect detection task, while for the
clone detection task, we ﬁrst obtain the sequence
embedding of each code snippet using the last
decoder state following Lewis et al. (2020) and
then predict the labels by measuring their simi-
larity. Both CodeT5-small and CodeT5-base out-
perform all baselines on the defect detection task
while CodeT5-base yields 2.6 accuracy score im-
provement than PLBART. For the clone detection
task, our CodeT5 models achieve comparable re-
sults to the SOTA GraphCodeBERT and PLBART
models. These results demonstrate that with an
encode-decoder framework, our CodeT5 can still
be adapted well for understanding tasks.
5.2
Effects of Bimodal Dual Generation and
Multi-task Learning
We examine the effects of bimodal dual genera-
tion at pre-training and multi-task learning at ﬁne-
tuning. The bimodal pre-training brings consistent
improvements for code summarization and genera-
tion tasks on both CodeT5-small and CodeT5-base.
However, this pre-training task does not help and
even sometimes slightly hurts the performance for
PL-PL generation and understanding tasks. We
anticipate this is because bimodal dual generation
learns a better alignment between PL and NL that
naturally beneﬁts the former tasks involving both
PL and NL. As a side effect, this objective could
bias the model towards the PL-NL tasks and affect
its performance on PL-PL tasks.
In multi-task learning, it generally improves
most of downstream tasks except the code trans-
lation and defect detection. Particularly, it largely
boosts the performance on code summarization,
which is not surprising as code summarization
takes up the largest portion of sub tasks (six out
of thirteen) and thereby beneﬁt the most from
the multi-task learning. Besides, we observe that
multi-task learning consistently improves the per-

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

8704
Type
Code
Source
Text: returns the string value of the
specified field. the value is obtained from
whichever scan contains the field.
Env: Scan
s1 ; Scan
s2 ; boolean
hasField
CodeT5
String function (String arg0){
if ( s1 . hasField (arg0))
return
s1 .getString(arg0);
else return
s2 .getString(arg0);}
W/o MIP+IT
String function (String arg0){
return
s1 .getString(arg0);}
Figure 4:
One code generation example on Concode
test set, where our CodeT5 gives a correct prediction.
The important identiﬁers are highlighted.
formance of code reﬁnement, which might beneﬁt
from the joint training of both small and medium
reﬁnement data. Another possible reason is that
multi-task training with defect detection would en-
able the model to better comprehend the code se-
mantics for bug detection, which is also a necessary
intermediate step for code reﬁnement.
5.3
Analyzing Identiﬁer-aware Pre-training
We provide an ablation study to examine the con-
tribution of each component in our identiﬁer-aware
pre-training objective. Speciﬁcally, we compare
the performance of our CodeT5-small on four se-
lected tasks by ablating each of the three objectives:
masked span prediction (MSP), identiﬁer tagging
(IT), and masked identiﬁer prediction (MIP). As
shown in Table 6, we observe that generally re-
moving one of the objectives would reduce the
performance for all tasks, indicating that all objec-
tives contribute to the better code understanding
of our CodeT5. However, the effect of each ob-
jective differs across tasks. Speciﬁcally, removing
MSP would largely reduce the performance of all
generation tasks but instead increase the defect de-
tection performance. This shows that masked span
prediction is more crucial for capturing syntactic
information for generation tasks. On the contrary,
removing MIP would hurt the defect detection task
the most, indicating that it might focus more on
code semantic understanding. By combining these
objectives, our CodeT5 can better capture both syn-
tactic and semantic information from code.
We further provide outputs from CodeT5 and its
variant without MIP and IT on code generation in
Figure 4. We observe that CodeT5 can correctly
generate the exact function, while the model with-
out MIP and IT fails to recover the identiﬁers of “s2”
and “hasField”. This shows our identiﬁer-aware
denoising pre-training can better distinguish and
leverage the identiﬁer information.
Methods
MSP
MIP
Acc
#Pred M
Acc
#Pred M
MSP-only
50.13
99.80
2.94
1.60
MIP-only
1.68
82.40
42.75
98.80
MIP+MSP
48.26
99.60
42.72
98.60
Table 7: Compare MSP and MIP on a subset of Java in
CodeSearchNet. “#Pred M” denotes the ratio of predic-
tion numbers that matches the sentinel token numbers.
We also investigate the identiﬁer tagging perfor-
mance and ﬁnd it achieves over 99% F1 for all PLs,
showing that our CodeT5 can conﬁdently distin-
guish identiﬁers in code. We then check whether
MSP and MIP tasks would have conﬂicts as they
employ the same sentinel tokens for masking. In
identiﬁer masking, all occurrences of one unique
identiﬁer are replaced with the same sentinel token,
resulting in a many-to-one mapping compared to
the one-to-one mapping in span prediction. We
compare models pre-trained with either MSP or
MIP, and both on these two tasks in Table 7. We
report the prediction accuracy and also the ratio of
how often they can generate the same number of
predictions as the sentinel tokens. We observe that
pre-training only with either MIP or MSP would
bias the model towards that task, achieving poor
accuracy and higher mismatch in number of predic-
tions when applied to the other task. Interestingly,
we ﬁnd that MIP-only objective can better recover
the correct number of predictions in the MSP task
than MSP-only does for the MIP task, meaning
that it is easier to adapt from many-to-one mapping
to one-to-one mapping and difﬁcult for the oppo-
site. At last, combining them can help our model
to make a good trade-off on both tasks.
6
Conclusion
We have presented CodeT5, a pre-trained encoder-
decoder model that incorporates the token type in-
formation from code. We propose a novel identiﬁer-
aware pre-training objective to better leverage the
identiﬁers and propose a bimodal dual generation
task to learn a better NL-PL alignment using code
and its comments. Our uniﬁed model can sup-
port both code understanding and generation tasks
and allow for multi-task learning. Experiments
show that CodeT5 signiﬁcantly outperforms all
prior work in most CodeXGLUE tasks. Further
analysis also reveals its better code comprehension
capability across various programming languages.

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

8705
Broader Impact and Ethical Consideration
Our work generally belongs to NLP applications
for software intelligence. With the goal of improv-
ing the development productivity of software with
machine learning methods, software intelligence
research has attracted increasing attention in both
academia and industries over the last decade. Soft-
ware code intelligence techniques can help develop-
ers to reduce tedious repetitive workloads, enhance
the programming quality and improve the overall
software development productivity. This would
considerably decrease their working time and also
could potentially reduce the computation and oper-
ational cost, as a bug might degrade the system per-
formance or even crash the entire system. Our work
addresses the fundamental challenge of software
code pre-training, our study covers a wide range
of code intelligence applications in the software
development lifecycle, and the proposed CodeT5
method achieves the state-of-the-art performance
on many of the benchmark tasks, showing its great
potential beneﬁt towards this goal.
We further discuss the ethical consideration of
training CodeT5 and the potential risks when ap-
plying it into real-world downstream applications:
Dataset bias.
The training datasets in our study
are source code including user-written comments
from open source Github repositories and publicly
available, which do not tie to any speciﬁc appli-
cation. However, it is possible that these datasets
would encode some stereotypes like race and gen-
der from the text comments or even from the source
code such as variables, function and class names.
As such, social biases would be intrinsically embed-
ded into the models trained on them. As suggested
by Chen et al. (2021), interventions such as ﬁltra-
tion or modulation of generated outputs may help
to mitigate these biases in code corpus.
Computational cost.
Our model pre-training re-
quires non-trivial computational resources though
we have tried our best to carefully design our ex-
periments and improve experiments to save unnec-
essary computation costs. In fact, compared to the
recent large-scale language model Codex (Chen
et al., 2021), our CodeT5-base has a much smaller
model size of 220M than theirs of 12B (∼55×).
In addition, we experiment on Google Cloud Plat-
form which purchases carbon credits to reduce its
carbon footprint, e.g., training CodeT5-base pro-
duced around 49.25 kg CO2 which was totally off-
set by the provider. Furthermore, we release our
pre-trained models publicly to avoid repeated train-
ing for the code intelligence research community.
Automation bias.
As CodeT5 can be deployed
to provide coding assistance such as code genera-
tion for aiding developers, automation bias of ma-
chine learning systems should be carefully consid-
ered, especially for developers who tend to over-
rely on the model-generated outputs. Sometimes
these systems might produce functions that superﬁ-
cially appear correct but do not actually align with
the developer’s intents. If developers unintention-
ally adopt these incorrect code suggestions, it might
cause them much longer time on debugging and
even lead to some signiﬁcant safety issues. We sug-
gest practitioners using CodeT5 should always bear
in mind that its generation outputs should be only
taken as references which require domain experts
for further correctness and security checking.
Security implications.
We train CodeT5 on ex-
isting code corpus including CodeSearchNet (Hu-
sain et al., 2019) and a small fraction of Google
BigQuery, both of which are originally collected
from public Github repositories. Pre-trained mod-
els might encode some sensitive information (e.g.,
personal addresses or identiﬁcation numbers) from
the training data. Though we have conducted multi-
rounds of data cleaning to mitigate this before train-
ing our models, it is still possible that some sen-
sitive information cannot be completely removed.
Besides, due to the non-deterministic nature of gen-
eration models like CodeT5, it might produce some
vulnerable code to harmfully affect the software
and even be able to beneﬁt more advanced malware
development when deliberately misused.
Acknowledgements
We thank Akhilesh Deepak Gotmare, Amrita Saha,
Junnan Li, and Chen Xing for valuable discussions.
We thank Kathy Baxter for the ethical review. We
thank the CodeXGLUE team (Lu et al., 2021) who
provide wonderful code5 to facilitate the easy eval-
uation on their benchmarks and especially thank
Daya Guo for clarifying some confused points. We
also thank our anonymous reviewers for their in-
sightful feedback on our paper.
5https://github.com/microsoft/
CodeXGLUE

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

8706
References
Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi
Ray, and Kai-Wei Chang. 2021. Uniﬁed pre-training
for program understanding and generation.
In
Proceedings of the 2021 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
NAACL-HLT 2021, Online, June 6-11, 2021, pages
2655–2668. Association for Computational Linguis-
tics.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde de Oliveira Pinto, Jared
Kaplan, Harrison Edwards, Yuri Burda, Nicholas
Joseph, Greg Brockman, Alex Ray, Raul Puri,
Gretchen Krueger, Michael Petrov, Heidy Khlaaf,
Girish Sastry, Pamela Mishkin, Brooke Chan, Scott
Gray, Nick Ryder, Mikhail Pavlov, Alethea Power,
Lukasz Kaiser, Mohammad Bavarian, Clemens Win-
ter, Philippe Tillet, Felipe Petroski Such, Dave Cum-
mings, Matthias Plappert, Fotios Chantzis, Eliza-
beth Barnes, Ariel Herbert-Voss, William Hebgen
Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie
Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain,
William Saunders, Christopher Hesse, Andrew N.
Carr, Jan Leike, Joshua Achiam, Vedant Misra, Evan
Morikawa, Alec Radford, Matthew Knight, Miles
Brundage, Mira Murati, Katie Mayer, Peter Welin-
der, Bob McGrew, Dario Amodei, Sam McCandlish,
Ilya Sutskever, and Wojciech Zaremba. 2021. Evalu-
ating large language models trained on code. CoRR,
abs/2107.03374.
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and
Christopher D. Manning. 2020.
ELECTRA: pre-
training text encoders as discriminators rather than
generators.
In 8th International Conference on
Learning Representations, ICLR 2020, Addis Ababa,
Ethiopia, April 26-30, 2020. OpenReview.net.
Colin B. Clement, Dawn Drain, Jonathan Timcheck,
Alexey Svyatkovskiy, and Neel Sundaresan. 2020.
Pymt5: multi-mode translation of natural language
and python code with transformers. In Proceedings
of the 2020 Conference on Empirical Methods in
Natural Language Processing, EMNLP 2020, On-
line, November 16-20, 2020, pages 9052–9065. As-
sociation for Computational Linguistics.
Alexis Conneau and Guillaume Lample. 2019. Cross-
lingual language model pretraining.
In Advances
in Neural Information Processing Systems 32: An-
nual Conference on Neural Information Processing
Systems 2019, NeurIPS 2019, December 8-14, 2019,
Vancouver, BC, Canada, pages 7057–7067.
Sergio Cozzetti B. de Souza, Nicolas Anquetil, and
Káthia Marçal de Oliveira. 2005. A study of the doc-
umentation essential to software maintenance.
In
Proceedings of the 23rd Annual International Con-
ference on Design of Communication: documenting
& Designing for Pervasive Information, SIGDOC
2005, Coventry, UK, September 21-23, 2005, pages
68–75. ACM.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, NAACL-HLT 2019, Minneapolis, MN,
USA, June 2-7, 2019, Volume 1 (Long and Short Pa-
pers), pages 4171–4186.
Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xi-
aodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou,
and Hsiao-Wuen Hon. 2019.
Uniﬁed language
model pre-training for natural language understand-
ing and generation.
In Advances in Neural Infor-
mation Processing Systems 32: Annual Conference
on Neural Information Processing Systems 2019,
NeurIPS 2019, December 8-14, 2019, Vancouver,
BC, Canada, pages 13042–13054.
Ahmed Elnaggar, Wei Ding, Llion Jones, Tom Gibbs,
Tamas Feher, Christoph Angerer, Silvia Severini,
Florian Matthes, and Burkhard Rost. 2021. Code-
trans: Towards cracking the language of silicone’s
code through self-supervised deep learning and high
performance computing. CoRR, abs/2104.02443.
Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xi-
aocheng Feng, Ming Gong, Linjun Shou, Bing Qin,
Ting Liu, Daxin Jiang, and Ming Zhou. 2020. Code-
bert: A pre-trained model for programming and nat-
ural languages.
In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing: Findings, EMNLP 2020, Online Event,
16-20 November 2020, pages 1536–1547. Associa-
tion for Computational Linguistics.
Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng,
Duyu Tang, Shujie Liu, Long Zhou, Nan Duan,
Alexey Svyatkovskiy, Shengyu Fu, Michele Tu-
fano, Shao Kun Deng, Colin B. Clement, Dawn
Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, and
Ming Zhou. 2021.
Graphcodebert:
Pre-training
code representations with data ﬂow.
In 9th Inter-
national Conference on Learning Representations,
ICLR 2021, Virtual Event, Austria, May 3-7, 2021.
OpenReview.net.
Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis
Allamanis, and Marc Brockschmidt. 2019.
Code-
searchnet challenge: Evaluating the state of seman-
tic code search. CoRR, abs/1909.09436.
Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, and
Luke Zettlemoyer. 2018. Mapping language to code
in programmatic context.
In Proceedings of the
2018 Conference on Empirical Methods in Natural
Language Processing, Brussels, Belgium, October
31 - November 4, 2018, pages 1643–1652. Associ-
ation for Computational Linguistics.
Aditya Kanade, Petros Maniatis, Gogul Balakrishnan,
and Kensen Shi. 2020.
Learning and evaluating

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

8707
contextual embedding of source code. In Proceed-
ings of the 37th International Conference on Ma-
chine Learning, ICML 2020, 13-18 July 2020, Vir-
tual Event, volume 119 of Proceedings of Machine
Learning Research, pages 5110–5121. PMLR.
Mike
Lewis,
Yinhan
Liu,
Naman
Goyal,
Mar-
jan Ghazvininejad, Abdelrahman Mohamed, Omer
Levy, Veselin Stoyanov, and Luke Zettlemoyer.
2020. BART: denoising sequence-to-sequence pre-
training for natural language generation, translation,
and comprehension. In Proceedings of the 58th An-
nual Meeting of the Association for Computational
Linguistics, ACL 2020, Online, July 5-10, 2020,
pages 7871–7880. Association for Computational
Linguistics.
Chin-Yew Lin and Franz Josef Och. 2004. ORANGE:
a method for evaluating automatic evaluation met-
rics for machine translation. In COLING 2004, 20th
International Conference on Computational Linguis-
tics, Proceedings of the Conference, 23-27 August
2004, Geneva, Switzerland.
Fang Liu, Ge Li, Yunfei Zhao, and Zhi Jin. 2020. Multi-
task learning based pre-trained language model for
code completion.
In 35th IEEE/ACM Interna-
tional Conference on Automated Software Engineer-
ing, ASE 2020, Melbourne, Australia, September 21-
25, 2020, pages 473–485. IEEE.
Xiaodong Liu, Pengcheng He, Weizhu Chen, and Jian-
feng Gao. 2019a. Multi-task deep neural networks
for natural language understanding. In Proceedings
of the 57th Conference of the Association for Compu-
tational Linguistics, ACL 2019, Florence, Italy, July
28- August 2, 2019, Volume 1: Long Papers, pages
4487–4496. Association for Computational Linguis-
tics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019b.
Roberta: A robustly optimized BERT pretraining ap-
proach. CoRR, abs/1907.11692.
Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey
Svyatkovskiy, Ambrosio Blanco, Colin B. Clement,
Dawn Drain, Daxin Jiang, Duyu Tang, Ge Li, Li-
dong Zhou, Linjun Shou, Long Zhou, Michele Tu-
fano, Ming Gong, Ming Zhou, Nan Duan, Neel Sun-
daresan, Shao Kun Deng, Shengyu Fu, and Shujie
Liu. 2021. Codexglue: A machine learning bench-
mark dataset for code understanding and generation.
CoRR, abs/2102.04664.
Antonio Mastropaolo, Simone Scalabrino, Nathan
Cooper, David Nader-Palacio, Denys Poshyvanyk,
Rocco Oliveto, and Gabriele Bavota. 2021. Study-
ing the usage of text-to-text transfer transformer to
support code-related tasks. In 43rd IEEE/ACM Inter-
national Conference on Software Engineering, ICSE
2021, Madrid, Spain, 22-30 May 2021, pages 336–
347. IEEE.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8):9.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J. Liu. 2020. Exploring the limits
of transfer learning with a uniﬁed text-to-text trans-
former. J. Mach. Learn. Res., 21:140:1–140:67.
Shuo Ren, Daya Guo, Shuai Lu, Long Zhou, Shujie
Liu, Duyu Tang, Neel Sundaresan, Ming Zhou, Am-
brosio Blanco, and Shuai Ma. 2020. Codebleu: a
method for automatic evaluation of code synthesis.
CoRR, abs/2009.10297.
Baptiste
Rozière,
Marie-Anne
Lachaux,
Lowik
Chanussot, and Guillaume Lample. 2020.
Unsu-
pervised translation of programming languages. In
Advances in Neural Information Processing Systems
33:
Annual Conference on Neural Information
Processing Systems 2020, NeurIPS 2020, December
6-12, 2020, virtual.
Baptiste
Rozière,
Marie-Anne
Lachaux,
Marc
Szafraniec, and Guillaume Lample. 2021. DOBF:
A deobfuscation pre-training objective for program-
ming languages. CoRR, abs/2102.07492.
Rico Sennrich, Barry Haddow, and Alexandra Birch.
2016. Neural machine translation of rare words with
subword units. In Proceedings of the 54th Annual
Meeting of the Association for Computational Lin-
guistics, ACL 2016, August 7-12, 2016, Berlin, Ger-
many, Volume 1: Long Papers. The Association for
Computer Linguistics.
Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu, and Tie-
Yan Liu. 2019.
MASS: masked sequence to se-
quence pre-training for language generation. In Pro-
ceedings of the 36th International Conference on
Machine Learning, ICML 2019, 9-15 June 2019,
Long Beach, California, USA, volume 97 of Pro-
ceedings of Machine Learning Research, pages
5926–5936. PMLR.
Yu Sun, Shuohuan Wang, Yu-Kun Li, Shikun Feng,
Xuyi Chen, Han Zhang, Xin Tian, Danxiang Zhu,
Hao Tian, and Hua Wu. 2019.
ERNIE: en-
hanced representation through knowledge integra-
tion. CoRR, abs/1904.09223.
Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu,
and Neel Sundaresan. 2020.
Intellicode compose:
code generation using transformer.
In ESEC/FSE
’20: 28th ACM Joint European Software Engineer-
ing Conference and Symposium on the Founda-
tions of Software Engineering, Virtual Event, USA,
November 8-13, 2020, pages 1433–1443. ACM.
Michele Tufano, Cody Watson, Gabriele Bavota, Mas-
similiano Di Penta, Martin White, and Denys Poshy-
vanyk. 2019.
An empirical study on learning
bug-ﬁxing patches in the wild via neural machine

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

8708
translation.
ACM Trans. Softw. Eng. Methodol.,
28(4):19:1–19:29.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Pro-
cessing Systems 30: Annual Conference on Neural
Information Processing Systems 2017, December 4-
9, 2017, Long Beach, CA, USA, pages 5998–6008.
Wenhan Wang, Ge Li, Bo Ma, Xin Xia, and Zhi
Jin. 2020.
Detecting code clones with graph neu-
ral network and ﬂow-augmented abstract syntax
tree.
In 27th IEEE International Conference on
Software Analysis, Evolution and Reengineering,
SANER 2020, London, ON, Canada, February 18-
21, 2020, pages 261–271. IEEE.
Yaqin Zhou, Shangqing Liu, Jing Kai Siow, Xiaon-
ing Du, and Yang Liu. 2019.
Devign: Effective
vulnerability identiﬁcation by learning comprehen-
sive program semantics via graph neural networks.
In Advances in Neural Information Processing Sys-
tems 32: Annual Conference on Neural Information
Processing Systems 2019, NeurIPS 2019, December
8-14, 2019, Vancouver, BC, Canada, pages 10197–
10207.
Daniel Zügner, Tobias Kirschstein, Michele Catasta,
Jure Leskovec, and Stephan Günnemann. 2021.
Language-agnostic representation learning of source
code from structure and context.
In 9th Inter-
national Conference on Learning Representations,
ICLR 2021, Virtual Event, Austria, May 3-7, 2021.
OpenReview.net.

[Vista original de la página 13](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-13.png)

![Página PDF 13, representación visual original](../../../../../images/v5/estructura_colecciones/Other/not%20defined/CodeT5.emnlp-main.685/page-13.png)
