# Ficha — LLM See, LLM Do (LogiCoder)

## Identidad
- **Título de archivo:** *LLM See, LLM Do*; sistema referido como LogiCoder.
- **Autores/año/venue:** Pendiente de cotejo del artículo.
- **Fuente:** Extracción PyMuPDF, paginación física desde 1; no inspección visual.
- **Grupo:** Same Solution / terceary / not_processed.
- **Cobertura:** Lectura íntegra reportada en la sesión previa.

## Pregunta y contribución
Generación de funciones a nivel repositorio guiada por razonamiento sobre posibles callees: identifica callees, recupera ejemplos de uso de esos callees y los combina con búsqueda semántica. No es completion de líneas ni reparación.

## Método
Generación funcional con retrieval de ejemplos API/callee y contexto semántico. Usa pruebas como evaluación de corrección y reporta Recall@1 para recuperación; distinguir ambas familias de métricas.

## Documentos y arquitectura
El contexto recuperado consiste en código/ejemplos de uso de funciones llamadas; no es documentación humana o generada, aunque ayuda a reutilizar APIs.

## Evaluación
Resultado principal reportado en DevEval-cf; generalización en DevEval y CoderEval. Pass@1 y Recall@1 figuran en el texto. No se consignan cifras aquí sin cotejar tablas; no se reprodujo.

## Artefactos
No verificados.

## Relación con nuestra tesis
Vecino cercano en generación funcional y recuperación para reutilizar APIs. Diferencia: recupera ejemplos de callees/código, no documentos vinculados a las APIs recuperadas; valorar contra RepoScope requiere conservar mismas tareas y APIs.

## Riesgos
La predicción de callees puede fallar y sesgar recuperación; la disponibilidad de tests y splits debe auditarse. DevEval-cf y DevEval no deben sumarse como independientes sin revisar solapamiento.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Detecta posibles callees y recupera ejemplos de uso, fusionados con retrieval semántico. | Extracción del paper | Abstract/Method, pp. 1–5 | Método reportado |
| Evalúa función generation con pruebas; DevEval-cf principal y DevEval/CoderEval generalización. | Extracción del paper | Evaluation, pp. 6–10 | Diseño reportado |
| Pass@1 y Recall@1 se reportan como métricas distintas. | Extracción del paper | Evaluation/Results, pp. 7–11 | Métricas reportadas |

## Pendientes
Completar metadatos, cifras, modelos, baselines y definición exacta de DevEval-cf; verificar artefactos y solapamientos.
