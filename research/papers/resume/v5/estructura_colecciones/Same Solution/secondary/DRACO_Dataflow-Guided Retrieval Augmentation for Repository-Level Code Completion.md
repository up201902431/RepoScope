# Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion

## Identidad
- **paper_id:** provisional `draco-dataflow-guided-retrieval`; sin ID canónico local.
- **Título:** *Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion*.
- **Autores:** Wei Cheng, Yuhan Wu y Wei Hu.
- **Año/venue:** ACL 2024, 62nd Annual Meeting of the Association for Computational Linguistics, vol. 1: Long Papers, pp. impresas 7957–7977. No DOI/arXiv ID visible en el ejemplar ACL local.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/DRACO_Dataflow-Guided Retrieval Augmentation for Repository-Level Code Completion.md`; PDF homónimo.
- **Versión/alias:** ILC cita un preprint `arXiv:2405.19782` con mismo título, autores y año; posible versión anterior del mismo trabajo, no cotejada directamente. El PDF local corresponde a ACL.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** Markdown completo, con apéndices; PDF local de 21 páginas físicas. Portada y páginas 7–8 con tablas cotejadas visualmente; no inspección visual de todo el PDF.

## Pregunta y contribución
**Hecho:** DRACO recupera contexto de código guiado por flujo de datos para completar la línea editada en Python.

**Interpretación:** su grafo asocia entidades y dependencias de código; no enlaza documentos a APIs recuperadas ni filtra documentos por requisito.

## Método
- **Entrada/salida:** código incompleto antes del cursor y contexto del repositorio → línea completada.
- **Indexación:** grafo de entidades para módulos, clases, funciones y variables; propiedades incluyen docstrings y, para funciones, cuerpo.
- **Relaciones:** `assigns`, `as`, `refers`, `typeof`, `inherits`; analiza importaciones/uso del código incompleto.
- **Recuperación:** selecciona entidades relacionadas y las ordena/ensambla como código. Los alcances `definition` y `complete` difieren en inclusión de implementaciones y sentencias variables.
- **Dependencias:** parser/análisis de flujo de datos y modelos de generación; adaptación a otros lenguajes no demostrada.

## Documentos y arquitectura
El grafo incluye docstrings como atributos de entidades, pero la salida recuperada se describe como código. No evalúa documentación como unidad de recuperación, ni arquitectura documental o cambios/versiones.

## Evaluación
- **Benchmarks:** subconjunto Python de CrossCodeEval y ReccEval, más ReccEval propio en Python.
- **Modelos/métricas:** siete familias/tamaños de LLM; EM, similitud de edición, ID.EM, F1 y tiempo de generación del prompt.
- **Resultados localizables:** Tablas 3–4 (PDF pp. 7–8) reportan aumentos promedio absolutos de EM/F1 frente a RepoCoder en CrossCodeEval; hay excepciones por modelo en ReccEval (p.ej., CodeGen-350M). Tabla 5 reporta 40 ms frente a 4.062 ms para generación del prompt en CrossCodeEval con CodeGen-350M; no incluye tiempo de generación del LLM. Tablas inspeccionadas visualmente.
- **Límites:** comprensión de contexto largo, intención ambigua, adaptación a otros lenguajes; el artículo señala incertidumbre de contaminación en entrenamiento Code Llama/GPT. La variante multilínea está en apéndice y tiene resultados más limitados.

## Artefactos
El artículo declara código y datos en `github.com/nju-websoft/DraCo`; no se comprobó acceso, contenido, versión, licencia ni ejecución.

## Relación con nuestra tesis
Puede inspirar recuperación estructural de contexto, no selección documental. Sus métricas de identificadores no son API P/R/F1 de la tesis.

## Riesgos
El posible preprint citado no se verificó directamente; no afirmar equivalencia de versión como hecho. La presencia de docstrings no convierte el método en recuperación documental.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Título y edición ACL | Markdown y raster de portada | 1 | Hecho, cotejado visualmente |
| Grafo y flujo de recuperación | Markdown; §§3–4 | 3–5 | Hecho |
| Benchmarks/métricas | Markdown; §4 | 5–6 | Hecho |
| Tablas de resultados y tiempos | Markdown; Tablas 3–5; rasters inspeccionados | 7–8 | Hecho reportado |
| Preprint 2405.19782 posiblemente relacionado | ILC, referencias; portada DRACO | ILC p. 20; DRACO p. 1 | Interpretación, pendiente de cotejo |
| Relación con selección documental | Brief frente al método | No aplica | Interpretación |

## Pendientes
Verificar relación de versiones solo con acceso autorizado. Artefactos no comprobados.
