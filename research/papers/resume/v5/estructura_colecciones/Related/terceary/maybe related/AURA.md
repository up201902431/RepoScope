# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *AURA: Automated Updates And Repository Assistant*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/terceary/maybe related/AURA.md`
- cobertura: Markdown íntegro; diseño impreso de la página no cotejado

## Pregunta y contribución
Marco modular para asistir planificación, codificación, QA y versionado de tareas GitHub.

## Método
- entrada: archivos completos, grafos de código y diffs
- tareas: planificación, implementación, QA y versionado
- proveedores: distintos modelos LLM
- salida: cambios o propuestas y acciones de flujo de trabajo

## Documentos y arquitectura
- no es generador documental ni sistema de trazabilidad
- usa archivos/grafos/diffs como contexto
- no selecciona documentación según requisito

## Evaluación
- ejemplos pequeños de bug fixing
- costes/tokens de algunos issues
- sin benchmark amplio verificable en la extracción

## Artefactos
- texto anuncia marco abierto
- repositorio, licencia y ejecución no comprobados

## Relación con nuestra tesis
Antecedente de agentes sobre repositorios y trabajo de mantenimiento. No es evaluación de documentación ni API F1.

## Riesgos
- diffs pueden revelar soluciones
- inputs visuales/estructurales no equivalen a documentación textual
- evaluación limitada

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Marco modular y entradas | mismo archivo | secciones “Our Approach” y seguridad | Hecho extraído |
| Bug fixing limitado | mismo archivo | evaluación; PDF impresa 223 según extracción | Hecho reportado |

## Pendientes
- verificar título, autores, versión y artefacto
- comprobar split y exposición a soluciones
