# A³-CodGen

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador de trabajo provisional: `A3-CodGen`.
- **Título:** *A³-CodGen: A Repository-Level Code Generation Framework for Code Reuse With Local-Aware, Global-Aware, and Third-Party-Library-Aware*.
- **Autores:** Dianshu Liao, Shidong Pan, Xiaoyu Sun, Xiaoxue Ren, Qing Huang, Zhenchang Xing, Huan Jin y Qinying Li.
- **Año/venue:** IEEE *Transactions on Software Engineering*, vol. 50, n.º 12, diciembre de 2024, pp. impresas 3369–3384. DOI `10.1109/TSE.2024.3486195`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/A3-CodGen.md`; PDF: `research/papers/pdf/Same Solution/primary/A3-CodGen.pdf`.
- **Procedencia/cobertura:** el informe del lote declara lectura íntegra del Markdown extraído. Se contrastaron visualmente páginas/PNG locales 1, 9, 11 y 12; no se inspeccionó visualmente el PDF completo. Extracción declarada automática y no verificada manualmente.
- **Grupo/etiquetas:** se conserva `Same Solution/primary`; no se infiere aprobación formal.

## Pregunta y contribución
**Hecho del paper:** estudia reutilización de información local, global y de bibliotecas de terceros en generación de código de repositorios; propone A³-CodGen y el benchmark RepoEval.

**Interpretación:** aborda conocimiento del repositorio y reutilización, no la selección de documentación explícitamente vinculada a APIs según requisito.

## Método
- **Entrada/salida/tarea:** requisito/comentario del desarrollador y contexto del archivo; salida, función Python generada.
- **Conocimiento local:** funciones del módulo actual, atributos de instancia, variables del módulo y nombre completo del módulo (FQN).
- **Recuperación global:** genera una función “what-if” para recuperar funciones candidatas por similitud semántica/código; fusiona candidatos y pasa FQN, firma y resumen.
- **Bibliotecas:** extrae nombres de bibliotecas de sentencias `import`; no incluye su código.
- **Generación:** prompt estructurado con conocimiento local, global y de terceros, más secuencia de instrucciones/CoT.
- **Granularidad/dependencias:** unidad funcional Python; genera resúmenes de funciones con GPT-3.5 para mejorar la recuperación.

## Documentos y arquitectura
Los resúmenes generados son representaciones de funciones para recuperación, no documentos finales. No genera documentación de arquitectura ni establece enlaces de procedencia documento→API. No se reporta selección de documentos por requisito.

## Evaluación
- **Benchmark/selección:** RepoEval se construye a partir de 29 repositorios Python de PyPI; 383 funciones se seleccionan para evaluación manual tras los filtros descritos por los autores.
- **Métricas:** *reuse awareness* (Precision/Recall/F1 y Accuracy), corrección de reutilización, cobertura de bibliotecas y LOC. No son Pass@1 ni API F1 bajo el protocolo de tesis.
- **Resultados reportados:** Tabla III: añadir conocimiento de bibliotecas cambia F1 de awareness de 0,536 a 0,720 y cobertura de 0,875 a 0,940. Tabla IV: A³-CodGen con GPT-3.5-Turbo-16k obtiene F1 awareness local/global/terceros 0,694/0,606/0,720; con GPT-4o, 0,718/0,701/0,898.
- **Límites:** Python; los autores reconocen límites de anotación manual y control de versiones de dependencias. La selección temporal no demuestra ausencia de contaminación; el artículo indica que no controla versiones de bibliotecas en los experimentos.

## Artefactos
El artículo declara que réplica, datos, código y resultados se ofrecen en un repositorio enlazado desde la referencia [19]. No se comprobó disponibilidad, licencia, contenido ni reproducción.

## Relación con nuestra tesis
**Interpretación acotada:** comparte el uso de contexto y APIs para reutilización. Se distingue porque no vincula documentos humanos a APIs ni filtra esos documentos por requisito; sus resúmenes son representaciones de funciones.

## Riesgos
- Las métricas de awareness/corrección de reutilización no equivalen a corrección funcional por tests.
- No controlar versiones de dependencias introduce incertidumbre en la reproducibilidad.
- La selección temporal no prueba por sí sola ausencia de fuga de repositorios o datos.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Identidad y cita | PDF/Markdown; raster de portada | 1 | 3369 | Metadato |
| Diseño de A³-CodGen | PDF/Markdown local | 5–7 | 3373–3375 | Método |
| Benchmark y métricas | PDF/Markdown local | 8–9 | 3376–3377 | Evaluación |
| Tablas III y IV | PDF y raster local | 11–12 | 3379–3380 | Resultados reportados |

## Pendientes
Comprobar el repositorio y versiones de dependencias si se considera reutilizar el benchmark; mantener sus métricas separadas de las métricas de tesis.
