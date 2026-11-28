# CodeBERT: A Pre-Trained Model for Programming and Natural Languages

## Identidad
- **paper_id:** alias provisional `codebert`.
- **Título:** *CodeBERT: A Pre-Trained Model for Programming and Natural Languages*.
- **Autores:** Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang y Ming Zhou.
- **Año/venue:** Findings of EMNLP 2020, pp. 1536–1547.
- **Fuente original:** Markdown `.../primary/codebert.md`; PDF `research/papers/pdf/Documentation-Code/primary/codebert.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 12 páginas extraídas; extracción automática PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/primary`; clasificación conservada.

## Pregunta y contribución
Presenta un preentrenamiento bimodal NL–PL con representaciones generales para búsqueda de código y generación de documentación. No es, por sí solo, un sistema de trazabilidad ni un generador de README.

## Método
- Arquitectura RoBERTa-base, 125M parámetros.
- Entrada NL+PL con `[CLS]`/`[SEP]`; salida contextual por token y representación `[CLS]`.
- Entrena sobre 2.137M pares NL–PL y 6.452M de código unimodal de GitHub en seis lenguajes.
- Objetivos combinados: masked language modeling y replaced token detection con generadores NL/PL.
- Fine-tuning para búsqueda NL–código y encoder–decoder para code-to-text.

## Documentos y arquitectura
Usa documentaciones de función humanas o existentes como pares NL–PL; no distingue ni preserva procedencia a versión/commit en el paper extraído. Produce resúmenes de código como tarea generativa, no documentación arquitectónica ni enlaces explícitos. No presenta modelo de arquitectura.

## Evaluación
- CodeSearchNet en Ruby, JavaScript, Go, Python, Java y PHP; MRR por modelo específico.
- CodeBERT MLM+RTD alcanza macro MRR `.7603`, frente a `.6972` de RoBERTa.
- NL–PL probing: accuracy `.8566` PL y `.7453` NL con `CodeBERT (MLM)`.
- Code-to-documentation: BLEU total `.17.83`, frente a `.16.57` RoBERTa.
- C# unseen: BLEU `22.36`, sobre RoBERTa `19.81`; inferior a code2seq `23.04`.

## Artefactos
El Markdown remite a github.com/microsoft/CodeBERT para código/datos. No se verificó localmente artefacto, licencia, commit ni reproducibilidad.

## Relación con nuestra tesis
Puede servir como representador semántico para recuperar APIs/documentación, no como componente probadamente mejorado en ejecución. Hay que separar representación NL–PL de generación, selección y procedencia documental.

## Riesgos
- Datos públicos de GitHub pueden causar solapamiento con repositorios de evaluación.
- Métricas code-to-text no implican utilidad para requisitos/API.
- El corpus de preentrenamiento no expone política temporal ni versión.
- Fine-tuning por lenguaje puede afectar generalización.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Arquitectura y objetivos | Markdown/PDF | §§3.1–3.4, pp. 1–4 | Evidencia |
| Corpus y filtros | Markdown/PDF | §3.3, pp. 2–3 | Evidencia |
| Búsqueda, probing y generación | Markdown/PDF | §§4.1–4.4, pp. 5–8 | Evidencia |

## Pendientes
Comprobar disponibilidad de versión/código oficial; identificar riesgo de fuga de proyectos; validar si embeddings se usan sin fine-tuning en contexto local.
