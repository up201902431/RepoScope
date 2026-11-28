# LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering

## Identidad
- **paper_id:** alias provisional `SSDE_LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering`.
- **Título:** *LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering*.
- **Autores:** Shuzhao Feng, Boqi Chen, Brett H Meyer y Gunter Mussbacher.
- **Año/venue:** FSE Companion 2026, pp. 1257–1261.
- **Fuente original:** Markdown homónimo en `.../primary/`; PDF homónimo en `.../pdf/Documentation-Code/primary/`.
- **Procedencia/cobertura:** lectura íntegra de las 5 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/primary`; no implica selección del pipeline.

## Pregunta y contribución
Propone SSDE: usar Gherkin/domain models como especificaciones estructuradas verificables para generación MVC a nivel repositorio.

## Método
- Tres sistemas MVC con Gherkin, modelos Umple/Ecore y firmas generadas.
- Genera controladores Python con cinco LLMs, 10 repeticiones y temperatura/reasoning configurados.
- Compara lenguaje natural, Gherkin, dominio y firmas.
- Evalúa contra test suite humana verificada y inspección cualitativa.

## Documentos y arquitectura
Input estructurado: Gherkin, domain models y firmas; outputs: controladores/repositorio MVC. Los documentos son especificaciones humanas/estructuradas, no generación automática de API-doc, module-doc ni arquitectura. Se mantiene el origen en sistemas seleccionados, pero no se registra una política temporal de commits.

## Evaluación
- TPR global; configuración Gherkin+modelo mejora varios pares, pero no supera consistentemente lenguaje natural.
- Claude 4.5 es el mejor: >80% en 4/6 pares y perfecto en algunas repeticiones.
- Más del 70% de fallos puede detectarse mediante análisis estático.
- Principales fallos: API inexistente 49%, mismatch de tipos 20.2%, constraint 11.5%.

## Artefactos
El paper usa repositorios GitHub y test suites humanas. No se verificó ejecutabilidad local ni commits exactos.

## Relación con nuestra tesis
Apoya el uso de especificaciones estructuradas como contexto verificable, pero no demuestra utilidad de documentación recuperada por requisito. Puede aportar criterios de verificación y separación humano/generado.

## Riesgos
- Pilot pequeño: tres sistemas y 10 repeticiones.
- Gherkin/modelo no se generan con el mismo pipeline bajo estudio.
- Actualización parcial, historia y cortes temporales no definidos.
- Fallos propagables sin feedback.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Hipótesis y arquitectura SSDE | Markdown/PDF | §§1–2, pp. 1257–1259 | Evidencia |
| Resultados y errores | Markdown/PDF | §§3–4, pp. 1259–1261 | Evidencia |
| Limitaciones futuras | Markdown/PDF | §§4–5, pp. 1260–1261 | Evidencia |

## Pendientes
Definir dataset ampliado, feedback y criterio de net productivity; validar commit/corte temporal; confirmar que Gherkin/domain models son humanos, no derivados del objetivo.
