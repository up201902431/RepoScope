# Cronología verificable de generación de código basada en repositorios

## Alcance y método de revisión

Este documento separa:

1. **cronología pública verificable**, basada en versiones arXiv, conferencias o publicaciones formales;
2. **líneas metodológicas**, sin asignar causalidad ni presentar trabajos como generaciones sucesivas;
3. **comparaciones numéricas dentro de cada paper**;
4. **condiciones comunes reejecutadas** frente a resultados reunidos por el propio paper.

No se asume que un paper mejora a otro por aparecer después. Tampoco se comparan resultados entre papers con modelos, datasets o métricas distintas.

## Convenciones

- `A.5.` = década de la fuente local no implica primera publicación.
- `Primera publicación pública` = primera v1 del documento, primera presentación o anuncio formal cuando la fuente local permite verificarlo.
- `Cálculo del informe` = diferencia matemática calculada a partir de valores publicados.
- `Puntos porcentuales` = diferencia absoluta entre porcentajes.
- `Mejora relativa` = `(método - baseline) / baseline × 100`.
- `pendiente de verificar` se usa cuando falta información suficiente en las fuentes disponibles.

## Vista A. Cronología por primera publicación pública verificable

| Trabajo | Autores | Primera aparición pública verificable | Versión local comprobada | Publicación formal | Fecha de conferencia o publicación | Identificador | Evidencia local |
|---|---|---|---|---|---|---|---|
| RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation | Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, Weizhu Chen | arXiv v1: 22-03-2023 | Pendiente de verificar la versión exacta del Markdown. El PDF local identifica la publicación de EMNLP 2023. | EMNLP 2023 | 6-10-12-2023 | arXiv: `2303.12570` | [RepoCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoCoder.md), Página 1 |
| A3-CodGen: A Repository-Level Code Generation Framework for Code Reuse With Local-Aware, Global-Aware, and Third-Party-Library-Aware | Dianshu Liao, Shidong Pan, Xiaoxia Sun, Xiaoxue Ren, Qing Huang, Zhenchang Xing, Huan Jin, Qinying Li | arXiv v1: 12-12-2023 | El Markdown no declara versión arXiv. | IEEE Transactions on Software Engineering | Recibido 03-03-2024; revisado 30-09-2024; aceptado 13-10-2024; publicado 24-10-2024 | arXiv: `2312.05772`; DOI pendiente de verificar | [A3-CodGen](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/A3-CodGen.md), Página 1 |
| RepoHyper: Search-Expand-Refine on Semantic Graphs for Repository-Level Code Completion | Huy N. Phan, Hoang N. Phan, Tien N. Nguyen, Nghi D. Q. Bui | arXiv v1: 10-03-2024 | Pendiente de verificar la versión exacta del Markdown. | Pendiente de verificar | Pendiente de verificar | arXiv: `2403.06095` | [RepoHyper](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoHyper.md), Página 1 |
| CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges | Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, Zhi Jin | arXiv v1: pendiente de verificar; el local indica arXiv y v2 el 09-08-2024 | El local contiene arXiv: `2401.07339v2` | Pendiente de verificar formalmente | Pendiente de verificar | arXiv: `2401.07339` | [CodeAgent](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/CodeAgent.md), Página 1 |
| DRACO: Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion | Wei Cheng, Yuhan Wu, Wei Hu | arXiv v1: 30-05-2024 | Pendiente de verificar la versión exacta del Markdown. | ACL 2024 | 11-16-08-2024, Bangkok | arXiv: `2405.19782`; DOI pendiente de verificar | [DRACO](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/DRACO_Dataflow-Guided%20Retrieval%20Augmentation%20for%20Repository-Level%20Code%20Completion.md), Página 1 |
| GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang | arXiv v1: 11-06-2024 | El local indica revisión del 13-09-2024 | ASE 2024 | 27-10-2024 a 1-11-2024 | arXiv: `2406.07003`; DOI pendiente de verificar | [GraphCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/GraphCoder.md), Página 1 |
| RLCoder: Reinforcement Learning for Repository-Level Code Completion | Yanlin Wang, Yanli Wang, Daya Guo, Jiachi Chen, Ruikai Zhang, Yuchi Ma, Zibin Zheng | arXiv v1: 28-07-2024 | El Markdown no declara otra versión. | Pendiente de verificar | Pendiente de verificar | arXiv: `2407.19487` | [RLCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/terceary/less%20important/RLCoder.md), Página 1 |
| AllianceCoder / What to Retrieve for Effective Retrieval-Augmented Code Generation | Wenchao Gu, Juntao Chen, Yanlin Wang, Tianyue Jiang, Xingzhe Li, Mingwei Liu, Xilin Liu, Yuchi Ma, Zibin Zheng | arXiv v1: 26-03-2025 | El local indica arXiv: `2503.20589v1` | Pendiente de verificar formalmente | Pendiente de verificar | arXiv: `2503.20589`; DOI pendiente de verificar | [AllianceCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/AllianceCoder.md), Página 1 |
| RepoMind: Enhancing Repository-Level Code Generation via LLM Reasoning over Structured Repository Documentation | Songwen Gong, Mengzhen Wang, Jiexin Wang, Yi Cai | Pendiente de verificar v1 en repositorio; el documento formal es ICPC 2026 | El Markdown no declara versión arXiv | ICPC 2026, research track | 12-13-04-2026 | DOI: `10.1145/3794763.3794823`; arXiv pendiente de verificar | [RepoMind](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/RepoMind.md), Página 1 |
| RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation | Yang Liu, Li Zhang, Fang Liu, Zhuohang Wang, Donglin Wei, Zhishuo Yang, Kechi Zhang, Jia Li, Lin Shi | arXiv v1/v2: pendiente de verificar la primera; el local muestra arXiv `2507.14791v2` | Versión local comprobada: `v2` | ICSE 2026 | 12-18-04-2026 | arXiv: `2507.14791`; DOI `10.1145/3744916.3773211` | [RepoScope](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/RepoScope.md), Página 1 |
| RepoFuse: Repository-Level Code Completion with Fused Dual Context | Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, Peng Di | Primera aparición local pendiente de verificar; arXiv local del trabajo 2024: pendiente de verificar | El Markdown 2024 no declara versión y corresponde a otra publicación denominada RepoFuse | Publicación 2024 pendiente de verificar formalmente | Pendiente de verificar | Identificador pendiente de verificar | [RepoFuse 2024](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse.md), Página 1 |
| RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale | Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan, Peng Di | Pendiente de verificar | Pendiente de verificar | FSE Companion 2026 | 5-9-07-2026 | DOI: `10.1145/3803437.3805230`; arXiv pendiente de verificar | [RepoFuse 2026](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse.md), Página 1 |
| RepoShapley: Shapley-Enhanced Context Filtering | Yu Huo, Kun Zeng, Siyu Zhang, Yuquan Lu, Cheng Yang, Yifu Guo, Xiaoying Tang | Pendiente de verificar | El Markdown no declara versión | Pendiente de verificar formalmente | Pendiente de verificar | Pendiente de verificar | [RepoShapley](../papers/text/v5/estructura_colecciones/Same%20Solution/fourth/repoShapley.md), Página 1 |
| MRCoder: An Efficient Context Selecting Approach for Repository-Level Code Generation | Peiding Wang, Li Zhang, Fang Liu | arXiv: `2607.26805`, primera aparición pendiente de verificar | El local no declara versión | Pendiente de verificar formalmente | Pendiente de verificar | arXiv: `2607.26805`; DOI pendiente | [MRCoder](../papers/text/v5/estructura_colecciones/Related/fourth/mrcoder.md), Página 1 |
| FeatX: Editing Software by Editing Features for Repository-Level Code Evolution | Xutian Li, Yifeng Zhu, Xianlin Zhao, Yanzhen Zou, Lu Zhang, Bing Xie | arXiv v1: 30-06-2026 | El Markdown no declara versión | ASE 2026 | 12-16-10-2026 | arXiv: `2606.31206`; DOI pendiente de verificar | [FeatX](../papers/text/v5/estructura_colecciones/Documentation-Code/fourth/FeatX.md), Página 1 |
| RepoProbe: Benchmarking Architecture-Aware Repository Comprehension with Checklists | Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Yuhong Liu, Zhen Qin | arXiv v1: pendiente de verificar; arXiv local `2608.04783v2` indica revisión | Versión local comprobada: `v2` | ASE 2026 | pendiente de verificar fecha exacta dentro de la conferencia | arXiv: `2608.04783`; DOI/DOI local pendiente de verificar | [RepoProbe](../papers/text/v5/estructura_colecciones/Evaluation/fourth/repoProbe.md), Página 1 |
| FeatLens: Feature-Guided Dependency Retrieval for Repository-Level Code Generation | Xutian Li, Bo Xiong, Yifeng Zhu, Runbang Yan, Yanzhen Zou, Lu Zhang, Bing Xie | **Primera publicación pública v1: 22-09-2026** | **Versión local comprobada: v2** | Pendiente de verificar formalmente | Revisión v2: 28-10-2026 | arXiv: `2609.26480v2`; DOI pendiente | [FeatLens](../papers/text/v5/estructura_colecciones/Same%20Solution/fourth/FeatLens.md), Página 1 |

---

## Diferencias entre RepoFuse 2024 y RepoFuse 2026

El nombre repetido no identifica un único trabajo.

- El Markdown 2024 describe contexto dual llamado `analogy context` y `rationale context`.
- La publicación 2026 describe `semantic context` y `similar context`, un experimento industrial y un A/B test de una semana.
- Sus resultados no deben combinarse.
- Sin una identificación formal de las dos versiones en los metadatos locales, su relación de software o continuidad permanece pendiente de verificar.

---

## Vista B. Mapa metodológico

Las siguientes líneas son paralelas y no generan por sí mismas una secuencia histórica.

### B1. Recuperación por similitud

**Problema:** el código del repositorio supera el contexto disponible y puede contener patrones relevantes.

**Cambio:** indexar o recuperar snippets textualmente o semánticamente similares.

**Evidencia:** RepoCoder combina recuperación con generación iterativa; además, AllianceCoder encuentra que snippets similares pueden añadir ruido.

**Limitación:** la semejanza no garantiza dependencia funcional.

**Relación con la tesis:** es un baseline conceptual para el contexto seleccionado, no una representación suficiente de API-documento-requisito.

### B2. Compleción iterativa

**Problema:** una consulta incompleta no describe suficientemente el target.

**Cambio:** usar el borrador generado como nueva consulta.

**Evidencia:** RepoCoder reporta mejoras sobre In-File y RAG vanilla, pero no existen datos comunes que permitan afirmar que la misma mejora se mantiene frente a todos los métodos posteriores.

**Limitación:** el borrador puede contener APIs inventadas o incompletas.

**Relación con la tesis:** el requisito inicial y las APIs recuperadas podrían combinarse, pero la iteración no prueba por sí misma calidad documental.

### B3. Recuperación estructural

**Problema:** imports, llamadas, tipos y dependencias no quedan representados por texto similar.

**Cambio:** construir grafos repo-específicos o usar análisis de dataflow/controlflow.

**Evidencia:** RepoHyper usa un Repo-level Semantic Graph; DRACO usa dataflow; GraphCoder usa control, data y control-dependence.

**Limitación:** algunas estructuras tienen coste, requieren adaptación o pueden recuperar elementos irrelevantes.

**Relación con la tesis:** aporta mecanismos para ligar API y documentación con el flujo real del repositorio.

### B4. Separación de contexto local, global y externo

**Problema:** el contexto del archivo actual no basta; también intervienen clases, módulos y librerías externas.

**Cambio:** representar explícitamente contexto local, global y third-party.

**Evidencia:** A3-CodGen organiza estas tres vistas.

**Limitación:** las métricas de reuse y correcta API no equivalen automáticamente a Pass@1.

**Relación con la tesis:** una documentación asociada a API podría clasificarse por alcance local/global sin asumir equivalencia.

### B5. Aprender utilidad de recuperación

**Problema:** un retriever no dispone siempre de candidatos labeled.

**Cambio:** usar feedback del generador o de perplexity para actualizar el retriever y decidir cuándo recuperar.

**Evidencia:** RLCoder usa perplexity, weighted perplexity y stop signal. RepoShapley usa utilidad marginal e interacción entre chunks.

**Limitación:** la utilidad depende del modelo generador y puede no transferirse.

**Relación con la tesis:** podría filtrar documentos asociados a APIs recuperadas.

### B6. Agentes con herramientas

**Problema:** la navegación y validación pueden requerir búsquedas y ejecución iterativa.

**Cambio:** dar al modelo herramientas para buscar símbolos, documentación, archivos y pruebas.

**Evidencia:** CodeAgent integra cinco herramientas y cuatro estrategias.

**Limitación:** múltiples llamadas, coste y problemas de estrategia.

**Relación con la tesis:** no es necesario asumir que un agente genera documentación mejor que una representación preconstruida.

### B7. Documentación jerárquica

**Problema:** el repositorio completo no cabe en el contexto y las descripciones a nivel de API no muestran suficiente estructura.

**Cambio:** construir documentación API, archivo y módulo o paquete.

**Evidencia:** RepoMind genera API-Doc, File-Doc y Module-Doc; el trabajo jerárquico empresarial agrega segmento, archivo y paquete.

**Limitación:** calidad, procedencia, filtrado y compatibilidad entre documentos no están resueltos.

**Relación con la tesis:** es el núcleo documental candidato, pero debe evaluarse separadamente de documentación humana.

### B8. Selección y filtrado de contexto

**Problema:** añadir más contexto aumenta ruido, coste y longitud.

**Cambio:** borrar, rankear o compactar fragmentos antes de generación.

**Evidencia:** MRCoder usa Map–Reduce y drafts; RepoShapley estima utilidad coalicional; RepoScope preserva vistas y estructura.

**Limitación:** los resultados dependen del presupuesto, modelo y segmentación.

**Relación con la tesis:** este mecanismo puede asociarse al filtro requisito–documento y no reemplazar la recuperación de APIs.

### B9. Features y dependencias

**Problema:** una API o snippet similar puede no cubrir todas las dependencias funcionales.

**Cambio:** vincular descripción funcional, entidad de código y dependencias dispersas.

**Evidencia:** FeatLens construye un índice feature–código y expande dependencias; FeatX mantiene feature-to-code mappings para evolución.

**Limitación:** todavía no verificamos compatibilidad ni adaptación a Python para todos los datasets.

**Relación con la tesis:** ofrece una posible unidad intermedia entre requisito y documentación.

### B10. Comprensión arquitectónica

**Problema:** Pass@1 puede recompensar generación sin comprender el repositorio.

**Cambio:** evaluar respuestas abiertas sobre arquitectura con hechos verificables.

**Evidencia:** RepoProbe usa GitHub Discussions y checklist-based verification.

**Limitación:** es evaluación, no un método de generación.

**Relación con la tesis:** puede complementar Pass@1, API Precision/Recall/F1 y calidad de enlaces.

---

# Comparaciones numéricas verificables

## RepoMind contra otros métodos

**Fuente:** [RepoMind](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/RepoMind.md), sección 5.1, Tabla 1, página PDF física 7.

**Tabla conjunta disponible:** CoderEval y DevEval; GPT-4o-Mini, DeepSeek-V3 y Qwen3-235B-A22B.

| Dataset/modelo | SimpleRAG | RepoCoder | DRACO | CodeAgent | RLCoder | AllianceCoder | RepoScope | RepoMind |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CoderEval GPT-4o-Mini | 39.13 | 37.68 | 40.10 | 27.54 | 38.16 | 41.02 | 44.93 | 47.34 |
| CoderEval DeepSeek-V3 | 48.79 | 50.72 | 47.34 | 39.13 | 46.86 | 51.69 | 59.42 | 56.04 |
| CoderEval Qwen | 43.00 | 44.44 | 41.06 | 33.82 | 40.58 | 45.41 | 49.28 | 52.17 |
| DevEval GPT-4o-Mini | 22.61 | 20.84 | 25.26 | 15.33 | 19.69 | 33.98 | 26.18 | 37.37 |
| DevEval DeepSeek-V3 | 28.53 | 28.93 | 32.09 | 25.89 | 27.90 | 46.15 | 35.82 | 48.34 |
| DevEval Qwen | 21.81 | 22.96 | 29.39 | 21.70 | 22.39 | 39.55 | 30.02 | 44.89 |

**Procedencia de RepoScope:** RepoMind indica: `REPOSCOPE did not release its code, so the experimental data was sourced from the original paper, and comparisons for RQ could not be performed.` La nota aparece en la sección 4.2 / página 7 de [RepoMind](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/RepoMind.md).

**No se confirma que RepoMind reejecute RepoScope.**

### Diferencias calculadas por el informe

- CoderEval GPT-4o-Mini: RepoMind 47.34 frente a RepoScope 44.93.
  - Diferencia absoluta: **+2.41 puntos porcentuales**.
  - Mejora relativa calculada: `(47.34 - 44.93) / 44.93 × 100 = 5.36%`.
- CoderEval Qwen: RepoMind 52.17 frente a RepoScope 49.28.
  - Diferencia absoluta: **+2.89 puntos porcentuales**.
  - Mejora relativa calculada: **5.86%**.
- DevEval GPT-4o-Mini: RepoMind 37.37 frente a AllianceCoder 33.98.
  - Diferencia absoluta: **+3.39 puntos porcentuales**.
  - Mejora relativa calculada: **9.98%**.
- CoderEval DeepSeek-V3: RepoScope 59.42 frente a RepoMind 56.04.
  - Diferencia absoluta: **-3.38 puntos porcentuales**.
  - RepoScope supera a RepoMind en esta celda según la propia tabla.

Estas diferencias son cálculos del informe. El paper no las atribuye todas como mejoras porcentuales propias.

## RLCoder contra RepoCoder y métodos previos

**Fuente:** [RLCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/terceary/less%20important/RLCoder.md), Tabla II y texto de RQ1, páginas físicas 7–10.

- CrossCodeEval Python, DeepSeekCoder-7B: RLCoder 30.28 EM frente al mejor baseline RepoCoder 26.99 EM.
- Diferencia absoluta publicada en la página: **+12.2%**.
- Este incremento se presenta como mejora relativa del EM frente al baseline.
- RepoEval Line: RLCoder 39.88 frente a baseline relacionado 37.95, según el texto local.
- RepoEval API: RLCoder queda por debajo o empate según el modelo; no se debe afirmar mejora general.
- Integración RepoCoder con RLCoder:
  - CrossCodeEval Python: mejora 12.4% EM.
  - CrossCodeEval Java: mejora 8.1% EM.

**Procedencia del baseline:** no se confirma que todas las variantes se hayan reejecutado en una única infraestructura. El paper presenta comparaciones de su propia tabla, pero el Markdown local no permite comprobar todas las configuraciones.

## RepoScope contra baselines

**Fuente:** [RepoScope](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/RepoScope.md), Tabla 2, página física 8.

El paper afirma que compara contra baselines en CoderEval y DevEval con cuatro modelos.

- DevEval/Claude-3.5-Haiku: RepoScope supera al mejor baseline DRACO con una mejora relativa reportada de **36.35%** en Pass@1.
- CoderEval/DeepSeek-V3: el paper reporta una mejora relativa de **17.15%**.
- Los porcentajes deben conservarse como mejora relativa reportada.
- No se debe inferir que esa mejora se alcanza para todos los modelos o datasets.
- Integración:
  - RepoScope* 53.14;
  - +RLCoder 54.11, mejora relativa reportada 1.83%;
  - +RepoCoder 56.04, mejora relativa reportada 5.46%.

**Fuente:** Tabla 5, página 10.

No se confirma que estas integraciones sean ejecuciones externas independientes de todos los componentes. Son resultados del paper.

## DRACO

**Fuente:** [DRACO](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/DRACO_Dataflow-Guided%20Retrieval%20Augmentation%20for%20Repository-Level%20Code%20Completion.md), abstract y experimental analysis.

- Comparación reportada:
  - Exact Match: mejora de 3.43% frente al método previo.
  - Identifier F1: mejora de 3.27%.
- La fuente no permite delimitar sin ambigüedad si ambos son puntos porcentuales absolutos o mejoras relativas.
- Baseline concreto: estado previo de su tabla, pendiente de verificar en el texto/tablas locales.
- Dataset/subconjunto: ReccEval y comparativas adicionales en CrossCodeEval; las condiciones completas están pendientes de verificar.

## GraphCoder

**Fuente:** [GraphCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/GraphCoder.md), Página 1.

- Code match: **+6.06** frente a baselines RAG.
- Identifier match: **+6.23**.
- Estas diferencias son sumas absolutas de métricas reportadas por el paper; no son mejoras relativas.
- Baseline concreto, dataset y modelo exactos: pendientes de verificar en la Tabla de resultados.

## AllianceCoder

**Fuente:** [AllianceCoder](../papers/text/v5/estructura_colecciones/Same%20Solution/primary/AllianceCoder.md), abstract y tablas, páginas 1 y 7–9.

- El abstract afirma hasta 20% en Pass@1 sobre enfoques existentes.
- El Markdown local contiene comparaciones text-to-code y API recall, pero no permite verificar sin ambigüedad el baseline principal de ese 20%.
- Por ello: **pendiente de verificar el baseline concreto y si el 20% es relativo o absoluto**.
- Las tablas sí muestran comparaciones internas donde API retrieval directo reduce Pass@1 frente a descripciones semánticas.

## RepoFuse

### RepoFuse 2024

**Fuente:** [RepoFuse 2024](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse.md), Página 1.

- Las dos fuentes locales de RepoFuse contienen métricas distintas.
- En la versión 2024 se reportan mejoras de 40.90% a 59.75% sobre analogy context y de 32.13% a 69.45% sobre rationale context según fragmentos HTML/arXiv.
- Estas cifras requieren confirmar baseline y definición: podrían ser mejoras relativas o diferencias percentuales.
- En el Markdown local, esta tabla no puede verificarse con suficiente detalle para atribuir una única comparación consolidada.

### RepoFuse 2026

**Fuente:** Markdown [RepoFuse 2026](../papers/text/v5/estructura_colecciones/Same%20Solution/secondary/RepoFuse.md), página 1.

- Aceptación industrial: +18%, valor reportado por el paper.
- Latencia: 156 ms.
- CrossCodeEval: mejoras de 4.26 EM Python y 3.01 EM Java.
- Sin confirmar si 4.26 y 3.01 son puntos de EM o mejoras relativas.
- La cifra de aceptación procede de A/B test de una semana y no es reejecutable sin el entorno industrial.

---

# Síntesis por línea metodológica

## Problema → cambio → evidencia → limitación → relación

### Similitud

- Problema: recuperar snippets relevantes.
- Cambio: construir RAG y similitud semántica.
- Evidencia disponible: RAG simple aparece como baseline en RepoMind y RepoCoder como mejora iterativa.
- Limitación: los resultados no permiten declarar que toda recuperación por similitud sea mala.
- Relación con la tesis: usar como baseline o condición de control.

### Iteración retrieval–generation

- Problema: el contexto incompleto no genera una consulta suficiente.
- Cambio: reutilizar el borrador para recuperar otra vez.
- Evidencia: RepoCoder afirma mejoras sobre In-File y RAG vanilla.
- Limitación: no demuestra compatibilidad con documentación.
- Relación con la tesis: la iteración puede cambiar el conjunto de documentos recuperados.

### Estructura

- Problema: imports, flujo y llamadas no aparecen en la similitud.
- Cambio: construir grafos o dataflow.
- Evidencia: RepoHyper, DRACO y GraphCoder presentan mejoras propias.
- Limitación: modelos, baselines y métricas no se pueden cruzar.
- Relación con la tesis: documentación vinculada podría conservar dependencias además de API.

### API como unidad

- Problema: el snippet similar no identifica qué API necesita el requisito.
- Cambio: descomponer requisitos y recuperar descripciones de API.
- Evidencia: AllianceCoder y RepoMind usan descripciones de API.
- Limitación: los resultados específicos no prueban que un método sea extensible al otro.
- Relación con la tesis: API→documento es una condición central candidata.

### Agentes

- Problema: encontrar símbolos y pruebas requiere exploración.
- Cambio: herramientas e interacción iterativa.
- Evidencia: CodeAgent mejora frente a su generación directa y otros productos.
- Limitación: coste y evaluación específica.
- Relación con la tesis: agente no es sinónimo de mejor documentación.

### Documentación

- Problema: el código completo es demasiado granular o el repositorio supera el contexto.
- Cambio: generar API-Doc, File-Doc y Module-Doc.
- Evidencia: RepoMind reporta mejoras en sus tablas.
- Limitación: no hay evidencia local de implementación conjunta con RepoScope.
- Relación con la tesis: es el componente central posible, no una solución demostrada.

### Filtro

- Problema: más contexto puede empeorar generación.
- Cambio: seleccionar fragmentos útiles y conservar coaliciones.
- Evidencia: MRCoder, RepoShapley y RLCoder.
- Limitación: cada uno usa un mecanismo distinto.
- Relación con la tesis: puede reducir documentos irrelevantes sin cambiar API retrieval.

### Features

- Problema: el requisito no se mapea directamente a API o archivo.
- Cambio: vincular feature, entidad y dependencia.
- Evidencia: FeatLens, FeatX.
- Limitación: resultados en evolution o dependencies no se deben convertir en Pass@1 documental.
- Relación con la tesis: feature puede ser unidad de selección de documento.

### Comprensión arquitectónica

- Problema: Pass@1 no mide explicación o diseño.
- Cambio: checklist y preguntas abiertas.
- Evidencia: RepoProbe.
- Limitación: no mide generación.
- Relación con la tesis: complemento necesario si se estudia arquitectura.

---

# Tipos de tarea

Los trabajos se clasifican en cinco categorías:

1. **Generación de funciones:** RepoMind, RepoScope, AllianceCoder, A3-CodGen, MRCoder, FeatLens.
2. **Completion:** RepoCoder, RepoHyper, DRACO, GraphCoder, RLCoder, RepoFuse, RepoShapley.
3. **Documentación:** RepoMind, documentación jerárquica empresarial, FeatX y FeatLens para feature-index.
4. **Recuperación:** RLCoder, DRACO, GraphCoder, RepoHyper, AllianceCoder, RepoET, GrepRAG y filtrado coalicional.
5. **Comprensión arquitectónica:** RepoProbe y trabajos que evalúan estructura sin producir código.

Esta clasificación no implica que un paper pertenezca exclusivamente a una categoría.

---

# Resultados calculados y procedencia

## Resultados que sí se presentan en una tabla común

- RepoMind tabla 1: comparación conjunta bajo su propio experimento.
- RLCoder Tabla II: comparación conjunta bajo sus propios experimentos.
- RepoScope Tabla 2: comparación conjunta bajo sus propios experimentos.
- RepoScope Tabla 5: integración con RLCoder y RepoCoder.
- RepoMind Tabla 2: ablaciones internas.

## Resultados cuyo baseline no fue reejecutado o no pudo confirmarse

- RepoScope dentro de RepoMind: tomado del paper original, no reejecutado por RepoMind.
- AllianceCoder 20%: baseline concreto pendiente de verificar.
- DRACO 3.43%/3.27%: baseline y formulación absoluta/relativa pendiente de verificar.
- GraphCoder: baselines concretos y tabla completa pendientes de verificar.
- RepoFuse 2024 y 2026: procedencia y resultados no deben asociarse.
- RepoMind al afirmar mejoras internas: se presentan tablas comparadas, pero no todas las implementaciones están disponibles.
- RepoProbe, MRCoder, RepoShapley y FeatLens: no se confirmó una tabla común compartida con RepoScope/RepoMind.
- FeatLens: versión local v2, no confundir con primera publicación v1.

---

# Datos pendientes de verificar

- Fecha de v1 de CodeAgent.
- Fecha y revista formal de RepoHyper.
- Publicación formal y DOI de RLCoder.
- Publicación formal y DOI de AllianceCoder.
- Primera aparición pública y arXiv de RepoMind.
- Primera fecha pública exacta y v1/v2 de RepoScope.
- Autores, DOI y fechas exactas de ambas publicaciones RepoFuse.
- Identificador bibliográfico de RepoShapley.
- Fecha formal y DOI de MRCoder.
- DOI formal y datos completos de FeatX.
- Versión v1/v2 de RepoProbe y DOI formal.
- Definición exacta de los 3.43% y 3.27% de DRACO.
- Baseline concreto del 20% de AllianceCoder.
- Diferencia absoluta o relativa exacta de las mejoras de RepoFuse.
- Contraste reejecutado entre RepoMind y RepoScope.

---

# Conclusión delimitada

Las comparaciones disponibles muestran que el RAG simple puede resultar inferior a métodos que añaden iteración, estructura o recuperación de API en tablas específicas. No permiten afirmar que toda variante RAG simple sea inferior en todos los modelos o tareas.

La documentación jerárquica aparece como una línea independiente. RepoMind la combina con búsqueda vectorial y razonamiento, pero no puede presentarse como extensión implementada de RepoScope.

Para la tesis, una dirección verificable consiste en fijar un baseline, fijar las APIs recuperadas y comparar distintos tipos de documentos asociados:

`baseline -> documentos asociados -> selección por requisito -> generación`

Mantener esta comparación separada evita atribuir mejoras cruzadas sin condiciones comunes.
