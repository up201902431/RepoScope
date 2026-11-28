# RepoBench

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoBench`.
- **Título:** *Benchmarking Repository-Level Code Auto-Completion Systems*.
- **Autores/año/versión:** Tianyang Liu, Canwen Xu y Julian McAuley; arXiv `2306.03091v2`, 2023.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/repoBench.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, conservado.
- **Cobertura:** lectura íntegra del Markdown declarada; una página de resultados (física 7) visualizada. PDF completo no inspeccionado visualmente.

## Pregunta y contribución
**Hecho:** benchmark de sistemas de autocompletado a nivel de repositorio.

**Interpretación:** evalúa recuperación y completado de siguiente línea; no generación de función completa ni documentación.

## Método
Tres tareas para Python y Java: RepoBench-R (recuperación), RepoBench-C (siguiente línea) y RepoBench-P (pipeline de recuperación + completado).

## Documentos y arquitectura
El objeto es contexto/código de repositorio. No hay generación documental, arquitectura textual ni enlace requisito-documento-API.

## Evaluación
Accuracy@k en recuperación; EM y Edit Similarity para completado y pipeline. Agregados “All” se ponderan por tamaño de configuraciones, no necesariamente media macro equitativa. Las conclusiones dependen de variantes de contexto, lenguaje y modelo.

## Artefactos
No se verificó disponibilidad de artefactos externos ni reproducción.

## Relación con nuestra tesis
Antecedente para recuperación cross-file y contexto; no trasladar sus métricas como evidencia de mejora en Pass@1 o API P/R/F1.

## Riesgos
EM/Edit Similarity no equivalen a corrección funcional por tests. Agregados ponderados pueden ocultar el efecto de configuraciones de distinto tamaño.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Tareas y métricas | PDF/Markdown local | §§3–4, 5–7 | No indicada en informe retenido | Método |
| Resultados RepoBench-C | PDF y raster local | Tabla 1–4; página física 7 | 7 visible en imagen | Resultado; cotejo visual |

## Pendientes
Verificar artefactos y revisar si la evaluación de recuperación es útil para una comparación secundaria, sin confundir objetivos.
