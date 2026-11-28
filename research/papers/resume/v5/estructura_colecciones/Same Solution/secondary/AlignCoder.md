# AlignCoder

## Identidad
- **paper_id:** provisional `aligncoder`; sin ID canónico local.
- **Título:** *AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion*.
- **Autores:** Tianyue Jiang, Yanli Wang, Yanlin Wang, Daya Guo, Ensheng Shi, Yuchi Ma, Jiachi Chen y Zibin Zheng.
- **Año/venue:** ASE 2025; DOI `10.1109/ASE63991.2025.00085`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/AlignCoder.md`; PDF homónimo en `research/papers/pdf/Same Solution/secondary/`.
- **Versión/procedencia:** PDF local de 12 páginas físicas; portada y páginas seleccionadas cotejadas con rasters locales. No se verificó preprint ni checksum.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown íntegro, incluidas referencias; cotejo visual selectivo de páginas físicas 1, 5, 8 y 9. No inspección visual página por página.

## Pregunta y contribución
**Hecho:** AlignCoder busca alinear recuperación con la intención del objetivo en completion de código a nivel de repositorio. AlignRetriever es el recuperador entrenado; no es un paper distinto.

**Interpretación:** su recuperación sensible a intención puede ser antecedente metodológico, pero cambia el recuperador y no añade documentos asociados a APIs recuperadas.

## Método
- **Entrada/salida/tarea:** fragmento incompleto y repositorio → completion de código.
- **Unidad/contexto:** fragmentos de código candidatos y dependencias del repositorio; no documentos API.
- **Recuperación:** BM25 obtiene candidatos gruesos; un sampler produce completions que enriquecen la consulta para recuperación fina. Un evaluador por perplexity genera señal de recompensa para entrenamiento de AlignRetriever.
- **Generación:** el generador recibe los fragmentos recuperados y produce el completion.
- **Dependencias:** retriever entrenado, sampler, métrica de perplexity y LLM generador.

## Documentos y arquitectura
El contexto es código, firmas y dependencias extraídas; no documentación redactada, diagramas o arquitectura. No selecciona documentos usando un requisito en lenguaje natural.

## Evaluación
- **Benchmarks/idiomas:** CrossCodeEval (Python y Java) y RepoEval (line-level y API invocation); cinco backbones.
- **Métricas:** Exact Match y Edit Similarity.
- **Resultados localizables:** el artículo informa hasta 18,1% de mejora relativa en EM de CrossCodeEval Python frente a RLCoder (resumen, PDF p. 1); la Tabla I por modelo está en p. 8. La magnitud depende de la configuración/modelo y no debe generalizarse a todas las filas. Tablas II–III: ablaciones de dependencias, query enhancement y RL, p. 9.
- **Límites:** completion no equivale a resolución de issues ni a corrección funcional evaluada como en la tesis. EM/ES no son API P/R/F1. Cambiar retrieval se aparta de la comparación central con APIs fijas.

## Artefactos
El artículo afirma que código y datos están en `https://anonymous.4open.science/r/AlignCoder`. No se comprobó acceso, contenido, licencia, versión ni ejecución.

## Relación con nuestra tesis
Puede orientar una variante separada de recuperación sensible a intención, pero la pregunta de tesis trata selección de documentos vinculados explícitamente a las APIs que recupera el baseline. No sustituir RepoScope ni presentar el resultado publicado como evidencia del efecto documental.

## Riesgos
No equiparar métricas de completion con corrección funcional o alineación API del protocolo local. Comparaciones entre variantes cambian el componente de recuperación.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Título, autores, venue y DOI | Markdown; raster de portada | 1 (971) | Hecho, cotejado visualmente |
| Query enhancement y flujo coarse/fine | Markdown; Fig. 3 y §III | 5–6 (975–976) | Hecho |
| Dependencias y entrenamiento/recompensa | Markdown; §§III.A–C | 6–7 (976–977) | Hecho |
| Benchmarks y métricas | Markdown; §IV | 7 (977) | Hecho |
| Tabla principal y ablaciones | Markdown; Tablas I–III; rasters revisados | 8–9 (978–979) | Hecho reportado |
| Relevancia para selección documental | Brief de tesis frente al método | No aplica | Interpretación |

## Pendientes
La posible relación con versiones previas no se establece aquí; comprobar cualquier preprint solo con fuente autorizada. Artefactos no verificados.
