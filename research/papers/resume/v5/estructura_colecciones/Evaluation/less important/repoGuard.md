# RepoGuard

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoGuard`.
- **Título:** *Harmonising Security and Functional Correctness in LLM-Guided Repository-Level Code Generation*.
- **Autores/año/venue:** Cassiano Darif Zago et al.; ICICT 2026. DOI `10.1145/3803291.3803376`.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/less important/repoGuard.md`; PDF `research/papers/pdf/Evaluation/less important/repoGuard.pdf`.
- **Grupo:** se conserva `Evaluation/less important`.
- **Cobertura:** Markdown íntegro según informe; Tabla 3 cotejada visualmente en página seleccionada. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** arquitectura para armonizar seguridad y corrección funcional en generación guiada por LLM a nivel de repositorio.

**Interpretación:** ejemplo de reparación y validación; no evalúa documentación ni enlaces arquitectónicos.

## Método
Pipeline Python: recuperación de contexto AST, Qwen2.5-Coder 7B local, Auto-Importer, escáneres SAST y tests en ciclo RCI. Evalúa siete casos derivados de especificaciones OWASP/CWE y un caso sintético multi-CWE.

## Documentos y arquitectura
Opera sobre código, contexto AST, pruebas y reglas de seguridad; no genera documentación ni selecciona documentos vinculados a APIs.

## Evaluación
Mide éxito funcional y seguridad mediante tests/SAST, convergencia, iteraciones y tiempo. Reporta dos regresiones del baseline en siete casos y 7/7 para RepoGuard. No informa variación por repeticiones ni comparación amplia de repositorios.

## Artefactos
El paper declara código/dataset en GitHub. No se verificaron disponibilidad, licencia, contenido ni ejecución.

## Relación con nuestra tesis
Puede informar el control de validación/seguridad, pero su suite controlada no es benchmark directo para medir enriquecimiento documental.

## Riesgos
Los autores reconocen que el dataset controlado no representa repositorios empresariales complejos. “OWASP Top 10” no implica cobertura exhaustiva: la tabla contiene siete casos. La comparación debe aislar Auto-Importer, SAST y ciclo de reparación.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Arquitectura y setup | PDF/Markdown local | §§3–4.3, 3–8 | 380–385 | Método |
| Tabla 3, resultados | PDF y raster local | 7 | 384 | Resultado; cotejo visual |
| Límites | PDF/Markdown local | Conclusión | Dentro del rango 3–8 | Limitación reportada |

## Pendientes
Verificar artefactos y ampliar evidencia antes de extraer una conclusión sobre generalización o seguridad.
