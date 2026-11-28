# Ficha canónica de paper

## Identidad
- **paper_id:** unixcoder
- **Título:** *UniXcoder: Unified Cross-Modal Pre-training for Code Representation*
- **Autores:** Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin.
- **Año/venue verificados:** 2022; ACL 2022, volumen 1, páginas 7212-7225.
- **Identificador:** no DOI visible; arXiv asociado no indicado en el extracto principal.
- **Fuente original:** PDF local.
- **PDF/texto y procedencia:** `research/papers/pdf/Other/not defined/UniXcoder.pdf`; texto paralelo en `research/papers/text/v5/estructura_colecciones/Other/not defined/UniXcoder.md`. Extracción PyMuPDF automática, 2026-11-24, no verificada manualmente.
- **Paginación:** física 1-14; impresión de proceedings 7212-7225. El mismo extracto incluye apéndices hasta física 14.
- **Grupo/etiquetas:** Other / v5 / unified code representation / cross-modal.
- **Aprobación:** no disponible.
- **Cobertura de lectura:** lectura completa de las 14 páginas incluidas, incluidas modelo, tareas, análisis y apéndices.

## Pregunta y contribución
**Evidencia:** UniXcoder unifica modos encoder, decoder y encoder-decoder mediante prefix adapters y máscaras de atención. Incorpora comments y AST, transforma AST en secuencia one-to-one y añade contrastive learning y cross-modal generation para embeddings.

**Interpretación:** Es relevante como representación unificada y para retrieval code-to-code, pero no constituye por sí solo un pipeline repository-level ni selección de artefactos documentales.

## Método
- Entrada/salida: comentarios + AST flatten + código; embeddings o texto/código generado según modo.
- Unidad/contexto: fragmento de código, AST flatten y comment.
- Recuperación: embeddings para zero-shot code-to-code search.
- Generación: MLM, ULM, denoising y generation from AST/code.
- Granularidad: fragmento/función, línea.
- Dependencias: parser tree-sitter, mapping one-to-one y pretraining multimodal.

## Documentos y arquitectura
- Origen: código, comentarios y AST.
- Tipo: cross-modal code representation.
- Arquitectura: Transformer 12 capas compartidas con [Enc]/[Dec]/[E2D], masked attention y mean pooling.
- Versión: 768 dimensiones, 12 heads según apéndice.
- Procedencia: CodeSearchNet 2.3M functions + cross-modal data.

## Evaluación
- Benchmarks: clone, code search, summarization, generation, completion y zero-shot code-to-code.
- Datasets: POJ-104, BigCloneBench, CosQA, AdvTest, CSN, CONCODE, PY150, Java Corpus, CodeNet subset.
- Métricas: MAP, MRR, BLEU, EM, Edit Similarity.
- Resultados: estado del arte reportado en varias tareas y fuerte resultado en zero-shot code-to-code.
- Límites: AST no mejora todos los tasks; parser introduces coste y el agregado puede sesgar a code search.

## Artefactos
- **Código/datos:** https://github.com/microsoft/CodeBERT según el paper.
- No se confirmó licencia/versionado ni se ejecutó.

## Relación con nuestra tesis
Coincide en embeddings cross-modal de código y NL y puede apoyar recuperación. Diferencia: no enlaza documentación humana/generada ni implementa evolución/arquitectura; no reemplaza pipeline repository-level.

## Riesgos
- Representaciones pueden perder estructura si el parser/mapping falla.
- AST aumenta coste y no siempre mejora generación.
- Duplicación, benchmark leakage y sesgo de lenguajes.
- Zero-shot retrieval no valida mantenibilidad ni adecuación de documentación.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página | Tipo |
|---|---|---|---|
| Prefijos/máscaras permiten [Enc], [Dec] y [E2D] compartidos | Archivo local | §3.2, físicas 4-5 / impresas 7215-7216 | Evidencia |
| AST se convierte one-to-one a secuencia y conserva estructura | Archivo local | §3.1, físicas 3-4 / impresas 7214-7215 | Evidencia |
| MCL + CMG aprenden embeddings de fragmentos | Archivo local | §3.3, físicas 5-6 / impresas 7216-7217 | Evidencia |
| Estado del arte en tasks reportados | Archivo local | §4.2-4.5, físicas 6-8 / impresas 7217-7219 | Evidencia |
| Ablaciones muestran aporte de comment/AST/MCL/CMG | Archivo local | §4.6, física 8 / impresa 7219 | Evidencia |
| Aplicación repository-level es extrapolación propia | Interpretación propia | Relación con tesis | Interpretación |

## Pendientes
- Verificar nombre/versión exacta del repositorio oficial y artefactos.
- Confirmar si zero-shot code-to-code dataset debe usarse como evaluación solo como señal de representación.
- Comparar con otros embeddings de código sin asumir plug-and-play.
