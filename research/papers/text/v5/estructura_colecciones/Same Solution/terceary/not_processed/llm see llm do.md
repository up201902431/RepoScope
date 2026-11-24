# LLM See, LLM Do: Enhancing Repository-Aware Code Generation in LLMs Through Logical Context and Usage Knowledge

- source_pdf: ../../../../../../pdf/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

LLM See, LLM Do: Enhancing Repository-Aware Code Generation in
LLMs Through Logical Context and Usage Knowledge
TANGHAORAN ZHANG, National University of Defense Technology, China
XINJUN MAO∗, National University of Defense Technology, China
YUXIN ZHAO, National University of Defense Technology, China
KANG YANG, National University of Defense Technology, China
ZHANG ZHANG, National University of Defense Technology, China
YAO LU, National University of Defense Technology, China
YOUREN CHEN, National University of Defense Technology, China
YUE YU∗†, Peng Cheng Laboratory, China
Large language models (LLMs) have significantly advanced automatic code generation. Although they have demonstrated
remarkable ability in writing standalone code, they still struggle with real-world repository-level coding tasks due to the lack
of repository-specific knowledge. Existing studies typically employ retrieval-augmented generation (RAG) approaches to
retrieve relevant context to guide LLMs’ generation. However, these approaches fail to ensure the logical relevance and the
usability of retrieved results, leading to suboptimal code generation. To address this problem, we propose LogiCoder, a novel
RAG approach that leverages logical relationships within code repositories to retrieve usage knowledge for LLMs. Specifically,
LogiCoder first builds a dependency graph to identify candidate callee functions. By tracing their call relationships, LogiCoder
retrieves their usage examples from the entire repository. Then it integrates the most contextually similar ones with semantic
search results via re-ranking. These top-ranked examples are eventually incorporated into LLMs’ prompts to enhance their
repository awareness during code generation. We apply LogiCoder to five widely-used LLMs and evaluate it on the DevEval
benchmark. Experimental results show that on challenging tasks that require cross-file calls, LogiCoder achieves a new
state-of-the-art Pass@1 of 44.58%, with relative improvements of up to 27.26% in Pass@1 and 14.71% in Recall@1 over existing
baselines. Ablation studies confirm the effectiveness of each component in LogiCoder.
CCS Concepts: • Software and its engineering →Automatic programming; Software libraries and repositories; • Com-
puting methodologies →Artificial intelligence; • Information systems →Information retrieval.
Additional Key Words and Phrases: Code Generation, Large Language Models, Repository-Level Context, Retrieval-Augmented
Generation, Logical Context, Static Analysis
∗Xinjun Mao and Yue Yu are corresponding authors.
†The author was also affiliated with National University of Defense Technology during the completion of this work.
Authors’ Contact Information: Tanghaoran Zhang, zhangthr@nudt.edu.cn, National University of Defense Technology, Changsha, Hu-
nan, China; Xinjun Mao, xjmao@nudt.edu.cn, National University of Defense Technology, Changsha, Hunan, China; Yuxin Zhao, yux-
inzhao@nudt.edu.cn, National University of Defense Technology, Changsha, Hunan, China; Kang Yang, yangkang@nudt.edu.cn, National
University of Defense Technology, Changsha, Hunan, China; Zhang Zhang, zhangzhang14@nudt.edu.cn, National University of Defense
Technology, Changsha, Hunan, China; Yao Lu, luyao08@nudt.edu.cn, National University of Defense Technology, Changsha, Hunan, China;
Youren Chen, chenyouren0808@nudt.edu.cn, National University of Defense Technology, Changsha, Hunan, China; Yue Yu, yuy@pcl.ac.cn,
Peng Cheng Laboratory, Changsha, Hunan, China.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that
copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy
otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org.
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1557-7392/2026/10-ART
https://doi.org/10.1145/3849809
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 1](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-01.png)

![Página PDF 1, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

2
•
Zhang et al.
1
Introduction
Automatic code generation, known as the process of generating programs automatically from high-level user
requirements without the need for manual coding, has been studied by researchers in the software engineering
domain for years [16, 23, 51]. Recently, large language models (LLMs) have significantly advanced the progress
of this task [27]. These models are capable of completing various coding tasks through extensive pre-training
on vast code corpora [24, 37, 56, 65], even surpassing most human programmers on CodeForces1. Due to LLMs’
remarkable performance, they are widely adopted in code generation tasks [28, 30] or even deployed as intelligent
software development tools, e.g., GitHub Copilot2, Cursor3, etc.
However, compared with generating standalone code, LLMs are less effective when tasked with repository-
aware code generation [31, 33, 60], a common requirement in real-world software development. One important
reason is that LLMs lack the repository-specific knowledge [5, 34, 63]. Specifically, real software repositories often
possess rich contextual information and intricate dependencies among modules and files [31]. The generated
code should fit the specific needs of developers’ repository context, e.g., using intra-repository APIs to implement
features [62]. As for LLMs, such knowledge could be inaccessible due to data availability issues in the training
phase [61]. Meanwhile, their limited context window and distractible nature [36, 47, 59] also prevent LLMs from
learning all repository-level knowledge in the inference phase.
To enable LLMs’ better utilization of external knowledge, the retrieval-augmented generation (RAG) frame-
work [8, 19, 32] is proposed. It aims to guide LLMs for expected generation with relevant context from the
knowledge base. A common practice is to use adjacent context of the completion target as a query for retrieval
and then insert retrieved results into LLMs’ prompts [43]. Software engineering researchers also follow such
pattern to design approaches for code generation [38, 63]. As RAG approaches rely on the few-shot learning
abilities of LLMs [7], their effectiveness can be highly related to the quality of retrieved results [18]. To enhance
retrieval, prior studies mainly focus on two directions: (1) similarity-based approaches [34, 40, 63] that identify
relevant code using textual or semantic similarity, and (2) static-analysis-enhanced approaches [2, 11, 38, 39] that
incorporate structural relationships derived from static analysis to guide the retrieval process.
However, repository-aware code generation is not only about code retrieval, but also requires LLMs to
synthesize correct code based on the retrieved results. Existing approaches still exhibit limitations in retrieving
useful context for LLMs’ subsequent generation. Specifically, as illustrated in Figure 1, similarity-based approaches
can retrieve code snippets with high similarity, but their retrieved results are not guaranteed to be logically
relevant and may not aid the generation process. In comparison, current static-analysis-enhanced approaches
like DraCo and RepoScope can extract relevant code, e.g., the potential callee functions as declarative background
knowledge. However, this places the burden on LLMs to correctly use such dependencies and may also incur
suboptimal code generation [33]. We assume that without enough local context or implementation details, LLMs
cannot accurately utilize such dependency knowledge during the generation. This highlights a critical need
for retrieval techniques that ensure both the logical relevance and the immediate usability of context in the
LLM-based repository-aware code generation task.
To address the above challenges, we introduce a novel retrieval strategy tailored for Python code repositories
by leveraging the call relationships between elements. The core idea is to retrieve similar usage examples of the
dependencies. As illustrated in Figure 1, we first extract all the candidate callees, covering all dependencies of the
generation task. Then we trace their callers and retrieve the most similar usage examples for LLMs’ subsequent
generation. Firstly, these examples are relevant to the generation task, as prior studies find that similar usage
examples are semantically related [1, 3]. Secondly, they represent correct contextual usage of repository-specific
1https://codeforces.com/ratings
2https://github.com/features/copilot
3https://www.cursor.com
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 2](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-02.png)

![Página PDF 2, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

LLM See, LLM Do
•
3
# boto/ec2/instance.py
def update(self, validate=False, dry_run=False):
  rs = self.connection.get_all_snapshots(
    [self.id], dry_run=dry_run
  )
  if len(rs) > 0:
    self._update(rs[0])
  elif validate:
    raise ValueError('%s is not a valid Snapshot ID' % self.id)
  return self.status
# boto/ec2/volume.py
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
class Volume(TaggedEC2Object):
  ...
  def update(self, validate=False, dry_run=False):
    """
    This function updates the data associated with a volume ...
    """
    unfiltered_rs = self.connection.get_all_volumes(
      [self.id], dry_run=dry_run
    )
    rs = [x for x in unfiltered_rs if x.id == self.id]
    if len(rs) > 0:
      self._update(rs[0])
    elif validate:
      raise ValueError('%s is not a valid Volume ID' % self.id)
    return self.status
# boto/vpc/vpngateway.py
def attach(self, vpc_id, dry_run=False):
  return self.connection.attach_vpn_gateway(self.id, vpc_id, 
dry_run=dry_run)
# boto/manage/volume.py
def create_from_volume_id(cls, region_name, volume_id, name):
  vol = None
  ec2 = boto.ec2.connect_to_region(region_name)
  rs = ec2.get_all_volumes([volume_id])
  if len(rs) == 1:
    v = rs[0]
    vol = cls()
    vol.volume_id = v.id
    vol.name = name
    vol.region_name = v.region.name
    vol.zone_name = v.zone
    vol.put()
  return vol
# boto/resultset.py
class ResultSet(list):
  def __init__(self, marker_elem=None): 
    ...
Similarity-Based Retrieval
SA-Enhanced Retrieval
Repository-Aware Code Generation
Retrieval Based on Logical Context 
LLM
Are these contexts relevant to my task?
LLM
How to use these contexts in my generation?
LLM
Now, I know how to 
implement this function!
Candidate Callees
(Logical Context)
Similar Usage Examples
1. Trace callees
2. Trace callers
Repo: boto
# boto/ec2/tag.py
class Tag(object):
  def __init__(self, connection=None, res_id=None, res_type= 
None, name=None, value=None):
   ...
# boto/ec2/ec2object.py
class EC2Object(object):
 def __init__(self, connection=None):
   ...
class TaggedEC2Object(EC2Object):
 def __init__(self, connection=None):
   ...
Ground Truth
# boto/ec2/volume.py
def _update(self, updated): 
  ...# boto/ec2/connection.py
def get_all_volumes(self, volume_ids=None, ...): 
  ...# boto/ec2/connection.py
def get_all_snapshots(self, snapshots_ids, ...): 
  ...
# boto/ec2//networkinterface.py
def update(self, validate=False, dry_run=False):
  rs = self.connection.get_all_snapshots(
    [self.id], dry_run=dry_run
  )
  if len(rs) > 0:
    self._update(rs[0])
  elif validate:
    raise ValueError('%s is not a valid Snapshot ID' % self.id)
  return self.status
# boto/ec2/snapshot.py
def update(self, validate=False, dry_run=False):
  rs = self.connection.get_all_snapshots(
    [self.id], dry_run=dry_run
  )
  if len(rs) > 0:
    self._update(rs[0])
  elif validate:
    raise ValueError('%s is not a valid Snapshot ID' % self.id)
  return self.status
Usage
Fig. 1. Comparisons between the retrieval of existing RAG baselines and LogiCoder’s retrieval based on logical context.
Code generated by different approaches is shown in Figure 8.
dependencies. It only requires LLMs to imitate rather than learn to use the dependencies from scratch, which is
also aligned to the objectives of few-shot learning [7]. Based on this, we propose LogiCoder, an RAG approach
that enables LLMs to effectively utilize usage knowledge within repositories for code generation. Specifically, we
first construct a dependency graph for each repository to capture multiple relationships between code elements,
including their accessibility and call relationships. For each function to be generated, LogiCoder identifies all
available intra-repository functions based on its current context and the dependency graph. These candidates
callees are the logical context of the target function, serving as intermediate cues for further retrieval. By tracing
their call relationships, LogiCoder then retrieves their usage examples from the entire repository and ranks
them with their context similarity. To mitigate the issues of irrelevant examples and the absence of direct call
patterns, LogiCoder integrates semantic search as a complementary retrieval strategy. It employs a re-ranking
technique to fuse two retrieval results. Eventually, LogiCoder incorporates these re-ranked code examples into
LLMs’ prompts to enhance their context utilization and repository awareness during code generation.
We evaluate LogiCoder on a real-world repository-aware code generation benchmark, DevEval [31], using
five widely-used LLMs. We perform a comprehensive comparison with various baselines and conduct a thorough
ablation study for each component of LogiCoder. Experimental results show that: (1) On challenging tasks that
require cross-file calls, LogiCoder outperforms the state-of-the-art baselines across all backbone LLMs, with
relative improvements up to 27.26% in Pass@1 and 14.71% in Recall@1; (2) LogiCoder can effectively capture
logical relationships within code repositories, with 40.25% actual callee functions included in its top retrieved
usage examples; (3) Compared to directly providing candidate callees, showing their similar usage examples can
substantially enhance LLMs’ code generation performance; (4) Semantic search fusion can effectively complement
the retrieval based on logical context and further improve LogiCoder’s performance; (5) LogiCoder consistently
yields positive performance gains on the broader mixed-dependency setting, though to a more moderate extent;
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 3](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-03.png)

![Página PDF 3, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

4
•
Zhang et al.
and (6) To balance effectiveness and computational cost, we identify 3K tokens as the optimal retrieval context
length for using LogiCoder in practice.
This paper makes the following contributions:
• We introduce a novel retrieval strategy designed for repository-aware code generation task. Instead of retrieving
similar context in a single hop, we model the logical structure of code in a dependency graph and perform
usage example retrieval based on it. This modeling enriches LLMs with a distinct profile of code repositories.
• We propose a novel retrieval-augmented code generation approach named LogiCoder. It leverages logical
context to retrieve similar usage examples within the repository and integrates them with semantic search
results. LogiCoder provides LLMs with essential repository-specific knowledge and enhances their context
utilization capability, which can also be integrated with LLM-based agent frameworks in the future.
• By conducting comprehensive experiments, we demonstrate the effectiveness of LogiCoder over state-of-the-
art baselines. Our ablation study further shows that providing similar usage examples of repository-specific
APIs can elicit LLMs’ code generation capability more effectively than providing the dependencies alone. The
source code of LogiCoder and our experimental results for replication are provided here4.
The rest of this paper is organized as follows: Section 2 introduces the background of our study and discusses
its related work. Section 3 proposes our design of LogiCoder. Section 4 presents experiment settings of our study.
Section 5 exhibits the evaluation results of LogiCoder. Section 6 presents a case study and further discusses the
strengths, weaknesses and implications of LogiCoder. Section 7 discusses potential threats to validity. Section 8
concludes the paper.
2
Background and Related Work
2.1
LLM-based Code Generation
Since LLMs are pre-trained on an extremely large scale of data consisting of both natural language and source
code corpora, LLMs are empowered with remarkable capabilities in code generation tasks. Although general
LLMs like GPT-series [7] gain emergent abilities [52] on code generation, researchers further fine-tune those
models to produce code LLMs for better coding ability, including their closed-source ones (e.g., Codex [10])
and open-source replications (e.g., CodeGen [42], InCoder [17], WizardCoder [41], DeepSeek-Coder [21], etc.).
To further elicit LLMs’ code generation capability, recent studies highlight the critical role of prompt engi-
neering [37, 45]. Approaches like chain-of-thought [30, 53] or self-planning [28] are adapted to the domain
of code generation, achieving state-of-the-art performance in generating code snippets from natural language
descriptions in benchmarks like HumanEval [10]. Based on these prompting techniques, approaches such as
CodeAgent [64] introduce the agentic workflows to code generation tasks, empowering LLMs with tool-use ability
to interact with code context in a multi-turn process. More recent specialized agents, such as SWE-agent [58]
and OpenCode5, push it further by incorporating optimized tool calls and workflows, specifically designed for
complex software engineering tasks such as end-to-end issue resolution. While LLMs excel at small-scale and
independent coding tasks, their effectiveness diminishes when confronted with repository-specific requirements
that demand awareness of local repository context [63]. Hence, in this paper, we aim to enhance LLMs’ repository
awareness during code generation to facilitate their applications in real-world coding scenarios.
2.2
Repository-level Code Completion
Repository-level code completion is widely recognized as a scenario aligned with real-world software development,
which has received increasing attention from the software engineering community. To address the limitation of
4https://github.com/ztwater/LogiCoder
5https://github.com/anomalyco/opencode
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 4](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-04.png)

![Página PDF 4, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

LLM See, LLM Do
•
5
LLMs in leveraging repository-specific knowledge, current studies have primarily explored two approaches. The
first way is model training or fine-tuning. Through specialized training, LLMs are expected to develop the ability to
utilize repository-specific knowledge to complete code tokens. Representative frameworks include RepoFusion [48]
and CoCoMIC [14]. Wang et al. propose ToolGen [50], which fine-tunes LLMs to trigger autocompletion tools.
Based on the recommendations from tools, LLMs could generate code with less dependency errors within the
repository context. However, such methods exhibit limited flexibility and generalization ability, which require
retraining or fine-tuning to adapt to evolving proprietary repositories.
To enable LLMs to utilize repository-level context during the inference phase, existing studies adopt RAG
as an alternative approach. Its core idea is to leverage LLMs’ few-shot learning ability [7] to complete code
based on selected context provided in their prompts. Zhang et al. propose RepoCoder [63], a framework that
iteratively retrieves similar context from code repositories to enhance LLMs’ code completion. The approach
leverages the generated code to refine the retrieval process in turn, thereby reducing the semantic gap between
the retrieved context and the generated content. Besides, Bi et al. [5] incorporate compiler feedback into search
queries and prompts to equip LLMs with knowledge during execution. By iteratively fixing the identified errors,
they significantly improve LLMs’ capabilities to generate code dependent on the repository-specific context.
Wu et al. [54] observe that a large proportion of retrieved context provides no benefits for LLMs’ completions.
To improve the efficiency of the RAG pipeline, they propose RepoFormer by employing a selective policy to
trigger the retrieval process. Liao et al. propose the 𝐴3𝐶𝑜𝑑𝐺𝑒𝑛framework [34] to reuse repository-level context
by extracting local, global and third-party knowledge from a constructed knowledge base.
However, the above approaches primarily consider the similarity between the completion target and its adjacent
context, while neglecting characteristics of the code itself. To this end, several studies improve RAG approaches
with static analysis results. Agrawal et al. propose monitor-guided decoding [2] to assist LLMs for code generation.
Their approach automatically triggers static analysis at partial object dereferences to adjust token probabilities
during LLMs’ decoding phase. Cheng et al. propose a dataflow-guided RAG approach, DraCo [11], to address
LLMs’ knowledge deficiency in private repositories. It uses dataflow analysis to build a repository-specific
context graph for retrieval, enhancing LLMs with relevant background knowledge. GraphCoder [38] builds a code
context graph using control flow, data dependence and control dependence. It uses a program slice generated
from the incomplete function to perform retrieval. However, current static-analysis-enhanced RAG approaches
are designed to assist code completion within an existing function body. Their retrieval or prompt generation
techniques depend on the presence of local code context (e.g., partial expressions or local variables), which
is unavailable for function-level code generation from scratch. This limitation motivates our study to explore
RAG approaches independent of intra-function context. More recently, RepoScope [39] predicts the call chain
of the target function to retrieve its direct callers and potential callees. It then combines this information with
similarity-based retrieval to provide a multi-view context. Besides, approaches like DraCo and RepoScope only
retrieve relevant code entities (e.g., potential callees) as isolated background knowledge without demonstrating
how they should be used in the specified context. It cannot illustrate how they should be used in the specified
context. We hypothesize that this may hinder LLMs’ ability to synthesize these entities into a correct function
implementation. To address this gap, we further investigate the logical relationships within the repository and
enhance LLM generation by providing relevant usage examples.
3
LogiCoder
3.1
Overview
The task of repository-aware code generation can be described as follows:̂
𝐹= ℳ(𝐹𝑠𝑖𝑔, 𝐶𝑟𝑒𝑝𝑜)
(1)
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 5](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-05.png)

![Página PDF 5, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

6
•
Zhang et al.
where 𝐹𝑠𝑖𝑔represents the signature of the target function 𝐹to complete, and 𝐶𝑟𝑒𝑝𝑜represents current repository-
level context. A LLM ℳgenerates the predicted code based on 𝐹𝑠𝑖𝑔and 𝐶𝑟𝑒𝑝𝑜. However, it is impractical to
include the whole repository 𝐶𝑟𝑒𝑝𝑜in the prompt of ℳ. Thus, current RAG approaches leverage a retriever ℛ
to extract a set of relevant code snippets 𝑆= {𝑠1, 𝑠2, … , 𝑠𝑛} from 𝐶𝑟𝑒𝑝𝑜based on 𝐹𝑠𝑖𝑔, which can be denoted as
𝑆= ℛ(𝐹𝑠𝑖𝑔, 𝐶𝑟𝑒𝑝𝑜). Then the LLM includes the retrieved snippets 𝑆in its prompt to generate the target function̂ 𝐹.
Intra-file Context
def update(self, validate=False, 
dry_run=False):
    """
    This function updates the data 
associated with a volume ...
    """
Target Function
Import Edge
Current File
Function Node
Association Edge
Top Usage Examples
1
Logical Context Extraction
Current File 
to Complete
2
Usage Example Retrieval
4
Augmented Generation
Rank By Context 
Similarity
LLM
Target Func
Intra-file Ctx
Correct Use
Generation Prompt
Current Class
Associated 
Class
Other Files
Logical 
Context
Call Edge
Function Node
Usage Node
Extract By Dependency
Retrieved Code
Trace Call 
Relationship 
Embedding
3
Semantic Search Fusion
Funcs in Repo
…
Index
Rank By Cosine 
Similarity
Rerank
Reranked
Examples
Target Func
Generated 
Code
Target Func
Fig. 2. The framework of LogiCoder.
The overall framework of LogiCoder is illustrated in Figure 2. To better model the context of a software
repository 𝐶𝑟𝑒𝑝𝑜, we first construct a dependency graph by extracting its code elements and their relations
(Section 3.2). Given the target function to be generated, LogiCoder employs a four-module pipeline to obtain
the final output̂ 𝐹. It starts with the Logical Context Extraction (LCE) module, which extracts candidate callee
functions from the dependency graph (Section 3.3). Next, the Usage Example Retrieval (UER) module retrieves the
corresponding usage examples for each candidate callee in the logical context. These examples are then ranked
based on their contextual similarity to the current task context (Section 3.4). Then the Semantic Search Fusion (SSF)
module integrates this ranked list with semantic search results via re-ranking, which serves as a relevance filter
and fallback mechanism (Section 3.5). Eventually, the Augmented Generation module incorporates top-ranked
examples into LLMs’ prompts to generate the final function̂ 𝐹(Section 3.6).
3.2
Dependency Graph Construction
Previous studies such as RepoCoder [63] regard code corpora as natural language corpora, and use a sliding
window to chunk code files into fragments that are equal in length. Such approaches harm the inherent structure
and logic of code, leading to incomplete code and the loss of dependency relationships. For instance, a complete
function may be split into multiple fragments, or a single fragment covers multiple functions. Such chunking
may hinder the understanding and analysis of the code, making it difficult to determine relevant contextual
information for the retriever.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 6](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-06.png)

![Página PDF 6, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

LLM See, LLM Do
•
7
To preserve the characteristics of code, we decompose each repository into individual code elements. Their
hierarchy, arranged from the highest to the lowest level, consists of modules, classes, methods, functions, and
variables. We store all the declared code elements within each repository individually for quick indexing. Since
our retrieval goal is to identify potential candidate callee functions and then their usage examples, we model
relationships between code elements based on the their accessibility and call dependencies. As we focus on
function-level code generation scenarios, there is no intra-procedural dependencies like data flows for analysis.
Hence, unlike approaches such as GraphCoder [38], we exclusively focus on inter-procedural dependencies
including def-and-use, import and belong_to.
# boto/ec2/volume.py
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
# boto/ec2/connection.py
# boto/ec2/ec2object.py
class EC2Object(object):
  def __init__(self, connection=None):
    ...
Current File
class EC2Connection(AWSQueryConnection):
  ...
 
  def get_all_volumes(self, volume_ids=None, ...): 
    ...
  def get_all_snapshots(self, snapshots_ids, ...): 
    ...
Associated Class
class TaggedEC2Object(EC2Object):
  def __init__(self, connection=None):
    ...
Imported Class
class Volume(TaggedEC2Object):
  def __init__(self, connection=None):
     super(Volume, self).__init__(connection)
     ...
    
  def _update(self, updated): 
    ...
def update(self, validate=False, dry_run=False):
  """
  This function updates the data associated with a 
volume ...
  """
Current Class
Target Function
belong_to
define
use
import
Other Files
Fig. 3. An example of the four relation types in our dependency graph.
To this end, we construct a dependency graph 𝒢= ⟨𝒱, ℰ⟩using an open-source Python static analysis tool
pyan6. Here, 𝒱= {𝑣1, 𝑣2, … , 𝑣𝑚} represents the set of all extracted code elements. ℰ= {𝑒1, 𝑒2, … , 𝑒𝑛} denotes the
collection of all dependency edges. Each edge is represented as a triple (𝑣𝑖, 𝑒, 𝑣𝑗), where 𝑣𝑖, 𝑣𝑗∈𝒱and 𝑒is one of
the four relation types in the following:
• def : A directed edge from 𝑣𝑖to 𝑣𝑗, denoting that 𝑣𝑖defines (i.e., is invoked or referenced by) 𝑣𝑗.
• use: A directed edge from 𝑣𝑖to 𝑣𝑗, denoting that 𝑣𝑖uses (i.e., invokes or references) 𝑣𝑗. Note that the edge
(𝑣𝑗, 𝑢𝑠𝑒, 𝑣𝑖) is exactly the reverse of the def edge (𝑣𝑖, 𝑑𝑒𝑓, 𝑣𝑗). We store both directions of each call dependency
to enable efficient backward traversal.
• import: A directed edge from 𝑣𝑖to 𝑣𝑗, denoting that 𝑣𝑖imports 𝑣𝑗.
• belong_to: A directed edge from 𝑣𝑖to 𝑣𝑗, denoting that 𝑣𝑖belongs to 𝑣𝑗. For instance, a declared method belongs
to its class and its module.
An example of the four relation types included in our dependency graph is shown in Figure 3.
3.3
Logical Context Extraction (LCE)
In this step, we extract all potential callee functions accessible to the target function 𝐹, forming its logical context.
These callees represent the repository-specific APIs that 𝐹could realistically invoke during its implementation.
Our key insight is to use these candidate callees as intermediate cues for the subsequent usage example retrieval,
rather than direct input to the LLM as DraCo [11] does. Based on the constructed dependency graph 𝒢, we extract
three types of candidate callees according to their scopes as follows:
6https://github.com/davidfraser/pyan
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 7](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-07.png)

![Página PDF 7, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

8
•
Zhang et al.
• Intra-file (LC𝑖𝑛𝑓𝑖𝑙𝑒): Global functions declared in the same file of the target function 𝐹and its sibling methods.
• Associated (LC𝑎𝑠𝑠𝑜𝑐): Methods from related classes within the current repository.
• Imported (LC𝑖𝑚𝑝𝑜𝑟𝑡): Functions imported from other modules within the current repository.
The process of the LCE module is illustrated in Algorithm 1. Specifically, given a dependency graph 𝒢and
the signature of the target function 𝐹𝑠𝑖𝑔, LogiCoder first identifies its immediate context, including its class
𝑣𝑐𝑙𝑎𝑠𝑠, module 𝑣𝑚𝑜𝑑𝑢𝑙𝑒, and sibling functions 𝑣𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑠via belong_to edges. The intra-file logical context (LC𝑖𝑛𝑓𝑖𝑙𝑒) is
obtained as the union of 𝑣𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑠and all functions defined within 𝑣𝑚𝑜𝑑𝑢𝑙𝑒. LogiCoder then extracts the associated
logical context (LC𝑎𝑠𝑠𝑜𝑐) by traversing 𝑢𝑠𝑒edges from 𝑣𝑐𝑙𝑎𝑠𝑠and all sibling functions. This identifies code elements,
e.g., classes, that are functionally related to the current context. All functions defined within these associated
entities are then added to the set. To capture cross-module dependencies, the imported logical context (LC𝑖𝑚𝑝𝑜𝑟𝑡)
is obtained by traversing all the 𝑖𝑚𝑝𝑜𝑟𝑡edges from 𝑣𝑚𝑜𝑑𝑢𝑙𝑒and 𝑣𝑐𝑙𝑎𝑠𝑠and merging all functions defined within
the corresponding imported modules or classes. The final logical context LC is the union of these three sets.
Throughout this process, we ensure the target function itself is excluded to prevent data leakage. Note that the
LCE module is designed as an intermediate stage. Its primary objective is to retrieve the candidate callees as
completely as possible to ensure no critical dependencies are missed during the initial collection. While this
strategy captures a broad set of candidates (including irrelevant ones), the potential noise is eliminated in the
subsequent modules.
Algorithm 1: Logical Context Extraction Process of LogiCoder
Input: Dependency graph 𝒢= ⟨𝒱, ℰ⟩and the signature of the target function 𝐹𝑠𝑖𝑔.
Output: Logical Context LC.
1 𝑣𝑐𝑙𝑎𝑠𝑠←GetParentClass(𝐹𝑠𝑖𝑔);
2 𝑣𝑚𝑜𝑑𝑢𝑙𝑒←GetParentModule(𝐹𝑠𝑖𝑔);
3 𝑣𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑠←GetChildFuncs(𝑣𝑐𝑙𝑎𝑠𝑠);
// Step 1: Get intra-file candidates.
4 LC𝑖𝑛𝑓𝑖𝑙𝑒←𝑣𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑠∪GetChildFuncs(𝑣𝑚𝑜𝑑𝑢𝑙𝑒);
5 for 𝑒𝑘= (𝑣𝑖, 𝑒𝑡𝑦𝑝𝑒, 𝑣𝑗) ∈ℰdo
// Step 2: Get associated candidates.
6
if 𝑣𝑖∈{𝑣𝑐𝑙𝑎𝑠𝑠} ∪𝑣𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑠and 𝑒𝑡𝑦𝑝𝑒= 𝑢𝑠𝑒then
7
LC𝑎𝑠𝑠𝑜𝑐←LC𝑎𝑠𝑠𝑜𝑐∪GetChildFuncs(𝑣𝑗);
8
end
// Step 3: Get imported candidates.
9
if 𝑣𝑖= 𝑣𝑚𝑜𝑑𝑢𝑙𝑒and 𝑒𝑡𝑦𝑝𝑒= 𝑖𝑚𝑝𝑜𝑟𝑡then
10
LC𝑖𝑚𝑝𝑜𝑟𝑡←LC𝑖𝑚𝑝𝑜𝑟𝑡∪GetChildFuncs(𝑣𝑗);
11
end
12 end
13 LC ←LC𝑖𝑛𝑓𝑖𝑙𝑒∪LC𝑎𝑠𝑠𝑜𝑐∪LC𝑖𝑚𝑝𝑜𝑟𝑡;
14 return LC;
3.4
Usage Example Retrieval (UER)
After identifying all candidate callee functions as logical context, we trace their call relationships to locate their
callers. For the code generation task, these callers serve as usage examples of repository-specific knowledge, which
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 8](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-08.png)

![Página PDF 8, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

LLM See, LLM Do
•
9
may exhibit similar usage patterns as the target function, e.g., similar parameter configurations or application
scenarios. Prior studies also suggest that similar usage examples are semantically related [1, 3]. Thus, these
examples could help LLMs to align their implementations with the established practices of the repository during
the subsequent code generation process. Specifically, LogiCoder takes the dependency graph 𝒢, logical context
LC and the signature of the target function 𝐹𝑠𝑖𝑔as input. It first traverses each candidate callee in LC to retrieve
its caller functions as usage examples. However, the two-phase tracing, i.e., LCE and UER, may result in an
overly broad range of retrieved results. To filter out false positives and irrelevant examples, LogiCoder performs
a similarity-based ranking for all usage examples. In this step, adjacent context is utilized to complement the
semantic information. LogiCoder extracts the context of the target function and each usage example and
computes token-level similarity using an embedding model. Finally, the examples are merged and ranked based
on their contextual similarity scores, producing a list of top usage examples as retrieved results. The algorithm is
described in Algorithm 2:
Algorithm 2: Usage Example Retrieval Process of LogiCoder
Input: Dependency graph 𝒢= ⟨𝒱, ℰ⟩, logical context LC and the signature of the target function 𝐹𝑠𝑖𝑔.
Output: Top usage examples UE𝑡𝑜𝑝.
1 𝑆←∅;
2 for 𝑙𝑐∈LC do
3
for 𝑒𝑘= (𝑣𝑖, 𝑒𝑡𝑦𝑝𝑒, 𝑣𝑗) ∈ℰdo
// Step 1: Trace define edges for usage examples.
4
if 𝑣𝑖= 𝑙𝑐and 𝑒𝑡𝑦𝑝𝑒= 𝑑𝑒𝑓and VType(𝑣𝑗) = 𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛and Namespace(𝑣𝑗) ≠Namespace(𝐹𝑠𝑖𝑔) then
// Step 2: Calculate context similarity between the target function and the usage example.
5
𝑐𝑡𝑥_𝑠𝑖𝑚←CalCtxSim(𝐹𝑠𝑖𝑔, 𝑣𝑗);
6
𝑆←𝑆∪{(𝑣𝑗, 𝑐𝑡𝑥_𝑠𝑖𝑚)};
7
end
8
end
9 end
// Step 3: Rank usage examples by context similarity.
10 UE𝑡𝑜𝑝←GetTopKByValue(𝑆);
11 return UE𝑡𝑜𝑝;
3.5
Semantic Search Fusion (SSF)
While our retrieval based on logical context identifies usage examples with high context similarity, it has a
blind spot. Specifically, it operates independently of the semantics of task requirements, potentially retrieving
functionally irrelevant usage examples. This issue will be exacerbated particularly when no candidate callees or
their usage examples exist in the repository. To address this gap, we integrate semantic similarity search as a
complementary retrieval strategy. The reason for this fusion is two-fold: (1) Semantic search directly measures the
similarity between natural language requirement and code snippets within the repository. This provides a crucial
filtering mechanism to eliminate contextually similar but semantically distant usage examples, compensating for
the requirement-agnostic nature of our retrieval based on logical context. (2) Semantic search serves as a fallback
mechanism to enhance the robustness of our retrieval. By enabling direct semantic search across the entire
repository, it ensures retrieval capability when no direct “callee-caller” patterns exist. To effectively integrate
the semantic search with our retrieved usage examples, we employ Reciprocal Rank Fusion (RRF) [12] as our
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 9](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-09.png)

![Página PDF 9, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

10
•
Zhang et al.
Algorithm 3: Semantic Search Fusion Process of LogiCoder
Input: Dependency graph 𝒢= ⟨𝒱, ℰ⟩, top usage examples UE𝑡𝑜𝑝, the task requirement Req and the
signature 𝐹𝑠𝑖𝑔of the target function.
Output: Top re-ranked code examples RE𝑡𝑜𝑝.
// Step 1: Get top-k semantically similar functions and merge with selected usage examples.
1 𝑆←∅;
2 𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘←∅;
3 for 𝑣∈𝒱do
4
if VType(𝑣) = 𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛and Namespace(𝑣) ≠Namespace(𝐹𝑠𝑖𝑔) then
5
𝑠𝑒𝑚_𝑠𝑖𝑚←CalSemSim(Req , 𝑣);
6
𝑆←𝑆∪{(𝑣, 𝑠𝑒𝑚_𝑠𝑖𝑚)};
// Directly add selected usage examples to the final semantic similarity rank list.
7
if 𝑣∈UE𝑡𝑜𝑝.keys then
8
𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘←𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘∪{(𝑣, 𝑠𝑒𝑚_𝑠𝑖𝑚)};
9
end
10
end
11 end
12 𝑇𝑜𝑝𝑆𝑒𝑚←GetTopKByValue(𝑆);
13 𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘←SortByValue(𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘∪𝑇𝑜𝑝𝑆𝑒𝑚);
// Step 2: Get context similarity for added functions and merge with selected usage examples.
14 𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘←UE𝑡𝑜𝑝;
15 for 𝑣∈𝑇𝑜𝑝𝑆𝑒𝑚.keys do
16
𝑐𝑡𝑥_𝑠𝑖𝑚←CalCtxSim(𝐹𝑠𝑖𝑔, 𝑣);
17
𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘←𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘∪{(𝑣, 𝑐𝑡𝑥_𝑠𝑖𝑚)};
18 end
19 𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘←SortByValue(𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘);
// Step 3: Re-rank all functions by reciprocal rank fusion.
20 𝑆←∅;
21 for 𝑣∈𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘.keys do
22
𝑅𝑅𝐹𝑠𝑐𝑜𝑟𝑒←RRF(𝑣, 𝑆𝑒𝑚𝑆𝑖𝑚𝑅𝑎𝑛𝑘, 𝐶𝑡𝑥𝑆𝑖𝑚𝑅𝑎𝑛𝑘);
23
𝑆←𝑆∪{(𝑣, 𝑅𝑅𝐹𝑠𝑐𝑜𝑟𝑒)};
24 end
25 RE𝑡𝑜𝑝←GetTopKByValue(𝑆);
26 return RE𝑡𝑜𝑝;
re-ranking technique. RRF integrates ranking results from multiple retrieval systems by considering the position
of each item rather than numerical scores. This approach has been validated as reliable in prior studies [9, 12, 22].
The calculation of RRF score for a candidate function 𝑣is as follows:
𝑅𝑅𝐹𝑠𝑐𝑜𝑟𝑒(𝑣) = ∑
𝑟∈𝑅
1
𝑘+ 𝑟(𝑣)
(2)
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 10](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-10.png)

![Página PDF 10, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

LLM See, LLM Do
•
11
where 𝑅represents the set of rankings (semantic similarity and context similarity), 𝑟(𝑣) denotes the rank of
function 𝑣in ranking 𝑟, and 𝑘is a hyperparameter that mitigates the impact of high-ranking outliers. In our paper,
we set 𝑘= 60 by following the established practices [9, 12]. The overall process of semantic search fusion is
described in Algorithm 3.
3.6
Augmented Generation
Based on the retrieval results, LogiCoder constructs a prompt to guide the LLM in generating the target
function. Following established practices [15, 38, 63], our prompt integrates both the retrieved context across the
whole repository and the local context within the target file, as both have been shown to be essential for code
generation [63]. As illustrated in Figure 4, our prompt is structured into three key components:
Please complete the `update` function based on the relevant snippets and 
the contexts above the function.
# Here are some relevant code snippets from the repository to help you 
complete the target function:
# --------------------------------------------------
# The below function `update` can be found in:
# boto/ec2/snapshot.py
# --------------------------------------------------
# The code of `update` is:
#   def update(self, validate=False, dry_run=False):
#     rs = self.connection.get_all_snapshots([self.id], dry_run=dry_run)
#     if len(rs) > 0:
#       self._update(rs[0])
#     elif validate:
#       raise ValueError('%s is not a valid Snapshot ID' % self.id)
#     return self.progress
# --------------------------------------------------
# ...
# --------------------------------------------------
# The contexts above the `update` function are:
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
class Volume(TaggedEC2Object):
  def __init__(self, connection=None):
    ...
  def ...
  
  def _update(self, updated):
    self.__dict__.update(updated.__dict__)
# The `update` function to complete is a method of `Volume` class, which is 
as follows:
  def update(self, validate=False, dry_run=False):
    """
    This function updates ...
    Input-Output Arguments:
    ...
    """
Intra-file Context
Target Function
Retrieved Context
Fig. 4. An example of the prompt used in LogiCoder.
• Retrieved Examples: The first part includes a curated list of code examples retrieved from the repository. In
line with prior work [38, 63], each example is annotated with its source file path. Since the order of examples
can significantly influence LLMs’ performance [18], we mitigate this potential issue by constructing multiple
prompts with different orders (i.e., ascending and descending by similarity) in our generation.
• Intra-File Context: The second part includes the code from the target file that precedes the function to
be generated. This provides the LLM with the necessary immediate context, such as imported modules and
previously defined classes or functions.
• Function to Be Generated: The third part specifies the code generation task. It includes the signature of the
target function, which precisely defines the task requirement, its inputs and expected outputs.
4
Experimental Setup
To evaluate the effectiveness of LogiCoder, we address the following six research questions (RQs):
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 11](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-11.png)

![Página PDF 11, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

12
•
Zhang et al.
• RQ1 (Overall Performance): How does LogiCoder perform compared with other methods on repository-
aware code generation tasks?
• RQ2 (Effectiveness of LCE): How does logical context extraction (LCE) enhance LogiCoder’s performance
on repository-aware code generation tasks?
• RQ3 (Effectiveness of UER): How does usage example retrieval (UER) enhance LogiCoder’s performance
on repository-aware code generation tasks?
• RQ4 (Effectiveness of SSF): How does semantic search fusion (SSF) enhance LogiCoder’s performance on
repository-aware code generation tasks?
• RQ5 (Generalization Ability): How does LogiCoder perform on code generation tasks with mixed depen-
dency types?
• RQ6 (Analysis of Retrieval Context Length): How does the length of retrieval context influence LogiCoder
on repository-aware code generation tasks?
4.1
Dataset
To evaluate the effectiveness of LogiCoder, we primarily use the DevEval [31] benchmark in our study, which
includes 1,825 Python function-level code generation tasks from 115 real-world repositories. Our selection of this
benchmark for our core evaluation is based on three essential criteria, including task granularity, dependency
complexity and evaluation robustness. Firstly, we focus on the repository-aware, function-level code generation
task, which requires LLMs to generate complete functional logic from scratch. Existing benchmarks like Cross-
CodeEval [15] mainly focus on fine-grained (API-level or line-level) code completion tasks. Such tasks operate in
an “acceleration mode” [4], where developers trigger auto-completion for known implementations. The immediate
local context within the incomplete function will provide significant hints for implementation. Nevertheless,
function-level tasks require LLMs to generate substantially larger code snippets, e.g., tasks in DevEval are on
average 7.7× longer than those in CrossCodeEval. Secondly, to effectively evaluate repository-aware RAG ap-
proaches, a benchmark should rely on massive, non-local repository-specific knowledge. While CoderEval [60] is
a high quality benchmark, approximately 90% of its Python instances are file-runnable, leaving only 23 instances
that explicitly require cross-file dependencies. This sparse dependency distribution is insufficient for evaluation
of retrieval capabilities. However, DevEval offers substantially higher dependency complexity. Therefore, for our
primary experiments (RQ1-RQ4), we filter the DevEval benchmark to include only tasks that involve at least one
cross-file call. This results in a refined and challenging dataset of 471 tasks across 67 repositories, which we denote
as DevEval-cf . Thirdly, the functional correctness of generated code should be evaluated with robust metrics.
Prior work demonstrates that similarity-based metrics, such as Edit Similarity and CodeBLEU, are unreliable
measures of true functional equivalence [33]. Such metrics are frequently used in repository-level benchmarks,
e.g., CrossCodeEval [15], RepoEval7 [63], etc.). To address this, DevEval provides comprehensive test suites for
execution-based evaluation. Furthermore, it introduces a Recall@𝑘metric, which allows us to directly measures
LLMs’ ability to utilize the correct repository dependencies.
For the above reasons, the majority of our evaluation is conducted on the DevEval-cf subset, a targeted
diagnostic setting that emphasizes the cross-file retrieval capability. Hence, it is not representative of the full
distribution of repository-aware code generation tasks. To validate LogiCoder’s robustness and generalization
ability in real-world scenarios (where dependency types are mixed and unknown in advance), we subsequently
evaluate our approach against the full DevEval benchmark and the Python subset of the CoderEval benchmark
in our generalization study (RQ5).
7While the data for function body completion in RepoEval is available, the official replication package does not include the necessary code for
executing and evaluating these specific tasks.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 12](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-12.png)

![Página PDF 12, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

LLM See, LLM Do
•
13
4.2
Baselines
As this paper focuses on enhancing LLMs’ capabilities on the repository-aware code generation task, we select
two categories of baselines: (1) approaches without RAG and (2) RAG approaches.
4.2.1
Approaches without RAG. The baselines without RAG utilize LLMs’ own generalization ability to generate
target functions without any retrieval from code repositories. We select four representative approaches in the
following:
• Direct: This approach merely uses the signature of target function 𝐹𝑠𝑖𝑔as the input of LLMs to generate the
code. It reflects the performance of LLMs without any repository-specific context.
• In-File Context: This approach uses the local file context above the target function to trigger LLMs’ completion
ability. This simulates the scenarios where developers continue to write the function within the current file. It
reflects the performance of LLMs without any cross-file or non-local repository-specific context.
• CoT: This approach leverages chain-of-thoughts [53] (CoT) to generate the target function. We craft a few-shot
CoT prompt (as shown in Figure 13 in Appendix A.) for LLMs to generate intermediate steps and then the
corresponding code. Both the local file context and the signature of target function 𝐹𝑠𝑖𝑔are provided.
• Self-Planning [28]: This approach first asks LLMs to conduct a separate planning phase to generate a stepwise
plan based on the signature of target function 𝐹𝑠𝑖𝑔. Then LLMs follow the plan to generate target code in the
implementation phase. The local file context and the signature of target function are provided in both phases.
Its prompts are shown in Figure 14 in Appendix A.
4.2.2
RAG Approaches. To evaluate the effectiveness of the new RAG pattern in LogiCoder, we compare it with
nine established RAG baselines for repository-aware code generation. For a fair comparison, all RAG approaches
(except CodeAgent) use the identical prompt structure illustrated in Figure 4.
• Sparse Retrieval: This approach constructs a query with the target function’s signature and requirement and
uses BM25 algorithm to retrieve similar functions from the repository.
• Dense Retrieval: This approach first encodes all functions within the repository as dense vectors, then encodes
the target function’s signature and requirement to retrieve similar functions via cosine similarity.
• Vanilla RAG: This approach chunks the whole repository into fragments via sliding window algorithm and
uses a fixed-size context window that precedes the target function to retrieve similar code snippets.
• Shifted RAG: This approach is similar to Vanilla RAG, but it shifts a few lines down for each retrieved snippet
and uses the subsequent code to augment LLM generation. It is called fragment alignment and has also been
demonstrated to be effective in ReACC [40].
• RepoCoder [63]: RepoCoder is an iterative RAG approach that also leverages preceding context for repository-
level retrieval. After the first iteration, RepoCoder combines preceding context with the top lines of generated
code as the new query for next retrieval.
• DraCo [11]: This approach is a dataflow-guided RAG approach which first constructs a repository-specific
context graph and retrieves relevant background knowledge through fine-grained import information.
• GraphCoder [38]: This approach is a graph-based RAG approach which constructs an intra-procedural Code
Context Graph (CCG) to capture control flow, data- and control-dependence between statements. It employs a
coarse-to-fine retrieval process to locate contextually similar code snippets.
• RepoScope [39]: This approach leverages both structural information and similarity-based retrieval to provide
a multi-view context. It leverages call chain prediction to improve the identification of callees in the target
function.
• CodeAgent [64]: This approach is a coding agent specifically designed for the code generation task. It equips
LLMs with various tools to iteratively gather repository-specific knowledge and refines its output before
returning the final code.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 13](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-13.png)

![Página PDF 13, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-13.png)


<!-- PDF page 14 -->

## Página PDF 14

14
•
Zhang et al.
4.3
Evaluation Metrics
We evaluate LLM performance on the repository-aware code generation task using two metrics:
• Pass@𝑘: For function-level code generation, we are concerned about the functional correctness of the generated
code. Pass@𝑘is an execution-based metric that estimates the likelihood of a task being solved in 𝑘attempts
based on unit test execution, which can be calculated by:
Pass@𝑘= 𝔼Task [1 −
(𝑛−𝑐
𝑘)
(𝑛
𝑘)
]
(3)
where 𝑛is the total number of samples, 𝑐is the number of correct samples that pass all the tests and 𝑘represents
the number of attempts considered.
• Recall@𝑘: For repository-aware code generation, we expect LLMs to use dependencies from the local repository
instead of implementing them from scratch or using external libraries. As introduced in the original DevEval
benchmark [31], Recall@𝑘measures the recall of ground-truth dependencies 𝐷𝑔𝑡(referenced in the canonical
solution) in the LLM-generated code. It could be calculated by:
recall@𝑘= 𝔼Task [ max
𝑖=1…𝑘
∣𝐷𝑖∩𝐷𝑔𝑡∣
∣𝐷𝑔𝑡∣
]
(4)
where 𝐷𝑖represents the dependencies extracted from the 𝑖-th generation, and 𝑘is the total number of generated
results.
Following prior work [31], we set 𝑘= 1 and use the greedy decoding (𝑡𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑒= 0) to calculate Pass@1 and
Recall@1. This selection is computationally efficient and reflects real-world developer behavior, as studies show
developers typically consider only the first suggestion from AI coding assistants [4]. Considering LLM sensitivity
to the order of in-context examples, we follow a prior study [18] to report the average Pass@1 and Recall@1
scores across prompts with different example orders. To quantify the stability of each approach, we also report
its Coefficient of Variation (CV) [6], defined as 𝜎/𝜇, where 𝜎is the standard deviation and 𝜇is the mean. A lower
CV value indicates greater robustness to example ordering.
4.4
Implementation Details
Retrieval. To prevent potential data leakage from exact duplicates, we use a file-hashing technique to identify
and exclude any files within the repository that are identical to the source file of the target function. This ensures
a realistic evaluation of LLMs’ generation ability by preventing them from accessing the duplicate solution that
should not exist. For RAG baselines, Sparse Retrieval uses BM25 algorithm to perform retrieval while Dense
Retrieval, Vanilla RAG and Shifted RAG use a state-of-the-art code embedding model, UniXcoder [20], to convert
text and code into dense vectors. Regarding the hyperparameters of repository chunking for Vanilla RAG, Shifted
RAG and RepoCoder, we adopt the ones suggested by Zhang et al. [63]. Specifically, we chunk the source code
files in each repository into snippets with the window size of 50 lines and the sliding size of 10 lines. For
RepoCoder, we follow its established practice by using bag-of-words as the tokenizer and calculating similarity
with Jaccard Index [26]. To adapt GraphCoder for code generation tasks, we use its intra-file context as the initial
code completion context and slice it to form the query Code Context Graph (query CCG). For CodeAgent, we
implement the agent using the LangChain8 framework, equipping the LLM with three external tools: a Website
Search tool, a Code Symbol Navigation tool (to traverse definitions and references within the repository), and a
Format Checker tool. The maximum iteration is set to 15 to control the inference cost. For LogiCoder, we use the
simple bag-of-words and Jaccard Index to calculate the context similarity between the target function and usage
8https://www.langchain.com
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 14](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-14.png)

![Página PDF 14, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-14.png)


<!-- PDF page 15 -->

## Página PDF 15

LLM See, LLM Do
•
15
Table 1. Pass@1 and Its CV of LogiCoder and Various Baselines Based on Five LLMs Across the DevEval-cf Benchmark.
Method
Kimi-K2
DeepSeek-
V3
GPT-4o
Qwen2.5
Llama-3.1
Direct
10.40
5.73
9.13
3.40
1.70
CoT
34.61
29.30
31.00
24.20
9.55
Self-Planning
31.00
30.36
31.00
21.66
13.80
In-File Context
28.24
31.63
31.42
21.02
12.95
Sparse Retrieval
34.18 (0.02)
32.38 (0.01)
32.91 (0.03)
23.47 (0.04)
14.33 (0.02)
Dense Retrieval
33.75 (0.00)
32.59 (0.02)
32.22 (0.00)
22.62 (0.00)
12.85 (0.04)
Vanilla RAG
31.11 (0.04)
32.59 (0.02)
33.86 (0.02)
20.80 (0.01)
20.07 (0.01)
Shifted RAG
33.55 (0.01)
33.76 (0.03)
35.25 (0.01)
20.91 (0.04)
22.08 (0.02)
RepoCoder
33.55 (0.03)
35.14 (0.01)
36.20 (0.01)
22.19 (0.02)
21.77 (0.00)
DraCo
29.30 (0.01)
31.32 (0.02)
33.01 (0.00)
22.91 (0.06)
14.23 (0.03)
GraphCoder
24.62 (0.02)
34.50 (0.00)
35.14 (0.03)
16.45 (0.06)
14.43 (0.03)
RepoScope
35.03*
25.69*
26.33
15.07
12.74
CodeAgent
-
27.81
33.41
24.63
13.38
LogiCoder
44.58 (0.01)
41.83 (0.02)
40.55 (0.02)
29.09 (0.00)
25.16 (0.01)
Relative
27.26% ↑
19.04% ↑
12.02% ↑
18.11% ↑
13.95% ↑
*Due to the original models being taken offline, RepoScope is evaluated on their more recent checkpoints, i.e., Kimi-K2-250905
and DeepSeek-V3-250324.
examples. Then we use UniXcoder as the embedding model for Semantic Search Fusion module. To ensure a fair
comparison among RAG approaches, we set the maximum retrieval context to 3,000 tokens and the maximum
retrieved examples to 10. The influence of retrieval context length on LogiCoder will be further analyzed in
Section 5.6.
Generation. To comprehensively evaluate our approach, we select five widely-used LLMs as our back-
bone models for evaluation, including Kimi-K2 [49], DeepSeek-V3 [13], GPT-4o9, Qwen2.5-Coder-14B [25] and
Llama-3.1-8B10. This selection provides a broad coverage across multiple sources, model sizes (from 8B to 1T),
specializations (general and code-specific), and architectures (dense and mixture-of-experts). We access Kimi-K2,
DeepSeek-V3 and GPT-4o via their official APIs, whose checkpoints are kimi-k2-250711, deepseek-v3-241226 and
gpt-4o-2024-11-20, respectively. For Qwen2.5-Coder-14B and Llama-3.1-8B, we deploy them on a Ubuntu 22.04
server with four GeForce RTX 4090-24G GPUs.
5
Evaluation Results
5.1
RQ1: Overall Performance
Table 1 and Table 2 present the evaluation results of LogiCoder and various baselines on five LLMs. For
each RAG approach, we report its average Pass@1 and Recall@1 scores and include the CV values in brackets.
LogiCoder consistently achieves the best Pass@1 and Recall@1 scores across all models, demonstrating its robust
improvement over existing baselines. Notably, when evaluated on the Kimi-K2 model, LogiCoder achieves a new
state-of-the-art Pass@1 of 44.58% and a Recall@1 of 46.39%. It outperforms the best-performing baseline with
9https://platform.openai.com/docs/models/gpt-4o
10https://huggingface.co/meta-llama/Llama-3.1-8B
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 15](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-15.png)

![Página PDF 15, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-15.png)


<!-- PDF page 16 -->

## Página PDF 16

16
•
Zhang et al.
Table 2. Recall@1 and Its CV of LogiCoder and Various Baselines Based on Five LLMs Across the DevEval-cf Benchmark.
Method
Kimi-K2
DeepSeek-
V3
GPT-4o
Qwen2.5
Llama-3.1
Direct
13.99
10.42
14.89
11.60
10.49
CoT
39.56
36.02
38.48
36.04
31.75
Self-Planning
38.35
36.18
39.13
34.86
35.38
In-File Context
36.20
37.89
40.16
32.93
35.84
Sparse Retrieval
40.25 (0.00)
39.42 (0.03)
40.84 (0.00)
37.64 (0.01)
36.89 (0.01)
Dense Retrieval
39.99 (0.00)
39.94 (0.03)
41.25 (0.00)
36.56 (0.00)
37.66 (0.01)
Vanilla RAG
39.44 (0.00)
39.53 (0.03)
41.09 (0.00)
34.66 (0.00)
36.33 (0.00)
Shifted RAG
40.39 (0.01)
39.83 (0.03)
41.66 (0.00)
35.08 (0.03)
37.83 (0.02)
RepoCoder
40.44 (0.01)
40.43 (0.02)
41.59 (0.00)
34.83 (0.00)
37.78 (0.00)
DraCo
39.08 (0.00)
40.77 (0.01)
42.44 (0.01)
36.57 (0.03)
36.10 (0.01)
GraphCoder
40.24 (0.02)
41.59 (0.00)
41.88 (0.01)
38.45 (0.00)
37.30 (0.00)
RepoScope
40.31*
34.05*
36.95
31.78
31.34
CodeAgent
-
31.65
39.74
34.99
37.43
LogiCoder
46.39 (0.01)
46.11 (0.01)
46.62 (0.00)
42.86 (0.00)
42.17 (0.00)
Relative
14.71% ↑
10.87% ↑
9.85% ↑
11.47% ↑
11.47% ↑
*Due to the original models being taken offline, RepoScope is evaluated on their more recent checkpoints, i.e., Kimi-K2-250905
and DeepSeek-V3-250324.
relative improvements of 27.26% in Pass@1 and 14.71% in Recall@1. These results demonstrate that LogiCoder
helps LLMs appropriately integrate the required dependencies to generate functionally correct code.
Among all baselines, RepoCoder generally achieves the most competitive Pass@1, e.g., 35.14% on DeepSeek-V3
and 36.20% on GPT-4o. This advantage likely stems from its iterative retrieval strategy, which leverages generated
implementation context from the previous generation. However, LogiCoder still surpasses it by at least 12%,
indicating that purely semantic retrieval remains insufficient for code generation tasks with complex dependencies.
We observe that DraCo and GraphCoder achieve Recall@1 scores up to 42.44% and 41.88% respectively on GPT-4o,
but they underperform most of the baselines in Pass@1. This suggests that while DraCo and GraphCoder can
retrieve relevant code entities, they are less effective in guiding LLMs to successfully use them in the final
generation. As a recent multi-view approach that incorporates both structural and similarity-based contexts,
RepoScope achieves the highest baseline Pass@1 on Kimi-K2 (35.03%). However, its advantage is unstable across
LLMs. Regarding CodeAgent, its performance lags behind that of LogiCoder by a large margin. It achieves the best
Pass@1 (24.63%) among baselines on Qwen2.5-Coder. However, we notice that when evaluated on the powerful
Kimi-K2 model, CodeAgent falls into an infinite tool-calling loop. This suggests that its multi-turn exploration
can be inefficient in complex repositories. In contrast, LogiCoder’s one-pass retrieval can extract relevant
repository-specific knowledge deterministically, which is more accurate, stable and economical. Generally, RAG
approaches outperform non-RAG baselines. Interestingly, CoT prompting achieves high Pass@1 scores among all
baselines on Kimi-K2. This indicates that the training of this LLM enables it to generate correct code independently
through an internal reasoning process.
Regarding the robustness to the example order, RAG approaches maintain stable performance across most
LLMs. We only observe slightly higher CV values (0.06) on Qwen2.5-Coder. Among all evaluated approaches,
LogiCoder exhibits the best stability against prompt variations, maintaining a maximum CV of only 0.02. To
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 16](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-16.png)

![Página PDF 16, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-16.png)


<!-- PDF page 17 -->

## Página PDF 17

LLM See, LLM Do
•
17
Table 3. Performance of LogiCoder with Different Example Orders.
Method
Kimi-K2
DeepSeek-V3
GPT-4o
Qwen2.5
Llama-3.1
P@1
R@1
P@1
R@1
P@1
R@1
P@1
R@1
P@1
R@1
LogiCoderasc
44.16
46.69
41.19
46.35
39.92
46.57
29.09
42.65
24.84
42.14
LogiCoderdesc
45.01
46.10
42.46
45.86
41.19
46.68
29.09
43.07
25.48
42.20
further understand the impact of the example order on LogiCoder, we detail its performance under two different
ordering configurations (ascending and descending by fused similarity score) in Table 3. The results indicate that
the descending order consistently outperforms the ascending order in the Pass@1 metric across all five LLMs.
For Recall@1, Kimi-K2 and DeepSeek-V3 show a slight preference for the ascending order, while the other three
LLMs perform better with the descending order. Apart from this, we analyze the composition of LogiCoder’s
retrieved knowledge types within these prompts. On average, a prompt contains slightly more examples retrieved
by logical context than semantic ones (4.96 vs. 4.55). Furthermore, logical examples achieve higher similarity
scores, with an average rank of 5.04 for logical vs. 5.68 for semantic. The result indicates that while placing logical
examples first in the prompt is beneficial, LogiCoder is robust against variations in example order within LLM
prompts.
We further investigate the differences between LogiCoder and representative baselines by analyzing the
overlap of their successfully generated code. Figure 5 presents two Venn diagrams comparing the sets of correctly
resolved tasks using LogiCoder and representative baselines on the two best-performing LLMs. Most importantly,
LogiCoder generates the highest number of unique tasks that all other baselines fail to solve. Specifically, it
successfully generates correct code for an additional 32 unique tasks on Kimi-K2 and 22 unique tasks on DeepSeek-
V3. While different RAG approaches (RepoCoder and DraCo) have their own distinct advantages, the majority of
their solved tasks are covered by LogiCoder. This validates that LogiCoder’s fused retrieval can capture the
strengths of both approaches. On DeepSeek-V3, CodeAgent successfully generates 18 unique tasks. However,
it misses a massive intersection of 38 tasks solved by other approaches. The non-RAG baseline, CoT, can also
solve a unique set of tasks (10 on Kimi-K2 and 6 on DeepSeek-V3) where all RAG approaches fail. We will
qualitatively analyze the success and failure cases of LogiCoder in Section 6.1 to better understand its strengths
and limitations.
Finding 1: LogiCoder outperforms all baseline approaches across all five LLMs achieving relative improve-
ments of up to 27.26% in Pass@1 and 14.71% in Recall@1. This shows that the context retrieved by LogiCoder
can effectively enhance LLM code generation. Furthermore, LogiCoder exhibits the greatest robustness
against variations in example order within LLM prompts.
5.2
RQ2: Effectiveness of LCE
As mentioned in Section 3.3, LogiCoder extracts candidate callee functions from three sources: 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒, 𝐿𝐶𝑎𝑠𝑠𝑜𝑐,
and 𝐿𝐶𝑖𝑚𝑝𝑜𝑟𝑡. To evaluate the contribution of these LCE components to subsequent retrieval and code generation,
we conduct an ablation study on the two best-performing LLMs, Kimi-K2 and DeepSeek-V3. The ablated LCE
variants are denoted as w/o in-file, w/o assoc and w/o import. To better measure retrieval performance, we introduce
two additional metrics for evaluation:
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 17](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-17.png)

![Página PDF 17, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-17.png)


<!-- PDF page 18 -->

## Página PDF 18

18
•
Zhang et al.
32 
2 
3 
5 
15 
2 
22 
10 
13 
3 
19 
6 
23 
4 
85 
CoT
RepoCoder
DraCo
LogiCoder
(a) Kimi-K2
22 
18 
15 
1 
7 
1 
0 
5 
13 
1 
5 
4 
6 
0 
9 
6 
1 
2 
2 
2 
6 
1 
4 
1 
2 
0 
7 
0 
38 
3 
63 
CoT
RepoCoder
DraCo
CodeAgent
LogiCoder
(b) DeepSeek-V3
Fig. 5. The Venn diagram of correctly generated code for LogiCoder and representative baselines on Kimi-K2 and DeepSeek-
V3.
• Callee Coverage: The proportion of required callee functions for the target method that are present in the
extracted logical context. This measures the completeness of the candidate callee set provided by the three
components of LogiCoder.
• Recall𝑓@𝑘: This metric adapts the standard Recall@𝑘to measure the recall of the true callee functions within
the top-𝑘retrieved usage examples. It indicates the relevance of the retrieved examples. Due to the limitation
of retrieval context length, Recall𝑓@𝑘with a smaller 𝑘is more influential as they are always included in LLM
prompts.
Table 4 shows the impact of different components in LCE on the identification performance. All three compo-
nents are necessary because removing each of them leads to a substantial decrease in all metrics. Specifically,
LogiCoder with all components achieves a Callee Coverage of 97.36% and a Recall𝑓@1 of 40.25%. Regarding
the contribution, the removal of 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒(intra-file candidates) has the greatest impact on the initial candidate
set, which drops the Callee Coverage to 56.90%. Removing 𝐿𝐶𝑖𝑚𝑝𝑜𝑟𝑡(imported candidates) also causes a marked
decrease, with coverage falling to 61.44%. In addition, the removal of the 𝐿𝐶𝑖𝑚𝑝𝑜𝑟𝑡component proves to be the
most detrimental to the relevance of retrieved examples. It causes the largest drop in Recall𝑓@𝑘, especially when
𝑘= 1. Recall𝑓@1 falls from 40.25% to 15.52%, indicating a relative decrease of over 60%. The removal of 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒
and 𝐿𝐶𝑎𝑠𝑠𝑜𝑐(associated candidates) also substantially impacts the retrieval, leading to a Recall𝑓@1 of 24.19% and
27.48%, respectively. These results indicate the critical importance of incorporating all accessible logical context
to ensure a complete and relevant retrieval.
Table 5 illustrates the impact of each LCE component on the final code generation performance, measured by
Pass@1 and Recall@1 on the two best-performing backbone models, i.e., Kimi-K2 and DeepSeek-V3. Removing
any key component leads to performance degradation in both metrics for both LLMs. The most substantial
influence on functional correctness is observed when removing 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒with DeepSeek-V3, which results in a
relative decrease of 9.16% in Pass@1. The Recall@1 metric also degrades for all variants. For Kimi-K2, the removal
of associated candidates 𝐿𝐶𝑎𝑠𝑠𝑜𝑐causes the largest relative drop of 2.89%, while it is also the most influential for
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 18](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-18.png)

![Página PDF 18, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-18.png)


<!-- PDF page 19 -->

## Página PDF 19

LLM See, LLM Do
•
19
Table 4. The Ablation Study of Key Components in LCE for Callee Extraction
Method
Callee
Coverage
Recall𝑓@1
Recall𝑓@3
Recall𝑓@5
Recall𝑓@10
LogiCoder
97.36%
40.25%
54.78%
61.19%
71.14%
w/o in-file
56.90%
24.19%
31.63%
36.53%
41.94%
w/o assoc
88.18%
27.48%
40.76%
46.04%
55.26%
w/o import
61.44%
15.52%
27.14%
30.64%
38.57%
Table 5. Pass@1 and Recall@1 of LogiCoder and Its LCE Variants Based on Two Best-Performing LLMs Across the DevEval-cf
Benchmark.
Method
Kimi-K2
DeepSeek-V3
Pass@1 (CV)
Recall@1 (CV)
Pass@1 (CV)
Recall@1 (CV)
LogiCoder
44.58 (0.01)
46.39 (0.01)
41.83 (0.01)
46.11 (0.01)
w/o in-file
41.40 (0.02) 7.13% ↓
45.59 (0.01) 1.72% ↓
38.00 (0.01) 9.16% ↓
45.06 (0.01) 2.28% ↓
w/o assoc
41.50 (0.00) 6.91% ↓
45.05 (0.00) 2.89% ↓
39.39 (0.02) 5.83% ↓
44.79 (0.00) 2.86% ↓
w/o import
41.50 (0.00) 6.91% ↓
45.53 (0.00) 1.85% ↓
39.59 (0.01) 5.36% ↓
44.82 (0.01) 2.80% ↓
DeepSeek-V3. In comparison, the removal of 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒shows the smallest drop on both LLMs, suggesting that
while retrieval based on intra-file context is critical for achieving correct functionality, its absence does not limit
LLMs’ context utilization as such immediate context is included in the prompt.
Finding 2: LogiCoder’s performance benefits from logical relationships captured by all three components of
the LCE module. The 𝐿𝐶𝑖𝑚𝑝𝑜𝑟𝑡component is the most critical for the identification of relevant usage examples,
while 𝐿𝐶𝑖𝑛𝑓𝑖𝑙𝑒is the most essential for the functional correctness in LLMs’ final code generation.
5.3
RQ3: Effectiveness of UER
As mentioned in Section 3.4, LogiCoder leverages both call relationships and context similarity to perform usage
example retrieval (UER). To evaluate the effectiveness of our UER module design, we introduce the following
settings:
• w/ Callee: This setting does not further trace call relationships to obtain repository-specific usage examples,
which measures the performance of using potential callees instead of their usage examples for generation. We
also sort callees by their context similarity as LogiCoder does in UER.
• w/ Random: This setting performs random selection for usage examples, which aims to investigate the impact
of our ranking technique using context similarity.
Table 6 presents the ablation study results on Kimi-K2 and DeepSeek-V3. The w/ Callee setting, which bypasses
call relationship tracing, shows the most notable performance drop compared to LogiCoder. Specifically, its
Pass@1 decreases by 24.99% (relative) for Kimi-K2 and 20.06% (relative) for DeepSeek-V3. This indicates that,
in code generation tasks, LLMs benefit more from concrete usage examples than from being given the callees
alone. Additionally, the Recall@1 score of the w/ Callee variant decreases by over 10%. This suggests that usage
examples can also guide LLMs to correctly use repository-specific knowledge during code generation. The w/
Random variant, which replaces the context similarity ranking with random selection, also leads to performance
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 19](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-19.png)

![Página PDF 19, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-19.png)


<!-- PDF page 20 -->

## Página PDF 20

20
•
Zhang et al.
Table 6. Pass@1 and Recall@1 of LogiCoder and Its UER Variants Based on Two Best-Performing LLMs Across the DevEval-cf
Benchmark.
Method
Kimi-K2
DeepSeek-V3
Pass@1 (CV)
Recall@1 (CV)
Pass@1 (CV)
Recall@1 (CV)
LogiCoder
44.58 (0.01)
46.39 (0.01)
41.83 (0.01)
46.11 (0.01)
w/ Callee
33.44 (0.01) 24.99% ↓
41.43 (0.00) 10.69% ↓
33.44 (0.01) 20.06% ↓
40.81 (0.01) 11.49% ↓
w/ Random
40.97 (0.01) 8.10% ↓
44.96 (0.01) 3.08% ↓
39.28 (0.01) 6.10% ↓
44.12 (0.01) 4.32% ↓
Table 7. Pass@1 and Recall@1 of LogiCoder and Its SSF Variants Based on Two Best-Performing LLMs Across the DevEval-cf
Benchmark.
Method
Kimi-K2
DeepSeek-V3
Pass@1 (CV)
Recall@1 (CV)
Pass@1 (CV)
Recall@1 (CV)
LogiCoder
44.58 (0.01)
46.39 (0.01)
41.83 (0.01)
46.11 (0.01)
w/o SSF
39.39 (0.02) 11.64% ↓
43.59 (0.00) 6.04% ↓
37.15 (0.00) 11.19% ↓
42.14 (0.04) 8.61% ↓
w/ ScoreAdd
42.47 (0.01) 4.73% ↓
45.95 (0.01) 0.95% ↓
40.23 (0.01) 3.83% ↓
45.22 (0.00) 1.93% ↓
w/ RRF (𝑘= 50)
43.74 (0.02) 1.88% ↓
44.76 (0.02) 3.51% ↓
41.40 (0.01) 1.03% ↓
45.48 (0.01) 1.37% ↓
w/ RRF (𝑘= 70)
43.73 (0.03) 1.91% ↓
45.30 (0.00) 2.35% ↓
41.30 (0.00) 1.27% ↓
45.42 (0.00) 1.50% ↓
w/o LCE+UER
33.75 (0.00) 24.27% ↓
39.99 (0.00) 13.80% ↓
32.59 (0.02) 22.09% ↓
39.94 (0.03) 13.38% ↓
degradation. Its Pass@1 score exhibits a relative decrease of 8.10% for Kimi-K2 and 6.10% for DeepSeek-V3.
Similarly, its Recall@1 drops by 3.08% (relative) and 4.32% (relative) respectively. Though the drop is smaller than
that of w/ Callee, this result confirms that our context-similarity-based ranking can effectively identify relevant
usage examples and thereby improve LLMs’ code generation.
Finding 3: Both the call relationship tracing and context similarity ranking in LogiCoder’s UER module
are essential. Our results also suggest that showing similar usage examples to LLMs can elicit their code
generation capability more effectively than providing logical context, i.e., potential callee functions.
5.4
RQ4: Effectiveness of SSF
To evaluate the effectiveness of our Semantic Search Fusion (SSF) module, we conduct an ablation study on the
two best-performing LLMs. Specifically, we compare LogiCoder to the following settings:
• w/o SSF: This setting removes the entire SSF module and constructs prompts using only the top-ranked usage
examples from the UER module.
• w/ ScoreAdd: This setting replaces the Reciprocal Rank Fusion (RRF) with a direct addition of the semantic and
contextual similarity scores to assess the impact of our rank-based fusion.
• w/ RRF-k: To analyze the sensitivity of the RRF hyperparameter 𝑘, we evaluate its alternative values of 50 and
70, compared to our default of 𝑘= 60 from the established practices.
• w/o LCE+UER: To directly compare the performance of our two standalone retrieval strategies, we also report
the variant that relies only on semantic search. This setting is the same as Dense Retrieval baseline.
Table 7 presents the results of the ablation study. To understand the role of the SSF module as a whole, we
first compare the w/o SSF variant against the w/o LCE + UER variant (which relies solely on Dense Retrieval). The
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 20](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-20.png)

![Página PDF 20, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-20.png)


<!-- PDF page 21 -->

## Página PDF 21

LLM See, LLM Do
•
21
w/o LCE + UER variant exhibits the largest performance degradation, with its Pass@1 decreasing by a drastic
24.27% (relative) for Kimi-K2 and 22.09% (relative) for DeepSeek-V3. In contrast, removing the semantic search
only results in a smaller 11.64% and 11.19% relative drop on Pass@1 for Kimi-K2 and DeepSeek-V3 respectively.
Note that the standalone retrieval based on logical context maintains a Pass@1 of 39.39% on Kimi-K2, which still
substantially outperforms existing RAG baselines. The results confirm that while SSF serves as a crucial relevance
filter and robust fallback mechanism, the retrieval based on logical context is the primary source of LogiCoder’s
performance gains.
27 
10 
11 
9 
42 
10 
128 
LogiCoder w/o SSF
LogiCoder w/o LCE + UER
LogiCoder
(a) Kimi-K2
24 
15 
11 
6 
38 
3 
127 
LogiCoder w/o SSF
LogiCoder w/o LCE + UER
LogiCoder
(b) DeepSeek-V3
Fig. 6. The Venn diagram of correctly generated code for LogiCoder and its two variants on Kimi-K2 and DeepSeek-V3.
To further separate the performance gains, we analyze the overlap of successfully resolved tasks using Venn
diagrams shown in Figure 6. Firstly, the result reveals that our retrieval based on logical context contributes more
unique successes than semantic search, e.g., 42 vs 11 on Kimi-K2 and 38 vs 11 on DeepSeek-V3. Secondly, our SSF
module is not merely a re-ranking strategy. It fuses two complementary types of knowledge, including exact
dependency information and fuzzy semantics. Their combination can further compensate for their respective
blind spots. Figure 6 shows that 27 and 24 additional tasks are successfully solved by LogiCoder on Kimi-K2 and
DeepSeek-V3 respectively, which neither variant could solve alone.
Regarding the fusion technique, we compare LogiCoder (using RRF) with its w/ ScoreAdd variant. Replacing
RRF with a simple addition of similarity scores leads to a minor relative drop of 4.73% and 3.83% in Pass@1 for
Kimi-K2 and DeepSeek-V3 respectively, alongside a slight decrease in Recall@1. The results demonstrate that
while the rank-based RRF is effective at combining distinct similarity metrics (cosine similarity and Jaccard index),
the performance gain of the SSF module mainly comes from the fusion of different aspects of information rather
than the ranking algorithm itself. Furthermore, the sensitivity analysis on the hyperparameter 𝑘in RRF further
demonstrates its robustness. Adjusting its value from 60 to 50 or 70 results in only minor decrease in Pass@1.
The maximum relative decrease is 1.91% when evaluating w/ RRF (𝑘= 70) on Kimi-K2. This confirms that though
the choice of 𝑘= 60 based on established practices achieves the best performance, our SSF module is not highly
sensitive to minor changes in this hyperparameter.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 21](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-21.png)

![Página PDF 21, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-21.png)


<!-- PDF page 22 -->

## Página PDF 22

22
•
Zhang et al.
Table 8. Pass@1 of LogiCoder and Its Baselines Based on Two Best-Performing LLMs Across the DevEval and CoderEval
Benchmarks.
Method
DevEval
CoderEval
Kimi-K2
DeepSeek-V3
Kimi-K2
DeepSeek-V3
Direct
22.47
23.45
29.58
22.07
CoT
44.00
42.52
44.13
42.25
Self-Planning
41.81
41.42
40.85
40.38
In-File Context
39.23
45.15
40.85
39.91
Sparse Retrieval
45.53
46.47
42.25
43.66
Dense Retrieval
45.81
46.68
50.70
46.48
Vanilla RAG
46.30
46.68
43.19
43.66
Shifted RAG
45.59
46.63
46.01
46.01
RepoCoder
45.75
47.01
44.60
44.60
DraCo
41.26
44.71
42.25
41.31
GraphCoder
36.88
40.60
38.97
42.25
RepoScope
44.32*
38.85*
45.07*
44.60*
CodeAgent
-
40.05
35.68
22.07
LogiCoder
51.78
54.47
53.05
48.83
Relative
11.84% ↑
15.87% ↑
4.64% ↑
5.06% ↑
*Due to the original models being taken offline, RepoScope is evaluated on their more recent checkpoints, i.e., Kimi-K2-250905
and DeepSeek-V3-250324.
Finding 4: While retrieval based on logical context is the primary driver of performance gains, the SSF module
also provides crucial complementary semantic knowledge, which also substantially increases LogiCoder
performance. Furthermore, the RRF component is effective and robust in combining these distinct retrieval
results.
5.5
RQ5: Generalization Ability
In the preceding sections, we have evaluated LogiCoder’s effectiveness on DevEval-cf, a challenging subset
where each task requires at least one cross-file call. However, in real-world software development, developers may
encounter an unpredictable mix of cross-file, local-file, and entirely self-contained tasks. To validate LogiCoder’s
robustness and generalizability in these mixed-dependency scenarios, we evaluate it against all baselines on
the complete, unfiltered DevEval benchmark, as well as the Python subset of the CoderEval [60] benchmark11.
Table 8 presents the results of all approaches on the two best-performing LLMs, i.e., Kimi-K2 and DeepSeek-V3.
Results on DevEval. LogiCoder demonstrates robustness when applied across tasks with diverse dependency
types. It achieves a Pass@1 of 51.78% on Kimi-K2 and 54.47% on DeepSeek-V3, yielding relative improvements of
11.84% and 15.87% over the best-performing baselines. This indicates that LogiCoder’s retrieval does not degrade
LLMs’ code generation performance on tasks with diverse dependency types.
Results on CoderEval: The CoderEval benchmark exhibits a different distribution of task dependency types.
As shown in Table 8, Dense Retrieval proves to be the most competitive baseline, with a Pass@1 of 50.70% on
11After filtering out 17 invalid instances due to incorrect file paths or missing target functions, we eventually obtain 213 tasks from CoderEval
for the evaluation.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 22](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-22.png)

![Página PDF 22, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-22.png)


<!-- PDF page 23 -->

## Página PDF 23

LLM See, LLM Do
•
23
Kimi-K2 and 46.48% on DeepSeek-V3. This suggests that a particular part of tasks in CoderEval can be resolved
via semantic search. Nevertheless, LogiCoder still surpasses all other approaches, achieving 53.05% and 48.83%
Pass@1 on Kimi-K2 and DeepSeek-V3, respectively. This yields relative improvements of 4.64% and 5.06% over
Dense Retrieval.
These results confirm LogiCoder’s robustness to diverse dependency types and its strong generalizability for
real-world code generation tasks. It is worth noting that, compared with the DevEval-cf subset, LogiCoder’s
relative improvement narrows on the broader mixed-dependency benchmarks. This is the expected behavior
of a focused method: it yields the greatest benefit where cross-file retrieval is most needed, while remaining
consistently positive and never degrading performance on tasks that do not require cross-file calls.
Finding 5: Compared to tasks in DevEval-cf, the relative improvement of LogiCoder narrows but remains
consistently positive on the broader mixed-dependency task space. Its performance is robust to the absence of
cross-file calls. This confirms the generalizability of LogiCoder for practical code generation.
5.6
RQ6: Analysis of Retrieval Context Length
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
Context Length
37
38
39
40
41
42
43
44
45
46
47
48
Pass@1/Recall@1
39.39
42.89
44.58
44.63
43.72
43.60
45.10
44.00
44.08
45.58
46.38
46.38
46.16
46.67
46.06
46.19
Pass@1
Recall@1
Pass@1 95%CI
Recall@1 95%CI
(a) Kimi-K2
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
Context Length
37
38
39
40
41
42
43
44
45
46
47
48
Pass@1/Recall@1
38.30
39.67
41.83
40.78
40.87
41.96
41.20
41.91
43.11
44.81
46.11
45.24
45.67
45.84
46.15
45.69
Pass@1
Recall@1
Pass@1 95%CI
Recall@1 95%CI
(b) DeepSeek-V3
Fig. 7. Influence of retrieval context length on LogiCoder’s performance on Kimi-K2 and DeepSeek-V3.
Apart from the quality of retrieved examples, the retrieval context length is another key factor influencing the
performance of RAG approaches [18]. To optimize the trade-off between computational cost and effectiveness,
we investigate the impact of retrieval context length on LogiCoder’s performance. We evaluate LogiCoder
across a range of context lengths, from 1K to 10K tokens, using the two best-performing LLMs (i.e., Kimi-K2
and DeepSeek-V3). For each length, we perform 6 independent runs to mitigate randomness and enable robust
statistical testing. The above settings are selected to balance comprehensive analysis with the high computational
cost of LLM inference.
Figure 7 illustrates the relationship between LogiCoder’s performance and retrieval context length. To quantify
the uncertainty in our measurement, we calculate the 95% confidence interval (based on the t-distribution) for
each data point. We observe a sharp increase in both Pass@1 and Recall@1 as the context length grows from
1K to 3K tokens. The first peak appears at 3K. Beyond this point, the performance of LogiCoder stabilizes and
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 23](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-23.png)

![Página PDF 23, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-23.png)


<!-- PDF page 24 -->

## Página PDF 24

24
•
Zhang et al.
Table 9. Pairwise Statistical Comparisons of LogiCoder’s Performance for Different Retrieval Context Lengths with P-Values
from Mann-Whitney U Tests.
Metric
Hypothesis
Context Length of 𝑃𝑒𝑎𝑘(tokens)
2000
3000
4000
5000
6000
8000
Pass@1 (Kimi-K2)
ℋ𝑃𝑟𝑒
0
0.001
< 0.001
0.005
0.450
0.606
< 0.001
ℋ𝑃𝑜𝑠𝑡
0
< 0.001
0.892
0.968
0.078
0.016
0.999
Recall@1 (Kimi-K2)
ℋ𝑃𝑟𝑒
0
0.001
< 0.001
0.009
0.173
0.008
0.451
ℋ𝑃𝑜𝑠𝑡
0
< 0.001
0.779
0.784
0.336
0.958
0.242
Pass@1 (DeepSeek-V3)
ℋ𝑃𝑟𝑒
0
0.001
< 0.001
0.125
0.125
< 0.001
0.104
ℋ𝑃𝑜𝑠𝑡
0
< 0.001
0.985
< 0.001
< 0.001
0.988
0.001
Recall@1 (DeepSeek-V3)
ℋ𝑃𝑟𝑒
0
0.001
< 0.001
0.155
0.041
0.026
< 0.001
ℋ𝑃𝑜𝑠𝑡
0
< 0.001
0.999
< 0.001
0.024
0.168
0.999
exhibits only slight fluctuations. For Kimi-K2, its Pass@1 below 3K tokens is shown to be more sensitive to
context length extension than Recall@1.
To statistically validate these observations and identify an optimal context length for practices, we conduct a
series of hypothesis tests. We define a robust performance peak as a length (i.e., 𝑃𝑒𝑎𝑘) that satisfies two conditions:
(1) its performance should be significantly better than at shorter context lengths and (2) its performance should not
be significantly worse than at longer context lengths. We formalize this with the following two null hypotheses
for a suspected peak length:
• ℋ𝑃𝑟𝑒
0 : The performance at 𝑃𝑒𝑎𝑘is less than or equal to the mean performance at shorter context lengths.
• ℋ𝑃𝑜𝑠𝑡
0
: The performance at 𝑃𝑒𝑎𝑘is greater than or equal to the mean performance at longer context lengths.
We consider that a “true” peak should reject the first hypothesis (ℋ𝑃𝑟𝑒
0 ) but fail to reject the second (ℋ𝑃𝑜𝑠𝑡
0
). The
most cost-effective choice would be the shortest context length that meets these criteria. We test our hypotheses
using the one-sided Mann-Whitney U test, which is a non-parametric method suitable for our small sample size.
Results in Table 9 confirm that 3K tokens is the optimal context length for both Kimi-K2 and DeepSeek-V3.
At this length, LogiCoder’s performance is statistically superior to that of shorter contexts while showing no
significant difference from longer ones. This confirms that 3K tokens provides an effective balance between
performance and computational efficiency.
Finding 6: The optimal retrieval context length for LogiCoder is 3K tokens. Its performance increases
significantly up to this point, after which it plateaus. Our statistical tests also confirm that 3K tokens yields
significantly better performance than shorter contexts, while longer contexts provide no statistically significant
improvement.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 24](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-24.png)

![Página PDF 24, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-24.png)


<!-- PDF page 25 -->

## Página PDF 25

LLM See, LLM Do
•
25
6
Discussion
6.1
Case Study
To illustrate the strengths and weaknesses of LogiCoder, we present three examples (one successful and two
failed) by comparing LogiCoder to other baselines in Figure 8 to 10.
# boto/ec2/volume.py
def update(self, validate=False, dry_run=False):
  rs = self.connection.get_all_volumes(
    [self.id], dry_run=dry_run
  )
  if len(rs) > 0:
    self._update(rs[0])
  elif validate:
    raise ValueError('%s is not a valid Volume ID' % self.id)
  return self.status
# boto/ec2/snapshot.py
def update(self, validate=False, dry_run=False):
  rs = self.connection.get_all_snapshots(
      [self.id], dry_run=dry_run
  )
  if len(rs) > 0:
    self._update(rs[0])
  elif validate:
    raise ValueError('%s is not a valid Snapshot ID' % self.id)
  return self.status
# boto/ec2/volume.py
def update(self, validate=False, dry_run=False):
  if not self.id:
    raise ValueError("Volume ID is not set")
  volumes = self.connection.get_all_volumes(
    [self.id], dry_run=dry_run
  )
  if not volumes:
    if validate:
      raise ValueError(f"Volume {self.id} does not exist")
    return None
  updated_volume = volumes[0]
  self._update(updated_volume)
  return self.status
# boto/ec2/volume.py
def update(self, validate=False, dry_run=False):
  if dry_run:
    raise self.status
  volumes = self.connection.get_all_volumes(
    [self.id], dry_run=dry_run
  )
  if not volumes:
    if validate:
      raise ValueError(f"Volume {self.id} does not exist")
    return self.status
  updated_volume = volumes[0]
  self._update(updated_volume)
  return self.status
Usage Example Retrieved by LOGICODER
Code Generated by LOGICODER
Code Generated by RepoCoder
Code Generated by DraCo
Relevant Usage
Fig. 8. An example of LogiCoder’s retrieval and its correct generation compared to two baseline approaches. Details of the
task and its retrieval are illustrated in Figure 1 and Figure 3.
A successful example of LogiCoder is shown in Figure 8. In this task, the target function to be generated is an
update method of the Volume class, where an invocation of a cross-file dependency get_all_volumes is required.
Leveraging the logical context extracted from EC2Connection (Figure 3), LogiCoder retrieved a similar example
from the Snapshot class, which provides crucial implementation knowledge for LogiCoder. It includes the correct
output handling logic for the target callee (by checking its length of resulting list using if len(rs) > 0). Although
the true callee (get_all_volumes) does not have usage in the repository, this similar usage pattern retrieved by
LogiCoder successfully guided LLMs to generate the correct target function. In comparison, RepoCoder and
DraCo failed to produce the correct implementation without the guidance of usage examples (their retrieved
examples are shown in Figure 1). Specifically, RepoCoder, relying on a similarity-based retriever, failed to identify
the semantically unrelated code from the Snapshot class, while DraCo’s static analysis was limited by the absence
of dataflow dependency between the Volume and Snapshot classes. Without knowledge about “usage”, these two
approaches incorrectly checked the result list with if not volumes and included an excessive condition, leading
to their failures. This example explains why LogiCoder’s retrieval strategy focuses on similar usage examples
instead of the callees themselves.
However, misleading usage examples and the integration of semantic search may sometimes lead to Logi-
Coder’s failures. As shown in Figure 9, the task requires the LLM to generate a function for calculating the part
size for Glacier’s data uploading. It involves a cross-file callee minimum_part_size, which returns 4MB by default
unless a large volume of data is provided. In this case, LogiCoder retrieved a usage example from a unit test,
test_gigabyte_data, which only handled an edge case for the target callee. This unrepresentative example misled
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 25](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-25.png)

![Página PDF 25, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-25.png)


<!-- PDF page 26 -->

## Página PDF 26

26
•
Zhang et al.
# boto/glacier/concurrent.py
def _calculate_required_part_size(self, total_size):
  from boto.glacier.utils import minimum_part_size
  min_part_size_required = minimum_part_size(total_size)
  ...
# boto/glacier/concurrent.py
def _calculate_required_part_size(self, total_size):
  # 4 MB minimum part size for Glacier
  min_part_size_required = 4 * 1024 * 1024
  ...
# boto/glacier/concurrent.py
def _calculate_required_part_size(self, total_size):
  MAX_PARTS = 10000
  # Calculate the minimum required part size to keep the 
number of parts under MAX_PARTS
  min_part_size_required = math.ceil(total_size / MAX_PARTS)
  ...
# tests/unit/glacier/test_utils.py
def test_gigabyte_size(self):
  # If we're over the maximum default part size, we go up to 
  # the next power of two until we find a part size that keeps 
  # us under 10,000 parts.
  self.assertEqual(minimum_part_size(8 * 1024 * 1024 * 10000),
                   8 * 1024 * 1024)
Code Generated by CoT
Usage Example Retrieved by LOGICODER
Code Generated by LOGICODER
Ground Truth
# boto/glacier/utils.py
def minimum_part_size(...):
  
  # if total_size 
# Default is 4 MB, recalculate 
> 40,000 MB
Callee
Misleading Usage
Fig. 9. A failure example of LogiCoder caused by misleading retrieval while CoT succeeded.
the LLM into generating an incorrect calculation for the standard use case. However, a non-RAG CoT succeeded
by correctly inferring the default value, though such implementation may introduce defects (if total_size exceeds
40,000 MB) by neglecting repository-specific knowledge. Figure 10 illustrates a complex edge case that reveals
the limitations of LogiCoder’s two retrieval strategies and LLMs’ generation capabilities. This task requires
calling a cross-file function, get_common_name. Our retrieval based on logical context failed to identify this callee
as it relies on a local import in the ground truth. Because our static analysis identifies candidate callees based
on available context, such local imports could be overlooked. In this case, the SSF module successfully acted
as a fallback by direct semantic matching. However, due to its lack of strict dependency constraints the LLM
eventually failed to generate the necessary local import statement and resulted in a NameError. We highlight this
case because: (1) it validates the power of the SSF module as a crucial and complementary component in complex
retrieval scenarios; and (2) it reveals a remaining challenge of LLMs in correctly synthesizing code even when
provided with accurate retrieval results.
# sslyze/plugins/certificate_info/_cli_connector.py
def _get_name_as_short_text(name_field: x509.Name) -> str:
  from sslyze.plugins.certificate_info._certificate_utils 
import get_common_names
  common_names = get_common_names(name_field)
  if common_names:
    return common_names[0]
  else:
    return name_field.rfc4514_string()
Ground Truth
# sslyze.plugins.certificate_info._certif
icate_utils
def get_common_names(...):
Callee
RepoCoder
/Draco
Relevant context 
not found!
LOGICODER
Callee & its usage 
found (by SSF)
def _get_name_as_short_text(name_field: x509.Name) -> str:
  for attribute in name_field:
    if attribute.old == x509.NameOID.COMMON_NAME: ...
Correct reimplementation
def _get_name_as_short_text(name_field: x509.Name) -> str:
  common_names = get_common_names(name_field)
  ...
Missing import
Fig. 10. A failure example of LogiCoder caused by Semantic Search Fusion.
6.2
Robustness to Static Analysis Failures
A common challenge in applying static analysis to dynamic languages like Python is the fragility of the tools
like pyan. They may produce uncertain relations or miss critical edges due to dynamic bindings or complex
local imports, which may result in an incomplete dependency graph. To quantify how robust LogiCoder is to
these static analysis failures, we conduct a sensitivity analysis. To simulate such failures, we intentionally and
randomly drop 25%, 50%, and 75% of the correctly identified candidate callees and usage examples retrieved by
call relationships. The experiment is conducted on the two best-performing models, Kimi-K2 and DeepSeek-V3,
using the DevEval-cf benchmark. The results are shown in Table 10.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 26](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-26.png)

![Página PDF 26, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-26.png)


<!-- PDF page 27 -->

## Página PDF 27

LLM See, LLM Do
•
27
Table 10. Evaluation Results of the Robustness of LogiCoder to Static Analysis Failures.
Method
Kimi-K2
DeepSeek-V3
Pass@1 (CV)
Recall@1 (CV)
Pass@1 (CV)
Recall@1 (CV)
LogiCoder
44.58 (0.01)
46.39 (0.01)
41.83 (0.01)
46.11 (0.01)
- 25% LC+UE
41.83 (0.01) 6.17% ↓
45.34 (0.01) 2.26% ↓
38.19 (0.02) 8.70% ↓
44.53 (0.01) 3.43% ↓
- 50% LC+UE
40.86 (0.00) 8.34% ↓
44.04 (0.00) 5.07% ↓
35.96 (0.03) 14.03% ↓
44.41 (0.01) 3.69% ↓
- 75% LC+UE
40.12 (0.01) 10.00% ↓
43.19 (0.00) 6.90% ↓
35.75 (0.04) 14.54% ↓
43.78 (0.01) 5.05% ↓
We can observe that degrading the graph completeness negatively impacts performance. However, the drop is
not critical. When the dependency graph degrades 25%, LogiCoder’s Pass@1 only drops from 44.58% to 41.83%
on Kimi-K2 and from 41.83% to 38.19% on DeepSeek-V3. On Kimi-K2, even when 75% of candidate callees and
usage examples are deleted, LogiCoder only suffers a 10.00% relative decrease, maintaining a Pass@1 of 40.12%.
Regarding DeepSeek-V3, this drop is slightly higher, with a relative drop of 14.54%. However, at this extreme
75% degradation, LogiCoder still outperforms all state-of-the-art baselines, e.g., RepoCoder’s 35.14% Pass@1.
The results indicate LogiCoder’s robustness to imperfect static analysis. It benefits largely from the SSF module.
Even if the whole dependency graph is collapsed, it will only degrade to the similarity-based retrieval, i.e., Dense
Retrieval.
6.3
Comparison to Feeding Whole Repository into Long Context Models
With the expansion of LLM context windows, we are interested in whether retrieval in LogiCoder is still
necessary for repository-aware code generation tasks. To this end, we establish a Full-Repo Context baseline by
simply feeding the entire repository context into LLMs.
First, we find that feeding the full repository is still not a universally applicable approach. As shown in Figure 11,
our analysis of 67 repositories in DevEval-cf reveals that 56% (38 repositories) exceed the 128K token limit of
most popular LLMs, with 3 repositories even exceeding 1M tokens. Therefore, retrieval remains necessary for
short-context LLMs and large-scale repositories.
Secondly, to provide a fair comparison across baselines, we derive a subset of 77 tasks from repositories under
the 128K token limit. We then implement the Full-Repo Context baseline by concatenating all source code files in
the repository into the prompt. The prompt structure is identical to our standard template (as shown in Figure 4),
with the exception that the Retrieval Context section is replaced by the repository context. We evaluate all
approaches with the Full-Repo Context baseline across all five LLMs. The results are presented in Table 11.
The results demonstrate that RAG remains critical in repository-aware code generation tasks. We find that on
three of the evaluated LLMs (Kimi-K2, Qwen2.5, and Llama-3.1), Full-Repo Context is outperformed not only by
most RAG approaches, but also by non-RAG baselines, e.g., In-File Context. Our LogiCoder approach surpasses
Full-Repo Context by a substantial margin across four out of five LLMs. This confirms that simply flooding the LLM
with an entire repository may introduce noise and hinder LLMs’ ability to locate and utilize relevant contextual
knowledge [36, 46]. GPT-4o is an exception, where Full-Repo Context (49.35%) surpasses LogiCoder (38.96%).
While this highlights GPT-4o’s exceptional long-context comprehension ability (but possibly with data leakage),
this strategy remains highly impractical for real-world development scenarios. Besides, this excessive token
consumption also introduces unacceptable financial costs and computational latency. To process these 77 tasks,
LogiCoder only consumes a total of 242.6K tokens. In contrast, the Full-Repo Context baseline consumes 4.6M
tokens, which is 19.1× larger than LogiCoder. Therefore, LogiCoder is still a superior and cost-effective code
generation approach even in the era of long-context LLMs.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 27](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-27.png)

![Página PDF 27, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-27.png)


<!-- PDF page 28 -->

## Página PDF 28

28
•
Zhang et al.
0
16K
32K
64K
128K
256K
512K
1M
>1M
Total Tokens / Repository
0
2
4
6
8
10
12
14
16
18
20
22
Number of Repositories
3
3
10
13
17
10
8
3
128K Token Boundary
Fig. 11. The Total Token Number Distribution of Repositories in DevEval-cf.
Table 11. Performance of Feeding Full Repository into LLMs’ Context Based on Five LLMs Across the DevEval-cf Benchmark.
Method
Kimi-K2
DeepSeek-
V3
GPT-4o
Qwen2.5
Llama-3.1
Direct
10.39
7.79
3.90
5.19
3.90
CoT
32.47
29.87
20.78
24.68
14.29
Self-Planning
32.47
29.87
20.78
23.38
13.29
In-File Context
25.97
31.17
23.38
20.78
22.08
Sparse Retrieval
31.17
33.77
22.08
24.68
19.48
Dense Retrieval
36.36
36.36
27.27
23.38
19.48
Vanilla RAG
36.36
27.27
25.97
22.08
19.48
Shifted RAG
32.47
28.57
28.57
24.68
18.18
RepoCoder
37.66
31.17
28.57
24.68
19.48
DraCo
32.47
32.47
29.87
29.87
20.78
GraphCoder
25.97
31.17
29.87
12.99
15.58
RepoScope
27.27*
23.38*
25.97
14.29
12.99
CodeAgent
-
19.48
25.97
20.78
16.88
Full-Repo Context
23.38
41.56
49.35
18.18
18.18
LogiCoder
42.86
45.45
38.96
35.06
28.57
*Due to the original models being taken offline, RepoScope is evaluated on their more recent checkpoints, i.e., Kimi-K2-250905
and DeepSeek-V3-250324.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 28](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-28.png)

![Página PDF 28, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-28.png)


<!-- PDF page 29 -->

## Página PDF 29

LLM See, LLM Do
•
29
Table 12. Retrieval Latency of LogiCoder and RAG baselines.
Method
Retrieval Latency (s)
Sparse Retrieval
0.35
Dense Retrieval
0.79
Vanilla RAG
0.91
Shifted RAG
0.94
RepoCoder
27.98
DraCo
0.18
GraphCoder
7.21
RepoScope
231.69
LogiCoder
1.68
6.4
Retrieval Latency of LogiCoder
We analyze the efficiency of LogiCoder against other RAG baselines by measuring its average retrieval latency
per task on the DevEval-cf. To reduce the impact of randomness, we run each approach 10 times. The results are
shown in Table 12. Among all approaches, DraCo is the most time-efficient, with an average retrieval latency
of 0.18 seconds. The reason is that its type-sensitive knowledge organization (which relies on available local
context) is bypassed in the function-level generation tasks. The one-pass similarity-based approaches belong to
the second tier. Their retrieval latencies are within a second due to their efficient lexical or semantic similarity
calculation, especially for Sparse Retrieval. In comparison, LogiCoder exhibits a higher retrieval latency of 1.68
seconds, but it is still faster than GraphCoder (7.21s), RepoCoder (27.98s) and RepoScope (231.69s). To pinpoint
where LogiCoder’s latency originates, we conduct a detailed stage-by-stage latency breakdown analysis. The
result is shown in Figure 12.
In our analysis, we distinguish between one-pass initialization stages and per-query inference stages. The
reason is that, in a real-world deployment, repository analysis could be performed asynchronously in an offline
manner and updated incrementally during its maintenance. Such operations may not block users’ real-time
requests. As for one-pass stages, the Dependency Graph Construction (DGC) stage, i.e., the pyan analysis, is the
most computationally expensive one. It has a mean latency of over 10 seconds, with extreme outliers up to 230
seconds for massive repositories. The Embedding stage only has a mean of 0.5 seconds, spiking to 10 seconds
for repositories with numerous functions (e.g., Telethon). Once the dependency graph and vector knowledge
base are constructed, the actual retrieval overhead is exceptionally low, i.e., only about 0.6 seconds on average.
Among the per-query inference stages, the Usage Example Retrieval (UER) stage is most time-consuming, which
involves the collection and ranking process of usage examples. As shown in Figure 12, for most repositories,
this takes less than 0.2 seconds. Due to outliers, its mean value is approximately 0.6 seconds. In comparison, the
latencies for Logical Context Extraction (LCE) and Semantic Search Fusion (SSF) are almost negligible, taking only
0.005 seconds on average.
6.5
Effectiveness with Frontier LLMs and Coding Agents
Given the rapid scaling of LLM and agent capabilities, a natural question is whether the gains of LogiCoder
persist as the underlying LLMs and agents become stronger. To investigate this, we conduct two supplementary
experiments, i.e., evaluating LogiCoder with stronger frontier LLMs and integrating it into state-of-the-art
coding agents.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 29](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-29.png)

![Página PDF 29, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-29.png)


<!-- PDF page 30 -->

## Página PDF 30

30
•
Zhang et al.
0.0002
0.0005 0.001 0.002
0.005 0.01
0.02
0.05
0.1
0.2
0.5
1
2
5
10
20
50
100
200
Time (seconds, log scale)
DGC
(one-pass)
LCE
(average)
UER
(average)
Embedding
(one-pass)
SSF
(average)
Stage
twilio-fatisar
230.21s
twilio-fatisar
0.04s
barf
12.74s
Telethon
10.33s
dash
0.05s
Mean
Fig. 12. Stage-by-stage latency breakdown analysis of LogiCoder.
Table 13. Performance of LogiCoder and Representative Baselines Based on Frontier LLMs Across the DevEval-cf Benchmark.
Method
GPT-5.5
Kimi-K2.6
DeepSeek-V4-Pro
Direct
29.52
16.99
11.89
In-File Context
47.98
39.07
33.55
RepoCoder
57.54
42.25
40.76
DraCo
54.56
41.61
35.88
RepoScope
56.69
35.24
34.61
LogiCoder
62.21
47.56
46.92
Relative
8.12% ↑
12.57% ↑
15.11% ↑
With frontier LLMs. We re-evaluate LogiCoder and representative baselines on DevEval-cf using the latest
frontier LLMs, including GPT-5.512, Kimi-K2.613, and DeepSeek-V4-Pro14. As shown in Table 13, LogiCoder still
achieves the best Pass@1 across three frontier LLMs (e.g., 62.21% on GPT-5.5), consistently outperforming the
strongest baseline. Although the margin becomes moderate, frontier LLMs still benefit from the LogiCoder’s
retrieval.
Integrated with coding agents. LLM-based coding agents have shown remarkable potential in various
software engineering tasks by leveraging tools to perceive, reason, and act with codebases [35, 58, 66]. Typically,
an agent framework includes two kinds of control: (1) a feed-forward process that provides necessary context
to steer the agent before it acts, and (2) a feedback process of iterative execution and repair that helps it self-
correct after acting. LogiCoder targets the former and can be integrated into coding agents as a retrieval
12https://platform.openai.com/docs/models/gpt-5.5
13https://platform.kimi.com/docs/guide/kimi-k2-6-quickstart
14https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 30](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-30.png)

![Página PDF 30, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-30.png)


<!-- PDF page 31 -->

## Página PDF 31

LLM See, LLM Do
•
31
Table 14. Performance of Integrating LogiCoder and Representative Baselines with Coding Agent Frameworks.
Method
OpenCode
Mini-SWE-Agent
Framework-Only
56.68
58.17
+RepoCoder
57.11 0.76% ↑
61.78 6.21% ↑
+DraCo
56.05 1.11% ↓
60.93 4.74% ↑
+LogiCoder
58.81 3.76% ↑
62.85 8.05% ↑
component. To this end, we integrate LogiCoder into two state-of-the-art agent frameworks, OpenCode15 and
Mini-SWE-Agent [58], using DeepSeek-V4-Pro as the backbone LLM. As the iterative execution and repair process
would leak the test oracle and introduce undesirable cost, we inject LogiCoder’s retrieval results as the initial
guidance of the agents and only allow agents to explore the repository and perform reasoning. As shown in
Table 14, running the two frameworks directly achieves a strong Pass@1 of 56.68% and 58.17%, respectively. After
integrating LogiCoder, their Pass@1 further improves to 58.81% and 62.85%. Its relative improvement is up to
8.05%, surpassing the integration with other retrieval baselines. This confirms that LogiCoder’s retrieval can
benefit current coding agents with directional and high-quality context. Meanwhile, the multi-turn exploration
of these agents incurs substantially higher time (9.3× for OpenCode and 7.6× for Mini-SWE-Agent) and token
costs (43.9× for OpenCode and 36.2× for Mini-SWE-Agent) than LogiCoder’s single-pass retrieval, making them
unnecessarily heavy for function-level code generation tasks. In comparison, LogiCoder can serve both as an
efficient standalone code generation approach and as a high-precision retrieval component that can be plugged
into coding agents to boost their performance.
6.6
Implications on Other Repository-level Software Engineering Tasks
LogiCoder introduces a novel RAG pattern for advancing LLM-powered software engineering. Its core method-
ology is to retrieve similar usage examples through logical context, which has significant implications beyond
code generation, particularly for other repository-level software engineering tasks.
Although LogiCoder targets a well-scoped task, i.e., repository-aware code generation, in this paper, it
is worth noting that its retrieval based on logical context could also be generalized to other repository-level
software engineering tasks where understanding code context and its usage is important. A typical example
is SWE-bench [29], which evaluates LLMs’ ability to resolve real-world GitHub issues. This process involves
two main tasks, fault localization and patch generation [55]. The logical context extracted by LogiCoder can
help narrow down the search space for faulty code by identifying code entities relevant to the issue. After
localization, LogiCoder can retrieve correct and similar usage examples to guide the generation of a contextually
appropriate patch, which are important fix ingredients in program repair studies [57]. Nevertheless, building a
full issue-resolution agent around LogiCoder and evaluating it on SWE-bench require a substantial separate
effort, which differs from the primary focus of this work. Therefore, we regard it as a promising direction and
will prioritize it by extending LogiCoder in our future work.
7
Threats to Validity
Internal Validity. One of the threats to internal validity is the use of an imperfect static analysis tool. As
mentioned in Section 6.4, pyan may include uncertain define-and-use relations in its results and hence may
introduce biases to the effectiveness and efficiency of LogiCoder. Besides, as our dependency graph is built
via static analysis, it only models functional dependencies and does not capture non-functional ones such as
15https://github.com/anomalyco/opencode
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 31](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-31.png)

![Página PDF 31, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-31.png)


<!-- PDF page 32 -->

## Página PDF 32

32
•
Zhang et al.
configuration files or environment variables. While our Semantic Search Fusion module can index and retrieve
these artifacts, how to effectively leverage this non-functional information still requires further exploration,
which we plan to address in our future work. Regarding model selection, there may be a potential data leakage
issue with recently released models such as Kimi-K2, as their training data may overlap with our evaluation
benchmark. To ensure a fair and controlled comparison, we evaluate LogiCoder and its baselines using the
same backbone models. Another threat lies in manually crafted prompts. As LLMs are shown to be sensitive to
different prompt inputs [30, 65], we address this issue by following the established prompt design [15, 38, 63]
and evaluating RAG approaches using multiple prompts with different demonstration orders [18]. However, our
paper does not exhaustively explore the entire space of prompt engineering and hence may be still suboptimal.
Techniques like automatic prompt optimization [44] should be an open and promising direction to further address
this issue. Moreover, RAG approaches suffer from the potential risk of propagating technical debt, i.e., code smells,
in the existing repository. To mitigate this, LogiCoder could integrate code quality assurance techniques in
practical scenarios. For instance, linters could be applied during the Dependency Graph Construction phase to
prune low-quality code from the knowledge base.
External Validity. We only evaluate LogiCoder on two Python benchmarks, DevEval and CoderEval. Hence,
the generalizability of our approach to other programming languages remains unexplored. However, the core idea
of LogiCoder, constructing an abstract dependency graph to extract logical context and retrieve usage examples,
is language-agnostic. The transfer of LogiCoder merely requires replacing the Python-specific pyan parser with
appropriate static analyzers capable of extracting fundamental code relations (i.e., define-and-use, imports, and
belonging). For instance, tools like Joern16 can generate code property graphs from source code for multiple
languages, while frameworks like Soot or the TypeScript Compiler API can also provide the necessary dependency
information. Besides, our experiments only focus on five widely-used LLMs. Since different LLMs could have
different behaviors in response to provided context, it is worth investigating whether our approach is effective
for other series of LLMs. Another threat to external validity is that our evaluation is limited to repository-aware
code generation and does not cover other repository-level software engineering tasks, such as issue resolution.
We will further investigate the application of LogiCoder to those scenarios for future work.
8
Conclusion
In this paper, we propose a novel RAG approach, LogiCoder, to enhance LLMs’ awareness of repository-specific
knowledge during code generation. Specifically, LogiCoder first identifies the candidate callees of the target
function based on a constructed dependency graph. By tracing their call relationships, LogiCoder retrieves their
contextually similar usage examples. Then it integrates these examples with the results from semantic search to
mitigate the risk of ineffective retrieval. After that, the top-ranked examples are incorporated into LLMs’ prompts
for repository-aware code generation. Our experimental results demonstrate that LogiCoder outperforms all
state-of-the-art baselines on repository-aware code generation tasks, especially on those that require cross-file
calls. Our findings indicate the importance of exploiting the logical relationships within code repositories and
demonstrate the effectiveness of using concrete usage examples to guide LLMs. In future work, we will further
investigate how to effectively utilize contextual knowledge to address other practical software engineering tasks.
Acknowledgments
We gratefully acknowledge the financial support from the National Key Research and Development Program of
China (Grant No.2023YFB4503802) and the National Natural Science Foundation of China (Grant No.62332005
and Grant No.62302515).
16https://joern.io
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 32](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-32.png)

![Página PDF 32, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-32.png)


<!-- PDF page 33 -->

## Página PDF 33

LLM See, LLM Do
•
33
References
[1] Shamsa Abid, Shafay Shamail, Hamid Abdul Basit, and Sarah Nadi. 2021. FACER: An API usage-based code-example recommender for
opportunistic reuse. Empirical Software Engineering 26, 6 (Nov. 2021), 110. https://doi.org/10.1007/s10664-021-10000-w
[2] Lakshya A. Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K. Lahiri, and Sriram K. Rajamani. 2023. Guiding Language Models of
Code with Global Context using Monitors. http://arxiv.org/abs/2306.10763 arXiv:2306.10763 [cs].
[3] Sushil K. Bajracharya, Joel Ossher, and Cristina V. Lopes. 2010. Leveraging usage similarity for effective retrieval of examples in code
repositories. In Proceedings of the Eighteenth ACM SIGSOFT International Symposium on Foundations of Software Engineering (Santa Fe, New
Mexico, USA) (FSE ’10). Association for Computing Machinery, New York, NY, USA, 157–166. https://doi.org/10.1145/1882291.1882316
[4] Shraddha Barke, Michael B. James, and Nadia Polikarpova. 2023. Grounded Copilot: How Programmers Interact with Code-Generating
Models. Proceedings of the ACM on Programming Languages 7, OOPSLA1 (April 2023), 85–111. https://doi.org/10.1145/3586030 Publisher:
Association for Computing Machinery (ACM).
[5] Zhangqian Bi, Yao Wan, Zheng Wang, Hongyu Zhang, Batu Guan, Fangxin Lu, Zili Zhang, Yulei Sui, Hai Jin, and Xuanhua Shi. 2024.
Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback. In Findings of the Association
for Computational Linguistics: ACL 2024, Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational
Linguistics, Bangkok, Thailand, 2336–2353. https://doi.org/10.18653/v1/2024.findings-acl.138
[6] Charles E. Brown. 1998. Coefficient of Variation. In Applied Multivariate Statistics in Geohydrology and Related Sciences. Springer Berlin
Heidelberg, Berlin, Heidelberg, 155–157. https://doi.org/10.1007/978-3-642-80328-4_13
[7] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,
Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot
Learners. http://arxiv.org/abs/2005.14165 arXiv:2005.14165 [cs].
[8] Deng Cai, Yan Wang, Lemao Liu, and Shuming Shi. 2022. Recent Advances in Retrieval-Augmented Text Generation. In Proceedings of the
45th International ACM SIGIR Conference on Research and Development in Information Retrieval (Madrid, Spain) (SIGIR ’22). Association
for Computing Machinery, New York, NY, USA, 3417–3419. https://doi.org/10.1145/3477495.3532682
[9] Partha Chakraborty, Mahmoud Alfadel, and Meiyappan Nagappan. 2025. BLAZE: Cross-Language and Cross-Project Bug Localization
via Dynamic Chunking and Hard Example Learning. IEEE Transactions on Software Engineering 51, 8 (Aug. 2025), 2254–2267. https:
//doi.org/10.1109/TSE.2025.3579574
[10] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda,
Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin,
Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe
Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen
Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher
Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira
Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. 2021.
Evaluating Large Language Models Trained on Code. arXiv:2107.03374 [cs.LG] https://arxiv.org/abs/2107.03374
[11] Wei Cheng, Yuhan Wu, and Wei Hu. 2024. Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Association for
Computational Linguistics, Bangkok, Thailand, 7957–7977. https://doi.org/10.18653/v1/2024.acl-long.431
[12] Gordon V. Cormack, Charles L A Clarke, and Stefan Buettcher. 2009. Reciprocal rank fusion outperforms condorcet and individual rank
learning methods. In Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval.
ACM, Boston MA USA, 758–759. https://doi.org/10.1145/1571941.1572114
[13] DeepSeek-AI. 2024. DeepSeek-V3 Technical Report. arXiv:2412.19437 [cs.CL] https://arxiv.org/abs/2412.19437
[14] Yangruibo Ding, Zijian Wang, Wasi Ahmad, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing
Xiang. 2024. CoCoMIC: Code Completion by Jointly Modeling In-file and Cross-file Context. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), Nicoletta Calzolari, Min-Yen Kan,
Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.). ELRA and ICCL, Torino, Italia, 3433–3445.
https:
//aclanthology.org/2024.lrec-main.305/
[15] Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati,
Parminder Bhatia, Dan Roth, and Bing Xiang. 2023. CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code
Completion. In Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track. https://openreview.
net/forum?id=wgDcbBMSfh
[16] Yihong Dong, Ge Li, and Zhi Jin. 2023. CODEP: Grammatical Seq2Seq Model for General-Purpose Code Generation. In Proceedings of
the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA 2023). Association for Computing Machinery,
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 33](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-33.png)

![Página PDF 33, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-33.png)


<!-- PDF page 34 -->

## Página PDF 34

34
•
Zhang et al.
New York, NY, USA, 188–198. https://doi.org/10.1145/3597926.3598048 event-place: Seattle, WA, USA.
[17] Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike
Lewis. 2023. InCoder: A Generative Model for Code Infilling and Synthesis. http://arxiv.org/abs/2204.05999 arXiv:2204.05999 [cs].
[18] Shuzheng Gao, Xin-Cheng Wen, Cuiyun Gao, Wenxuan Wang, Hongyu Zhang, and Michael R. Lyu. 2023. What Makes Good In-Context
Demonstrations for Code Intelligence Tasks with LLMs?. In 2023 38th IEEE/ACM International Conference on Automated Software
Engineering (ASE). 761–773. https://doi.org/10.1109/ASE56229.2023.00109
[19] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, and Haofen Wang. 2024.
Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv:2312.10997 [cs.CL] https://arxiv.org/abs/2312.10997
[20] Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin. 2022. UniXcoder: Unified Cross-Modal Pre-training for Code
Representation. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (Eds.). Association for Computational Linguistics, Dublin, Ireland, 7212–7225.
https://doi.org/10.18653/v1/2022.acl-long.499
[21] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Y. Wu, Y. K. Li, Fuli Luo, Yingfei
Xiong, and Wenfeng Liang. 2024. DeepSeek-Coder: When the Large Language Model Meets Programming – The Rise of Code Intelligence.
http://arxiv.org/abs/2401.14196 arXiv:2401.14196 [cs].
[22] Sichong Hao, Xianjun Shi, and Hongwei Liu. 2024. RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type
Errors. In 2024 IEEE International Conference on Software Maintenance and Evolution (ICSME). 199–210.
https://doi.org/10.1109/
ICSME58944.2024.00028 ISSN: 2576-3148.
[23] Shirley Anugrah Hayati, Raphael Olivier, Pravalika Avvaru, Pengcheng Yin, Anthony Tomasic, and Graham Neubig. 2018. Retrieval-
Based Neural Code Generation. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, Ellen Riloff,
David Chiang, Julia Hockenmaier, and Jun’ichi Tsujii (Eds.). Association for Computational Linguistics, Brussels, Belgium, 925–930.
https://doi.org/10.18653/v1/D18-1111
[24] Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, and Haoyu Wang. 2024. Large
Language Models for Software Engineering: A Systematic Literature Review. ACM Transactions on Software Engineering and Methodology
(Sept. 2024), 3695988. https://doi.org/10.1145/3695988
[25] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. 2024.
Qwen2. 5-Coder Technical Report. arXiv preprint arXiv:2409.12186 (2024).
[26] Paul Jaccard. 2010. The Distribution of the Flora in the Alpine Zone. New Phytologist 11, 2 (2010), 37–50.
[27] Juyong Jiang, Fan Wang, Jiasi Shen, Sungju Kim, and Sunghun Kim. 2024. A Survey on Large Language Models for Code Generation.
http://arxiv.org/abs/2406.00515 arXiv:2406.00515 [cs].
[28] Xue Jiang, Yihong Dong, Lecheng Wang, Zheng Fang, Qiwei Shang, Ge Li, Zhi Jin, and Wenpin Jiao. 2024. Self-Planning Code Generation
with Large Language Models. ACM Trans. Softw. Eng. Methodol. 33, 7 (Sept. 2024). https://doi.org/10.1145/3672456 Place: New York, NY,
USA Publisher: Association for Computing Machinery.
[29] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. 2024. SWE-bench: Can
Language Models Resolve Real-World GitHub Issues? http://arxiv.org/abs/2310.06770 arXiv:2310.06770 [cs].
[30] Jia Li, Ge Li, Yongmin Li, and Zhi Jin. 2024. Structured Chain-of-Thought Prompting for Code Generation. ACM Transactions on Software
Engineering and Methodology (Aug. 2024), 3690635. https://doi.org/10.1145/3690635
[31] Jia Li, Ge Li, Yunfei Zhao, Yongmin Li, Huanyu Liu, Hao Zhu, Lecheng Wang, Kaibo Liu, Zheng Fang, Lanshen Wang, Jiazheng Ding,
Xuanming Zhang, Yuqi Zhu, Yihong Dong, Zhi Jin, Binhua Li, Fei Huang, Yongbin Li, Bin Gu, and Mengfei Yang. 2024. DevEval:
A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories. In Findings of the Association for
Computational Linguistics ACL 2024. Association for Computational Linguistics, Bangkok, Thailand and virtual meeting, 3603–3614.
https://doi.org/10.18653/v1/2024.findings-acl.214
[32] Jia Li, Yunfei Zhao, Yongmin Li, Ge Li, and Zhi Jin. 2024. AceCoder: An Effective Prompting Technique Specialized in Code Generation.
ACM Trans. Softw. Eng. Methodol. 33, 8, Article 204 (Nov. 2024), 26 pages. https://doi.org/10.1145/3675395
[33] Shanchao Liang, Nan Jiang, Yiran Hu, and Lin Tan. 2025. Can Language Models Replace Programmers for Coding? REPOCOD Says
‘Not Yet’. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Wanxiang
Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). Association for Computational Linguistics, Vienna,
Austria, 24698–24717. https://doi.org/10.18653/v1/2025.acl-long.1204
[34] Dianshu Liao, Shidong Pan, Xiaoyu Sun, Xiaoxue Ren, Qing Huang, Zhenchang Xing, Huan Jin, and Qinying Li. 2024. A3-CodGen: A
Repository-Level Code Generation Framework for Code Reuse With Local-Aware, Global-Aware, and Third-Party-Library-Aware. IEEE
Transactions on Software Engineering 50, 12 (Dec. 2024), 3369–3384. https://doi.org/10.1109/TSE.2024.3486195
[35] Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, Zhenpeng Chen, Lingming Zhang, and Yiling Lou. 2024. Large Language Model-Based
Agents for Software Engineering: A Survey. https://doi.org/10.48550/arXiv.2409.02977 arXiv:2409.02977 [cs].
[36] Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the
Middle: How Language Models Use Long Contexts. Transactions of the Association for Computational Linguistics 12 (2024), 157–173.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 34](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-34.png)

![Página PDF 34, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-34.png)


<!-- PDF page 35 -->

## Página PDF 35

LLM See, LLM Do
•
35
https://doi.org/10.1162/tacl_a_00638 Place: Cambridge, MA Publisher: MIT Press.
[37] Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. 2021. Pre-train, Prompt, and Predict: A
Systematic Survey of Prompting Methods in Natural Language Processing. http://arxiv.org/abs/2107.13586 arXiv:2107.13586 [cs].
[38] Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang. 2024. GraphCoder: Enhancing
Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph. In Proceedings of the 39th IEEE/ACM
International Conference on Automated Software Engineering. ACM, Sacramento CA USA, 570–581. https://doi.org/10.1145/3691620.
3695054
[39] Yang Liu, Li Zhang, Fang Liu, Zhuohang Wang, Donglin Wei, Zhishuo Yang, Kechi Zhang, Jia Li, and Lin Shi. 2025. RepoScope: Leveraging
Call Chain-Aware Multi-View Context for Repository-Level Code Generation. arXiv:2507.14791 [cs.SE] https://arxiv.org/abs/2507.14791
[40] Shuai Lu, Nan Duan, Hojae Han, Daya Guo, Seung-won Hwang, and Alexey Svyatkovskiy. 2022. ReACC: A Retrieval-Augmented Code
Completion Framework. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers). Association for Computational Linguistics, Dublin, Ireland, 6227–6240. https://doi.org/10.18653/v1/2022.acl-long.431
[41] Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. 2023.
WizardCoder: Empowering Code Large Language Models with Evol-Instruct. http://arxiv.org/abs/2306.08568 arXiv:2306.08568 [cs].
[42] Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023. CodeGen:
An Open Large Language Model for Code with Multi-Turn Program Synthesis. In The Eleventh International Conference on Learning
Representations. https://openreview.net/forum?id=iaYcJKpY2B_
[43] Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. 2023. In-Context
Retrieval-Augmented Language Models. Transactions of the Association for Computational Linguistics 11 (2023), 1316–1331. https:
//doi.org/10.1162/tacl_a_00605
[44] Kiran Ramnath, Kang Zhou, Sheng Guan, Soumya Smruti Mishra, Xuan Qi, Zhengyuan Shen, Shuai Wang, Sangmin Woo, Sullam
Jeoung, Yawei Wang, Haozhu Wang, Han Ding, Yuzhe Lu, Zhichao Xu, Yun Zhou, Balasubramaniam Srinivasan, Qiaojing Yan, Yueyan
Chen, Haibo Ding, Panpan Xu, and Lin Lee Cheong. 2025. A Systematic Survey of Automatic Prompt Optimization Techniques.
https://doi.org/10.48550/arXiv.2502.16923 arXiv:2502.16923 [cs].
[45] Laria Reynolds and Kyle McDonell. 2021. Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm. http:
//arxiv.org/abs/2102.07350 arXiv:2102.07350 [cs].
[46] Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H Chi, Nathanael Schärli, and Denny Zhou. 2023. Large
language models can be easily distracted by irrelevant context. In International Conference on Machine Learning. PMLR, 31210–31227.
[47] Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Schärli, and Denny Zhou. 2023. Large
Language Models Can Be Easily Distracted by Irrelevant Context. In Proceedings of the 40th International Conference on Machine Learning
(Proceedings of Machine Learning Research, Vol. 202), Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan
Sabato, and Jonathan Scarlett (Eds.). PMLR, 31210–31227. https://proceedings.mlr.press/v202/shi23a.html
[48] Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, and Torsten Scholak. 2023. RepoFusion: Training Code Models
to Understand Your Repository. http://arxiv.org/abs/2306.10998 arXiv:2306.10998 [cs].
[49] Kimi Team. 2025. Kimi K2: Open Agentic Intelligence. arXiv:2507.20534 [cs.LG] https://arxiv.org/abs/2507.20534
[50] Chong Wang, Jian Zhang, Yebo Feng, Tianlin Li, Weisong Sun, Yang Liu, and Xin Peng. 2025. Teaching Code LLMs to Use Autocompletion
Tools in Repository-Level Code Generation. ACM Trans. Softw. Eng. Methodol. (Jan. 2025). https://doi.org/10.1145/3714462 Just Accepted.
[51] Yue Wang, Weishi Wang, Shafiq Joty, and Steven C.H. Hoi. 2021. CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing,
Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). Association for Computational Linguistics, Online
and Punta Cana, Dominican Republic, 8696–8708. https://doi.org/10.18653/v1/2021.emnlp-main.685
[52] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou,
Donald Metzler, Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, and William Fedus. 2022. Emergent Abilities of
Large Language Models. http://arxiv.org/abs/2206.07682 arXiv:2206.07682 [cs].
[53] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. 2023. Chain-of-
Thought Prompting Elicits Reasoning in Large Language Models. http://arxiv.org/abs/2201.11903 arXiv:2201.11903 [cs].
[54] Di Wu, Wasi Uddin Ahmad, Dejiao Zhang, Murali Krishna Ramanathan, and Xiaofei Ma. 2024. Repoformer: Selective Retrieval for
Repository-Level Code Completion. In Forty-first International Conference on Machine Learning. https://openreview.net/forum?id=
moyG54Okrj
[55] Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2024. Agentless: Demystifying LLM-based Software Engineering
Agents. http://arxiv.org/abs/2407.01489 arXiv:2407.01489 [cs].
[56] Chunqiu Steven Xia and Lingming Zhang. 2024. Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42
Each using ChatGPT. In Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis. ACM, Vienna
Austria, 819–831. https://doi.org/10.1145/3650212.3680323
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 35](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-35.png)

![Página PDF 35, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-35.png)


<!-- PDF page 36 -->

## Página PDF 36

36
•
Zhang et al.
[57] Deheng Yang, Xiaoguang Mao, Liqian Chen, Xuezheng Xu, Yan Lei, David Lo, and Jiayu He. 2022. TransplantFix: Graph Differencing-based
Code Transplantation for Automated Program Repair. In 37th IEEE/ACM International Conference on Automated Software Engineering.
ACM, Rochester MI USA, 1–13. https://doi.org/10.1145/3551349.3556893
[58] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. 2024. SWE-agent:
Agent-Computer Interfaces Enable Automated Software Engineering. https://doi.org/10.48550/arXiv.2405.15793 arXiv:2405.15793 [cs].
[59] Ori Yoran, Tomer Wolfson, Ori Ram, and Jonathan Berant. 2024. Making Retrieval-Augmented Language Models Robust to Irrelevant
Context. In The Twelfth International Conference on Learning Representations. https://openreview.net/forum?id=ZS4m74kZpH
[60] Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie. 2024. CoderEval:
A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models. In Proceedings of the IEEE/ACM 46th International
Conference on Software Engineering. ACM, Lisbon Portugal, 1–12. https://doi.org/10.1145/3597503.3623316
[61] Daoguang Zan, Bei Chen, Zeqi Lin, Bei Guan, Wang Yongji, and Jian-Guang Lou. 2022. When Language Model Meets Private Library.
In Findings of the Association for Computational Linguistics: EMNLP 2022, Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.).
Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 277–288. https://doi.org/10.18653/v1/2022.findings-
emnlp.21
[62] Daoguang Zan, Bei Chen, Dejian Yang, Zeqi Lin, Minsu Kim, Bei Guan, Yongji Wang, Weizhu Chen, and Jian-Guang Lou. 2022. CERT:
Continual Pre-training on Sketches for Library-oriented Code Generation. In Proceedings of the Thirty-First International Joint Conference
on Artificial Intelligence, IJCAI-22, Lud De Raedt (Ed.). International Joint Conferences on Artificial Intelligence Organization, 2369–2375.
https://doi.org/10.24963/ijcai.2022/329 Main Track.
[63] Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen. 2023. RepoCoder:
Repository-Level Code Completion Through Iterative Retrieval and Generation. In Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing. Association for Computational Linguistics, Singapore, 2471–2484. https://doi.org/10.18653/v1/
2023.emnlp-main.151
[64] Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024. Codeagent: Enhancing code generation with tool-integrated agent systems
for real-world repo-level coding challenges. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers). 13643–13658.
[65] Tanghaoran Zhang, Yue Yu, Xinjun Mao, Shangwen Wang, Kang Yang, Yao Lu, Zhang Zhang, and Yuxin Zhao. 2025. Instruct or Interact?
Exploring and Eliciting LLMs’ Capability in Code Snippet Adaptation Through Prompt Engineering. In 2025 IEEE/ACM 47th International
Conference on Software Engineering (ICSE). 566–577. https://doi.org/10.1109/ICSE55347.2025.00104
[66] Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Abhik Roychoudhury. 2024. AutoCodeRover: Autonomous Program Improvement.
http://arxiv.org/abs/2404.05427 arXiv:2404.05427 [cs].
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 36](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-36.png)

![Página PDF 36, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-36.png)


<!-- PDF page 37 -->

## Página PDF 37

LLM See, LLM Do
•
37
A
Prompts for Baseline Methods
Please generate a step-wise plan for the given function `update` to divide 
a function-level task into steps and then complete it based on the 
following examples and the file context of the function.
# Here are some examples:
# --------------------------------------------------
```python
def digits(n: int) -> int:
  """
  Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1) == 1
  digits(4) == 0
  digits(235) == 15
  Plan:
    1. Initialize a product variable to 1.
    2. Initialize a counter for odd digits to 0.
    3. Convert the integer `n` to a string to iterate through each digit.
    ...
  """
  product = 1
  odd_count = 0
  for digit in str(n):
    int_digit = int(digit)
    if int_digit % 2 == 1:
      product = product * int_digit
      odd_count += 1
  if odd_count == 0:
    return 0
  else:
    return product
```
# --------------------------------------------------
...
# --------------------------------------------------
CoT Examples
# The contexts above the `update` function are:
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
class Volume(TaggedEC2Object):
  def __init__(self, connection=None):
    ...
  def ...
  
  def _update(self, updated):
    self.__dict__.update(updated.__dict__)
# The `update` function to complete is a method of `Volume` class, which is 
as follows:
  def update(self, validate=False, dry_run=False):
    """
    This function updates ...
    Input-Output Arguments:
    ...
    """
Intra-file Context
Target Function
Fig. 13. The prompt for CoT.
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 37](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-37.png)

![Página PDF 37, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-37.png)


<!-- PDF page 38 -->

## Página PDF 38

38
•
Zhang et al.
Please generate a plan for the given function `update` to divide a 
function-level task into steps based on the following examples and the file 
context of the function.
# Here are some examples:
# --------------------------------------------------
```python
def digits(n: int) -> int:
  """
  Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1) == 1
  digits(4) == 0
  digits(235) == 15
  """
```
# Plan:
[
  "Initialize a product variable to 1.", 
  "Iterate through each digit of n.", 
  "Multiply the product by each odd digit."，
  "Return 0 if the product remains 1, otherwise return the product."
]
# --------------------------------------------------
...
# --------------------------------------------------
Note that:
- Your plan should be a list of strings where each represents a single step.
- Your plan should describe the solution to the problem at the high level, 
where each step should describe what to do and for what purpose.
- Your plan should be concise and contain as few steps as possible.
- Each step in your plan should be written as ONE verb-object phrase.
- Each step in your plan should NOT contain titles as well as any markdown, 
latex or html syntax.
# Your Answer:
# The contexts above the `update` function are:
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
class Volume(TaggedEC2Object):
  def __init__(self, connection=None):
    ...
  def ...
  
  def _update(self, updated):
    self.__dict__.update(updated.__dict__)
# The `update` function to complete is a method of `Volume` class, which is 
as follows:
  def update(self, validate=False, dry_run=False):
    """
    This function updates ...
    Input-Output Arguments:
    ...
    """
Target Function
Intra-file Context
Plan Examples
Plan Instructions
Please complete the `update` function based on the plan and the file 
context of the function.
# The contexts above the `update` function are:
from boto.resultset import ResultSet
from boto.ec2.tag import Tag
from boto.ec2.ec2object import TaggedEC2Object
class Volume(TaggedEC2Object):
  def __init__(self, connection=None):
    ...
  def ...
  
  def _update(self, updated):
    self.__dict__.update(updated.__dict__)
# The `update` function to complete is a method of `Volume` class, which is 
as follows:
  def update(self, validate=False, dry_run=False):
    """
    This function updates ...
    Input-Output Arguments: ...
    Return: ...
    Plan:
      1. Check if the volume exists in EC2 by querying the EC2 API.
      2. Raise a ValueError if the volume does not exist and the validate 
parameter is True.
      3. Update the volume's attributes with the data returned from the EC2 
API.
      4. Return the updated status of the volume.
    ""“
Target Function
Intra-file Context
Instruction
Fig. 14. The prompt for Self-Planning.
Received 4 November 2025; revised 21 June 2026; accepted 19 September 2026
ACM Trans. Softw. Eng. Methodol.

[Vista original de la página 38](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-38.png)

![Página PDF 38, representación visual original](../../../../../../images/v5/estructura_colecciones/Same%20Solution/terceary/not_processed/llm%20see%20llm%20do/page-38.png)
