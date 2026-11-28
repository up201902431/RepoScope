# Ficha canónica de paper

## Identidad
- paper_id: pendiente
- título: *Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs*
- autores/año/venue/DOI: pendientes de verificación bibliográfica
- fuente original: extracción local
- PDF/texto/procedencia: `research/papers/text/v5/estructura_colecciones/Related/fourth/hierarchical repository.md`
- grupo/etiquetas: Related/fourth; documentation/summarization
- cobertura: Markdown leído íntegramente; PDF no cotejado visualmente de forma sistemática

## Pregunta y contribución
¿Cómo resumir jerárquicamente código Java de una aplicación empresarial con LLM locales, incorporando contexto de negocio?

## Método
- entrada: unidades sintácticas Java y contexto de negocio
- análisis: identificación de funciones, variables, clases/interfaces y paquetes
- generación: resúmenes locales agregados hacia archivo y paquete
- salida: documentación textual jerárquica
- granularidad: función/variable → clase/archivo → paquete
- generación local: el texto extraído enfatiza LLM locales, sin lista completa ni configuración verificable

## Documentos y arquitectura
- documentación generada desde código
- origen: código Java y contexto empresarial
- no conserva trazabilidad requisito→API→documento en el sistema descrito
- estructura jerárquica y agregación de resúmenes

## Evaluación
- caso declarado: sistema BSS de telecomunicaciones
- magnitudes extraídas: 122 clases, 20 interfaces, 762 funciones, 704 variables y 36 paquetes
- métricas: cobertura de análisis sintáctico y relevancia al añadir contexto de negocio
- resultados: el texto afirma mejor cobertura con análisis sintáctico y mayor relevancia con contexto empresarial; cifras completas pendientes
- selección/exclusiones y repositorios de referencia: pendientes

## Artefactos
- el texto menciona repositorio/artifacto, no verificable en esta lectura
- disponibilidad, licencia, versión y ejecución: pendientes

## Relación con nuestra tesis
Es el antecedente documental más cercano del lote: demuestra generación jerárquica de resúmenes desde código. Sin embargo, no prueba selección de documentación según requisito ni asociación explícita a APIs recuperadas. En la tesis sería un candidato de fuente documental generada, separado de documentos humanos y evaluado solo bajo el mismo set de APIs.

## Riesgos
- documentación derivada puede contener o revelar soluciones si usa contexto futuro
- calidad dependiente de contexto de negocio y lenguaje Java
- las métricas cualitativas no equivalen a API P/R/F1 ni Pass@1
- posible mezcla de resúmenes humanos/generados si se reutilizan sin etiquetado

## Evidencia
| Afirmación | Fuente/archivo | Sección/página | Tipo |
|---|---|---|---|
| Resumen jerárquico de unidad a paquete | `research/papers/text/v5/estructura_colecciones/Related/fourth/hierarchical repository.md` | abstract, introducción y método; PDF pp. 1–9 según extracción | Hecho extraído |
| BSS y magnitudes del caso | mismo archivo | evaluación de la extracción | Hecho extraído |
| Falta de enlace explícito requisito-API-documento | síntesis del lote | interpretación | Interpretación |

## Pendientes
- ver portada, bibliografía, paginación y tablas
- confirmar modelos, prompts, longitud y criterios
- verificar artefacto, licencia y procedencia
