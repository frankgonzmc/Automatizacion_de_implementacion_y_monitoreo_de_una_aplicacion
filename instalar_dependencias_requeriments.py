import subprocess

def instalar_dependencias():
    # Comando para instalar las dependencias desde el archivo requirements.txt
    comando = ['pip', 'install', '-r', 'requirements.txt']
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print(resultado.stdout)
        print("Dependencias instaladas con éxito."),
    except subprocess.CalledProcessError as e:
        # Este error ocurre si el comando pip falla (por ejemplo, si requirements.txt no existe o hay un problema de red)
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida estándar del error: {e.stdout}")
        print(f"Error estándar del comando: {e.stderr}")
    except FileNotFoundError:
        # Este error ocurre si pip no está instalado o no se encuentra en el sistema
        print("El comando pip no se encuentra en el sistema. Asegúrate de que Pip esté instalado.")
    except Exception as e:
        # Para otros errores generales
        print(f"Ocurrió un error inesperado: {e}")