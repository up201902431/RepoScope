# RepoTransBench

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoTransBench`.
- **Título:** *A Real-World Multilingual Benchmark for Repository-Level Code Translation*.
- **Autores/año/venue:** Yanli Wang et al.; IEEE TSE 52(2), febrero de 2026. DOI `10.1109/TSE.2025.3645056`.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/repoTransBench.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, preservado.
- **Cobertura:** lectura íntegra del Markdown declarada; Tabla IV revisada visualmente en página local 10. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** benchmark multilingüe de traducción de código a nivel de repositorio y sistema RepoTransAgent.

**Interpretación:** tarea distinta a generación de una función condicionada por documentación.

## Método
1.897 muestras y 13 pares direccionales entre siete lenguajes; pruebas ejecutables a nivel de repositorio.

## Documentos y arquitectura
La tarea traduce código/repositorios; no genera documentación ni selecciona documentos vinculados a APIs.

## Evaluación
SR exige que todos los tests de una tarea pasen; CR mide compilación; APR promedia la fracción de tests pasados por repositorio; AMPR promedia módulos de prueba totalmente aprobados. Mejor SR reportado: 32,8 % para RepoTransAgent; éxito varía ampliamente por dirección lingüística. Las métricas no son intercambiables ni de API.

## Artefactos
El paper declara código y datos en GitHub; disponibilidad, licencia y ejecución no verificadas.

## Relación con nuestra tesis
Aporta ejemplo de agregación de tests y evaluación multilingüe; no es baseline directo de la tesis.

## Riesgos
El resultado depende de dirección de traducción y repositorios; no extrapolar desde traducción a generación documentalmente enriquecida.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Métricas | PDF/Markdown local | §V-C, física 9 | 683 | Definiciones |
| Resultados y Tabla IV | PDF y raster local | §VI-A, física 10 | 684 | Resultado; cotejo visual |

## Pendientes
Verificar artefactos y considerar las direcciones lingüísticas por separado si se compara cobertura de tests.
