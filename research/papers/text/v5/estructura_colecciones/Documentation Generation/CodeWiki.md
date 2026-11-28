# CodeWiki — nota de lectura

- **Título:** *CodeWiki: Evaluating AI’s Ability to Generate Holistic Documentation for Large-Scale Codebases*
- **Autores:** Anh Nguyen Hoang, Minh Le-Anh, Bach Le y Nghi D. Q. Bui.
- **Versión local:** arXiv:2510.24428v6, 4 de abril de 2026. La fecha de primera versión pública no se verificó aquí.
- **Versión local analizada:** PDF de 24 páginas físicas, no incluido en el commit; [arXiv:2510.24428v6](https://arxiv.org/abs/2510.24428v6).
- **Cobertura:** análisis de las secciones de planteamiento, arquitectura, evaluación, conclusión y límites (pp. físicas 1–12); apéndices no revisados íntegramente. No se inspeccionó visualmente cada página.
- **Imagen:** [diagrama analítico del flujo](../../../../images/v5/estructura_colecciones/Documentation%20Generation/CodeWiki.svg), síntesis propia del método.

> Nota de investigación resumida; no es una transcripción del artículo.

## Problema y aporte

CodeWiki genera documentación jerárquica de repositorios a escala, buscando cubrir relaciones entre archivos, módulos y arquitectura, junto con diagramas y visualizaciones. El artículo introduce también CodeWikiBench, con rúbricas jerárquicas y evaluación basada en jueces LLM. (PDF local, abstract y §1, p. física 1; §4, p. física 5).

## Método

- Analiza repositorios con parsers Tree-sitter para construir relaciones entre entidades.
- Descompone la estructura en una jerarquía de módulos.
- Ejecuta agentes recursivos que documentan módulos hoja, con delegación dinámica.
- Ensambla documentación de abajo hacia arriba, sintetizando módulos padres a partir de sus hijos.
- Incluye síntesis textual y artefactos visuales como diagramas arquitectónicos y flujos de datos.

(PDF local, §§3.1–3.3, pp. físicas 4–6; Fig. 1, p. física 2).

## Evaluación reportada

La versión local afirma soporte para siete lenguajes y compara CodeWiki con varias alternativas, incluida DeepWiki. Reporta puntuación global de calidad 68.79% para CodeWiki y 64.06% para DeepWiki; el abstract atribuye una diferencia de 4.73% y también describe ganancias mayores en subconjuntos por lenguaje. No se interpreta aquí como mejora de generación de código. (PDF local, abstract, p. física 1; §5, pp. físicas 7–9).

El artículo declara límites en lenguajes de sistemas, en la validación humana piloto (tres participantes, tres repositorios) y en la evaluación basada en jueces/rúbricas generadas automáticamente. (PDF local, §6, pp. físicas 10–12; apéndice F, p. física 23).

## Relación acotada con la disertación

Es un candidato para documentación global generada y un referente de organización jerárquica. No equivale a RepoDocsAgent ni a documentación por API sin verificar esa implementación; tampoco resuelve por sí mismo la selección de documentos pertinentes a un requisito ni demuestra mejora de generación funcional.

## Evidencia y pendientes

| Afirmación | Localizador |
|---|---|
| Título, autores, versión y alcance | Abstract, p. física 1 |
| Análisis, descomposición jerárquica y síntesis | §3 y Fig. 1, pp. físicas 2, 4–6 |
| Benchmarks y rúbricas | §4, pp. físicas 5–6 |
| Resultados reportados | §5, pp. físicas 7–9 |
| Límites declarados | §6, pp. físicas 10–12; apéndice F, p. física 23 |

**Pendiente:** verificar la primera versión arXiv, el estado exacto del repositorio, licencia y condiciones de reproducibilidad. El informe no incorpora ejecución propia.
