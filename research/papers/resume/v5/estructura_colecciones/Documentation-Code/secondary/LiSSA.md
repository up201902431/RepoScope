# LiSSA: Toward Generic Traceability Link Recovery through Retrieval-Augmented Generation

## Identidad
- **paper_id:** alias provisional `LiSSA`.
- **Título:** *LiSSA: Toward Generic Traceability Link Recovery through Retrieval-Augmented Generation*.
- **Autores:** Dominik Fuchß, Tobias Hey, Jan Keim, Haoyu Liu, Niklas Ewald, Tobias Thirolf y Anne Koziolek.
- **Año/venue:** ICSE 2025.
- **Fuente original:** Markdown `.../secondary/LiSSA.md`; PDF `.../pdf/Documentation-Code/secondary/LiSSA.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 13 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/secondary`.

## Pregunta y contribución
Framework RAG genérico para TLR en requisitos→código, documentación→código y documentación→modelos.

## Método
- Preprocesa artifacts como NL, código o modelo y genera elementos.
- Recupera Top-k candidatos por embeddings/coseno.
- Clasifica relación con prompt KISS o chain-of-thought.
- Agrega relaciones al nivel deseado.

## Documentos y arquitectura
Usa documentación existente/requisitos y UML. No distingue documentación humana de generada ni crea documentación arquitectónica. Model preprocessor extrae componentes/interfaz/operación de UML para texto.

## Evaluación
- GPT-4o: supera FTLR/COMET en F1 promedio para requisitos→código; mejor configuración suele no preprocesar.
- Docs→código: mejora significativamente proyectos pequeños; proyectos grandes tienen recall deficiente por retrieval.
- Docs→modelo: no supera ArDoCo.
- CoT supera clasificación simple en F1.

## Artefactos
Replication package Zenodo `10.5281/zenodo.14714706`. No comprobado localmente.

## Relación con nuestra tesis
Es el antecedente directo de RAG para artefactos heterogéneos. Puede informar Top-k y prompting, pero no resuelve selección ni procedencia documental; su recuperación también depende de granularidad.

## Riesgos
- Retrieval fija upper bound de recall.
- proyectos grandes pueden necesitar cientos de candidatos.
- modelos cerrados y repositorios abiertos pueden tener fuga.
- fine-grained preprocessing no mejora consistently.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Framework y prompts | Markdown/PDF | §§III–III-C, pp. 3–5 | Evidencia |
| Dataset y modelos | Markdown/PDF | §IV-A–IV-E, pp. 6–7 | Evidencia |
| Resultados | Markdown/PDF | §IV-F, pp. 7–10 | Evidencia |
| Limitaciones | Markdown/PDF | §IV-G–VI, pp. 10–13 | Evidencia |

## Pendientes
Validar costo y replicabilidad GPT-4o/mini; mejorar retrieval para muchos enlaces; comparar RAG con baseline de embeddings sin LLM; conservar procedencia.
