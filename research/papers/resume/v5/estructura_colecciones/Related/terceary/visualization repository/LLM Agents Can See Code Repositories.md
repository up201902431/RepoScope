# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *LLM Agents Can See Code Repositories*
- fuente: `research/papers/text/v5/estructura_colecciones/Related/terceary/visualization repository/LLM Agents Can See Code Repositories.md`
- cobertura: Markdown íntegro; PDF no cotejado visualmente de forma sistemática

## Pregunta y contribución
Si añadir representación visual de estructura y dependencias ayuda a agentes LLM a resolver issues.

## Método
- tarea: resolución/localización de issues
- entrada: repositorio representado visualmente como grafo
- cuatro modelos multimodales
- salida: candidato/parche o localización

## Documentos y arquitectura
- modalidad visual suplementaria
- no equivale a documentación textual ni a modelo arquitectónico interoperable
- no hay enlace requisito-documento-API

## Evaluación
- 500 instancias de SWE-bench Verified
- visualización sola degrada resultados
- contexto visual complementario puede mantener/mejorar resolución y reducir costo/token
- hasta 26% de reducción según el resumen extraído

## Artefactos
- disponibilidad no comprobada

## Relación con nuestra tesis
Permite distinguir visualización de arquitectura/documentación textual. No prueba compatibilidad entre CodeWiki/SemArc/TransArC ni mejora documental.

## Riesgos
- 500 instancias no garantizan separación/limpieza
- reducción de costo puede depender de modelo y tarea
- representación visual no aporta procedencia semántica

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| Diseño visual y cuatro modelos | mismo archivo | abstract y diseño; PDF físico/impreso referido por extracción | Hecho extraído |
| SWE-bench y 26% | mismo archivo | evaluación | Hecho reportado |

## Pendientes
- verificar título, autores, año/venue y tablas
- comprobar artefacto y fuga
- no asumir interoperabilidad con TransArC
