import subprocess
import os

def clone_repositorio(path):
    link = input("Introduce el link del repositorio: ")
    #Ejecutar el comando git clone en la ruta especificada
    try:
        nombre_repositorio = link.rstrip('/').split('/')[-1].replace('.git', '')
        comando = ["git", "clone", link]
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd=path, check=True)
        print(resultado.stdout)
        # Ruta completa al directorio clonado
        ruta_clonada = os.path.join(path, nombre_repositorio)
        return ruta_clonada
    except subprocess.CalledProcessError as e:
        # Este error ocurre si el comando git falla (por ejemplo, si no es un repositorio git válido)
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida estándar del error: {e.stdout}")
        print(f"Error estándar del comando: {e.stderr}")
        return None
    except FileNotFoundError:
        # Este error ocurre si git no está instalado o no se encuentra en el sistema
        print("El comando git no se encuentra en el sistema. Asegúrate de que Git esté instalado.")
        return None
    except Exception as e:
        # Para otros errores generales
        print(f"Ocurrió un error inesperado: {e}")
        return None