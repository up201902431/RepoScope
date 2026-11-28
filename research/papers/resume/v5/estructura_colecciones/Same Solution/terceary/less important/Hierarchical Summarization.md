# Ficha canónica — Repository-Level Code Understanding by LLMs via Hierarchical Summarization

## Identidad
- **paper_id:** DOI `10.1007/978-3-031-97576-9_6`.
- **Título:** *Repository-Level Code Understanding by LLMs via Hierarchical Summarization: Improving Code Search and Bug Localization*.
- **Autores:** Amirkia Rafiei Oskooei, Selcan Yukcu, Mehmet Cevheri Bozoglan y Mehmet S. Aktas.
- **Publicación:** capítulo de *Computational Science and Its Applications – ICCSA 2025 Workshops*, LNCS 15886, pp. impresas 88–105; el volumen indica ICCSA Workshops, Istanbul, 30-junio a 3-julio-2025, y el documento lleva copyright Springer 2026. No confundir fechas del evento y del volumen.
- **Fuente local:** `research/papers/text/v5/estructura_colecciones/Same Solution/terceary/less important/Hierarchical Summarization.md`; PDF asociado: `research/papers/pdf/Same Solution/terceary/less important/Hierarchical Summarization.pdf`.
- **Cobertura:** lectura completa del capítulo en la extracción, páginas PDF físicas 157–174 (páginas impresas 88–105), incluyendo método, estudio, conclusión, apéndice y referencias del capítulo. El Markdown contiene además el resto del volumen de actas, que no se leyó. Extracción automática; no se cotejaron visualmente las páginas. Por tanto, las afirmaciones sobre la figura y tabla se basan en sus pies y texto extraído, no en inspección visual.
- **Clasificación:** se conserva `Same Solution/terceary/less important`; no implica aprobación de clasificación.

## Pregunta y contribución
**Hecho del paper:** propone una representación jerárquica de repositorios mediante resúmenes para facilitar comprensión, búsqueda semántica y localización de bugs por LLM, con foco en reportes Jira redactados por usuarios no técnicos.

**Interpretación:** es un método de comprensión y localización de archivos, no de generación de funciones ni selección de APIs.

## Método
- **Entrada:** repositorio, árbol abstracto, reglas y guías del proyecto, README, documentación del proyecto y reporte de bug en lenguaje natural.
- **Preprocesamiento:** crea un resumen de proyecto con un LLM de contexto largo; lo usa para primar un LLM como “context-aware”. Luego resume archivos y agrega esos resúmenes bottom-up en resúmenes de directorios, formando un árbol de conocimiento de tres niveles (raíz, directorio y archivo).
- **Inferencia:** búsqueda top-down. El LLM recibe reporte y resúmenes de directorio para elegir top-k directorios; después recibe resúmenes de sus archivos y elige top-n archivos candidatos.
- **Salida:** ranking/localización de archivos relevantes; no genera un parche ni código.
- **Granularidad:** proyecto → directorio → archivo, con localización final a nivel de archivo.

## Documentos y arquitectura
Utiliza documentación preexistente del proyecto (README, reglas, guías y otros documentos) junto con el código para construir un resumen raíz. Además genera resúmenes de archivos y directorios. Los resúmenes forman una representación contextual para comprensión y localización; no se usan para elegir APIs de implementación ni se combinan con APIs para generar una función. No produce un modelo arquitectónico o diagrama formal.

## Evaluación
- **Dataset:** un repositorio Java privado de arquitectura de microservicios: 743 archivos, de los que 474 son Java, y 95.873 líneas de código. 86 issues Jira de bugs reportados por usuarios finales; la tabla describe 9 reporters. El número de issues y el número de reporters no son intercambiables.
- **Baselines:** Flat Retrieval con UnixCoder y ModernBERT más FAISS KNN; y herramientas comerciales Codeium y Cursor, tratadas como LLM+RAG. El artículo identifica GPT-4o para su método y declara selección de GPT-4o como modelo para comparación LLM, pero las herramientas comerciales son cajas negras y su configuración interna no queda detallada.
- **Métricas:** Pass@10 = presencia de al menos un archivo relevante en los diez primeros; Recall@10 = proporción de archivos relevantes recuperados en el top-10.
- **Resultados reportados en Tabla 2, p. impresa 101 / PDF física 170:** método propuesto GPT-4o: Pass@10 0,89; Recall@10 0,33. Cursor AI GPT-4o: 0,67 y 0,26. Codeium GPT-4o: 0,67 y 0,24. ModernBERT: 0,22 y 0,11. UnixCoder: 0,22 y 0,14. Son resultados del paper bajo su estudio; no se reejecutaron aquí.
- **Límites:** evaluación en un único repositorio privado y 86 issues; las herramientas comerciales son propietarias y sus métodos no son transparentes. Generalización a otros proyectos, lenguajes y tareas queda sin demostrar en este experimento.

## Artefactos
La fuente consultada no permitió verificar un paquete de replicación, licencia, código accesible o ejecución independiente. La disponibilidad del artículo no equivale a disponibilidad o reproducción de los artefactos.

## Relación con nuestra tesis
**Interpretación acotada:** antecedente para resumir jerárquicamente un repositorio y suministrar contexto a un LLM. La tarea evaluada es localizar archivos a partir de issues, no generación funcional. Puede informar una posible vista de contexto de proyecto, pero no demuestra que resúmenes documentales enlazados a APIs mejoren Pass@1 o alineación de APIs.

## Riesgos
- El resumen raíz se genera con el código completo y documentos del proyecto durante preprocesamiento. El artículo no establece con precisión el snapshot temporal usado ni si se excluyó información posterior a los issues; la ausencia de esa descripción deja pendiente el análisis de fuga temporal.
- Los datos del repositorio son privados y la comparación con herramientas propietarias limita la reproducibilidad independiente.
- Pass@10 y Recall@10 miden localización de archivos, no corrección del código generado ni exactitud de enlaces requisito-documento-API.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Título, autores, volumen, DOI y páginas del capítulo | Markdown local, capítulo iniciado en PDF p. 157 | 157 | 88 | Metadato |
| Motivación, tarea y contribución | §1 | 157–160 | 88–91 | Descripción del paper |
| Árbol, LLM contextual y resúmenes bottom-up | §3.1 | 163–165 | 94–96 | Método |
| Búsqueda top-down de directorios y archivos | §3.2 | 166–167 | 97–98 | Método |
| Dataset, baselines y métricas | §§4.1–4.3 | 168–170 | 99–101 | Evaluación |
| Comparación reportada | Tabla 2, §4.4 | 170 | 101 | Resultado reportado |
| Conclusión y alcance futuro | §5 | 171 | 102 | Conclusión del paper |
| Ejemplos de prompts y versiones de herramientas | Apéndice A | 172 | 103 | Evidencia del paper |

## Pendientes
Verificar si existe artefacto oficial y su contenido; aclarar snapshot del repositorio y política temporal frente a cada issue; revisar visualmente Figuras 2–6 y Tabla 2; evaluar generalización fuera del repositorio privado. No usar estos resultados como evidencia de mejora en generación de código.
