# Beyond Maintenance

## Identidad
- **paper_id:** no asignado; identificador local provisional por nombre de archivo.
- **Título:** *Beyond Maintenance: A Benchmark and Multi-Agent Framework for Repository-Usage Code Generation*.
- **Autores/año/venue:** Kaitao Lin et al.; SIGIR 2026. DOI `10.1145/3805712.3808589`.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/Beyond Maintenance.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, ubicación preservada.
- **Cobertura:** lectura íntegra del Markdown declarada; Tablas 2–4 visualizadas en página física 6. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** RUCCE evalúa cómo un usuario externo encuentra APIs internas y compone scripts ejecutables; RUCACoder combina Retriever, Verifier y Coder. No es mantenimiento del código base.

**Interpretación:** relevante para separar recuperación de APIs de generación posterior.

## Método
Usuario/requisito de uso de repositorio → recuperación de APIs internas, verificación y composición de script ejecutable. La tarea es uso externo del repositorio.

## Documentos y arquitectura
No se reporta generación documental ni documentación arquitectónica como intervención central; el foco es API interna y scripts.

## Evaluación
Recuperación: Precision@k/Recall@k respecto a APIs de referencia. Generación: API Reuse Rate y RepoNativeScore; este último promedia tres jueces LLM. Se reportan mejoras en subconjuntos Easy/Medium/Hard; el desempeño varía por dificultad y backbone. Métricas de recuperación expresan alineación con referencia, no juicio absoluto de todas las APIs válidas.

## Artefactos
Dataset/código declarados en Hugging Face; no se verificaron disponibilidad, licencia, contenido ni reproducción.

## Relación con nuestra tesis
Antecedente útil para congelar APIs recuperadas y separar recuperación de generación en el diseño experimental. No equivale al aporte documental.

## Riesgos
Jueces LLM introducen incertidumbre; no es benchmark de cambio documental. No comparar sus métricas de reutilización directamente con API F1 sin definición común.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Tarea/RUCACoder | PDF/Markdown local | §§5.1–5.4, físicas 5–6 | 3296–3297 | Método |
| Tablas 2–4 | PDF y raster local | 6 | 3297 | Resultados; cotejo visual |

## Pendientes
Verificar dataset, código y jueces; estudiar compatibilidad de las APIs de referencia con la definición operativa de la tesis.
