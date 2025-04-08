import os
#Archivos py
from directorioProyecto import get_project_path


def main():
    path = get_project_path()
    if path != None:
        print("La ruta es correcta")
    else:
        print("La ruta no es correcta")
        main()


if __name__ == "__main__":
    main()