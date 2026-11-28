# Needle in the Repo

## Identidad
- **paper_id:** no asignado; identificador local provisional por título.
- **Título:** *Diagnosing Maintainability Failures in AI-Generated Repository Edits*.
- **Autores/año/venue:** Haichao Zhu et al.; ASE 2026.
- **Fuente:** `research/papers/text/v5/estructura_colecciones/Evaluation/secondary/Needle in the Repo.md`; PDF homónimo en `research/papers/pdf/Evaluation/secondary/`.
- **Grupo:** `Evaluation/secondary`, sin reclasificación.
- **Cobertura:** Markdown íntegro declarado; Tablas 2–3 cotejadas visualmente en página local seleccionada. PDF completo no inspeccionado.

## Pregunta y contribución
**Hecho:** diagnostica fallos de mantenibilidad en ediciones de repositorio generadas por IA, además de corrección funcional.

**Interpretación:** advierte que tests funcionales no cubren todas las propiedades estructurales; no mide selección documental.

## Método
21 probes C++ en nueve dimensiones de mantenibilidad: 10 casos micro y 11 multi-etapa. Cada caso combina tests funcionales ocultos con un oráculo estructural oculto.

## Documentos y arquitectura
No genera ni evalúa documentos; las propiedades examinadas son estructura y mantenibilidad de cambios de código.

## Evaluación
23 configuraciones; éxito exige pasar ambos oráculos. Los totales son combinaciones configuración–caso (483), no intentos independientes ni estimaciones poblacionales. Reporta 36,2 % de resultados que pasan ambos oráculos; 64/483 (13,3 %) pasan tests pero fallan el oráculo estructural. Se distinguen errores funcionales, estructurales y de compilación.

## Artefactos
El paper declara repositorio y DOI Zenodo; disponibilidad, licencia y ejecución no comprobadas.

## Relación con nuestra tesis
Útil para contextualizar límites de Pass@1 como medida única; C++ y probes de mantenibilidad no evalúan la intervención documental propuesta.

## Riesgos
Los autores advierten que oráculos específicos no conforman taxonomía universal de mantenibilidad. Dimensiones con pocos casos son diagnósticas, no estimaciones generales.

## Evidencia
| Afirmación | Fuente | Sección/página PDF física | Página impresa | Tipo |
|---|---|---:|---:|---|
| Suite y protocolo | PDF/Markdown local | §§3–5, 2–9 | 893–900 | Método |
| Resultados y distinción de fallos | PDF y rasters locales | Tablas 2–3, física 7 | 898 | Resultado; cotejo visual |

## Pendientes
Verificar repositorio/DOI y analizar si alguna métrica estructural resulta pertinente al alcance fijado para la tesis.
