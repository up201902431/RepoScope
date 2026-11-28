# Ficha canónica de paper

## Identidad
- **paper_id:** large-language-models-software-engineering-slr
- **Título:** *Large Language Models for Software Engineering: A Systematic Literature Review*
- **Autores:** Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, Haoyu Wang.
- **Año/venue verificados:** 2024; ACM Transactions on Software Engineering and Methodology, vol. 33, no. 8, artículo 220.
- **DOI:** 10.1145/3695988.
- **Fuente original:** revisión sistemática extraída de PDF local.
- **PDF/texto y procedencia:** `research/papers/pdf/Other/diss prop bibl/Large Language Models for Software Engineering.pdf`; texto Markdown paralelo en `research/papers/text/v5/estructura_colecciones/Other/diss prop bibl/Large Language Models for Software Engineering.md`. Extracción PyMuPDF automática, fecha 2026-11-24, no verificada manualmente.
- **Paginación:** 79 páginas físicas numeradas desde 1; impresión ACM aparece como 220:1–220:79.
- **Grupo/etiquetas:** Other / v5 / SLR / LLM4SE.
- **Aprobación:** no disponible en esta ficha.
- **Cobertura de lectura:** exhaustiva del documento completo de 79 páginas físicas que proporcionó el lote; survey secundario, no lectura de sus 395 estudios primarios ni de las referencias individuales.

## Pregunta y contribución
**Evidencia:** RQ1-RQ4 buscan mapear modelos usados en SE, datos/datasets, técnicas de optimización/evaluación y tareas SE abordadas. Selecciona 395 artículos primarios publicados entre enero de 2017 y enero de 2024 mediante búsqueda manual, automatizada y snowballing. Clasifica arquitecturas encoder-only, encoder-decoder y decoder-only; resume datos, tuning, prompts, métricas y tareas.

**Interpretación:** Es útil como mapa taxonómico y evidencia indirecta de tendencias, no como evaluación de repositorios ni de componentes específicos de esta tesis. El rango temporal y el sesgo hacia arXiv deben atenuar afirmaciones de estado del arte.

## Método
- Entrada/salida: artículo primario: datos de modelo, dataset, técnica de adaptación, métrica y tarea SE.
- Unidad y contexto: tareas agrupadas en RE, diseño, desarrollo, aseguramiento de calidad, mantenimiento y gestión.
- Recuperación: QGS, siete bases, manual, forward/backward snowballing y deduplicación.
- Generación: no propone un generador; clasifica usos de LLM.
- Granularidad: estudio/artículo y taxonomía por tarea.
- Dependencias: calidad de búsquedas, criterios de inclusión/exclusión, evaluación subjetiva; el estudio admite sesgo posible de selección y omisión.

## Documentos y arquitectura
- Origen: fuente secundaria humana/publicada.
- Tipo: survey/SLR, sin arquitectura de documentación de repositorio propia.
- Texto/modelo/diagrama: texto, tablas, figuras de distribución y taxonomías de modelos.
- Versión: revisión 2024 con corte 31-01-2024.
- Generador: no aplica.
- Filtrado por requisito: no propone selección de documentación según requisitos; sí identifica datasets textuales, code-based y combinados.

## Evaluación
- Corpus: 395 artículos primarios; 154 peer-reviewed y 241 arXiv según el recuento del paper.
- Selección/exclusiones: artículos <8 páginas, duplicados, tesis/libros/keynotes, demos, workshops, grey literature, no inglés y otros filtros detallados.
- Métricas principales: precisión, recall, F1, accuracy, AUC, MRR, BLEU/Pass@k, Exact Match, Edit Similarity y otras por tipo de tarea.
- Resultados localizables: 56.65% del corpus cae en desarrollo y 22.71% en mantenimiento; code generation y program repair son tareas dominantes.
- Límites: predice correlaciones de atención y uso, no causalidad; depende de búsquedas históricas y sesgo de publicación.

## Artefactos
- **Artefacto oficial:** https://github.com/security-pride/LLM4SE_SLR
- El Markdown local declara verificación fechada 2026-11-24 solo para la extracción, no para la disponibilidad o reproducibilidad del repositorio.
- No se ejecutaron enlaces ni experimentos.

## Relación con nuestra tesis
Coincide en que la generación de código puede combinar código, texto de repositorio y contexto. Diferencia: no evalúa pipelines de documentación generada/humana, arquitectura enlazada ni evolución; por ello debe usarse como panorama, no como baseline de RepoScope.

## Riesgos
- Contaminación entre train/test, datos industriales escasos y sesgo industrial/abierto.
- Ambigüedad en generación, desactualización, coste de cómputo y falta de interpretabilidad.
- El gran corpus incluye artículos arXiv no peer-reviewed; las cifras no prueban superioridad generalizable.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| El estudio revisa 395 artículos de 2017 a enero de 2024 y define RQ1-RQ4 | Archivo Markdown y PDF local | Abstract, física 1 / impresa 220:1; §2 física 4 / impresa 220:4 | Evidencia |
| La búsqueda combina QGS, siete bases y snowballing; aplica criterios de calidad | Archivo local | §2.2-2.4, físicas 5-8 / impresas 220:5-220:8 | Evidencia |
| Clasifica LLM como encoder-only, encoder-decoder y decoder-only | Archivo local | §3.1, físicas 10-11 / impresas 220:10-220:11 | Evidencia |
| Destaca preprocesado de datos, tipos de entradas y preprocesamiento | Archivo local | §4.1-4.4, físicas 14-20 / impresas 220:14-220:20 | Evidencia |
| Resume PEFT, prompting y métricas | Archivo local | §5.1-5.3, físicas 21-25 / impresas 220:21-220:25 | Evidencia |
| Distribuye 85 tareas en seis actividades y code generation es dominante | Archivo local | §6.1, físicas 25-26 / impresas 220:25-220:26 | Evidencia |
| Enumera retos de tamaño, datos, generalización, evaluación y ética | Archivo local | §8.1, físicas 41-43 / impresas 220:41-220:43 | Evidencia |
| Uso limitado de este paper como mapa del corpus; no como prueba de diseño | Interpretación propia | Todo el documento | Interpretación |

## Pendientes
- Verificar el contenido oficial del enlace GitHub y su replicación sin ejecutar.
- Contrastar sus referencias con papers individuales del corpus de RepoScope.
- Determinar qué conclusiones son aplicables a selección de documentos y cuáles solo a code completion/generation.
