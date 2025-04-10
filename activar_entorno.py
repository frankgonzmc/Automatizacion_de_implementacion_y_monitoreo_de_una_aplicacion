import subprocess

def activar_entorno_virtual():
    comando = ['venv\\Scripts\\activate.bat']
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("Entorno virtual activado con éxito.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        # Este error ocurre si el comando falla (por ejemplo, si el entorno virtual no se encuentra o no se puede activar)
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida estándar del error: {e.stdout}")
        print(f"Error estándar del comando: {e.stderr}")
    except FileNotFoundError:
        # Este error ocurre si el entorno virtual no existe o no se encuentra en la ruta especificada
        print("El entorno virtual no se encuentra en la ruta especificada. Asegúrate de que el entorno virtual esté creado.")
    except Exception as e:
        # Para otros errores generales
        print(f"Ocurrió un error inesperado: {e}")