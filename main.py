import os
import time
#Archivos py
from directorioProyecto import get_project_path
from url_github import clone_repositorio
from crear_entorno_virtual import ejecutar_comando_entorno_virtual
from activar_entorno import activar_entorno_virtual
from instalar_dependencias_requeriments import instalar_dependencias

def main():
    path = get_project_path()
    if path != None:
        print("La ruta es correcta")
        #Llamar a la funcion para clonar el repositorio
        respuesta = clone_repositorio(path)
        if respuesta != None:
            print("Repositorio clonado correctamente")
            #Ir al directorio de proyecto clonado
            os.chdir(respuesta)
            print("Esperando 3 segundos...")
            time.sleep(3)  # Pausa de 3 segundos
            print("Creando entorno virtual...")
            #Crear entorno virtual
            ejecutar_comando_entorno_virtual()
            #Activar entorno virtual
            print("Activando entorno virtual...")
            time.sleep(3)
            activar_entorno_virtual()
            #Instalar dependencias
            print("Instalando dependencias...")
            time.sleep(3)
            instalar_dependencias()
            

        else:
            print("Error al clonar el repositorio")
    else:
        print("La ruta no es correcta")
        main()


if __name__ == "__main__":
    main()