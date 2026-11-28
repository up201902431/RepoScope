# From Model Diagram to Code: A Benchmark Dataset and Multi-Agent Framework

## Identidad
- **paper_id:** alias provisional `MDCAgent_From Model Diagram to Code`.
- **Título:** *From Model Diagram to Code: A Benchmark Dataset and Multi-Agent Framework*.
- **Autores:** Mengzhen Wang, Xunbin Huang, Jiayuan Xie, Shukai Ma, Jiale Men, Dayong Liang y Yi Cai.
- **Año/venue:** ACM MM ’25, pp. 1754–1763.
- **Fuente original:** Markdown homónimo en `.../primary/`; PDF homónimo en `.../pdf/Documentation-Code/primary/`.
- **Procedencia/cobertura:** lectura íntegra de las 10 páginas extraídas. Extracción automática PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/primary`.

## Pregunta y contribución
Introduce MDCDataset y MDCAgent para generar código de arquitectura desde diagramas de modelos de papers.

## Método
- Dataset de 1,008 tripletas: diagrama, texto estructurado y código ground truth.
- Parsing Agent analiza módulos, relaciones y flujo.
- Generation Agent traduce análisis a código.
- Check Agent verifica módulos/lógica contra diagrama y análisis.
- Evalúa sin y con secciones del paper.

## Documentos y arquitectura
Texto y diagramas provienen de papers; son artefactos humanos/publicados. El framework no genera documentación del repositorio ni mantiene enlaces a commit. El diagrama representa arquitectura funcional del paper; no se transforma en SAM compatible con ArCoTL/TransArC.

## Evaluación
- 16 MLLMs; Claude-3.7-Sonnet lidera con LLM Score `56.14`, CodeBLEU `34.52`, CrystalBLEU `46.59`.
- Texto del apartado Method produce la mejora más consistente; full paper depende de capacidad de contexto.
- MDCAgent mejora promedio LLM Score `+3.10` sin contexto y `+2.10` con contexto.
- Ablación: eliminar Parsing degrada más; eliminar Check también pierde calidad.

## Artefactos
Dataset/código GitHub declarado en `https://github.com/afdyff/MDC`. No se comprobó licencia, disponibilidad actual ni ejecución local.

## Relación con nuestra tesis
Es un benchmark cercano a transducir diagramas/texto a código, pero no prueba selección documental según requisito ni trazabilidad a API. El diagrama no es evidencia de compatibilidad con pipeline arquitectónico.

## Riesgos
- Una arquitectura admite múltiples implementaciones válidas.
- Métricas automáticas pueden no capturar equivalencia estructural.
- Dataset construido con filtro LLM+humanos y papers 2015–2025.
- Extracción de texto puede introducir ruido si el paper contiene solución objetivo.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Construcción MDCDataset | Markdown/PDF | §§3–4, pp. 1756–1758 | Evidencia |
| Método MDCAgent | Markdown/PDF | §5, pp. 1757–1758 | Evidencia |
| Experimentos/ablaciones | Markdown/PDF | §§6.4–6.9, pp. 1759–1761 | Evidencia |

## Pendientes
Comprobar reproducción/artefactos oficiales; inspeccionar figuras si se citan; validar que los diagrams ground truth no colisionan con documentos humanos permitidos.
