# AURA: Automated Updates And Repository Assistant

- source_pdf: ../../../../../../pdf/Related/terceary/maybe%20related/AURA.pdf
- extraction_tool: PyMuPDF
- extraction_date: 2026-11-24
- status: automatic-text-extraction; not manually verified
- pagination: physical PDF pages, starting at 1

> Copia de trabajo para búsqueda y citas. Verifica tablas, fórmulas, figuras y orden visual en el PDF original o en el PNG de la página.


<!-- PDF page 1 -->

## Página PDF 1

AURA: Automated Updates And Repository Assistant
Daniel Ivanov,
Itamar Alon,
Daniel Bar-On,
Sarel Cohen
The Academic College of Tel Aviv-Yaffo, Israel
{danielba2, danieliv, itamaral2, sarelco}@mta.ac.il
ABSTRACT
AI development faces challenges from fragmented workflows
and varied LLM integrations. This modular GitHub frame-
work offers structured guidance, seamless support for major
LLMs, and clear, low-maintenance workflows—enabling sus-
tainable and collaborative innovation.
CCS CONCEPTS
• Software and its engineering →Software develop-
ment frameworks; Version control; Open source model;;
KEYWORDS
LLM’s, Version Control, Automated Testing, API Integration
1
INTRODUCTION
Recent advances in LLMs have boosted code automation,
but most tools still offer only snippet-level support, limiting
real-world applicability. As discussed by Cheng et al. [1],
shifting to workflow-centric frameworks is key to enabling
effective, AI-driven development. This work proposes a mod-
ular GitHub-based platform that unifies planning, coding,
testing, and version control, integrates with various LLM
providers, and experiments with full code and structured
graph inputs—aiming to create a sustainable foundation for
end-to-end AI-augmented software engineering.
2
OUR APPROACH
This work presents a modular, open-source GitHub frame-
work that unifies planning, coding, QA, and Git workflows,
with built-in CI and structured templates. It supports flexible
LLM integration (OpenAI, Google, self-hosted) and explores
full files, code graphs, and diffs as inputs. Unlike Cheng et al.
[1], it delivers a practical, scalable solution beyond snippet-
level assistance.
Permission to make digital or hard copies of part or all of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that copies
bear this notice and the full citation on the first page. Copyrights for third-
party components of this work must be honored. For all other uses, contact
the owner/author(s).
SYSTOR ’25, September 8–9, 2025, Virtual, Israel
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2119-9/2025/09.
https://doi.org/10.1145/3757347.3759151
Figure 1: Overview of the AURA system architecture.
3
ENHANCED SECURITY
AURA isolates every AI task in a Docker sandbox and auto-
matically vets generated code, blocking unauthorized access
and malicious actions.
Table 1: compares the token counts for the full AURA workflow
powered by GPT-4o and GPT-3.5-Turbo, against the total tokens con-
sumed by the low-cost o3-mini reasoning model when both are used
to fix the same GitHub issue.
LOC/Txt
Tokens
(4o/3.5)
Cost
(4o/3.5)
Tokens
(o3-mini)
Cost
(OpenAI)
19/9
2173/2128
$.0094/.0033
2006
$.0078
14/14
7776/7656
$.0230/.0116
9701
$.0230
33/12
3253/10926
$.0139/.0172
3151
$.0164
32/376
6181/-
$.0200/-
11684
$.0354
4
CONCLUSION
Initial experiments show that our workflow can resolve GitHub issues for
only a few cents using GPT-4o and GPT-3.5-turbo significantly cheaper
than larger reasoning models. Although tested on small bug-fix examples
and limited to issue triage in Docker, the approach hints at broader appli-
cations (e.g., automated code review, issue generation) once lightweight,
self-hostable counterparts such as DeepSeek are integrated. These early
results point toward affordable, fully automated code-maintenance pipelines
that could keep open-source projects healthy with minimal human effort.
REFERENCES
[1] Fei Cheng et al. Beyond snippet assistance: A workflow-centric frame-
work for end-to-end ai-driven code generation. In Proceedings of the 31st
ACM Joint European Software Engineering Conference and Symposium
on the Foundations of Software Engineering (ESEC/FSE), pages 1234–1246.
ACM, 2023.
223

[Vista original de la página 1](../../../../../../images/v5/estructura_colecciones/Related/terceary/maybe%20related/AURA/page-01.png)

![Página PDF 1, representación visual original](../../../../../../images/v5/estructura_colecciones/Related/terceary/maybe%20related/AURA/page-01.png)
