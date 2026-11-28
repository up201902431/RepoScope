# Knowledge Graph Based Repository-Level Code Generation

## Identidad
- **paper_id:** provisional `knowledge-graph-repository-code-generation`; sin ID canónico local.
- **Título:** *Knowledge Graph Based Repository-Level Code Generation*.
- **Autores:** Mihir Athale y Vishal Vaddina.
- **Año/venue:** IEEE/ACM International Workshop on Large Language Models for Code (LLM4Code), 2025; DOI `10.1109/LLM4Code66737.2025.00026`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Knowledge Graph Based Repository-Level Code Generation.md`; PDF homónimo.
- **Versión/procedencia:** PDF local de 8 páginas físicas, impreso pp. 169–176. Portada, figuras 2–3 y Tabla I cotejadas con imágenes locales.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo y revisión visual selectiva de páginas físicas 1 y 4–5.

## Pregunta y contribución
**Hecho:** propone generar código de repositorio a partir de consulta en lenguaje natural mediante grafo de conocimiento, recuperación híbrida y filtrado de subgrafo.

**Interpretación:** documentación y descripciones generadas aparecen como atributos/representaciones en el grafo, pero el trabajo no evalúa generación documental ni selección de documentación enlazada a APIs según requisito.

## Método
- **Entrada/salida:** repositorio Python y consulta natural → código generado.
- **Grafo:** AST genera entidades de archivo, clase, método, función, atributo y descripciones; Neo4j. Embeddings documentales/descripciones con all-MiniLM-L6-v6, según el artículo.
- **Recuperación:** LLM extrae entidades de consulta; búsqueda full-text y vectorial; expansión de varios saltos y filtrado semántico del subgrafo.
- **Configuración de benchmark:** en EvoCodeBench localiza función objetivo, sustituye cuerpo por `pass` y recupera a dos saltos desde nodo objetivo; omite consulta natural porque el objetivo ya se conoce. No es idéntico al flujo general descrito.

## Documentos y arquitectura
El grafo incluye comentarios/documentación y descripciones generadas por LLM como datos derivados del código; su exactitud no se valida como producto documental. No estudia historia de versiones ni modelo arquitectónico independiente.

## Evaluación
- **Benchmark/idioma:** EvoCodeBench, 275 muestras de 25 repositorios, Python.
- **Métrica:** pass@1 mediante tests; Tabla I compara con resultados de EvoCodeBench y CodeXGraph.
- **Resultados localizables:** mayor resultado informado para el enfoque: 36,36% con Claude 3.5 Sonnet; también 32,00% GPT-4 y 33,45% GPT-4o (PDF p. 6). CodeXGraph se evaluó en 212 de 275 muestras y hay modelos distintos en algunas filas; comparación no plenamente pareada.
- **Límites:** coste de expansión/filtrado de subgrafo; esquema/lenguaje podrían ampliarse. La generación documental solo aparece como trabajo futuro, no resultado.

## Artefactos
No se encontró declaración de liberación de código/datos en el texto leído. No se verificó disponibilidad externa.

## Relación con nuestra tesis
Puede inspirar búsqueda híbrida y filtrado estructural, pero para la tesis se necesitaría asociación explícita requisito→API→documento y control de procedencia. No inferir que descripciones derivadas equivalen a documentación humana.

## Riesgos
La evaluación modifica el flujo de consulta; resultados no permiten atribución causal universal. Los datos generados desde código pueden derivar de información objetivo; no se verificó política de fuga que satisfaga el protocolo local.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad, autores, venue y DOI | Markdown y portada raster | 1 (169) | Hecho, cotejado visualmente |
| Entidades y descripciones del grafo | Markdown; §III-A, Figs. 2–3 | 4 (172) | Hecho |
| Búsqueda híbrida y expansión | Markdown; §§III-B–C | 4–5 (172–173) | Hecho |
| Benchmark/resultados y diferencia de muestras | Markdown; §IV–V, Tabla I; raster revisado | 5–6 (173–174) | Hecho reportado |
| Documentación generada solo como futuro | Markdown; §VI | 6–7 (174–175) | Hecho |
| Adaptación a pregunta tesis | Brief frente al método | No aplica | Interpretación |

## Pendientes
No se comprobó artefacto externo; mantener separada la salida futura propuesta de resultados evaluados.
