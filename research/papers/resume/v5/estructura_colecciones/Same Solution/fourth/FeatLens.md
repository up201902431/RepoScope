# Ficha — FeatLens

## Identidad
- **Título:** *FeatLens: Feature-Guided Dependency Retrieval for Repository-Level Code Generation*.
- **Autores/año/versión:** Xutian Li et al.; arXiv:2609.26480v2, fechado en la extracción como 28-10-2026. Metadatos de publicación no verificados por separado.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Same Solution/fourth/FeatLens.md`; extracción PyMuPDF de PDF, paginación física desde 1, no cotejada visualmente.
- **Grupo/etiqueta:** Same Solution / fourth (clasificación de origen; no revalidada).
- **Cobertura:** Lectura íntegra reportada en la sesión previa; contenido de extracción automática. No se inspeccionaron visualmente páginas PDF.

## Pregunta y contribución
Cómo recuperar dependencias dispersas que implementen un requisito funcional, en lugar de devolver solo código semánticamente parecido. FeatLens enlaza descripciones de features con entidades de código a nivel función, selecciona features, crea semillas de dependencias, expande un grafo y filtra candidatos con heurísticas semánticas y estructurales. La etapa online de recuperación se reporta sin llamadas a LLM.

## Método
Indexación offline NL-feature→entidades; búsqueda guiada por requisito y ubicación destino; expansión de grafo y selección sujeta a presupuesto. Es recuperación de contexto para generación de funciones/tareas de repositorio, no generación documental ni reparación por sí sola.

## Documentos y arquitectura
Usa descripciones de features y entidades/relaciones del código. No se reporta en la evidencia leída un corpus de documentación humana o documentación generada, ni un enlace estable a documentos por API. El grafo de código y la relación feature-entidad no deben equipararse automáticamente a ArCoTL/TransArC.

## Evaluación
DevEval y EvoCodeBench. Reporta DR@15 de 0.527 y 0.529, respectivamente, como mejor recall de dependencias entre los baselines evaluados a presupuesto fijo. En DevEval, el contexto recuperado obtiene el mejor Pass@1 no-oráculo con DeepSeek-V3.2 y GPT-5-mini. No inferir causalidad documental: evalúa recuperación de dependencias/features. Los artefactos y la reproducción local no se comprobaron.

## Artefactos
La fuente contiene identificador arXiv; no se verificó repositorio, licencia, disponibilidad de implementación ni comandos. No reproducido.

## Relación con nuestra tesis
Antecedente cercano para seleccionar contexto según un requisito y recuperar dependencias relevantes. Diferencia central: no estudia seleccionar documentación enlazada explícitamente a las APIs recuperadas ni aísla ese módulo sobre RepoScope. Su esquema puede inspirar una alternativa de recuperación, no se integra automáticamente.

## Riesgos
La calidad depende del índice feature-entidad, del grafo y de la cobertura/precisión del análisis. La extracción automática puede perder estructura de tablas/figuras. Los resultados son reportados, no verificados independientemente.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| FeatLens crea índice feature-entidad y expande semillas de dependencias. | Extracción del paper | Abstract e Introduction, p. 1 | Evidencia reportada |
| DevEval/EvoCodeBench; DR@15 0.527/0.529; Pass@1 no-oráculo en DevEval. | Extracción del paper | Abstract, p. 1 | Resultado reportado |
| No llamadas LLM en recuperación online. | Extracción del paper | Abstract, p. 1 | Evidencia reportada |

## Pendientes
Cotejo visual de tablas/figuras, verificación bibliográfica y de artefactos, detalle de protocolo y fugas, y cualquier comparación empírica con RepoScope.
