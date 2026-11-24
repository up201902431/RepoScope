# Matriz de componentes candidatos

Estado: síntesis de conversación y fuentes indicadas; no verificación de ejecución ni soporte actual de repositorios. Confirmar artefactos y versiones antes de seleccionar.

| Componente | Papel | No confundir con | Fuente para verificar |
|---|---|---|---|
| RepoDocsAgent (RepoMind) | API-Doc, File-Doc y Module-Doc desde código y contexto | Solo documentación de firmas | RepoMind, sección 3.2 |
| CodeWiki (FSoft-AI4Code) | Documentación global y diagramas de repositorio | Todos los productos llamados CodeWiki; modelo automáticamente compatible con TransArC | Repositorio oficial y paper CodeWiki |
| SemArc | Recuperación de estructura arquitectónica apoyada en dependencias y semántica | Generador idéntico a CodeWiki | ChangeWiki 3.3.1 y artículo SemArc |
| ChangeWiki | Resúmenes jerárquicos de cambios entre dos versiones e historia | Documentación exhaustiva de una sola versión o seguimiento automático de cambios en documentos humanos | ChangeWiki 3.1–3.4 y 6.3 |
| KDM | Metamodelo/representación de conocimiento del software | IA que redacta arquitectura | TransArC 4.1.1 y especificación KDM |
| ArDoCo | Texto arquitectónico ↔ modelo arquitectónico existente | Generación texto→imagen | Paper TransArC 3 y 4.2 |
| ArCoTL | Modelo arquitectónico estructurado ↔ código | Análisis directo de PNG/JPG | Paper TransArC 4.1 |
| TransArC | Composición texto↔modelo↔código | Herramienta llamada TLR | Paper TransArC 4.2 |
| TAROT / FTLR | Recuperación requisitos↔código | Método ya validado requisito↔documento arbitrario | Papers originales; TransArC 2 y 5.3 |
| IRBM | Enfoque híbrido requisitos↔código a estudiar | Filtro documental directamente equivalente | A Hybrid Approach Combining IR and LLMs for TLR |
| ArtifactSync | Impacto de cambios y mantenimiento de consistencia entre artefactos | Generador inicial equivalente a RepoDocsAgent | ArtifactSync 2 y 6 |
| RepoAgent / DeepWiki-Open | Alternativas documentales opcionales | Dependencias seleccionadas | Fuentes originales por revisar |
| ARTEMIS | Papel exacto pendiente de lectura del material | Clasificación automática por nombre | Paper original disponible |

## Hechos relevantes y límites de la evidencia
TransArC: representación de componentes, interfaces y firmas; implementación descrita para UML/PCM y Java/Bash. No asumir que un Mermaid generado sirve como entrada.
ChangeWiki: evaluación en C/C++; extensión a otros lenguajes pendiente según paper. Comprobar adaptadores antes de usar con Python.
SemArc: aquí se conoce por su uso en ChangeWiki; falta revisar directamente su paper/implementación.
No se eligió generador texto→modelo/diagrama compatible. Una visualización no es requisito automático para enriquecer prompts con texto.

## Fuentes locales sugeridas
RepoMind.pdf; TLR_Recovering-Trace-Links-Between-Software-Documentation-And-Code.pdf; ChangeWiki.pdf; ArtifactSync.pdf; IRBM_A-Hybrid-Approach-Combining-Information-Retrieval-and-Large-Language-Models-for-Traceability-Link-Recovery.pdf.
Las rutas exactas se completan tras inventario. No usar IDs internos de otra plataforma como referencias bibliográficas.
