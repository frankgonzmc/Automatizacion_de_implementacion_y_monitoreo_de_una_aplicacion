import subprocess

def instalar_nginx():
    try:
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', '-y', 'nginx'], check=True)
        print("Nginx instalado correctamente.")
        return True
    except subprocess.CalledProcessError as e:
        print("Error instalando nginx:", e)
        return False
