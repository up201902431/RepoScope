# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título extraído: *COCOGEN — Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/terceary/less important/02_IterativeRefinement.md`
- cobertura: Markdown íntegro; PDF no cotejado sistemáticamente

## Pregunta y contribución
Mejorar generación Python dependiente de proyecto refinando iterativamente contexto y código según feedback estático/de compilador.

## Método
- entrada: requisito y contexto de proyecto
- recuperación/análisis estático: identifica incompatibilidades
- feedback de compilador: guía refinamiento
- salida: código generado corregido
- modelos mencionados: GPT-3.5-Turbo y Code Llama 13B

## Documentos y arquitectura
- no genera documentación
- usa dependencias y contexto de proyecto
- no enlaza documento/requisito/API

## Evaluación
- generación Python con feedback
- extracción reporta más de 80% de mejora frente a modelos base en contexto dependiente
- cifras exactas, fórmulas y selección requieren cotejo

## Artefactos
- disponibilidad no verificada

## Relación con nuestra tesis
Aporta retroalimentación estática como posible criterio de selección o validación de contexto, no reemplaza documentación ni recuperación de API.

## Riesgos
- mejora declarada no comparable sin resultados completos
- corrección de compilación no implica corrección funcional
- acceso al repositorio objetivo puede causar fuga

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Método de feedback iterativo | mismo archivo | abstract, método y evaluación; páginas impresas 2336–2353 según extracción | Hecho extraído |
| Resultados y modelos | mismo archivo | evaluación | Hecho reportado |

## Pendientes
- verificar título, autores, venue y metadatos
- cotejar tablas y métricas
- confirmar artefacto y particiones
