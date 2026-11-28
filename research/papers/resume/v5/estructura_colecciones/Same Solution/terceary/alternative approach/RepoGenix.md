# Ficha — RepoGenix

## Identidad
- **Título:** *RepoGenix: Dual Context-Aided Repository-Level Code Completion with Language Models*.
- **Autores/año/venue:** Ming Liang et al.; ASE 2024, según la primera página extraída; DOI 10.1145/3691620.3695331.
- **Fuente:** Markdown PyMuPDF de 2 páginas; paginación física desde 1, no verificada visualmente.
- **Grupo:** Same Solution / terceary / alternative approach.
- **Cobertura:** Texto completo (2 páginas) consultado.

## Pregunta y contribución
Reducir la latencia de completion repository-level sin perder la utilidad de contexto. Combina **analogous context** (código similar) y **relevant context** (relaciones/entidades relevantes, extendiendo un Code Property Graph) y usa Context-Aware Selection (CAS) para comprimir el prompt.

## Método
Completion de código; recuperación dual, selección de contexto con límite de tokens y generación por modelo de lenguaje. Es aceleración/selección para completion, no reparación, revisión ni generación documental.

## Documentos y arquitectura
Fuentes principales: chunks de código, entidades y relaciones de importación/dependencia. No propone docs humanos o generados ni un enlace a documentación de APIs.

## Evaluación
CrossCodeEval, subconjunto Python, StarCoder-7B. Tabla 1 informa: contextos de 4096 tokens para analog/relevant/RepoGenix sin CAS y 2048/1024 con CAS. Para Relevant Context: ES 78.69, ID-F1 74.85; ambos contextos sin CAS: ES 80.82, ID-F1 77.31; CAS 2048: ES 80.27, ID-F1 76.36 y speedup 33.29%; CAS 1024: ES 79.73, ID-F1 75.29 y speedup 48.41%. El abstract reporta reducción de tiempo de inferencia de 48.41%. No confundir estos resultados con Pass@1.

## Artefactos
El artículo afirma implementación y prueba en entorno Ant Group y futura apertura; no se comprobó código público ni se reprodujo.

## Relación con nuestra tesis
Compara fuentes de contexto y presupuesto, pero no documentación enlazada explícitamente a APIs. No sustituye a RepoScope ni permite inferir aporte causal documental.

## Riesgos
Solo benchmark Python reportado en el texto consultado; generalización limitada. La comparación de latencia depende del presupuesto/contexto y del entorno.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Tipo |
|---|---|---|---|
| Contexto análogo + relevante y CAS. | Extracción | Abstract e Introduction, p. 1; RepoGenix in a Nutshell, pp. 1–2 | Método |
| CrossCodeEval Python, StarCoder-7B y valores ES/ID-F1/speedup. | Extracción | Evaluation, Table 1, p. 2 | Resultados reportados |
| El código se declara en proceso de extensión/open-source, no se verifica disponibilidad. | Extracción | Abstract, p. 1 | Anuncio de autores |

## Pendientes
Validar visualmente tabla y configuración; verificar artefactos/commit; no hay reproducción local.
