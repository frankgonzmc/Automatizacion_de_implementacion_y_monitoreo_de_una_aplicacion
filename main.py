import os
import time
#Archivos py
from directorioProyecto import get_project_path
from url_github import clone_repositorio
from crear_entorno_virtual import ejecutar_comando_entorno_virtual
from activar_entorno import activar_entorno_virtual_instalar_dependencias
from instalar_gunicorn import install_gunicorn
from instalar_nginx import instalar_nginx

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
            respuesta_entorno_virtual = ejecutar_comando_entorno_virtual()
            if (respuesta_entorno_virtual == True):
                #Activar entorno virtual
                print("Activando entorno virtual...")
                time.sleep(3)
                respuesta_activar_entorno_y_instalar_dependencias = activar_entorno_virtual_instalar_dependencias()
                if (respuesta_activar_entorno_y_instalar_dependencias == True):
                    #Instalar dependencias
                    print("Entorno virtual y dependencias instaladas con exito...")
                    print("Preparando instalacion de gunicorn.")
                    time.sleep(3)
                    print("Instalado gunicorn...")
                    time.sleep(3)
                    respuesta_install_gunicorn = install_gunicorn()
                    if (respuesta_install_gunicorn == True):
                        print("Instalacion de gunicorn exitosa.")
                        print("Instalado nginx en SO.")
                        time.sleep(3)
                        respuesta_nginx = instalar_nginx()
                        if (respuesta_nginx == True):
                            print("SUCCESS")
                        else:
                            print("Proceso finalizado.")
                    else:
                        print("Error al instalar gunicorn.")
                else:
                    print("Error al activar entorno virtual y/o instalar dependencias.")
            else:
                print("Error al crear entorno virtual.")    

        else:
            print("Error al clonar el repositorio")
    else:
        print("La ruta no es correcta")
        main()


if __name__ == "__main__":
    main()