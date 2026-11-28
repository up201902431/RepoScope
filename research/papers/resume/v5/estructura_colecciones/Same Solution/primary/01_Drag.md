# Dynamic Retrieval-Augmented Generation (DRAG)

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador de trabajo provisional: `01_Drag`.
- **Título:** *Dynamic Retrieval-Augmented Generation*.
- **Autores:** Anton Shapkin, Denis Litvinov, Yaroslav Zharov, Egor Bogomolov, Timur Galimzyanov y Timofey Bryksin.
- **Año/venue:** la copia identifica `arXiv:2312.08976v2`, fechado 20-feb-2024. No se verificó venue ni DOI.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/01_Drag.md`; PDF asociado: `research/papers/pdf/Same Solution/primary/01_Drag.pdf`.
- **Procedencia/cobertura:** el informe de lectura del lote declara lectura íntegra del Markdown extraído (10 páginas físicas). PDF y PNG locales de páginas físicas 1, 6 y 7 consultados; el PDF completo no fue inspeccionado visualmente. La extracción se atribuye a PyMuPDF y advierte que no está verificada manualmente.
- **Grupo/etiquetas:** se conserva la ubicación `Same Solution/primary`; esto no implica aprobación formal de la clasificación.

## Pregunta y contribución
**Hecho del paper:** propone DRAG para que el generador emita entidades disponibles como unidades, no solo copiando sus nombres desde texto de contexto. Presenta el método y datos para generación de código a nivel de proyecto.

**Interpretación:** el foco es recuperación e inserción de entidades nombradas durante la generación; no propone documentación ni selección de documentos por requisito.

## Método
- **Entrada/salida/tarea:** para generación Python a nivel de proyecto, entrada de función con firma y descripción/docstring; salida, cuerpo de función. Las entidades disponibles incluyen nombre de función y código completo como contenido.
- **Recuperación/generación:** el embedder codifica las entidades disponibles y sus vectores extienden el vocabulario del generador. El modelo puede seleccionar una entidad representada por un token. No hay recuperación tradicional separada previa a generar: puede exponerse el conjunto de entidades y el modelo decide cuáles emitir.
- **Unidad/granularidad:** función como entidad en código; también se estudian nombres de flags Bash y columnas/campos SQL.
- **Dependencias:** el artículo describe entrenamiento conjunto o de generador y conectores; no se ejecutó ni reprodujo aquí.
- **Documentación/arquitectura:** no genera documentación ni diagramas. En otros dominios usa documentación de flags/schema como representación de entidades.

## Documentos y arquitectura
El método opera principalmente con contenido de entidades del código. No describe procedencia documental por afirmación, enlaces documento→API ni filtrado de documentos según requisito. La documentación de flags/schema mencionada en tareas auxiliares no constituye generación de documentación de repositorio.

## Evaluación
- **Datos/selección:** el artículo informa un conjunto Python propio de aproximadamente 16.000 muestras de alrededor de 1.000 repositorios, separado por repositorio en proporción 80/10/10. Entre los criterios citados figuran repositorios posteriores al 01-ene-2022, funciones con docstring y llamadas intraproyecto.
- **Benchmarks/tareas:** generación de proyecto Python, NL2Bash y Spider text-to-SQL.
- **Métricas/modelos:** para Python reporta ChrF y recuperación de entidades; no es una evaluación funcional por tests en esa tabla. NL2Bash usa Exact Match y recall de entidades; Spider, EM y Execution Accuracy.
- **Resultados reportados:** Tabla 1, CodeGen-Mono-350M: `No + Prompt` 23,1 ChrF/0,07 recall; `RepoCoder + Prompt` 25,2/0,27; `All + DRAG` 38,5/0,35; `RepoCoder + DRAG` 40,0/0,48; `Oracle + DRAG` 42,1/0,74. También reporta `GPT-3.5 + RepoCoder + Prompt` 42,8/0,39. En Spider, T5 con `All + DRAG`: EM 63,9/recall 0,78; `Oracle + DRAG`: EM 80,8/0,97. Son cifras del paper, no reproducidas.
- **Límites:** ChrF y recall de nombres no prueban corrección funcional ni uso semánticamente correcto de la API. El artículo identifica que una entidad seleccionada no puede modificarse para concordar gramaticalmente.

## Artefactos
El paper dice que publicará dataset y código tras aceptación y que adjunta una muestra. No se comprobó disponibilidad actual, contenido, licencia ni reproducción. No se ejecutaron comandos.

## Relación con nuestra tesis
**Interpretación acotada:** aporta una alternativa conceptual para seleccionar/referenciar APIs del repositorio durante generación. No aborda documentación humana, enlace requisito-documento ni selección de documentación enlazada a APIs. No es una adaptación directa de RepoScope.

## Riesgos
- La separación por repositorio reduce contaminación entre particiones, pero la fecha de creación no demuestra por sí sola ausencia en datos de entrenamiento.
- Las métricas de similitud y recuperación no equivalen a corrección funcional.
- Queda por comprobar cómo se construyó la colección de entidades y si se excluyó el objetivo y sus derivados.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Identidad y versión arXiv | PDF local y raster de portada; Markdown local | 1 | 1 | Metadato del paper |
| Arquitectura DRAG y tarea | PDF/Markdown local | 2–4; figura en 3 | 2–4 | Método |
| Datos y separación reportada | PDF/Markdown local | 6–7 | 6–7 | Evaluación |
| Tablas de resultados 1–3 | PDF y raster local | 6–7 | 6–7 | Resultado reportado |

## Pendientes
Verificar bibliografía/artefactos desde fuentes autorizadas si se requiere, inspeccionar páginas no contrastadas visualmente y auditar la exclusión del objetivo antes de indexar entidades.
