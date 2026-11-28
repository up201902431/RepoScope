# CODEDOC — nota de lectura

- **Título:** *Standards-Guided and Dependency-Aware Code-Level Documentation Generation*
- **Autores:** Tingxu Han, Wei Song, Ziming Li, Yuchen Chen, Weisong Sun, Zhenpeng Chen, Chunrong Fang, Zhenyu Chen y Yang Liu.
- **Versión local:** arXiv:2610.27634v1, fechada 20 de octubre de 2026.
- **Versión local analizada:** PDF de 14 páginas físicas, no incluido en el commit; [registro arXiv:2610.27634v1](https://arxiv.org/abs/2610.27634v1).
- **Cobertura:** revisión analítica del texto extraído, con foco en §§2–5 y el apéndice (pp. físicas 2–11, 13–14). No se inspeccionó visualmente cada página.
- **Imagen:** [diagrama analítico del flujo](../../../../images/v5/estructura_colecciones/Documentation%20Generation/CodeDoc.svg). Es una síntesis nueva, no una copia de la figura del paper.

> Nota de investigación resumida; no es una transcripción del artículo.

## Problema y aporte

CODEDOC plantea que generar documentación de código no debería ser generación de texto sin especificación: deriva criterios de calidad de estándares de documentación y guías de estilo, y los usa tanto para guiar la generación como para evaluar/refinar el resultado. Su alcance es documentación por entidad (funciones y clases), organizada por ruta de código; no genera una descripción arquitectónica global del repositorio. (PDF local, §2.2, p. física 3; §3, pp. 3–6).

## Método

1. **Criterios offline:** extrae criterios candidatos desde ISO/IEC/IEEE 26514 y la guía de estilo de GitHub, con revisión manual de autores.
2. **Análisis del repositorio:** Pyan3 construye un grafo estático de llamadas; el análisis AST aporta jerarquía, firmas, parámetros y rangos de líneas.
3. **Generación por entidad:** el prompt combina código local, ruta, dependencias directas y criterios aplicables; los documentos se organizan por la ruta del código.
4. **Evaluación/refinamiento:** un LLM juez puntúa dimensiones y ofrece retroalimentación; el proceso permite una pasada de refinamiento.

La representación depende de análisis estático: en los repositorios evaluados la recuperación de dependencias tuvo alta precisión y recall más moderado, en especial con características dinámicas. (PDF local, §§3.1–3.4, pp. 3–7; §4.4, p. 10).

## Evaluación reportada

El estudio usa diez repositorios Python y compara con RepoAgent y un baseline de contexto largo bajo el mismo modelo GPT-5-mini. La Tabla 2 informa puntuaciones medias por rúbrica y régimen de evaluación; el paper reporta mejoras relativas de 11.6–17.0% frente a RepoAgent y 21.4–29.6% frente al baseline largo, además de menor consumo de tokens que este último. Son resultados reportados por el artículo, no reproducidos aquí. (PDF local, §4.3 y Tabla 2, p. física 8; §4.4 y Tablas 3–4, p. 10).

La evaluación automática se cotejó con evaluación humana y reporta Spearman ρ = 0.72. La cobertura de dependencias incompleta y la evaluación basada en jueces LLM siguen siendo límites relevantes. (PDF local, §4.2, p. 8; §5, pp. 10–11).

## Relación acotada con la disertación

Es pertinente como referencia de generación de documentación de entidades de código con contexto de dependencias y criterios explícitos. No prueba que pasar documentos a un generador de código mejore la corrección funcional; tampoco implementa la selección requisito→documento→API planteada en el brief.

## Evidencia y pendientes

| Afirmación | Localizador |
|---|---|
| Define documentación por entidad, no global | §2.2, p. física 3 |
| Criterios derivados de estándares y guías | §3.1, pp. físicas 3–4 |
| AST + grafo de llamadas y generación condicionada por dependencias | §§3.2–3.3, pp. físicas 4–7 |
| Comparación, puntuaciones y modelos | §4.3, Tabla 2, p. física 8 |
| Límites de validez y análisis estático | §§4.4–5, pp. físicas 10–11 |

**Pendiente:** verificar artefactos, licencia y reproducibilidad por separado. El PDF anuncia un repositorio, pero esta nota no lo consulta ni ejecuta.
