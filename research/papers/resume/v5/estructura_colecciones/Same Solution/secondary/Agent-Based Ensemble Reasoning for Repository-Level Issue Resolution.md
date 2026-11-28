# Agent-Based Ensemble Reasoning for Repository-Level Issue Resolution

## Identidad
- **paper_id:** provisional `agent-based-ensemble-reasoning-repository-issue-resolution`; sin ID canónico local.
- **Título:** *Agent-Based Ensemble Reasoning for Repository-Level Issue Resolution*.
- **Autores:** Zhao Tian, Pengfei Gao, Junjie Chen y Chao Peng.
- **Año/venue:** ICSE 2026; DOI `10.1145/3744916.3787761`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Agent-Based Ensemble Reasoning for Repository-Level Issue Resolution.md`; PDF homónimo en `research/papers/pdf/Same Solution/secondary/`.
- **Versión/procedencia:** PDF local de 13 páginas físicas; portada cotejada con raster local. No se verificó preprint ni checksum.
- **Grupo/etiquetas:** Same Solution / secondary, conservados sin nueva aprobación.
- **Cobertura:** Markdown completo (incluidas referencias); cotejo visual selectivo de portada y páginas 4, 7 y 10. No hubo inspección visual página por página del PDF.

## Pregunta y contribución
**Hecho:** EnAgent aborda resolución de issues de repositorio: genera varios parches, poda candidatos mediante normalización/deduplicación y pruebas de regresión, y selecciona un parche final mediante agentes selectores. La salida es un parche, no documentación ni una función completada.

**Interpretación:** el patrón de separar generación y selección/verificación podría ser una idea metodológica distante; no constituye evidencia sobre documentos enlazados a APIs o seleccionados por requisito.

## Método
- **Entrada/salida/tarea:** issue de GitHub y repositorio → parche para resolver el issue.
- **Unidad/contexto:** issue/parche; los agentes inspeccionan código del repositorio y pueden generar/ejecutar pruebas.
- **Recuperación/generación:** no se describe un recuperador documental. Generación paralela y diversa de candidatos; poda por normalización, duplicados y regresión; votación entre ejecuciones del selector.
- **Dependencias:** LLM, repositorio, herramientas de prueba y configuración del ensemble.

## Documentos y arquitectura
No propone ni evalúa documentación humana o generada, documentación API, documentos de arquitectura ni enlaces de procedencia. El contexto procede de inspección de código y pruebas.

## Evaluación
- **Benchmark/tarea:** SWE-bench Verified, resolución de issues.
- **Diseño/métrica:** Pass@1; un issue cuenta como resuelto si el parche pasa todas las pruebas de oro. Se comparan Augment, Augment con poda, DeiBase y variantes con poda; se miden también tiempo y tokens. El artículo indica ensemble de tamaño 3 en RQ1 y tres repeticiones.
- **Resultados localizables:** Tabla 1, PDF físico p. 7, reporta 62,27% con Gemini 2.5 Pro, 66,40% con Claude 3.7 Sonnet, 59,00% con GPT-4.1 y 65,67% en configuración Mixture. Tabla 6 reporta 63,28% de exactitud y 3,69% de falsos negativos en el análisis de calidad de las pruebas (p. 10).
- **Límites:** evaluación centrada en SWE-bench Verified; la poda por pruebas puede equivocarse. No mide calidad documental ni API Precision/Recall/F1.

## Artefactos
El artículo anuncia código y enlaza una página de EnAgent en GitHub. **No se comprobó** acceso, contenido, versión, licencia ni ejecución.

## Relación con nuestra tesis
La tarea y salida difieren de la comparación RepoScope frente a RepoScope más módulo documental. La separación generación/selección podría motivar una idea de diseño, pero requeriría adaptación y evaluación propia; no es un baseline ni una demostración de la hipótesis documental.

## Riesgos
No transferir Pass@1 de resolución de issues a corrección de generación de funciones o alineación de APIs. La prueba de regresión puede tener falsos negativos; el artículo informa que existen.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Autores, ICSE 2026 y DOI | Markdown y portada raster del PDF | 1 (1406) | Hecho, cotejado visualmente |
| Generación, poda y selección | Markdown; Fig. 2 y §3 | 4–5 (1409–1410) | Hecho |
| Benchmark y diseño experimental | Markdown; §§4.1–4.4 | 6 (1411) | Hecho |
| Resultados principales y evaluación de poda | Markdown; Tablas 1 y 6; rasters revisados | 7 (1412), 10 (1415) | Hecho reportado |
| Relevancia documental acotada | Método del artículo frente al brief de tesis | No aplica | Interpretación |

## Pendientes
Comprobar artefactos solo si se autoriza; no inferir que el anuncio equivale a disponibilidad o reproducción.
