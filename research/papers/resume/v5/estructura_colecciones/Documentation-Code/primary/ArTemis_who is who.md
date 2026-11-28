# Who’s Who? LLM-assisted Software Traceability with Architecture Entity Recognition

## Identidad
- **paper_id:** alias provisional `ArTemis_who is who`.
- **Título:** *Who’s Who? LLM-assisted Software Traceability with Architecture Entity Recognition*.
- **Autores:** Dominik Fuchß, Haoyu Liu, Sophie Corallo, Tobias Hey, Jan Keim, Johannes von Geisau y Anne Koziolek.
- **Año/venue:** ACM TAAS; 2026, 30 páginas físicas extraídas.
- **Fuente original:** Markdown homónimo en `.../primary/`; PDF homónimo en `research/papers/pdf/Documentation-Code/primary/`.
- **Procedencia/cobertura:** lectura íntegra de las 30 páginas extraídas. Extracción automática PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/primary`; sin aprobación nueva.

## Pregunta y contribución
Combina ExArch, que extrae nombres de componentes desde SAD/código, con ArTEMiS, que identifica entidades arquitectónicas en documentación y las enlaza con modelos.

## Método
- ExArch usa prompting encadenado para extraer componentes desde SAD, paquetes de código o ambos.
- Agrega nombres por prompt o distancia de Levenshtein y los pasa a TransArC como SAM simple.
- ArTEMiS usa dos prompts: extracción NER y JSON; mapea líneas exactas/similares y enlaza mediante Jaro-Winkler, Levenshtein y embeddings.
- Entidad→línea; no se confunde con una recuperación probabilística completa.

## Documentos y arquitectura
Trabaja con documentación humana SAD, modelos SAM manuales o generados y código. ExArch genera una SAM mínima de nombres, no documentación arquitectónica completa ni artefactos generados por commit. Mantiene una separación entre entidades y fuente de texto, aunque no se verificó procedencia longitudinal.

## Evaluación
- Cinco proyectos y un benchmark de SAD/SAM/código revisado.
- En benchmark original, ExArch GPT-4o weighted F1 `0.86` frente a TransArC manual `0.87`; supera baselines sin SAM.
- Benchmark revisado: GPT-4o weighted F1 `0.87`.
- ArTEMiS GPT-5 alcanza avg. recall `0.85`, F1 `0.81`, frente a SWATTR `0.77/0.80`.
- TransArC + ExArch + ArTEMiS alcanza weighted F1 `0.87` sin SAM, frente a ArDoCode `0.62`.

## Artefactos
Menciona paquetes de replicación en Zenodo DOI `10.5281/zenodo.18957376` y `10.5281/ZENODO.14506935`. No se comprobó localmente su disponibilidad/licencia ni se ejecutó.

## Relación con nuestra tesis
Es relevante para documentación humana, extracción de entidades arquitectónicas y trazabilidad SAD–SAM–código. No demuestra que documentación generada sea útil ni compatible con SemArc/CodeWiki; la SAM simple no equivale a arquitectura recuperada completa.

## Riesgos
- Propagación de errores entre ExArch, ArTEMiS y TransArC.
- Dependencia de proyectos abiertos y modelos cerrados; posible fuga no descartada.
- Temperatura cero no disponible para GPT-5; variabilidad documentada.
- Benchmark revisado puede cambiar ground truth respecto a la evaluación inicial.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Diseño ExArch/TransArC | Markdown/PDF | §§3–3.3, pp. 6–8 | Evidencia |
| Diseño ArTEMiS | Markdown/PDF | §4, pp. 9–10 | Evidencia |
| Benchmark y resultados | Markdown/PDF | §§5.1–5.5, pp. 10–23 | Evidencia |
| Amenazas | Markdown/PDF | §5.6, pp. 23–24 | Evidencia |

## Pendientes
Validar visualmente figuras y tablas si se reproducen; comprobar replicación y política de temperatura; distinguir explícitamente SAM generada de documentación humana/generada.
