# Ficha — CECoder

## Identidad
- **Título:** *CECoder: Fine-Grained Code Element Retrieval for Repository-Level Code Generation*.
- **Autores/año/venue:** Yiming He et al.; IEEE ISSREW 2025 según portada; DOI 10.1109/ISSREW67781.2025.00051.
- **Fuente:** Extracción PyMuPDF; páginas físicas desde 1; no cotejada visualmente.
- **Grupo:** Same Solution / terceary / less important.
- **Cobertura:** Lectura íntegra reportada previamente.

## Pregunta y contribución
Evitar mal uso de clases/métodos del repositorio recuperando ejemplos de cómo se invocan y componen elementos de código. Primero recupera snippets por requisito y genera borrador; divide este en bloques de invocaciones/contexto, vuelve a recuperar usos específicos, reordena e integra los snippets.

## Método
Generación funcional repository-level con recuperación en dos granularidades. Es retrieval + generation, no reparación de issues ni generación documental.

## Documentos y arquitectura
Recupera ejemplos de código fuente para uso de elementos; no crea documentación API. Se relaciona con reutilización de APIs, pero el artefacto insertado es snippet de implementación.

## Evaluación
DevEval (1825 tareas reportadas). El abstract declara superioridad sobre RepoCoder en métricas evaluadas y reporta Exact Match 4.39%, Edit Similarity 41.97%, Pass@1 27.01% y Recall@1 39.25% (interpretados como puntuaciones de CECoder; no como ganancias relativas). No mezclar Recall@1 de retrieval con API Recall del protocolo de tesis.

## Artefactos
No verificados; no se reprodujo.

## Relación con nuestra tesis
Vecino cercano por generación funcional y uso de APIs propias del repo. Diferencia: recupera código demostrativo, no selecciona documentos vinculados explícitamente a APIs recuperadas; su pipeline cambia la recuperación si se compara directamente con RepoScope.

## Riesgos
El borrador intermedio condiciona la segunda recuperación y puede propagar errores; duplicación entre repos puede influir. Los valores del abstract requieren confirmar tabla/normalización.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Dos etapas: generación de borrador, partición por invocaciones y retrieval fino. | Extracción | Abstract/Introduction, pp. 1–2 | Método |
| DevEval con 1825 tareas; EM, ES, Pass@1 y Recall@1 reportados. | Extracción | Abstract, p. 1 | Resultados reportados |

## Pendientes
Verificar visualmente escalas, tablas, baselines, modelos y splits; comprobar artefactos y solapamientos del benchmark.
