import subprocess

def ejecutar_comando_entorno_virtual():
    comando = ['python3', '-m', 'venv', 'venv']
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("Entorno virtual creado con éxito.")
        print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        # Este error ocurre si el comando falla (por ejemplo, si python no está instalado o no se encuentra en el sistema)
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida estándar del error: {e.stdout}")
        print(f"Error estándar del comando: {e.stderr}")
        return False
    except FileNotFoundError:
        # Este error ocurre si python no está instalado o no se encuentra en el sistema
        print("El comando python no se encuentra en el sistema. Asegúrate de que Python esté instalado.")
        return False
    except Exception as e:
        # Para otros errores generales
        print(f"Ocurrió un error inesperado: {e}")
        return False