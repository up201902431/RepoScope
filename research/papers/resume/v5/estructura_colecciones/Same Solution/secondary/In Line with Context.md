# In Line with Context: Repository-Level Code Generation via Context Inlining

## Identidad
- **paper_id:** provisional `in-line-with-context`; sin ID canónico local.
- **Título:** *In Line with Context: Repository-Level Code Generation via Context Inlining*.
- **Autores:** Chao Hu, Wenhao Zeng, Yuling Shi, Beijun Shen y Xiaodong Gu.
- **Año/venue:** 2026, *Proceedings of the ACM on Software Engineering*, vol. 3, FSE, artículo FSE066; DOI `10.1145/3797094`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/In Line with Context.md`; PDF homónimo.
- **Versión/procedencia:** PDF local de 23 páginas físicas; portada y páginas de tablas/figuras selectas cotejadas con rasters. Sin checksum.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo; revisión visual selectiva de páginas 1, 12, 14 y 16. No inspección integral del PDF.
- **Alias:** InlineCoder es el framework del artículo, no un título/artículo independiente. CodePlan, DRACO y GraphCoder aparecen como trabajos relacionados y son publicaciones distintas.

## Pregunta y contribución
**Hecho:** InlineCoder completa cuerpos de funciones usando contexto inlined en ambas direcciones: borradores en llamadores (upstream) y funciones llamadas (downstream).

**Interpretación:** aporta una forma de ampliar contexto de generación, pero su contexto son cuerpos y llamadas de código, no documentos asociados a APIs.

## Método
- **Entrada/salida:** firma y descripción de tarea → cuerpo completo de función.
- **Flujo:** genera un borrador (anchor) y lista de llamadas; inserta borrador en llamadores con sustitución de parámetros, normalización de retorno y redirección de asignación; recupera funciones downstream llamadas; combina contextos, borrador e información de tarea en prompt final.
- **Confianza:** perplejidad del borrador con Qwen2.5-Coder-1.5B y tres niveles; downstream usa llamadas AST/LLM y coincidencia de nombres por subcadena.
- **Backbones:** DeepSeek-V3, Qwen3-Coder y GPT-5-mini.

## Documentos y arquitectura
No produce o recupera documentación ni modelos arquitectónicos. Contexto derivado de llamadas, borrador y funciones/repositorio.

## Evaluación
- **Benchmarks:** DevEval (1.825 muestras Python, 115 repositorios) y RepoExec (355 funciones Python).
- **Métricas/comparadores:** EM, ES, BLEU e ID.F1; In-File, Vanilla, RepoCoder, DRACO, GraphCoder e InlineCoder. No emplea Pass@k.
- **Resultados localizables:** el artículo informa mejoras relativas medias frente al baseline más fuerte: DevEval 5,13%/10,86%/10,67% en EM/ES/BLEU; RepoExec 29,73%/20,82%/49,34%. Tablas 1–2 en PDF p. 12, cotejadas visualmente; ablaciones en p. 13.
- **Incidencia visual:** Fig. 7, p. 16, parece mostrar `parsed = {}` y luego `parsed = values[0]` antes de `return parsed`, en tensión con el texto que afirma retorno de tipo dict. No se resolvió si es errata, render/extracción o discrepancia del ejemplo; no usarla como prueba concluyente.
- **Límites:** evaluación descrita para Python; uso de borrador y recuperación por nombres; extensión a otros lenguajes no evaluada.

## Artefactos
El artículo declara código/datos en `github.com/ythere-y/InlineCoder`. No se comprobaron accesibilidad, contenido, versión, licencia del software ni ejecución. El artículo indica CC BY-NC-ND para publicación, que no debe confundirse con licencia de software.

## Relación con nuestra tesis
Puede orientar contexto bidireccional de función, pero requiere rediseño para vincular documentos a APIs recuperadas y seleccionarlos por requisito. No reemplaza RepoScope ni prueba la hipótesis documental.

## Riesgos
La anomalía visual de Fig. 7 sigue pendiente; los resultados no equivalen a Pass@1/API P/R/F1 del protocolo. No inferir causalidad entre cifras de distintos trabajos.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---:|---|
| Identidad, autores y DOI | Markdown y raster de portada | 1 | Hecho, cotejado visualmente |
| Context inlining y pipeline | Markdown; §§3–4 | 4–11 | Hecho |
| Resultados DevEval/RepoExec | Markdown; Tablas 1–2; rasters revisados | 12 | Hecho reportado |
| Ablaciones y ejemplos | Markdown; Tablas 3–4 y Fig. 7 | 13–16 | Hecho reportado; Fig. 7 con discrepancia |
| Límites y disponibilidad anunciada | Markdown; §§6–7 | 18–19 | Hecho reportado |
| Pertinencia para documentación API | Brief frente al método | No aplica | Interpretación |

## Pendientes
Resolver la Fig. 7 con versión/suplemento; comprobar artefactos solo con autorización.
