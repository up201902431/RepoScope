# RepoMind

- source_pdf: ../../../../../pdf/Same%20Solution/primary/RepoMind.pdf
- extraction_tool: pdfplumber
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

RepoMind: Enhancing Repository-Level Code Generation via
LLM Reasoning over Structured Repository Documentation
Songwen Gong∗ Mengzhen Wang∗
South China University of Technology South China University of Technology
Guangzhou, China Guangzhou, China
202421045674@mail.scut.edu.cn 202311089439@mail.scut.edu.cn
Jiexin Wang Yi Cai†
South China University of Technology South China University of Technology
Guangzhou, China Guangzhou, China
jiexinwang@scut.edu.cn Key Laboratory of Big Data and Intelligent Robot (SCUT),
Ministry of Education
Guangzhou, China
ycai@scut.edu.cn
Abstract CCS Concepts
Repository-level code generation aims to generate target code • Software and its engineering → Automatic programming.
conditioned on the context of the specified repository. Existing
approaches generally adopt the Retrieval-Augmented Generation Keywords
(RAG) framework to retrieve relevant contextual information from
Repository-Level Code Generation, Retrieval-Augmented Genera-
the repository, thereby mitigating the challenge of long context
tion, Code Retrieval, Large Language Models
windows. However, these methods typically struggle to identify
truly relevant information for the current generation requirement, ACMReferenceFormat:
and they generally overlook the imperative need for understanding Songwen Gong, Mengzhen Wang, Jiexin Wang, and Yi Cai. 2026. Repo-
the repository-level code structure during the retrieval process. To Mind: Enhancing Repository-Level Code Generation via LLM Reasoning
addresstheseissues,weproposeRepoMind,anovelframeworkthat overStructuredRepositoryDocumentation.In34thIEEE/ACMInternational
advances repository-level code generation by leveraging a repos- ConferenceonProgramComprehension(ICPC’26),April12–13,2026,Riode
itory documentation library and LLM reasoning capabilities for
Janeiro,Brazil.ACM,NewYork,NY,USA,12pages.https://doi.org/10.1145/
3794763.3794823
API retrieval. Specifically, RepoMind first introduces the RepoDocs
Agent. This component constructs multi-granularity, hierarchical
structural documentation in a bottom-up manner, providing LLMs
1 Introduction
with a high-quality knowledge base for understanding repository
functionality and structure. Built upon this hierarchical knowledge Code generation [38, 45, 51] aims to automatically generate code
base, RepoMind further integrates the Reasoning-Retrieval Agent. according to natural-language specifications, demonstrating great
This agent mimics human developer patterns by utilizing the repos- potential and practical value in improving software development
itory documentation for layer-by-layer exploration, and ultimately efficiency. In recent years, Large Language Models (LLMs) such
precisely localizes the relevant API sets. Finally, the framework as GPT-4o [19], Qwen3 [43], and Deepseek-V3 [25] have shown
combines the functionally relevant API set retrieved via LLM rea- rapid capability advancement, achieving outstanding performance
soningwiththesemanticallysimilarAPIsetretrievedbythevector in standalone code generation tasks [7, 9, 18]. However, their per-
retriever, utilizing this hybrid context to boost code generation formance often degrades significantly when tackling more complex
performance. Evaluation on widely-used repository-level code gen- repository-level code generation tasks. Repository-level code gen-
eration benchmarks, CoderEval and DevEval, demonstrates that eration aims to generate target code conditioned on the broader
RepoMind surpasses state-of-the-art methods, achieving up to a context of the repository. Despite its critical nature, this remains a
13.50% relative improvement in Pass@1 scores. The open-source challenging task because the limited context window of LLMs re-
code will be released at https://github.com/ABigTrouble/RepoMind. strictsaccesstothebroaderprojectcontextandhindersastructured
understanding of repository knowledge [5].
∗Bothauthorscontributedequallytothisresearch. To mitigate these limitations, most existing methods adopt the
†Correspondingauthor.
RAG [13] paradigm, retrieving relevant contextual information
from the code repository to support more accurate code genera-
tion. Early approaches leverage code context as a query to retrieve
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. similar code snippets [41, 47], or employ static analysis [23] and
ICPC’26,RiodeJaneiro,Brazil draft-generated code [6, 24] to identify semantically related APIs.
©2026Copyrightheldbytheowner/author(s).
More recent research tends to exploit graph-based representations
ACMISBN979-8-4007-2482-4/26/04
https://doi.org/10.1145/3794763.3794823 to capture the complex dependencies within repositories, including
355

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
However, dict_merge introduces terms in its summary that are se-
. L . O . G = logger.LOG Generation requirement mantically dissimilar to the requirement, such as recursively merges.
de f d " i " c " t i _ n i s n e s r e t r t a ( d v i a c l , u e v a o l f , a k e n y e , s t * e k d ey k s e ) y : into a dictionary Crucially, recursively merges is strongly functionally relevant to
to insert value for a nested key, all ancestor keys should be given nested key mentioned in the generation requirement, as nested
as method's arguments
example: structures often require a recursive solution. Despite this strong
dict_insert({}, 'val', 'key1.key2'.split('.'))
:param dic: a dictionary object to insert the nested key value into functional link, these two terms are not close in the semantic space,
:param val: a value to insert to the given dictionary
:param key: first key in a chain of key that will store the value consequently leading to retrieval failure.
:param keys: sub keys in the keys chain When the retrieved context exhibits superficial similarity but
""" infrared
lacks genuine functional relevance, it often misguides the LLM,
Function summary: ...merge two lists Similarity-based therebydegradingthefinalqualityofthegeneratedcode.Although
contained within dictionaries, specifi- retrieval result
c
t
a
h
l
e
l y
v al
un
u
d
e
e
s
r
. .
a
. s
gi
ec
v
o
en
nd
k
l
e
i
y
s
.
t
I
a
t
n d
c he
a
c
p
k
p
s
e n
i
d
f
s ...
sever
c
a
o
l
m
s
m
tr
o
u
n
cture-aware methodisns[p4e,c1to1r, 32] attempt to mivtaiglidaatteors.py
ConflictResolver
def unique_append_list_resolver(first, second, key): th..i.svailsisduateesb yobjineccto cropmpoar-ating .. d . e fa p c e il n i d ta e t n in c g y se r a e m l l a e t s i s o nsh.i.p. scoomrpldiaantcae -wfliothw predefined This class provides methods to
if isinstance(first[key], list) and isinstance(second[key], intifboirlmitya twiiotnh ,JtShONe yforsmtaitll..e.ncoeuxnectuetriodn ibffiy ccuonlftiiremsinign..e.ffesccthievmeasly foars sAenssisbilne gconfigurations... handle key conflicts...
list):... core utils dict_utils.py dict_merge
the practical relevance of the retrieved context.
...enhances output management ...dictionary operations, ...merging dictionaries …is merge two dictionaries...
Function summary ...merge two dictionaries Relevant API byL caoncskoliodfatRinge pdaotas itory-LevsetrleUamlnindiengr.s.t.anding in Rwheilter ieeffveactli.veElxy.-.. recursively merges...
. t . h . e i w r h i va l l e u h e a s n . d l I i f n g b o p t o h t e d n i t c i t a i l o n c a o r n i f e l s i c h t a s v e i n is h t a i n n d g lin m g e .. t . hodologies also general…ly overlook the imperative…need …
the same key and the values associated with that key are also api.py
dictionaries, it recursively merges those dictionaries... for understanding the repository-level code, which is pivotal for
This module enables the
def dict_merge(first, second,
acinctuegrraatteiolny orfe tprluiegivnisn igntroe .l.e.vant context. Failing to grasp the global
conflict_resolver=...): reposit…ory structure and its functional interfaces during retrieval
significantly increases the likelihood of retrieving irrelevant con-
def dict_insert(dic, val, key, *keys): Target function
if dic is None: tent. For example, some existing approaches [14, 24] employ a
return generate-then-retrieve paradigm where the draft-generated code
if not keys:
if isinstance(dic.get(key, None), dict) and isinstance(val, dict): lacks prerequisite knowledge of the available repository’s function-
dict_merge(dic[key], val)
else: alities. This fundamental oversight creates an erroneous starting
dic[key] = val
point that severely misguides the subsequent retrieval phase, mak-
return
dict_insert(dic.setdefault(key, {}), val, *keys) ing it challenging to locate genuinely relevant code.
To address these limitations, we propose RepoMind, a novel
frameworkthatadvancesrepository-levelcodegenerationbylever-
Figure 1: A motivating example. Similarity-based retrieval
aging the repository’s documentation library for relevant context
method often struggles to retrieve relevant information.
retrieval via LLM reasoning. Specifically, RepoMind begins by em-
represents semantically similar content. represents func-
ploying the RepoDocs Agent to construct a hierarchical, multi-
tionally relevant content. represents the API invoked by
grained structured documentation (API-Doc, File-Doc, and Module-
the target function.
Doc) in a bottom-up manner, thereby providing the LLM with a
rich background knowledge base for relevant API retrieval. Subse-
quently, retrieval begins with a vector retriever to gather a set of
dataflow analysis [11], repository-level semantic graph construc- similarity-based APIs, providing a preliminary retrieval direction
tion [33], control-flow, data-dependence modeling [27], and API for the subsequent relevance retrieval. Building on this initial direc-
callchainprediction[28].Meanwhile,agent-basedpipelinesfurther tion, the Reasoning-Retrieval Agent analyzes the coarse-grained
extendthesecapabilitiesthroughtoolinvocation,iterativeretrieval, Module-Doc descriptions to infer the specific sub-modules or files
and feedback evaluation [10, 30, 48]. While these methods have highlyrelevanttothegenerationrequirement.Theagentiteratively
significantly improved repository-level code generation, several narrows the search scope, ultimately pinpointing the relevant set
challenges remain. of APIs within the identified Python files. This approach, which
Insufficient Relevance in Similarity-Based Retrieval. In mimics developer cognitive patterns, effectively overcomes the rel-
the RAG framework, the identification of genuinely relevant con- evance shortcomings of traditional similarity-based retrieval. By
text is a critical determinant of the generated code’s functional continuously integrating repository structure and functionality
correctness. However, existing similarity-based retrieval methods into the retrieval process, RepoMind significantly boosts retrieval
[12,14,24]aretypicallyemployedtoretrieveAPIsthataretextually accuracy. Finally, by integrating both the functionally relevant API
or semantically similar, while struggling to capture functionally set and the semantically similar API set for code generation, Repo-
relevant information required for the generation requirement [37]. Mind elevates the final quality of the generated code. We evaluate
As illustrated in Figure 1, a similarity-based retrieval approach RepoMind on two widely-used repository-level code generation
(as indicated by the orange box content) identifies the function benchmarks, CoderEval [46] and DevEval [21], using three back-
unique_append_list_resolver, whose functional summary is simi- bone LLMs and conduct comprehensive experiments. The evalua-
lar to the generation requirement, but fails to retrieve the func- tion results demonstrate that RepoMind outperforms the baseline,
tionally relevant API, dict_merge (as indicated by the green box achieving up to 13.50% relative improvement in Pass@1 score.
content). The functional summaries of unique_append_list_resolver In summary, the contributions of our work are as follows:
and dict_merge both exhibit a degree of semantic similarity to the
generation requirement, containing terms like key and dictionaries.
356

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

...
from infrared.core.utils import logger Generation requirement
LOG = logger.LOG
def dict_insert(dic, val, key, *keys):
"""insert a value of a nested key into a dictionary to insert value for
a nested key, all ancestor keys should be given as method's arguments
example:
dict_insert({}, 'val', 'key1.key2'.split('.'))
RepoMind: Repo-LevelCodeGenviaLLMReasoningoverStructuredDocumentation ICPC’26,April12–13,2026,RiodeJaneiro,Brazil
:param dic: a dictionary object to insert the nested key value into
:param val: a value to insert to the given dictionary
:param key: first key in a chain of key that will store the value
:param keys: sub keys in the keys chain
""" infrared
# core.utils.dict_utils.ConflictResolver. Similarity-base retrieval
unique_append_list_resolver
def unique_append_list_resolver(first, second, key): common inspector validators.py ConflictResolver
""“...merge two lists contained within dictionaries, specif-
ically under a given key. It checks if the values ...second ...validates object compa- ...facilitating seamless ... compliance with predefined This class provides methods to
list and appends ...""“ tibility with JSON format... execution by confirming... schemas for Ansible configurations... handle key conflicts...
core utils dict_utils.py dict_merge
...enhances output management ...dictionary operations, ...merging dictionaries …is merge two dictionaries...
relevance-base retrieval by consolidating data streamlining... while effectively... recursively merges...
d e f d i c t _ m c e o r n g f e l ( i f c i t r _ s r t e , s o s l e v c e o r n = d . , ..): handling ... … … …
""“...merge two dictionaries,..., while handling potential api.py
conflicts in their values. If both dictionaries have the same
key and the values associated with that key are also diction- This module enables the
aries, it recursively merges those dictionaries...""“ integration of plugins into ...
…
def dict_insert(dic, val, key, *keys):
Figure 2: The process of developers leveraging repository documentation to perform hierarchical reasoning retrieval for the
if dic is None: Target function
return generation requirement in Figure 1.
if not keys:
if isinstance(dic.get(key, None), dict) and isinstance(val, dict):
dict_merge(dic[key], val)
else: • We introduce RepoMind, a repository-level code genera- and finally, locating the API set highly relevant to the requirement.
dic[key] = val
return tion framework that leverages LLM reasoning over reposi- As shown in Figure 2, documentation-driven reasoning yields the
dict_insert(dic.setdefault(key, {}), val, *keys) tory documentation. By integrating hierarchical repository correct retrieval path: infrared → core → utils → dict_utils.py →
knowledge and LLM-based retrieval to identify function- dict_merge. This path is derived by iteratively leveraging reposi-
allyrelevant contexts, RepoMind consequentlyimprovesthe tory documentation, such as recognizing merging dictionaries in
performance of repository-level code generation. dict_utils.pyandrecursivelymerges infunctiondict_merge,whichis
• We introduce the RepoDocs Agent, which constructs multi- functionallyrelevanttothetargetfunction.Comparedtosimilarity-
granularity repository documentation. The resulting struc- based matching, this documentation-guided retrieval not only sig-
tured knowledge enables accurate context retrieval by pro- nificantly improves retrieval accuracy but also provides a deeper
vidingrichbackgroundinformationforunderstandingrepos- understanding of the underlying repository structure during the
itory functionality. retrieval process.
• We introduce the Repository-Reasoning Agent, which per- Ourresearchmotivationispreciselyfocusedonthedocumentation-
forms LLM-based retrieval from coarse-grained modules to guided, hierarchical, and reasoning-based retrieval paradigm, aim-
fine-grained APIs. This process mimics developers’ reason- ing to enhance the accuracy of API retrieval.
ing process when navigating large repositories, effectively
mitigating the limitations of pure similarity-based retrieval. 2.2 Repository-level Code Generation
• Weconductextensiveexperimentsontwowidely-usedbench- Prior to the advent of LLMs, code generation techniques have
marks, CoderEval [46] and DevEval [21], across three back- achieved significant breakthroughs, yet these advancements are
bone LLMs. The results show that RepoMind outperforms limited to standalone code snippets. As the rapid development of
strong baselines, achieving up to 13.50% relative improve- LLMs has led to substantial improvements in both code generation
ment in Pass@1, and demonstrating superior retrieval accu- capacity and context window length, research focus has shifted to-
racy and generation quality. wardthemorechallengingtaskofrepository-levelcodegeneration,
thereby addressing the development needs of complex, real-world
2 Preliminaries software projects.
In this context, the RAG framework has been broadly adopted in
2.1 Motivation Example
the repository-level code generation methods. The repository-level
In practical repository-level code development, a core challenge in code generation process can be formally formulated as follows:
efficiently and compliantly transforming a generation requirement
𝐶𝑜𝑑𝑒 = Generate(𝑟,Retrieval(𝑟,Repository)) (1)
into code lies in how to rapidly understand the repository structure
and retrieve relevant context from massive information. where Repository represents the given code repository, and r is
Consequently, to effectively accomplish code generation, devel- the generation requirement of the target function. The function
opers must leverage repository documentation (e.g., README.md, Retrieval(·) extractsrelevantinformationfromtheRepository based
module overviews) to hierarchically understand the repository. on the generation requirement, while Generate (·) integrates the
These documents provide critical information regarding the project retrievedinformationwiththeoriginalgenerationrequirementand
structure and module functionalities, which is essential for rapidly utilizes LLMs to generate the target code.
retrieving the relevant API set. Developers employ a top-down The types of the retrieved information can be broadly classified
exploration process: first, grasping the macro-architecture via doc- into three categories: similar code, API, and context.
umentation; next, pinpointing the core module corresponding to Similar code. It refers to the similar code snippets retrieved
the generation requirement; then, exploring the files of the module; from the same repository, based on the fundamental assumption
357

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
API-Database RepoDocsAgent
Generation
Code Repository requirement
M
AST
C Retriever
F
API-Docs File-Docs Module-Docs Similarity retrieval
API-Database results
RepoDocs
(1) RepoDocs Construction (2) Similarity-Based Retrieval
(3) LLM-Reasoning-based Retrieval (4) Code Generation
root/dir1
Generation root/ Generation
requirement dir2 requirement
dir1
3.py
Retrieve
1.py LLM
Target Code
Relevance
retrieval
2.py
Similarity Reasoning- results
Retrieval Retrieval Agent
results
Figure 3: Workflow of RepoMind.
that these analogous pieces of code share stylistic, structural, or LLM-Reasoning-based Retrieval stage, we propose the Reasoning-
functional characteristics with the target code being generated. Retrieval Agent, which leverages the previously constructed Re-
APIretrieval.ItfocusesonidentifyingrelevantAPIsthatshould poDocs and the similarity-based API set to perform LLM-guided
be invoked in the target code. The primary goal is to reduce code reasoning. Its primary goal is to retrieve APIs that are functionally
redundancy while simultaneously enabling customization and sup- relevant to the generation requirement, rather than merely similar.
porting complex functionality. Providing information on available Finally, both the functionally relevant API set and the semantically
APIs helps capture partial functionality within the overall genera- similar API set are integrated into a prompt, which is fed into the
tion requirement, thereby improving code reusability and reducing LLM to generate the target function.
implementation difficulty.
Context.Itreferstocontextualinformationfromthesamefileas 3.2 RepoDocs Construction
thefunctionrequirement.Itincludesdetailssuchaslibraryimports,
High-qualityrepositorydocumentationisindispensableforthesoft-
class definitions, and method implementations. This information
waredevelopmentlifecycle.Suchdocumentationsignificantlyhelps
helps LLMs better understand the code style, reduce redundancy,
LLMs in better comprehending the repository structure and pro-
and correctly interpret the target generation requirement.
videsarobustfoundationforreasoningduringtheretrievalprocess,
enabling them to make more accurate inference decisions when
3 Approach
retrieving relevant APIs. Therefore, we propose RepoDocs Agent, a
3.1 Overview framework for generating high-quality repository documentation.
It consists of DocsWriter, which generates the documentation con-
With the key insights presented in Section 2.1, we propose the
tent, and DocsVerifier, which evaluates the quality of the generated
RepoMind framework, which generates repository-level functions
documentation and provides revision suggestions. The construc-
by leveraging an LLM-based reasoning process over the reposi-
tion process of the RepoDocs Agent strictly adheres to a bottom-up
tory’s documentation library. As illustrated in Figure 3, RepoMind
manner: it initially generates fine-grained API descriptions (API-
comprises four primary stages: RepoDocs Construction, Similarity-
Doc),andsubsequentlyaggregatestheintra-fileAPIdescriptionsto
Based Retrieval, LLM-Reasoning-based Retrieval, and Code Gen-
produce the file’s functional description (File-Doc). Furthermore, it
eration. In the RepoDocs Construction stage, we introduce the Re-
recursivelyleveragesthefunctionaldescriptionsofallfilesandsub-
poDocs Agent, which employs a bottom-up methodology to build
directories within a directory1 to generate the module’s functional
RepoDocs,amulti-graineddocumentationlibrary.Thiscomprehen-
summary (Module-Doc). Thus, the RepoDocs are systematically
sive library provides the reasoning foundation for the subsequent
constructed. The template of RepoDocs is illustrated in Figure 4.
retrieval stage. Subsequently, RepoMind employs a vector retriever
to gather a set of similarity-based APIs, providing a preliminary
retrieval direction for the subsequent relevance retrieval. In the 1Inthispaper,themodulecorrespondsdirectlytothedirectory.
358

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

RepoMind: Repo-LevelCodeGenviaLLMReasoningoverStructuredDocumentation ICPC’26,April12–13,2026,RiodeJaneiro,Brazil
3.2.1 Dependency Graph Construction. To achieve the generation
...
from infrared.core.utils import logger Generation requirement Root/dir1o/ffhilieg1h.lpyy.pmredcise repository documentation, a c F o i m le p - re D h o en c sive com- Root/dir1/file1.py.md
LOG = logger.LOG prehension of the dependency structure within the repository is a File-Doc
def dict_insert(dic, val, key, *keys): # Python Code Analysis # Python Code Analysis
"""insert a value of a nested key into a dictionary to insert value for ## Over p a r l e l r C e o q d u e i s F it u e n . c R ti e on p a o l D ity ocs Agent initially performs Abstract Syntax ## Overall Code Functionality
a nested key, all ancestor keys should be given as method's arguments [Use cleTarre ean(Ad SdTi)repcatr slinanggounagael ltsoo udrecsecrfiilbees atchreo sfsilteh’esr empaions itory. This [Use clear and direct language to describe the file’s
example: functionssy,s tekmeya tcicappaabrislinitgifeasc,il iatantde sltihmeitaactciuornaste, ihdeelnptiifincga tuisoenrsa nqdueixctkrlayc - main functions, key capabilities, and limitations,
dict_insert({}, 'val', 'key1.key2'.split('.')) assess its suitability. Also explain the module’s role within the helping users quickly assess its suitability.]
:param dic: a dictionary object to insert the nested key value into system, t f io o n cu o s f in c g o d o e n e w n h t a it t i e i s, t sp do e e c s ifi r c a a t ll h y er c la t s h s a e n s , h m ow e t i h t o d w s o , r a k n s d .] functions,
:param val: a value to insert to the given dictionary alongwiththeirinterdependencies.Thesedependenciesencompass ## Class & Structure Analysis
:param key: first key in a chain of key that will store the value ## Classfu &n cStitornuc/mtuerteh oAdnaclaylsliss,class inheritance relatioAnsPhiIp-s,Danodcattribute ### Class API
: " p " a " ram keys: sub keys in the keys chain # - # Su # m m C a la r a y scs : c [ eA o sP n sIe e s - . l S i u ne b se d q es u c e r n i t p ly t , i t o h n e f e o x c tr u a s c i t n e g d i o n n t e W r H d A e T p e t n h d e e n c c l i a e s s s a reutilized - - S D u e m s m c a r r i y ption
representtosc,o nfostcruusc totnh ethceo dceordee ppeunrdpoesnec yogr rarpeshpfoonrsithbielrietpyo]sitory. - Parameters API-Doc
# core.utils.dict_utils.ConflictResolver. Similarity-base retrieval - Description:[Describe scenarios or conditions where this class - Attributes
unique_append_list_resolver should b3e.2 .u2sedA]PI-Doc. The functionality exposed by a code entity is in- - Example
- Attributes:[explain the significance and type of each parameter] #### def method(self,arg1):
def unique_append_list_resolver(first, second, key): - Parame t t ri e n r s s i : c [ a e ll x y pl re a l i a n t e t d h n e o p t u o r n p l o y se to , i s ts ig s n o i u f r i c c e a c n o c d e e a b n u d t t a y ls p o e t o o f i t e s a c c a h l lees. - Summary
"""Merges first and second lists """ attributFeu]rthermore, the functionality of a method is also influenced by - Description
if isinstance(first[key], list) and isinstance(second[key], list): - Examplites:[ssuhrorwo uan dpirnagctciocnalte,x tr,enala-mwoerlyldt huesacglaes sscietnbaerlioon]gs to. Beyond - Args
for item in second[key]: - Returns
if item not in first[key]: #### d t e h f is m , t e h t e ho c d a ( l s le e r lf s , o ar f g a 1) c : ode entity provide crucial clues regarding its - Raises
first[key].append(item) - Summarpyr:e[coinsee-ulsiangee daenscdrpiputripoons ef.oCcuosnisnegq uoenn WtlHyA,TR tehpeo DfuonccstAiogne ndtoepsr e- - Example
...
# core.cli.cli.NestedBase._resolve a - n D d e s e c m r p i hp p aa t sr i ie o zs n ea : t [ c e ho x em p l op a ure i th n c oe t mn h es e iv oe p r u c r eo p fn o ft s ee e cx tt a ]d n e d r i u v s e e d f r a o n m d t d h e e sc d r e i p b e e n d w e h n e c n y t g o r a u p s h e ## Function Analysis
this fun c c o t n i s o t n r ] ucted in the prior step for the DocsWriter, encompassing the ### def funcA(arg1):
def _resolve(self, value，skip_nested_split=False): - Args:[seoxuprlcaeinc otdhee osfitghneiftaicrganectec oadned etnytpitey ,otfh eeaccahl lepeasr,aamnetdetrh]e callers. - Summary
.. . # allow escaping the . (dot) in key of nested dictionaries - - R R e a t i u s r e n s Fs : o: [ r[ l em i x s ep t tl ha s oi p dn e s c ,w i th f ha i et c st c oh o ue n r d cr i ee t ct i ou o r n dn s e ov t fa r l i thu g e g e e er r ne i cp n lr g oe ss e ien a n c gt h cs l] e a x s c s e i p s t a i d o d n] itionally - - D Ar e g s s cription:
keys = [k.replace('\\', ‘’) for k in re.split(r'(?<!\\)\.', key)] - Examplper:o[vSihdoewd .pTrhacistiriccahl cuosnatgeex tsicseunsaerdiotso]guide the LLM in generating - Returns
di ct _ r u e t t i u l r s n . d r i e c s t u _ l i t n s s _ e d r i t c ( t results_dict, _value, *keys) the precise API documentation. For distinct types of code entities, - - E R x a a i m s p e l s e
... RepoDocs Agent structures the documentation content differently:
## Function Analysis
Methods/Functions description includes a brief summary, detailed
### def funcA(arg1): root/dir1/dir.md
- Summardye:s[cornipet-iloinn,ei ndpeustcrpiaprtaimone tefrosc,uosuitnpgu tonp aWrHaAmT ettehres ,feuxnccetpitoino ndso,easn d
de f d i i f c t d _ i i c n s is e r N t o ( n d e i : c, val, key, *keys): Target function a - n d D e e s m c p r h i ea p xs t ai i mz o e n p : let [ s e h;e x C p o l lau a st i sc n eo sm t e h d e eo sr p c u rie r pf p tf o ie s oc e nt c] a o n m d p u r s i e s e s a a nd b r d ie e f sc su ri m b m e a w r h y e , n d e t t o a i u le s d e # Python Code Analysis Module-Doc
return this fundcetsicornip]tion, constructor parameter descriptions, attributes, and ex- ## Overall Code Functionality
if not keys: - Args:[aemxppllaeis.n Stuhbes esqiugenniftliyc,atnhcee gaennde rtaytpeed oAfP Ieadcehs cpraiprtaimoent,earl]ong with [Use clear and direct language to describe the module’s
if isinstance(dic.get(key, None), dict) and isinstance(val, dict): - Returns:[explain what the return value represents] main functions, key capabilities, and limitations,
dict_merge(dic[key], val) - Raises t : h [ e l e i n s t t i ty sp ’s e s c o i u fi rc c e c c o o n d d e it a i n o d n i s t s t c r o i n g t g e e x r t i , n is g fe e d ac t h o t e h x e ce D p o t c i s o V n e ] rifier to helping users quickly assess its suitability.]
else: - Examplreig:o[Srohouws lypraascsteiscsailts uqsuaaglei tys.cUenpaornioesv]aluation, the DocsVerifier ei-
dic[key] = val
therapprovestheAPIdescriptionorprovidesspecificimprovement
return
suggestions to the DocsWriter for the next generation iteration. Figure4:ThetemplateofAPI-Doc,File-Doc,andModule-Doc
dict_insert(dic.setdefault(key, {}), val, *keys) root/dir1/dir.md in a markdown format.
3.2.3 File-Doc. Despitethegenerationofhigh-qualitydescriptions
# Pythonfo Crotdhee Arenaployssiistory’s APIs, significant limita M tio o n d s u pe le rs - is D t o in c the re-
## Overall Code Functionality
trievalstage.Inparticular,thesheerquantityofAPIsoftenprevents
[Use clear and direct language to describe the module’s main 3.2.4 Module-Doc. Although File-Doc summarizes the function-
functiontsh,e iknecylu csiaopnaboiflailtliAePsI,d easncdr ilpitimointsatwiiotnhsin, thheelpprionmg putsceornst eqxuti.cEkvleyn
assess iatssL sLuMitsacboilnititnyu. eAtlosos uepxppolratinlo nthgee rmcoodunltee’xst, rtholeey mwiatyhionv etrhleo ok alities of the API-Docs, repositories comprising a large number of
system, focusing on what it does rather than how it works.] files can still increase the difficulty for the LLM to comprehend
critical details in extremely long contexts [26]. Furthermore, an
the repository. Consequently, the RepoDocs Agent is tasked with
extended context saturated with irrelevant or noisy information
further compressing and abstracting the File-Doc. Specifically, the
can become a source of interference.
RepoDocs Agent employs a recursive process, commencing ab-
Consequently, there is an imperative need to further condense
straction from the deepest module layer. For any given module,
and abstract the functional descriptions of the APIs. To achieve
RepoDocs Agent utilizes the functional descriptions of all its sub-
this, the RepoDocs Agent utilizes all previously generated API-
modules and all direct files as the DocsWriter’s context to generate
Docs within a Python file as the context for DocsWriter. DocWriter
the module’s concise functional description (Module-Doc). Analo-
then produces a brief functional description for the file (File-Doc).
goustotheprecedingstage,thisdescriptionisthensubjectedtothe
Following this, the File-Doc is subjected to the same assessment
DocsVerifier’s assessment and feedback mechanism to determine
and feedback mechanism via the DocsVerifier as in API-Doc con-
the necessity of subsequent generation iterations. This mechanism
struction. Finally, a large number of fine-grained API-Docs are
effectively condenses and abstracts the medium-grained File-Doc
condensed and abstracted into a medium-grained File-Doc.
into the coarse-grained Module-Doc.
𝐹 𝑖 = DocsWriter(𝐴 𝑖) (2) Ultimately, the RepoDocs Agent completes the bottom-up con-
struction of the comprehensive repository documentation library,
where 𝐹 𝑖 represents the 𝐹𝑖𝑙𝑒-𝐷𝑜𝑐 corresponding to 𝑓𝑖𝑙𝑒 𝑖, 𝐴 𝑖 = RepoDocs. Furthermore, the API-Docs are isolated to function as
{𝐴 𝑖1, ,𝐴 𝑖2 ,...,𝐴 𝑖𝑛} represents the set of all API-Doc for 𝑓𝑖𝑙𝑒 𝑖 and an independent retrieval database, API-Database, the specific role
𝐴 𝑖𝑗 is the API-Doc of the 𝑗-th code entity in 𝑓𝑖𝑙𝑒 𝑖. of which will be detailed in the section 3.3.
359

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
3.3 Similarity-Based Retrieval identifiedfiles.Concurrently,theAgentgainsaholisticunderstand-
To mitigate the inherent ambiguity in the generation requirement, ing of the repository’s structure and functionality throughout the
similarity retrieval is employed to secure contextual information. retrieval process.
This information provides an initial retrieval direction and implicit Retrieval Process. The retrieval process is initiated by using
semantic constraints for the subsequent retrieval process detailed the top_K similarity-based retrieval results 𝑆𝐴, along with their
in Section 3.4. Specifically, for every API, we extract and concate- corresponding API paths and the generation requirements as a part
nate the brief summary and the detailed description from API-Doc of the prompt to provide an initial retrieval direction for the LLM.
to form the API-Database entries. Subsequently, the generation Subsequently, it performs top-down reasoning and retrieval based
requirement is encoded into a representation vector using the same on the repository’s inherent hierarchical structure. Specifically,
pre-trainedmodelappliedforencodingAPIdescriptionsintheAPI- the Reasoning-Retrieval Agent invokes the explore_folder_structure
Database. API retrieval is then performed using a cosine similarity tool on the root directory to obtain the tree structure and concise
score to yield the top-K most similar APIs from the API-Database functionalities; then, utilizing the LLM’s reasoning capability to
for the generation requirement. determine which subdirectories or files are likely relevant to the
generation requirement. If the determination points to a directory,
𝑆𝐴 = Retriever(𝑟,API-Database) (3) the Agent continues the downward exploration by iteratively in-
voking explore_folder_structure tool. If a Python file is identified,
where r is the generation requirement, API-Database represents
theAgentinvokesexplore_api_file toacquireallcorrespondingAPI-
the retrieval library where each entry is a brief API description,
and SA = {𝑠𝑎 1 ,...,𝑠𝑎 𝐾} represents the set of 𝐾 APIs that have the Docs within the file. These API-Docs are then provided as context,
highest similarity score to the functional description𝑟. thereby successfully filtering the repository’s all API down to a
small set of API within a few Python files, drastically reducing the
context length. Finally, the powerful reasoning capacity of the LLM
3.4 LLM-Reasoning-based Retrieval
is leveraged to select the core API set that is highly relevant to the
FollowingtheRepoDocsconstructionandsimilarity-basedretrieval, generation requirement.
RepoMind proceeds to precisely simulate the developer’s program- Evaluate the retrieval Results. Following the retrieval of the
ming process. Since the abstract, top-level Module-Doc may lack relevant API set, the Reasoning-Retrieval Agent executes a post-
obviousrelevancetothegenerationrequirementatthebeginningof evaluation process on the results. Specifically, this evaluation in-
retrieval, we utilize the paths of the similarity-based API set𝑆𝐴 as volves two key aspects: first, a secondary filtering is performed by
preliminary retrieval guidance. With this guidance, the Reasoning- instructing the LLM to review the direct relevance of the retrieved
Retrieval Agent performs hierarchical retrieval of relevant APIs APIs to the generation requirements; and second, the accuracy of
within the RepoDocs. theAPIpathsisverifiedandcorrected.Finally,theretrievalprocess
concludes by presenting the refined and verified API set 𝑅𝐴.
3.4.1 Tools Design for RepoDocs Exploration. To facilitate effec-
Through the top-down reasoning mechanism, the Reasoning-
tive interaction between the Reasoning-Retrieval Agent and Re-
Retrieval Agent achieves a holistic understanding of the reposi-
poDocs, we designed two dedicated tools for its operation: ex-
tory’s structure and functionality. This process leverages the LLM’s
plore_folder_structure and explore_api_file.
powerful inference ability to retrieve the key APIs that are truly
explore_folder_structure: Inspired by how programmers typi-
relevant (rather than merely similar) from the massive API data-
cally consult Readme.md to identify the appropriate module, the
base. Crucially, due to the inherent reasoning capabilities of the
Reasoning-Retrieval Agent invokes this tool to retrieve the con-
LLM, this retrieval process also exhibits interpretability, a feature
cise Module-Doc and File-Doc of all subdirectories and direct files
fundamentally lacking in traditional vector retrieval. The retrieval
within a specified directory path. The results are returned in a di-
outcomeisthereforenotmerelyalistofsimilarityscores,butrather
rectory tree structure. The usage pattern of this tool is formatted
as: explore_folder_structure(dir_path) a complete chain of reasoning that explains why the APIs were
selected.
explore_api_file: After identifying the relevant files, the sub-
sequent step is to pinpoint the specific APIs. To achieve this, the
Reasoning-Retrieval Agent invokes this tool to retrieve all API- 3.5 Code Generation
Doc for a given Python file, with the result returned in Mark-
Finally, combining the relevance-based and similarity-based APIs,
down format. The usage pattern of this tool is formatted as: ex-
we place all retrieved code before the contextual information and
plore_api_file(file_path)
the generation requirement, thereby constructing the complete
3.4.2 Reasoning-RetrievalAgent. Subsequently,RepoMindemploys prompt, which is then fed into the LLM to generate the final code.
theLLM’sreasoningcapabilitytoretrieveAPIswithhighrelevance
to the generation requirement. Given the context limitation that 𝑐 = LLM(𝑅𝐴,𝑆𝐴,𝑟,𝑐𝑡) (4)
precludes using all API descriptions as context for LLM inference,
the Reasoning-Retrieval Agent leverages the inherent hierarchical
structure of the code repository to perform a top-down retrieval. where 𝑅𝐴 = {𝑟𝑎 1 ,...,𝑟𝑎 𝑡} is the set of APIs retrieved in Section
It begins by utilizing coarse-grained Module-Doc to infer and de- 3.4,𝑆𝐴 = {𝑠𝑎 1 ,...,𝑠𝑎 𝐾} is the set of APIs retrieved in Section 3.3, r
termine which sub-modules or direct files are relevant to the gen- is the generation requirement, ct is the contextual information and
eration requirement, ultimately locating the core APIs within the the𝑐 is the target code that satisfies the generation requirement.
360

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

RepoMind: Repo-LevelCodeGenviaLLMReasoningoverStructuredDocumentation ICPC’26,April12–13,2026,RiodeJaneiro,Brazil
Table 1: Overall performance of different methods on the CoderEval and DevEval datasets in terms of the Pass@1.
Backbone Model
Dataset Method
GPT-4o-Mini DeepSeek-V3 Qwen3-235B-A22B
SimpleRAG 39.13 48.79 43.00
RepoCoder 37.68 50.72 44.44
DRACO 40.10 47.34 41.06
CodeAgent 27.54 39.13 33.82
CoderEval
RLCoder 38.16 46.86 40.58
AllianceCoder 41.02 51.69 45.41
REPOSCOPE 44.93 59.42 49.28
RepoMind 47.34 56.04 52.17
SimpleRAG 22.61 28.53 21.81
RepoCoder 20.84 28.93 22.96
DRACO 25.26 32.09 29.39
CodeAgent 15.33 25.89 21.70
DevEval
RLCoder 19.69 27.90 22.39
AllianceCoder 33.98 46.15 39.55
REPOSCOPE 26.18 35.82 30.02
RepoMind 37.37 48.34 44.89
4 Evaluation • AllianceCoder[14].Itisanovelcontext-integratedmethod
that leverages Chain-of-Thought (CoT) prompting to decom-
4.1 Research Questions
pose requirements and retrieve APIs via semantic descrip-
• RQ1: How effective is RepoMind in repository-level code
tions according to the decomposed requirements.
generation? • REPOSCOPE2 [28]. It is a novel framework leveraging call
• RQ2: To what extent do the key components of RepoMind
chain-aware multi-view context for repository-level code
contribute to its performance?
generation.
• RQ3: How effective is the impact of different types of API
retrieval results on repository-level code generation?
4.3 Datasets and Metrics
• RQ4: How effectively does the RepoDocs Agent enhance
the retrieval’s effectiveness? We conduct experiments in repo-level function generation tasks
• RQ5: Can RepoMind understand the repository when re- using two widely adopted benchmarks:
trieving?
• CoderEval[46].Itconsistsof230Pythonand230Javatasks
from real-world open-source projects. We use the Python
4.2 Baselines
subset. Each task contains a function signature, a function
We select several representative repository-level code generation description, and several unit tests to evaluate the functional
methods, including the current state-of-the-art, as baselines for correctness of the generated code. Due to incorrect file_path
comparison with RepoMind. entriesinsomesamples,weexcludethosesamples,resulting
• SimpleRAG. It retrieves a fixed set of similar code snippets in a total of 207 samples.
according to similarity score and directly incorporates them • DevEval [21]. It is designed to evaluate LLM’s code gen-
into the prompt for one-shot generation. eration abilities in real-world repositories, which includes
• RepoCoder [47]. It is a retrieval-augmented framework for 1,874 samples from 117 repos. Due to the presence of sam-
repository-level code completion that integrates similarity- ples whose reference solutions fail to pass the provided test
based retrieval with LLM generation in an iterative manner. suitesandsampleswithincorrectmetadata,weexcludethose
• DRACO[11].Itisarepository-levelcodecompletionmethod samples, resulting in a final dataset of 1,742 samples.
that constructs a repository-specific context graph through
WeevaluateRepoMind’sfunctionalcorrectnessusingthePass@1
extended dataflow analysis and enhances prompts by inte-
metric [9], as real-world scenarios typically focus on the quality of
grating structurally relevant background knowledge.
thesinglegeneratedcode.Ageneratedcodeisconsideredsuccessful
• CodeAgent [48]. It is an agent-based framework that im-
only if it passes all test cases.
proves repository-level code generation by equipping LLMs
with external programming tools.
• RLCoder [41]. It is a reinforcement learning–based frame-
work for repository-level code completion that optimizes 2REPOSCOPEdidnotreleaseitscode,sotheexperimentaldatawassourcedfromthe
the retriever’s behavior using perplexity feedback. originalpaper,andcomparisonsforRQcouldnotbeperformed.
361

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
4.4 Implementation Details Table 2: Ablation study results on CoderEval.
Inallconductedexperiments,weutilizeGPT-4o-Mini[19],Deepseek-
V3 [25], and Qwen3-235B-A22B [43] as our backbone LLMs, which Model Method Pass@1
can be accessed via their respective online APIs. For RepoDocs
RepoMind 47.34
Agent, we only use GPT-4o-Mini as the backbone LLM. Except for
the temperature parameter, which is set to 0.2 in RepoDocs Agent, w/o AF 46.38
GPT-4o-Mini
1.0 in Reasoning-Retrieval Agent, and 0.2 in code generation, all w/o FD 43.96
other decoding parameters are kept at their default values. We re- w/o RRA 42.03
trieve 5 APIs in the Similarity-based Retrieval stage and up to 5 w/o SAG 43.00
APIs3 in the LLM-Reasoning-based Retrieval stage. The final API RepoMind 56.04
set is formed by filling the LLM-Reasoning results with APIs from
w/o AF 54.11
the Similarity-Based stage, ensuring a total of 5 APIs. The embed- Deepseek-V3
w/o FD 52.66
ding model (retriever) varies across methods: RLCoder employs a
w/o RRA 53.14
custom fine-tuned version of UniXCoder [15], while both Alliance-
w/o SAG 49.76
Coder and RepoMind rely on the pre-trained UniXCoder. All other
baseline methods employ bge-small-en-v1.5 [31]. RepoMind 52.17
w/o AF 49.28
5 Results and Analysis Qwen-235B-A22B
w/o FD 50.72
5.1 RQ1: How effective is RepoMind in w/o RRA 49.76
repository-level code generation? w/o SAG 50.72
ToevaluatetheeffectivenessofRepoMind,weconductexperiments
usingthreeLLMbackbonemodelsontheCoderEval[46]andDevE-
val [21]. As illustrated in Table 1, our method consistently achieved
the highest Pass@1 scores across all backbone models, except for
Deepseek-V3 on CoderEval, where it is surpassed by REPOSCOPE.
Notably, among the three LLM backbone models, Qwen3-235B-
A22B yielded the highest overall gains on both datasets, achieving
improvements of 5.86% in CoderEval and 13.50% in DevEval. These
results strongly confirm that RepoMind effectively enhances LLM
performance in repository-level code generation by providing an
API set that is more relevant to the generation requirement. More-
over, GPT-4o-Mini also achieves significant improvements on both
datasets. While Deepseek-V3 demonstrated a notable 4.75% im-
provement on DevEval, its performance on CoderEval decreased Figure 5: Performance Comparison of RepoMind with
by 5.69% relative to REPOSCOPE. We hypothesize that this perfor- similarity-based and LLM-based reasoning API Retrieval.
mancediscrepancystemsfromthedepthoftherepositoryhierarchy.
Deepseek-V3 tends to terminate its function-calling sequence pre-
maturelyinthedeephierarchyofCoderEval,whichpreventsitfrom Descriptions (w/o FD): We remove the File-Doc and Module-Doc
fullyexploitingtherepositorydocumentationforcompleteretrieval, content, retaining only the raw file and directory names returned
consequentlylimitingitscodegenerationperformance.Conversely, by the𝑒𝑥𝑝𝑙𝑜𝑟𝑒_𝑓𝑜𝑙𝑑𝑒𝑟_𝑠𝑡𝑟𝑢𝑐𝑡𝑢𝑟𝑒 tool, (2) Excluding API Files (w/o
the shallower repository structure of DevEval allows Deepseek-V3 AF): We remove the structured API-Doc, retaining only the raw
to effectively explore the repository, leading to superior retrieval Python source code returned by the𝑒𝑥𝑝𝑙𝑜𝑟𝑒_𝑎𝑝𝑖_𝑓𝑖𝑙𝑒 tool, (3) Ex-
results. Overall, these results demonstrate that RepoMind, by uti- cluding the Reasoning-Retrieval Agent (w/o RRA): This configura-
lizing hierarchical documentation and LLM reasoning to retrieve tion reduces RepoMind to a conventional similarity-based retrieval
highly relevant APIs and fusing them with similarity APIs, effec- approach, (4) Excluding Similarity API set Guidance (w/o SAG): We
tively enhances the performance of LLMs in repository-level code remove the Similarity API Set from the prompt of the Reasoning-
generation tasks. Retrieval Agent, while they remain included in the final context
used for code generation. As illustrated in Table 2, the results con-
5.2 RQ2: To what extent do the key components sistently indicate that eliminating any component leads to a drop
of RepoMind contribute to its performance? in the Pass@1 score, thereby confirming the necessity of each
component for the overall performance enhancement. Notably, for
To evaluate the effectiveness of each component in RepoMind, we
GPT-4o-Mini and Deepseek-V3, removing the file and module func-
conduct an ablation study on the CoderEval using three backbone
tionaldescriptions(w/oFD)resultsintheperformancedegradation
models. Specifically, our configuration involves individually re-
of 7.14% and 6.03%, respectively. This suggests that providing the
moving critical information and components: (1) Excluding Folder
structural information effectively helps the models identify rele-
3TheresultoftheLLM-Reasoning-BasedRetrievalstageistypicallyfewerthan5APIs. vant files and modules. Furthermore, removing API-Docs (w/o AF)
362

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

RepoMind: Repo-LevelCodeGenviaLLMReasoningoverStructuredDocumentation ICPC’26,April12–13,2026,RiodeJaneiro,Brazil
leads to performance degradation, demonstrating the critical role Table 3: Evaluation of integrating the RepoDocs with Al-
of structured API-Docs in the precise selection of APIs. Moreover, lianceCoder on CoderEval.
theperformanceofallLLMsdropssignificantlywhenremovingthe
Similarity API set Guidance from the Reasoning-Retrieval Agent Model Method Pass@1
(w/o SAG). This indicates that similar API paths play an important
AllianceCoder 41.02
role in helping the agent retrieve truly relevant APIs by providing GPT-4o-Mini
+RepoDocs 43.00
an initial search direction. This effectively mitigates the challenge
arising from the lack of direct correspondence between the highly AllianceCoder 51.69
Deepseek-V3
abstract top-level Module-Docs and the generation requirement +RepoDocs 52.66
at the beginning of retrieval. Finally, the decline in performance
AllianceCoder 45.41
observed upon removing the Reasoning-Retrieval Agent (w/o RRA) Qwen-235B-A22B +RepoDocs 48.31
further validates the overall effectiveness of our reasoning-based
retrieval method leveraging repository documentation.
5.3 RQ3: How effective is the impact of different LLMs with our API-Database, achieving up to a 6.39% relative gain.
This result further demonstrates the significant effectiveness of Re-
types of API retrieval results on
poDocsAgentingeneratinghigh-quality,context-awarerepository
repository-level code generation?
documentation.
RepoMind employs a hybrid strategy that combines relevance re-
trievalresultsderivedfromLLM-basedreasoningretrievalwithsim- 5.5 RQ5: Can RepoMind understand the
ilarity retrieval results obtained from similarity-based retrieval. To repository when retrieving?
validate this approach, we investigate the individual and combined
To evaluate RepoMind’s ability to comprehend the repository dur-
impact of these two types of retrieval results on repository-level
ing the retrieval process and thereby enhance result relevance, we
code generation performance. Specifically, we conduct code gener-
conduct a comparative analysis. AllianceCoder employs CoT to
ation using the relevant API set and the similar API set separately
decompose the generation requirement into detailed implementa-
as context. The former, generated by the LLM, varied in size but
tion steps, subsequently generating API descriptions based on the
is limited to a maximum of five APIs, while the latter consistently
steps,andfinallyretrievingrepositoryAPIssimilartothegenerated
selects the top-5 most similar APIs.
descriptions. Crucially, during the decomposition and description
As shown in Figure 5, relying solely on either retrieval method
generation phases, AllianceCoder only relies on the LLM’s internal
leads to a significant performance degradation. The majority of the
knowledge, neglecting repository-specific information. Conversely,
performancedeclineisattributabletousingonlysimilarityretrieval
results,withthelargestrelativedropreaching11.22%.Thissuggests RepoMind utilizes the initial generation requirement as context, en-
abling the Reasoning-Retrieval Agent to invoke tools that interact
the inherent limitation of similarity-based approaches, which often
with the repository’s documentation library. This allows the agent
fail to retrieve APIs that are genuinely relevant to the functional
to retrieve functional descriptions of Python files and modules in
requirements. Moreover, performance also decreased when using
the repository, dynamically adjusting the retrieval direction based
only relevance retrieval results, mainly due to two reasons: first, it
on the repository structure and module functionality. As shown
cannot guarantee the retrieval of all necessary APIs; and second,
in Table 1 and Table 3, even when substituting AllianceCoder’s
even when relevant APIs are retrieved, the challenge of composing
original retrieval library with our high-quality API-Database, Re-
and utilizing them correctly to meet the requirements remains.
poMind consistently outperforms AllianceCoder across all three
In contrast, combining both retrieval results effectively compen-
backbone models, achieving gains of 10.09%, 6.42%, and 8.00%, re-
sates for these individual weaknesses: relevance retrieval provides
spectively. This gap strongly suggests that RepoMind’s retrieval is
functionally relevant APIs, while similarity retrieval contributes
guided by an inherent understanding of the repository structure,
code templates and implementation details for addressing similar
which significantly boosts the relevance of the retrieval results.
requirements, collectively enhancing RepoMind’s performance in
repository-level code generation.
6 Discussion
5.4 RQ4: How effectively does the RepoDocs 6.1 Case study
Agent enhance the retrieval’s effectiveness?
To intuitively demonstrate the effectiveness of RepoMind, we pro-
Since the repository documentation, specifically the API-Doc, con- vide a concrete example in Figure 6 comparing the retrieval results
structed by the RepoDocs Agent is independently available, it can of RepoMind against AllianceCoder and a purely similarity-based
be seamlessly integrated with other similarity-based API retrieval API retrieval method. In AllianceCoder, decomposing the require-
methods to achieve enhanced performance. AllianceCoder [14] ment led to the retrieval of 10 APIs, but only two, 𝑖𝑠_𝑓𝑜𝑙𝑑𝑒𝑟 and
constructs its API retrieval database by only considering the func- 𝑥𝑚𝑙_𝑓𝑖𝑙𝑒𝑠_𝑙𝑖𝑠𝑡, are relevant to the generation requirement, conse-
tion under analysis, while ignoring other dependent code entities. quently introducing a substantial amount of irrelevant code. Con-
Therefore, we replace AllianceCoder’s API retrieval database with versely, the similarity-based API retrieval method, which selects
our API-Database mentioned in Section 3.3. As shown in Table 3, the top-5 APIs based on cosine similarity score, only yields the
the Pass@1 score of AllianceCoder consistently improves across all function _𝑔𝑟𝑜𝑢𝑝_𝑓𝑖𝑙𝑒𝑠_𝑏𝑦_𝑥𝑚𝑙_𝑓𝑖𝑙𝑒𝑛𝑎𝑚𝑒 as genuinely invokable
363

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
Threatstoexternalvalidityrelatetothepotentialdataleakage
infrared # scieloorg---packtools/packtools/sps/models/packages.py
def _explore_folder(folder): Generation requirement & from the LLM’s pre-training corpus. Although our datasets are
""" Target Function
Get packages' data from folder widely used in prior work and published in 2024, some repository
Groups files by their XML basename and returns data in dict format.
common inspector validators.py ConflictResolver Parameters: folder : str Folder of the package code may have been included in the pretraining data of evaluated
. t . i . b v i a l l i c i t o d y r a e t w e i s t h o b J j S e O c N t f c o o r m m p a a t - ... . e . x . ec fa ut ci io l u i n t ta b il y t s i c n o g n s f e ir a m ml i e ng s . s .. . s . c . h e c m o a m s p l f i o a r n c A e n d s i w i c i b t t l _ h e u p c t r o i e n ls d f . e i p f g y i u n r e a d t ions... T h h a i n s d l c e l a k s e s y p c r o d o n i v f c i l t d i _ e c m s t s e m . e . r t . g h e ods to R " i e " f t " u f r d i n a l s t e : a _ u = t d i i l _ c s g t . ro i u s p _ _ f f o i l l d e e s r _ ( b f y o _ l x d m e l r _ ) f : ilename(folder, L in L v M es s t . ig In at t e h d e to fu m tu i r ti e g , a d t y e n th am is i t c h a r l e ly at e . volving benchmarks could be
. b . y . e c n o h n a s n o c l e i s d a o t u i t n p g u t d a m t a a n agement . s . t . r d e i a c m t l i i o n n i a n r g y . . o . perations, . w . h . i m l e e r g e i f n f g e c d t i i c v t e i l o y n . a . r . ies … i i n s t e d g e r s a i t g i n o e n d o t f o t f w a o c i d l i i c t t a i t o e n a t r h i e e s… f f i i l l e e _ _ u u t t i i l l s s . . x f m i l l _ e f s i _ l l e i s s _ t l ( i f s o t l ( d f e o r l ) d , er),
handling ... … … …
Relevant API: 2/10
api.py AllianceCoder 7 Related Work
def is_folder(source):
T i h n i t s e g m r o a d t u i l o e n e o n f a b p l l e u s g i t n h s e into ... return os.path.isdir(source)
7.1 Code Summarization
… def xml_files_list(path):
""" Return the XML files found in `path` """
return (f for f in os.listdir(path) if f.endswith(".xml")) High-qualitycode summariesarecrucialfor effectivecoderetrieval
as well as for repository-level code generation tasks. Consequently,
def file_path(self, file_path):
if file_utils.is_folder(self._source): code summarization has been extensively studied by researchers.
...
Pre-trainedencoder-onlymodelssuchasGraphCodeBERT[16]and
7 irrelevant APIs omitted
UniXCoder [15] introduced bi-modal and code-specific structure-
aware learning, while encoder-decoder models like CodeT5 [40]
Relevant API: 1/5 Similarity-based API retrieval
unified code generation and summarization. CLCoSum [17] fur-
def _group_files_by_xml_filename(source, xmls, files):
""" Group files by their XML basename ther leveraged data augmentation and curriculum learning [3] to
Groups files by their XML basena
... enhance code summarization performance. RBCoSum [8] incor-
4 irrelevant APIs omitted porated the generated Chain Of Comments as auxiliary interme-
diate information for the model to bridge the gap between code
Relevant API: 4/5 and summaries. More recently, LLMs such as StarCoder [22] and
RepoMind
def is_folder(source): CodeLlama [34] have demonstrated powerful zero-shot summa-
return os.path.isdir(source)
rization capabilities. Code summarization granularity has gradu-
def xml_files_list(path):
""" Return the XML files found in `path` """ ally shifted from the method-level to the file-level. SparseCoder
return (f for f in os.listdir(path) if f.endswith(".xml"))
[39] introduces an identifier-aware sparse transformer to handle
def files_list(path):
return os.listdir(path) file-level summarization. However, these methods typically lack
repository-level context, dependency awareness, and collaboration.
def _group_files_by_xml_filename(source, xmls, files):
""" Group files by their XML basename. Groups files by their XML ... Consequently, approaches such as DocAgent [44] and RepoAgent
1 irrelevant APIs omitted [29] have emerged, which utilize multi-agent to analyze complex
dependencieswithincoderepositoriesforcodesummarization.Nev-
ertheless, these methods remain constrained to the API granularity
Figure 6: An example of the APIs retrieved by AllianceCoder,
and do not generate the structure-aware documentation required
Similarity-based API retrieval, and RepoMind.
to capture the repository’s architecture. Therefore, we propose the
RepoDocs Agent to generate summaries at three granularities fol-
lowing the repository structure. This approach provides a more
by the target function. In contrast, RepoMind, leveraging reposi- comprehensive summarization that better aligns with the actual
tory comprehension derived from documentation and LLM-based documentation requirements of a repository.
reasoning, not only accurately retrieves all relevant functions but
also minimizes the number of irrelevant APIs. Consequently, this
precise retrieval mechanism enables RepoMind to achieve superior 7.2 Repository-level Code Generation
performance in repository-level code generation tasks.
Repository-level code generation has garnered increasing atten-
tion in recent years due to its closer alignment with real-world
6.2 Threats to Validity
software development. This growing interest has stimulated the
Threats to internal validity stem from the generalizability of introductionofdiversedatasets[20,21,46],furtheracceleratingthe
ourmethodandfindings.AlthoughRepoMinddemonstratesstrong field’sdevelopment.Totacklethechallengeofintegratingextensive
performance on Python-based datasets, and its core mechanism repository knowledge within the limited context window of LLM,
is inherently programming-language agnostic, it remains uncer- HCP [49] employs hierarchical context pruning to fit the entire
tain whether its effectiveness can be extended to other datasets codebase into the context. The predominant methodology relies on
or programming languages. We leave this exploration to future RAG techniques [13] to retrieve relevant code from the repository.
work. Due to computational budget constraints, our evaluation is Early methods [35, 47] used retrievers to identify code snippets
limited to a representative set of LLMs. Some models not included most similar to the generation context and adopted an iterative
in this study may potentially outperform those we evaluate. We retrieval-then-generation framework. Additionally, AllianceCoder
willcontinuetomonitorthedevelopmentsinthisfieldandareopen [14] utilizes the LLM to generate API functional descriptions as
to incorporating other advanced models in future work. queries to retrieve relevant APIs within the repository.
364

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

RepoMind: Repo-LevelCodeGenviaLLMReasoningoverStructuredDocumentation ICPC’26,April12–13,2026,RiodeJaneiro,Brazil
However,codeisnotplaintextsinceitsintrinsicstructuraldepen- (x2rjD2250190), the Fundamental Research Funds for the Central
dency relationships encapsulate rich semantic information. Conse- Universities (2025ZYGXZR064).
quently, many studies have utilized graph structures to deeply rep-
resent the complex dependency relationships within the repository.
Among them. DRACO [11] identifies local import information by References
performing dataflow analysis. Repohyper [33] constructs a method- [1] Ingeol Baek, Hwan Chang, Byeongjeong Kim, Jimin Lee, and Hwanhee Lee.
level graph to compute node relevance scores for retrieval, while 2024. Probing-rag:Self-probingtoguidelanguagemodelsinselectivedocument
retrieval. arXivpreprintarXiv:2410.13339 (2024).
GraphCoder [27] analyzes finer code-line granularity control-flow
[2] RamakrishnaBairi,AtharvSonwane,AdityaKanade,VageeshDC,ArunIyer,
and dependencies. REPOSCOPE [28] proposes building a reposi- SureshParthasarathy,SriramRajamani,BalasubramanyanAshok,andShashank
tory structural semantic graph and a call chain prediction method. Shet.2024. Codeplan:Repository-levelcodingusingllmsandplanning. Proceed-
ingsoftheACMonSoftwareEngineering 1,FSE(2024),675–698.
Despite achieving partial gains in generation performance, these
[3] Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason Weston. 2009.
methodsstillfallshortinfullyleveragingprogramstructuralseman- Curriculumlearning.InProceedingsofthe26thannualinternationalconference
tics. Moreover, similarity-based retrieval methods cannot always
onmachinelearning.41–48.
[4] ZhangqianBi,YaoWan,ZhengWang,HongyuZhang,BatuGuan,FangxinLu,
successfully identify the most relevant information. This limita- ZiliZhang,YuleiSui,HaiJin,andXuanhuaShi.2024. Iterativerefinementof
tion has prompted some works to employ Reinforcement Learning project-levelcodecontextforprecisecodegenerationwithcompilerfeedback.
arXivpreprintarXiv:2403.16792 (2024).
to improve the accuracy of retrieving information [36, 41] or use
[5] EgorBogomolov,AleksandraEliseeva,TimurGalimzyanov,EvgeniyGlukhov,
selective retrieval to minimize unnecessary retrieval [1, 42]. Anton Shapkin, Maria Tigina, Yaroslav Golubev, Alexander Kovrigin, Arie
More recently, Agent-based methods [2, 10, 50] have received VanDeursen,MalihehIzadi,etal.2024. Longcodearena:asetofbenchmarks
forlong-contextcodemodels. arXivpreprintarXiv:2406.11612 (2024).
increasing attention due to their strong performance in repository-
[6] Tuan-DungBui,Duc-ThieuLuu-Van,Thanh-PhatNguyen,Thu-TrangNguyen,
level code generation. CodeAgent [48] investigates the integration SonNguyen,andHieuDinhVo.2024. Rambo:Enhancingrag-basedrepository-
oftool-callingmechanisms,allowingtheLLMtodetermineretrieval levelmethodbodycompletion. arXivpreprintarXiv:2409.15204(2024).
[7] LiuwenCao,YiCai,JiexinWang,HongkuiHe,andHailinHuang.2024. Beyond
targets. LingmaAgent [30] combines Monte Carlo Tree Search with code: Evaluate thought steps for complex code generation. In Proceedings of
LLM-based evaluation to identify the most relevant snippets. the2024JointInternationalConferenceonComputationalLinguistics,Language
ResourcesandEvaluation(LREC-COLING2024).2296–2306.
However, enabling the LLM to directly participate in retrieving
[8] Liuwen Cao, Hongkui He, Hailin Huang, Jiexin Wang, and Yi Cai. 2025.
relevantAPIsremainsachallengingproblem.Incontrasttoexisting Rethinking-basedCodeSummarizationwithChainofComments.InProceedings
approaches, RepoMind directly provides the LLM with repository
ofthe31stInternationalConferenceonComputationalLinguistics.3043–3056.
[9] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde
structure and documentation, empowering the model to leverage
De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph,
the powerful reasoning capability for an in-depth analysis of the GregBrockman,etal.2021. Evaluatinglargelanguagemodelstrainedoncode.
repository,ratherthanrelyingsolelyonsimplesimilaritymatching,
arXivpreprintarXiv:2107.03374(2021).
[10] Zhaoling Chen, Xiangru Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei
thereby achieving precise retrieval of relevant APIs. Jiang, Viktor Prasanna, Arman Cohan, and Xingyao Wang. 2025. Locagent:
Graph-guidedllmagentsforcodelocalization. arXivpreprintarXiv:2503.09089
(2025).
8 Conclusion
[11] WeiCheng,YuhanWu,andWeiHu.2024. Dataflow-guidedretrievalaugmen-
tation for repository-level code completion. arXiv preprint arXiv:2405.19782
ThispaperintroducesRepoMind,anovelframeworkforrepository-
(2024).
level code generation. It operates by constructing a comprehensive [12] Aryaz Eghbali and Michael Pradel. 2024. De-Hallucinator: Mitigating LLM
repository documentation library and utilizing LLM-based reason- HallucinationsinCodeGenerationTasksviaIterativeGrounding. arXivpreprint
arXiv:2401.01701(2024).
ing for relevant API retrieval. RepoMind introduces the RepoDocs
[13] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yixin
Agent to construct multi-granularity, hierarchical documentation, Dai,JiaweiSun,HaofenWang,andHaofenWang.2023. Retrieval-augmented
establishing a rich knowledge base for understanding repository generationforlargelanguagemodels:Asurvey. arXivpreprintarXiv:2312.10997
2,1(2023).
functionality. Furthermore, RepoMind incorporates the Repository- [14] WenchaoGu,JuntaoChen,YanlinWang,TianyueJiang,XingzheLi,Mingwei
Reasoning Agent, which simulates developer behavior to perform Liu,XilinLiu,YuchiMa,andZibinZheng.2025. WhattoRetrieveforEffective
Retrieval-AugmentedCodeGeneration?AnEmpiricalStudyandBeyond. arXiv
layer-by-layer exploratory searches and effectively retrieve rel- preprintarXiv:2503.20589 (2025).
evant APIs. By combining similarity-based and relevance-based [15] DayaGuo,ShuaiLu,NanDuan,YanlinWang,MingZhou,andJianYin.2022.
retrieval results, RepoMind generates code that meets functional Unixcoder: Unified cross-modal pre-training for code representation. arXiv
preprintarXiv:2203.03850 (2022).
requirements. Extensive experiments demonstrate that RepoMind
[16] DayaGuo,ShuoRen,ShuaiLu,ZhangyinFeng,DuyuTang,ShujieLiu,Long
achieves state-of-the-art performance on major repository-level Zhou,NanDuan,AlexeySvyatkovskiy,ShengyuFu,etal.2020. Graphcodebert:
code generation benchmarks. Pre-trainingcoderepresentationswithdataflow. arXivpreprintarXiv:2009.08366
(2020).
[17] HongkuiHe,JiexinWang,LiuwenCao,andYiCai.2025. CLCoSum:Curricu-
Acknowledgments
lumLearning-BasedCodeSummarizationforCodeLanguageModels.In2025
IEEE/ACM33rdInternationalConferenceonProgramComprehension(ICPC).IEEE
Thisresearchis supported bytheScience andTechnologyPlanning ComputerSociety,1–13.
[18] DanHendrycks,StevenBasart,SauravKadavath,MantasMazeika,AkulArora,
ProjectofGuangdongProvince(2025B0101120003),theGuangdong
EthanGuo,CollinBurns,SamirPuranik,HoraceHe,DawnSong,etal.2021. Mea-
Provincial Fund for Basic and Applied Basic Research—Regional suringcodingchallengecompetencewithapps. arXivpreprintarXiv:2105.09938
Joint Fund Project (Key Project) (2023B1515120078), National Natu- (2021).
[19] AaronHurst,AdamLerer,AdamPGoucher,AdamPerelman,AdityaRamesh,
ral Science Foundation of China (62476097, 62402185), Guangdong AidanClark,AJOstrow,AkilaWelihinda,AlanHayes,AlecRadford,etal.2024.
ProvincialNaturalScienceFoundationforOutstandingYouthTeam Gpt-4osystemcard. arXivpreprintarXiv:2410.21276(2024).
[20] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir
Project (2024B1515040010), the Fundamental Research Funds for
Press,andKarthikNarasimhan.2023. Swe-bench:Canlanguagemodelsresolve
the Central Universities, South China University of Technology real-worldgithubissues? arXivpreprintarXiv:2310.06770 (2023).
365

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

ICPC’26,April12–13,2026,RiodeJaneiro,Brazil Gongetal.
[21] JiaLi,GeLi,YunfeiZhao,YongminLi,HuanyuLiu,HaoZhu,LechengWang, [43] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng,
Kaibo Liu, Zheng Fang, Lanshen Wang, et al. 2024. Deveval: A manually- BowenYu,ChangGao,ChengenHuang,ChenxuLv,etal.2025. Qwen3technical
annotatedcodegenerationbenchmarkalignedwithreal-worldcoderepositories. report. arXivpreprintarXiv:2505.09388(2025).
arXivpreprintarXiv:2405.19856(2024). [44] DayuYang,AntoineSimoulin,XinQian,XiaoyiLiu,YuweiCao,ZhaopuTeng,
[22] RaymondLi,LoubnaBenAllal,YangtianZi,NiklasMuennighoff,DenisKocetkov, andGreyYang.2025. DocAgent:AMulti-AgentSystemforAutomatedCode
ChenghaoMou,MarcMarone,ChristopherAkiki,JiaLi,JennyChim,etal.2023. DocumentationGeneration. arXivpreprintarXiv:2504.08725 (2025).
Starcoder:maythesourcebewithyou! arXivpreprintarXiv:2305.06161(2023). [45] ZezhouYang,SirongChen,CuiyunGao,ZhenhaoLi,XingHu,KuiLiu,andXin
[23] Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Peng Di, Hongwei Xia.2025.Anempiricalstudyofretrieval-augmentedcodegeneration:Challenges
Chen,ChengpengWang,GangFan,etal.2024. Repofuse:Repository-levelcode andopportunities. ACMTransactionsonSoftwareEngineeringandMethodology
completionwithfuseddualcontext. arXivpreprintarXiv:2402.14323(2024). (2025).
[24] DianshuLiao,ShidongPan,XiaoyuSun,XiaoxueRen,QingHuang,Zhenchang [46] HaoYu,BoShen,DezhiRan,JiaxinZhang,QiZhang,YuchiMa,GuangtaiLiang,
Xing, Huan Jin, and Qinying Li. 2024. A 3-codgen: A repository-level code YingLi,QianxiangWang,andTaoXie.2024. Codereval:Abenchmarkofprag-
generationframeworkforcodereusewithlocal-aware,global-aware,andthird- maticcodegenerationwithgenerativepre-trainedmodels.InProceedingsofthe
party-library-aware. IEEETransactionsonSoftwareEngineering (2024). 46thIEEE/ACMInternationalConferenceonSoftwareEngineering.1–12.
[25] AixinLiu,BeiFeng,BingXue,BingxuanWang,BochaoWu,ChengdaLu,Cheng- [47] FengjiZhang,BeiChen,YueZhang,JackyKeung,JinLiu,DaoguangZan,YiMao,
gangZhao,ChengqiDeng,ChenyuZhang,ChongRuan,etal.2024. Deepseek-v3 Jian-GuangLou,andWeizhuChen.2023. Repocoder:Repository-levelcodecom-
technicalreport. arXivpreprintarXiv:2412.19437 (2024). pletionthroughiterativeretrievalandgeneration.arXivpreprintarXiv:2303.12570
[26] NelsonFLiu,KevinLin,JohnHewitt,AshwinParanjape,MicheleBevilacqua, (2023).
FabioPetroni,andPercyLiang.2023. Lostinthemiddle:Howlanguagemodels [48] KechiZhang,JiaLi,GeLi,XianjieShi,andZhiJin.2024. Codeagent:Enhancing
uselongcontexts. arXivpreprintarXiv:2307.03172 (2023). code generation with tool-integrated agent systems for real-world repo-level
[27] WeiLiu,AilunYu,DaoguangZan,BoShen,WeiZhang,HaiyanZhao,ZhiJin,and codingchallenges. arXivpreprintarXiv:2401.07339 (2024).
QianxiangWang.2024. Graphcoder:Enhancingrepository-levelcodecompletion [49] LeiZhang,YunshuiLi,JiamingLi,XiaoboXia,JiaxiYang,RunLuo,Minzheng
via code context graph-based retrieval and language model. arXiv preprint Wang, Longze Chen, Junhao Liu, Qiang Qu, et al. 2025. Hierarchical context
arXiv:2406.07003(2024). pruning:Optimizingreal-worldcodecompletionwithrepository-levelpretrained
[28] YangLiu,LiZhang,FangLiu,ZhuohangWang,DonglinWei,ZhishuoYang,Kechi codellms.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39.
Zhang,JiaLi,andLinShi.2025. EnhancingRepository-LevelCodeGeneration 25886–25894.
with Call Chain-Aware Multi-View Context. arXiv preprint arXiv:2507.14791 [50] YuntongZhang,HaifengRuan,ZhiyuFan,andAbhikRoychoudhury.2024. Au-
(2025). tocoderover:Autonomousprogramimprovement.InProceedingsofthe33rdACM
[29] QinyuLuo,YiningYe,ShihaoLiang,ZhongZhang,YujiaQin,YaxiLu,YesaiWu, SIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis.1592–1604.
Xin Cong, Yankai Lin, Yingli Zhang, et al. 2024. Repoagent: An llm-powered [51] ShuyanZhou,UriAlon,FrankFXu,ZhengbaoJiang,andGrahamNeubig.2022.
open-source framework for repository-level code documentation generation. Docprompting:Generatingcodebyretrievingthedocs.InTheEleventhInterna-
arXivpreprintarXiv:2402.16667 (2024). tionalConferenceonLearningRepresentations.
[30] YingweiMa,QingpingYang,RongyuCao,BinhuaLi,FeiHuang,andYongbin
Li.2025. Alibabalingmaagent:Improvingautomatedissueresolutionviacom-
prehensiverepositoryexploration.InProceedingsofthe33rdACMInternational
ConferenceontheFoundationsofSoftwareEngineering.238–249.
[31] Multi-LingualityMulti-FunctionalityMulti-Granularity.2024. M3-Embedding:
Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings
ThroughSelf-KnowledgeDistillation.
[32] Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao
Jia, Jiawei Han, Hongming Zhang, and Dong Yu. 2024. Repograph: Enhanc-
ing ai software engineering with repository-level code graph. arXiv preprint
arXiv:2410.14684(2024).
[33] HuyNPhan,HoangNPhan,TienNNguyen,andNghiDQBui.2025. Repohyper:
Search-expand-refineonsemanticgraphsforrepository-levelcodecompletion.
In2025IEEE/ACMSecondInternationalConferenceonAIFoundationModelsand
SoftwareEngineering(Forge).IEEE,14–25.
[34] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiao-
qingEllenTan,YossiAdi,JingyuLiu,RomainSauvestre,TalRemez,etal.2023.
Codellama:Openfoundationmodelsforcode. arXivpreprintarXiv:2308.12950
(2023).
[35] AntonShapkin,DenisLitvinov,YaroslavZharov,EgorBogomolov,TimurGal-
imzyanov,andTimofeyBryksin.2023.DynamicRetrieval-AugmentedGeneration.
arXivpreprintarXiv:2312.08976(2023).
[36] Jicheng Wang, Yifeng He, and Hao Chen. 2024. Repogenreflex: Enhanc-
ingrepository-levelcodecompletionwithverbalreinforcementandretrieval-
augmentedgeneration. arXivpreprintarXiv:2409.13122 (2024).
[37] MengzhenWang,YiCai,JiayuanXie,JiexinWang,XinWu,JieLiu,andRonghui
Yang.2026. Code-EnhancedCross-PerspectiveBugQuestionRetrieval. ACM
Trans.Softw.Eng.Methodol.(Jan.2026). doi:10.1145/3789667 JustAccepted.
[38] MengzhenWang,XunbinHuang,JiayuanXie,ShukaiMa,JialeMen,Dayong
Liang,andYiCai.2025. FromModelDiagramtoCode:ABenchmarkDatasetand
Multi-AgentFramework.InProceedingsofthe33rdACMInternationalConference
onMultimedia.1754–1763.
[39] YanlinWang,YanxianHuang,DayaGuo,HongyuZhang,andZibinZheng.2024.
Sparsecoder:Identifier-awaresparsetransformerforfile-levelcodesummariza-
tion.In2024IEEEInternationalConferenceonSoftwareAnalysis,Evolutionand
Reengineering(SANER).IEEE,614–625.
[40] YueWang,WeishiWang,ShafiqJoty,andStevenCHHoi.2021.Codet5:Identifier-
awareunifiedpre-trainedencoder-decodermodelsforcodeunderstandingand
generation. arXivpreprintarXiv:2109.00859 (2021).
[41] YanlinWang,YanliWang,DayaGuo,JiachiChen,RuikaiZhang,YuchiMa,and
ZibinZheng.2024. Rlcoder:Reinforcementlearningforrepository-levelcode
completion. arXivpreprintarXiv:2407.19487 (2024).
[42] Di Wu, Wasi Uddin Ahmad, Dejiao Zhang, Murali Krishna Ramanathan, and
XiaofeiMa.2024. Repoformer:Selectiveretrievalforrepository-levelcodecom-
pletion. arXivpreprintarXiv:2403.10059 (2024).
366

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/primary/RepoMind/page-12.png)
