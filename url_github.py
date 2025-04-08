import subprocess


def clone_repositorio(path):
    link = input("Introduce el link del repositorio: ")
    #Ejecutar el comando git clone en la ruta especificada
    try:
        comando = ["git", "clone", link]
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd=path, check=True)
        print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        # Este error ocurre si el comando git falla (por ejemplo, si no es un repositorio git válido)
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida estándar del error: {e.stdout}")
        print(f"Error estándar del comando: {e.stderr}")
        return False
    except FileNotFoundError:
        # Este error ocurre si git no está instalado o no se encuentra en el sistema
        print("El comando git no se encuentra en el sistema. Asegúrate de que Git esté instalado.")
        return False
    except Exception as e:
        # Para otros errores generales
        print(f"Ocurrió un error inesperado: {e}")
        return False