# RepoSummary — concise resume

- **Reference:** Yifeng Zhu et al., *RepoSummary: Feature-Oriented Summarization and Documentation Generation for Code Repositories*, arXiv:2510.11039v1 (2025).
- **What it does:** Generates epics/features from Java repository code and links them to implementing methods and files (RepoSummary, local PDF, §§3–4, pp. 6–9).
- **How:** Eclipse JDT static relations + LLM method/file summaries + Sentence-BERT semantic similarity; hierarchical Leiden/CPM clustering at file then method level; LLM feature generation and epic aggregation (RepoSummary, local PDF, §§3.1–3.4, pp. 6–8).
- **Evaluation:** Three Java repositories (Dronology, eTour, iTrust) and 26 commits from three projects; compared with HMCS and HGEN using GPT-4o mini and Claude 3 (RepoSummary, local PDF, §§4.1–4.2, 5.3, pp. 9–10, 16).
- **Reported results:** For GPT-4o mini, average complete feature coverage is 0.711 vs. HGEN's 0.612; mean traceability recall is 0.530 vs. 0.299; Link@3 recall on the commit set reaches 0.622 (RepoSummary, local PDF, pp. 13–16).
- **Relevance:** Useful precedent for generating feature-oriented repository documentation with code trace links. It does not retrieve/select documents for a requirement over recovered APIs or test whether documentation improves code generation (interpretation based on RepoSummary, local PDF, §§3–5, pp. 6–17).
- **Caveats:** Java-only implementation; three repository datasets; LLM-judge/prompt dependence; human coverage comparison limited to two repositories (RepoSummary, local PDF, §§4, 6, pp. 9–13, 18–19). Results are paper-reported, not reproduced here.
- **Coverage/localizers:** Analytical reading focused on §§1, 3–6 and evaluation tables; PDF pages 2–19. The paper has 22 physical pages; references and related work were not exhaustively reviewed.
- **Source:** [arXiv record](https://arxiv.org/abs/2510.11039v1) · local PDF [`repoSummary.pdf`](../../../../../pdf/Documentation-Code/fourth/repoSummary.pdf).
- **Visual:** Original pipeline schematic: [pipeline.png](../../../../../images/v5/estructura_colecciones/Documentation-Code/fourth/repoSummary/pipeline.png) · [vector version](../../../../../images/v5/estructura_colecciones/Documentation-Code/fourth/repoSummary/pipeline.svg).
