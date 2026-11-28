# CatCoder

## Identidad
- **paper_id:** provisional `catcoder`; sin ID canónico local.
- **Título:** *CatCoder: Repository-Level Code Generation with Relevant Code and Type Context*.
- **Autores:** Zhiyuan Pan, Xing Hu, Xin Xia y Xiaohu Yang.
- **Año/venue:** *ACM Transactions on Software Engineering and Methodology*, vol. 35, núm. 8, artículo 221, julio de 2026; DOI `10.1145/3779217`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/CatCoder.md`; PDF homónimo bajo `research/papers/pdf/Same Solution/secondary/`.
- **Versión/procedencia:** PDF de 25 páginas físicas; portada, método y tablas señaladas cotejadas con imágenes locales. No se verificó arXiv ni checksum.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown íntegro, incluidas referencias; revisión visual selectiva de portada, Fig. 1, Tabla 1, Tabla 5, Tabla 7 y materiales de escalabilidad. No inspección página por página.

## Pregunta y contribución
**Hecho:** CatCoder combina código recuperado y contexto de tipos para generar cuerpos de funciones en lenguajes estáticamente tipados.

**Interpretación:** el suministro de firmas y tipos es análogo al uso de información API, pero no equivale a recuperar documentación asociada a APIs según requisito.

## Método
- **Entrada/salida:** repositorio y función vacía, con docstring cuando existe → cuerpo de función.
- **Recuperación:** BM25 y búsqueda densa para fragmentos de código, fusionados por Reciprocal Rank Fusion.
- **Contexto tipado:** analizadores estáticos extraen campos y firmas de tipos relacionados; el alcance se limita a vecinos directos.
- **Generación:** el LLM congelado recibe fragmentos y contexto tipado y genera el cuerpo.
- **Dependencias:** parsers y análisis estático, retrievers, presupuesto del prompt y modelo generador.

## Documentos y arquitectura
El “type context” son tipos, campos y firmas derivados estáticamente, no documentación humana ni generada. No evalúa documentos de arquitectura.

## Evaluación
- **Benchmarks/idiomas:** Java, 199 tareas adaptadas de CoderUJB/Defects4J tras filtros; Rust, 90 tareas de RustEval, 13 crates.
- **Configuración/métricas:** CodeLlama-13B-Instruct en comparación principal, n=10, temperatura 0,6 y top_p=0,7; compile@k y pass@k con k=1,3,5.
- **Resultados localizables:** el artículo informa mejoras máximas de hasta 14,44% compile@k y 17,35% pass@k para Java, y 3,27%/6,68% para Rust; las Tablas 5 y 7 desglosan resultados y ablaciones (PDF pp. 13 y 16). No convertir máximos en promedio general.
- **Límites:** Java/Rust; análisis estático puede omitir reflexión y otros rasgos dinámicos. La evaluación de escalabilidad excluye latencia de inferencia del LLM y usa caché; el propio texto reconoce que contexto correcto no garantiza la lógica generada.

## Artefactos
El artículo anuncia código, benchmarks y scripts en `https://github.com/pan2013e/catcoder`. No se verificaron acceso, contenido, licencia, versión ni ejecución.

## Relación con nuestra tesis
Antecedente técnico próximo para estudiar cómo proporcionar información estructurada de APIs. Para la tesis habría que enlazar documentos a las APIs recuperadas y seleccionarlos por requisito, manteniendo fijo el baseline; CatCoder no hace esa comparación.

## Riesgos
No equiparar compile@k/pass@k con las métricas operativas aún incompletas del protocolo. La extracción estática y el alcance de lenguajes limitan generalización.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad, journal y DOI | Markdown; raster de portada | 1 | Hecho, cotejado visualmente |
| Flujo de retrieval y type context | Markdown; Fig. 1 y §3 | 4–9 | Hecho |
| Benchmarks y filtros | Markdown; §4.3 | 10–12 | Hecho |
| Resultados principales y ablación | Markdown; Tablas 5 y 7; rasters revisados | 13 y 16 | Hecho reportado |
| Escalabilidad/limitaciones | Markdown; §§5–6 | 17–21 | Hecho reportado |
| Correspondencia con la pregunta documental | Brief de tesis frente al método | No aplica | Interpretación |

## Pendientes
No se comprobó el artefacto externo ni su licencia.
