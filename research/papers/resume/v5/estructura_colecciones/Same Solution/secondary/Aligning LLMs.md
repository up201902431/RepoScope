# Aligning LLMs to Fully Utilize the Cross-file Context in Repository-level Code Completion

## Identidad
- **paper_id:** provisional `aligning-llms-cross-file-context`; sin ID canónico local.
- **Título:** *Aligning LLMs to Fully Utilize the Cross-file Context in Repository-level Code Completion*.
- **Autores:** Jia Li, Hao Zhu, Huanyu Liu, Xianjie Shi, He Zong, Yihong Dong, Kechi Zhang, Siyuan Jiang, Zhi Jin y Ge Li.
- **Año/venue:** ASE 2025; DOI `10.1109/ASE63991.2025.00125`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Aligning LLMs.md`; PDF homónimo bajo `research/papers/pdf/Same Solution/secondary/`.
- **Versión/procedencia:** PDF local de 13 páginas físicas; portada y tablas indicadas cotejadas visualmente. Sin checksum ni verificación de preprint.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo, incluidas referencias; cotejo visual selectivo de páginas físicas 1 y 8–10. No inspección visual integral del PDF.
- **Alias/diferenciación:** COLA es *Code Long-context Alignment*; COLA-132K es el dataset. No es el paper AlignCoder: difieren título, autores y DOI aunque ambos son ASE 2025.

## Pregunta y contribución
**Hecho:** estudia si un modelo utiliza el contexto cross-file suministrado para completar código; presenta COLA-132K y entrenamiento SFT/DPO para alinear modelos con ese contexto.

**Interpretación:** es antecedente de utilización del contexto, no una intervención de documentación vinculada y seleccionada según requisito.

## Método
- **Entrada/salida:** código incompleto, contexto in-file y cross-file → completion.
- **Datos/unidad:** 120.000 ejemplos de entrenamiento y 12.000 de prueba, de 2.000 repositorios y cuatro lenguajes (Python, Java, C++ y Go); incluye objetivos de invocaciones API cross-file y fragmentos similares.
- **Generación/entrenamiento:** SFT y DPO sobre modelos; no es RAG documental.
- **Dependencias:** dataset, modelo afinado y contexto de código entre archivos.

## Documentos y arquitectura
No evalúa documentación humana/generada, diagramas ni arquitectura. Las invocaciones API son objetivos/contexto de código, no documentos de API.

## Evaluación
- **Benchmarks/idiomas:** COLA-132K y CrossCodeEval; cuatro lenguajes en el dataset.
- **Métricas:** EM y BLEU; API Accuracy es un sondeo de exactitud de nombres API, no API Precision/Recall/F1.
- **Resultados localizables:** el artículo informa una mejora EM de 19,7% para code spans en Python en COLA-132K. En CrossCodeEval, aiXcoder-7B frente a aiXcoder-7B-v2: Python 31,22→40,52 EM (+29,8% relativo), Java 42,50→51,43 (+21,0%); Tablas I–III, PDF p. 8. Tabla V reporta API Accuracy del modelo v2: 94,4% Python, 92,4% Java, 87,7% C++ y 81,3% Go (p. 9).
- **Límites:** solo dos tipos explícitos de relación con contexto; el artículo reconoce diferencias de versiones de repositorio como reto. Sus controles contra contaminación son afirmaciones de los autores, no auditoría independiente. La intervención requiere entrenamiento y no aísla documentación con APIs fijas.

## Artefactos
Se anuncia liberación de datasets y pesos y se cita un paquete de replicación anónimo. No se comprobaron disponibilidad, contenido, licencia ni ejecución.

## Relación con nuestra tesis
Útil como antecedente sobre uso del contexto cross-file. Difiere de la tesis: entrenamiento para usar código, no módulo documental vinculado a APIs recuperadas y seleccionado por requisito. No atribuir novedad absoluta a la generación documental.

## Riesgos
Posible dependencia de versiones del repositorio y riesgo de contaminación según el propio artículo. API Accuracy no es métrica de alineación API P/R/F1.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad, ASE 2025 y DOI | Markdown; raster de portada | 1 (1477) | Hecho, cotejado visualmente |
| Datos y objetivos de COLA-132K | Markdown; §III.A | 2–4 (1478–1480) | Hecho |
| SFT y DPO | Markdown; §III.B | 5 (1481) | Hecho |
| Resultados y API Accuracy | Markdown; Tablas I–V; imágenes revisadas | 8–9 (1484–1485) | Hecho reportado |
| Riesgos/versiones y límites | Markdown; §§VIII–X | 10–11 (1486–1487) | Hecho reportado |
| Diferencia respecto a la hipótesis documental | Brief de tesis frente al método | No aplica | Interpretación |

## Pendientes
No se comprobaron artefactos ni políticas de datos fuera de lo que declara el artículo.
