# Clasificación

Importar clasificación existente del usuario antes de asignar grupos. Primary/secondary son sus categorías de lectura; no significan automáticamente estudio primario/revisión secundaria.

reading_group: primary | secondary | other | unassigned.
tags: same-solution; documentation-code; evaluation (combinables).
Estados: classification_status proposed/approved; review_status unread/screened/partial/reviewed.
Unassigned no es other. Los criterios exactos de los grupos están pendientes.

Definiciones temáticas propuestas: same-solution para soluciones cercanas a tarea/mecanismo; documentation-code para documentación, estructura y trazabilidad; evaluation para métricas, benchmarks y validez. Validar con usuario.

Catálogo activo: research/papers/catalog.csv, vacío hasta que se aprueben entradas.
Campos: paper_id,title,authors,year,doi,arxiv_id,version,reading_group,tags,pdf_path,text_path,note_path,review_status,classification_status,classification_reason.
CSV escapado correctamente; tags separados por punto y coma. ID estable, una ficha canónica y originales versionados sin borrado automático.
No añadir herramientas candidatas al catálogo como papers verificados sin metadatos originales.
