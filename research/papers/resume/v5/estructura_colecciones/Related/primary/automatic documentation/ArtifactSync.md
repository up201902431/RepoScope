# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *ArtifactSync: Automated Repository Synchronization through Hierarchical Change Impact Analysis*
- autores: Ebube Alor, João Pedro de Souza Olivo Tardivo, SayedHassan Khatoonabadi y Emad Shihab
- año/venue: 2026, ICSE-Companion ’26, Río de Janeiro
- DOI: `10.1145/3774748.3787617`
- fuente original: extracción PyMuPDF
- PDF/texto: `research/papers/pdf/Related/primary/automatic documentation/ArtifactSync.pdf`; `research/papers/text/v5/estructura_colecciones/Related/primary/automatic documentation/ArtifactSync.md`
- imágenes: `research/papers/images/v5/estructura_colecciones/Related/primary/automatic documentation/ArtifactSync/page-01.png` a `page-04.png`
- cobertura: texto íntegro; portada y páginas 1–4 cotejadas visualmente

## Pregunta y contribución
Detectar artefactos potencialmente afectados por un cambio de código y evaluar si quedaron inconsistentes, explicando y proponiendo reparaciones.

## Método
- entrada: repositorio, README, `.gitignore`, diff y commit seleccionado
- tarea: análisis de impacto y sincronización de artefactos
- análisis: extensiones progresivas desde nombre e overview hasta contenido completo
- salida: artefactos afectados/inconsistentes, explicación y propuesta de reparación aplicable/rechazable
- arquitectura: backend Python de análisis, consistencia y recomendaciones; extensión VS Code
- proveedores declarados: OpenAI, Gemini y Anthropic

## Documentos y arquitectura
- trabaja sobre README, documentación y otros artefactos, pero no genera documentación inicial de API desde cero
- integra trazabilidad cambio→artefacto→propuesta
- no selecciona documentos por requisito ni fija APIs recuperadas

## Evaluación
- 10 commits individuales por repositorio en Crawl4AI y Unity Catalog
- commits grandes adicionales: prueba de estrés con cambios combinados
- Crawl4AI: 10/10 en escenarios individuales
- Unity Catalog: impacto 10/10; arreglos correctos parciales en 8/10 en escenarios individuales
- commit grande combinado: impacto 16/20 (80%), recomendación 15/20 (75%), arreglo 13/20 (65%)
- fórmulas y configuración completa no disponibles en el texto revisado

## Artefactos
- anuncia backend en `github.com/Alor-e/artifact-sync-backend` y extensión VS Code en `github.com/Alor-e/artifact-sync`
- PDF declara licencia CC BY 4.0
- disponibilidad externa, versión, licencia práctica y ejecución no verificadas

## Relación con nuestra tesis
Antecedente acotado de mantenimiento de consistencia entre código y documentación. Puede informar cómo preservar/sincronizar artefactos después de cambios, no el módulo que selecciona documentación ligada a APIs para mejorar generación.

## Riesgos
- acceso al diff/commit objetivo podría revelar una solución si se usa como preprocesamiento de generación
- estructura anidada produjo fallos reportados
- evaluación pequeña y ad hoc; no extrapolar a Pass@1/API F1

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Identidad, DOI y licencia | PDF/e extracción | PDF físico p. 1 / impresa 105 | Hecho cotejado |
| Arquitectura y flujo | PDF/extracción | físico pp. 2–3 / impresas 106–107 | Hecho |
| Diseños y cifras | PDF/extracción | físico p. 4 / impresa 108 | Hecho reportado |

## Pendientes
- comprobar disponibilidad y ejecución reales
- cerrar modelos/configuración, fórmulas y exclusiones
- auditar política temporal si se usa en preprocesamiento
