# Alcance de la disertación

## Pregunta central de trabajo
¿Enriquecer el contexto de generación con documentación vinculada explícitamente a APIs recuperadas y seleccionada según el requisito mejora corrección funcional y alineación de reutilización de APIs?

## Núcleo previo
RepoScope es el baseline principal previamente decidido. El usuario informa que reprodujo resultados; falta enlazar evidencia local, commit y comandos.
Comparación central: RepoScope original frente a RepoScope + módulo documental, manteniendo tareas, modelo, parámetros y APIs recuperadas.
Métricas previstas: Pass@1 y API Precision/Recall/F1. Definiciones operativas incompletas.

## Intención actual ampliada del usuario
Seleccionar proyectos de CoderEval, DevEval y RepoExec; aprovechar documentación humana y generar documentación donde sea escasa. Estudiar arquitectura y cambios/versiones. Explorar RepoMind además de RepoScope.
Esta es la dirección candidata, no una aprobación de ejecutar todos los benchmarks ni integrar todas las herramientas.
Consulta pipeline.md y component-matrix.md.

## Aporte a delimitar
Enlace explícito y selección de documentos por requisito sobre APIs recuperadas. Usar un generador de otro trabajo no convierte esa generación en contribución original.
Para documentación generada, estudiar reorganización/selección de conocimiento del código; para humana, información documental disponible. No mezclar ambas conclusiones.

## Antecedentes y cautelas
RepoMind: RepoDocsAgent genera API-Doc, File-Doc y Module-Doc. Código publicado según comprobación previa del usuario; escenario exacto por validar.
CodeAgent puede llevar documentación al generador: no justificar novedad afirmando lo contrario.
La lista previa de 39 proyectos de RQ1 de RepoScope no está validada contra protocolo publicado.
ACK es nombre informal sin definición aprobada; no atribuir estándar ni expansión.

## Pendiente
Subconjuntos y lenguajes finales, requisitos disponibles por benchmark, identidad de APIs, documentos permitidos, criterio de escasez, uso real de historia, presupuesto y RQs definitivas. Idioma final de tesis por confirmar.
