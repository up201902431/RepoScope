# RepoXray — nota de lectura

- **Título:** *Repoxray: A Retrieval-Augmented Framework for Semantic Analysis and Repository-Level Understanding of Software Codebases*
- **Autores:** Hrishita Gohain, Nidhi Pote, Manasi Rugle y Shehnaz Siddique.
- **Publicación indicada por el PDF:** *International Journal of Advanced Research in Science, Communication and Technology*, vol. 6, n.º 3, noviembre de 2026; DOI 10.48175/IJARSCT-40821.
- **Versión local analizada:** PDF de 10 páginas físicas (paginación impresa 172–181), no incluido en el commit; [DOI 10.48175/IJARSCT-40821](https://doi.org/10.48175/IJARSCT-40821).
- **Cobertura:** lectura analítica del texto extraído, centrada en §§III–VIII y resultados (pp. físicas 3–9). No se verificó el registro bibliográfico fuera del PDF ni se inspeccionó visualmente cada página.
- **Imagen:** [diagrama analítico del flujo](../../../../images/v5/estructura_colecciones/Documentation%20Generation/RepoXray.svg), síntesis propia.

> Nota de investigación resumida; no es una transcripción del artículo.

## Problema y aporte

RepoXray presenta una interfaz para analizar y explorar repositorios mediante análisis LLM por archivo, embeddings, búsqueda vectorial, síntesis Map–Reduce y preguntas en lenguaje natural. Produce informes de arquitectura y observaciones de seguridad; también incluye un explorador de archivos. (PDF local, §§III–V, pp. físicas 3–6).

## Método

El sistema adquiere y filtra un repositorio, resume archivos individualmente, codifica contenido con un servicio de embeddings, guarda vectores en PostgreSQL/pgvector y sintetiza resultados de archivo a nivel de repositorio. Para consultas, incrusta la pregunta, recupera contexto similar y lo entrega al LLM para generar una respuesta. (PDF local, §§IV–VI, pp. físicas 4–7).

## Evaluación reportada y cautela

El paper informa una evaluación de 20 repositorios públicos en cuatro lenguajes. Reporta cobertura de hechos arquitectónicos de 84.91% (394/464) y exactitud de preguntas RAG de 84.75% (150/177). La evaluación de seguridad aparece como N/A porque el conjunto no tenía vulnerabilidades positivas etiquetadas; la puntuación conjunta es un promedio de las otras dos métricas y no debe leerse como exactitud general del sistema. (PDF local, §VI-I–J, p. física 7; §VII, Tabla II, p. física 8).

Los resultados son declaraciones del artículo y no se reprodujeron. El alcance es comprensión/consulta de repositorio, no generación de funciones; el documento pide más evaluación de escalabilidad y seguridad. (PDF local, §VIII, p. física 9).

## Relación acotada con la disertación

Puede ser un antecedente de recuperación y síntesis de conocimiento de repositorio. No demuestra selección de documentación por requisito ni mejora de generación de código. Su informe arquitectónico no debe confundirse con recuperación de una arquitectura evaluada contra ground truth.

## Evidencia y pendientes

| Afirmación | Localizador |
|---|---|
| Flujo Map–Reduce, embeddings y preguntas RAG | §§IV–V, pp. físicas 4–6 |
| Implementación e interfaces | §VI, pp. físicas 6–7 |
| Dataset, métricas y límites de la evaluación | §VI-I–J–§VII, pp. físicas 7–8 |
| Conclusión y evaluación futura | §VIII, p. física 9 |

**Pendiente:** verificar formalmente la revista/DOI y los artefactos. La nota no considera el factor de impacto ni la etiqueta editorial como evidencia de calidad metodológica.
