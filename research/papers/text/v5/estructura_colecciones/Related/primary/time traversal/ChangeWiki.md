# ChangeWiki

- source_pdf: ../../../../../../pdf/Related/primary/time%20traversal/ChangeWiki.pdf
- extraction_tool: pdfplumber
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

ChangeWiki: Repository-Level Change Summarization
Augmented with Architecture Semantics
✉
Zijun Wang Wuxia Jin Jiale Li
Xi’an Jiaotong University Xi’an Jiaotong University Xi’an Jiaotong University
the School of Software Engineering the School of Software Engineering the School of Software Engineering
Xi’an, China Xi’an, China Xi’an, China
wang_zijun8143@stu.xjtu.edu.cn jinwuxia@mail.xjtu.edu.cn jialeli@stu.xjtu.edu.cn
Zhanhong Mou Ting Liu
Xi’an Jiaotong University Xi’an Jiaotong University
the School of Software Engineering the School of Cyber Science and
Xi’an, China Engineering
1303469826@stu.xjtu.edu.cn Xi’an, China
tingliu@mail.xjtu.edu.cn
Abstract Keywords
Understanding software evolution at the repository level is es- change summarization, repository, architecture semantics
sential for tasks such as release management, code review, and
ACMReferenceFormat:
regression testing. However, existing change summarization tech-
Zijun Wang, Wuxia Jin, Jiale Li, Zhanhong Mou, and Ting Liu. 2026.
niques are largely confined to single commits or functions, fail-
ChangeWiki: Repository-Level Change Summarization Augmented
ing to capture cross-commit evolutionary context, while recent with Architecture Semantics. In Proceedings of the 41st IEEE/ACM
repository-level understanding tools focus on static documentation International Conference on Automated Software Engineering (ASE ’26),
of single-version codebases, overlooking evolution over time. To October12–16,2026,Munich,Germany.ACM,NewYork,NY,USA,13pages.
bridgethisgap,weproposeChangeWiki,anarchitecturesemantic- https://doi.org/10.1145/3832783.3834436
augmented approach for repository-level change summarization.
ChangeWikifirstconstructshierarchical,multi-granularitychange 1 Introduction
entity trees enriched with multi-source contexts to infer change in-
tentandimpact.Itthenrecoversmodularstructuresacrossversions Software enters a continuous evolution phase after its initial deliv-
andemploysabidirectionalcontext-guidedaggregationmechanism, ery, undergoing diverse change activities including corrective (i.e.,
synthesizingcode-levelchangesfromthebottomupwhileinjecting bug fixes), preventive (i.e., dependency upgrade), adaptive (i.e., en-
architectural semantics as top-down constraints. ChangeWiki fi- vironmentmigration),andperfectivemaintenance(i.e.,refactoring)
nally generates coherent, traceable summaries that capture both [18, 34]. Code changes capture the trajectory of design decisions
local modifications and system-level evolution. We construct com- and issue resolutions, serving as a critical carrier for understanding
prehensive benchmarks and evaluate ChangeWiki on real-world software evolution. To help developers comprehend these changes,
projects. Experimental results demonstrate significant improve- change summarization techniques [21, 32, 35] have been proposed
ments in semantic accuracy, completeness, and cross-granularity to identify change behaviors, infer intent, and characterize poten-
traceability. A prototype of ChangeWiki has been deployed in an tialimpactinnaturallanguage.Asthescaleandcomplexityofcode
industrial setting for upstream-downstream code evolution, where changes grow, grasping the overall landscape of software evolution
developers reported that the hierarchical summaries significantly at the repository level–seeing the forest for the trees–has become
reduced manual effort in issue localization caused by upstream a critical requirement [40]. Unlike the approaches focused on in-
changes and show potential for automating version release notes. dividual commits or local code differences, repository-level change
summarization models related modifications scattered across mul-
CCS Concepts tiple commits within an evolutionary context, revealing the ratio-
nale, semantic associations, and overall impact from a system-level
•Softwareanditsengineering→Softwareevolution;Software
perspective. This holistic view can support key activities such as
reverse engineering.
release management [5, 17], code review [1], and regression testing
[16], helping developers quickly grasp core design decisions amidst
massive volumes of changes.
Existing change summarization methods primarily focus on the
granularity of commits or functions, evolving from template-based
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. approaches(e.g.,ChangeScribe[29])toneuralmodelswithretrieval
ASE’26,Munich,Germany augmentation [21] and AST/graph-based semantic enhancement
©2026Copyrightheldbytheowner/author(s).
[8, 30], and more recently to LLM-based solutions [11] that signifi-
ACMISBN979-8-4007-2882-2/2026/10
https://doi.org/10.1145/3832783.3834436 cantly improve fluency and readability. While these advances have
1333

[Vista original de la página 1](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-01.png)

![Página PDF 1, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
improved the effectiveness of change summaries, they remain con- BERTScore. RQ2 ablation studies show that removing the architec-
finedto single-commitgranularity,failingto capture broader evolu- ture abstraction module causes an approximately 26% performance
tionary context across multiple commits. Meanwhile, recent efforts drop,whileremovingmulti-sourcecontextenrichmentresultsinan
on repository-level code understanding, such as CodeWiki [14, 19] about7.7%decline,confirmingtheeffectivenessofeachcomponent.
and DeepWiki [6], focus on static documentation generation for In RQ3, developers who are recruited to participate in the manual
single-version codebases, neglecting software evolution over time. evaluation rate ChangeWiki highly across accuracy, completeness,
Consequently, repository-level change summarization, which synthe- readability, and traceability, with an overall average score of 4.5
sizes scattered changes across versions into a coherent evolutionary outof5,indicatingitsutilityinunderstandingrepositoryevolution.
narrative, remains underexplored. What is urgently needed, there- A prototype deployed in an industrial setting further validates its
fore, is an evolution-aware counterpart to DeepWiki that extends practical value, where developers reported that the hierarchical
repository-level understanding to capture cross-version change summaries significantly reduced effort in understanding changes
semantics and architectural evolution. across large version gaps. We believe our work will benefit real-
However, repository-level change summarization faces the non- world co-evolution and version release management. In summary,
trivial challenges. ❶ Focusing on diff fragments makes it difficult our work makes the following contributions.
to discern change intent and potential impact. Taking the modifica- • WeproposeChangeWiki,thefirstworkonrepository-level
tionoffunctionuv__run_timersinlibuvasanexample(Section2), change summarization via multi-source context enrichment
existing methods output judgments like “refactoring to introduce a and bidirectional hierarchical aggregation.
ready queue," while the actual intent is to avoid busy-loop issues • We evaluate ChangeWiki on real-world projects using com-
caused by zero-millisecond timers and ensure proper event loop prehensive metrics. Results show significant improvements
progression.Thisrevealsthatdiffinformationalonecannotcapture over baselines.
design rationale, highlighting the need for diverse contexts to infer • Wecontributeadatasetcoveringmultipleprojectsandmulti-
why a change was made beyond what changed. ❷ Modifications granularity change semantics. It surpasses existing datasets
related to a common theme often span multiple commits, yet exist- in both scale and diverse granularity.
ing methods treat each commit in isolation, lacking cross-commit
architecturalcontext.Consequently,architecturaldecisionsbecome 2 Motivation
buried in fine-grained implementation details. In libuv’s evolution Problem Definition. Given a version pair (𝑉 𝑎 ,𝑉 𝑏) of a codebase,
from v1.44.2 to v1.48.0 (with 286 commits and 25KLOC), enhance- repo-level change summarization (𝐺 𝑟𝑒𝑝𝑜) aims to generate a set of
ments including CPU affinity, CPU awareness, and thread priority natural language descriptions𝑆 𝑎𝑏 to capture the underlying intent
are scattered across nearly 200 commits. Viewed in isolation, they and system-level impact ofcode changes𝐶 𝑖 accumulated acrossthe
appear as fragmented additions, while aggregated analysis reveals commits from𝑉 𝑎 to𝑉 𝑏.
a common goal: “evolving the thread subsystem from basic encap- (cid:216)
sulation toward scheduling control and awareness". Identifying 𝐺 𝑟𝑒𝑝𝑜 : 𝐶 𝑖 → 𝑆 𝑎𝑏
and aggregating such cross-commit architectural semantics from 𝐶𝑖∈[𝑉𝑎,𝑉𝑏]
massive scattered commits remains a critical challenge. Unlike commit-level change summarization, which generates a
To address the above challenges, we propose ChangeWiki , an description𝑆 𝑖 foranindividualcommit𝐶 𝑖,thetaskaddressedinthis
architecture semantic-augmented approach for repository-level work,𝐺 𝑟𝑒𝑝𝑜, is a cross-commit evolution understanding problem.
code change summarization, aiming to recover system-level evo- We take the popular project libuv [28] as an example, analyzing
lution semantics from scattered code changes across versions. To itsevolutionfromversionv1.44.2tov1.48.0.Specifically,thisperiod
tackle Challenge ❶, ChangeWiki anchors on program entities to encompasses 286 commits, involving 272 files and over 25k lines of
construct a hierarchical, multi-granularity change entity structure, code modifications. Summarizing such a large volume of changes,
and incorporates multi-source contexts such as dependency chains which are scattered across multiple commits, at the repository level
and commit history to model change intent and potential impact, presents two major challenges.
overcoming the limitations of diff-centric analysis. To address Chal- Challenge❶: Focusing on diff fragments as input makes it
lenge❷,ChangeWikiemploysarchitecturerecoverytechniquesto difficult to discern the underlying change intent and poten-
extract modular structures and their cross-version differences, and tial impact. Code diffs can explicitly present local editing behav-
designs a bidirectional context-guided hierarchical semantic aggre- iors and describe what changes occurred, yet they provide limited
gationmechanism.Thismechanismsynthesizescode-levelchanges support for reliably inferring why the change was made or what
from the bottom up while simultaneously injecting architectural potential effects it produces.
semanticsastop-downconstraints,enablingholisticunderstanding Using uv__run_timers in the libuv commit #51a22f6 as an ex-
of change interdependencies and system-level impact at the reposi- ample, Figure 1(a) shows the corresponding code diffs and change
tory scale. The resulting summaries maintain semantic coherence summary results. Existing methods [31, 41] typically identify struc-
andtraceabilityacrossgranularitylevels,providingdeveloperswith turalchanges,outputting𝑆 𝑖 thatrefactoruv_run_timerstointroduce
a globally consistent view of software evolution. a ready queue and decouple heap operation from callback execution
We construct a benchmark dataset covering real-world projects via two-phase processing. We observe that this output merely offers
acrossdiversescalesanddomains,comprising1,400annotatedsum- a judgment, i.e., refactoring or optimizing implementation).
mariesatdifferentgranularities.InRQ1,ChangeWikioutperforms However, the actual intent of this modification, as shown in our
thebestbaselineby7.83%inROUGE-L,4.35%inBLEU,and7.54%in summary 𝑆 𝑎𝑏, is to avoid the busy-loop issue caused by starting a
1334

[Vista original de la página 2](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-02.png)

![Página PDF 2, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
1
2
vo
st
i
r
d
u c
u
t
v
h
_
e
_
a
r
p
u
_
n
n
_
o
ti
d
m
e
e
*
r s
h
(
e
u
a
v
p
_
_
l
n
o
o
o
d
p
e
_
;
t* loop) { 1
2
vo
st
i
r
d
u c
u
t
v
h
_
e
_
a
r
p
u
_
n
n
_
o
ti
d
m
e
e
*
r s
h
(
e
u
a
v
p
_
_
l
n
o
o
o
d
p
e
_
;
t* loop) { 𝒔𝒊
V1.44.2
C1… C35…
…
C50…
… … …
C246… C286
V1.48.0
3 uv_timer_t* handle; 3 4 u st v r _ u t c i t m u e v r _ _ _ t* q u h e a u n e d * le q ; ueue_node; refactor uv__run_timers to introduce a ready queue and e900006 64669fd e135dfe
5 struct uv__queue ready_queue; decouple heap operations from callback execution:
6 7 uv__queue_init(&ready_queue); The two phases—"collecting expired timers" and "executing id 𝒔𝒊 changed entities 𝑺𝒂𝒃
5 for (;;) { 9 for (;;) { c st a r l u lb c a tu c r k a s l " m — o w d e if r i e cat s i p o l n it is t s o ues av … oi … d potential re-entrancy and add a thread CPU ① ② i s n rc c / l u u n d i e x / / u t v h . r h ead.c A systematic
1 11 0 uv h i _ f a t i ( n m h d a e l n e r_ d = t l , e c - h o > e n t a i t p m a _ i e n n o e o u r d _ t e o > ) f ; ( l h o e o a p p -> _n ti o m d e e ) , 1 1 4 5 no h i d f a e ( n . h h d a e l n a e p d = ) l ; e c - o > n ti t m ai e n o e u r_ t o > f ( l h o e o a p p -> _n ti o m d e e ) , uv_timer_t, 𝑺𝒂𝒃 C35 a in ff te in rf it a y c e c … on … trol ③ …… src/win/thread.c e th n r h e a a n d c a e n m d e nt the
1 1 1 2 3 4 uv br _ e t a im k; er_stop(handle); 1 1 1 1 6 7 8 9 >n u u o v v b d r _ _ e e t _ .q a i q m k u u ; e e e u r u _ e e s ) _ ; to in p s ( e h r a t n _ d ta le il ) ( ; &ready_queue, &handle- P a C u h ze r a r p n o o g - s m e e s : i : l T li T o s h e f c e ix on p th d ro e t c i p m e o s e s te r in n w g ti i a t o h l f i b n u e a x sy p t - i i l m r o e o e d r p c t i i s a m s l u l e b e r a s c c a k is u . s s e p d li b t y in st t a o rt t i w n o g C50 a a vi d w a d a u s r v e t _ h n t r h e e s r a s e d a c d a C _ p P g a U e b t i c li p t u ie ( s ) ① ② ③u i s v n r _ c c / t l u h u n r d e i e x a / / u d t v h _ . r g h e e a tc d p .c u() s p s y u r n i b m c s h y it s r i t o v e e n m iz f a r t o io m n
2 2 0 1 } phases: removing timers from the heap and collecting them … …… basic
... commit . . 5 . 1a22f6 2 2 2 2 2 .. 2 3 4 5 6 . no w q u u h d h u v v a e i n . l e _ _ q e d u _ _ u e l ( q q e e ! _ u u u u n = e e e v o u u ) _ c d ; e e _ o e _ _ q n r i = u t n e a e m i u i t u n ( v o q e e _ v _ u r _ e _ e e ( q o m u q u f e u p ( e _ q e t u n y u u e o ( e e . _ & d . u _ . h e e n r e ) e _ o ; a a n d d d o e ( y & d ) _ ; e r q , e u u a e v d u _ y e t _ i ) m q ) u { e e r u _ e t, ) ; i I c i n t m a e t l r o l p a b a t t a h i c o c e t k n : r , e P e f a n r r d o e s y m v u _ e r q n in u b ts g e e u i t z n h e e g … e ro e … - t v r m e ig n il g t li e l s r o e e o c d p on c a d a g n a ti i p m n ro e g r in s re r s t e s h s p e ta ro r c t p e u e d r r r l e y w . n i t thi l n oop a C246 u s th e n t r t i e i x n a ,w d g s i p … n r … i … or … ity u t f i o li r t y for ① ② ③ … i s s n r r c c c / / l u w u n d in i e x / / / t u t h v h r . r e h e a ; a d d .c .c e t c a o n o w w n c a a a t r r p r e o d s n l u e s a l c s a n s h t d . i e . o . d . n . u . ling
(a) The modification of uv__run_timers() in commit #51a22f6 (b) The modification across multiple commits
Figure 1: An Example of libuv Project for Motivation
zero-millisecond timers within a timer callback and thus ensuring across two project versions. Figure 2 illustrates the overall frame-
the event loop progress properly. The disparity between𝑆 𝑖 and𝑆 𝑎𝑏 work. The inputs of ChangeWiki are the targeted codebase with
demonstrates that relying solely on diff fragments is insufficient historical commit records and the specified versions; The output is
for accurately uncovering the true intent and effects of changes. a hierarchical natural language summary that captures both code-
This limitation motivates the need to incorporate diverse contexts level modifications and their architectural semantics (i.e., modules
for discerning change semantics. and system-wide impacts) across the version interval, offering a
Challenge❷: It struggles to capture architectural change holistic view absent from fragmented commit descriptions.
semantics at the repository level from scattered commits. To address Challenge❶, ChangeWiki organizes code changes
Modifications related to a common theme often span multiple com- within each file into a hierarchical change entity tree, annotating
mits, with each individual commit reflecting only a local implemen- multi-granularity entities with type-aware multi-source contexts.
tation. When treating each commit as an isolated unit for change This enables better discernment of change intent and potential im-
summarization, it lacks the architectural context to connect these pactbeyondwhatdiff-centricanalysisalonecanprovide.Toaddress
scatteredchanges.Consequently,criticalchangedecisionsandtheir Challenge❷, ChangeWiki first recovers modular structures and
systemic impacts become buried in implementation details, hinder- theircross-versiondifferencesviaarchitecturerecoverytechniques.
ing holistic understanding at the repository scale. It then designs a bidirectional context-guided hierarchical aggre-
Figure 1(b) illustrates the 286 commits in libuv from v1.44.2 to gation mechanism to progressively synthesize multi-granularity
v1.48.0. When generating change summaries 𝑆 𝑖 for each commit entities, producing repository-level summaries that expose the ar-
𝐶 𝑖 individually, we observe that 𝐶 35 adds a thread CPU affinity chitectural semantics and systemic impacts otherwise buried in
control interface, 𝐶 adds thread CPU awareness capabilities via scatteredcommits.Notably,thegeneratedsummarypreservestrace-
50
uv_thread_getcpu(),and𝐶 introducesautilityforsettingthread ability acrosshierarchicallevels,therebylinkinghigh-levelmodular
246
priority. In isolation, these summaries present a fragmented view changes to code-level modifications that underpin them.
of unrelated thread enhancements–a challenge compounded by the
substantial commit distance (e.g., nearly 200 commits between𝐶 3.2 Type-Aware Multi-Granularity Change
35
and𝐶 ), which further obscures architectural change coherence. Contextualization
246
However, when aggregated and analyzed, the result reveals a
To address Challenge❶, this module takes as input two versions
consistent architectural goal underlying these changes. As cap-
tured in 𝑆 𝑎𝑏 (Figure 1(b)), they collectively extend and unify the of a repository, 𝑃 𝑎 and 𝑃 𝑏, along with their commit history, and
outputsasetofcontext-augmentedhierarchicalchangeentitytrees
threadscheduling,evolvingthethreadandsynchronizationprimitive
subsystem from basic encapsulation toward scheduling control and (𝐻 𝑠 ∗). Specifically, ChangeWiki adopts differentiated context ac-
quisition for entities at multiple granularities, including functions,
awareness. This raises a fundamental challenge about integrating
classes,andfiles,andorganizesthemhierarchically.Unlikeexisting
cross-commit changes to expose architectural evolution. Recent
methods[7]thatrelyprimarilyoncodediffs,ChangeWikianchors
empirical findings highlight this challenge, revealing that a sub-
changedescriptionstoconcreteprogramentitiesandenrichesthem
stantial portion of commits (27%) induce architectural changes [50],
withmulti-sourcecontexts,suchasdependency chainsandcommit
highlighting the need for dedicated attention to such evolution.
messages, tailored to each entity’s granularity. This design enables
the recovery of both the intent behind a change and its potential
3 Method
impact.
3.1 Overview
3.2.1 Entity Change Detection. his phase detects code changes at
We propose ChangeWiki , a repository-level code change summa- multiple granularities between 𝑃 𝑎 and 𝑃 𝑏, building on RefDiff [38].
rization method augmented with architectural semantics. It aims to First, we extend the Code Structure Tree proposed by RefDiff, ex-
recover system evolution semantics from scattered code commits panding its modeling scope from coarse-grained entities such as
1335

[Vista original de la página 3](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-03.png)

![Página PDF 3, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
Architecture-Level Change Semantic Abstraction Bidirectional Context-guided
Hierarchical Change Summarization
Modular Structure 𝑨 𝒂 ,𝑨 𝒃 Structure Differencing 𝑴′
Recovery and Weighting project level
CodeBase module level
Change
Type-Aware Multi-Granularity Change Contextualization file level Summary
V: Pa, Pb
Entity Change 𝑫 Hierarchical Change 𝑯
𝒔
Multi-source Change 𝑯𝑺 ∗ class level
Srepo
Detection Entity Tree Construction Context Association
function level
Figure 2: The Overview of ChangeWiki
files, classes, and functions to fine-grained structures like expres- First, we extract the entity’s code context𝐶code(𝑒). Based on the
sions, thereby obtaining a structured representation of the source location recorded in𝜓(𝑣), the code snippets defining or declaring
code. Subsequently, similar to the RefDiff, we perform node match- 𝑒 in versions 𝑃 𝑎 and 𝑃 𝑏 are extracted. Second, we construct the
ingbasedonstructuralfeaturestoestablishentitycorrespondences historicalcommitcontext𝐶cm(𝑒).Usingtheentity’snameandloca-
between the two versions. Finally, we determine specific change tion information, we employ the git command to retrieve historical
types using predefined rules, including basic operations like Add, commitsinvolvingthatentitywithintheversionrange (𝑉 𝑎 ,𝑉 𝑏) and
Remove, and Change, as well as common refactoring behaviors like extract the corresponding commit messages. Furthermore, we con-
ExtractandRename.Theoutputisasetofchangeresults𝐷,where struct a dependency-change context𝐶dep(𝑒) based on a type-aware
each change record 𝑑 ∈ 𝐷 is denoted as 𝑑 = ⟨kind,𝑒 𝑎 ,𝑒 𝑏 ,diff⟩. 𝑑 strategy. For a given changed entity 𝑒, we selectively retrieve its
contains the change type kind, the entity node information𝑒 𝑎 and dependent changed entities 𝑒′ ∈ 𝐸. We consider call, implement,
𝑒 𝑏 from the respective pre- and post-change versions, and a code and link dependencies for function entities, and extend relation-
diff fragment to supplement the fine-grained change description. ships for class entities. We exclude file-level dependency chains
(such as include) to avoid redundant context, as these dependencies
3.2.2 Hierarchical Change Entity Tree Construction. Based on 𝐷 =
are already captured through the functions or classes they con-
{𝑑}, we construct a set of hierarchical change entity tree𝐻 𝑠, which
tain. Therefore, the context-augmented representation for a change
characterizes the program entities that have changed between ver- entity𝑒 is𝑟(𝑒) = (𝐶code(𝑒),𝐶cm(𝑒),𝐶dep(𝑒)).
sions and their hierarchical structure.
On this basis, the attribute information contained in the aug-
First, we extracted all entity nodes from 𝐷. A mapping function mented change entity is denoted as 𝑒∗ = ⟨𝜓(𝑒),𝛾(𝑒),𝑟(𝑒)⟩. The
map(·) maps the matched entity pairs from the two versions into a augmented tree presents as 𝐻∗ = (𝐸∗,𝑇), whose all change entities
unified change entity. Coarse-grained change entities are retained
are associated with the multi-source context. All augmented trees
to form the set:
can be finally obtained as
𝐸 = {map(𝑑.𝑒 𝑎 ,𝑑.𝑒 𝑏) | 𝑑 ∈ 𝐷,level(𝑑.𝑒 𝑎) ∨level(𝑑.𝑒 𝑏) ∈ 𝐺} 𝐻 𝑠 ∗ = {𝐻 1 ∗,𝐻 2 ∗,...𝐻 𝑛 ∗},𝑤ℎ𝑒𝑟𝑒 𝐻 𝑖 ∗ = (𝐸 𝑖 ∗,𝑇 𝑖)
Thus,𝐺 = {File,Class,Function};𝑒 ∈ 𝐸 representsanentitythathas
3.3 Architecture-Level Change Semantic
undergone a change such as addition, deletion, and modification.
Simultaneously; a containment relationship between entities is Abstraction
established to indicate that entity 𝑒 structurally contains entity ToaddressChallenge❷,ChangeWikileveragesarchitecturerecov-
𝑣 according to the scoping rule. After that, the changes for a file
erytechniquestoextractarchitecturalchangefromthesourcecode
w na it m h e in ly a 𝐻 ve = rsi ( o 𝐸 n ,𝑇 ra ) n . g T e h c e a c n h b a e n r g e e p s re fo se r n a t l e l d fi a le s s a i h s i a er s a e r t c o h f ic 𝐻 al 𝑖: structure, 𝑃
st
𝑎
ru
a
c
n
t
d
ur
𝑃
e
𝑏
s
.
b
It
et
t
w
he
e
n
en
id
th
en
e
t
t
i
w
fie
o
s
v
d
e
i
r
ff
si
e
o
r
n
e
s
n
,
c
c
e
h
s
a
i
r
n
ac
t
t
h
e
e
ri
r
z
e
in
c
g
ov
f
e
u
r
n
e
c
d
ti
m
on
o
a
d
l
u
a
l
n
a
d
r
𝐻 𝑠 = {𝐻 1 ,𝐻 2 ,...,𝐻 𝑛},𝑤ℎ𝑒𝑟𝑒 𝐻 𝑖 = (𝐸 𝑖 ,𝑇 𝑖) non-functional changes, and assigning change weights to prioritize
the significance of these changes. Unlike existing repository un-
We then define an attribute structure for each node from 𝐸, derstanding work [19, 49] that organizes system modules solely by
i.e.,𝑒 = ⟨𝜓(𝑒),𝛾(𝑒)⟩. Here, 𝛾(𝑒) = {𝑑 ∈ 𝐷 | map(𝑑.𝑒 𝑎 ,𝑑.𝑒 𝑏) = 𝑒} directorystructure,ChangeWikiincorporatesthisrecoveredarchi-
represents the set of change records from 𝐷 that correspond to𝑒. tectural knowledge to guide the induction of module-level change
𝜓(𝑒) denotes the structural attributes of the entity, including its semantics and enables coherent repository-level understanding.
granularitytype,name,andlocations(LOCnumber)inthepre-and
post-change code, which are extracted from𝑑.𝑒 𝑎 and𝑑.𝑒 𝑏. 3.3.1 ModularStructureRecovery. ChangeWikiemploysthelatest
advanced architecture recovery method, SemArc [52], to recover
3.2.3 Multi-source Change Context Association. After obtaining the architectures from the two versions (𝑃 𝑎, 𝑃 𝑏) respectively. This
𝐻 𝑠, we associate multi-source context information with the change methodfirstcombinescodedependencystructuresandfilesemantic
entities as anchors. The associated context varies by entity type. generated by LLMs to construct a weighted directed graph. Then,
The result is a set of augmented hierarchical change entity trees, and then clusters the graph around core components as anchors to
denoted as 𝐻 𝑠 ∗. recover its modular structure. Through above process, we recover
1336

[Vista original de la página 4](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-04.png)

![Página PDF 4, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
1 2 /* File: src/timer.c */ 1 2 /* File: src/timer.c */ id =10 Type: File 𝜓 & 𝛾 timer.c……
3void uv__run_timers(uv_loop_t* loop) { 3void uv__run_timers(uv_loop_t* loop) { • kind: Add_New_Variable 𝜓 Name: timer.c c13--unix,win: reset the timer
4 5 s u t v r _ u t c i t m h e e r a _ p t _ * n h o a d n e d * l e h ; eap_node; 4 5 6
7
s u s
s
t
t
t v r r
r
_ u u
u
t c
c
c i t
t
t m u h
u
e v e
v
r a _
_
_ p _
_
t _ * q
q
n u
u
h o e
e
a d u
u
n e e
e
d * * l
r
e
e
h q ;
a
e u
d
a e
y
p u
_
_ e
q
n _
u
o n
e
d o
u
e d
e
; e
;
; • •
id
b a
=
f e t f
1
e o r
1
r : e “ : . . N ... o .q n u e eue_node” in Function uv__run_timers[6, 6]
𝛾
L
id
o
:
c
3
: pa=0, pb=0 𝒓 𝑪𝒄𝒎 q c1 u 1 e … ue on stop; As there were…
8 ...... 12 ...... • kind: Add_New_Variable
11 15 • before: None
16 uv_timer_stop(handle); 20 uv_timer_stop(handle); • after: “……ready_queue” in Function uv__run_timers[7, 7]
21&h u a v n _ d _ l q e- u > e n u o e d _ e in .q s u er e t u _ e ta ); il(&ready_queue, id = 12 Type: Function
22 } • kind: Add_Function_Call 𝜓 Name: timer_less_than
17 uv_timer_again(handle); 2 2 2 3 3 4 0 9 w . u h .. v i . _ l .. e t } i ( m !u e v r_ _ a _ g q a u i e n u ( e h _ a e n m dl p e t ) y ; (&ready_queue)) { • • b a u e f v t f _ e o r _ r : r e u “ : u n N v _ o _ t n i _ m e qu e e r u s[ e 2 _ 1 in , 2 se 1 r ] t_tail()”in Function 𝛾 L id o : c : 1 p 4 a=21, pb=35 ……
18 handle->timer_cb(handle); 31 handle->timer_cb(handle); id = 13 𝜓 & 𝛾 uv__run_timers……
1 2 9 0} st } atic int timer_less_than(const struct 3 3 2 3} st } atic int timer_less_than(const struct • • k b i e n fo d r : e A : d N d o _ n S e tmt Type: Function 𝑪𝒄𝒎 c ti 1 m 1 e -- o f u ix t t b im us e y r s l … oop with zero
2 2 2 2 1 3 5 7 h { . h . . . e . a . e a a = p p _ c _ n o n o n o d t d a e e i * n ) ; e h r a _ , o c f o (h n a s , t u st v r _ u t c i t m h e e r a _ p t, _ node* hb) 3 3 3 4 5 7 9 1 h . . . . e . a . a = p _ c n o o n d ta e i * n e h r a _ , o c f o (h n a s , t u st v r _ u t c i t m h e e r a _ p t, _ n no o d d e e * .h h e b a ) p { ); • i • • • d a k b a = f f i e n t t f 1 e e o d r r 4 r : : : e C “ “ : w … h “ a h … n i n l g h o e e e { d _ a … e C p .h _ a } e n l ” l a o _ p i d n A ) e ” F r ) i g ” n u u n i F m n c u t e F i n n o u c t n n ti c u o t n v io _ t n _ im r ti u e m n r_ e _ r l t e i _ m s l s e e _ s r t s h s _ [ a t 2 h n 4 a , [ n 2 2 4 9 [2 , ] 4 2 , 4 2 ] 4] 𝜓 𝛾 N L id o a : c m 1 : e 0 p : , u a 1 = v 1 3 _ , , _ 1 p r 2 u , b = 1 n 3 3 _timers 𝒓 𝑪 𝑪 𝒄 𝒅 𝒐 𝒆 𝒅 𝒑 𝒆 c q 𝑎 𝑏 a : u : l v v e l— o o u i i e d d C _ u u i h n v v a s _ _ n e _ _ g r r r e t u u _ d n n t F a _ _ u i t t l i i n m m c e e ti r r o s s n { { … … } }
(a) Code Diff (b) Change Detection Results 𝑫 (c) A Change Entity Tree 𝑯 (left) and enhanced 𝑯∗(right)
Figure 3: An Example of Type-Aware Multi-Granularity Change Contextualization for libuv
𝐴 𝑎 and𝐴 𝑏 from 𝑃 𝑎 and 𝑃 𝑏, respectively. For𝐴 𝑖: where 𝐸 𝑑𝑒𝑙 and 𝐸 𝑎𝑑𝑑 denote sets of deleted and added files in the
𝐴 𝑖 = ⟨𝐶 𝑖 ,𝑅 𝑖 ,𝑀 𝑖⟩, 𝑚 ∈ 𝑀 𝑖 𝑎𝑛𝑑 𝑚 = ⟨name,𝐹 𝑚 ,𝑆 𝑚⟩
entirerepository,respectively.Foraddedordeletedmodules,𝛿(𝑚′)
captures the structural cost introduced by file changes and module
where𝐶 𝑖 representsthesetofarchitecturalcomponentsinaversion; creation or removal. For matched modules, repository-level file
𝑅 𝑖 represents relationships between components;𝑀 𝑖 represents the additions and deletions are excluded to preserve only the internal
set of modules; name denotes the module name; 𝐹 𝑚 denotes the structural reorganization cost. The module change weight is then
set of source files within the module; and𝑆 𝑚 denotes the module’s obtained through normalization:𝑤 𝑚′ =𝛿(𝑚′)/((cid:205) 𝑚′′∈𝑀′ 𝛿(𝑚′′))
feature description generated by LLMs. A larger𝑤 𝑚′ indicates a greater contribution of the correspond-
ing module to architectural evolution, and thus the module is as-
3.3.2 Structure Differencing and Weighting. To characterize the
signed greater importance in subsequent change semantic genera-
degree of change in modules across versions, we first alignment
tion. It is incorporated into the unified change module representa-
modules by using a bipartite matching, where the module sets
tion described in the next subsection.
from the old and new versions, denoted by 𝑀 𝑎 and 𝑀 𝑏, form the
To uniformly represent architectural evolution information, we
two partitions. For each (𝑚 𝑎 ,𝑚 𝑏) ∈ 𝑀 𝑎 × 𝑀 𝑏, a candidate edge construct a change module𝑚′ for each aligned module, which uni-
is constructed with weight defined as the size of file overlap, i.e.,
formly encapsulates its structural information, functional and non-
𝑠(𝑚 𝑎 ,𝑚 𝑏) = |𝐹(𝑚 𝑎) ∩ 𝐹(𝑚 𝑏)|. We then solve a maximum-weight functional semantics, and change weight derived from a2a. That is,
matchingunderone-to-oneconstraints,therebymaximizingmatch-
𝑚′ = ⟨name,𝐹 𝑚′ ,𝑆 𝑚′ ,𝑤 𝑚′⟩. Here, name is the module name, and
ing strength and coverage. This yields the set of matched module
p de a n ir o s te 𝑀 d 𝑚 a 𝑎 s 𝑡𝑐 𝑀 ℎ. 𝑎 U 𝑑𝑑 n o m r a 𝑀 tc 𝑑 h 𝑒 e 𝑙. d modules in the new or old version are 𝐹 𝐹 ta 𝑚 𝑚 in ′ ′ e = d d e 𝐹 n in 𝑚 o 𝑎 t th e ∪ s e 𝐹 t m 𝑚 h o 𝑏 e d . s u 𝐹 e 𝑚 l t e 𝑎 o fr a f o n s m d ou 𝐹 𝑃 r 𝑚 𝑎 c 𝑏 e a r n fi e d l p e 𝑃 r s e 𝑏 s i ; n e f n s o i t r d t a e h d e t d h s e e e d t m s o o r o f d d s e u o l l e u e t r , e c d d e e m fi fi l o n e d s e u d co le a n s s - ,
ChangeWiki adopts the structural operation counting principle
only the file set from the corresponding version is retained. Simi-
ofthea2ametric[25]toquantifythedegreeofarchitecturalchange.
larly,𝑆 𝑚′ denotes the union of the module’s semantic descriptions
Specifically, a2a measures architectural differences by estimating
the minimum number of structural operations, denoted as mto, from the two versions.Finally,𝑤 𝑚′ denotes the change weight com-
puted in the previous subsection. During the subsequent change
required to transform one architecture into another, including file
summary generation phase, the complete change module repre-
additions, deletions, and movements, as well as module additions
sentation𝑚′ is provided as one of the inputs to the LLM, enabling
and removals: a2a = 1−mto(𝐴 𝑎 ,𝐴 𝑏)/(aco(𝐴 𝑎) +aco(𝐴 𝑏))
the model to consider both the architectural change information
The a2a metric has been widely adopted in architecture-related
and its relative significance, guided by the change weight. Finally,
studies[4,33,51].However,itonlyprovidesaglobal-leveldifference
the architecture-level change information from 𝑃 𝑎 to 𝑃 𝑏 can be
measurementandcannotrevealthecontributionofindividualmod-
represented as the set of change modules:
ules to architectural evolution. Therefore, ChangeWiki borrows
the operation-based view of a2a to define a module-level structural- 𝑀′ = {𝑚 1 ′,𝑚 2 ′,...,𝑚 𝑘 ′ }, 𝑤ℎ𝑒𝑟𝑒 𝑚 𝑖 ′ = ⟨name,𝐹 𝑚′ ,𝑆 𝑚′ ,𝑤 𝑚′⟩
change salience score thatquantifies each module’s involvement in
architectural evolution. Let 𝑀′ = 𝑀 𝑚𝑎𝑡𝑐ℎ ∪𝑀 𝑎𝑑𝑑 ∪𝑀 𝑑𝑒𝑙. For each 3.4 Bidirectional Context-guided Hierarchical
module-level change entity𝑚′ ∈ 𝑀′, the score is defined as:
Change Summarization
𝛿(𝑚′) =  2 2 | | 𝐹 𝐹 𝑚 𝑚𝑏 𝑎 | | + + 1 1 , , 𝑚 𝑚′ ′ ∈ ∈ 𝑀 𝑀 𝑑 𝑎𝑑 𝑒𝑙 𝑑 T le h v i e s l s c ta h g a e ng ta e k m es o a d s u i l n e p s u 𝑀 t t ′ h , e an a d ug g m en en e t r e a d te t s re a es re 𝐻 p 𝑠 ∗ os a i n to d r a y r - c le h v it e e l c h tu ie re r- -


|
|
𝐹
𝐹
𝑚
𝑚𝑏
𝑎
\
\
(
(
𝐸
𝐸 𝑑
𝑎𝑑
𝑒𝑙
𝑑
∪
∪
𝐹
𝐹
𝑚
𝑚
𝑏
𝑎
)
)
|
|
+
, 𝑚′ ∈ 𝑀 𝑚𝑎𝑡𝑐ℎ
a
C
r
h
c
a
h
n
ic
g
a
e
l
W
ch
ik
an
i
g
em
e
p
su
lo
m
ys
m
a
a
b
ry
idi
𝑆
r
r
e
e
c
p
t
o
i
.
o
U
na
n
l
li
c
k
o
e
nt
p
e
u
x
r
t
e
g
l
u
y
id
b
a
o
n
t
c
to
e
m
m
-
e
u
c
p
ha
i
n
de
is
a
m
s,
1337

[Vista original de la página 5](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-05.png)

![Página PDF 5, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
name 𝑭 𝒎′ 𝑺 𝒎′ 𝒘 𝒎′
include/uv.h; include/uv/errno.h; Provides error detection, handling, and propagation during asynchronous I/O
Async I/O Reliability &
src/queue.h; execution to ensure correctness. Emphasizes high reliability and fault 0.22699
Error Handling
docs/code/helloworld/main.c tolerance for stable operation in concurrent environments.
System Testing & Provides system-level testing and platform-specific asynchronous I/O
src/timer.c; src/threadpool.c;
Platform implementations. Emphasizes cross-platform consistency and high test 0.22086
src/win/tcp.c; test/test-tcp-bind.c
Implementation coverage to improve robustness.
Provides a unified event loop and asynchronous execution model across
Event-driven Execution include/uv.h; src/unix/core.c;
operating systems. Emphasizes high performance and scalability for event- 0.15951
Framework src/unix/loop.c; src/win/core.c
driven architectures.
Figure 4: Architecture Change Abstraction Results for Three Modules in libuv
to address Challenge❷: it aggregates lower-level entity changes Algorithm 1 Hierarchical Change Semantic Aggregation
upward while simultaneously injecting high-level architectural se- Require: Enhanced change entity trees 𝐻 𝑠 ∗, architectural change
mantics(i.e.,thoserecoveredin𝑀′ astop-downconstraintstoguide module set 𝑀′, directory hierarchy𝑇
dir
thesummarization.Thisdesignmitigatessemanticdriftandensures Ensure: Repository-level semantic summary𝑆
repo
coherence across layers. The output comprises change semantics 1: Partition 𝐻 𝑠 ∗.𝐸∗ into function set 𝐸 𝑓, class set 𝐸 𝑐, and file set
generated layer by layer for functions, classes, files, modules, and 𝐸
file
the project. 2: 𝐺 𝑓 ← DependDepthGrouping(𝐸 𝑓)
3: 𝐺 𝑐 ← DependDepthGrouping(𝐸 𝑐)
3.4.1 Hierarchical Change Semantic Aggregation. Algorithm1 illus- 4: for each group𝐺 in𝐺 𝑓 do
trates the hierarchical aggregation of change semantics. Let the
directory structure containing the change files be𝑇 = (𝐷dir,𝑇dir), 5: for each changed function with multi-source context𝑒∗ ∈ 𝐺
dir do
where a node𝑑 ∈ 𝐷dir represents a change directory; if𝑑 is a leaf
node, it corresponds to a changed file. An edge (𝑑,𝑝) ∈ 𝑇dir in- 6:
SummarizeByLLM(𝑒∗,𝐻
𝑠
∗.𝑇)
end for
7:
dicates a parent-child relationship between directories. First, the
end for
a i S n l e g g c o o t r h n it e d h , f m u ba n p s c a e t r i d o ti n o ti n o se n d t s e 𝐸 p th 𝑓 e , e n c d e l e a n n s t s i c t y y se c n t o o 𝐸 n d 𝑐 t e , e s a x n i t n , d 𝐸 𝐻 fi 𝑓 𝑠 l ∗ e a b n e y n d t g 𝐸 i r t 𝑐 a y n a s u r e e l t a g 𝐸 ri r fi t o l y e u , ( p o li b e n d t e a b i 1 n y ) - . 1 1 0 1 8 9 : : : : for fo e r S a u c e h a m c g m h r a o ch r u i a p z n e 𝐺 g B e y i d n LL c 𝐺 l M a 𝑐 s ( s d 𝑒 o w ∗, i 𝐻 th 𝑠 ∗. m 𝑇 u ) lti-source context𝑒∗ ∈ 𝐺 do
dependency depth to generate change semantics (lines 2–9). The
end for
generation depth value 𝜋(𝑒) for a change entity is defined as: 12:
end for
13:
𝜋(𝑒) = (cid:40) 0, if𝐶dep(𝑒) = ∅ 1 1 4 5 : : for Su e m ac m h a c r h iz a e n B g y ed LL fi M le ( w 𝑒∗ i , t 𝐻 h 𝑠 ∗ m .𝑇 u ) lti-source context𝑒∗ ∈ 𝐸 file do
1+max𝑒𝑑∈𝐶dep(𝑒) 𝜋(𝑒 𝑑), otherwise
16:
end for
17: Construct directory tree𝑇 dir
Entitiesarethenpartitionedintogroups𝑔 𝑘 = {𝑒 ∈ 𝐸 | 𝜋(𝑒) =𝑘} 18: for each directory node𝑑 in post-order of𝑇 dir do
accordingtotheirdepth.Semanticgenerationisperformedingroup
19:
SummarizeByLLM(𝑑,𝐻
𝑠
∗.𝑇,𝑇
dir,
,𝑀′)
order, and entities within the same group can be processed in par- end for
20:
allel. This strategy ensures that the change semantics of dependent return 𝑆
21: repo
entitiescanbegeneratedfirst,therebyprovidingcompletesemantic
context for subsequent entities.
Subsequently, change semantics are generated for all file entities
𝐸 file (lines10–12).Next,thechangedirectorytree𝑇 dir isconstructed 3.4.2 Unified Semantic Generation by LLM. To generate change se-
basedonthepathinformationofchangefiles(line13).Eachchange manticstailoredfordifferentgranularitylevels,ChangeWikiadopts
directory𝑑 is associated with the architectural module change in- a prompt engineering strategy and designs a unified semantic gen-
formation 𝑀′(𝑑). Thus, the attributes of a directory node can be eration process, SummarizeByLLM, based on a hierarchical prompt
represented as 𝑑 = ⟨𝜓(𝑑),𝑀′(𝑑)⟩, where𝜓(𝑑) denotes the struc- framework. For each change node𝑢 (i.e., code entity or directory),
tural information of the directory, including its path, the set of the process first identifies its node type, selects the corresponding
subdirectories and files it contains; 𝑀′(𝑑) comprises the architec- prompt template according to its granularity, and then invokes
tural change modules associated with the files in 𝑑, defined as the LLM to generate the corresponding semantic summary. The
𝑀′(𝑑) = {𝑚 ∈ 𝑀′ | ∃𝑓 : (𝑑, 𝑓) ∈𝑇 dir ∧ 𝑓 ∈ 𝐹 𝑚 ′ }. prompttemplatesmainlyconsistoftaskdefinition,structuredinput
Finally, by performing a post-order traversal of𝑇 , change se- description, semantic analysis guidance, output format, and genera-
dir
mantics are generated layer by layer and aggregated into architec- tion constraints. The task definition specifies the analysis objective
tural evolution semantics (lines 14–16). of the LLM at the current granularity level, guiding the model to
1338

[Vista original de la página 6](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-06.png)

![Página PDF 6, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
focus on concrete change semantics rather than generating generic Project
descriptions; the structured input description clarifies the semantic ◆Summary: This update signifies a major architectural evolution of the libuv……
roles of different information sources. For code entity nodes, the ◆Functionality Change: Thread Scheduling & Control
prompt incorporates structural information𝜓(𝑢), change records Introduce cross-platform thread scheduling interfaces to support priority control [include/uv.h] ,
CPU affinity binding [test/test-thread-affinity.c] , and runtime CPU querying, enabling fine-
𝛾(𝑢),multi-sourcecontextualinformation𝑟(𝑢),andchildsemantics
grained resource management
𝑆 (𝑢); for directory nodes, ChangeWiki associates correspond- ◆Functionality Change: Event Loop and Timer Mechanism
child
ing architectural module changes 𝑀′(𝑢) through directory and Refactor timer internals[include/uv/win.h, include/uv/unix.h] to eliminate busy loops [src/timer.c],
and prevent memory corruption from improper state reset.
file paths, and combines them with child semantics 𝑆 child (𝑢) to ……
generate module and project-level semantics, where 𝑀′(𝑢) covers
Module: src
addedanddeletedarchitecturalmodulesandmodifiedmodulepairs.
◆Summary: The module change focuses on modernization restructuring and security……
Moreover,thepromptsintroducestructuredsemanticanalysisguid- ◆Functionality Change：Event Loop & Timer
ance, decomposing change understanding into several predefined Restructure the timer execution logic to break the busy loop[src/timer.c], and fix the memory
corruption risk caused by failure to reset queue state[src/uv-common.c] when stopping the timer.
dimensions, including overall change conclusions, before-and-after
◆Non-Functionality Change：Build Compatibility & Memory Safety
differences, detailed change descriptions, related change analysis, Improves build compatibility and memory safety by……
and functional/non-functional characteristic changes. Finally, uni- ……
fied output formats and explicit constraint rules (e.g., analyzing
File:src/timer.c
only based on provided information and avoiding unsupported
◆Conclusion：refactor
dependency inference) are applied to reduce semantic drift and hal- ◆Behavior: ①Timer execution model refactored: two-phase execution and queue-based
lucination during LLM generation. Through iterative refinement of mechanism[uv__run_timers()] ②State management & memory safety fix: state reset and
structure adaptation[timer_less_than()]……
prompt structures, constraint rules, and output organization strate-
◆Reason: Aimed at addressing two key issues……
gies, ChangeWiki establishes stable prompt templates, improving ◆Impact: Fixed the relevant issues……
the consistency, traceability, and reliability of the generated change ◆ before condition: uv_timer_init()change details: Only initializes basic attributes……
semantics. ◆ after condition: uv_timer_init()change details: Add new uv__queue_init() call to ……
Function: src/timer.c uv__run_timers
3.5 A Running Example ◆Conclusion ：refactor
◆Behavior : Changes timer handling from immediate callback execution to deferred execution via
We illustrate the key outputs of ChangeWiki using libuv from a ready queue.
◆Reason: Zero-timeout timers created inside callbacks could be repeatedly triggered during heap
v1.44.2 to v1.48.0. Figure 3 shows the type-aware multi-granularity
traversal, causing a busy loop.
context construction: we obtain a change set 𝐷, then build a hierar- ◆Impact:Improves event loop stability and prevents repeated timer triggering within the same
chicalentitytree𝐻 coveringdifferententitylevels,witheachentity traversal cycle.
◆Dependency:New uv__queue_* APIs provide queue operations used by the refactored
enrichedbymulti-sourcecontexts(commitmessages,dependencies,
implementation. These changes enable the new mechanism but do not semantically require the
code snippets) to form𝐻∗. For example, uv__run_timers is linked modification.
toitscommitsemanticsandcalldependencies.Figure4presentsthe ◆before condition: When handling expired timers, the code directly calls……
recovered changing modules 𝑀′, where a module such as “Async ◆after condition: The local variable ready_queue is introduced as a temporary buffer……
◆detail description: Details of change points and specific analysis of related dependent……
I/O Reliability & Error Handling" illustrates related files, captures
Description: the format like [src/timer.c] indicates thecode change linkage for
functional semantics, and carries a change weight. Figure 5 shows
traceability across change summaries; yellow highlights the change description which
the hierarchical summaries: code-level outputs include change be-
are semantically consistent.
havior,reason,andimpact,whilearchitecture-leveloutputsabstract
functional and non-functional semantics, with cross-level links en- Figure 5: Example of Hierarchical Summarization for libuv
abling traceability.
Overall,ChangeWikielevateschangesemanticsfromwhathap-
pened to why and what impact. For libuv’s 286 commits, 272 files,
ChangeContexting andArchitecture-LevelChangeSemanticAbstrac-
and over 27KLOC, our method provides an overview of evolution
tion, to analyze their contribution to summary quality.
and summarizes the changes into 10 key points across 8 system
RQ3.Howdousersperceivethequalityof ChangeWikiin
features (e.g., thread scheduling, I/O optimization).
terms of semantic accuracy, completeness, readability, and
traceability when generating repository-level change sum-
4 Evaluation Setup maries?Toanswerthisquestion,weconductauserstudyinwhich
participants rate the generated summaries across the four dimen-
We design the following research questions.
RQ1. How effective is ChangeWiki in generating reposi- sions to assess their practical utility in supporting developers’ un-
tory version change summaries? This question is used to evalu- derstanding of repository evolution.
ate the overall effectiveness of the proposed approach. We employ
4.1 Data Construction
well-established automatic metrics to compare our method against
multiple baseline approaches. We select real-world open-source projects from GitHub as eval-
RQ2. What is the impact of the key components on the uation subjects, covering diverse scales and domains to ensure
change summary quality? We conduct ablation studies by pro- representativeness. For each project, we choose two versions with
gressivelyremovingkeycomponents,Type-AwareMulti-Granularity a clear evolution interval and extract the complete commit history
1339

[Vista original de la página 7](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-07.png)

![Página PDF 7, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
4.3 Baseline
and source code within this interval. The selection satisfies three
criteria: (1) Project scale– C/C++ projects exceeding 10 KLOC to Since there are no repository-level change summary tools, we con-
reflect analysis complexity; (2) Change significance–obvious func- structgeneralbaselinesusingLLMs,i.e.,LLMandLLM+CoT.Specif-
tional or architectural evolution between versions (e.g., changed ically, we select three mainstream models, including DeepSeek-
files account for over 50% of total files); (3) Evolution activity–the V3.2,qwen3.5-plus, and Kimi-2.5. To ensure a fair comparison, both
version interval includes more than 80 commits to represent large ChangeWiki and the baseline LLM methods adopt the hierarchi-
change gaps. After selecting candidate projects, we further dis- cal summary generation workflow and receive the identical input
cussedwithdomainexpertsfromthepartnercompany.Theexperts information, including code diffs and commit messages. At each
finally determined the subjects and their key version intervals. hierarchy level, summaries generated for lower-level entities are
Table 1 lists the selected project version pairs. Codebase sizes used as intermediate inputs for summarizing higher-level entities.
range from tens of thousands to millions of lines of code, covering We design two prompt strategies: (1) Direct generation (LLM),
system-level libraries (e.g., libuv), application frameworks (e.g., where the model is instructed with a unified prompt to directly
CEF), and industrial-grade graphics engines (e.g., Skia). generate structured change summaries (2) Chain-of-thought rea-
Due to the lack of publicly available datasets for repository- soning (LLM+CoT), where the model is guided to reason over the
level change summarization, we construct reference summaries for provided change information step by step before generating the
the selected projects and their version pairs using a semi-manual final structured semantic summary.
approach. The construction process consists of three steps. First,
we collect source code, commit messages, release logs, and code
diffs for each version pair. Second, we employ LLMs to generate 5 Evaluation Results
initial reference summaries based on these materials. Third, we
5.1 RQ1 Results
recruit 12 researchers, divided into 4 groups for independent an-
notation. Following established practices in prior work [5, 17], we To evaluate the effectiveness of ChangeWiki , we compare it with
conduct multiple rounds of revision and consensus discussion to LLM-based baseline methods across multiple granularities. The
reachagreement,ensuringannotationqualityandconsistency.Due results are shown in Table 3.
to a large volume of changes and non-trivial manual effort to anno- Overall, ChangeWiki consistently outperforms baseline meth-
tate the change summaries, we perform stratified random sampling ods across all granularities and evaluation metrics, demonstrating
at the module, file, class, and function levels with a ratio of 1:1:2:3, stable improvements. From the average results (Avg), on deepseek-
and cover multiple types of code changes to ensure data diversity. v3.2, ChangeWiki achieves BLEU, ROUGE-L, and BERTScore of
The final benchmark is shown in Table 2. In summary, the dataset 9.95%, 29.95%, and 70.94%, respectively, which significantly sur-
includes 1387 change summaries. pass the LLM baseline (5.60%, 22.12%, and 63.40%). Similar trends
are observed on kimi-2.5 and qwen3.5-plus models, indicating that
ChangeWiki exhibits robustness across LLMs. Furthermore, com-
pared with the LLM+CoT baseline, ChangeWiki maintains advan-
tages on most metrics.
Across different granularities, ChangeWiki demonstrates stable
and consistent performance improvements. At the module level,
4.2 Evaluation Metrics
the advantage of ChangeWiki is particularly highlighted (e.g.,
We employ a set of comprehensive metrics to assess our method. on qwen3.5-plus, ROUGE-L improves from 17.06% to 26.07%), in-
Automatic evaluation metrics. We adopt commonly used dicating its effectiveness in capturing system-level evolutionary
text generation evaluation metrics [20, 41, 45], including BLEU, semantics.Atfinergranularitiessuchasthefilelevelandclasslevel,
ROUGE,andBERTScore,tomeasurethelexicalandsemanticsim- ChangeWiki also consistently outperforms the baselines.
ilarity between generated summaries and benchmark summaries. Notably, LLM+CoT baseline does not outperform the vanilla
BLEU focuses on n-gram precision, ROUGE emphasizes recall, and LLM baseline, and even shows performance degradation on several
BERTScore leverages contextual semantic representations to com- metrics. This suggests that for repository-level change summariza-
pute similarity. tion tasks, merely enhancing reasoning capability is insufficient
Human evaluation metrics. Following the typical evaluation to compensate for the lack of contextual information, and might
criteria proposed in prior work [41, 46, 47], we also assess change introduce redundant or semantically deviated reasoning processes.
summary quality in terms of accuracy, completeness, and read- In contrast, ChangeWiki employs a bidirectional context-guided
ability, each scored on a scale of 1–5. Importantly, to evaluate the hierarchical aggregation mechanism, effectively mitigating seman-
semantic alignment and traceability across change summaries, we tic drift and enabling coherent semantic representations across
introduce a traceability metric. Accuracy assesses whether the different granularities.
summary correctly reflects change semantics without errors or am- Answer to RQ1: Compared with baseline methods, our method
biguities. Completeness evaluates whether the main changes are achieves superior performance on repository-level change summa-
covered without missing key points. Readability measures clarity, rizationtasks.Takingdeepseek-v3.2asanexample,averagedacross
fluency, and logical coherence. Traceability examines whether different granularities, our method improves BLEU, ROUGE-L, and
high-level summaries align with fine-grained changes and support BERTScore by approximately 4.35%, 7.83%, and 7.54%, respectively.
tracing back to underlying details. Consistent improvement can be observed across other models.
1340

[Vista original de la página 8](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-08.png)

![Página PDF 8, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
Table 1: Summary of Selected Projects and Version Intervals
Project Lang Description VersionPair(V1,V2) #Files LOC #ChangedFiles #ChangedLOC #Commits
libnl[27] C Netlinkprotocollibrary (libnl3_0,libnl3_8_0) 612 140.8k 660 111,525 1,687
libuv[28] C AsynchronousI/Olibrary (v1.44.2,v1.48.0) 460 12.9k 319 27,456 286
CEF[3] C++ Embeddedbrowserframework (5735,5,993) 2,130 452.2k 536 12,893 83
jsoncpp[37] C++ JSONprocesslibrary (1.5.4,1.9.3) 241 25.6k 223 13,659 713
Skia[15] C++ 2Dgraphicsrenderingengine (chrome/m132,chrome/m135) 12,031 2503.1k 1,344 85,408 949
Table 2: Benchmark Collection at Different Granularities
to a more pronounced degradation (25%–27%) in architectural-level
change semantics across all metrics.
Project Module File Class/Struct Function Total
libuv 30 25 0 50 105
5.3 RQ3 Results
Skia 60 75 196 91 422
CEF 40 49 160 45 294 To evaluate the practical usability of summaries produced by the
libnl 50 25 0 50 125
approachfromadeveloper’sperspective,weconductedauserstudy
jsoncpp 20 25 37 359 441
followingcommonempiricalevaluationmethodologiesforsoftware
Total 200 199 393 595 1387
engineering tools [20, 26]. We recruited 12 practitioners through
laboratory and industry collaboration channels, all with over four
yearsofsoftwaredevelopmentandmaintenanceexperienceinlarge-
5.2 RQ2 Results
scale C/C++ projects. During the experiment, participants were
To evaluate the contribution of each core module, we design two provided with code diffs and commit information and then asked
ablation settings: w/o context and w/o arch. to evaluate the change summaries generated by ChangeWiki . The
The w/o context removes the code context component centered evaluation dimensions are detailed in section 4.2 , using a 1–5 scale,
on Type-aware Multi-granularity Change Contextualization, using where 1 indicates “very poor / completely unsatisfactory” and 5
only code change information as input, while adjusting prompt of indicates “excellent / fully satisfactory.”
relevantgranularitylevelstoaccommodatethereducedinputfields Each function- and class-level summary was independently eval-
and retaining the architectural semantics provided by Architecture- uated by two participants, while each file- and module-level sum-
Level Change Semantic Abstraction. mary was independently evaluated by four participants. The arith-
The w/o arch removes the architectural information component, metic mean of the scores was used as the final result. For low-
suchthathigh-levelsemanticconstraints(e.g.,architecturalchanges scoring samples, they were additionally required to record the cor-
and module characteristic semantics) are no longer introduced responding issue types (e.g., semantic misunderstanding, missing
duringupper-levelsummarygeneration,andsummariesaredirectly information, unclear expression, or cross-level semantic inconsis-
aggregated based on code-level information. Under this setting, the tency) for subsequent error analysis. All evaluation tasks were
code-level input remains unchanged; therefore, the results at the conducted under a unified experimental environment.
code level remain consistent, with differences primarily reflected Overall, ChangeWiki achieves the highest scores in Accuracy
in the ability to produce module-level summaries. (4.79) and Completeness (4.75), indicating that it can accurately and
Table 4 shows that removing either component leads to perfor- comprehensively reflect the semantics of code changes. Traceabil-
mance degradation. Specifically, w/o context shows a consistent ity (4.56) and Readability (4.67) are slightly lower but still remain
drop across overall metrics (e.g., Avg BERTScore decreases from at a high level, suggesting that the overall quality of generated
71.43% to 70.72%, and BLEU from 6.07% to 5.60%), indicating that summaries is well-balanced.
the absence of multi-source contextual information (e.g., commit In terms of Accuracy, the scores across all granularities are con-
messages and dependency relations) weakens the model’s ability sistently above 4.7, demonstrating that the method effectively cap-
to capture the reason and impact of changes, while also reducing tures the main semantics of code changes. However, developers
semantic alignment and information coverage. In addition, the per- report some insufficient understanding of boundary conditions,
formance at the architectural level also declines under this setting. call relationships, or the scope of change impact generated by our
In contrast, removing architectural semantics (w/o arch) results results, leading to imprecise descriptions of certain details. Regard-
in more obvious degradation, e.g., BERTScore drops from 60.55% ing Completeness, the overall score is also high, especially at the
to 44.69%, and ROUGE-L from 24.39% to 17.8%. This indicates that, class level (4.93), indicating that the model can adequately cover
without module-level alignment and architectural semantic con- key change information. We also observed that, in function-level
straints, the model struggles to reconstruct system-level evolution- scenarios, due to scattered changes or cross-function dependencies,
ary information from fragmented code changes and is therefore partial information may still be missing.
more prone to semantic drift during summary organization. For Readability, the module level and file level achieve higher
Answer to RQ2. Compared with the full version of our method, scores (4.82 and 4.92), suggesting that higher-level summaries have
removing the code context component leads to an average decline, clearerstructureandmorefluentexpression.Incontrast,Readability
withBLEUandROUGE-Ldecreasingby7.7%and5.2%,respectively. decreases a little at the class level and function level (4.53 and 4.39),
The corresponding metrics for architectural-level summaries drop mainly because the produced summaries sometimes over-specify
by 10.9% and 10.3%. Removing the architectural component leads fine-grained modifications, making them less readable to users. For
1341

[Vista original de la página 9](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-09.png)

![Página PDF 9, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
Table 3: Automatic evaluation results(%) for RQ1
Module File Class Function Avg
Method Model
BLEU ROUGE-L BERTScore BLEU ROUGE-L BERTScore BLEU ROUGE-L BERTScore BLEU ROUGE-L BERTScore BLEU ROUGE-L BERTScore
deepseek-v3.2 11.48 25.50 59.88 9.73 29.71 74.43 8.25 31.92 75.02 10.34 32.68 74.45 9.95 29.95 70.94
ChangeWiki kimi-2.5 11.40 26.07 67.46 10.92 30.64 74.55 11.06 34.05 76.09 12.04 33.90 75.09 11.36 31.17 73.30
qwen3.5-plus 10.91 24.41 60.48 10.03 31.23 74.87 7.49 30.57 75.07 9.91 31.55 74.20 9.58 29.44 71.16
deepseek-v3.2 3.11 11.98 38.02 5.54 23.02 70.71 6.34 26.28 72.41 7.41 27.20 72.48 5.60 22.12 63.40
LLM kimi-2.5 0.93 6.99 28.33 5.75 22.10 69.80 5.74 26.64 73.49 8.08 28.55 73.41 5.13 21.07 61.26
qwen3.5-plus 3.66 17.06 56.16 5.67 22.24 70.79 4.55 25.37 73.14 6.71 27.28 73.10 5.15 22.99 68.30
deepseek-v3.2 3.45 7.04 18.11 5.36 23.92 71.67 7.50 29.18 73.83 7.06 28.29 73.01 5.84 22.11 59.15
LLM+CoT kimi-2.5 2.82 6.12 16.62 7.17 24.70 71.69 7.36 30.10 74.11 6.95 28.14 72.75 6.08 22.27 58.79
qwen3.5-plus 3.94 8.68 22.45 5.85 25.01 72.40 8.25 30.26 74.54 8.41 29.63 73.49 6.61 23.39 60.72
Table4:Ablationresultsunderarchitectureandcode-level(%)
have implemented ChangeWiki as an interactive web-based sys-
tem. The system is built with Vue [44] and a component library
Code-level for the frontend, with the backend powered by the Flask frame-
Method Metric Arch Avg
work [12]. Users input a repository URL and a version interval,
Behav. Reason Impact
and our system automatically executes the entire analysis pipeline.
BLEU 11.16 12.12 3.93 2.15 6.07 The interface presents results in a structured, expandable tree view
ChangeWiki ROUGE-L 24.39 38.35 25.07 21.03 28.15 that visualizes the hierarchical relationships among modules, files,
BERTScore 60.55 76.05 70.34 67.88 71.43 classes, and functions, with change summaries and code snippets
displayed in a linked panel. Hyperlinks support cross-layer naviga-
BLEU 9.94 12.58 2.47 1.74 5.60
ChangeWiki tion and traceability. Users can expand nodes to inspect details or
ROUGE-L 21.89 38.89 21.30 19.89 26.69
w/o context
BERTScore 56.35 76.06 68.88 67.24 70.72 collapse them for a high-level overview of change summaries. Our
demo system is available in our public repository.
ChangeWiki BLEU 8.28 12.12 3.93 2.15 6.07 Industrial Application. Our ChangeWiki has been applied
ROUGE-L 17.85 38.35 25.07 21.03 28.15
w/o arch through collaboration with an industry partner. The partner in-
BERTScore 44.69 76.05 70.34 67.88 71.43
tegrated it into their internal workflow for version synchroniza-
tion between their codebase and upstream dependencies. When an
Table 5: Manual Evaluation Across Four Dimensions. upstream library changes, the downstream must synchronize to
maintain co-evolution. Developers reported that the hierarchical
Metric Module File Class Function Avg. summaries generated by ChangeWiki significantly reduced the
effort to understand changes across large version gaps. They partic-
# Samples 50 50 100 150 350 ularly valued output traceability supported by ChangeWiki –the
Accuracy 4.83 4.81 4.78 4.74 4.79 ability to navigate from architectural-level descriptions down to
Completeness 4.75 4.71 4.93 4.59 4.75 code-level modifications–which improved issue localization caused
Readability 4.82 4.92 4.53 4.39 4.67
byupstreamchanges.Furthermore,thepartnerplanstoincorporate
Traceability 4.48 4.35 4.86 – 4.56
ChangeWikiintotheirreleasenotegenerationtoautomatechange
summaries. This feedback highlights the potential of our work to
support repository-level change understanding in co-evolution and
Traceability, the overall score is 4.56, with stable performance at
release management scenarios.
the module, file, and class levels. However, we observed that some
summaries do not explicitly indicate the sources of changes, or the
tracing paths are unclear in cross-file scenarios. 6.2 Limitations
Answer to RQ3: The results show that ChangeWiki received
Despite the encouraging results achieved by ChangeWiki , sev-
an overall average rating of approximately 4.5 out of 5 across all
eral limitations remain. First, ChangeWiki may be less effective or
four dimensions, indicating that the generated summaries are ac-
even inapplicable for projects with poor modularization or severely
curate, complete, and readable to users, and effectively support
degraded architecture. The effectiveness of our approach depends
understanding of repository evolution.
on the quality of architecture recovery to guide the LLM in under-
6 Discussion standingversionevolution.Insuchprojects,therecoveredmodular
structureislikelytobeincompleteorinaccurate,whichcanmislead
6.1 Implications
subsequentrepository-levelevolutioninferenceandcausemisalign-
We demonstrate the practical value of ChangeWiki from two ment between code-level changes and their architectural semantics.
perspectives, i.e., system usability and industrial application. Second, ChangeWiki ’s bidirectional context guidance mechanism
Practical Deployment and Usability. To facilitate the adop- relies on clear dependency-chain contexts. For projects with sparse
tion of our approach in real-world development workflows, we or tangled dependency structures, our granularity-differentiated
1342

[Vista original de la página 10](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-10.png)

![Página PDF 10, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
context acquisition strategy may struggle to fully capture the in- method and variable change detection, as well as RefDiff [38, 39]
tended evolution semantics. Third, ChangeWiki relies on LLMs for for multi-language support. Building upon such techniques,
semantic summary generation, which introduces significant compu- we organizes detected changes into a hierarchical, multi-
tational overhead. For large-scale repositories containing thousands granularity structure and enriches entities with type-aware
of commits, the time and resource costs may be non-negligible. multi-source contexts to support subsequent summarization.
Code Change Summarization. Such work aims to generate
6.3 Threats to Validity natural language descriptions that explain the modifications made
to source code. Early approaches [29] relied on pre-defined rules to
First, the performance of ChangeWiki depends on the accuracy of
extract key information from code diffs. Subsequent work adopted
changedetection,architecturerecoveryandthequalityofintermediate
neuralmachinetranslationmodels[21]withenhancementssuchas
hierarchical summaries. Errors in lower-level summaries may prop-
data cleaning, retrieval augmentation [32], hybrid frameworks [30,
agate to higher levels during hierarchical generation. To mitigate
46], and graph structures for semantic representation [8, 30]. With
this issue, we extended the mature tool RefDiff [38] for change de-
large-scale pretraining on code corpora [31], some methods in-
tection based on AST difference, achieving 94.6% accuracy through
corporate commit history or issues as contextual signals [9, 47].
sampling validation on a dataset containing 13.8k change detec-
Recently,theintroductionofLLMs[11]significantlyimprovesread-
tion results. We adopted the state-of-the-art architecture recovery
ability [48]. Unlike single-commit summarization, our work
methodSemArc,whichrecentworkhasshowntoimproveaccuracy
address the repository-level change summaries.
by 32% over eight existing approaches [52]. Additionally, like other
Repository-Level Code Understanding. Recent efforts have
LLM-based methods, ChangeWiki ’s performance is sensitive to
explored holistic modeling and documentation generation for code-
LLM capability. To address this, we evaluated our method with
bases. CodeWiki [19] constructs dependency graphs and module
multiple mainstream LLMs in RQ1.
hierarchies combined with multi-agent generation to produce the
Second, the manual construction of the benchmark may introduce
repository-level documentation. Similarly, DocAgent [49] lever-
subjective bias and potential leakage from LLM-assisted drafting. To
ages dependency graphs and collaborative agents to generate struc-
mitigate this, we recruited 12 researchers, divided into 4 groups for
tured the component-level documentation. Industrial tools such
independent annotation. Following established practices in prior
as Google’s CodeWiki [14] and Cognition AI’s DeepWiki [6] also
work [5, 17], we conducted multiple rounds of revision and consen-
support repository-level understanding and interactive question
sus discussion to reach agreement. Specifically, qwen3.5-plus was
answering.Theseworksprimarilyfocusonstaticcodebaseun-
onlyusedforinitialdraftgeneration,whileallreferencesummaries
derstanding,neglectingsoftwareevolution.ChangeWikican
were manually revised and validated. Table 3 shows no clear per-
capture version change semantics, serving as an evolution-
formance advantage for qwen3.5-plus over other LLMs, suggesting
aware counterpart to DeepWiki.
low risk of leakage, although such bias cannot be fully excluded.
Third,humanevaluationmaybeinfluencedbyindividualcognitive 8 Conclusion
differences..Toreducethebias,followingpriorwork[41,46,47],we
We presented ChangeWiki , an architecture semantic-augmented
employ multiple independent reviewers and average their scores
to mitigate potential individual subjectivity. Fourth, the external va- approach for repository-level change summarization. By introduc-
lidity primarily concerns the generalizability of our approach. While ing multi-source context enrichment and bidirectional hierarchical
aggregation guided by architectural semantics, ChangeWiki cap-
ChangeWiki is conceptually language-agnostic, its applicability in
tures both local modifications and system-level evolution, generat-
other programming environments remains to be validated. Our ex-
ing coherent and traceable summaries across versions. Extensive
periments selected C/C++ projects based on scale, domain, and evo-
evaluations on real-world projects demonstrate that the approach
lutionary activity, with domain experts from our industry partner
achieves significant improvements in semantic accuracy, complete-
involved in project selection and result analysis. The current imple-
ness, and cross-granularity coherence. A prototype deployed in an
mentation relies on language-specific program analysis techniques,
industrial setting further validates its practical value. Future work
such as AST extraction and dependency analysis. In the future, we
includes extending ChangeWiki to multi-language ecosystems,
will leverage multi-language analysis tools (e.g., ENRE[22, 23]) to
integrating it with code review workflows, and exploring its poten-
extend the evaluation to more programming languages.
tial for other software evolution tasks such as architectural change
7 Related Work prediction and impact analysis.
This section discusses related work from three perspectives. Code Acknowledgments
Change Detection. Existing approaches can be categorized into
This work was supported by the National Natural Science Founda-
text-based and AST-based differencing. Text-based methods [36]
tion of China (62232014, 62372368, 62272377, 62293501, 62293502,
identify line-level insertions and deletions. AST-based approaches
62032010, and 62372367), the XJTU Research Fund for AI Science
capture syntactic structural changes by comparing tree representa-
(No. 2025YXYC004), and the CCF–Huawei Populus Grove Fund.
tions, enabling fine-grained operation detection such as insertion,
deletion, movement, and update [2, 10, 13]. Building on these tech- 9 Data Availability Statement
niques, many studies incorporate entity modeling to support pro-
Thedatasetandcodeareavailableathttps://doi.org/10.5281/zenodo.
gram element tracking and refactoring detection. Representative
19251834.Ademovedioisavailableathttps://youtu.be/5y0astdbmIA.
tools include CodeTracker [24] and RefactoringMiner [42, 43] for
1343

[Vista original de la página 11](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-11.png)

![Página PDF 11, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

ASE’26,October12–16,2026,Munich,Germany ZijunWang,WuxiaJin,JialeLi,ZhanhongMou,andTingLiu
References
2019IEEE/ACM41stInternationalConferenceonSoftwareEngineering:Companion
[1] AlbertoBacchelliandChristianBird.2013. Expectations,outcomes,andchal- Proceedings(ICSE-Companion).67–70. doi:10.1109/ICSE-Companion.2019.00040
lengesofmoderncodereview.In201335thInternationalConferenceonSoftware [23] WuxiaJin,ShuoXu,DaweiChen,JiajunHe,DinghongZhong,MingFan,Hongxu
Engineering(ICSE).712–721. doi:10.1109/ICSE.2013.6606617 Chen,HuijiaZhang,andTingLiu.2024. PyAnalyzer:AnEffectiveandPractical
[2] SudarshanS.Chawathe,AnandRajaraman,HectorGarcia-Molina,andJennifer
ApproachforDependencyExtractionfromPythonCode.InProceedingsofthe
Widom. 1996. Change detection in hierarchically structured information. In IEEE/ACM46thInternationalConferenceonSoftwareEngineering (Lisbon,Por-
Proceedingsofthe1996ACMSIGMODInternationalConferenceonManagement tugal)(ICSE’24).AssociationforComputingMachinery,NewYork,NY,USA,
ofData(Montreal,Quebec,Canada)(SIGMOD’96).AssociationforComputing Article112,12pages. doi:10.1145/3597503.3640325
Machinery,NewYork,NY,USA,493–504. doi:10.1145/233269.233366 [24] Mehran Jodavi and Nikolaos Tsantalis. 2022. Accurate method and variable
[3] Chromium Embedded Framework contributors. n.d.. Chromium Embedded
trackingincommithistory.InProceedingsofthe30thACMJointEuropeanSoftware
EngineeringConferenceandSymposiumontheFoundationsofSoftwareEngineering
Framework(CEF). https://github.com/chromiumembedded/cef. AccessedJuly
14,2025.
(Singapore,Singapore)(ESEC/FSE2022).AssociationforComputingMachinery,
[4] DiCui,JiaqiGuo,TingLiu,andQinghuaZheng.2021. AnEmpiricalStudyof NewYork,NY,USA,183–195. doi:10.1145/3540250.3549079
ArchitecturalChangesinCodeCommits.InProceedingsofthe12thAsia-Pacific [25] DucMinhLe,PooyanBehnamghader,JoshuaGarcia,DanielLink,ArmanShah-
SymposiumonInternetware(Singapore,Singapore)(Internetware’20).Association bazian,andNenadMedvidovic.2015.AnEmpiricalStudyofArchitecturalChange
for Computing Machinery, New York, NY, USA, 11–20. doi:10.1145/3457913.
inOpen-SourceSoftwareSystems.In2015IEEE/ACM12thWorkingConference
3457924 onMiningSoftwareRepositories.235–245. doi:10.1109/MSR.2015.29
[5] FarbodDaneshyan,RunzhiHe,JianyuWu,andMinghuiZhou.2025. SmartNote: [26] JennyT.Liang,ChenyangYang,andBradA.Myers.2024. ALarge-ScaleSurvey
AnLLM-Powered,PersonalisedReleaseNoteGeneratorThatJustWorks. Pro- ontheUsabilityofAIProgrammingAssistants:SuccessesandChallenges.In
ceedingsoftheACMonSoftwareEngineering 2(062025),1663–1686. doi:10.1145/ ProceedingsoftheIEEE/ACM46thInternationalConferenceonSoftwareEngineering
3729345
(Lisbon,Portugal)(ICSE’24).AssociationforComputingMachinery,NewYork,
[6] DeepWikicontributors.n.d.. DeepWiki. https://deepwiki.com/. AccessedJuly14, NY,USA,Article52,13pages. doi:10.1145/3597503.3608128
2025. [27] libnlcontributors.n.d.. libnl:NetlinkProtocolLibrarySuite. https://github.com/
[7] JinhaoDong,YilingLou,DanHao,andLinTan.2023. RevisitingLearning-Based thom311/libnl. AccessedJuly14,2025.
CommitMessageGeneration.InProceedingsofthe45thInternationalConference [28] libuvcontributors.n.d.. libuv:Cross-PlatformAsynchronousI/OLibrary. https:
onSoftwareEngineering (Melbourne,Victoria,Australia)(ICSE’23).IEEEPress, //github.com/libuv/libuv/. AccessedJuly14,2025.
794–805. doi:10.1109/ICSE48619.2023.00075 [29] Mario Linares-Vásquez, Luis Fernando Cortés-Coy, Jairo Aponte, and Denys
[8] JinhaoDong,YilingLou,QihaoZhu,ZeyuSun,ZhilinLi,WenjieZhang,andDan Poshyvanyk.2015. ChangeScribe:AToolforAutomaticallyGeneratingCommit
Hao.2022. FIRA:Fine-GrainedGraph-BasedCodeChangeRepresentationfor Messages. In 2015 IEEE/ACM 37th IEEE International Conference on Software
AutomatedCommitMessageGeneration.In2022IEEE/ACM44thInternational Engineering,Vol.2.709–712. doi:10.1109/ICSE.2015.229
ConferenceonSoftwareEngineering(ICSE).970–981. doi:10.1145/3510003.3510069 [30] ShangqingLiu,CuiyunGao,SenChen,LunYiuNie,andYangLiu.2022. ATOM:
[9] Aleksandra Eliseeva, Yaroslav Sokolov, Egor Bogomolov, Yaroslav Golubev, CommitMessageGenerationBasedonAbstractSyntaxTreeandHybridRanking
DannyDig,andTimofeyBryksin.2024. FromCommitMessageGenerationto . IEEETransactionsonSoftwareEngineering48,05(May2022),1800–1817. doi:10.
History-AwareCommitMessageCompletion.InProceedingsofthe38thIEEE/ACM 1109/TSE.2020.3038681
InternationalConferenceonAutomatedSoftwareEngineering(Echternach,Luxem- [31] ShangqingLiu,YanzhouLi,XiaofeiXie,WeiMa,GuozhuMeng,andYangLiu.
bourg)(ASE’23).IEEEPress,723–735. doi:10.1109/ASE56229.2023.00078 2024. AutomatedCommitIntelligencebyPre-training. ACMTrans.Softw.Eng.
[10] Jean-RémyFalleri,FloréalMorandat,XavierBlanc,MatiasMartinez,andMartin Methodol.33,8,Article201(Nov.2024),30pages. doi:10.1145/3674731
Monperrus.2014. Fine-grainedandaccuratesourcecodedifferencing.InPro- [32] ZhongxinLiu,XinXia,AhmedE.Hassan,DavidLo,ZhenchangXing,andXinyu
ceedingsofthe29thACM/IEEEInternationalConferenceonAutomatedSoftware Wang. 2018. Neural-machine-translation-based commit message generation:
Engineering(Vasteras,Sweden)(ASE’14).AssociationforComputingMachinery, howfararewe?.InProceedingsofthe33rdACM/IEEEInternationalConference
NewYork,NY,USA,313–324. doi:10.1145/2642937.2642982
onAutomatedSoftwareEngineering (Montpellier,France)(ASE’18).Association
[11] LishuiFan,JiakunLiu,ZhongxinLiu,DavidLo,XinXia,andShanpingLi.2025. forComputingMachinery,NewYork,NY,USA,373–384. doi:10.1145/3238147.
ExploringtheCapabilitiesofLLMsforCode-Change-RelatedTasks. ACMTrans. 3238190
Softw.Eng.Methodol.34,6,Article159(July2025),36pages. doi:10.1145/3709358 [33] ThibaudLutellier,DevinChollak,JoshuaGarcia,LinTan,DerekRayside,Nenad
[12] Flaskcontributors.n.d.. Flask. https://flask.palletsprojects.com/en/stable/. Ac- Medvidovic,andRobertKroeger.2015. ComparingSoftwareArchitectureRe-
cessedJuly14,2025.
coveryTechniquesUsingAccurateDependencies.In2015IEEE/ACM37thIEEE
[13] Beat Fluri, Michael Wursch, Martin PInzger, and Harald Gall. 2007. Change InternationalConferenceonSoftwareEngineering,Vol.2.69–78. doi:10.1109/ICSE.
Distilling:TreeDifferencingforFine-GrainedSourceCodeChangeExtraction. 2015.136
IEEETransactionsonSoftwareEngineering 33,11(2007),725–743. doi:10.1109/ [34] MockusandVotta.2000. Identifyingreasonsforsoftwarechangesusinghistoric
TSE.2007.70731
databases.InProceedings2000InternationalConferenceonSoftwareMaintenance.
[14] Google.n.d.. CodeWiki. https://codewiki.google/. AccessedJuly14,2025. 120–130. doi:10.1109/ICSM.2000.883028
[15] GoogleSkiaTeam.n.d.. SkiaGraphicsLibrary. https://github.com/google/skia. [35] LauraMoreno,JairoAponte,GiriprasadSridhara,AndrianMarcus,LoriPollock,
AccessedJuly14,2025. andK.Vijay-Shanker.2013.Automaticgenerationofnaturallanguagesummaries
[16] RenanGreca,BrenoMiranda,andAntoniaBertolino.2023. StateofPractical
forJavaclasses.In201321stInternationalConferenceonProgramComprehension
ApplicabilityofRegressionTestingResearch:ALiveSystematicLiteratureReview. (ICPC).23–32. doi:10.1109/ICPC.2013.6613830
ACMComput.Surv.55,13s,Article274(July2023),36pages. doi:10.1145/3579851 [36] EugeneW.Myers.1986. AnO(ND)differencealgorithmanditsvariations. Algo-
[17] JiaweiGuo,HaoranYang,andHaipengCai.2025. VerLog:EnhancingRelease rithmica1,1–4(Nov.1986),251–266. doi:10.1007/BF01840446
NoteGenerationforAndroidAppsusingLargeLanguageModels. Proc.ACM [37] Open-Source-Parserscontributors.n.d.. JsonCpp:AC++LibraryforInteracting
Softw.Eng.2,ISSTA,ArticleISSTA084(June2025),23pages. doi:10.1145/3728961 withJSON. https://github.com/open-source-parsers/jsoncpp. AccessedJuly14,
[18] AhmedE.Hassan.2009. Predictingfaultsusingthecomplexityofcodechanges. 2025.
In2009IEEE31stInternationalConferenceonSoftwareEngineering.78–88. doi:10. [38] DaniloSilva,JoãoPaulodaSilva,GustavoSantos,RicardoTerra,andMarcoTulio
1109/ICSE.2009.5070510 Valente.2021. RefDiff2.0:AMulti-LanguageRefactoringDetectionTool. IEEE
[19] AnhNguyenHoang,MinhLe-Anh,BachLe,andNghiD.Q.Bui.2026. CodeWiki: TransactionsonSoftwareEngineering 47,12(2021),2786–2802. doi:10.1109/TSE.
Evaluating AI’s Ability to Generate Holistic Documentation for Large-Scale 2020.2968072
Codebases. In Findings of the Association for Computational Linguistics: ACL [39] DaniloSilvaandMarcoTulioValente.2017. RefDiff:detectingrefactoringsin
2026,MariaLiakata,VivianeP.Moreira,JiajunZhang,andDavidJurgens(Eds.). versionhistories.InProceedingsofthe14thInternationalConferenceonMining
AssociationforComputationalLinguistics,SanDiego,California,UnitedStates,
SoftwareRepositories(BuenosAires,Argentina)(MSR’17).IEEEPress,269–279.
5812–5827. doi:10.18653/v1/2026.findings-acl.288 doi:10.1109/MSR.2017.14
[20] YuanHuang,ZhicaoTang,XiangpingChen,ChanglinYang,ZibinZheng,and [40] Margaret-AnneD.Storey,DavorČubranić,andDanielM.German.2005. Onthe
XiaocongZhou.2025. CommitMessagesGenerationBasedonCoreChanges. useofvisualizationtosupportawarenessofhumanactivitiesinsoftwaredevel-
ACMTrans.Softw.Eng.Methodol.(July2025). JustAccepted. doi:10.1145/3750039 opment:asurveyandaframework.InProceedingsofthe2005ACMSymposium
[21] SiyuanJiang,AmeerArmaly,andCollinMcMillan.2017. Automaticallygenerat-
onSoftwareVisualization(St.Louis,Missouri)(SoftVis’05).AssociationforCom-
ingcommitmessagesfromdiffsusingneuralmachinetranslation.In201732nd putingMachinery,NewYork,NY,USA,193–202. doi:10.1145/1056018.1056045
IEEE/ACM International Conference on Automated Software Engineering (ASE). [41] WeiTao,YuchengZhou,YanlinWang,HongyuZhang,HaofenWang,andWen-
135–146. doi:10.1109/ASE.2017.8115626 qiangZhang.2024. KADEL:Knowledge-AwareDenoisingLearningforCommit
[22] WuxiaJin,YuanfangCai,RickKazman,QinghuaZheng,DiCui,andTingLiu. MessageGeneration. ACMTrans.Softw.Eng.Methodol.33,5,Article133(June
2019. ENRE: A Tool Framework for Extensible eNtity Relation Extraction. In 2024),32pages. doi:10.1145/3643675
1344

[Vista original de la página 12](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-12.png)

![Página PDF 12, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

ChangeWiki: Repository-LevelChangeSummarizationAugmentedwithArchitectureSemantics ASE’26,October12–16,2026,Munich,Germany
[42] NikolaosTsantalis,AmeyaKetkar,andDannyDig.2022. RefactoringMiner2.0. Engineering 50,12(2024),3208–3224. doi:10.1109/TSE.2024.3478317
IEEETransactionsonSoftwareEngineering 48,3(2022),930–950. doi:10.1109/TSE. [49] DayuYang,AntoineSimoulin,XinQian,XiaoyiLiu,YuweiCao,ZhaopuTeng,
2020.3007722 andGreyYang.2025. DocAgent:AMulti-AgentSystemforAutomatedCode
[43] NikolaosTsantalis,MatinMansouri,LalehM.Eshkevari,DavoodMazinanian, DocumentationGeneration.InProceedingsofthe63rdAnnualMeetingoftheAsso-
andDannyDig.2018. Accurateandefficientrefactoringdetectionincommit ciationforComputationalLinguistics(Volume3:SystemDemonstrations),Pushkar
history.InProceedingsofthe40thInternationalConferenceonSoftwareEngineering Mishra,SmarandaMuresan,andTaoYu(Eds.).AssociationforComputational
(Gothenburg,Sweden)(ICSE’18).AssociationforComputingMachinery,New Linguistics,Vienna,Austria,460–471. doi:10.18653/v1/2025.acl-demo.44
York,NY,USA,483–494. doi:10.1145/3180155.3180206 [50] WenjingZhan,RanMo,YingjieJiang,andDongyuWang.2025. Just-in-Time
[44] Vue.jscontributors.n.d.. Vue.js. https://vuejs.org/. AccessedJuly14,2025. PredictionofSoftwareArchitecturalChangesThroughCommit-LevelAnalyses.
[45] GuoqingWang,ZeyuSun,JinhaoDong,YuxiaZhang,MingxuanZhu,Qingyuan IEEETransactionsonSoftwareEngineering 51,8(2025),2285–2304. doi:10.1109/
Liang, and Dan Hao. 2025. Is It Hard to Generate Holistic Commit Message? TSE.2025.3587849
ACMTrans.Softw.Eng.Methodol.34,2,Article36(Jan.2025),28pages. doi:10. [51] YiranZhang,ZhengziXu,ChengweiLiu,HongxuChen,JianwenSun,DongQiu,
1145/3695996 andYangLiu.2023. SoftwareArchitectureRecoverywithInformationFusion.
[46] HaoyeWang,XinXia,DavidLo,QiangHe,XinyuWang,andJohnGrundy.2021. InProceedingsofthe31stACMJointEuropeanSoftwareEngineeringConference
Context-awareRetrieval-basedDeepCommitMessageGeneration. ACMTrans. andSymposiumontheFoundationsofSoftwareEngineering (SanFrancisco,CA,
Softw.Eng.Methodol.30,4,Article56(July2021),30pages. doi:10.1145/3464689 USA)(ESEC/FSE2023).AssociationforComputingMachinery,NewYork,NY,
[47] LiranWang,XunzhuTang,YichenHe,ChangyuRen,ShuhuaShi,ChaoranYan, USA,1535–1547. doi:10.1145/3611643.3616285
andZhoujunLi.2024.DelvingintoCommit-IssueCorrelationtoEnhanceCommit [52] Wenting Zhao, Wuxia Jin, Yiran Zhang, Ming Fan, Haijun Wang, Li Li, Yang
MessageGenerationModels.InProceedingsofthe38thIEEE/ACMInternational Liu, and Ting Liu. 2026. Software Architecture Recovery Augmented With
ConferenceonAutomatedSoftwareEngineering (Echternach,Luxembourg)(ASE Semantics. IEEETransactionsonSoftwareEngineering52,01(Jan.2026),338–359.
’23).IEEEPress,710–722. doi:10.1109/ASE56229.2023.00050 doi:10.1109/TSE.2025.3620670
[48] PengyuXue,LinhaoWu,ZhongxingYu,ZhiJin,ZhenYang,XinyiLi,Zhenyu
Yang,andYueTan.2024. AutomatedCommitMessageGenerationWithLarge Received2026-03-26;accepted2026-06-18
LanguageModels:AnEmpiricalStudyandBeyond.IEEETransactionsonSoftware
1345

[Vista original de la página 13](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-13.png)

![Página PDF 13, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/primary/time%20traversal/ChangeWiki/page-13.png)
