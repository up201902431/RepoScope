# Repository-level code completion with adaptive segmentation and fused retrieval

## Identidad
- **paper_id:** provisional `adaptive-segmentation-fused-retrieval`; sin ID canónico local.
- **Título:** *Repository-level code completion with adaptive segmentation and fused retrieval*.
- **Autores:** Yuanyuan Shen, Pinle Qin, Kaiyi Zhao, Fuwei Zhang, Fan Zhang y Guiji Li.
- **Año/venue:** *Empirical Software Engineering* (2026), 31:26; DOI `10.1007/s10664-025-10762-7`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Repository-level code completion with adaptive segmentation and fused retrieval.md`; PDF homónimo.
- **Versión/procedencia:** artículo con fechas editoriales 8-abr-2025 recibido, 3-nov-2025 aceptado y 5-dic-2025 publicado online; 28 páginas físicas. Portada y páginas señaladas cotejadas visualmente.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo, incluidas referencias; visuales selectivos de Figuras 2–3 y Tablas 2–11. No verificación visual página por página.

## Pregunta y contribución
**Hecho:** propone completar código a nivel de línea con segmentación sintáctica adaptativa y recuperación fusionada textual/funcional.

**Interpretación:** los resúmenes funcionales son representaciones de código para retrieval, no documentación enlazada a API ni documentos elegidos por requisito.

## Método
- **Entrada/salida:** contexto in-file y repositorio → código completado en línea.
- **Segmentación:** ventanas ajustadas a límites sintácticos (funciones, clases, bloques de control, etc.).
- **Retrieval:** BM25 sobre últimas cinco líneas del contexto; señal funcional basada en resúmenes generados con DeepSeek-v2 para archivo/chunks y embeddings UniXcoder; combina señales con pesos ω1/ω2 y rerank.
- **Generación:** prompt integra contexto in-file y hasta K chunks según presupuesto de tokens.
- **Dependencias:** lenguaje/parser, coste de resumen, pesos, K y límite de contexto. El texto consultado no fija valores de ω1/ω2.

## Documentos y arquitectura
El resumen se genera desde código y funciona como representación de chunk; el generador recibe código. No se evalúa documentación humana, arquitectura o historia.

## Evaluación
- **Benchmark:** CrossCodeEval: Python (471 repos/1.368 archivos/2.665 ejemplos), Java (239/745/2.139), TypeScript (193/779/3.356), C# (99/642/1.768).
- **Métricas:** EM/ES de code match, EM/F1 de identifier match. DyPyBench propio para prueba adicional.
- **Resultados:** para DeepSeekCoder-7B, Tabla 2 reporta EM 33,51% Python y 31,42% Java frente a RLCoder 30,28%/26,09%; autores atribuyen ganancias relativas 10,7%/20,4%, con baselines de publicaciones previas y configuraciones no idénticas. Tablas 3–10 ablan retrieval, segmentación y modelos (pp. 15–22). DyPyBench reporta pass rate 38,23%, con muestra pequeña (Tabla 11, p. 23).
- **Límites:** resultados variables por lenguaje, estructura sintáctica y dependencia larga; resumen/vectores añaden coste (autores reportan unas 103 horas para sumarizar bloques Python). El ejemplo de Tabla 11 es ilustrativo, no benchmark completo.

## Artefactos
El artículo declara código/datos en un repositorio GitHub. URL textual local parece `https://github.com/fiou.../repository-level-code-completion/tree/master`; no comprobé acceso, contenido, versión, licencia ni ejecución.

## Relación con nuestra tesis
Puede orientar módulos de segmentación/retrieval, pero no aborda documentos asociados a APIs ni selección documental por requisito. No reemplaza RepoScope ni es evidencia directa de la hipótesis.

## Riesgos
No tratar los baselines publicados como comparación controlada. Los resúmenes generados desde código podrían contener información derivada; el protocolo local de fuga requeriría auditoría propia.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---:|---|
| Identidad y DOI | Markdown/PDF; raster de portada | 1 | Hecho |
| Segmentación y retrieval fusionado | Markdown; §§4.1–4.2, Figs. 2–3 | 7–12 | Hecho, figuras cotejadas |
| Benchmark/métricas | Markdown; §§5.1–5.2 | 13 | Hecho |
| Resultados y ablaciones | Markdown; §§5.3–6.5, Tablas 2–10 | 14–22 | Hecho reportado, tablas cotejadas |
| DyPyBench y amenazas | Markdown; Tabla 11 y §§7–8 | 23–24 | Hecho |
| Relación con tesis | Brief frente al método | No aplica | Interpretación |

## Pendientes
Confirmar URL exacta desde fuente si se autoriza; no ejecutar ni asumir artefactos disponibles.
