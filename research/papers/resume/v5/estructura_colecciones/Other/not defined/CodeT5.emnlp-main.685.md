# Ficha canónica de paper

## Identidad
- **paper_id:** codet5
- **Título:** *CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation*
- **Autores:** Yue Wang, Weishi Wang, Shafiq Joty, Steven C.H. Hoi.
- **Año/venue verificados:** 2021; EMNLP 2021, páginas proceedings 8696-8708.
- **Versión:** arXiv 2109.00859; repositorio oficial declarado por los autores.
- **Fuente original:** PDF local.
- **PDF/texto y procedencia:** `research/papers/pdf/Other/not defined/CodeT5.emnlp-main.685.pdf`; texto paralelo en `research/papers/text/v5/estructura_colecciones/Other/not defined/CodeT5.emnlp-main.685.md`. Extracción PyMuPDF automática, 2026-11-24, no verificada manualmente.
- **Paginación:** física 1-13; impresión EMNLP 8696-8708 (main), física 1 coincide con impresión 8696.
- **Grupo/etiquetas:** Other / v5 / code pretraining / encoder-decoder.
- **Aprobación:** no disponible.
- **Cobertura de lectura:** lectura completa de las 13 páginas del extracto, método, 14 subtareas, análisis, impactos y referencias.

## Pregunta y contribución
**Evidencia:** CodeT5 unifica encoder-decoder para entender y generar código. Se construye sobre T5 y añade preentrenamiento identificador-aware mediante Identifier Tagging e Identifier Prediction, además de generación dual NL↔PL.

**Interpretación:** Es relevante para representaciones de código y tareas PL/NL, pero no garantiza la selección de documentación de repositorio ni la coherencia arquitectónica.

## Método
- Entrada/salida: secuencia NL/PL concatenada; salida texto o código según tarea.
- Unidad/contexto: identifiers, spans, funciones y pares NL-PL.
- Recuperación: no usa recuperación externa; preentrenamiento paramétrico.
- Generación: denoising Seq2Seq T5, span masking, bimodal dual generation.
- Granularidad: función/clase no siempre; code snippet.
- Dependencias: datos de CodeSearchNet, C/C#, AST via tree-sitter y etiquetado de identifiers.

## Documentos y arquitectura
- Origen: código fuente y comentarios/documentación bimodal.
- Tipo: representaciones del código; no generación documental de repositorio.
- Arquitectura: encoder-decoder T5 de 60M/220M; task control codes y fine-tuning/task-multitasking.
- Versión: CodeT5-base/small.
- Generador: preentrenamiento por masked spans and identifiers.

## Evaluación
- Benchmarks: CodeXGLUE 14 subtareas: resumen, generación, traducción, refinamiento, defect/clone.
- Métricas: BLEU, Exact Match, CodeBLEU, F1 y accuracy.
- Resultados: estado del arte reportado en varias subtareas; mejora code generation/defect y traducción/refinamiento.
- Límites: dual bimodal puede sesgar tareas PL-PL; BLEU no refleja siempre funcionalidad.

## Artefactos
- **Código/modelos:** https://github.com/salesforce/CodeT5
- Contenido oficial no comprobado; no se descargó ni ejecutó.

## Relación con nuestra tesis
Coincide en alinear código y texto NL y en modelar identificadores. Diferencia: no usa documentación humana/generada como entrada recuperable ni evalúa evolución/repositorio. Reutilizable acotadamente como encoder-decoder o representador.

## Riesgos
- Sesgo de datasets y propietarios.
- Coste de cómputo y sensibilidad a hiperparámetros.
- Emparejamiento NL-PL puede contener documentación pobre o sesgada.
- Automatización de código genera riesgo de sugerencias incorrectas/unsafe.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| CodeT5 usa T5 + identifier-aware objectives + dual NL-PL | Archivo local | §1-3, físicas 1-4 / impresas 8696-8699 | Evidencia |
| Preentrena en 8.35M instancias y 6+ PL | Archivo local | §4.1, física 5 / impresa 8700 | Evidencia |
| Evalúa 14 subtareas CodeXGLUE | Archivo local | §4.3-4.5, física 6 / impresa 8701 | Evidencia |
| Mejora sobre modelos previos en generación y defect detection | Archivo local | §5.1, físicas 7-8 / impresas 8702-8703 | Evidencia |
| Ablación muestra aportes de MSP, IT y MIP | Archivo local | §5.3, física 9 / impresa 8704 | Evidencia |
| Aplicación documental a RepoScope es una interpretación | Interpretación propia | Relación con tesis | Interpretación |

## Pendientes
- Verificar la versión oficial de CodeT5 usada y licencia.
- Evitar confundir CodeT5+ / CodeT5 y variants como modelos duplicados si reaparecen.
- Validar compatibilidad y coste antes de cualquier selección.
