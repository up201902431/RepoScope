# From Function to Repository

## Identidad
- **paper_id:** no asignado; identificador local provisional por nombre de archivo.
- **Título:** *From Function to Repository: Towards Understanding and an Agentic Approach for Repo-Level Directed Input Generation*.
- **Autores/año/venue:** Haoyu Wang et al.; ASE 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/From Function to Repository.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, preservado.
- **Cobertura:** lectura íntegra del Markdown declarada; se cotejaron fórmula/tabla en extracción y la página física 5 para protocolo. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** RepoEval y AgenticDIG se dirigen a generar entradas de prueba que alcanzan líneas objetivo.

**Interpretación:** investigación de testing dirigido, no benchmark de corrección de código generado ni módulo documental.

## Método
Evalúa cinco modelos en repositorios C/C++, Java y Python. AgenticDIG añade análisis orientado al objetivo, extracción de intención, inyección de fallas y feedback.

## Documentos y arquitectura
No genera documentación; el objeto son entradas de prueba, líneas objetivo y feedback de ejecución.

## Evaluación
Pass@K se define como proporción de líneas objetivo alcanzadas por al menos una entrada entre K consultas. Pass@3fb incluye feedback/iteración y no equivale a tres muestras independientes de Pass@3. El artículo informa máximo de 37,35 % de cobertura media de líneas objetivo para un baseline con Pass@3 y mejora relativa de cobertura de AgenticDIG frente al mejor baseline.

## Artefactos
Disponibilidad no verificada externamente; no se ejecutó.

## Relación con nuestra tesis
Puede aportar ideas sobre evaluación orientada a ejecución, pero no es benchmark directo para generación con documentación.

## Riesgos
La iteración con feedback cambia el presupuesto/condición de evaluación; no debe confundirse con generación one-shot.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Definición Pass@K/protocolo | PDF/Markdown local | §§3.3–5.1, física 5 | 3066 | Métrica/protocolo |
| Resultado de cobertura | PDF/Markdown local | §§3.3–5.1; tabla posterior a física 5 | Página exacta pendiente | Resultado reportado; tabla no localizada con precisión |

## Pendientes
Localizar página exacta de la tabla de resultados y verificar artefactos antes de reutilizar el benchmark.
