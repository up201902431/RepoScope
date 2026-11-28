# FeatX: Editing Software by Editing Features for Repository-Level Code Evolution

## Identidad
- **paper_id:** alias provisional `FeatX`.
- **Título:** *FeatX: Editing Software by Editing Features for Repository-Level Code Evolution*.
- **Autores:** Xutian Li, Yifeng Zhu, Xianlin Zhao, Yanzhen Zou, Lu Zhang y Bing Xie.
- **Año/venue:** ASE ’26; arXiv 2606.31206; 4 páginas.
- **Fuente original:** Markdown `.../fourth/FeatX.md`; PDF `.../pdf/Documentation-Code/fourth/FeatX.pdf`.
- **Procedencia/cobertura:** lectura íntegra de las 4 páginas extraídas. Extracción PyMuPDF no verificada visualmente.
- **Grupo/etiquetas:** `Documentation-Code/fourth`.

## Pregunta y contribución
Herramienta orientada a features que extrae epics/features jerárquicos con enlaces explícitos a entidades de código y traduce edición de feature a diff mediante un agente en tres etapas.

## Método
- Construye matriz estructural y semántica, las fusiona y clustera a nivel fichero/función.
- Evolution Agent amplía contexto estático/semántico, localiza y planifica, y modifica código.
- Interfaz con Feature Panel, CodeMap, Agent Panel y Diff Panel.

## Documentos y arquitectura
Genera una abstracción jerárquica de features y mapas feature–código; no genera README/API-doc ni conserva historia temporal por commit. Es documentación derivada del repositorio, no documentación humana. No presenta modelo arquitectónico compatible.

## Evaluación
- 38 commits de cinco repos Java.
- User study 10 participantes: NASA-TLX `12.5→7.4`, SUS `73→84`.
- F1 localización a nivel función `0.385`, frente a `0.270` de Claude-opus-4.5: mejora relativa 42.6%.
- Coste LLM total declarado `$0.07`, frente a `$45.05` para Claude directo.

## Artefactos
Repo declarado `github.com/a496263365/FeatX/tree/demo` y dataset; no comprobados localmente. No se verificaron licencia/commit/ejecución.

## Relación con nuestra tesis
Puede aportar una abstracción editada por intención y trazabilidad interna feature–código, pero no prueba selección de documentación según requisito ni integración con API retrieval.

## Riesgos
- Ground truth de función extraído de commits y validado parcialmente manualmente.
- Feature extraction puede incorporar código solución y filtrar mal objetivos.
- Evaluación humana pequeña y sesgo de idiomas.
- Coste no incluye infraestructura/interacción humana.

## Evidencia
| Afirmación | Fuente/archivo | Sección/página PDF física | Tipo |
|---|---|---|---|
| Diseño e interfaz | Markdown/PDF | §§1–3, pp. 1–3 | Evidencia |
| Estudios y métricas | Markdown/PDF | §4, pp. 3–4 | Evidencia |
| Limitaciones futuras | Markdown/PDF | §5, p. 4 | Evidencia |

## Pendientes
Comprobar release/demo y licencia; separar extracción de feature humana/derivada; validar generalización fuera de Java y commits reales.
