# Recovering Trace Links Between Software Documentation And Code

## Identidad
- **paper_id:** alias provisional `TLR_Recovering-Trace-Links-Between-Software-Documentation-And-Code`.
- **Alias observado:** el PDF se nombra `TLR_Recovering Trace Links Between Software Documentation And Code.pdf`; no asumir que el cambio de guiones/es un duplicado distinto.
- **Título:** *Recovering Trace Links Between Software Documentation and Code*.
- **Autores:** Jan Keim, Sophie Corallo, Dominik Fuchß, Tobias Hey, Tobias Telge y Anne Koziolek.
- **Año/venue:** ICSE ’24, 13 páginas.
- **Fuente original:** Markdown `.../primary/TLR_Recovering-Trace-Links-Between-Software-Documentation-And-Code.md`; PDF en `.../pdf/Documentation-Code/primary/TLR_Recovering Trace Links Between Software Documentation And Code.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 13 páginas extraídas con pdfplumber. Sin revisión visual de tablas/figuras.
- **Grupo/etiquetas:** `Documentation-Code/primary`.

## Pregunta y contribución
Presenta TransArC, combinación transitoria de ArDoCo (SAD→SAM) y ArCoTL (SAM→código), para recuperar enlaces SAD–código.

## Método
- Transformar SAM y código a representaciones intermedias comunes.
- ArCoTL aplica heurísticas standalone/dependientes y un computational graph para nombres, paquetes, rutas, métodos, relaciones e interfaces.
- Combina mapeos con maximum, best/first y filtros.
- TransArC concatena enlaces ArDoCo y ArCoTL mediante elementos SAM compartidos.

## Documentos y arquitectura
SAD humana y SAM estructurada como artifacts intermedios; el código es fuente. No genera documentación ni expone snapshots/commits. El enfoque demuestra que SAM puede reducir brecha semántica, pero no prueba compatibilidad con documentación generada.

## Evaluación
- Cinco proyectos: MS, TS, TM, BBB y JR.
- ArCoTL model→code: avg F1 `0.98`, weighted `0.99`.
- TransArC SAD→code: avg F1 `0.82`, weighted `0.87`, supera TAROT/FTLR/CodeBERT/ArDoCode.
- Baselines avg F1: TAROT `.22`, FTLR `.21`, CodeBERT `.28`, ArDoCode `.37`.

## Artefactos
Replication package citado Zenodo `10.5281/zenodo.10411853`. No comprobado localmente.

## Relación con nuestra tesis
Es candidato para el enlace documental–arquitectura–API/código, no para asumir compatibilidad con selección de documentación. Los SAM manuales son el insumo que el pipeline ampliado podría intentar generar, pero debe validar formato y procedencia.

## Riesgos
- Requiere SAM; su calidad afecta precisión.
- Mapeo por nombres puede generar falsos positivos y depender de estilo/abrev.
- SAM de diferentes niveles de abstracción limita generalización.
- Gold standards y proyectos abiertos pueden contener sesgos.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Diseños ArCoTL/TransArC | Markdown/PDF | §§3–4, pp. 3–7 | Evidencia |
| Dataset y métricas | Markdown/PDF | §5.1–5.3, pp. 8–9 | Evidencia |
| Resultados | Markdown/PDF | §5.4, pp. 9–10 | Evidencia |
| Amenazas | Markdown/PDF | §6, pp. 10–11 | Evidencia |

## Pendientes
Revisar tablas/figuras si se reproduce; validar replicación; identificar si SAM puede derivarse automáticamente sin confundir reverse engineering con trazabilidad.
