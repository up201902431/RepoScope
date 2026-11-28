# AllianceCoder

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador provisional: `AllianceCoder`.
- **Título:** *What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond*.
- **Autores:** Wenchao Gu, Juntao Chen, Yanlin Wang, Tianyue Jiang, Xingzhe Li, Mingwei Liu, Xilin Liu, Yuchi Ma y Zibin Zheng.
- **Versión verificable:** `arXiv:2503.20589v1`, 26-mar-2025. No se verifica venue ni DOI: la copia conserva metadatos de plantilla (“Conference acronym ’XX” y DOI marcador).
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/AllianceCoder.md`; PDF: `research/papers/pdf/Same Solution/primary/AllianceCoder.pdf`.
- **Procedencia/cobertura:** el informe del lote declara lectura íntegra del Markdown extraído; se inspeccionaron raster locales de páginas físicas 1 y 9. El PDF completo no se revisó visualmente. La paginación impresa no es fiable en la plantilla.
- **Grupo/etiquetas:** se conserva `Same Solution/primary`; esto no afirma aprobación formal.

## Pregunta y contribución
**Hecho del paper:** estudio empírico sobre qué recuperar (contexto, APIs, fragmentos similares) y propuesta AllianceCoder, que recupera APIs mediante descripciones semánticas.

**Interpretación:** aporta una estrategia de recuperación de APIs, no un método de documentación ni de enlace requisito-documento.

## Método
- **Entrada/salida/tarea:** requisito de generación, contexto del archivo y APIs candidatas; salida, función de repositorio.
- **Recuperación:** genera descripciones en lenguaje natural para APIs; descompone el requisito en pasos; produce y amplía descripciones de APIs potenciales; codifica y recupera por similitud coseno una API por descripción.
- **Generación/granularidad:** añade APIs recuperadas al contexto y requisito y genera una función. Opera a nivel de API/función.
- **Modelos:** el artículo informa GPT-4o Mini y Gemini 1.5 Flash a temperatura 0,7; UniXcoder como modelo de representación.
- **Documentación:** son descripciones sintéticas generadas desde código, no documentación humana ni de arquitectura.

## Documentos y arquitectura
Las descripciones de APIs son artefactos generados para recuperación. No se reportan File-Doc/Module-Doc, documentación arquitectónica ni enlaces de procedencia documento→API.

## Evaluación
- **Benchmarks:** CoderEval y RepoExec. El documento describe estudio preliminar con acceso “oracle” a información ideal y comparaciones entre contexto, API y fragmentos similares.
- **Métricas/protocolo:** Pass@1/3/5; cada caso se repite cinco veces según la discusión de validez.
- **Resultados reportados:** Tabla 4: AllianceCoder-GPT obtiene Pass@1 34,93 en RepoExec y 36,52 en CoderEval; AllianceCoder-Gemini, 35,49 y 24,78. El texto comunica hasta 20% de mejora relativa de Pass@1; depende del conjunto/modelo de comparación y es una afirmación de los autores.
- **Límites:** posible contaminación de benchmarks por preentrenamiento; calidad de descripciones generadas; la cantidad de APIs recuperadas puede ser excesiva. El paper señala baja recall de API aun cuando generación mejora. No se determinó completamente la composición lingüística de cada subconjunto.

## Artefactos
El paper anuncia un paquete de réplica en `https://anonymous.4open.science/r/AllianceCoder`. No se comprobó accesibilidad, contenido, licencia ni reproducción.

## Relación con nuestra tesis
**Interpretación acotada:** antecedente útil para recuperación de APIs condicionada por un requisito descompuesto. La descripción de API la genera el propio trabajo desde código; no enlaza documentación humana ni selecciona documentos vinculados explícitamente a las APIs recuperadas.

## Riesgos
- Metadatos editoriales de plantilla: no citar como publicación ACM confirmada.
- Posible contaminación de datos/modelos y dependencia de la calidad de descripciones sintéticas.
- La configuración “oracle” no debe confundirse con un sistema sin acceso privilegiado.
- No se verificó la exclusión del objetivo/derivados en la creación de descripciones.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---|---|
| Título, autores y versión arXiv | PDF, Markdown y raster de portada | 1–2 | No fiable por plantilla | Metadato |
| Diseño experimental y modelos | PDF/Markdown local | §§3–4, 6.1–6.4; 7–8 | No fiable por plantilla | Método |
| Tabla 4 y Tablas 5–7 | PDF y raster local | 9 | No verificable | Resultados reportados |
| Validez/limitaciones | Markdown local | 12 | No verificable | Amenazas reportadas |

## Pendientes
Verificar versión bibliográfica y paquete en una comprobación autorizada; precisar idiomas y política de acceso oracle; inspeccionar visualmente páginas no revisadas.
