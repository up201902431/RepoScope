# CodePlan

## Identidad
- **paper_id:** provisional `codeplan`; sin ID canónico local.
- **Título:** *CodePlan: Repository-Level Coding using LLMs and Planning*.
- **Autores:** Ramakrishna Bairi, Atharv Sonwane, Aditya Kanade, Vageesh D. C., Arun Iyer, Suresh Parthasarathy, Sriram Rajamani, B. Ashok y Shashank Shet.
- **Año/venue:** 2024, *Proceedings of the ACM on Software Engineering*, vol. 1, FSE, artículo 31; DOI `10.1145/3643757`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/CodePlan.md`; PDF homónimo en `research/papers/pdf/Same Solution/secondary/`.
- **Versión/procedencia:** PDF local de 24 páginas físicas; portada y Tabla 3 cotejadas visualmente. Sin comprobación de preprint o checksum.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** lectura completa del Markdown, incluidas referencias; revisión visual selectiva de páginas 1 y 13. No inspección visual página por página.

## Pregunta y contribución
**Hecho:** CodePlan coordina ediciones de código a nivel repositorio mediante planificación adaptativa, análisis de dependencias e interacción iterativa con un LLM y un oráculo.

**Interpretación:** puede aportar ideas sobre dependencias y propagación de cambios, pero la unidad es una obligación de edición, no un documento asociado a un API.

## Método
- **Entrada/salida:** repositorio, instrucciones o ediciones semilla, oráculo y LLM → ediciones coordinadas.
- **Unidad/contexto:** bloques de código y grafo de dependencias; contexto espacial (código relacionado) y temporal (ediciones previas).
- **Proceso:** análisis incremental, análisis de impacto potencial, planificación adaptativa, aplicación de cambios y uso de oráculo para proponer nuevas semillas cuando persisten errores.
- **Tareas/lenguajes:** migraciones C# y ediciones temporales Python.

## Documentos y arquitectura
No produce ni recupera documentación. El contexto es código y ediciones previas; el artículo no evalúa arquitectura documental o selección por requisito.

## Evaluación
- **Datos:** migraciones C# en repositorios internos y públicos; ediciones temporales Python en tres repositorios públicos.
- **Oráculos/métricas:** build para C#; Pyright/Pyright Strict para Python; bloques coincidentes/omitidos/espurios, DiffBLEU, distancia Levenshtein y validez compuesta (superar el oráculo y coincidir con target salvo formato/espacios).
- **Resultados localizables:** Tabla 3 reporta 5/7 repositorios que pasan la comprobación compuesta con CodePlan y ninguno de los baselines de reparación guiada por oráculo (PDF p. 13). Algunas filas Python fallan aunque no tengan errores Pyright porque el resultado no coincide con el target.
- **Límites:** el artículo señala limitaciones de análisis estático, dependencias dinámicas y cobertura de tareas/lenguajes/repositorios; la validez depende también de coincidencia con target, no es Pass@1 de generación de funciones.

## Artefactos
El artículo declara datos, scripts y material suplementario en `github.com/microsoft/codeplan`, excluyendo dos repositorios propietarios. Disponibilidad actual, licencia, versión y ejecución no comprobadas.

## Relación con nuestra tesis
Referencia periférica para dependencias/cambios. No evalúa documentos enlazados a APIs, ni seleccionados según requisito, ni la comparación central RepoScope vs. módulo documental.

## Riesgos
No presentar los 5/7 como resultado comparable a pass rate de benchmark distinto o como efecto causal aislado del componente de planificación.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Título, autores, FSE y DOI | Markdown y raster de portada | 1 (31:1) | Hecho, cotejado visualmente |
| Grafo de dependencias y planificación | Markdown; §§1–2.3 | 2–10 | Hecho |
| Diseño y tareas | Markdown; §§3.2–4.1 | 11–14 | Hecho |
| Resultado de validez compuesta | Markdown; Tabla 3; raster revisado | 13 | Hecho reportado |
| Límites | Markdown; §5 | 18–19 | Hecho reportado |
| Diferencia frente a documentación seleccionada | Brief de tesis frente a tarea | No aplica | Interpretación |

## Pendientes
No se comprobaron los artefactos ni los repositorios externos.
