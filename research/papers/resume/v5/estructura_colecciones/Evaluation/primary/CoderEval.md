# CoderEval

## Identidad
- **paper_id:** no asignado en catálogo; identificador local provisional `CoderEval`.
- **Título:** *A Benchmark of Pragmatic Code Generation with Generative Pre-trained Models*.
- **Autores/año/venue:** Hao Yu et al.; ICSE 2024. DOI `10.1145/3597503.3623322`.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/primary/CoderEval.md`; PDF `research/papers/pdf/Evaluation/primary/CoderEval.pdf`.
- **Grupo:** se conserva `Evaluation/primary`; esto no implica aprobación de clasificación.
- **Cobertura:** el informe del lote declara lectura íntegra del Markdown extraído. PDF: páginas de resultados seleccionadas visualmente, no el documento completo; extracción local no está verificada manualmente en su totalidad.

## Pregunta y contribución
**Hecho:** benchmark pragmático de generación de funciones/métodos con dependencias de repositorio en Python y Java.

**Interpretación:** referencia de evaluación funcional con contexto de repositorio, no evaluación del aporte documental de la tesis.

## Método
460 funciones/métodos (230 Python, 230 Java) de 43 proyectos Python y 10 Java. Se estratifican en seis niveles de dependencia, de self-contained a project-runnable. Se excluyeron, entre otros, tests, interfaces, funciones obsoletas, funciones sin comentario en inglés y casos no ejecutables. Generan CodeGen, PanGu-Coder y `gpt-3.5-turbo`; 10 muestras por tarea.

## Documentos y arquitectura
Los comentarios/descripciones forman parte de la tarea y la selección excluye funciones sin comentario en inglés. No estudia documentación vinculada explícitamente a APIs ni arquitectura.

## Evaluación
Pass@1/5/10 usa el estimador no sesgado de HumanEval: fracción de tareas con al menos una solución que pasa todos los tests entre K muestras. Acc@K mide si tokens de `oracle_context` aparecen en alguna muestra; no es corrección funcional ni API F1. La tabla reporta para ChatGPT Pass@1 21,04 % en Python y 35,39 % en Java. Se repitió 10 veces y se presenta el grupo mediano por Pass@10.

## Artefactos
La publicación declara código y resultados abiertos. Disponibilidad, licencia, contenido y ejecución no verificados.

## Relación con nuestra tesis
Antecedente útil para generación funcional dependiente del repositorio. Sus Acc@K y Pass@K no sustituyen API P/R/F1 ni aíslan el efecto de documentos enlazados a APIs.

## Riesgos
La selección manual y descripciones humanas mitigan algunas fugas de docstrings, pero no prueban ausencia de contaminación de repositorios. El informe del paper reconoce alcance limitado de modelos.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---|---|
| Diseño y criterios | PDF/Markdown local | §§3.1–4.3 | No verificada | Método |
| Métricas y protocolo | PDF/Markdown local | §5.1 | No verificada | Evaluación |
| Tabla 3 y Pass@1 reportado | PDF y raster local | 7 (rango revisado 4–10) | No verificada | Resultado; cotejo visual |

## Pendientes
Completar autores si se requiere cita exhaustiva, verificar artefactos y revisar el PDF íntegro para detalles no incluidos en la extracción.
