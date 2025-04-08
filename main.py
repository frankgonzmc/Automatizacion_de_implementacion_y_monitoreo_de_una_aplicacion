import os
#Archivos py
from directorioProyecto import get_project_path
from url_github import clone_repositorio


def main():
    path = get_project_path()
    if path != None:
        print("La ruta es correcta")
        #Llamar a la funcion para clonar el repositorio
        if clone_repositorio(path):
            print("Repositorio clonado correctamente")
        else:
            print("Error al clonar el repositorio")
    else:
        print("La ruta no es correcta")
        main()


if __name__ == "__main__":
    main()