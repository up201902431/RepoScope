# Hierarchical Repository-Level Code Summarization — nota de lectura

- **Título:** *Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs*
- **Autores:** Nilesh Dhulshette, Sapan Shah y Vinay Kulkarni.
- **Versión local:** arXiv:2501.07857v1, 14 de enero de 2025.
- **Versión local analizada:** PDF de 9 páginas físicas, no incluido en el commit; [arXiv:2501.07857v1](https://arxiv.org/abs/2501.07857v1).
- **Cobertura:** lectura analítica del texto extraído de método y evaluación (pp. físicas 1–7); referencias y página final no revisadas en detalle. No se inspeccionó visualmente cada página.
- **Imagen:** [diagrama analítico del flujo](../../../../images/v5/estructura_colecciones/Documentation%20Generation/HierarchicalRepository.svg), síntesis propia.

> Nota de investigación resumida; no es una transcripción del artículo.

## Problema y aporte

El trabajo aborda resúmenes de código de negocio en varios niveles. Propone dividir el código en entidades pequeñas que puedan procesarse con LLM locales, agregar los resúmenes hasta nivel de archivo y paquete, y proporcionar contexto del dominio y problema para mejorar la relevancia de los resúmenes. (PDF local, abstract y §§I–III, pp. físicas 1–4).

## Método

Un parser Java crea un AST y segmenta el código en funciones, variables, constructores, enums e interfaces. Se resumen esos segmentos con LLM locales; luego se agregan en resúmenes de archivo y paquete. Para archivo y paquete se incorpora contexto de negocio/dominio mediante prompts. (PDF local, §III y Fig. 1, pp. físicas 3–4).

## Evaluación reportada

El trabajo estudia un sistema BSS de telecomunicaciones, pero por restricciones de propiedad intelectual presenta resultados con un repositorio público descrito como de características similares. Usa ROUGE-L, BLEU, BERTScore, similitud semántica y evaluación G-Eval; también incluye evaluación experta. El paper reporta que el análisis sintáctico jerárquico mejora cobertura y que el contexto de negocio mejora especificidad de dominio. (PDF local, §IV, p. física 5; §V, pp. físicas 5–7).

La evidencia es específica a Java y a un contexto empresarial. No demuestra que los resúmenes se utilicen para seleccionar documentación para un requisito de generación de código.

## Relación acotada con la disertación

Puede servir como antecedente de resúmenes jerárquicos y documentación derivada de código. Mantenerlo distinto de la generación de API-Doc/File-Doc/Module-Doc y de recuperación de arquitectura; su salida descrita es resumen funcional de entidades, archivos y paquetes.

## Evidencia y pendientes

| Afirmación | Localizador |
|---|---|
| Propone segmentación y agregación jerárquica con LLM locales | Abstract, §I, pp. físicas 1–2 |
| AST y niveles de resumen | §III y Fig. 1, pp. físicas 3–4 |
| Contexto de negocio y diseño de evaluación | §§III-D–IV, pp. físicas 4–5 |
| Resultados de segmentos y grounding de dominio | §V, Tablas III–VII, pp. físicas 6–7 |

**Pendiente:** verificar metadatos de publicación formal, artefactos, licencia y los detalles del conjunto público usado como proxy.
