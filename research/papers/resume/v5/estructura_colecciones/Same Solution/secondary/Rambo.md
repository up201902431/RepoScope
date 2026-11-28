# Rambo

## Identidad
- **paper_id:** provisional `rambo`; sin ID canónico local.
- **Título:** *Rambo: Enhancing RAG-based repository-level method body completion*.
- **Autores:** Tuan-Dung Bui, Thieu Luu, Thanh-Phat Nguyen, Thu-Trang Nguyen, Hieu Dinh Vo y Son Nguyen.
- **Año/venue:** *Information and Software Technology* 200 (2026), artículo 108322; DOI `10.1016/j.infsof.2026.108322`.
- **Fuente original:** `research/papers/text/v5/estructura_colecciones/Same Solution/secondary/Rambo.md`; PDF homónimo.
- **Versión/procedencia:** artículo de revista, 13 páginas físicas e impresas; portada y Tablas 1–3 y 7 cotejadas con renders locales.
- **Grupo/etiquetas:** Same Solution / secondary, conservados.
- **Cobertura:** lectura completa del Markdown, incluidos referencias/apéndices; cotejo visual selectivo de p. 1, 3–6 y 10. `Rambo`/`RAMBO` son variaciones tipográficas del mismo sistema, no papers separados.

## Pregunta y contribución
**Hecho:** método RAG para completar cuerpos de métodos de repositorio, identificando elementos esenciales de código y recuperando ejemplos de sus usos.

**Interpretación:** puede inspirar recuperación de entidades y usos de APIs, pero los artefactos recuperados son código, no documentación seleccionada por requisito.

## Método
- **Entrada/salida:** firma/contexto circundante y repositorio → cuerpo del método.
- **EEI:** busca métodos de firma/interfaz y nombre similares; genera sketch con LLM; analiza sketch y busca métodos, campos y tipos con nombres similares.
- **RUE:** localiza métodos que usan esos elementos, ordena usos por similitud al sketch y selecciona ejemplos.
- **Generación:** combina métodos de referencia, usos recuperados y contexto para producir cuerpo.
- **Dependencias:** calidad del sketch, herramientas JDT/Joern, corpus y modelo. El artículo informa unos 8 min de preprocesamiento/repositorio y 18 s por solicitud en su configuración.

## Documentos y arquitectura
No usa documentos humanos como fuente central, no genera API/file/module docs ni evalúa arquitectura. Recupera código y usos.

## Evaluación
- **Benchmarks:** Java (470 problemas propios en 26 repositorios; 204 derivados de CoderUJB/Defects4J en 14 proyectos) y 373 problemas Python de RepoEval.
- **Modelos/métricas:** DeepSeek Coder 6.7B, Code Llama 7B y GPT-3.5 Turbo; BLEU, CodeBLEU, compilación, pass@k y EM.
- **Resultados localizables:** Tabla 2, Rambo benchmark con DeepSeek Coder, reporta 50,44 BLEU, 53,20 CodeBLEU, 61,70% compilación y 18,94% EM. Tabla 7, RepoEval Python, informa 46,92 Pass@1 y 20,11 EM con Code Llama. En Defects4J con Code Llama, Tabla 3 informa Pass@k 44,12 para Rambo frente a 46,57 RepoCoder; no hay superioridad uniforme.
- **Límites:** depende de calidad del sketch; puede degradarse con repositorios/referencias mayores; recuperación ruidosa; sin evaluación humana; posibles efectos de memorización. La comparación con Copilot usa solo 50 muestras y no es control equivalente.

## Artefactos
El artículo enlaza sitio/repositorio y dice que datos estarán disponibles bajo petición. No se accedió a enlaces ni se verificaron contenido, licencia, versión o ejecución.

## Relación con nuestra tesis
Útil como idea para identificar entidades y ejemplos de uso; necesitaría añadir documentación enlazada a APIs y filtro por requisito. No es sustituto de RepoScope ni evidencia directa para la pregunta central.

## Riesgos
No resumir como victoria universal; métricas, modelos y benchmarks tienen excepciones. El diseño no aísla un efecto de documentación.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física (impresa) | Tipo |
|---|---|---:|---|
| Identidad/DOI/fechas editoriales | Portada del Markdown/PDF | 1 (1) | Hecho |
| EEI/RUE y sketch | Markdown; §III.1 y Fig. 1 | 3–4 | Hecho |
| Benchmarks y exclusiones | Markdown; §IV.1 y Tabla 1 | 4–5 | Hecho |
| Resultados y excepción RepoCoder | Markdown; Tablas 2–3 y 7; rasters revisados | 6, 9–11 | Hecho reportado |
| Adaptación documental | Brief frente a método | No aplica | Interpretación |

## Pendientes
Artefactos y disponibilidad por petición no comprobados; no ejecutar sin protocolo aprobado.
