from pathlib import Path

def get_project_path():
    path = input("Ingrese la ruta donde se clonará el proyecto: ")
    path_v = Path(path)
    if path_v.is_dir():
        return path_v
    else:
        return None