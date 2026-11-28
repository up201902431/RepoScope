# Ficha — AutoCodeRover

## Identidad
- **Título:** *AutoCodeRover: Autonomous Program Improvement*.
- **Autores/año/venue:** Pendiente de cotejo bibliográfico con el PDF.
- **Fuente:** Extracción PyMuPDF, páginas físicas 1–13; no visualmente revisada.
- **Grupo:** Same Solution / terceary / bug_fix.
- **Cobertura:** Lectura íntegra reportada previamente.

## Pregunta y contribución
Automatizar mejora de programas y resolución de issues explorando código. El sistema localiza elementos en AST y orienta la búsqueda para producir parches. Es reparación, no completion o generación documental.

## Método
Workflow autónomo con exploración estructural y búsqueda de localización; genera cambios que se evalúan como resolución de tareas y calidad de parche. No equiparar parche aceptado con precisión de API.

## Documentos y arquitectura
La estructura AST/código no es documentación arquitectónica ni documento API enlazado. No se reporta generador documental en la caracterización de esta ficha.

## Evaluación
La extracción muestra evaluación comparativa con sistemas agentic (incluidos Devin y SWE-agent en el texto) sobre SWE-bench y analiza número de issues resueltos, coste por tarea y calidad de parches. No transcribo cifras sin verificar tabla; los resultados son de reparación con tests, no completion Pass@1.

## Artefactos
No se verificó repo, versión, licencia ni ejecución local.

## Relación con nuestra tesis
Antecedente de contexto/razonamiento en repositorios y vecino lejano por tarea. No es baseline central de la tesis; comparar solo si se define un experimento específico de issue resolution.

## Riesgos
Sensibilidad al presupuesto y herramientas del agente; los tests no cubren toda la calidad de parche. Revisar fuga por tests, archivos de issue, historial/caches y contexto objetivo.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Workflow de mejora programática con localización estructural/AST. | Extracción del paper | Abstract/Method, pp. 1–5 | Método reportado |
| Comparación en SWE-bench y métricas de resolución/coste/calidad. | Extracción del paper | Evaluation, Tables 2 y siguientes, pp. 7–9 | Resultados reportados; cifras por cotejar |

## Pendientes
Verificar metadatos, cifras y protocolo en PDF visual; comprobar artefactos y amenazas de fuga. Sin reproducción local.
