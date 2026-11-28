# TRIAD: Automated Traceability Recovery based on Biterm-enhanced Deduction of Transitive Links among Artifacts

## Identidad
- **paper_id:** alias provisional `TRAID` (nombre de archivo y carpeta); el título usa **TRIAD**. No asumir duplicado/renombrado sin catálogo.
- **Título:** *TRIAD: Automated Traceability Recovery based on Biterm-enhanced Deduction of Transitive Links among Artifacts*.
- **Autores:** Hui Gao, Hongyu Kuang, Wesley K. G. Assunção, Christoph Mayr-Dorn, Guoping Rong, He Zhang, Xiaoxing Ma y Alexander Egyed.
- **Año/venue:** ICSE 2024.
- **Fuente original:** Markdown `.../secondary/TRAID.md`; PDF `.../pdf/Documentation-Code/secondary/TRAID.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 13 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/secondary`.

## Pregunta y contribución
Propone TRIAD para cerrar brecha de abstracción con biterms consensuales e enlaces transitivos internos/externos.

## Método
- Extrae biterms de artefactos fuente/intermedios/objetivo y retiene los consensuales centrados en intermedios.
- Enriquece textos fuente/objetivo y calcula ranked candidates con VSM/LSI/JS.
- Deduce outer links y inner links, forma paths y ajusta IR score multiplicativamente.

## Documentos y arquitectura
Usa requerimientos/documentación, artefactos intermedios y código. No genera ni distingue documentación humana/generada. Intermedios pueden ser requisitos/design/test code; no equivalen a SAM ni modelo arquitectónico obligatorio.

## Evaluación
- Cinco sistemas: Dronology, WARC, EasyClinic, EBT y LibEST.
- TRIAD supera IR-only en AP/MAP en mayoría de casos y TAROT/LIA/COMET; claims >15% AP y >10% MAP.
- Ablación: consensuales, outer links e inner links contribuyen incrementalmente.
- En LibEST puede empeorar por exceso de biterms y test code semánticamente distante.

## Artefactos
Replication package en GitHub/Zenodo declarado por el paper. No comprobado localmente.

## Relación con nuestra tesis
Aporta un mecanismo de enlace via artefactos intermedios y biterms, relevante a RAG/selección. No cambia APIs por sí mismo ni justifica integrar todos los candidatos.

## Riesgos
- Threshold m/t y granularidad no calibrados para el pipeline local.
- Código grande puede producir exceso de términos.
- Ground truth y transitive links pueden depender de calidad de intermedios.
- No usa documentación generada ni historial.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Método y ejemplo | Markdown/PDF | §§1–3, pp. 1–7 | Evidencia |
| Configuración/datasets | Markdown/PDF | §4, pp. 8 | Evidencia |
| Resultados/ablación | Markdown/PDF | §5, pp. 9–11 | Evidencia |
| Discusión/amenazas | Markdown/PDF | §§6–8, pp. 10–13 | Evidencia |

## Pendientes
Revisar tablas y figuras si se citan; calibrar thresholds solo con desarrollo separado de test; verificar si los intermedios son adecuados o solo test/code.
