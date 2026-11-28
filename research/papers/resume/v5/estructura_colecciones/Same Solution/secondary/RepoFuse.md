# RepoFuse

## Identidad
- **paper_id:** provisional `repofuse`; sin ID canónico local.
- **Título:** *RepoFuse: A Dual-Context Approach to Repository-Level Code Completion at Industrial Scale*.
- **Autores:** Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Wei Jiang, Chengpeng Wang, Gang Fan y Peng Di.
- **Año/venue:** FSE Companion ’26, ACM, Montreal, 5–9 julio 2026; DOI `10.1145/3803437.3805230`; pp. impresas 568–579.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/RepoFuse.md`; PDF homónimo.
- **Versión/procedencia:** 12 páginas físicas; portada, figuras y tablas señaladas cotejadas con imágenes locales, no todas las páginas.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo con referencias; visuales selectivos pp. 1, 3, 6, 9 y 10.

## Pregunta y contribución
**Hecho:** RepoFuse combina contexto semántico del repositorio y fragmentos similares bajo presupuesto de tokens para completion.

**Interpretación:** la separación de tipos de contexto podría inspirar una ablación, pero RepoFuse no evalúa selección de documentación por requisito.

## Método
- **Semantic context:** entidades (firmas, clases/interfaces, módulos/paquetes) y relaciones derivadas de RSSG construido con AST, resolución de símbolos, inferencia de tipos y análisis de flujo.
- **Similar context:** código funcionalmente similar, mediante `crossfile_context` de CrossCodeEval y BM25, hasta cinco fragmentos.
- **Selección:** RCS/ODC combina candidatos bajo presupuesto con puntuaciones y estrategia greedy; incluye variantes semánticas, léxicas, aleatorias y Oracle.
- **Generación:** infilling con prefijo y sufijo; no solo contexto de prefijo de IDE.

## Documentos y arquitectura
Contexto semántico consiste principalmente en estructura y firmas de código; no genera documentos ni usa documentación requisito-API.

## Evaluación
- **Benchmarks/idiomas:** CrossCodeEval, Python y Java como comparaciones principales; además presenta TypeScript y C#.
- **Modelos/métricas:** DeepSeek-Coder y StarCoder de varios tamaños; EM, Edit Similarity, ID-F1 y speedup.
- **Resultados:** el artículo destaca incrementos EM de 4,26 para Python y 3,01 para Java; Tabla 2 contiene detalle por modelo/baseline (PDF p. 6), Tablas 2–4 pp. 6–7. No extrapolar.
- **A/B industrial:** abstract y sección de despliegue mencionan 80.000 solicitudes y 73% de participantes que reportan menor cambio de contexto; Tabla 6 suma 546.753 solicitudes entre cuatro filas. Se habla de 5.000 y 10.000+ desarrolladores y períodos de una semana/un año sin reconciliar ámbitos. Tabla expresa aceptación relativa (1,12×, 1,10×, 1,18×), no tasa absoluta.
- **Límites:** análisis estático ante reflexión/metaprogramación, dependencia de puntuación; EM/ID-F1 no miden por completo productividad. El texto reconoce entorno controlado y supuesto idealizado de acceso completo al repositorio.

## Artefactos
El artículo anuncia código abierto en `github.com/codefuse-ai/RepoFuse`; acceso, contenido, versión, licencia y ejecución no comprobados.

## Relación con nuestra tesis
Puede inspirar separación semántico/ejemplar y selección bajo presupuesto, pero requiere enlazar documentos a APIs recuperadas, filtrarlos por requisito y registrar procedencia. No cambia el baseline ni constituye evidencia sobre la hipótesis central.

## Riesgos
No sintetizar cifras industriales como un único tamaño de estudio hasta reconciliar denominadores/periodos. Métricas y configuración no son intercambiables con RepoScope.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad, venue y DOI | Portada | 1 (568) | Hecho |
| Dual context y RSSG | Markdown; §§III.1–3.2, Figs. 2–3, Tabla 1 | 3 (570) | Hecho |
| RCS, presupuesto y método | Markdown; §III.3 | 4 (571) | Hecho |
| Resultados controlados | Markdown; §V.1, Tablas 2–4 | 6–7 (573–574) | Hecho reportado |
| Conteos industriales/aceptación | Markdown; §V.5, Tabla 6; raster revisado | 9 (576) | Hecho reportado, alcance no conciliado |
| Límites/despliegue | Markdown; §§VII–VIII | 10 (577) | Hecho |
| Adaptación a documentos de API | Brief frente al método | No aplica | Interpretación |

## Pendientes
Reconciliar conteos de A/B y despliegue; no comprobar enlaces externos sin autorización.
