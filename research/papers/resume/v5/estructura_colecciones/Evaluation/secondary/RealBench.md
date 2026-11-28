# RealBench

## Identidad
- **paper_id:** no asignado; identificador local provisional `RealBench`.
- **Título:** *A Repo-Level Code Generation Benchmark Aligned with Real-World Software Development Practices*.
- **Autores/año/venue:** Jia Li et al.; Proc. ACM Software Engineering, FSE078, julio de 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/RealBench.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, ubicación original.
- **Cobertura:** lectura íntegra del Markdown declarada; Tabla 5 contrastada con raster local. PDF completo no inspeccionado visualmente.

## Pregunta y contribución
**Hecho:** benchmark para generación de repositorios Python desde requisitos y UML, con comparación de estrategias de construcción/contextualización.

**Interpretación:** evalúa especificaciones de alto nivel; no selecciona documentos vinculados a APIs recuperadas.

## Método
Corpus de 61 repositorios según resumen retenido. Compara estrategias holistic, incremental y RAG; seis modelos; decoding greedy y una solución por tarea. UML es entrada estructurada.

## Documentos y arquitectura
Incluye requisitos y modelos UML. Un diseño UML no equivale a documentación API vinculada ni prueba procedencia de documentos.

## Evaluación
Requirement@1 y Architecture@1 son puntuaciones humanas de 0–4 para requisitos/diseño; Completion rate, Execution pass rate y Test pass rate miden aspectos distintos. Mejor promedio reportado: Completion 91,18 %, Execution pass 45,00 %, Test pass 19,39 %, Requirement@1 2,29 y Architecture@1 2,67. No son un único indicador de corrección.

## Artefactos
Disponibilidad no verificada en el informe de lote; no se ejecutó el benchmark.

## Relación con nuestra tesis
Antecedente para considerar arquitectura como entrada, pero no demuestra efecto de documentación asociada a APIs recuperadas.

## Riesgos
Evaluación de requisitos/arquitectura incorpora revisión humana y coste. Los resultados de generación, ejecución y juicio humano no deben colapsarse en una métrica única.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Corpus/setup y estrategias | PDF/Markdown local | §§3.2–4.1, 9–12 | FSE078:9–12 | Método |
| Tabla 5 | PDF y raster local | 12 | FSE078:12 | Resultado; cotejo visual |

## Pendientes
Verificar datos/artefactos y protocolos de evaluación humana si se reutilizan instrumentos o tareas.
