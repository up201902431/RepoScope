# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *Catmming: An LLM-based Chatbot to Support Self-Regulated Learning in Software Engineering Education*
- tipo: tesis del año anterior
- fuente: `research/papers/text/v5/estructura_colecciones/Related/terceary/last year tesis/Catmming.md`
- cobertura: Markdown íntegro; tablas y tiempos no cotejados sistemáticamente con el PDF

## Pregunta y contribución
Chatbot educativo RAG para apoyar aprendizaje autorregulado en ingeniería de software.

## Método
- entradas: datos Moodle y actividades de aprendizaje
- reformulación de consultas
- recuperación y selección de contexto
- salida: apoyo personalizado al estudiante
- no es generación de código ni documentación de repositorios

## Documentos y arquitectura
- RAG sobre materiales educativos
- sin trazabilidad código-API-documento
- sin arquitectura de repositorio

## Evaluación
- tesis: pruebas funcionales ligadas al modelo de aprendizaje autorregulado y simulaciones
- no evaluación con estudiantes reales
- extracción: 21 pruebas en versión final
- inconsistencias reportadas entre tabla y prosa sobre tiempos de respuesta

## Artefactos
- artefacto/tesis local no verificable como componente reproducible
- disponibilidad, licencia y ejecución pendientes

## Relación con nuestra tesis
Solo sirve como antecedente indirecto de reformulación, recuperación y selección. No aporta evidencia sobre repositorios, APIs o generación de código.

## Riesgos
- dominio educativo diferente
- simulaciones no equivalen a uso real
- cifras de tiempo inconsistentes

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| RAG educativo y flujo | mismo archivo | abstract y PDF pp. 3–4 / impresión según capítulo | Hecho extraído |
| Evaluación y 21 pruebas | mismo archivo | capítulos 7–9 | Hecho extraído |

## Pendientes
- verificar metadatos, tabla de tiempos y paginación
- no reutilizar sus métricas en benchmarks de código
