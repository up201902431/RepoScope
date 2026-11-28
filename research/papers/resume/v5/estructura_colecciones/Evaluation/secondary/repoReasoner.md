# RepoReasoner

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoReasoner`.
- **Título:** *Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models*.
- **Autores/año/venue:** Yanlin Wang et al.; Proc. ACM Software Engineering, FSE124, julio de 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/repoReasoner.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, preservado.
- **Cobertura:** lectura íntegra del Markdown declarada; tabla 3 cotejada visualmente en p. física 15. La extracción contiene un byte NUL que dificulta búsqueda normal; no se inspeccionó PDF completo.

## Pregunta y contribución
**Hecho:** evalúa razonamiento de modelos de contexto largo a nivel de repositorio.

**Interpretación:** mide predicción/comprensión de salidas y cadenas de llamadas, no generación de código ni calidad documental.

## Método
Dos tareas Python: 858 instancias de Output Prediction y 169 de Call Chain Prediction, de 14 repositorios; compara contexto oracle y recuperado, además de datos con I/O reescrito.

## Documentos y arquitectura
El material es código, entradas/salidas y cadenas/rutas de llamadas. No evalúa documentación enlazada a APIs.

## Evaluación
Pass@1/5 de Output Prediction usa coincidencia exacta con una salida aceptada; Call Chain F1 macro evalúa conjuntos de rutas/archivos por instancia y EM exige secuencia idéntica. Con oracle, DeepSeek-R1 alcanza Pass@1 0,691; al reescribir I/O baja a 0,650. Para cadenas se informa precisión relativamente alta y recall bajo; más contexto no siempre mejora por ruido.

## Artefactos
Se declara benchmark y pipeline; disponibilidad, licencia y ejecución no comprobadas.

## Relación con nuestra tesis
Útil para advertir sobre comprensión de dependencias y atajos de memorización; no es evaluación de corrección de código generado. Call Chain F1 no es API F1.

## Riesgos
Los contextos oracle y reescritura de I/O pueden alterar la dificultad. Definiciones de exactitud y macroagregación son específicas del benchmark.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Diseño y muestras | PDF/Markdown local | §§5.2–5.3, 13–16 | FSE124:13–16 | Método |
| Tabla 3 y efecto de I/O | PDF y raster local | 15 | FSE124:15 | Resultado; cotejo visual |

## Pendientes
Verificar pipeline/artefactos y revisar extracción alrededor del byte NUL antes de citar detalles no cubiertos por el informe.
