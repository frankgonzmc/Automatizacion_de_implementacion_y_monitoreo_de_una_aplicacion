Imagina que eres parte de un equipo de DevOps encargado de desplegar una aplicación web en un servidor Linux. Debes crear un script que cumpla las siguientes funciones:

Desplegar la aplicación:

. El script debe descargar el código fuente de la aplicación desde un repositorio Git (puede ser un repositorio privado o público de GitHub).

. El script debe configurar un entorno virtual de Python (si la aplicación es en Python) o instalar las dependencias necesarias según el lenguaje de la aplicación.

. Debe configurar un servidor web (por ejemplo, Nginx o Apache) para servir la aplicación.

Gestión de configuración:

. El script debe modificar un archivo de configuración de la aplicación con valores específicos (por ejemplo, cambiar un puerto o una clave API). Usa un archivo .env o un archivo de configuración similar que el script pueda editar.

. Debe realizar un backup del archivo de configuración original antes de hacer cualquier cambio.

Monitoreo básico:

. El script debe comprobar si el servidor web está funcionando correctamente después de la implementación.

. Implementa un simple script de monitoreo que verifique que la aplicación responde correctamente. Puedes hacerlo con curl o wget para hacer una petición HTTP al servidor.

. Si el servidor web no responde (código de estado 500, 502, etc.), el script debe enviar una alerta por correo electrónico (puedes usar mail o integrar con un servicio como SendGrid).

Logs y manejo de errores:

. El script debe registrar todos los pasos de la implementación y monitoreo en un archivo de log. Registra la fecha, hora y cualquier error que se produzca durante el proceso.

. Si algún paso falla (por ejemplo, si la aplicación no se puede descargar desde Git o si el servidor no se puede reiniciar), el script debe detenerse y registrar el error.

Requisitos adicionales:
. El script debe ser reutilizable, es decir, puede ser ejecutado múltiples veces sin problemas.

. Asegúrate de que tu script sea idempotente, es decir, que pueda ejecutarse varias veces sin cambiar el estado del sistema si ya ha sido aplicado correctamente.

Utiliza buenas prácticas de manejo de errores, como comprobaciones de estado de los comandos.
