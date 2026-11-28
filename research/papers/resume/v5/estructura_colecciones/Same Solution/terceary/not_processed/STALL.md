# Ficha — STALL+

## Identidad
- **Título:** *STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis*.
- **Autores/año/venue:** Pendiente de verificación bibliográfica.
- **Fuente:** Extracción PyMuPDF, páginas físicas 1–30; no cotejada visualmente.
- **Grupo:** Same Solution / terceary / not_processed.
- **Cobertura:** Lectura íntegra reportada previamente.

## Pregunta y contribución
Estudia cómo combinar análisis estático con completion repository-level, comparando ubicación del análisis en prompting, decoding y post-procesamiento, además de RAG. Reporta diferencias por lenguaje (Java/Python) y límites del análisis.

## Método
Completion de líneas en CrossCodeEval con code LLMs/general-purpose LLMs y baselines in-file/RAG. El análisis estático extrae/valida información para guiar el modelo o procesar la salida. No es generación de documentación.

## Documentos y arquitectura
Evidencia estructural obtenida del código mediante análisis estático. No equivale a documentación de APIs ni a enlaces persistentes hacia docs.

## Evaluación
CrossCodeEval, métricas de line-level EM. La extracción advierte resultados heterogéneos por lenguaje y errores del análisis; no transcribo resultados por modelo sin cotejar tablas. Una métrica de exactitud de línea no implica corrección funcional completa.

## Artefactos
No se comprobó implementación ni se ejecutaron scripts.

## Relación con nuestra tesis
Antecedente para considerar metadatos estructurados y extracción de relaciones; si se integra, sería una modificación metodológica separada y no evidencia del valor documental.

## Riesgos
Análisis estático incompleto/incorrecto, dependencia del lenguaje y código dinámico; comparar Java y Python por separado. Fuga posible si analiza función objetivo o dependencias no permitidas.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Compara prompting, decoding, post-procesamiento y RAG. | Extracción del paper | Abstract/Method, pp. 1–7 | Diseño reportado |
| Evaluación de completion de líneas en CrossCodeEval y diferencias por lenguaje. | Extracción del paper | Benchmark/Results, pp. 7–20 | Resultado reportado |
| El análisis estático puede errar y los resultados varían entre lenguajes. | Extracción del paper | Discussion/Threats, pp. 20–26 | Limitación reportada |

## Pendientes
Verificar tablas/figuras y resultados por setting; identificar metadatos y artefactos; definir vista permitida antes de transferir análisis.
