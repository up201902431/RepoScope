# RetNext

## Identidad
- **paper_id:** provisional `retnext`; sin ID canónico local.
- **Título:** *RetNext: Code Retrieval for Repository-Level Next Edit Suggestion*.
- **Autores:** Zhaoyuan Pan, Zheng Zhang y Cheng Cheng.
- **Año/venue:** DSDE 2026, 9th International Conference on Data Storage and Data Engineering, Chengdu, 12–14 junio 2026; DOI `10.1145/3830340.3830348`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/RetNext.md`; PDF homónimo.
- **Versión/procedencia:** PDF de 5 páginas físicas; portada y Figuras 1–6/Tablas 2–3 cotejadas con imágenes locales.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo, incluida bibliografía; inspección visual selectiva de pp. 1–5.

## Pregunta y contribución
**Hecho:** aborda Next Edit Localization (NEL): dado diff actual y chunks candidatos del repositorio, recuperar y ordenar la ubicación probable de la siguiente edición.

**Interpretación:** puede ser relevante para el eje candidato de evolución/historia, pero no genera código/documentación ni evalúa selección de documentos de API por requisito.

## Método
- **Datos:** RetNextBench con 583 instancias finales y ~26k pares de entrenamiento, de 18 repositorios y cuatro lenguajes.
- **Construcción:** relaciones entre diffs de commits, pares consulta-destino, filtro LLM y revisión humana; una categoría incluye sincronización de documentación y código.
- **Modelo:** adaptador LoRA específico para consulta; encoder de chunks congelado e índice estático compartido.
- **Salida:** ranking/localización de edición siguiente. Generador aparece en flujo demostrativo, pero el aporte principal evaluado es recuperación.

## Documentos y arquitectura
La etiqueta de sincronización de documentación y código es una categoría de anotación, no recuperación de documentación para una API. No evalúa arquitectura o generación documental.

## Evaluación
- **Benchmarks/métricas:** RetNextBench con MRR y Recall@10 por idioma/promedio; CoIR con NDCG@10 para cinco subtareas.
- **Resultados:** Tabla 2 informa RetNext-Qwen promedio MRR 25,13 y R@10 54,42 frente a Qwen3-embedding-0.6b base 21,63 y 49,36. Tabla 3 presenta resultados CoIR. Caso de generación Top-5 es demostrativo, no métrica de corrección funcional.
- **Límites:** generación de datos de alta calidad, evaluación del generador, reranking y pruebas en entornos IDE/repositorios cambiantes quedan como futuro. División por repositorio comparte los mismos repositorios entre desarrollo y evaluación; limita inferencia sobre proyectos no vistos, sin demostrar por sí misma fuga.

## Artefactos
No se encontró enlace explícito a implementación o dataset en el artículo consultado; no se comprobó fuera del texto.

## Relación con nuestra tesis
Prioridad interpretativa baja-media para pregunta documental; potencialmente relevante al estudiar evolución/localización de cambios. No sustituye un generador ni mide corrección funcional/API P/R/F1.

## Riesgos
Precisar política temporal/partición por commits antes de reutilizar el benchmark. No afirmar fuga a partir de compartir proyectos: aquí se registra como límite de generalización.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad y DOI | Markdown y raster de portada | 1 (51) | Hecho, cotejado visualmente |
| Flujo de NEL | Markdown; Fig. 1 | 2 (52) | Hecho |
| Benchmark/filtro/anotación | Markdown; §2, Figs. 2–4 | 2–3 (52–53) | Hecho |
| LoRA e índice estático | Markdown; §3, Fig. 5 | 3 (53) | Hecho |
| Resultados y demostración | Markdown; Tabla 2, Fig. 6, Tabla 3; rasters revisados | 4–5 (54–55) | Hecho reportado |
| Relevancia para historia y documentos | Brief frente al método | No aplica | Interpretación |

## Pendientes
No hay artefacto explícito verificado; revisar política temporal y partición solo si se plantea reutilizar RetNext.
