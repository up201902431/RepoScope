# RACE-Bench

## Identidad
- **paper_id:** no asignado; identificador local provisional `RACE-Bench`.
- **Título:** *A Reasoning-Augmented Benchmark for Repository-Level Code Agents on Feature Addition*.
- **Autores/año/venue:** Shuhan Liu et al.; ASE 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/RACE-Bench.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, preservado.
- **Cobertura:** lectura íntegra declarada; Tabla 2 contrastada con imagen local. PDF completo no inspeccionado visualmente.

## Pregunta y contribución
**Hecho:** benchmark de agentes de código para tareas de adición de funcionalidades a nivel de repositorio, con anotaciones de razonamiento.

**Interpretación:** benchmark de edición/agente, no de generación puntual basada en documentos.

## Método
528 tareas desde PR/issues en 12 repositorios Python; referencias intermedias abarcan intención, archivos, tareas y pasos, construidas mediante análisis de parche y apoyo/auditoría LLM. RACE-Bench Lite contiene 100 casos.

## Documentos y arquitectura
La fuente de tareas son issues/PR y artefactos de cambio. No evalúa documentación vinculada a APIs ni generación de documentos arquitectónicos.

## Evaluación
Tres agentes con DeepSeek V3.2 en benchmark completo. Resolved rate exige pasar FTP y PTP; también se reporta Patch Apply Rate. El análisis de razonamiento mide alineación con una trayectoria aceptada mediante recall/overprediction y puntuaciones con juez; no mide razonamiento correcto de forma absoluta. mini-SWE-Agent obtiene Resolved Rate 70,08 %, TraeAgent 52,65 % y AutoCodeRover 28,79 %. Una ejecución por instancia.

## Artefactos
Se declara paquete de replicación; no se verificaron disponibilidad, licencia ni ejecución.

## Relación con nuestra tesis
Útil para estudiar tareas de agentes y fuga entre issue, tests y parche; no mide enriquecimiento documental. Lite no es conjunto de test independiente para comparaciones posteriores: se selecciona para aproximar resultados de agentes del benchmark completo.

## Riesgos
La trayectoria de referencia es una solución válida, no necesariamente la única; el paper registra esa limitación. Una ejecución por instancia restringe inferencias sobre variabilidad.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Construcción y protocolo | PDF/Markdown local | §§2–4, 2–10 | 1639–1647 | Método |
| Resolved Rate por agente | PDF y raster local | Tabla 2, física 7 | 1644 | Resultado; cotejo visual |
| Limitaciones | PDF/Markdown local | Limitaciones dentro de §§2–4 | En rango 1639–1647 | Amenaza reportada |

## Pendientes
Verificar artefactos y auditar acceso temporal a issues, tests, PR y parches objetivo antes de reutilizar datos.
