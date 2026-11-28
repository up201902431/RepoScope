# CODEAGENT

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador provisional: `CodeAgent`.
- **Título:** *CODEAGENT: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges*.
- **Autores:** Kechi Zhang, Jia Li, Ge Li, Xianjie Shi y Zhi Jin.
- **Versión:** copia identificada como `arXiv:2401.07339v2`, 9-ago-2024. DOI/venue no verificados.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/CodeAgent.md`; PDF: `research/papers/pdf/Same Solution/primary/CodeAgent.pdf`.
- **Procedencia/cobertura:** lectura íntegra del Markdown declarada por el especialista; imágenes locales de páginas físicas 8 y 9 contrastadas. No se inspeccionó visualmente el PDF completo. No hay paginación impresa estable verificada.
- **Grupo/etiquetas:** se conserva `Same Solution/primary`; sin afirmar aprobación formal.

## Pregunta y contribución
**Hecho del paper:** propone un agente de generación a nivel de repositorio con herramientas externas y benchmark CODEAGENTBENCH.

**Interpretación:** sistema interactivo que puede navegar, ejecutar y revisar código; no es una comparación limpia de recuperación fija más generación.

## Método
- **Entrada/salida/tarea:** requisito/documentación de función o clase, repositorio, dependencias y entorno de ejecución; salida, código generado, con ciclos posibles de herramienta y reparación.
- **Herramientas:** WebSearch, DocSearch (BM25 sobre documentación), SymbolSearch (tree-sitter), FormatCheck (Black) y PythonREPL con feedback de ejecución.
- **Estrategias:** ReAct, Tool-Planning, OpenAIFunc y Rule-based.
- **Granularidad/generación:** funciones y clases; hay feedback de tests/ejecución y la salida puede modificarse iterativamente.
- **Documentación/arquitectura:** el artículo informa repositorios seleccionados con documentación generada con Sphinx; el agente puede resumir resultados largos con un LLM. No se determinó si todo el contenido de origen es humano o generado. No produce documentación arquitectónica como resultado.

## Documentos y arquitectura
DocSearch recupera documentación y SymbolSearch localiza símbolos; el paper no presenta un mecanismo explícito de enlace requisito→documento→API ni procedencia por afirmación. WebSearch introduce fuentes fuera del repositorio. La documentación Sphinx se usa como recurso de recuperación, no como salida evaluada.

## Evaluación
- **Benchmark:** CODEAGENTBENCH: 101 funciones/clases en seis repositorios Python, con suites de tests de los repositorios; el artículo describe aproximadamente 600 horas-persona para construirlo.
- **Modelos/métrica:** nueve LLMs; Pass@1. También se reporta HumanEval y comparación manual de productos comerciales en subconjunto.
- **Resultados reportados:** Tabla 3: GPT-4-turbo pasa de 21,8 sin agente a 37,6 con estrategia rule-based (+15,8 puntos). El artículo informa mejoras de 2,0 a 15,8 puntos según modelo/estrategia.
- **Límites:** posible contaminación de preentrenamiento, herramientas simples, comparación manual con productos y sensibilidad a prompts, según el paper.

## Artefactos
Esta lectura no comprobó contenido o accesibilidad de implementación/paquete ni ejecutó comandos. Las herramientas descritas en el artículo no equivalen a artefactos reproducidos.

## Relación con nuestra tesis
**Interpretación acotada:** evidencia de recuperación de documentación y navegación de símbolos dentro de un agente. No propone seleccionar documentos vinculados a APIs según requisito ni separa el aporte documental del de búsqueda web, ejecución y reparación. No es baseline directamente equiparable a RepoScope sin aislar esas capacidades.

## Riesgos
- WebSearch implica acceso remoto y resultados variables; el artículo dice bloquear sitios que puedan causar filtraciones, pero no se verificó el alcance de ese control.
- La ejecución y reparación amplían las capacidades respecto de un pipeline de generación fijo.
- Procedencia y contenido de la documentación Sphinx, además del corte temporal de fuentes web, no quedaron establecidos aquí.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---|---|
| Identidad de la copia arXiv | PDF/Markdown local | 1–2 | No estable/verificada | Metadato |
| Herramientas, tarea y estrategias | PDF/Markdown local | §§3–4.2, 3–6 | No estable/verificada | Método |
| Resultados de CODEAGENTBENCH | PDF y raster local | 8–9 | No estable/verificada | Resultados reportados |

## Pendientes
Verificar procedencia de la documentación Sphinx, política temporal de WebSearch y artefactos; cualquier comparación debe controlar ejecución, reparación y acceso web.
