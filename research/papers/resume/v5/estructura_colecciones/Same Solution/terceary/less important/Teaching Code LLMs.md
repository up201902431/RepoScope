# Ficha — Teaching Code LLMs

## Identidad
- **Título:** *Teaching Code LLMs* (título bibliográfico exacto pendiente de cotejo; se mantiene el nombre de archivo sin expandirlo).
- **Autores/año/venue:** Pendiente de verificar en el original.
- **Fuente:** Extracción PyMuPDF, 27 páginas físicas; no inspeccionada visualmente.
- **Grupo:** Same Solution / terceary / less important.
- **Cobertura:** Lectura íntegra reportada previamente.

## Pregunta y contribución
Enseñar al modelo a usar contexto de proyecto para generar funciones. ToolGen inserta un marcador `<COMP>` en entrenamiento y aplica Jedi más búsqueda greedy restringida en inferencia para completar dependencias/identificadores. Es generación funcional con recuperación/decoding asistido, no simple completion de línea.

## Método
Entrenamiento con marcadores y herramientas de análisis Python; evalúa dependencias, lint, similitud y Pass@1. Implementación descrita como específica de Python.

## Documentos y arquitectura
Contexto de código/imports y dependencias, no documentación humana o generada. Tooling estático y resolución de símbolos no equivalen a enlaces documentales.

## Evaluación
La fuente reporta mejoras de Pass@1 de 40.0% para CodeT5 y 25.0% para CodeLlama, frente a los correspondientes sistemas base según abstract. CoderEval se menciona para Pass@1. Interpretar como mejoras relativas solo en el setting del artículo; verificar tablas antes de citar cifras.

## Artefactos
Disponibilidad del sistema, versión de Jedi, checkpoints y comandos no comprobados; no reproducido.

## Relación con nuestra tesis
Antecedente de interacción entre contexto externo y generación; diferente de recuperar APIs fijas y seleccionar documentos asociados. No atribuir la herramienta como generador documental.

## Riesgos
Dependencia de Python/Jedi; análisis estático puede fallar en código dinámico y no resolver correctamente imports. Distinguir métricas de lint/dependencia de corrección funcional.

## Evidencia
| Afirmación | Fuente/archivo | Sección y página PDF física | Tipo |
|---|---|---|---|
| Marcador `<COMP>` y herramientas Jedi/greedy. | Extracción del paper | Abstract/Method, pp. 1–8 | Método reportado |
| Mejoras de Pass@1 reportadas para CodeT5 y CodeLlama. | Extracción del paper | Abstract, pp. 1–2 | Resultado reportado |
| Evaluación por dependencias, lint, similitud y Pass@1. | Extracción del paper | Evaluation, pp. 9–13 | Métricas reportadas |

## Pendientes
Verificar título exacto, tabla y referencia de mejora, benchmarks, versiones de modelos y artefactos.
