# GraphCoder

## Identidad
- **paper_id:** provisional `graphcoder`; sin ID canónico local.
- **Título:** *GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph*.
- **Autores:** Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin y Qianxiang Wang.
- **Año/venue:** ASE ’24; pp. impresas 570–581; DOI `10.1145/3691620.3695054`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/GraphCoder.md`; PDF homónimo en la carpeta paralela.
- **Versión/alias:** ILC cita preprint `arXiv:2406.07003` con autores coincidentes y título formulado de otra manera; posible versión previa, no comparada directamente.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo; PDF local de 12 páginas físicas. Portada y tablas de pp. 8–9 cotejadas visualmente; no inspección integral.

## Pregunta y contribución
**Hecho:** GraphCoder recupera fragmentos de código para predecir la siguiente sentencia en completion de repositorio mediante un grafo de contexto y recuperación coarse-to-fine.

**Interpretación:** el grafo puede inspirar recuperación estructural; no representa documentación ni selecciona documentos por requisito.

## Método
- **Entrada/salida:** contexto de completion y repositorio → siguiente sentencia.
- **Grafo:** por sentencia, combina CFG, DDG y CDG.
- **Recuperación:** consulta estructurada; filtro de candidatos por similitud de secuencias; reranking con distancia de edición de subgrafo y decaimiento según distancia.
- **Generación:** LLM recibe fragmentos recuperados y contexto de completion.

## Documentos y arquitectura
Corpus de fragmentos de código. No trata documentación humana/generada, arquitectura documental ni evolución.

## Evaluación
- **Benchmark:** RepoEval-Updated, 8.000 tareas, Python/Java, 20 repositorios; tareas line-level y API-level.
- **Baselines/métricas:** No RAG, Vanilla RAG, Shifted RAG y RepoCoder; EM/ES de código, EM/F1 de identificadores, además de tiempo, almacenamiento y tokens.
- **Resultados localizables:** artículo reporta mejoras medias de +6,06 en EM de código y +6,23 en EM de identificadores frente a baselines RAG. Tabla 2 por modelo/lenguaje/nivel en PDF p. 8; Tabla 3 de ablación en p. 9, ambas cotejadas visualmente.
- **Límites:** repositorios abiertos Python/Java; generalización a otros lenguajes/repositorios pendiente. Baja duplicación puede reducir recall. ID-F1 no es API P/R/F1.

## Artefactos
No se localizó en el cuerpo leído declaración de disponibilidad del artefacto específico GraphCoder. No se comprobó fuera del texto ni se atribuyó disponibilidad de proyectos citados.

## Relación con nuestra tesis
Una posible fuente de ideas para recuperar contexto estructural, pero requiere adaptar el selector a documentos explícitamente enlazados a APIs recuperadas y requisitos. No es evidencia de la hipótesis documental ni baseline alternativo aprobado.

## Riesgos
El preprint citado por ILC no se cotejó directamente. Resultados de RepoEval-Updated no son intercambiables con RepoScope o métricas de la tesis.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad y DOI | Markdown y raster de portada | 1 | Hecho, cotejado visualmente |
| CFG/DDG/CDG y recuperación coarse-to-fine | Markdown; §§3–4 | 3–5 | Hecho |
| Benchmark y resultados | Markdown; §§5–6; Tabla 2 | 5–8 | Hecho reportado |
| Ablación | Markdown; Tabla 3, raster revisado | 9 | Hecho reportado |
| Posible relación con arXiv 2406.07003 | ILC, referencias; GraphCoder, portada | ILC p. 21; GraphCoder p. 1 | Interpretación |
| Relación con tesis | Brief frente al método | No aplica | Interpretación |

## Pendientes
Verificar versión previa y artefactos solo si se autoriza.
