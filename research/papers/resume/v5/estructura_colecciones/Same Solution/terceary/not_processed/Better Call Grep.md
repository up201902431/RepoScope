# Ficha — Better Call Grep

## Identidad
- **Título:** *Better Call Grep: Evaluating and Improving Grep-Like Lexical Retrieval for Repository-Level Code Completion*.
- **Autores/año/venue:** Metadatos y versión no confirmados independientemente; no inferir publicación por el texto extraído.
- **Fuente:** Extracción PyMuPDF; páginas físicas desde 1, con advertencia de posibles alteraciones en tablas/figuras.
- **Grupo:** Same Solution / terceary / not_processed.
- **Cobertura:** Lectura íntegra reportada previamente. El anuncio de repositorio no fue verificado.

## Pregunta y contribución
Evalúa retrieval léxico tipo grep para completion repository-level y propone mejorar GrepRAG. El análisis reporta que recuperar fragmentos lexicalmente coincidentes puede ser eficaz; emplea BM25 reranking y deduplicación estructural para mejorar selección.

## Método
Contrasta retrieval léxico contra estrategias de mayor coste y baselines RAG. La tarea es completion; no generación de docs, reparación ni revisión.

## Documentos y arquitectura
Corpus de código fuente indexado léxicamente; reranking/deduplicación de fragmentos. Sin vínculo documental API-doc.

## Evaluación
El abstract reporta 7.04–15.58% de mejora relativa en code EM frente al mejor baseline y recuperación/generación más rápida (el texto extraído menciona ~0.40 s para enfoque GrepRAG frente a 3–7 s de baselines en un análisis). Los valores dependen de configuración; verificar tablas. El paper señala evaluación scripts en GitHub, pero no se comprobaron ni ejecutaron.

## Artefactos
URL anunciada en la fuente; disponibilidad, commit, licencia y correspondencia con esta versión no verificados.

## Relación con nuestra tesis
Comparador cercano para cuestionar si métodos documentales aportan frente a retrieval lexical/simple. No asume mismas APIs, contexto o tarea que RepoScope.

## Riesgos
Solapamiento lexical puede recuperar código con palabras compartidas pero semántica distinta; deduplicación puede quitar evidencia útil. Revisar fugas por duplicados/repos y medir coste con hardware homogéneo.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| GrepRAG y mejora relativa de EM 7.04–15.58%. | Extracción del paper | Abstract, pp. 1–2 | Resultado reportado |
| Método combina BM25 reranking y deduplicación estructural. | Extracción del paper | Method, aprox. pp. 4–8 | Método reportado |
| Diferencia de latencia mencionada (~0.40 s frente a 3–7 s). | Extracción del paper | Analysis/Results, pp. 3–4 | Resultado reportado |

## Pendientes
Verificar fecha/versión, tablas, protocolo temporal y hardware, URL/licencia y scripts. No reproducido.
