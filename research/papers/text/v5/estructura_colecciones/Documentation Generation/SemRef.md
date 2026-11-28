# SemRef — nota de lectura

- **Título:** *Semantic-Enhanced Automatic Refinement of Architecture Recovery Results Using LLMs*
- **Autores:** Yiran Zhang, Chengwei Liu, Yuqiang Sun, Zhengzi Xu, Weisong Sun, Wenke Li, Wuxia Jin y Yang Liu.
- **Publicación/versión local:** ICSE ’26 (12–18 de abril de 2026); arXiv:2607.23774v1, 26 de julio de 2026. La fecha de versión arXiv es posterior a las fechas de la conferencia y se registra por separado.
- **PDF:** [`SemRef.pdf`](../../../../pdf/Documentation%20Generation/SemRef.pdf), 13 páginas físicas.
- **Cobertura:** lectura analítica del método, resultados y discusión (pp. físicas 1–11); referencias no revisadas en detalle. No se inspeccionó visualmente cada página.
- **Imagen:** [diagrama analítico del flujo](../../../../images/v5/estructura_colecciones/Documentation%20Generation/SemRef.svg), síntesis propia.

> Nota de investigación resumida; no es una transcripción del artículo.

## Problema y aporte

SemRef toma resultados existentes de recuperación de arquitectura de software (SAR) y los refina semánticamente. No es principalmente un generador de documentación: busca mejorar agrupaciones y jerarquías de módulos obtenidas por herramientas de recuperación arquitectónica. (PDF local, §1, p. física 1; §3, pp. físicas 3–6).

## Método

Combina información estructural/de dependencias con análisis LLM de resúmenes de archivos y módulos. Construye/refina la jerarquía de módulos de manera iterativa; las operaciones descritas incluyen colocación, detección de módulos mal ubicados, división/fusión y refinamiento de módulos hoja. El resultado incluye arquitectura refinada y resúmenes para ayudar a comprender módulos. (PDF local, §3.1–3.4, pp. físicas 3–6; §5.1, p. física 11).

## Evaluación reportada

Evalúa sobre nueve proyectos y diez herramientas SAR de entrada; compara arquitectura de entrada y salida con cinco métricas. El paper reporta mejoras en métricas de recuperación, con variación según proyecto y medida; al combinar SemRef con SARIF compara también frente al mejor baseline por proyecto y métrica. No se interpreta como una comparación de generación de código. (PDF local, §4, Tablas 2–3, pp. físicas 7–8; Tabla 6, p. física 9).

## Relación acotada con la disertación

Es pertinente a la línea de comprensión/recuperación arquitectónica del pipeline candidato. Debe mantenerse separado de CodeWiki (documentación global) y de RepoDocsAgent (documentación de entidades); la arquitectura de SemRef es una estructura recuperada/refinada, no un texto documental ni un diagrama generado.

## Evidencia y pendientes

| Afirmación | Localizador |
|---|---|
| Motivación y definición de refinamiento SAR | §1, p. física 1 |
| Construcción y refinamiento jerárquico | §3, pp. físicas 3–6 |
| Comparación de salida/entrada y métricas | §4, Tablas 2–3, pp. físicas 7–8 |
| Discusión y resúmenes de módulos | §5.1, p. física 11 |

**Pendiente:** verificar acceso, código/datos y detalles de reproducción del sitio/recurso anunciado; no se ejecutó ni consultó ningún artefacto externo.
