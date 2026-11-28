# Ficha — FastCoder

## Identidad
- **Título:** *FastCoder: Accelerating Repository-level Code Generation via Efficient Retrieval and Verification*.
- **Autores/año/venue:** Qianhui Zhao et al.; metadatos de publicación por verificar en la extracción.
- **Fuente:** PyMuPDF, extracción con paginación física desde 1.
- **Grupo:** Same Solution / terceary / less important.
- **Cobertura:** Lectura íntegra reportada en la sesión previa; PDF no inspeccionado visualmente.

## Pregunta y contribución
Reducir latencia de generación mediante draft-verification, con datastore multi-fuente (conocimiento general y del proyecto), control temporal de retrieval, recuperación paralela y caché consciente de contexto/preferencias del LLM. Es aceleración de generación, no contribución documental.

## Método
Combina retrieval especulativo de candidatos, generación/validación de borradores y caching; evalúa stand-alone y repository-level. En el texto se comparan variantes con decodificación autoregresiva y REST; también se plantea integrar con métodos de corrección.

## Documentos y arquitectura
Datastore de secuencias/código general y repository-specific. No se afirma que el material sea documentación humana ni que esté enlazado por API.

## Evaluación
Abstract reporta hasta 2.53× y 2.54× speedup frente a decodificación autoregresiva para generación repository-level y stand-alone; integración con métodos de corrección puede superar 2.6×. DevEval, RepoEval y HumanEval aparecen en evaluación. En RepoEval se informa ES por no estar disponible el script Pass@k. Resultados reportados, no reproducidos.

## Artefactos
Disponibilidad, commit y ejecución no verificados.

## Relación con nuestra tesis
Puede servir como antecedente de coste/latencia si la tesis mide sobrecarga; no es baseline apropiado para aislar efecto documental sin fijar recuperación y decodificación.

## Riesgos
El speedup depende del hardware, datastore, cache hit rate y protocolo de tiempo; no implica mejor corrección. La caché puede introducir contaminación entre tareas/repositorios si no se aísla.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Datastore multi-fuente, recuperación paralela y caché contextual. | Extracción | Abstract/Introduction, p. 1; Method, pp. 3–6 | Método |
| Speedup 2.53×/2.54× y >2.6× al integrar. | Extracción | Abstract, p. 1 | Resultado reportado |
| RepoEval usa ES ante ausencia de scripts Pass@k. | Extracción | Evaluation Metrics, aprox. p. 7 | Decisión de métrica reportada |

## Pendientes
Confirmar páginas exactas de tablas, hardware y métricas; revisar política de caché y verificar artefactos.
