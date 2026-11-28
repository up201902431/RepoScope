# RepoCoder

## Identidad
- **paper_id:** `repocoder` (ya utilizado en ficha existente; conservar, sin asignación nueva).
- **Título:** *RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation*.
- **Autores:** Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou y Weizhu Chen.
- **Año/venue:** EMNLP 2023, pp. impresas 2471–2484; DOI `10.18653/v1/2023.emnlp-main.151`; arXiv `2303.12570` citado en trabajo relacionado.
- **Fuente de este lote:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/RepoCoder.md`; PDF homónimo bajo `research/papers/pdf/Same Solution/secondary/`.
- **Registro canónico:** esta nota cubre ambas copias locales del mismo artículo/DOI: `Same Solution/secondary/RepoCoder.md` y `Other/diss prop bibl/RepoCoder.md`. La segunda ruta contiene una referencia de alias; las clasificaciones fuente no se modifican.
- **Cobertura:** Markdown completo, 14 páginas físicas; portada, Fig. 3 y Tablas 2–3 cotejadas visualmente. El PDF no se inspeccionó página por página.
- **Grupo/etiquetas:** Same Solution / secondary como ubicación canónica de la ficha; la clasificación `Other/diss prop bibl` se conserva en las fuentes y se referencia como alias.

## Pregunta y contribución
**Hecho:** RepoCoder alterna recuperación por similitud y generación; la predicción anterior pasa a formar parte de la consulta siguiente. Introduce RepoEval para line, API invocation y function-body completion.

**Interpretación:** antecedente directo de recuperación contextual; no evalúa documentación humana/generada ni selección semántica de documentos por requisito.

## Método
- **Entrada/salida:** código incompleto in-file y fragmentos recuperados → línea, invocación API o cuerpo.
- **Unidad/contexto:** ventanas deslizantes de líneas contiguas del repositorio.
- **Recuperación:** sparse token/Jaccard; también UniXcoder denso. En iteraciones posteriores consulta combina parte del código incompleto y prefijo de predicción anterior.
- **Generación:** GPT-3.5-Turbo y CodeGen 6B/2B/350M; Oracle usa parte del ground truth y es un límite idealizado.

## Documentos y arquitectura
Contexto recuperado es código, no documentación; no modela arquitectura documental o historial.

## Evaluación
- **Benchmark:** RepoEval, Python; 1.600 ejemplos line, 1.600 API y 373 function-body, distribuidos en conjuntos de repositorios según tarea.
- **Métricas:** EM, Edit Similarity y Pass Rate por tests.
- **Resultados:** Tabla 3 informa en function-body con GPT-3.5-Turbo Pass Rate 42,63% para RepoCoder de dos iteraciones frente a 23,32% In-File y el mismo valor del Oracle. Tabla 2 desglosa line/API por modelo/iteraciones; iteraciones adicionales no siempre ayudan.
- **Límites:** poca duplicación reduce beneficio; número de iteraciones difícil de elegir y posteriores pueden degradar resultado; coste/latencia; modelos/prompts/retrievers explorados de forma limitada; ejemplos engañosos y predicciones previas ruidosas.

## Artefactos
El artículo declara código y benchmark en `github.com/microsoft/CodeT/tree/main/RepoCoder`; no se comprobó acceso, contenido, versión, licencia ni ejecución.

## Relación con nuestra tesis
Puede servir como antecedente/comparador metodológico en recuperación iterativa. No sustituye el baseline RepoScope ni responde a la intervención documental enlazada a APIs y requisito.

## Riesgos
No comparar resultados entre benchmark/configuraciones como causalidad general. Oracle no es un método desplegable; Pass Rate no equivale a API P/R/F1.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad y publicación | Portada | 1 (2471) | Hecho |
| Ventanas y consulta iterativa | Markdown; §§II.1–2.2, Fig. 3 | 2–3 (2472–2473) | Hecho |
| RepoEval, filtros y métricas | Markdown; §§III–IV | 4–5 (2474–2475) | Hecho |
| Resultados line/API y cuerpo | Markdown; Tablas 2–3; rasters revisados | 6 (2476) | Hecho reportado |
| Existencia de nota con misma identidad | Ficha Other con DOI/artículo concordante | No aplica | Duplicado cotejado |
| Relevancia documental | Brief frente al método | No aplica | Interpretación |

## Pendientes
No verificar artefactos ni volver a contar esta misma publicación como paper único sin considerar la ficha previa.
