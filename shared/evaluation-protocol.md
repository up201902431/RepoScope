# Protocolo experimental — borrador no cerrado

## Objetivo
Aislar aporte documental sobre APIs recuperadas fijas. Cambiar recuperador es otra variante.
No iniciar evaluación final hasta aprobar definiciones bloqueantes.

## Datos
Confirmar benchmarks, lenguajes, repositorios, commits, task_ids, tests y políticas de exclusión. Detectar solapamientos entre benchmarks; no contar tareas duplicadas como evidencia independiente.
Separar desarrollo/validación y evaluación final. Congelar configuración antes de ver resultados finales.
Reproducción publicada y ejecución bajo protocolo común deben registrarse por separado.

## Documentos
Etiquetar origen humano/generado/mixto, tipo, versión, generador, modelo, configuración, coste y fuentes utilizadas. Criterio de escasez y política de fallback pendientes.
Distinguir API/file/module docs, arquitectura textual, modelos estructurados, diagramas y evolución.
Conservar procedencia; revisar exactitud y cobertura en una muestra sin usar esa muestra para ajustar el test final.
No confundir calidad documental, link P/R/F1 y API P/R/F1.

## Prevención de fuga
Antes de todo preprocesamiento definir vista permitida por tarea: retirar cuerpo objetivo y derivados no autorizados. Revisar clase contenedora, caller/callee context, copias, ejemplos, docs previas y generadas.
Aislar caches e índices por manifiesto de código permitido; un documento generado en otra tarea puede contener esta solución.
Definir acceso a Git/historia/diffs/mensajes y corte temporal. Resúmenes históricos pueden revelar la implementación. Bloquear acceso remoto que la reponga.
Registrar excepciones y excluir con política previa, no después de ver rendimiento.

## Generación
Mismas tareas, modelo, parámetros, APIs recuperadas y configuración de tests. Registrar prompts y diferencias de tokens/contexto/latencia/coste.
Modelo y sistema de generación documental son preprocesamiento separado, reproducible y declarado.
No contar correcciones manuales como salida del sistema.

## Corrección
Pass@1 previsto. Definir número de muestras, estimador, semillas, timeouts, reintentos, fallos de infraestructura y agregación. Una muestra por tarea permite proporción observada de aciertos; no confundir con otros estimadores pass@k.

## APIs
Formulación candidata con conjuntos G generadas y R de referencia:
P=|G∩R|/|G| si G no vacío; Rcl=|G∩R|/|R| si R no vacío; F1=2P·Rcl/(P+Rcl) si suma positiva.
No define aún vacíos ni agregación. Métricas de alineación, no corrección absoluta.
Pendiente: qué API cuenta, internas/externas, resolución cualificada, alias/herencia/reexports, estático/dinámico, conjuntos/multiconjuntos, código no parseable, vacíos, macro/micro y muestras que fallan tests.
ACK: término informal pendiente. DIR de RepoExec y entidades de DRAG requieren inspección antes de reutilizar código o atribuir protocolo. No confundir F1 de awareness de A³-CodGen.

## Comparación y artefactos
Comparación pareada e incertidumbre a definir según datos. Ablaciones propuestas en pipeline.md no aprobadas automáticamente.
Guardar run_id, commits, IDs, manifiesto permitido, hashes documentales, configuración, prompts, salidas crudas, tests, extracción de APIs, métricas, coste y desviaciones.
