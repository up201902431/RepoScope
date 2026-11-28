# HumanEvo

## Identidad
- **paper_id:** no asignado; identificador local provisional `HumanEvo`.
- **Título:** *An Evolution-aware Benchmark for More Realistic Evaluation of Repository-level Code Generation*.
- **Autores:** Dewu Zheng et al.
- **Año/venue:** la portada extraída consultada no permitió verificar venue/año impreso; se conserva como dato pendiente.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/HumanEvo.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, preservado.
- **Cobertura:** lectura íntegra del Markdown declarada; Tabla II visualizada. Página impresa no visible en la imagen consultada; PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** benchmark con contexto del repositorio en estado evolutivo previo al commit objetivo y condición que ignora evolución.

**Interpretación:** antecedente relevante para fijar corte temporal, no garantía de ausencia de contaminación.

## Método
400 tareas: 200 Python y 200 Java. Contrasta contexto anterior al commit con versión más nueva; incluye análisis de dependencias y métodos de adquisición de contexto.

## Documentos y arquitectura
La intervención compara vistas/versiones de código y contexto; no evalúa documentación vinculada a APIs.

## Evaluación
Siete modelos; Pass@1 sobre tests ejecutables, temperatura 0,8 y promedio de tres repeticiones. Se observan caídas bajo contexto evolutivo frente a última versión. Pass@1 mide corrección funcional bajo ese protocolo, no API alignment.

## Artefactos
El paper declara replicación, código y dataset en GitHub. No se verificaron disponibilidad, licencia ni ejecución.

## Relación con nuestra tesis
Antecedente fuerte para política temporal/historial. El manifiesto de información permitida del experimento propio debe identificar commit, cuerpo objetivo y derivados.

## Riesgos
La muestra y los modelos no prueban contaminación cero. Usar última versión puede exponer cambios futuros respecto al objetivo.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---|---|
| Diseño evolutivo | PDF/Markdown local | §§C–V, física 7 | No verificada | Método |
| Tabla II | PDF y raster local | 7 | No verificada | Resultado; cotejo visual |
| Tablas II–IV | PDF/Markdown local | 7 | No verificada | Comparación reportada |

## Pendientes
Verificar metadatos editoriales, artefactos y commits/cortes exactos antes de adoptar el benchmark.
