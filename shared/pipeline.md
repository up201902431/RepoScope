# Pipeline candidato — edición 2

Estado: plan de investigación; las herramientas son candidatas. No constituye lista obligatoria de integraciones.

## 1. Selección y preparación
Inventariar proyectos/tareas de CoderEval, DevEval y RepoExec. Confirmar compatibilidad, commits, tests, disponibilidad documental y requisitos. Detectar duplicados o solapamientos. Registrar inclusiones/exclusiones antes de resultados.
Separar proyectos/tareas de desarrollo de evaluación final y congelar configuración tras el piloto.

## 2. Vista permitida del repositorio
Definir y preparar una vista sin solución objetivo ANTES de generar índices, documentos o modelos. Controlar clases completas, callers, ejemplos, diffs, historial, caches y acceso remoto.
No asumir que borrar el cuerpo del prompt final elimina la fuga previa.

## 3. Documentación y estructura
- Humana: conservar la disponible, con versión y origen.
- APIs/archivos/directorios: RepoDocsAgent de RepoMind como candidato.
- Documentación global/arquitectónica: CodeWiki como candidato.
- Recuperación de módulos/estructura: SemArc como candidato distinto.
- Resúmenes entre dos versiones: ChangeWiki como línea temporal opcional.
- Diagramas desde texto: no hay generador elegido; no atribuir a ArDoCo.
Definir criterio de escasez sin mirar rendimiento final. No asumir documentación generada solo por ausencia de carpeta docs/.

## 4. Enlaces
- Mantener procedencia al generar documentos: archivo, entidad, commit y configuración.
- Requisitos-código: TAROT/FTLR e IRBM son candidatos a estudiar, no cadena obligatoria.
- Texto arquitectónico-modelo: ArDoCo.
- Modelo estructurado-código: ArCoTL.
- Texto arquitectónico-código vía modelo: TransArC.
- Selección requisito-fragmento documental: componente pendiente; candidatos simples lexicales/embeddings y reranking a validar.
Procedencia no prueba exactitud semántica; evaluar muestra de enlaces y afirmaciones.
No asumir compatibilidad entre modelos SemArc, diagramas CodeWiki y entradas de TransArC.

## 5. Generación principal
Requisito → recuperación de APIs con baseline → documentos asociados a esas APIs → selección según requisito → contexto enriquecido → generación.
Mantener APIs fijas en comparación central. Si TAROT/FTLR/IRBM cambian APIs, registrar una variante experimental separada.

## 6. Evaluación
Reproducir baseline y medirlo con evaluador común propio son actividades distintas.
Empezar en RepoScope; RepoMind adicional si viable. Pass@1 y API P/R/F1 pendientes de cierre operativo.
Distinguir documento humano/generado/mixto; disponibilidad y coste. Calidad de enlaces no equivale a API F1.

## 7. Historia
Mínimo: procedencia y snapshots reproducibles.
Extensión: recuperación de historia, mantenimiento de enlaces o resúmenes de evolución. Cada uso requiere condición y política temporal propia. No permitir versiones futuras respecto al corte experimental.

## Experimentos candidatos, no aprobados
Baseline; + documentos sin enlace explícito; + documentos enlazados sin filtro; + enlazados y filtrados. Separar origen documental y presupuesto. No ejecutar factorial completo automáticamente.

## Entregable mínimo antes de ampliar
Un piloto reproducible con un generador o corpus, un mecanismo de asociación y un selector, sin necesidad de integrar todas las alternativas.
