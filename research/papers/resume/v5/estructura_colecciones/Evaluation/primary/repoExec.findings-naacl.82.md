# REPOEXEC

## Identidad
- **paper_id:** no asignado; identificador local provisional `repoExec.findings-naacl.82`.
- **Título:** *On the Impacts of Contexts on Repository-Level Code Generation*.
- **Autores/año/venue:** Nam Le Hai et al.; Findings of NAACL 2025, pp. impresas 1496–1524.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/primary/repoExec.findings-naacl.82.md`; PDF `research/papers/pdf/Evaluation/primary/repoExec.findings-naacl.82.pdf`.
- **Grupo:** `Evaluation/primary`, clasificación original preservada.
- **Cobertura:** el informe declara lectura íntegra del Markdown; Tabla 4 cotejada visualmente en página local seleccionada. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** estudia impactos del contexto en generación de código a nivel de repositorio y propone benchmark Python.

**Interpretación:** aporta una medida de uso de dependencias, no una prueba directa de alineación con API de referencia ni del efecto de documentación.

## Método
Benchmark de 355 funciones Python en repositorios, con dependencias directas y tres tamaños de contexto. Test cases se generan con LLM, se filtran y mejoran por cobertura; cobertura lineal reportada sube de 92,46 % a 96,25 %. Se excluyen muestras bajo el umbral de cobertura descrito. Se evaluaron 18 modelos; también hay depuración iterativa y fine-tuning en experimentos separados.

## Documentos y arquitectura
El contexto es código y dependencias de repositorio; no se reporta generación o recuperación de documentos de arquitectura.

## Evaluación
Pass@1/5 y DIR. DIR se define como intersección entre identificadores generados y dependencias proporcionadas, dividida por el número de dependencias proporcionadas. DeepSeek-V3 aparece con DIR 80,35 en Full context. DIR mide uso de contexto según esa definición, no API F1 ni validez absoluta. El análisis se limita a dependencias llamadas directamente.

## Artefactos
El paper declara dataset, código y `pydepcall` disponibles. No se verificaron URL, versión, licencia ni ejecución.

## Relación con nuestra tesis
Útil como antecedente de reutilización de dependencias y tests; mantener DIR separado de API P/R/F1 y Pass@1.

## Riesgos
Los tests sintéticos generados por LLM siguen siendo una amenaza de validez aunque se filtren. Depuración/fine-tuning son condiciones distintas y no deben mezclarse sin control.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Benchmark y contexto | PDF/Markdown local | §§3–6, 3–10 | 1498–1505 | Método |
| Definición/resultados DIR | PDF/Markdown local | Tablas 3–4 | 1503 (física 8) | Resultado; Tabla 4 cotejada visualmente |
| Amenazas | PDF/Markdown local | Limitaciones | Dentro del rango 3–10 | Amenaza reportada |

## Pendientes
Auditar construcción de tests, umbrales, particiones y acceso al objetivo; no inferir reproducibilidad del anuncio de código/datos.
