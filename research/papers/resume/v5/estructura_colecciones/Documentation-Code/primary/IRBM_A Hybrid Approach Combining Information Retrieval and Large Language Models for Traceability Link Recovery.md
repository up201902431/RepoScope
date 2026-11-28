# A Hybrid Approach Combining Information Retrieval and Large Language Models for Traceability Link Recovery

## Identidad
- **paper_id:** alias provisional `IRBM_A Hybrid Approach Combining Information Retrieval and Large Language Models for Traceability Link Recovery`; no hay identificación de catálogo local disponible.
- **Título:** *A Hybrid Approach Combining Information Retrieval and Large Language Models for Traceability Link Recovery*.
- **Autores:** Izumi Nagata, Israel Mendonça, Kaito Utsunomiya, Yuto Takaki, Keisuke Sasaki y Masayoshi Aritsugi.
- **Año/venue:** SAC ’26, 2026. DOI `10.1145/3748522.3779867`; 9 páginas físicas.
- **Fuente original:** Markdown `research/papers/text/v5/estructura_colecciones/Documentation-Code/primary/IRBM_A Hybrid Approach Combining Information Retrieval and Large Language Models for Traceability Link Recovery.md`; PDF homónimo en `research/papers/pdf/Documentation-Code/primary/`.
- **Procedencia/cobertura:** lectura íntegra de las 9 páginas extraídas. Extracción automática PyMuPDF, no verificada manualmente; tablas y figuras no revisadas visualmente aparte de los rasters referenciados por el Markdown.
- **Grupo/etiquetas:** `Documentation-Code/primary`; sin decisión nueva de clasificación.

## Pregunta y contribución
**Hecho del paper:** recupera enlaces requisito–código en proyectos no vistos combinando similitud semántica de código generado desde requisitos con TF-IDF/IR y un filtrado conservador en dos etapas.
**Interpretación acotada:** aporta una variante que usa generación de código como puente semántico, no conservación de trazabilidad durante generación ni documentación humana.

## Método
- Genera código a partir de cada requisito para cerrar la brecha requisito/código y obtiene embeddings del código generado y del código fuente.
- Calcula similitud semántica por coseno y textual por TF-IDF con VSM, LSI o JS; combina ambas mediante un lambda lineal seleccionado mediante validación.
- Filtra primero módulos por dependencias y una preferencia conservadora del LLM; luego recorta enlaces inferiores según correlación de rankings textual/semántico.

## Documentos y arquitectura
No estudia documentación humana o generada de repositorio como artefacto final. La única salida documental es código pseudo-implementado generado temporalmente desde requisitos; no se informa procedencia a archivo/commit ni calidad semántica. No presenta un modelo arquitectónico completo.

## Evaluación
- Cuatro datasets CoEST: eTour, iTrust, SMOS y eAnci.
- Métricas: Precision, Recall, F1 y MAP; VSM/LSI/JS; también OSM/CSM.
- VSM+GEM logra mejores resultados integrados en varios casos: eTour F1 `.480`, MAP `.538`; iTrust `.297`, `.318`; SMOS `.426`, `.487`; eAnci `.292`, `.136`.
- Filtro: reduce candidatos ~50% en promedio y conserva menos Recall en eAnci (`.628` después de ambos filtros).
- Comparado con FTLR/COMET/LiSSA, el paper reporta mejoras hasta 10.7 puntos F1 y 9.1 puntos MAP.

## Artefactos
No se verificó localmente artefacto reproducible ni versión de paquetes. El paper declara LLMs GPT-4o, text-embedding-3-small, Qwen y Jina. No confundir resultados publicados con reproducción.

## Relación con nuestra tesis
**Interpretación acotada:** la integración semántica+léxica puede inspirar selección posterior de documentos asociados a APIs, manteniendo APIs recuperadas fijas y separando enlace de selección. No convierte generación de código por requisito en documentación generada ni aporta procedencia.

## Riesgos
- Lambda uniforme se ajusta con subconjuntos y puede ser subóptimo por proyecto.
- Ground truth incompleto/sospechoso en eAnci y diferencia idioma en OSM.
- eAnci y iTrust muestran que ranking integrado no basta; filtrado puede perder enlaces correctos.
- Generación no valida ejecutabilidad ni fuga.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Tesis, contribuciones y método | Markdown/PDF local | §§1–3, pp. 1–4 | Evidencia |
| Datasets, RQs y métricas | Markdown/PDF local | §4, pp. 4–5 | Evidencia |
| Integración y resultados | Markdown/PDF local | §§5.1–5.4, pp. 5–8 | Evidencia |
| Limitaciones | Markdown/PDF local | §§6–7, pp. 8–9 | Evidencia |

## Pendientes
Verificar tablas/figuras visualmente si se usan métricas exactas; revisar alias de PDF; validar disponibilidad/reproducibilidad local y política temporal de requisitos/código.
