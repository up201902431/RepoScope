# One Size Does Not Fit All

## Identidad
- **paper_id:** no asignado; identificador local provisional `oneSize`.
- **Título:** *One Size Does Not Fit All: Revisiting Code Context Engineering for Repository-Level Code Generation*.
- **Autores/año/venue:** Yichen Li et al.; Proc. ACM Software Engineering, FSE131, julio de 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/less important/oneSize.md`; PDF `research/papers/pdf/Evaluation/less important/oneSize.pdf`.
- **Grupo:** se conserva `Evaluation/less important`.
- **Cobertura:** lectura íntegra del Markdown y contraste visual de Tabla 6 según informe del lote; PDF completo no inspeccionado visualmente.

## Pregunta y contribución
**Hecho:** compara estrategias de ingeniería de contexto para generación de código a nivel de repositorio.

**Interpretación:** antecedente de diseño de comparaciones de adquisición de contexto, no evidencia directa sobre selección documental.

## Método
Compara diez métodos de tres paradigmas: ICL por similitud, análisis estático y navegación. Corpus de 439 tareas: 230 CoderEval, 115 tareas muestreadas de DevEval y 94 RepoClassBench. El trabajo indica que eliminó directorios/archivos de tests antes del procesamiento. Adapta distintos métodos, incluido A³-CodGen.

## Documentos y arquitectura
Los métodos estudian contexto de código. No se evalúa un módulo de documentación enlazada a APIs ni arquitectura documental.

## Evaluación
Ocho modelos; Pass@1, tiempo de preparación, llamadas/tokens y DCR. DCR usa dependencias cross-file de referencia obtenidas por instrumentación de tests: cobertura recuperada por el método de contexto, no uso por el generador ni API F1. SAFile mejora respecto al baseline en las tablas para tareas de función; navegación logra resultados altos con modelos capaces, con mayor coste y llamadas.

## Artefactos
El artículo declara framework, métodos y datos públicos. Estado, licencia y ejecución no verificados.

## Relación con nuestra tesis
Es antecedente de comparación de adquisición de contexto. No demuestra que un componente documental específico mejore resultados; DCR no sustituye API F1.

## Riesgos
El estudio reconoce amenazas por decisiones de implementación y representatividad de métodos. Las 115 tareas muestreadas de DevEval se solapan con ese benchmark y no son una muestra independiente para comparar resultados sin deduplicación.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Corpus y métodos | PDF/Markdown local | §§3.1–4.3, 6–16 | FSE131:6–16 | Método |
| Comparativa y DCR | PDF y raster local | Tabla 6, física 10 | FSE131:10 | Resultado; cotejo visual |
| Límites | PDF/Markdown local | §§4.3 y discusión | Dentro del rango 6–16 | Amenaza reportada |

## Pendientes
Deduplicar tareas frente a DevEval; separar reproducción publicada de comparación propia y verificar coste/artefactos antes de reutilizar métodos.
