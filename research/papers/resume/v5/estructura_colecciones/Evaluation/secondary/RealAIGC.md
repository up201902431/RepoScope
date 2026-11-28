# RealAIGC

## Identidad
- **paper_id:** no asignado; identificador local provisional `RealAIGC`.
- **Título:** *Towards More Realistic Evaluation of AI-Generated Code Detection in Real-World Code Repository*.
- **Autores/año/venue:** Wentao Chen et al.; ASE 2026. DOI `10.1145/3832783.3834411`.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/RealAIGC.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, conservado.
- **Cobertura:** lectura íntegra del Markdown declarada; página física 8 contrastada visualmente. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** evaluación de detección de código generado por IA en repositorios reales y múltiples granularidades.

**Interpretación:** antecedente sobre etiquetas y sesgos de corpus, no sobre generación de documentación.

## Método
Cinco granularidades (repositorio, PR, commit, archivo, función); 26 conjuntos repositorio/lenguaje, más de cuatro millones de funciones, ocho lenguajes y cinco agentes según el texto. Compara 28 métodos.

## Documentos y arquitectura
No genera documentación ni evalúa trazabilidad de documentos; clasifica origen IA/humano del código.

## Evaluación
AUC-ROC para ciertos análisis por función y métricas de clasificación, incluido F1, para otras granularidades. El F1 es de detección de origen IA/humano, no calidad funcional ni API F1. Reporta caídas fuertes en repositorios grandes/multilingües y baja eficacia de métodos de perplejidad.

## Artefactos
No se verificó artefacto externo ni reproducción.

## Relación con nuestra tesis
Puede alertar sobre clasificación en código real y dependencia de historia/etiquetas, pero no evalúa la intervención propuesta.

## Riesgos
El informe registra discrepancia interna: 26 datasets particionados por repo/lenguaje frente a 22 repositorios únicos en limitaciones. Debe preservarse y aclararse antes de resumir el tamaño como cifra única.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Resultados por granularidad | PDF/Markdown y raster local | §5, Tablas 4–7, física 8 | 1025 | Resultado; página impresa visible |
| Conteos/discrepancia | PDF/Markdown local | Tablas 4–7 y limitaciones | No fijada en informe retenido | Datos reportados/contradicción |

## Pendientes
Resolver conteos con el texto/tablas originales y verificar corpus/artefactos antes de citar tamaños definitivos.
