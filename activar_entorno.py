import subprocess

def activar_entorno_virtual_instalar_dependencias():
    comando = ['./venv/bin/python3', '-m', 'pip', 'install', '-r', 'requirements.txt']
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("Script ejecutado en entorno virtual.")
        print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el script:", e.stderr)
        return False