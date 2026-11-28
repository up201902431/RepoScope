# Ficha — RepoMinCoder

## Identidad
- **Título:** *RepoMinCoder: Improving Repository-Level Code Generation Based on Information Loss Screening*.
- **Autores/año/venue:** Pendiente de completar desde metadatos de portada.
- **Fuente:** Extracción PyMuPDF, páginas físicas 1–10; no visualmente cotejada.
- **Grupo:** Same Solution / terceary / less important.
- **Cobertura:** Lectura íntegra reportada previamente.

## Pregunta y contribución
Reducir el contexto recuperado manteniendo información útil para generación repository-level. Combina retrieval iterativo con selección/ordenamiento basado en MDL (minimum description length) e information-loss screening.

## Método
Retrieval y selección/ordenamiento de snippets; la evaluación de RepoEval usa completion API y EM/ES. No es generación de documentación ni reparación.

## Documentos y arquitectura
Snippets del repositorio. La propuesta trata cantidad/orden del código de contexto y no el enlace explícito de documentación con APIs.

## Evaluación
RepoEval; EM y ES reportados. El artículo discute límites de candidatos, segmentación y simplificación de prompts. No se transcriben cifras sin revisión de tablas. Resultados del artículo, no reproducción.

## Artefactos
No comprobados.

## Relación con nuestra tesis
Antecedente de selección bajo presupuesto; separar su efecto del módulo documental exigiría mantener constante recuperación/API context. No implica compatibilidad directa con RepoScope.

## Riesgos
Los límites de candidatos y chunks pueden alterar recall y contexto; MDL/ES no equivale a corrección. Revisar fuga por código objetivo y ejemplos duplicados.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Retrieval iterativo y selección/orden MDL. | Extracción del paper | Abstract/Method, pp. 1–6 | Método reportado |
| RepoEval con completion API, EM/ES; límites de candidatos y segmentación. | Extracción del paper | Evaluation/Discussion, pp. 7–10 | Métrica y limitaciones reportadas |

## Pendientes
Verificar cifras, baselines, modelos, secuencia de retrieval y artefactos en PDF/repositorio.
