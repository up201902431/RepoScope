# Ficha canónica de paper

## Identidad
- **paper_id:** graphcodebert
- **Título:** *GraphCodeBERT: Pre-training Code Representations with Data Flow*
- **Autores:** Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou.
- **Año/venue verificados:** ICLR 2021.
- **Versión:** arXiv:2009.08366v4, 13-09-2021.
- **Fuente original:** PDF local.
- **PDF/texto y procedencia:** `research/papers/pdf/Other/not defined/GraphCodeBERT.pdf`; texto paralelo en `research/papers/text/v5/estructura_colecciones/Other/not defined/GraphCodeBERT.md`. Extracción PyMuPDF automática, 2026-11-24, no verificada manualmente.
- **Paginación:** 18 páginas físicas; impresión ICLR/ICLR arXiv usa numeración interna 1-18. El PDF no separa claramente página impresa distinta.
- **Grupo/etiquetas:** Other / v5 / code representation / data flow.
- **Aprobación:** no disponible.
- **Cobertura de lectura:** lectura completa de las 18 páginas incluidas, método, ablation, casos de error y apéndices.

## Pregunta y contribución
**Evidencia:** GraphCodeBERT usa código más data flow semántico (where-the-value-comes-from) para preentrenar representaciones. Añade Edge Prediction y Node Alignment sobre datos de código y flujo.

**Interpretación:** Es un modelo de representación de código complementario, no un sistema de recuperación documental ni de generación de arquitectura.

## Método
- Entrada/salida: comentario + código + variables/data flow.
- Unidad/contexto: nodos de variables y aristas de procedencia.
- Recuperación: embedding y similitud para code search.
- Generación: no es generador principal; representa/finetunea para search, clone, translation/refinement.
- Granularidad: función/código con variables.
- Dependencias: parser AST, extracción de data flow y alineación entre variables y código.

## Documentos y arquitectura
- Origen: código y comentarios; data flow derivado.
- Tipo: representación estructural semántica.
- Arquitectura: Transformer con graph-guided masked attention.
- Versión: 12 capas, 768 dimensiones, 12 cabezas según apéndice.
- Pretraining: MLM + Edge Prediction + Node Alignment.

## Evaluación
- Benchmarks: code search, clone detection, code translation, code refinement.
- Datos: CodeSearchNet; BigCloneBench; pares Java-C#; bug-fix datasets.
- Métricas: MRR, F1, BLEU/accuracy.
- Resultados: estado del arte reportado en cuatro tareas; ablation muestra aportes de data flow y tareas estructurales.
- Límites: dependencia de parser y extractor; no evalúa repositorios completos ni documentación.

## Artefactos
- **Código/datos:** `https://github.com/microsoft/CodeBERT` según el paper.
- No se comprobó disponibilidad ni se ejecutó.

## Relación con nuestra tesis
Coincide en representar estructura semántica además de texto. Diferencia: data flow no representa documentación ni evolución; puede ser útil como baseliner de representación de código.

## Riesgos
- Cobertura limitada a lenguajes/parsers y calidad de extracción.
- No capturar historia ni enlaces puede falsear contexto.
- Confundir estructura semántica con arquitectura es metodológicamente incorrecto.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página | Tipo |
|---|---|---|---|
| GraphCodeBERT usa data flow instead of/reduced AST depth | Archivo local | §1-3, físicas 1-3 | Evidencia |
| Arquitectura graph-guided masked attention y 3 pretraining tasks | Archivo local | §4, físicas 4-5 | Evidencia |
| Mejora code search/clone/translation/refinement | Archivo local | §5.1-5.4, físicas 6-8 | Evidencia |
| Ablation atribuye mejoras a EdgePred/NodeAlign/data flow | Archivo local | §5.5, física 8 | Evidencia |
| La relación con arquitectura de tesis sería reinterpretación | Interpretación propia | Relación con tesis | Interpretación |

## Pendientes
- Verificar si el repositorio oficial contiene artefactos exactos y licencia.
- Mantener alias “GraphCodeBERT” en esta ficha canónica.
- Determinar si data flow debe entrar en evaluación, no asumir compatibilidad.
