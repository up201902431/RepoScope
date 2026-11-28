# Preserving Model-to-Code Traceability During LLM-Based Code Generation

## Identidad
- **paper_id:** alias provisional `Preserving Model-to-Code Traceability During LLM-Based Code Generation`.
- **Título:** *Preserving Model-to-Code Traceability During LLM-Based Code Generation*.
- **Autores:** Marc North, Nelly Bencomo y Amir Atapour-Abarghouei.
- **Año/venue:** MODELS 2026, pp. 358–364.
- **Fuente original:** Markdown homónimo en `.../secondary/`; PDF homónimo en `.../pdf/Documentation-Code/secondary/`.
- **Procedencia/cobertura:** lectura íntegra de las 7 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/secondary`.

## Pregunta y contribución
Estudia cómo preservar trazas modelo–código durante generación LLM mediante atribución token–elemento, en lugar de recuperación post hoc.

## Método
- Dataset de 128 modelos XMI y generador determinista Python/Java; 3,707 trazas ground truth.
- Evalúa masking individual/XML, Gradients×Embedding, Integrated Gradients y Value Zeroing.
- Resuelve atribuciones a tokens previos, agrupa por feature y agrega al elemento XMI.
- Teacher forcing sobre tokens de salida.

## Documentos y arquitectura
Insumos: UML/XMI model diagrams y código generado. No usa documentación humana/generada del repositorio ni genera READMEs. Produce mapas de atribución como artefactos de trazabilidad, no arquitectura textual.

## Evaluación
- Cuatro open-weight LLMs: CodeLlama-7b, Phi-4-mini, Gemma-3-4b, Qwen2-0.5B.
- Value Zeroing mejor: ~90% top-1 y >95% top-5; Python ~97% top-1, 100% top-5.
- Más difícil: return types; más fácil: attributes.

## Artefactos
Dataset, framework e implementación declarados en `github.com/marcnorth/attribution-traceability`. No se verificaron localmente licencia/commit/reproducibilidad.

## Relación con nuestra tesis
Es una vía distinta de trazabilidad construida durante generación. Puede inspirar procedencia, pero no prueba selección documental ni API reuse y depende de explicar señales internas del generador.

## Riesgos
- Ground truth determinista puede no representar trazabilidad semántica humana.
- Teacher forcing no reproduce generación libre.
- Diferencias de arquitectura/tokenizer confunden efecto de tamaño.
- No cubre closed-source ni proyectos grandes.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Métodos de atribución | Markdown/PDF | §3, pp. 360–361 | Evidencia |
| Comparación y resultados | Markdown/PDF | §4, pp. 361–363 | Evidencia |
| Amenazas/futuro | Markdown/PDF | §§5–6, pp. 362–364 | Evidencia |

## Pendientes
Comprobar replicación oficial; validar si attribution survive free decoding; estudiar relación entre atribución, factualidad y procedencia.
