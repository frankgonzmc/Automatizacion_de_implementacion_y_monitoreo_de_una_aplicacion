import os
#Archivos py
from directorioProyecto import get_project_path
from url_github import clone_repositorio


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
        else:
            print("Error al clonar el repositorio")
    else:
        print("La ruta no es correcta")
        main()


if __name__ == "__main__":
    main()