# Ficha — RLCoder

## Identidad
- **Título:** *RLCoder* (título bibliográfico completo pendiente de verificar).
- **Autores/año/venue:** Pendiente de completar desde portada/referencia.
- **Fuente:** Extracción PyMuPDF; páginas físicas 1–13 en el Markdown.
- **Grupo:** Same Solution / terceary / less important.
- **Cobertura:** Lectura íntegra reportada anteriormente; extracción no revisada visualmente.

## Pregunta y contribución
Aprender qué contexto recuperar para completion repository-level usando una recompensa vinculada a perplexity y una señal de parada. Se trata de recuperación para completion, no reparación ni documentación generada.

## Método
Recuperador entrenado con recompensa de perplexity ponderada y stop signal para decidir selección/continuación. La evaluación incluye CrossCodeEval y RepoEval; confirmar formulación completa de recompensa y configuración antes de adaptar.

## Documentos y arquitectura
Recupera contexto de código entre archivos. No se documenta un mecanismo de documentación API ni enlace explícito a páginas/documentos.

## Evaluación
La extracción reporta EM/ES en CrossCodeEval y RepoEval; no transcribo cifras porque se requiere cotejo de tablas y configuración. RepoScope lo usa como baseline en el corpus, pero las condiciones no deben suponerse idénticas a una nueva ejecución.

## Artefactos
No se verificaron enlaces, versiones ni comandos; no reproducido localmente.

## Relación con nuestra tesis
Baseline/comparador relevante para retrieval de completion y posible antecedente a controlar; no evalúa beneficio incremental de documentación sobre APIs fijas.

## Riesgos
La recompensa puede favorecer similitud/perplexity sin equivaler a corrección funcional; stop/retrieval puede depender del modelo. Revisar solapamiento de repos y fuga por funciones objetivo/caller context.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Recuperador con recompensa de perplexity ponderada y stop signal. | Extracción del paper | Abstract/Method, pp. 1–4 | Método reportado |
| EM/ES evaluados en CrossCodeEval y RepoEval. | Extracción del paper | Evaluation, pp. 7–10 | Métricas reportadas |

## Pendientes
Completar título/autores/venue, cifras por benchmark y baselines; verificar artefactos y revisar el protocolo de fuga.
