# Rambo: Enhancing RAG-based repository-level method body completion

- source_pdf: ../../../../../pdf/Same%20Solution/secondary/Rambo.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

Contents lists available at ScienceDirect
Information and Software Technology
journal homepage: www.elsevier.com/locate/infsof
 
Rambo: Enhancing RAG-based repository-level method body completion
Tuan-Dung Bui
, Thieu Luu
, Thanh-Phat Nguyen
, Thu-Trang Nguyen
, Hieu Dinh Vo
∗, 
Son Nguyen
Faculty of Information Technology, VNU University of Engineering and Technology, Hanoi, Viet Nam
A R T I C L E  I N F O
Keywords:
Code completion
Repository-level
Method body completion
RAG-based code completion
Code LLMs
 
A B S T R A C T
Code completion is essential in software development, helping developers by predicting code snippets based on 
context. Among completion tasks, Method Body Completion (MBC) is particularly challenging as it involves 
generating complete method bodies based on their signatures and context. This task becomes significantly 
harder in large repositories, where method bodies must integrate repository-specific elements such as custom 
APIs, inter-module dependencies, and project-specific conventions. In this paper, we introduce Rambo, a novel 
RAG-based approach for repository-level MBC. Instead of retrieving similar method bodies, Rambo identifies 
essential repository-specific elements, such as classes, methods, and variables/fields, and their relevant usages. 
By incorporating these elements and their relevant usages into the code generation process, Rambo ensures 
more accurate and contextually relevant method bodies. Our experimental results with leading code LLMs 
across 40 Java projects show that Rambo significantly outperformed the state-of-the-art repository-level MBC 
approaches, with the improvements of up to 46% in BLEU, 57% in CodeBLEU, 36% in Compilation Rate, and 
up to 3X in Exact Match. Notably, Rambo surpassed RepoCoder Oracle method by up to 12% in Exact Match, 
setting a new benchmark for repository-level MBC.
1. Introduction
Code completion is a crucial task in software development that 
assists programmers by suggesting the next units of code based on the 
current context [1–5]. Recently, Large Language Models for code (Code 
LLMs) [6–9] such as Codedex, Code Llama, and Deepseek Coder have 
emerged as promising tools for code completion, offering the poten-
tial to automate repetitive tasks and increase developer productivity. 
Several code LLMs have been deployed as auto-completion plugins, 
such as Github Copilot and CodeGeeX2 [10] in modern IDEs, and 
successfully streamline real-world software development activities to a 
certain degree [11–14].
One of the most crucial tasks within code completion is Method 
Body Completion (MBC) which is the process of generating the full
implementation of a method based on its signature and surround-
ing context. MBC is particularly important in reducing the manual 
effort of developers, especially in large-scale projects where method 
implementations are complex and time-consuming. Unlike smaller com-
pletion tasks such as line completion or API invocation, which involve 
completing a single line or predicting an API call, MBC requires gen-
erating entire method bodies that can span multiple lines of code and 
may include several API invocations. These method bodies are often 
∗Corresponding author.
E-mail addresses: 21020006@vnu.edu.vn (T.-D. Bui), 21020476@vnu.edu.vn (T. Luu), 22028108@vnu.edu.vn (T.-P. Nguyen), trang.nguyen@vnu.edu.vn 
(T.-T. Nguyen), hieuvd@vnu.edu.vn (H.D. Vo), sonnguyen@vnu.edu.vn (S. Nguyen).
unique and require a deeper understanding of the method’s intended 
functionality. Moreover, repo(sitory)-level MBC adds another layer of 
complexity as it involves requires not only generating method bodies 
but also integrating repository-specific elements such as user-defined 
APIs, inter-module dependencies, and project-specific code conven-
tions [11,12,15,16]. Despite its difficulty, repo-level MBC remains an 
essential task in software development, playing a crucial role in im-
proving developer productivity and maintaining code quality in large 
projects.
To address the challenges of repo-level code completion, recent 
approaches have applied the Retrieval-Augmented-Generation (RAG) 
strategy. These methods provide repository-specific knowledge to en-
hance the performance of Code LLMs in completing repo-level code [15–
18]. RepoCoder [15] employs a similarity-based retriever in combina-
tion with a Code LLM to form an iterative retrieval-generation pipeline. 
This technique retrieves similar code snippets from the repository 
based on previous code or generated lines, using these examples as 
additional context for code generation. Additionally, RepoHyper [17] 
and RLCoder [18] improve the capability of searching for similar code 
within RepoCoder’s pipeline. However, useful similar code might not 
always exist or be found within the repository for code generation. 
https://doi.org/10.1016/j.infsof.2026.108322
Received 15 May 2025; Received in revised form 28 August 2026; Accepted 31 August 2026
Information and Software Technology 200 (2026) 108322 
Available online 7 September 2026 
0950-5849/© 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

[Vista original de la página 1](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-01.png)

![Página PDF 1, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-01.png)


<!-- PDF page 2 -->

## Página PDF 2

T.-D. Bui et al.
Indeed, Wu et al. [16] report that up to 80% of the standard retrievals 
performed using RepoCoder’s pipeline do not enhance the performance 
of common code LLMs and may degrade performance by introducing 
irrelevant information. This issue could be more severe for the task 
of MBC. Method bodies are typically much more unique than smaller 
completion units such as lines of code (in the Line Completion task) or 
API invocations (in the API Invocation Completion task). Consequently, 
when provided with dissimilar code, code LLMs could be inaccurately 
guided by irrelevant context, leading to the generation of low-quality 
method bodies.
In this paper, we propose Rambo, a novel RAG-based approach 
for Method Body Completion (MBC). Our approach is founded on the 
idea that constructing a method body correctly in a specific repository 
requires accurately using the essential repo-specific code elements.
Instead of retrieving merely similar method bodies as in existing approaches,
Rambo focuses on identifying and retrieving essential repo-specific el-
ements such as declared classes, methods, fields/variables, and their 
usages relevant to the infilling method. These elements serve as the 
‘‘materials’’, and their usages act as the ‘‘recipes’’ for accurately incor-
porating these materials into the generated method body. By providing 
these essential elements and their relevant usages to a code LLM, Rambo
enables the model to generate method bodies that are contextually 
accurate and aligned with the repository’s specific requirements.
To identify the essential code elements needed to complete the 
given infilling method 𝑚 in a repository, a naive solution might scan 
the entire codebase for all accessible elements, which would introduce 
excessive noise. Another approach could focus on methods with similar 
signatures or contexts; however, these often provide irrelevant elements 
that do not serve 𝑚’s functional purpose, leading to redundancy and 
missing critical elements. To address this, Rambo generates a sketch body 
which provides a rough outline of 𝑚. This sketch is analyzed to extract 
the potentially essential code elements. These elements are then used 
to search for similar classes, methods, and fields already declared in 
the repository which are considered as the essential code elements for 
constructing 𝑚’s body. In Rambo, to improve the relevancy of the gener-
ated sketch, it is crucial that the sketch code has similar functionality to 
𝑚. In other words, the sketch should use the parameter set to produce 
a type-correct output with a code structure that generally reflects 𝑚’s 
purpose. To achieve this, we generate the sketch by applying RAG with 
a context that includes methods having a similar signature to 𝑚 in the 
current repository.
After identifying the essential code elements, Rambo searches for all 
the methods in the repository that use these elements. These usages 
are then ranked based on their relevancy to the infilling method 𝑚. In
Rambo, the relevancy of an element’s usage to 𝑚 is estimated by the 
similarity of the usage and 𝑚. Finally, the most relevant usages of the 
identified essential code elements are fed into a code LLM to generate 
𝑚’s body.
We conducted several experiments to evaluate the performance of
Rambo in repo-level method body completion using state-of-the-art code 
LLMs, including DeepSeek Coder [7], Code Llama [6], and GPT-3.5 
Turbo [19]. These experiments were conducted across 40 Java projects 
with a total of 674 repo-level MBC problems. Our results demon-
strate that Rambo significantly surpasses RepoCoder across all evaluated 
code LLMs and metrics. Specifically, Rambo achieves impressive im-
provements over the other MBC approaches in various performance 
metrics, by up to 46% in BLEU, up to 57% in CodeBLEU, up to 36% 
in Compilation Rate, and up to 3X in Exact Match rate. Remarkably,
Rambo delivers up to 12% enhancement in Exact Match rate compared 
to the Oracle RAG-based method [15], which estimates the upper-
bound of performance for RepoCoder and other methods employing the 
same pipeline. This substantial improvement shows Rambo’s superior 
capability in generating high-quality method bodies and sets a new 
benchmark in the task of repository-level method body completion.
The contributions of this paper are listed as follows:
1. Introduction of Rambo: We present Rambo, a novel RAG-based 
approach specifically designed for repository-level method body com-
pletion (MBC), which leverages repo-specific knowledge to enhance 
code LLM performance.
2. Advanced Retrieval Strategy for RAG-based MBC: We intro-
duce a novel retrieval mechanism that identifies and utilizes essen-
tial repo-specific code elements, such as classes, methods, and fields, 
and their relevant usages to construct more accurate and contextually 
relevant contexts for RAG-based method body completion.
3. Comprehensive Evaluation and Benchmarking: We conduct 
extensive experiments with advanced code LLMs, demonstrating that
Rambo significantly outperforms the state-of-the-art RAG-based MBC 
techniques, and establish Rambo as a new benchmark for MBC.
2. Problem statement
Let 𝑅 denote a repository containing multiple source files, where 
each file 𝑓 includes one or more methods. Each method 𝑚 is defined 
by its signature 𝑚𝑠 and surrounding context 𝐶𝑓, consisting of left 
context 𝐶left
𝑓 (preceding the method) and right context 𝐶right
𝑓
 (following 
the method). The objective of repository-level Method Body Completion 
(MBC) is to generate the method body ̂𝑚𝑏 for a given method 𝑚, based 
on its signature 𝑚𝑠, context 𝐶𝑓, and repository-specific information 𝑅, 
formally:̂
𝑚𝑏= arg max
𝐵𝑃(𝐵∣𝑚𝑠, 𝐶𝑓, 𝑅),
where 𝐵 is a candidate method body, and 𝑃(𝐵∣𝑚𝑠, 𝐶𝑓, 𝑅) is the prob-
ability of 𝐵 being the correct completion, given the method signature, 
surrounding context, and repository. The key components include:
• Method Signature (𝑚𝑠) specifies the method’s name, parameters, 
and return type, guiding the overall structure of the body.
• Surrounding Context (𝐶𝑓) provides the surrounding code of-
fering insight into the intended behavior and logic of the given 
method.
• Repository (𝑅) contains project-specific information such as cus-
tom APIs, classes, and dependencies.
The challenge is to generate a method body ̂𝑚𝑏 that is both com-
pilable and functionally accurate, requiring correctly incorporating of 
repository-specific elements. This makes repository-level MBC more 
complex than standard method body completion, which typically fo-
cuses on isolated methods without broader dependencies.
3. Repository-level method body completion with retrieval-aug-
mented generation
Fig. 1 shows the overview of our novel RAG-based approach for 
repo-level MBC, Rambo. In general, for a given infilling method 𝑚 in file 
𝑓 of a specific repository 𝑅, Rambo first retrieves for the relevant repo-
specific context 𝐶𝑅, formally 𝐶𝑅= 𝑟𝑒𝑡𝑟𝑖𝑒𝑣𝑒(𝑚, 𝑅). Then, Rambo leverage 
a code LLM, ℳ, to generates the method body ̂𝑚𝑏 utilizing the retrieved 
relevant context and the surrounding context 𝐶𝑓, ̂𝑚𝑏= ℳ(𝑚, 𝐶𝑓, 𝐶𝑅).
In Rambo, procedure retrieve consists of two main steps, Essential 
Code Element Identification (EEI) and Relevant Usage Extraction (RUE). 
For the given infilling method 𝑚 in repo 𝑅, EEI identifies the repo-
specific essential code elements (e.g., methods, attributes, or types) as 
‘‘materials’’ to form 𝑚’s body (Section 3.1.1). After that, RUE extracts 
these elements’ usages (i.e., the methods using those elements) as 
‘‘recipes’’ of these materials to form the method body and then ranks 
these usages based on the relevancy to 𝑚 (Section 3.1.2). Then, the 
identified essential elements and their relevant usages are utilized to 
construct the context 𝐶𝑅 before feeding 𝐶𝑅 into ℳ to generate method 
body ̂𝑚𝑏.
Information and Software Technology 200 (2026) 108322 
2

[Vista original de la página 2](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-02.png)

![Página PDF 2, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-02.png)


<!-- PDF page 3 -->

## Página PDF 3

T.-D. Bui et al.
Fig. 1. Rambo: A Repository-Level Method Body Completion Approach.
3.1. Repository-specific context retrieval
This section describes the retrieval phase, in Rambo to search for 
the repo-specific context relevant to the given infilling method, 𝐶𝑅=
𝑟𝑒𝑡𝑟𝑖𝑒𝑣𝑒(𝑚, 𝑅). Our retrieval approach consists of two phases, Essential 
Code Element Identification and Relevant Usage Extraction.
3.1.1. Essential Code Element Identification (EEI)
In the Essential Code Element Identification (EEI) phase, the goal 
is to identify the code elements within repo 𝑅 that are crucial for 
constructing the given method, 𝑚. The challenge here is to ensure that 
these repo-specific elements are contextually relevant, meaning they 
should align with the specific needs of the method being completed 
while adhering to the broader repository’s structure and dependencies.
A naive solution might involve scanning the entire codebase to 
identify all accessible code elements from the completion point. This 
could lead to an overwhelming amount of information, much of which 
may be irrelevant, thereby providing much noise to the code generation 
process. Another approach is to search for methods similar to 𝑚’s 
signature 𝑚𝑠 or having a similar surrounding context 𝐶𝑓. The elements 
used in these similar methods could then be extracted as essential 
candidates for constructing 𝑚’s body. However, the methods that are 
similar in the signature or surrounding content may not necessarily 
provide the right elements for 𝑚, especially if they serve different 
functional purposes within the repository. Consequently, the resulting 
set of elements could still contain many redundant or irrelevant items 
while potentially missing key elements that are critical for the correct 
construction of 𝑚’s body.
In the EEI process of Rambo, our idea is to leverage the capabilities 
of code LLMs in understanding and generating code to narrow down 
the set of elements essential for method body construction. Specifically, 
we employ ℳ to generate a sketch body that provides a rough outline 
of the infilling 𝑚. This sketch serves as a preliminary framework for 
understanding the likely structure and components of 𝑚. Based on the 
elements used in this sketch (such as method calls, field accesses, and 
type declarations), Rambo then searches the repository 𝑅 for similar 
elements that have already been declared. In Rambo, these similar 
elements are considered essential for forming 𝑚’s body because they 
align with 𝑅’s structure and the functional needs of 𝑚.
To enhance the relevance of the sketch, Rambo first searches for 
the set of methods, 𝐿, within the repository 𝑅 whose interface (input–
output) and name are most similar to those of 𝑚. The set of methods 𝐿
serves as the reference points for understanding the expected structure 
and functionality of 𝑚. Then, Rambo employs a RAG-based method 
to generate a sketch code  of the method body using the retrieved 
methods 𝐿 and the surrounding context 𝐶𝑓. Although the sketch, 
generated as = ℳ(𝑚, 𝐿, 𝐶𝑓), may not fully accurate,  includes 
Information and Software Technology 200 (2026) 108322 
3

[Vista original de la página 3](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-03.png)

![Página PDF 3, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-03.png)


<!-- PDF page 4 -->

## Página PDF 4

T.-D. Bui et al.
potentially essential elements such as called methods, used fields, and 
types. These elements are then analyzed and extracted:
{𝑚, 𝑓, 𝑡} = analyze()
where 𝑚, 𝑓, and 𝑡 are the sets of called methods, accessed 
fields, and used types in the sketch , respectively. Note that analyzing 
the generated sketch code  by existing code analyzers (e.g., JDT or 
Joern [20]) is feasible because the code generated by pre-trained code 
models, especially code LLMs, is quite syntactically correct [13,21]. 
However, the employed code LLM may hallucinate code, possibly gen-
erate the code elements not existing/declared in the repo, or use them 
inappropriately [13,14].
To mitigate code LLM hallucination, after analyzing, Rambo searches 
for similar code elements already declared within the repository. This 
involves identifying the sets of methods, fields, and classes/types whose 
names are most similar to those found after analyzing : 
𝐸𝑚=
⋃
𝑒∈𝑚
{
arg
max
𝑚′∈med(𝑅)
(name_sim(𝑒, 𝑚′))}
(1)
𝐸𝑓=
⋃
𝑒∈𝑓
{
arg max
𝑣∈fid(𝑅) (name_sim(𝑒, 𝑣))
}
(2)
𝐸𝑡=
⋃
𝑒∈𝑡
{
arg max
𝑐∈cls(𝑅) (name_sim(𝑒, 𝑐))
}
(3)
where 𝐸𝑚, 𝐸𝑓, and 𝐸𝑡 are the sets of accessible methods, fields, and 
classes whose names are most similar to the methods, fields, and types 
in 𝑚, 𝑓, and 𝑡, respectively. Also, the functions med(𝑅) (in 
Formula (1)), fid(𝑅) (in Formula (2)), and cls(𝑅) (in Formula (3)) return 
the sets of all the accessible methods, fields, and classes existing in 𝑅.
3.1.2. Relevant Usage Extraction (RUE)
In the Relevant Usage Extraction (RUE) phase, Rambo focuses on 
extracting the relevant usages of these identified elements. The intu-
ition here is that understanding how these elements are used within 
the repository can provide code LLMs valuable insights into how they 
should be utilized within 𝑚. By analyzing the repository, Rambo identi-
fies methods that make use of these essential elements:
𝑈=
⋃
𝑒∈𝐸𝑚∪𝐸𝑓∪𝐸𝑡
{𝑚′ ∈med(𝑅)|𝑚′ uses 𝑒}
Once these usages are identified, they are ranked based on their rele-
vancy to the functionality of the method 𝑚. The relevancy of a usage 𝑢
is calculated by function rel:
rel(𝑢) ≈sim(𝑢, )
where sim(𝑢, ) calculates the similarity between a usage 𝑢∈𝑈 and the 
sketch  generated during EEI. The reason for this estimation of rel(𝑢)
is that the body of 𝑢 expresses how an essential element 𝑒 is utilized and 
 roughly expresses how potentially essential elements should be used. 
Thus, if the usage of 𝑒 is also present in the sketch code, it indicates that 
the usage of 𝑒 in 𝑢 is likely relevant to 𝑚. This ranking ensures that the 
most relevant usages are prioritized, providing the code LLM with high-
quality context that is both specific to the repository and relevant to 
the task at hand. Additionally, Rambo brings back the set of methods 𝐿
whose signature most closely matches that of 𝑚, serving as a structural 
and functional reference point for method 𝑚. The methods in 𝐿 and the 
top relevant usages are concatenated to form the repo-specific relevant 
context 𝐶𝑅. Finally, this context and the surrounding context 𝐶𝑓 of 𝑚
are fed into ℳ to generate the final method body ̂𝑚𝑏= ℳ(𝑚, 𝐶𝑓, 𝐶𝑅).
Discussion. In the EEI phase of the current Rambo’s version, a
single sketch is generated for each method to identify essential ma-
terial. In fact, multiple sketches could be generated for each method 
to increase the likelihood that the most relevant and diverse code 
elements are identified for method body construction. By generating 
multiple sketches, Rambo can explore various plausible ways in which 
the method 𝑚 could be completed within the repository 𝑅. Each sketch 
provides a different perspective on how the essential elements, such 
as method calls, field usages, and type initialization, can be utilized 
to form the method body. Additionally, this multi-sketch approach 
enhances the robustness of the retrieval process by allowing Rambo to 
capture a broader range of potential code structures and usage patterns 
that may be relevant to 𝑚. This mitigates the risk of missing out on 
critical context that could be overlooked if only a single sketch were 
generated.
However, generating and processing multiple sketches could intro-
duce significant computational overhead, particularly in large reposi-
tories or under time constraints. Moreover, it increases the potential 
for redundancy and noise due to the retrieval process with irrelevant 
elements. Given these trade-offs, the current version of Rambo adopts a 
simpler single-sketch approach.
3.2. Method body generation
In Rambo, the code generation phase synthesizes the method body ̂
𝑚𝑏 for an infilling method 𝑚 using the retrieved context 𝐶𝑅 and 
given surrounding context 𝐶𝑓. This process leverages a large lan-
guage model specialized in code generation, denoted as ℳ, to produce 
repository-specific method bodies that align with the existing codebase. 
Particularly, the method body ̂𝑚𝑏 is generated by passing the method 
𝑚 and context 𝐶 into the code LLM: ̂𝑚𝑏= ℳ(𝑚, 𝐶𝑅, 𝐶𝑓).
To generate 𝑚’s body, we design a prompt template that seamlessly 
integrates the identified relevant context 𝐶𝑅 with the infilling method, 
embedding the context as code comments within the file (as illustrated 
in Fig. 1). The retrieved usages are arranged in ascending order of 
relevancy, with each code snippet annotated by its original file path. 
The number of snippets included in the prompt is optimized based on 
the available prompt length. This approach ensures that the prompt 
is packed with relevant information, facilitating the generation of a 
method body that is both functionally accurate and consistent with the 
repository’s coding standards.
4. Evaluation methodology
To evaluate the repo-level method body completion (MBC) per-
formance of our approach, we seek to answer the following research 
questions:
RQ1: Accuracy and Comparison. How accurate is Rambo in com-
pleting method bodies with the state-of-the-art code LLMs [6,7,19]? 
And how is it compared to the state-of-the-art repo-level MBC ap-
proaches [15]?
RQ2: Intrinsic Analysis. How do different aspects of our approach 
impact the MBC performance of Rambo, including EEI and RUE phases, 
code embedding techniques used to compute similarity between code, 
and code LLM’s size?
RQ3: Sensitivity Analysis. How do various input factors, including 
surrounding context length and repository size, affect Rambo’s perfor-
mance?
RQ4: Execution Time. What is Rambo’s running time?
4.1. Dataset
To evaluates the performance of Rambo and the baselines on repo-
level MBC, we conduct experiments on the MBC benchmarks that 
provide the repo-level context. Specifically, we employ two large Java 
benchmarks: CoderUJB [22] and Rambo’s dataset, and one Python 
benchmark: RepoEval [15]. Table 1 shows an overview of these bench-
marks.
First, we employ the functional code generation benchmark from 
CoderUJB [22], which is constructed from Defects4J [23]. Although 
Defects4J was originally designed for studying software faults and 
testing techniques, it contains real-world projects with extensive test 
suites. These characteristics make it suitable for constructing code 
Information and Software Technology 200 (2026) 108322 
4

[Vista original de la página 4](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-04.png)

![Página PDF 4, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-04.png)


<!-- PDF page 5 -->

## Página PDF 5

T.-D. Bui et al.
Table 1
Datasets statistics.
 
Rambo’s benchmark
CoderUJB
 
 #Repositories
26
14
 
 #Files/repository
[49–4,061]
[11–813]
 
 #Methods/repository
[87–43,601]
[537–25,476] 
 Last update
May 2024
July 2019
 
 #MBC problems
470
204
 
 Body size in LOCs
[3–105]
[5–45]
 
 Body size in code tokens
[25–1,434]
[45–395]
 
 Test availability
NO
YES
 
generation tasks and evaluating the functional correctness of generated 
code. Following CoderUJB [22], we adapt this benchmark to the MBC 
setting by treating the body of a method as the target to be generated 
while keeping its signature and surrounding context. This results in 204 
MBC problems derived from 14 real-world open-source Java projects.
To complement CoderUJB and evaluate repo-level MBC in more 
recent repositories and larger repositories, we further construct a new 
benchmark consisting of active high-quality open-source repositories 
from GitHub. Specifically, we collect 26 Java repositories (other than 
those in Defects4J) that satisfy the following criteria: (1) the repository 
has an open-source license; (2) it has been actively maintained with 
commits in recent years (as of May 2024); (3) it has at least 2000 
GitHub stars to ensure project maturity and code quality, and (4) the 
project can be successfully compiled. From each non-test class in the 
collected projects, we randomly select a method to generate an MBC 
problem and the corresponding reference, which is the method’s body. 
To ensure a reasonable difficulty level of the benchmark, we exclude all 
constructors, getters, setters, and too-short methods with fewer 
than 3 LOCs. As a result, we obtain a total of 470 MBC problems. In this 
work, for every MBC problem, we omitted the import section in the left 
context, 𝐶left
𝑓
, to accurately reflect the coding activities in practice, that 
the necessary imports are usually unavailable before implementing the 
infilling method.
Although there exist other public code generation benchmarks, such 
as ClassEval [24] and ComplexCodeEval [25], we select CoderUJB, 
RAMBO’s benchmark, and RepoEval because their tasks can be natu-
rally formulated following the same repository-level MBC setting con-
sidered in this work. Specifically, each task provides an infilling method 
together with its surrounding code and repository, allowing all evalu-
ated approaches to retrieve repository-specific context and generate the 
complete method body under a consistent experimental protocol.
4.2. Evaluation setup, procedure, and metrics
4.2.1. Empirical procedure
RQ1. Accuracy and Comparison.
Baselines. We compared Rambo against the state-of-the-art repo-
level MBC approaches:
1. In-File Completion [26,27]: The conventional In-File Completion 
(In-File for short) utilizes large code language models for code 
generation in a zero-shot completion manner, conditioned on the 
surrounding context, including both left and right ones.
2. RawRAG: This baseline employs the RAG strategy in its most 
straightforward form by retrieving relevant context solely based 
on the left context using a similarity search. The retrieved snip-
pets are then directly fed into the code LLM for generation 
without further refinement of the retrieved content.
3. RLCoder [18]: RLCoder is a reinforcement learning framework 
that iteratively learns to retrieve high-quality context. In our 
work, RLCoder has been adapted to generate method bodies line 
by line until a complete body is formed.
4. RepoCoder [15]: RepoCoder employs a similarity-based retriever 
and a code LLM in an iterative retrieval-generation pipeline to 
generate complete unfinished code, e.g., unfinished lines, API 
invocations, or function/method bodies.
5. RepoCoder Oracle [15]: This method estimates the upper bound 
of RepoCoder’s performance by utilizing the ground truth code 
to search for relevant context before feeding into code LLMs in 
the RepoCoder. Note that this method performs a single retrieval 
process to obtain relevant code snippets.
6. Rambo Oracle: Inspired by RepoCoder Oracle [15], we estimated 
the upper bound of Rambo’s performance by its own Oracle. 
Within Rambo’s pipeline, this oracle method directly considers 
the ground truth code as the sketch code  in EEI and RUE. In 
this case, the essential elements are correctly identified, and 
their usages are ranked based on the similarities with the ground 
truth.
We used the implementation in their original papers for all the baseline 
approaches. For RepoCoder and RepoCoder Oracle, we used the hyper-
parameters recommended in the original work [15]. Additionally, we 
applied RepoCoder with a single iteration at which RepoCoder achieves 
the best overall performance with our studied dataset. We evaluated 
the MBC performance of the approaches under study using several 
representative code LLMs, both open-source and commercial, including 
DeepSeek Coder 6.7B [7], Code Llama 7B [6], and GPT-3.5 Turbo [19] 
with about 175B parameters. For detailed implementation and other 
hyper-parameters, one can see our website [28]. Note that all experi-
ments were run on a machine with an Intel Xeon Bronze 3104 (6 cores) 
@ 1.70 GHz, 32 GB RAM, and an NVDIA RTX A6000 GPU.
Modern agentic coding assistants, such as Claude Code, Codex, 
and GitHub Copilot, provide an important complementary direction 
for repository-level software engineering. However, these assistants 
operate as end-to-end systems that combine repository exploration, 
planning, tool invocation, execution feedback, and iterative refine-
ment with code generation. Their performance therefore reflects the 
combined effect of these components, making it difficult to attribute im-
provements specifically to repository-context retrieval and generation. 
In contrast, this work focuses on the repository-level MBC setting and 
evaluates the retrieval and generation methodology under a controlled 
protocol consistent with prior MBC studies.
Accordingly, to ensure a fair, controlled, and reproducible compari-
son, we follow established evaluation protocols in prior state-of-the-art 
MBC studies [15,17,18,29,30]. Our evaluation focuses on comparing
Rambo with algorithmic approaches designed for repo-level MBC, in-
cluding In-File Completion, RawRAG, RLCoder and RepoCoder. These 
approaches allow the core retrieval and generation mechanisms to 
be evaluated independently of additional agent-level capabilities, such 
as planning, tool orchestration, and execution-based refinement. This 
controlled evaluation enables us to directly assess the methodological 
contribution of Rambo while avoiding confounding factors introduced 
by end-to-end software engineering agents.
RQ2. Intrinsic Analysis. We conducted several experiments to 
study the impact of Rambo’s components on the MBC performance of
Rambo. We analyzed the impact of the following aspects:
• Retrieval Technique: We evaluated how the retrieval technique 
powered by different embedding methods affects the MBC per-
formance of Rambo.
• EEI and RUE: Contribution Analysis: We examined how EEI and
RUE contribute to the overall repo-level MBC performance of
Rambo.
• Relevant Context Size: We analyzed how changes in the size of the 
relevant context, 𝐶𝑅, influence the MBC performance.
• Code LLM’s Size: We studied the effect of the size of the employed 
code LLM, ℳ, on Rambo’s performance, balancing computational 
efficiency and the quality of the generated method bodies.
Information and Software Technology 200 (2026) 108322 
5

[Vista original de la página 5](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-05.png)

![Página PDF 5, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-05.png)


<!-- PDF page 6 -->

## Página PDF 6

T.-D. Bui et al.
Table 2
Repo-level MBC performance comparison on Rambo’s benchmark.
 Code LLM
BLEU
CodeBLEU
CR
EM 
 
CodeLlama (7B)
Rambo Oracle
41.83
46.22
51.28
14.89 
 
RepoCoder Oracle
46.59
49.53
55.96
14.68 
 
In-File
25.09
33.85
48.09
3.83 
 
RawRAG
41.57
45.96
54.89
12.55 
 
RLCoder
39.92
44.30
54.47
10.85 
 
RepoCoder
42.98
47.66
55.32
12.77 
 
Rambo
43.16
47.76
55.96
13.62 
 
DeepSeek Coder (6.7B)
Rambo Oracle
50.87
53.96
63.40
18.72 
 
RepoCoder Oracle
50.04
52.48
58.51
17.02 
 
In-File
25.99
33.84
45.11
4.04 
 
RawRAG
46.92
50.97
60.21
15.32 
 
RLCoder
45.08
48.58
55.96
14.26 
 
RepoCoder
46.22
50.31
57.23
15.53 
 
Rambo
50.44
53.20
61.70
18.94 
 
GPT3.5 - Turbo (175B)
Rambo Oracle
51.21
53.91
60.85
19.15 
 
RepoCoder Oracle
47.82
51.43
62.13
17.02 
 
In-File
33.93
39.25
53.11
6.38 
 
RawRAG
42.90
45.27
55.53
12.55 
 
RLCoder
45.12
49.48
58.72
15.32 
 
RepoCoder
44.41
49.64
58.09
15.74 
 
Rambo
49.58
52.71
58.94
19.15 
RQ3. Sensitivity Analysis. We investigated how variations in input 
factors affect the performance of Rambo. Specifically, we focused on:
• Surrounding Context Size: We analyzed how changes in the size 
of the left and right contexts influence the MBC performance of
Rambo.
• Repository Size: We examined the impact of repository sizes on
Rambo’s ability to retrieve relevant context and generate method 
bodies.
4.2.2. Metrics
To evaluate the performance of Rambo and other approaches, we 
employed several metrics to assess the quality of the generated bodies 
across various dimensions.
• BLEU [31] is a widely used metric in NLP, assessing the similarity 
between generated and reference text by comparing overlapping
n-grams. In the context of MBC, it measures surface-level sim-
ilarity, focusing on the direct overlap of tokens between the 
generated and reference code.
• CodeBLEU [32] extends the BLEU score by incorporating code-
specific properties, such as syntax and semantic structure. It 
measures the alignment between the generated and the reference 
codes, capturing deeper structural elements.
• Compilation Rate (CR) assesses the percentage of generated 
code bodies that successfully compile without errors. A higher 
compilation rate reflects the syntactical correctness of the gen-
erated code and its adherence to the language’s rules, making it 
a crucial metric for evaluating the practicality of code generation 
models.
• pass@k [33] evaluates the generated code’s ability to pass a set 
of unit tests, measuring the percentage of solutions that pass all 
the given tests when considering the top-k predictions. A higher 
pass@k value indicates stronger model performance in producing 
functionally correct code. In this work, 𝑘= 1 and pass@k is 
applicable for evaluation using Defects4J.
• Exact Match (EM) quantifies the rate at which the generated 
method body exactly matches the actual method body. This met-
ric is akin to string equality checks in many programming lan-
guages, where both case and spacing are considered.
Table 3
Repo-level MBC performance comparison on Defect4J dataset.
 Code LLM
BLEU
CodeBLEU
CR
pass@k
EM 
 
CodeLlama (7B)
Rambo Oracle
54.19
55.90
64.71
46.08
19.12 
 
RepoCoder Oracle
53.69
54.47
64.71
46.57
19.61 
 
In-File
44.06
46.73
55.88
33.82
8.82 
 
RawRAG
48.88
50.93
60.29
45.10
18.01 
 
RLCoder
50.37
51.12
60.29
42.65
17.54 
 
RepoCoder
51.27
53.46
60.78
46.57
20.10 
 
Rambo
52.04
54.98
63.73
44.12
20.59 
 
DeepSeek Coder (6.7B)
Rambo Oracle
51.31
53.54
67.16
49.51
21.57 
 
RepoCoder Oracle
50.74
52.96
64.71
45.59
21.57 
 
In-File
39.18
43.24
52.45
34.80
11.27 
 
RawRAG
44.96
48.47
61.27
45.10
18.01 
 
RLCoder
45.40
48.10
57.84
45.59
18.01 
 
RepoCoder
48.39
51.01
60.78
46.08
20.59 
 
Rambo
51.03
53.05
69.61
46.57
23.04 
 
GPT3.5 - Turbo (175B)
Rambo Oracle
67.80
67.96
76.96
61.76
35.29 
 
RepoCoder Oracle
62.76
64.85
72.06
57.84
31.37 
 
In-File
63.16
65.66
76.96
60.78
26.96 
 
RawRAG
66.09
67.36
75.00
61.27
31.28 
 
RLCoder
65.78
66.67
75.98
61.76
32.84 
 
RepoCoder
63.52
65.39
74.02
59.80
31.86 
 
Rambo
66.29
67.82
76.47
63.73
32.84 
5. Experimental results
5.1. Answering RQ1: Accuracy and comparison
Table 2 and Table 3 present the MBC performance of Rambo com-
pared to the state-of-the-art approaches using several representative 
code LLMs across our proposed benchmark and the Defects4J. As seen,
Rambo exhibits significant improvements over In-File, RawRAG, RL-
Coder [18], RepoCoder [15], and even RepoCoder Oracle. Even when 
compared to its own Oracle (Rambo Oracle), Rambo maintains a highly 
competitive performance. For example, with GPT-3.5 Turbo on Rambo’s 
benchmark, Rambo achieves a significant increase of about 12%–46%
in BLEU and 6%–34% in CodeBLEU compared to those of RepoCoder, 
RLCoder, RawRAG, and In-File. Similarly, on the Defects4J dataset with 
Code Llama, Rambo shows consistent gains, outperforming the other 
approaches by 2%–18% in BLEU and 3%–17% in CodeBLEU. These 
results highlight Rambo’s ability to consistently generate syntactically 
accurate and high-quality code across diverse repositories, outperform-
ing RepoCoder and RLCoder by a substantial margin in both BLEU and 
CodeBLEU metrics. This shows Rambo’s ability to generate syntactically 
and semantically accurate code with fewer errors.
Moreover, Rambo excels in generating method bodies that is compi-
lable and exactly match the reference implementations, as shown by 
its significantly better CR (Compilation Rate) and Exact Match (EM) 
rates. With DeepSeek Coder on Rambo’s benchmark, Rambo’s EM rate 
improves 22% and 3X the corresponding figures of RepoCoder and In-
File, respectively. With the same code LLM, Rambo delivers substantial
CR improvements of 8%–15% compared to RepoCoder in Defects4J. In 
terms of pass@k, Rambo also outperforms with 2/3 studied code LLMs, 
with the improvements of 1%–33%, further affirming its effectiveness 
in generating functionally correct code.
Especially our results indicate that Rambo not only achieves signifi-
cantly better performance compared to RepoCoder but also surpasses 
RepoCoder Oracle, which could represent the upper bound of Re-
poCoder’s potential performance and those of other similarity-based 
approaches. This shows that Rambo is not merely an incremental im-
provement but a substantial advancement in the task of repository-level 
method body completion.
In Tables 2 and 3, repo-level MBC approaches perform substantially 
better on Defect4J than Rambo’s benchmark. This discrepancy can be 
attributed to the greater complexity of Rambo’s benchmarks, which con-
tains larger repositories, longer reference code, and more repo-specific 
Information and Software Technology 200 (2026) 108322 
6

[Vista original de la página 6](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-06.png)

![Página PDF 6, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-06.png)


<!-- PDF page 7 -->

## Página PDF 7

T.-D. Bui et al.
Table 4
Supplementary comparison of repo-level MBC performance with 
GitHub Copilot on 50 repo-level MBC problems.
 
BLEU
Rouge-L
EM
 
 In-File
35.94
41.83
8.00 
 RepoCoder
48.76
51.62
10.00 
 GitHub Copilot
51.77
56.46
10.00 
 RAMBO
53.21
58.22
20.00 
code element invocations (7.2 on average and up to 43), compared with 
Defects4J (4.8 on average and up to 17).
Although coding assistants are not directly comparable to algorith-
mic repo-level MBC approaches under our main controlled evaluation, 
we conduct a small-scale supplementary experiment with GitHub Copi-
lot to provide additional insight into Rambo’s performance in a practical 
coding setting. Due to the interactive nature of Copilot, large-scale 
automated evaluation is non-trivial. We therefore perform this compar-
ison on a representative subset of 50 samples from the Rambo bench-
mark. As shown in Table 4, Rambo achieves an EM rate of 20.00%, ap-
proximately twice that of GitHub Copilot (10.00%). Rambo also achieves 
higher BLEU and ROUGE-L scores of 53.21 and 58.22, respectively, 
compared with 51.77 and 56.46 for GitHub Copilot. These results pro-
vide preliminary evidence that Rambo can perform competitively with a 
practical coding assistant for repo-level MBC. One possible explanation 
is that the repository context available to a general-purpose coding 
assistant is not specifically tailored to the target MBC problem and may 
therefore include less relevant information. In contrast, Rambo explicitly 
identifies potentially essential repository-specific code elements and 
retrieves their relevant usages to construct the generation context. By 
providing more targeted repository context, this retrieval strategy can 
facilitate more accurate method body generation.
  
 
Answer to RQ1: Our results show Rambo’s consistent superiority 
over existing repo-level MBC approaches and its competitive per-
formance compared to Rambo Oracle. Rambo not only outperforms 
existing approaches but also sets a new benchmark by exceeding 
the anticipated upper-bound performance of RepoCoder, showing 
its robustness, accuracy, and practical utility in real-world code 
generation tasks. 
Result Analysis. Upon analyzing the results, we observed that the 
quality of method bodies generated by Rambo is highly dependent on 
the accuracy of the initial sketch code. When the sketch code is poorly 
generated, it fails to narrow down the set of essential code elements 
effectively. This leads to the misidentification of essential elements (in 
EEI) and irrelevant extraction of usages (in RUE), ultimately providing 
the code LLM with inadequate context, resulting in low-quality method 
bodies. A similar issue arises in RepoCoder when the code generated 
in the first iteration is suboptimal; subsequent iterations rarely see 
significant improvements. This problem is particularly pronounced in 
repositories with highly unique and distinct method implementations.
Fig. 2 shows an MBC problem in repository Spring Cloud Gate-
way1 with the infilling method delete simplified in Fig. 2(a). The
delete method in the InMemoryRouteDefinition- Reposi-
tory class removes a RouteDefinition by its ID. It performs a
Route Existence Check by verifying if the route exists in the map. If 
found, the method removes it and returns an empty Mono<Void>
(Success Case). If the route ID is not present, it uses Mono.defer to 
lazily create and return a Mono.error emitting a NotFoundExcep-
tion (Error Handling). In this case, since the other declared methods in 
the repository are quite different from delete, the context provided 
to RepoCoder and its Oracle is insufficient. As shown in Fig. 2(b), the 
1 https://github.com/spring-cloud/spring-cloud-gateway
(a) Simplified MBC problem to fill in the body of
delete
(b) Method body generated by RepoCoder 
and RepoCoder Oracle with DeepSeek 
Coder are identical
(c) Sketch code generated to identify essential code elements 
and their relevant usages by Rambo
(d) A simplified relevant usage of methods error, empty, and flatMap
in Mono
(e) Method body generated by Rambo with DeepSeek 
Coder, which is exactly matched with the reference
Fig. 2. A MBC problem in repository Spring Cloud Gateway.
body generated by RepoCoder and its Oracle completely omits both the
Route Existence Check and Error Handling.
On the other hand, the sketch code generated by Rambo (Fig. 2(c)) 
includes the Route Existence Check and Success Case, but still misin-
terprets the error handling. Based on the sketch, Rambo identifies the 
essential elements and their usages within the repository. One relevant 
usage is the save method in the RedisRouteDefinitionRepos-
itory class (Fig. 2(d)). With this relevant usage as a reference where
Mono.error is used as expected (lines 8–9 in save), Rambo and the 
code LLM correctly generate the expected body for this MBC problem, 
as shown in Fig. 2(e).
Fig. 3 shows Rambo’s performance across different reference sizes 
(LOC). As expected, Rambo performs much better with smaller code 
snippets (1–50 LOC), achieving high CodeBLEU, CR, and EM. However,
Rambo’s performance declines gracefully as the reference size increases, 
Information and Software Technology 200 (2026) 108322 
7

[Vista original de la página 7](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-07.png)

![Página PDF 7, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-07.png)


<!-- PDF page 8 -->

## Página PDF 8

T.-D. Bui et al.
Fig. 3. Rambo’s performance by references’ size (LOC), left axis: CodeBLEU and
CR; right axis: Distribution.
Table 5
Performance of Rambo by Retrieval Techniques.
 
CodeBLEU
CR
EM
 
 Lexical Retrieval
53.20
61.70
18.94 
 Semantic Retrieval
52.61
61.49
18.09 
 Hybrid Retrieval
53.47
62.98
18.51 
particularly for larger codebases (201+ LOC). This trend also appears 
in the results of the other approaches [28]. This decline can be at-
tributed to the increased complexity and dependencies within larger 
code, which challenge Rambo’s ability to maintain its accuracy. These 
findings suggest that while Rambo is highly effective for smaller tasks, 
improvements are needed to enhance its scalability and performance 
on larger, more complex codebases.
5.2. Answering RQ2: Intrinsic analysis
To answer RQ2, we performed the experiments on Rambo’s bench-
mark with the state-of-the-art LLM specialized for code, DeepSeek 
Coder and its variants [7] as ℳ.
5.2.1. Impact of retrieval technique
To investigate the impact of the retrieval technique on Rambo’s 
performance, we applied several popular retrieval techniques used to 
gather relevant context from the repository in Rambo: Lexical Retrieval 
using Byte-Pair Encoding (BPE) [34] with Jaccard similarity, Semantic 
Retrieval powered by UniXCoder embeddings [35] with Cosine similar-
ity, and a Hybrid approach that averages the similarity scores by Lexical 
Retrieval and Semantic Retrieval.
Table 5 compares the performance of Rambo across three different 
retrieval methods. As seen, the performance of Rambo is slightly im-
pacted by the retrieval techniques with the relative margins of 1.6% in 
CodeBLEU, 2.4% in CR, and 4.8% in EM. Although Semantic Retrieval 
offers broader contextual insights, its performance slightly lags behind 
the other techniques. The reason could be that Rambo primarily relies 
on identifying functionally similar methods and code elements by 
comparing method signatures and element names, where deep semantic 
understanding may not be as critical. The Hybrid approach, which 
combines both lexical and semantic methods, marginally outperforms 
the individual approaches but introduces additional complexity. Given 
the small performance gains, this added complexity may not be justified 
compared to the efficiency of lexical retrieval. Indeed, Lexical retrieval, 
which focuses on token-level similarity, stands out for its balance of 
performance and efficiency. Its lightweight design allows for fast and 
accurate retrieval of relevant code snippets, making it particularly 
effective for Rambo’s MBC tasks.
Table 6
Contributions of EEI and RUE on Rambo’s performance.
 Variant
CodeBLEU
CR
EM
 
 Sketch generation
49.75
61.06
14.04 
 Essential elements only
41.10
61.49
13.40 
 Rambo
53.20
61.70
18.94 
5.2.2. EEI and RUE: Contribution analysis
To evaluate the impact of Essential Code Element Identification (EEI)
and Relevant Usage Extraction (RUE) on Rambo’s overall performance, we 
built two variants of Rambo. The first one contains only the component 
of Sketch generation serving as a baseline for evaluating performance 
without the additional contextual information provided by EEI or RUE. 
The second variant, Essential (code) elements only, analyzes the sketch 
code to identify most similar elements in the repository and uses their 
signatures as well as their bodies as the context for code generation by 
ℳ.
Table 6 shows the performance of these two variants compared to
Rambo. The Sketch generation component serves as a baseline, achieving 
a CodeBLEU of 49.75, a CR of 61.06, and an EM score of 14.04. 
Interestingly, the performance of the Essential elements only variant is 
lower than the sketch-only approach. Although the essential elements 
and their bodies are included as context, the performance decrease 
suggests that introducing them without proper usage context (as in 
RUE) may mislead the model. The retrieval of functionally similar code 
elements alone is insufficient without understanding their specific role 
in the repository, leading to less accurate code generation.
When EEI and RUE are combined in Rambo, the LLM achieves the 
highest performance. The integration of EEI allows Rambo to identify es-
sential elements relevant to the method, while RUE provides context for 
how these elements are used within the repository. This combination 
ensures that the code LLM receives both relevant code elements and 
usage patterns, improving its ability to generate functionally correct 
and syntactically accurate method bodies.
5.2.3. Impact of number of sketches
To study the impact of sketch generation on Rambo’s performance, 
we varied the number of generated sketches in Sketch Generation of
Rambo on Defects4J with DeepSeek Coder as the code LLM. When using 
a single sketch, Rambo achieves a BLEU score of 51.03, an ES of 53.05, 
and an EM rate of 23.06. Increasing the number of sketches to five
results in lower scores, e.g., BLEU of 49.43, CodeBLEU of 51.12, and EM 
of 21.57 in the case of generating 5 sketches. In our experiments, we 
found that the sketches generated are not substantially different from 
one another. Additionally, the sketches may even introduce irrelevant 
elements that slightly degrade performance. Consequently, using a 
single sketch is sufficient for effectively identifying the essential code 
elements for method body completion.
5.2.4. Impact of relevant context’s size
Fig. 4 shows the performance of Rambo as the size of the relevant 
context, 𝐶𝑅, increases, measured by the number of relevant methods 
included. The performance of Rambo improves consistently as more 
relevant context is incorporated, yielding gains of 59% in CodeBLEU, 
37% in Compilation Rate, and a 5X increase in Exact Match when 
the context size increases from 0 to 20 relevant methods. The most 
substantial improvement occurs when the context size grows from 
0 to 5 methods. Beyond this point, further increasing 𝐶𝑅 results in 
diminishing returns. This suggests that Rambo can effectively extract 
essential information with a relatively small set of relevant methods, 
while additional context provides only marginal benefits.
Furthermore, the case where 𝐶𝑅 is empty (i.e., containing 0 meth-
ods) corresponds to a setting where no repository-level context is 
retrieved, and the model relies solely on the method signature and its 
Information and Software Technology 200 (2026) 108322 
8

[Vista original de la página 8](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-08.png)

![Página PDF 8, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-08.png)


<!-- PDF page 9 -->

## Página PDF 9

T.-D. Bui et al.
Fig. 4. Rambo’s performance by the size of relevant context, 𝐶𝑅 (in the number 
of methods included in 𝐶𝑅).
surrounding context. This scenario approximates a cold-start situation 
in which the underlying repository contains little or no existing code 
to support retrieval. As shown in Fig. 4, although the performance 
decreases in this setting, Rambo can still capture useful information from 
the surrounding context, achieving a CodeBLEU score of 33.46 and a 
compilation rate of 45.11. These results suggest that the system remains 
capable of producing reasonable outputs even without repository-level 
context. However, incorporating relevant retrieved context plays an 
important role in improving generation quality.
5.2.5. Impact of code LLM’s size
To assess how the size of the Code LLM, ℳ, influences Rambo’s 
performance, we conducted experiments using two different model 
sizes. However, our experiments were performed with DeepSeek Coder 
models of 1.3B and 6.7B parameters due to resource limitations. As 
shown in Fig. 5, the larger 6.7B model significantly improves Rambo’s 
performance, particularly in CodeBLEU and EM, indicating that a larger 
model size is advantageous for achieving higher accuracy in repository-
level method body completion tasks. However, this comes at a cost: 
code generation time, with the 6.7B model, is 60% longer compared 
to Rambo with the 1.3B model, highlighting the trade-off between 
performance and computational efficiency.
  
 
Answer to RQ2: Rambo’s performance improves with relevant 
context and larger Code LLMs. Lexical retrieval provides the 
best trade-off between performance and efficiency. Performance 
gains diminish with excessive relevant context and larger models 
increase accuracy but slow down generation. Generating multiple 
sketches does not significantly enrich the set of essential code el-
ements, instead, it may introduce redundancy, leading to reduced 
performance. 
5.3. Answering RQ3: Sensitivity analysis
To answer RQ3, we used Rambo with Lexical Retrieval and DeepSeek 
Coder 6.7B on Rambo’s benchmark.
5.3.1. Impact of surrounding context size
Fig. 6 illustrates how Rambo’s performance varies with different sizes 
of the surrounding context, from 10–100 LOCs. In this experiment, the 
surrounding context is structured symmetrically, with the left context 
and the right context being of identical size. In general, there is an 
improvement across all metrics in the performance of Rambo when 
additional surrounding context is provided. Particularly, when the 
surrounding context size increases from 10–20 LOCs on both sides,
Fig. 5. Rambo’s performance by the sizes of ℳ (DeepSeek Coder).
Fig. 6. Rambo’s performance by surrounding context, 𝐶𝑓 in different sizes 
(LOCs).
Rambo’s performance significantly improves, 12% in CodeBLEU, 16% in 
CR, and 33% in EM. As the context size increases further (20–50 LOCs), 
the improvements remain steady but moderate. From 50–100 LOCs, the 
improvement trend slows down. Beyond 100 LOCs, a plateau effect 
becomes apparent. This shows that additional surrounding context 
might introduce redundancy or irrelevant information, which does not 
contribute meaningfully to generating high-quality method bodies.
Overall, these results demonstrate the importance of balancing sur-
rounding context size in Rambo. For practical applications, one should 
limit the surrounding context to around 50 LOCs, as larger contexts 
yield only marginal improvements in Rambo’s performance while adding 
complexity and potential noise to the generation process.
5.3.2. Impact of repository size
Fig. 7 illustrates Rambo’s performance across repositories of different 
sizes. Rambo performs optimally on smaller repositories (20 out of 
26 repositories with fewer than 800 files). On average, it achieves a 
CodeBLEU score of 54.5, a Compilation Rate (CR) of 64%, and an 
Exact Match (EM) rate of 21.1%. However, performance declines across 
all metrics as repository size increases. In particular, for very large 
repositories containing more than 2000 files, CodeBLEU drops to 49.23, 
and EM decreases to 13.95%.
This trend can be attributed to the enlarged retrieval search space in 
larger repositories. Through manual inspection of several large projects, 
we observed that these repositories often contain multiple relatively in-
dependent modules. Although such repositories provide a richer knowl-
edge base, they also substantially increase the number of candidate 
code elements and usages retrieved during the EEI and RUE phases. 
Information and Software Technology 200 (2026) 108322 
9

[Vista original de la página 9](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-09.png)

![Página PDF 9, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-09.png)


<!-- PDF page 10 -->

## Página PDF 10

T.-D. Bui et al.
Fig. 7. Rambo’s performance by repository sizes (files).
Table 7
Repo-level MBC performance Rambo and the others on RepoE-
val dataset (Python).
 
BLEU
CodeBLEU
Pass@1
EM
 
 Rambo Oracle
56.09
52.58
46.33
20.11 
 RepoCoder Oracle
52.71
48.91
40.47
15.28 
 Infile
35.82
34.22
24.63
5.90 
 RawRAG
48.21
44.73
36.66
14.21 
 RLCoder
52.79
50.38
43.70
18.23 
 RepoCoder
51.08
48.10
40.18
16.89 
 Rambo
55.78
52.39
46.92
20.11 
As a result, some retrieved candidates may originate from modules 
that are unrelated to the target method. This introduces noise into the 
retrieved context and negatively affects the code generation process. 
These findings suggest that maintaining retrieval precision in large 
multi-module repositories requires restricting the retrieval scope to 
modules that are structurally or semantically related to the target 
method.
5.3.3. Impact of programming languages
Table 7 shows the performance of Rambo with Code Llama on 
RepoEval which is a Python benchmark proposed simultaneously with 
RepoCoder [15]. The results on this Python benchmark indicate that
Rambo maintains significant improvements of 19%–240% in EM and up 
to 90% in Pass@1 over the existing approaches, even their upper-bound 
performance. These demonstrate Rambo’s ability to generate accurate 
and contextually relevant method bodies regardless of language. These 
findings affirm that the strategies employed by Rambo, particularly the 
identification of essential code elements and relevant usage extrac-
tion, are robust and effectively generalize across diverse programming 
environments.
  
 
Answer to RQ3: Rambo performs best with balanced surround-
ing context (𝐶𝑓) and excels in smaller repositories. Performance 
declines in larger repositories due to increased complexity and 
generation times. Additionally, our experiments on both Java and 
Python demonstrate that Rambo’s approach generalizes effectively 
across programming languages. 
5.4. Answering RQ4: Execution time
The execution time of Rambo consists of two stages: preparation and 
inference.
During the preparation stage, Rambo parses the entire repository and 
extracts code elements required for retrieval. This step is performed
once per repository and can be executed offline, so it does not need to 
be repeated for subsequent generation requests. In our experiments, this 
preprocessing stage takes approximately 8 min per repository.
When a generation request is received, the inference stage begins. 
First, the LLM generates a sketch of the target method, which takes 
about 7 s. Next, the EEI and RUE phases retrieve the top-k functionality-
similar elements and relevant usages, requiring approximately 0.9 s. 
Finally, the LLM generates the complete method body based on the 
retrieved context, which takes about 10 s. Overall, for each request, 
the inference stage, including sketch generation, context retrieval, and 
method body generation, takes approximately 18 s on average.
5.5. Threats to validity
The main threats to the validity of our work consist of internal, 
construct, and external threats.
Threats to internal validity include the hyperparameter settings 
of the baseline methods and Rambo. To mitigate this threat, we sys-
tematically varied the settings of Rambo and thoroughly examined its 
performance (as discussed in Section 5). Additionally, we reused the 
implementations and settings from the original papers of the baseline 
approaches [15] to ensure consistency in comparison. Another poten-
tial threat arises from the methods used to analyze generated sketch 
code and identify essential elements within the repository. To address 
this, we employed a robust code analyzer [20] and popular retrieval 
mechanisms applied by existing studies [15–17], ensuring our approach 
aligned with established practices. Furthermore, to minimize the threat 
of implementation errors, we conducted a detailed review of our code 
and have made it publicly available [28] to facilitate replication and 
validation by other researchers.
Threats to construct validity relate to the appropriateness of our 
evaluation procedure. We utilized widely accepted metrics for both 
text-based and code-based evaluations, including BLEU, CodeBLEU, Ex-
act Match, Compilation Rate, and pass@k, which are standard measures 
in code completion and code generation research. A potential threat 
remains due to the absence of a human evaluation, which could provide 
a more nuanced assessment of our approach. To address this limitation, 
we plan to incorporate human evaluations in future work, wherein 
experienced developers will assess the generated method bodies based 
on criteria such as functionality, accuracy, and adherence to reposi-
tory standards. Additionally, the controlled environments used in our 
experiments may not fully represent real-world scenarios. To miti-
gate this, we conducted evaluations in diverse settings and examined 
performance across multiple scenarios and configurations.
Threats to external validity primarily concern the generalizability 
of our results to different repositories, programming languages, and 
development environments. To reduce this threat, we selected repre-
sentative code LLMs models and repositories widely recognized in both 
NLP and SE communities [6,7,19]. Another potential threat arises from 
the programming languages and repositories used in our experiments. 
Our evaluation was conducted on Java and Python repositories. Java 
repositories are emphasized because they typically provide mature 
ecosystems and standardized build systems, which facilitate reliable 
evaluation of repo-level MBC. Meanwhile, Python is widely used in 
code generation benchmarks and prior studies on code LLMs [15,18,
33,36,37], making it a representative language for evaluating LLM-
based code generation approaches. Although Rambo is designed to 
be language-agnostic, our experiments are currently limited to Java 
and Python. While these languages cover two widely used program-
ming ecosystems, the findings may not necessarily generalize to other 
programming languages. In future work, we plan to extend our eval-
uation to a broader range of repositories and additional programming 
languages to further assess the generalizability of our approach.
A potential threat to external validity arises from possible memo-
rization effects in LLMs. Since code LLMs are typically pre-trained on 
large-scale public code corpora, it is possible that some repositories 
Information and Software Technology 200 (2026) 108322 
10

[Vista original de la página 10](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-10.png)

![Página PDF 10, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-10.png)


<!-- PDF page 11 -->

## Página PDF 11

T.-D. Bui et al.
or code fragments appearing in our benchmarks were included in the 
training data of the evaluated models. In such cases, the models might 
rely on memorized patterns rather than reasoning over the provided 
repository context. To mitigate this threat, we construct our benchmark 
using relatively recent open-source repositories that are less likely 
to appear in earlier training corpora. In addition, we evaluate the 
approaches using multiple backbone LLMs to reduce the likelihood that 
the observed results are specific to a single model or training dataset.
6. Related work
Rambo is closely related to the research on repository-level code 
completion, which utilizes the broader context provided by an entire 
code repository [15–18,38–41]. RepoPrompts [41] introduces an ap-
proach that first generates prompts reflecting the repository’s structure 
and predefined relevant contexts, then learns to select the prompt most 
likely to produce the desired output. In the work by Wang et al. [18], 
the task of retrieving useful context is framed as a reinforcement learn-
ing problem, where the retriever parameters are iteratively updated. 
MGD [38] monitors the code generated by LLMs, queries static analysis 
tools in the background, and leverages the resulting information to 
guide the LLMs during the decoding stage. RepoCoder [15] integrates 
a similarity-based retriever and a code LLM into an iterative retrieval-
generation pipeline. RepoHyper [17] improves the context retrieval 
quality over the prior work by introducing a hypergraph-based re-
triever that learns to model cross-file dependencies. While RepoHyper 
demonstrates strong performance in selecting informative context for 
code generation, it operates under the assumption that the necessary 
imported files are already present in the file being completed. Further-
more, RepoHyper requires a training phase for re-ranking and selecting 
suitable retrieved contexts, which may limit its applicability in dynamic 
or unseen repositories.
Although these efforts show promising performance, Rambo differs 
from them in that Rambo requires neither training nor modifications to 
the underlying code LLMs. To further improve its practical usability,
Rambo makes no assumptions about the existence of imported files 
in the current file. Additionally, instead of similarity-based retrieval,
Rambo emphasizes the extraction of code elements most relevant to the 
infilling method and their usage contexts. This design ensures that the 
generated method bodies are not only contextually accurate but also 
aligned with the repository’s specific coding practices.
Code completion is a critical feature in modern Integrated Devel-
opment Environments (IDEs) and has garnered significant interest from 
researchers [2–4,11,37,42–49]. Earlier approaches [42,50,51] relied on 
rule-based techniques or code example patterns for completing code. 
In recent years, learning-based approaches have been developed to 
enhance code completion performance [1–5,43–46]. The advent of 
large language models (LLMs) has further advanced this field, leading 
to their integration into code completion and generation tasks [11,37,
47–49]. For instance, ReACC [11], a retrieval-augmented code comple-
tion framework inspired by coding practices, enhances code generation 
by incorporating lexical copying and semantic retrieval, followed by 
generation through a decoder-only transformer model. ReCode [49] 
advances neural code generation by integrating subtree retrieval from 
existing code examples. DocPrompting [47] improves code generation 
by leveraging code documentation, effectively addressing challenges in 
generating code for unfamiliar functions and libraries. Zhang et al. [37] 
propose kNN-TRANX that improves code generation by leveraging 
syntax constraints for retrieval, reducing noise and computational time.
Recently, several learning-based approaches have been proposed 
for specific Software Engineering tasks such as code translation/mig-
ration [52–56], text-code translation [57–61], test generation [62,
63], bug detection [64–67], bug fix identification [68], and program 
repair [69,70].
7. Conclusion
In this paper, we introduced Rambo, a novel Retrieval-Augmented 
Generation (RAG)-based approach designed specifically for repository-
level method body completion (MBC). Our approach centers on the 
accurate identification and utilization of essential repo-specific code 
elements, significantly enhancing the performance of code LLMs in 
generating contextually relevant and syntactically correct method bod-
ies. Our experimental results show Rambo’s superiority across all key 
metrics, including BLEU, CodeBLEU, Compilation Rate, pass@𝑘, and
Exact Match. Notably, Rambo not only surpassed existing methods but 
also exceeded the performance of RepoCoder Oracle, setting a new 
benchmark in the field. These show Rambo’s robustness, accuracy, and 
practical utility in real-world code generation tasks. By leveraging 
essential code elements and relevant usages, Rambo addresses the limita-
tions of existing similarity-based approaches, providing a more precise 
and reliable solution for MBC in complex repositories.
CRediT authorship contribution statement
Tuan-Dung Bui: Validation, Software, Investigation, Data cura-
tion, Conceptualization. Thieu Luu: Validation, Software, Investiga-
tion, Data curation, Conceptualization. Thanh-Phat Nguyen: Valida-
tion, Software, Methodology, Data curation. Thu-Trang Nguyen: Writ-
ing – review & editing, Writing – original draft, Visualization, Software, 
Methodology, Conceptualization. Hieu Dinh Vo: Writing – review 
& editing, Supervision, Project administration, Funding acquisition, 
Conceptualization. Son Nguyen: Writing – review & editing, Writing 
– original draft, Visualization, Validation, Supervision, Methodology, 
Investigation, Formal analysis, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to 
influence the work reported in this paper.
Acknowledgments
This research is funded by Vietnam National University, Hanoi 
(VNU) under project number QG.24.37. Son Nguyen was funded by the 
Postdoctoral Scholarship Programme of Vingroup Innovation Founda-
tion (VINIF), code VINIF.2025.STS.13.
Data availability
Data will be made available on request.
References
[1] A. Hindle, E.T. Barr, M. Gabel, Z. Su, P. Devanbu, On the naturalness of software, 
Commun. ACM 59 (5) (2016) 122–131.
[2] R.-M. Karampatsis, H. Babii, R. Robbes, C. Sutton, A. Janes, Big code!=big 
vocabulary: Open-vocabulary models for source code, in: 2020 IEEE/ACM 
42nd International Conference on Software Engineering, ICSE, IEEE, 2020, pp. 
1073–1085.
[3] S. Nguyen, T. Nguyen, Y. Li, S. Wang, Combining program analysis and statistical 
language model for code statement completion, in: 2019 34th IEEE/ACM 
International Conference on Automated Software Engineering, ASE, IEEE, 2019, 
pp. 710–721.
[4] S. Nguyen, C.T. Manh, K.T. Tran, T.M. Nguyen, T.-T. Nguyen, K.-T. Ngo, H.D. 
Vo, Arist: An effective API argument recommendation approach, J. Syst. Softw. 
(2023) 111786.
[5] Z. Tu, Z. Su, P. Devanbu, On the localness of software, in: Proceedings of 
the 22nd ACM SIGSOFT International Symposium on Foundations of Software 
Engineering, 2014, pp. 269–280.
[6] B. Roziere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X.E. Tan, Y. Adi, J. Liu, 
T. Remez, J. Rapin, et al., Code llama: Open foundation models for code, 2023, 
arXiv preprint arXiv:2308.12950.
Information and Software Technology 200 (2026) 108322 
11

[Vista original de la página 11](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-11.png)

![Página PDF 11, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-11.png)


<!-- PDF page 12 -->

## Página PDF 12

T.-D. Bui et al.
[7] DeepSeek, DeepSeek coder: Let the code write itself, 2023, https://github.com/
deepseek-ai/DeepSeek-Coder.
[8] D. Fried, A. Aghajanyan, J. Lin, S. Wang, E. Wallace, F. Shi, R. Zhong, W.-t. 
Yih, L. Zettlemoyer, M. Lewis, Incoder: A generative model for code infilling 
and synthesis, 2022, arXiv preprint arXiv:2204.05999.
[9] A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, S. Yoo, J.M. Zhang, 
Large language models for software engineering: Survey and open problems, in: 
2023 IEEE/ACM International Conference on Software Engineering: Future of 
Software Engineering, ICSE-FoSE, IEEE, 2023, pp. 31–53.
[10] Q. Zheng, X. Xia, X. Zou, Y. Dong, S. Wang, Y. Xue, Z. Wang, L. Shen, A. Wang, 
Y. Li, T. Su, Z. Yang, J. Tang, CodeGeeX: A pre-trained model for code generation 
with multilingual benchmarking on HumanEval-X, in: Proceedings of the 29th 
ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2023, pp. 
5673–5684.
[11] S. Lu, N. Duan, H. Han, D. Guo, S.-w. Hwang, A. Svyatkovskiy, ReACC: A 
retrieval-augmented code completion framework, in: Proceedings of the 60th 
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long 
Papers), 2022, pp. 6227–6240.
[12] Z. Tang, J. Ge, S. Liu, T. Zhu, T. Xu, L. Huang, B. Luo, Domain adaptive code 
completion via language models and decoupled domain databases, in: 2023 38th 
IEEE/ACM International Conference on Automated Software Engineering, ASE, 
IEEE, 2023, pp. 421–433.
[13] T.-T. Nguyen, T.T. Vu, H.D. Vo, S. Nguyen, An empirical study on capability 
of large language models in understanding code semantics, Inf. Softw. Technol. 
185 (2025) 107780.
[14] F. Tambon, A. Moradi-Dakhel, A. Nikanjam, F. Khomh, M.C. Desmarais, G. 
Antoniol, Bugs in large language models generated code: An empirical study, 
Empir. Softw. Eng. 30 (3) (2025) 65.
[15] F. Zhang, B. Chen, Y. Zhang, J. Keung, J. Liu, D. Zan, Y. Mao, J.-G. Lou, W. 
Chen, RepoCoder: Repository-level code completion through iterative retrieval 
and generation, in: Proceedings of the 2023 Conference on Empirical Methods 
in Natural Language Processing, 2023, pp. 2471–2484.
[16] D. Wu, W.U. Ahmad, D. Zhang, M.K. Ramanathan, X. Ma, Repoformer: Selec-
tive retrieval for repository-level code completion, in: Forty-First International 
Conference on Machine Learning.
[17] H.N. Phan, H.N. Phan, T.N. Nguyen, N.D. Bui, Repohyper: Search-expand-
refine on semantic graphs for repository-level code completion, in: 2025 
IEEE/ACM Second International Conference on AI Foundation Models and 
Software Engineering, Forge, IEEE, 2025, pp. 14–25.
[18] Y. Wang, Y. Wang, D. Guo, J. Chen, R. Zhang, Y. Ma, Z. Zheng, Rlcoder: 
Reinforcement learning for repository-level code completion, in: 2025 IEEE/ACM 
47th International Conference on Software Engineering, ICSE, IEEE, 2025, pp. 
1140–1152.
[19] OpenAI, GPT-3.5 turbo, 2024, https://platform.openai.com/docs/models/gpt-3-
5-turbo. (Accessed September 2024).
[20] F. Yamaguchi, N. Golde, D. Arp, K. Rieck, Modeling and discovering vulnera-
bilities with code property graphs, in: 2014 IEEE Symposium on Security and 
Privacy, IEEE, 2014, pp. 590–604.
[21] Y. Wan, W. Zhao, H. Zhang, Y. Sui, G. Xu, H. Jin, What do they capture? a 
structural analysis of pre-trained language models for source code, in: Proceed-
ings of the 44th International Conference on Software Engineering, 2022, pp. 
2377–2388.
[22] Z. Zeng, Y. Wang, R. Xie, W. Ye, S. Zhang, CoderUJB: An executable and unified 
java benchmark for practical programming scenarios, in: Proceedings of the 
33rd ACM SIGSOFT International Symposium on Software Testing and Analysis, 
Association for Computing Machinery, New York, NY, USA, 2024.
[23] R. Just, D. Jalali, M.D. Ernst, Defects4J: A database of existing faults to 
enable controlled testing studies for java programs, in: Proceedings of the 2014 
International Symposium on Software Testing and Analysis, 2014, pp. 437–440.
[24] X. Du, M. Liu, K. Wang, H. Wang, J. Liu, Y. Chen, J. Feng, C. Sha, X. Peng, Y. 
Lou, Classeval: A manually-crafted benchmark for evaluating llms on class-level 
code generation, 2023, arXiv preprint arXiv:2308.01861.
[25] J. Feng, J. Liu, C. Gao, C.Y. Chong, C. Wang, S. Gao, X. Xia, Complexcodeeval: 
A benchmark for evaluating large code models on more complex code, in: 
Proceedings of the 39th IEEE/ACM International Conference on Automated 
Software Engineering, 2024, pp. 1895–1906.
[26] E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang, Y. Zhou, S. Savarese, 
C. Xiong, CodeGen: An open large language model for code with multi-
turn program synthesis, in: The Eleventh International Conference on Learning 
Representations.
[27] B. Chen, F. Zhang, A. Nguyen, D. Zan, Z. Lin, J.-G. Lou, W. Chen, Codet: Code 
generation with generated tests, in: The Eleventh International Conference on 
Learning Representations.
[28] RAMBO. URL https://github.com/iSE-UET-VNU/RAMBO.
[29] T. Jiang, Y. Wang, Y. Wang, D. Guo, E. Shi, Y. Ma, J. Chen, Z. Zheng, 
AlignCoder: Aligning retrieval with target intent for repository-level code comple-
tion, in: 2025 40th IEEE/ACM International Conference on Automated Software 
Engineering, ASE, IEEE, 2025, pp. 971–982.
[30] Y. Peng, J. Wan, Y. Li, X. Ren, Coffe: A code efficiency benchmark for code 
generation, Proc. ACM Softw. Eng. 2 (FSE) (2025) 242–265.
[31] K. Papineni, S. Roukos, T. Ward, W.-J. Zhu, Bleu: a method for automatic 
evaluation of machine translation, in: Proceedings of the 40th Annual Meeting 
of the Association for Computational Linguistics, 2002, pp. 311–318.
[32] S. Ren, D. Guo, S. Lu, L. Zhou, S. Liu, D. Tang, N. Sundaresan, M. Zhou, A. 
Blanco, S. Ma, Codebleu: a method for automatic evaluation of code synthesis, 
2020, arXiv preprint arXiv:2009.10297.
[33] M. Chen, J. Tworek, H. Jun, Q. Yuan, H.P.d. Pinto, J. Kaplan, H. Edwards, Y. 
Burda, N. Joseph, G. Brockman, et al., Evaluating large language models trained 
on code, 2021, arXiv preprint arXiv:2107.03374.
[34] R. Sennrich, B. Haddow, A. Birch, Neural machine translation of rare words with 
subword units, in: Proceedings of the 54th Annual Meeting of the Association 
for Computational Linguistics, Association for Computational Linguistics, Berlin, 
Germany, 2016, pp. 1715–1725.
[35] D. Guo, S. Lu, N. Duan, Y. Wang, M. Zhou, J. Yin, UniXcoder: Unified cross-modal 
pre-training for code representation, in: Proceedings of the 60th Annual Meeting 
of the Association for Computational Linguistics (Volume 1: Long Papers), 2022, 
pp. 7212–7225.
[36] J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, 
C. Cai, M. Terry, Q. Le, et al., Program synthesis with large language models, 
2021, arXiv preprint arXiv:2108.07732.
[37] X. Zhang, Y. Zhou, G. Yang, T. Chen, Syntax-aware retrieval augmented code 
generation, in: Findings of the Association for Computational Linguistics: EMNLP 
2023, 2023, pp. 1291–1302.
[38] L.A. Agrawal, A. Kanade, N. Goyal, S. Lahiri, S. Rajamani, Monitor-guided 
decoding of code LMs with static analysis of repository context, Adv. Neural 
Inf. Process. Syst. 36 (2024).
[39] Y. Ding, Z. Wang, W.U. Ahmad, M.K. Ramanathan, R. Nallapati, P. Bhatia, 
D. Roth, B. Xiang, CoCoMIC: Code completion by jointly modeling in-file and 
cross-file context, in: Proceedings of the 2024 Joint International Conference on 
Computational Linguistics, Language Resources and Evaluation, LREC-COLING 
2024, 2024, pp. 3433–3445.
[40] R. Bairi, A. Sonwane, A. Kanade, A. Iyer, S. Parthasarathy, S. Rajamani, B. Ashok, 
S. Shet, Codeplan: Repository-level coding using llms and planning, Proc. ACM 
Softw. Eng. 1 (FSE) (2024) 675–698.
[41] D. Shrivastava, H. Larochelle, D. Tarlow, Repository-level prompt generation for 
large language models of code, in: International Conference on Machine Learning, 
PMLR, 2023, pp. 31693–31715.
[42] R. Robbes, M. Lanza, How program history can improve code completion, 
in: 2008 23rd IEEE/ACM International Conference on Automated Software 
Engineering, IEEE, 2008, pp. 317–326.
[43] W. Zhou, S. Kim, V. Murali, G.A. Aye, Improving code autocompletion with 
transfer learning, in: Proceedings of the 44th International Conference on 
Software Engineering: Software Engineering in Practice, 2022, pp. 161–162.
[44] M. Izadi, R. Gismondi, G. Gousios, CodeFill: Multi-token code completion by 
jointly learning from structure and naming sequences, in: Proceedings of the 
30th ACM Joint Meeting on European Software Engineering Conference and 
Symposium on the Foundations of Software Engineering, 2022.
[45] V.J. Hellendoorn, P. Devanbu, Are deep neural networks the best choice for 
modeling source code? in: Proceedings of the 11th Joint Meeting on Foundations 
of Software Engineering, 2017, pp. 763–773.
[46] A. Svyatkovskiy, S.K. Deng, S. Fu, N. Sundaresan, Intellicode compose: Code 
generation using transformer, in: Proceedings of the 28th ACM Joint Meeting on 
European Software Engineering Conference and Symposium on the Foundations 
of Software Engineering, 2020, pp. 1433–1443.
[47] S. Zhou, U. Alon, F.F. Xu, Z. Jiang, G. Neubig, DocPrompting: Generating code 
by retrieving the docs, in: The Eleventh International Conference on Learning 
Representations.
[48] D. Zan, B. Chen, Z. Lin, B. Guan, W. Yongji, J.-G. Lou, When language 
model meets private library, in: Findings of the Association for Computational 
Linguistics: EMNLP 2022, 2022, pp. 277–288.
[49] S.A. Hayati, R. Olivier, P. Avvaru, P. Yin, A. Tomasic, G. Neubig, Retrieval-based 
neural code generation, in: Proceedings of the Conference on Empirical Methods 
in Natural Language Processing, 2018.
[50] M. Bruch, M. Monperrus, M. Mezini, Learning from examples to improve code 
completion systems, in: Proceedings of the 7th Joint Meeting of the European 
Software Engineering Conference and the ACM SIGSOFT Symposium on the 
Foundations of Software Engineering, 2009, pp. 213–222.
[51] H.A. Nguyen, T.N. Nguyen, D. Dig, S. Nguyen, H. Tran, M. Hilton, Graph-based 
mining of in-the-wild, fine-grained, semantic code change patterns, in: 2019 
IEEE/ACM 41st International Conference on Software Engineering, ICSE, IEEE, 
2019, pp. 819–830.
[52] R. Pan, A.R. Ibrahimzada, R. Krishna, D. Sankar, L.P. Wassi, M. Merler, B. 
Sobolev, R. Pavuluri, S. Sinha, R. Jabbarvand, Lost in translation: A study of 
bugs introduced by large language models while translating code, in: Proceedings 
of the IEEE/ACM 46th International Conference on Software Engineering, 2024, 
pp. 1–13.
[53] J. Zhang, P. Nie, J.J. Li, M. Gligoric, Multilingual code co-evolution using large 
language models, in: Proceedings of the 31st ACM Joint European Software Engi-
neering Conference and Symposium on the Foundations of Software Engineering, 
2023, pp. 695–707.
Information and Software Technology 200 (2026) 108322 
12

[Vista original de la página 12](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-12.png)

![Página PDF 12, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-12.png)


<!-- PDF page 13 -->

## Página PDF 13

T.-D. Bui et al.
[54] S. Tipirneni, M. Zhu, C.K. Reddy, Structcoder: Structure-aware transformer for 
code generation, ACM Trans. Knowl. Discov. Data 18 (3) (2024) 1–20.
[55] H.A. Nguyen, H.D. Phan, S.S. Khairunnesa, S. Nguyen, A. Yadavally, S. Wang, 
H. Rajan, T. Nguyen, A hybrid approach for inference between behavioral 
exception api documentation and implementations, and its applications, in: 
Proceedings of the 37th IEEE/ACM International Conference on Automated 
Software Engineering, 2022, pp. 1–13.
[56] N. Tran, H. Tran, S. Nguyen, H. Nguyen, T. Nguyen, Does BLEU score work for 
code migration? in: 2019 IEEE/ACM 27th International Conference on Program 
Comprehension, ICPC, IEEE, 2019, pp. 165–176.
[57] T.T. Vu, T.-D. Bui, T.-D. Do, T.-T. Nguyen, H.D. Vo, S. Nguyen, Automated de-
scription generation for software patches, Inf. Softw. Technol. (ISSN: 0950-5849) 
(2024) 107543.
[58] J. Xu, Z. Cui, Y. Zhao, X. Zhang, S. He, P. He, L. Li, Y. Kang, Q. Lin, Y. Dang, et 
al., UniLog: Automatic logging via LLM and in-context learning, in: Proceedings 
of the 46th IEEE/ACM International Conference on Software Engineering, 2024, 
pp. 1–12.
[59] M. Geng, S. Wang, D. Dong, H. Wang, G. Li, Z. Jin, X. Mao, X. Liao, Large 
language models are few-shot summarizers: Multi-intent comment generation 
via in-context learning, in: Proceedings of the 46th IEEE/ACM International 
Conference on Software Engineering, 2024, pp. 1–13.
[60] S. Gao, C. Gao, Y. He, J. Zeng, L. Nie, X. Xia, M. Lyu, Code structure–guided 
transformer for source code summarization, ACM Trans. Softw. Eng. Methodol. 
32 (1) (2023) 1–32.
[61] S. Nguyen, H. Phan, T. Le, T.N. Nguyen, Suggesting natural method names 
to check name consistencies, in: 2020 IEEE 42nd International Conference on 
Software Engineering, IEEE, 2020, pp. 1372–1384.
[62] Z. Liu, C. Chen, J. Wang, X. Che, Y. Huang, J. Hu, Q. Wang, Fill in the blank: 
Context-aware automated text input generation for mobile gui testing, in: 2023 
IEEE/ACM 45th International Conference on Software Engineering, ICSE, IEEE, 
2023, pp. 1355–1367.
[63] Y. Lan, Y. Lu, Z. Li, M. Pan, W. Yang, T. Zhang, X. Li, Deeply reinforcing 
android GUI testing with deep reinforcement learning, in: Proceedings of the 
46th IEEE/ACM International Conference on Software Engineering, 2024, pp. 
1–13.
[64] Y. Li, S. Wang, T.N. Nguyen, S. Van Nguyen, Improving bug detection via 
context-based code representation learning and attention-based neural networks, 
Proc. ACM Program. Lang. 3 (OOPSLA) (2019) 1–30.
[65] S. Nguyen, T.-T. Nguyen, T.T. Vu, T.-D. Do, K.-T. Ngo, H.D. Vo, Code-centric 
learning-based just-in-time vulnerability detection, J. Syst. Softw. 214 (2024) 
112014.
[66] F. Qiu, Z. Liu, X. Hu, X. Xia, G. Chen, X. Wang, Vulnerability detection via 
multiple-graph-based code representation, IEEE Trans. Softw. Eng. (2024).
[67] T.-T. Nguyen, H.D. Vo, Context-based statement-level vulnerability localization, 
Inf. Softw. Technol. 169 (2024) 107406.
[68] S. Nguyen, T.-T. Vu, D.-H. Vo, VFFINDER: A graph-based approach for auto-
mated silent vulnerability-fix identification, in: Proceedings of the 15th IEEE 
International Conference on Knowledge and Systems Engineering, 2023.
[69] C.S. Xia, Y. Wei, L. Zhang, Automated program repair in the era of large pre-
trained language models, in: 2023 IEEE/ACM 45th International Conference on 
Software Engineering, ICSE, IEEE, 2023, pp. 1482–1494.
[70] H. Ruan, Y. Noller, S. Tizpaz-Niari, S. Chattopadhyay, A. Roychoudhury, Timing 
side-channel mitigation via automated program repair, ACM Trans. Softw. Eng. 
Methodol. (2024).
Information and Software Technology 200 (2026) 108322 
13

[Vista original de la página 13](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-13.png)

![Página PDF 13, representación visual original](../../../../../images/v5/estructura_colecciones/Same%20Solution/secondary/Rambo/page-13.png)
