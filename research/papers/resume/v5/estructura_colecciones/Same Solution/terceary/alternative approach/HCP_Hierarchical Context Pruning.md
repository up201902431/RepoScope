# Ficha — HCP

## Identidad
- **Título:** *Hierarchical Context Pruning: Optimizing Real-World Code Completion with Repository-Level Pretrained Code LLMs*.
- **Autores/año/venue:** No verificados en esta ficha.
- **Fuente:** Extracción PyMuPDF, `terceary/alternative approach/HCP_Hierarchical Context Pruning.md`; paginación PDF física desde 1.
- **Grupo:** Same Solution / terceary / alternative approach, clasificación heredada.
- **Cobertura:** Lectura completa reportada en sesión previa; no inspección visual del PDF.

## Pregunta y contribución
Propone poda jerárquica de contexto para completion de código en repositorios, buscando mejorar utilidad práctica del contexto para modelos preentrenados a nivel repositorio. La tarea es completion; no document generation, issue repair ni revisión de código.

## Método
El trabajo organiza/filtra contexto en niveles jerárquicos antes de suministrarlo al modelo. El detalle de los niveles, puntuación, lenguajes y comparación de variantes debe cotejarse en las secciones de método; no se infiere que su jerarquía represente API→documento ni arquitectura del sistema.

## Documentos y arquitectura
El contexto es código del repositorio. No se acredita generación de documentación, origen humano de docs o enlaces persistentes hacia APIs.

## Evaluación
La extracción enumera páginas físicas 1–9. Los resultados y baselines concretos no se reproducen aquí porque requieren cotejo de tablas y fórmulas. No se ejecutó el sistema ni se verificaron artefactos.

## Artefactos
Disponibilidad, licencia, versión y comandos no comprobados.

## Relación con nuestra tesis
Puede informar el control de longitud/ruido del contexto en un baseline de completion, pero cambiar la poda también cambiaría el recuperador/contexto. No es evidencia aislada del aporte documental propuesto, que debe mantener fijas las APIs recuperadas.

## Riesgos
No equiparar reducción de contexto con selección semántica documental. Medidas automáticas y benchmark de completion no establecen calidad de documentación ni corrección general.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| El trabajo se centra en poda jerárquica para completion repository-level. | Extracción del paper | Título/Abstract, p. 1 | Encuadre reportado |
| El documento extraído tiene páginas PDF físicas 1–9. | Metadatos de extracción | Encabezados de página, pp. 1–9 | Cobertura |

## Pendientes
Recuperar detalle de algoritmo, benchmarks, métricas y cifras desde secciones/tablas; validar artefactos. No reutilizar resultados hasta hacerlo.
