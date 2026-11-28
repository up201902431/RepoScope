# Ficha — API-Repo

## Identidad
- **Título:** *API-Repo* (título completo, autores y venue no verificados en esta ficha).
- **Fuente:** Extracción PyMuPDF; PDF físico paginado desde 1.
- **Grupo:** Same Solution / terceary / not_processed (ubicación de clasificación de origen).
- **Cobertura:** Lectura íntegra reportada en sesión previa; no inspección visual.

## Pregunta y contribución
Recuperar APIs útiles del repositorio a partir de llamadas/API similares y APIs potencialmente aplicables, incluyendo clases base. La tarea reportada es completion/reutilización de API, no reparación ni generación documental.

## Método
Recuperación API-aware que usa similitud de llamadas y relaciones entre APIs/clases; los snippets/contextos recuperados guían generación de código. Debe mantenerse distinto de un selector de documentos: la salida principal son candidatos API/código.

## Documentos y arquitectura
Entidades de código, llamadas API y posibles relaciones de herencia. No evidencia de documentación humana/generada enlazada explícitamente a cada API.

## Evaluación
RepoEval y CrossCodeEval; EM/ES e identificadores reportados en el artículo. Valores concretos pendientes de cotejo de tablas. No se verificaron ejecuciones ni baselines localmente.

## Artefactos
No verificados.

## Relación con nuestra tesis
Muy próximo en fijar/recuperar APIs, por tanto importante para delimitar aporte. La diferencia candidata es usar documentación relacionada a esas APIs ya recuperadas, manteniendo el set API del baseline fijo. Evitar afirmar novedad sin comparación completa.

## Riesgos
Resolución de APIs puede depender de aliases, herencia, imports y análisis estático; fallos en parseo alteran conjuntos. API overlap no prueba corrección funcional.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Retrieval de llamadas similares y APIs potencialmente utilizables, incluidas clases base. | Extracción del paper | Abstract/Method, pp. 1–5 | Método reportado |
| Evaluación en RepoEval y CrossCodeEval con EM/ES/identificadores. | Extracción del paper | Evaluation, pp. 6–10 | Métricas reportadas |

## Pendientes
Completar metadatos, algoritmo y cifras/baselines; examinar reglas de identidad API y verificar repositorio.
