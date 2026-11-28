# Ficha — RepoShapley

## Identidad
- **Título:** *RepoShapley: Shapley-Enhanced Context Filtering for Repository-Level Code Completion*.
- **Autores/año/versión:** Yu Huo et al.; arXiv:2601.03378v2 (17-04-2026 según extracción). Venue no verificado independientemente.
- **Fuente:** Markdown extraído por PyMuPDF, páginas físicas desde 1; cotejo visual no realizado. GitHub mencionado en la página inicial, no comprobado.
- **Grupo/etiqueta:** Same Solution / fourth, según clasificación existente.
- **Cobertura:** Texto leído íntegramente en la sesión previa; extracción no verificada visualmente.

## Pregunta y contribución
Aborda la selección de chunks cuyo valor depende de interacciones: fragmentos complementarios pueden ser útiles juntos y fragmentos conflictivos pueden perjudicar. ChunkShapley produce supervisión de contribución marginal estilo Shapley; un surrogate estructurado aproxima saturación/conflicto; una verificación acotada con el generador determina coaliciones, cuyas etiquetas se destilan en tokens de control `<KEEP>/<DROP>` y señales de recuperación.

## Método
Completion a nivel repositorio con contexto RAG. Etiquetado offline por sondeo teacher-forced, juego surrogate y verificación post-generación; inferencia con modelo destilado para filtrar y activar recuperación. Es filtrado/selección de contexto, no creación de documentación ni reparación.

## Documentos y arquitectura
Opera sobre chunks de código recuperados y sus interacciones. No se identificó un componente de documentación API, documentación arquitectónica o enlace persistente API-documento. No confundir la atribución Shapley de chunks con selección de documentos documentales.

## Evaluación
La introducción reporta evaluación en varios benchmarks y backbones, mejora de calidad y reducción de contexto dañino/recuperaciones innecesarias; la figura inicial compara con No-Retrieve y menciona StarCoder-Base-7B y CodeLlama-13B. No consigno cifras agregadas porque requieren cotejar las tablas completas; el texto extraído advierte que tablas/figuras pueden alterarse. Resultados publicados por autores, no reproducidos.

## Artefactos
Se anuncia un enlace GitHub en la fuente; disponibilidad, commit, licencia y ejecución no verificados.

## Relación con nuestra tesis
Antecedente para selección sensible a interacciones bajo presupuesto y para una posible ablación de filtrado. Difiere de la pregunta de tesis: no evalúa el valor incremental de documentación vinculada a APIs recuperadas sobre RepoScope.

## Riesgos
Supervisión y verificación offline costosas; el surrogate puede no modelar todas las interacciones reales; control tokenizado hereda sesgos de etiquetas. Confirmar cortes de datos y seguridad de los contextos durante teacher-forcing antes de cualquier adaptación.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Motivación: utilidad contextual no aditiva y conflicto entre chunks. | Extracción del paper | Abstract e Introduction, p. 1 | Evidencia reportada |
| ChunkShapley, surrogate, verificación y destilación de decisiones. | Extracción del paper | Abstract y descripción de contribuciones, pp. 1–2 | Método reportado |
| Evaluación con múltiples benchmarks/backbones; figura de comparación inicial. | Extracción del paper | Abstract/Figura 1, p. 1 | Resultado reportado, sin transcribir cifras |

## Pendientes
Cotejar visualmente tablas de resultados y su protocolo; verificar repositorio/licencia; extraer benchmarks, métricas y valores por setting antes de una comparación cuantitativa.
