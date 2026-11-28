# DevEval

## Identidad
- **paper_id:** no asignado; identificador local provisional `DevEval`.
- **Título:** *A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories*.
- **Autores/año/venue:** Jia Li et al.; Findings of ACL 2024, pp. impresas 3603–3614.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/primary/DevEval.md`; PDF `research/papers/pdf/Evaluation/primary/DevEval.pdf`.
- **Grupo:** `Evaluation/primary`, sin afirmar aprobación formal.
- **Cobertura:** lectura íntegra del Markdown declarada por el informe de lote; tabla de resultados seleccionada cotejada con raster local. PDF completo no inspeccionado visualmente.

## Pregunta y contribución
**Hecho:** benchmark de generación de código alineado con repositorios reales y requisitos anotados manualmente.

**Interpretación:** antecedente directo para generación con contexto; no fija por sí solo el protocolo de evaluación de tesis.

## Método
1.825 tareas Python de 115 repositorios, filtradas desde 500 repositorios; 13 desarrolladores anotaron requisitos y dependencias. Se excluyeron casos sin tests ejecutables y tareas consideradas triviales/no admisibles. Evalúa función en repositorio con condiciones sin contexto, archivo local en completion e infilling.

## Documentos y arquitectura
La anotación incluye requisitos y dependencias; el trabajo no genera documentación arquitectónica ni evalúa selección de documentos enlazados a APIs.

## Evaluación
Ocho modelos, incluidos GPT-4, GPT-3.5, StarCoder 2, DeepSeek Coder y CodeLLaMa. Pass@k usa estimador no sesgado; k=1 con greedy. Recall@k es el máximo, entre k programas, de la fracción de dependencias de referencia recuperadas por parser estático; no es P/R/F1 ni juicio absoluto de API válida. Tabla principal: GPT-4 con infilling, Pass@1 53,81 % y Recall@1 65,42 %; sin contexto, Pass@1 17,00 %. Recall puede subestimar dependencias dinámicas; el artículo informa sesgo medido de 0,16 en la prueba descrita.

## Artefactos
El artículo declara benchmark, prompts y predicciones publicados; disponibilidad, licencia, contenido y reproducción no comprobados.

## Relación con nuestra tesis
Benchmark relevante, pero hay que distinguir tareas de desarrollo de evaluación y auditar solapamientos, repositorios vistos por modelos, callers/callees y derivados. Recall@k no debe presentarse como API F1.

## Riesgos
Monolingüe; contexto adicional limitado a archivos locales. La existencia de anotación manual no demuestra ausencia de contaminación por repositorios ni por modelos.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Corpus/protocolo | PDF/Markdown local | §§2.3–4.4 | 3605–3612 | Método |
| Resultados principales | PDF y raster local | 6 (rango revisado 3–10) | 3608 | Tabla 5, cotejo visual |
| Limitaciones | PDF/Markdown local | §5 y limitaciones | 3605–3612 | Amenazas reportadas |

## Pendientes
Verificar artefactos y mapear tareas/repositorios/commits al protocolo propio antes de seleccionar una muestra.
