# RepoProbe

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoProbe`.
- **Título:** *Benchmarking Architecture-Aware Repository Comprehension with Checklists*.
- **Autores/año/venue:** Yuexi Yang et al.; ASE 2026; PDF presenta arXiv v2 de agosto de 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/fourth/repoProbe.md`; PDF homónimo en `research/papers/pdf/Evaluation/fourth/`.
- **Grupo:** `Evaluation/fourth`, preservado.
- **Cobertura:** lectura íntegra del Markdown declarada; Tabla 3 visualizada en p. física 8. Página impresa no visible/verificada; PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** benchmark de comprensión de repositorios mediante respuestas con checklist de evidencia.

**Interpretación:** QA sobre repositorios, no generación ni edición de código.

## Método
500 Q&A de GitHub Discussions en 50 repositorios y 15 lenguajes. Cada instancia tiene requisito, respuesta aceptada y checklist; 225 casos incluyen contexto externo. Curación con varios LLM y revisión humana.

## Documentos y arquitectura
Evalúa respuestas con apoyo de contexto/requisitos y checklist; no produce documentación API ni arquitectura como salida.

## Evaluación
10 puntos por respuesta: ítems técnicos suman 9 y claridad/organización, 1. Juez LLM Claude Sonnet 4.5. Compara checklist frente a scoring escalar en cinco repeticiones para tres modelos; el informe identifica mayor estabilidad del checklist y casos de “Edit Bias”.

## Artefactos
La declaración de disponibilidad contiene un marcador URL pendiente de reemplazo. No se verificó artefacto público.

## Relación con nuestra tesis
Puede informar evaluación de evidencia/documentos, pero no prueba el efecto de documentos enlazados en generación.

## Riesgos
Posible sesgo del checklist generado y del juez LLM, reconocido por el trabajo. Repeticiones de una comparación específica no deben generalizarse a todo el protocolo.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---|---|
| Dataset y diseño del juez | PDF/Markdown local | §§3–5, físicas 4–11 | No visible/verificada | Método |
| Tabla 3 / estabilidad | PDF y raster local | 8 | No visible/verificada | Resultado; cotejo visual |

## Pendientes
Verificar URL/artefactos y evaluar el sesgo de checklist/juez antes de reutilizar una métrica.
