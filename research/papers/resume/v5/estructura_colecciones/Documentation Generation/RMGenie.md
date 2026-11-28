# RMGenie: An LLM-Based Agent Framework for Open Source Software README Generation

## Identidad
- **paper_id:** alias provisional `RMGenie`.
- **Título:** *RMGenie: An LLM-Based Agent Framework for Open Source Software README Generation*.
- **Autores:** Xing Cui, Jingzheng Wu, Zhiyuan Li, Tianyue Luo y Xiang Ling.
- **Año/venue:** ICSME 2025, pp. 505–516.
- **Fuente original:** Markdown `research/papers/text/v5/estructura_colecciones/Documentation Generation/RMGenie.md`; PDF `research/papers/pdf/Documentation Generation/RMGenie.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 12 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation Generation`; ubicación anterior: `Documentation-Code/secondary`.

## Pregunta y contribución
Propuesta de agente LLM para README de repositorios OSS con Tree of Actions y reflexion.

## Método
- LLM agent examina estructura, AST, dependencias, herramientas y conocimiento externo.
- ToA genera/filtra acciones por información gain y reward basado en TF-IDF.
- Reflexion detecta errores y retrocede a nodos previos.
- Plugin VSCode declarado.

## Documentos y arquitectura
Genera README from repository. README es documentación generada/derivada, no humana; el paper no registra commit/corte/entidad ni validación semántica por requerimiento. Aporta visión de estructura global, no API-Doc/Module-Doc formal.

## Evaluación
- 150 repos, 89 files promedio, 49,395 LOC.
- Human win rate: satisfacción 60–78%, completeness 79–88%, accuracy 62–80.67%, compliance 51–75%.
- Automated score RMGenie `84.33`, DeepSeek baseline `68.28`, GPT-4o `69.33`.
- Ablaciones confirman ToA/reflexion, especialmente factual accuracy/completeness.

## Artefactos
Plugin mencionado en VSCode Marketplace y PDF. No se verificó disponibilidad, licencia, código ni versión local.

## Relación con nuestra tesis
Es antecedente de generación automática global README. Requiere separación de documentación humana/generada, procedencia por archivo/commit y evaluación frente a baseline sin documento generado.

## Riesgos
- Evaluación humana pequeña/quality judge GPT-4o.
- Información externa puede cambiar con el tiempo.
- ToA/reflexion no garantiza factualidad.
- No controla fuga o versiones futuras.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Workflow y agentes | Markdown/PDF | §III, pp. 506–510 | Evidencia |
| Dataset/métricas | Markdown/PDF | §IV-A–IV-C, pp. 510–512 | Evidencia |
| Ablaciones/comparación | Markdown/PDF | §IV-D, pp. 511–514 | Evidencia |
| Amenazas/conclusión | Markdown/PDF | §§VI–VII, pp. 514–516 | Evidencia |

## Pendientes
Verificar plugin/artefacto; definir corte de repositorios y procedencia README; probar exactitud de enlaces archivo–afirmación.
