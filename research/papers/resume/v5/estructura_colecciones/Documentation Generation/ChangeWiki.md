# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *ChangeWiki: Repository-Level Change Summarization Augmented with Architecture Semantics*
- autores: Zijun Wang, Wuxia Jin, Jiale Li, Zhanhong Mou y Ting Liu
- año/venue: 2026, ASE ’26
- ubicación actual: Documentation Generation; ubicación anterior: Related/primary/time traversal
- DOI: `10.1145/3832783.3834436`
- fuente: PDF 13 páginas, extracción pdfplumber e imágenes locales
- PDF/texto: `research/papers/pdf/Documentation Generation/ChangeWiki.pdf`; `research/papers/text/v5/estructura_colecciones/Documentation Generation/ChangeWiki.md`
- imágenes: `research/papers/images/v5/estructura_colecciones/Documentation Generation/ChangeWiki/`
- cobertura: texto íntegro; páginas seleccionadas 1, 2, 4, 6, 8–11 cotejadas visualmente

## Pregunta y contribución
Generar resúmenes jerárquicos de cambios entre dos versiones, agrupando commits dispersos e incorporando semántica arquitectónica.

## Método
- entrada: dos versiones y commits entre ellas
- tareas: detección de cambios de entidad, construcción jerárquica y generación de resumen
- arquitectura: extensión de RefDiff para cambios; SemArc para arquitectura; LLM para agregación jerárquica
- salida: resúmenes trazables de función, clase, archivo, módulo y proyecto
- lenguaje: evaluación principalmente C/C++

## Documentos y arquitectura
- resúmenes de evolución, no documentación estática de API
- reconstruye arquitectura semántica de ambas versiones
- trazabilidad entre niveles jerárquicos y cambios
- no implementa selección requisito-documento-API

## Evaluación
- proyectos: libnl, libuv, CEF, jsoncpp y Skia
- benchmark declarado: 1.387 resúmenes (abstract: 1.400)
- desagregación: 200 módulo, 199 archivo, 393 clase/estructura y 595 función
- baselines: LLM y LLM+CoT
- modelos declarados: DeepSeek-V3.2, Kimi-2.5 y Qwen3.5-plus
- métricas: BLEU, ROUGE-L, BERTScore y evaluación humana 1–5
- resultados DeepSeek: BLEU 9,95%, ROUGE-L 29,95%, BERTScore 70,94%; frente a LLM 5,60%, 22,12%, 63,40%
- evaluación humana: exactitud 4,79; completitud 4,75; legibilidad 4,67; trazabilidad 4,56 sobre 350 muestras

## Artefactos
- código/dataset anunciado en Zenodo DOI `10.5281/zenodo.19251834`
- demostración anunciada en repositorio público y video
- disponibilidad externa, licencia, contenido y ejecución no verificadas

## Relación con nuestra tesis
Útil solo como línea opcional de contexto temporal y evolución. No sustituye documentación humana/generada asociada a APIs ni el baseline. Puede orientar procedencia y resúmenes de cambios, no su integración automática.

## Riesgos
- acceso a la versión futura/diff puede filtrar la solución
- desvío por resúmenes de referencia generados con LLM
- generalización pendiente fuera de C/C++
- calidad dependiente de SemArc y dependencias

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Identidad/DOI | PDF/extracción | físico p. 1 / impresa 1333 | Hecho cotejado |
| Problema y flujo | PDF/extracción | §§2–3; físicos pp. 2–7 / impresas 1334–1339 | Hecho |
| Selección y benchmark | PDF/extracción | §§4.1–4.3; físicos pp. 8–9 / impresas 1340–1341 | Hecho reportado |
| Resultados y amenazas | PDF/extracción | §§5–6 y 9; físicos pp. 9–11 / impresas 1341–1343 | Hecho reportado |

## Pendientes
- comprobar artefacto externo y licencia
- auditar política temporal y corte por tarea
- confirmar compatibilidad con Python y configuración reproducible
