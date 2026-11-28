# RepoScope

## Identidad
- **paper_id:** no asignado en el catálogo local; identificador provisional: `RepoScope`.
- **Título:** *RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation*.
- **Autores:** Yang Liu, Li Zhang, Fang Liu, Zhuohang Wang, Donglin Wei, Zhishuo Yang, Kechi Zhang, Jia Li y Lin Shi.
- **Año/venue:** ICSE ’26, 12–18-abr-2026. DOI `10.1145/3744916.3773211`. PDF de 13 páginas, impresas 374–386.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/primary/RepoScope.md`; PDF: `research/papers/pdf/Same Solution/primary/RepoScope.pdf`.
- **Procedencia/cobertura:** lectura íntegra del Markdown declarada por el especialista; portada y rasters locales de páginas físicas 8–10 inspeccionados. PDF completo no revisado visualmente.
- **Grupo/etiquetas:** se conserva `Same Solution/primary`; no implica aprobación formal.

## Pregunta y contribución
**Hecho del paper:** recupera contexto multivista consciente de cadenas de llamadas para generación de funciones en repositorios. Propone Repository Structural Semantic Graph (RSSG), predicción de cadenas de llamadas y serialización que conserva estructura.

**Interpretación:** antecedente del baseline de la tesis, no contribución de documentación ni selección documental.

## Método
- **Entrada/salida/tarea:** firma/docstring del objetivo y repositorio; salida, cuerpo de función.
- **Indexación:** análisis estático del repositorio y RSSG con clases, funciones/métodos y atributos; relaciones estructurales/de tipos, llamadas e imports.
- **Recuperación:** cuatro vistas: callers, cadenas de callees predichas, funciones similares y fragmentos similares. La predicción combina similitud y patrones de llamada de funciones similares; organiza contexto preservando jerarquía.
- **Generación:** prompt con los cuatro contextos; el artículo informa una llamada LLM y temperatura 0 tras indexación.
- **Documentación:** no genera documentación ni recupera biblioteca documental. Puede usar docstrings disponibles como representación de entidades; no equivale a documentación arquitectónica ni a documentos enlazados a APIs por requisito.

## Documentos y arquitectura
RSSG es una representación estructurada derivada del código, con relaciones de llamadas y otras dependencias; no es un modelo arquitectónico generado/documentado ni un enlace de procedencia de documentos.

## Evaluación
- **Benchmarks/subconjuntos:** CoderEval Python, 207 tareas; DevEval, 1.742; subconjunto de generación a nivel API de RepoEval, 1.600.
- **Métricas:** Pass@1 para CoderEval/DevEval; EM/ES para RepoEval.
- **Resultados reportados:** Tabla 2: RepoScope 44,93/55,07/49,28/59,42 en CoderEval y 26,18/41,56/30,02/35,82 en DevEval para los cuatro modelos reportados. El artículo declara máximo aumento relativo de 36,35% frente al mejor baseline bajo esa configuración. Tabla 3 presenta ablaciones; RepoEval reporta EM 40,25 y ES 67,74.
- **Límites:** el paper reconoce evaluación sistemática principalmente en Python, sensibilidad a hiperparámetros y limitaciones de Pass@1 como métrica de calidad.

## Artefactos
El artículo anuncia paquete de réplica en `https://github.com/Lorien1128/RepoScope`. No se comprobó accesibilidad, contenido, licencia ni ejecución. El artículo de RepoMind citado en el informe local afirma que no utilizó código RepoScope y tomó resultados publicados; no se resolvió esta discrepancia externamente.

## Relación con nuestra tesis
**Hecho del proyecto:** `shared/thesis-brief.md` y la decisión D-001 establecen RepoScope como baseline principal; la reproducción informada por el usuario aún no tiene evidencia local enlazada.

**Interpretación acotada:** la comparación central debe mantener recuperador/APIs y añadir el módulo documental como variante separada. RepoScope no incorpora documentación humana/generada enlazada a APIs por requisito.

## Riesgos
- No quedó verificado que cuerpo objetivo y derivados se excluyan antes de indexar RSSG/fragmentos; debe confirmarse antes de considerar controlada la fuga.
- Callers y fragmentos pueden incluir información relacionada con la solución.
- La disponibilidad de contexto de repositorio no implica por sí sola generación multifichero.
- La reproducción reportada por el usuario no fue validada en esta ficha.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Identidad/publicación | PDF/Markdown; raster portada | 1 | 374 | Metadato |
| RSSG, recuperación y generación | PDF/Markdown local | §§2–3, 3–6 | 376–379 | Método |
| Tablas 2–5 | PDF y rasters locales | 8–10 | 381–383 | Resultados reportados |
| Baseline establecido | `shared/thesis-brief.md` y D-001 referido por el brief | No aplica | No aplica | Contexto de tesis |

## Pendientes
Enlazar evidencia local de reproducción (commit y comandos) cuando exista y esté autorizada; verificar protocolo de ocultación del objetivo y versión/contenido del paquete.
