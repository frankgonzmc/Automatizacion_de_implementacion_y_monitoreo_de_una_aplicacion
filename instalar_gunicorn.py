import subprocess

def install_gunicorn():
    comando = ['./venv/bin/python3', '-m', 'pip', 'install', 'gunicorn']
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("Instalacion de gunicorn.")
        print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el script:", e.stderr)
        return False