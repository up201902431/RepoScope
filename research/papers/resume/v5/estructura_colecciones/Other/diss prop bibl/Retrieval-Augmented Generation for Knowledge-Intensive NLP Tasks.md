# Ficha canónica de paper

## Identidad
- **paper_id:** rag-knowledge-intensive-nlp
- **Título:** *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*
- **Autores:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela.
- **Año/versión verificados:** arXiv:2005.11401v4; versión 12-04-2021. También asociado a NeurIPS 2020 según el contexto bibliográfico del campo, pero el extracto local no declara proceedings.
- **DOI/versión:** arXiv:2005.11401v4.
- **Fuente original:** PDF local de preprint/arxiv.
- **PDF/texto y procedencia:** `research/papers/pdf/Other/diss prop bibl/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`; texto paralelo en `research/papers/text/v5/estructura_colecciones/Other/diss prop bibl/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.md`. Extracción PyMuPDF automática, 2026-11-24, no verificada manualmente.
- **Paginación:** páginas físicas e impresas coinciden aproximadamente 1-19 en el extracto; el primer PDF lleva arXiv y el apéndice continúa numeración propia.
- **Grupo/etiquetas:** Other / v5 / RAG / retrieval + generation.
- **Aprobación:** no disponible.
- **Cobertura de lectura:** lectura completa de las 19 páginas incluidas, incluidas resultados, impacto y apéndices.

## Pregunta y contribución
**Evidencia:** Introduce RAG como combinación de memoria paramétrica (BART) y memoria no paramétrica (índice denso DPR sobre Wikipedia). Define RAG-Sequence, que usa el mismo documento para toda la secuencia, y RAG-Token, que puede usar documentos distintos por token.

**Interpretación:** Establece el patrón general retrieval-generation y hot-swapping del índice, no una solución específica para repositorios de código ni una arquitectura documental probada en software.

## Método
- Entrada/salida: consulta de texto → documentos recuperados → texto generado/respuesta/clase.
- Unidad y contexto: pasajes de Wikipedia de 100 palabras.
- Recuperación: Dense Passage Retriever (DPR), query/document encoders BERT y MIPS/FAISS.
- Generación: BART-large (400M).
- Entrenamiento: marginalización end-to-end del documento latente; fine-tuning conjunto del query encoder y BART; documento encoder/index se mantienen fijos.
- Decodificación: thorough decoding, fast decoding y beam para RAG-Token.

## Documentos y arquitectura
- Origen: memoria externa humana de Wikipedia.
- Tipo: NLP knowledge base, no documentación de repositorio.
- Arquitectura: retriever DPR + seq2seq BART + índice vectorial.
- Versionado/contenido: índice no paramétrico reemplazable; el paper demuestra cambiar dumps 2016/2018 sin reentrenar.
- Filtrado por requisito: no aplica selección documental de software.

## Evaluación
- Tareas: Open-domain QA (NQ, TriviaQA, WebQuestions, CuratedTrec), MS-MARCO abstractive QA, Jeopardy generation y FEVER.
- Métricas: Exact Match, BLEU-1/Q-BLEU-1, Rouge-L y accuracy.
- Resultados: nuevo estado del arte reportado en cuatro QA abiertos; mejora factualidad, especificidad y diversidad frente a BART; FEVER dentro de 4.3% del pipeline state-of-the-art.
- Límites: bajo supervisión de recuperación, ruido, conocimiento de Wikipedia y falta de verificación externa.

## Artefactos
- Código abierto asociado a HuggingFace Transformers: https://github.com/huggingface/transformers/tree/master/examples/rag
- Demo interactiva declarada en el paper.
- No se verificó disponibilidad ni se ejecutó.

## Relación con nuestra tesis
Coincide en memoria paramétrica + índice externo y actualización cambiando el índice. Diferencia: sus documentos son pasajes generales, no artefactos de repositorio con historia, enlaces o requisitos. Reutilizable acotadamente como principio RAG y formulación de documento latente.

## Riesgos
- Alucinaciones aunque menores que el baseline; bias y sesgo factual de la fuente externa.
- Recuperación puede colapsar en tareas poco dependientes de conocimiento.
- Hot-swapping de conocimiento es más fácil que reentrenar, pero puede introducir inconsistencias.
- Fuga/overlap de benchmark y dependencia de Wikipedia no probada en código.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF o impresa | Tipo |
|---|---|---|---|
| RAG combina retriever DPR con BART y marginaliza documentos | Archivo local | §1-2, páginas 1-4 | Evidencia |
| RAG-Sequence y RAG-Token usan distintos esquemas de marginalización | Archivo local | §2.1, páginas 3-4 | Evidencia |
| Logra estado del arte en NQ, TriviaQA, WQ y CuratedTrec | Archivo local | §4.1 y Table 1, páginas 5-6 | Evidencia |
| Generación es más factual, diversa y específica que BART | Archivo local | §4.2-4.3 y §4.5, páginas 6-8 | Evidencia |
| El índice puede reemplazarse sin reentrenar | Archivo local | §4.5, páginas 7-8 | Evidencia |
| Uso como modelo de repositorio sería una adaptación no validada | Interpretación propia | Relación con tesis | Interpretación |

## Pendientes
- Confirmar identidad bibliográfica/neural y artefactos oficiales antes de catalogar.
- Comparar DPR/BART con modelos CodeT5/GraphCodeBERT solo como patrón, no como benchmark.
- Definir qué representa un documento en un repositorio si se aplica RAG.
