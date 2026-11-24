# DisertacionFeup — Copilot, edición 2

Paquete completo de configuración y documentos iniciales, actualizado con el pipeline candidato de documentación generada, arquitectura y evolución. No contiene PDFs ni código experimental.

## Instalación o actualización
1. Haz una copia o commit de tu workspace actual.
2. Descomprime y combina el contenido con DisertacionFeup. No sobrescribas notas o decisiones locales sin comparar diferencias.
3. Abre la carpeta raíz en VS Code y utiliza GitHub Copilot.
4. Comprueba en la configuración de agentes que aparece orchestrator. Los especialistas se invocan mediante delegación y se ocultan del selector habitual.
5. Verifica que tu versión reconoce la cabecera YAML y sus herramientas. Si algún alias no está disponible, usa las completaciones de VS Code y revisa la documentación; no concedas todas las herramientas como solución automática.
6. No se fija modelo: selecciona uno disponible en tu cuenta y controla consumo y permisos.

Los agentes usan .github/agents/*.agent.md. Las instrucciones globales y por ruta se encuentran en .github/. La configuración está destinada al entorno Copilot; las funciones concretas pueden variar por versión.

## Primer mensaje a orchestrator
Lee shared/thesis-brief.md, shared/pipeline.md y shared/state.md. Comprueba qué herramientas y especialistas tienes. Delega en documentation-code la revisión de los enlaces del pipeline y en evaluation los riesgos de fuga documental. No edites nada todavía. Entrega sus resultados y tu síntesis. Si no puedes delegar, dilo y no simules la ejecución.

## Importación del corpus
Coloca PDFs en research/papers/pdf/ y nuevas incorporaciones en research/inbox/. Aporta tu hoja de clasificación existente. No hay catálogo precargado ni clasificaciones inventadas. Las carpetas research/papers/text/, research/notes/, research/reports/ y research/state-of-the-art/ ya existen para organizar las incorporaciones.
No asumas lectura nativa completa de PDF: solicita extracción/OCR local cuando haga falta, con aprobación antes de instalar herramientas. Conserva correspondencia con las páginas originales.

## Implementación
system/ es el área lógica del sistema. Conserva estructura, Git y licencias de RepoScope y otros repositorios existentes; no los reorganices para imitar un ejemplo.
El orquestador no tiene terminal. Para programar abre una sesión de implementación y selecciona herramientas según la tarea. No hace falta un noveno agente inicialmente.

## Precauciones
Los archivos de instrucciones no son una sandbox. Revisa permisos y cambios. Local significa ubicación del workspace, no que el modelo procese todo sin servicios externos.
No hay procesos de investigación permanentes: la sesión activa invoca agentes. El estado persistente está en archivos, no en memoria compartida automática.
No contiene resultados de reproducción ni verificación nueva de los repositorios de herramientas.

## Fuentes técnicas
https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference
https://code.visualstudio.com/docs/agent-customization/custom-instructions

Consulta CHANGELOG.md para los cambios conceptuales respecto al paquete inicial.
