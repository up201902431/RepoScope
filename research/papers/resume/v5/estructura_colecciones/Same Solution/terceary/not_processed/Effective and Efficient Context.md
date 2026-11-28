# Ficha — Effective and Efficient Context

## Identidad
- **Título de archivo:** *Effective and Efficient Context*; título bibliográfico exacto pendiente de cotejo.
- **Autores/año/venue:** Por verificar en portada.
- **Fuente:** PyMuPDF; paginación física desde 1; documento de 13 páginas según extracción.
- **Grupo:** Same Solution / terceary / not_processed.
- **Cobertura:** Lectura íntegra reportada anteriormente; no inspección visual.

## Pregunta y contribución
La fuente describe DyCoder/DyRetriever: selección dinámica de puntos de entrada, razonamiento multi-hop sobre un grafo parcial construido con asistencia de LLM y recuperación por similitud para aportar contexto de generación. No es documentación de arquitectura generada ni evaluación de generación de docs.

## Método
Combina búsqueda/selección de punto de entrada, grafo parcial y retrieval semántico; la tarea es generación de funciones a nivel repositorio. Incluye evaluación de rendimiento y coste.

## Documentos y arquitectura
Usa relaciones del código/grafo y fragmentos recuperados. No equiparar ese grafo a CodeWiki/SemArc/ArCoTL/TransArC ni suponer que ofrece documentos vinculados a APIs.

## Evaluación
CoderEval y DevEval; reporta Pass@1 y coste. El abstract informa mejoras relativas Pass@1 de 25.63% y 59.73% frente a baselines (CoderEval y DevEval, respectivamente) y velocidad de 7.4× frente a baselines indicados en el texto. Las cifras requieren revisión de tablas para identificar configuración exacta; resultados reportados, no reproducidos.

## Artefactos
No comprobados.

## Relación con nuestra tesis
Vecino en selección de contexto según requisito; comparte objetivos generales, pero mezcla grafo/retrieval y no aísla documentación enlazada a APIs fijas. No asumir compatibilidad técnica con RepoScope.

## Riesgos
La asistencia LLM al grafo y la vista de código permitida requieren auditoría temporal/fuga; las ganancias dependen de los baselines y coste del preprocesamiento.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| DyCoder/DyRetriever con puntos de entrada, grafo parcial multi-hop y similitud. | Extracción del paper | Abstract/Method, pp. 1–6 | Método reportado |
| Pass@1 +25.63%/+59.73% y 7.4× frente a baselines descritos. | Extracción del paper | Abstract/Results, pp. 1–3 | Resultado reportado |
| Evaluación en CoderEval/DevEval. | Extracción del paper | Evaluation, pp. 7–11 | Benchmarks reportados |

## Pendientes
Completar título y metadatos; cotejar tablas, definiciones de mejora, coste, accesibilidad del grafo y controles de fuga.
