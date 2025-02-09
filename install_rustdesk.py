import os
import requests
import subprocess
import sys

def download_file(url, destination):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Archivo descargado: {destination}")
    else:
        print(f"Error al descargar el archivo: {response.status_code}")
        sys.exit(1)

def install_rustdesk():
    # URL del instalador de RustDesk
    # rustdesk_url = "https://github.com/rustdesk/rustdesk/releases/download/1.1.9/rustdesk-1.1.9.exe"
    rustdesk_url = "https://github.com/rustdesk/rustdesk/releases/download/1.3.7/rustdesk-1.3.7-x86_64.exe"
    
    # Ruta donde se guardará el instalador
    installer_path = os.path.join(os.getenv('TEMP'), 'rustdesk-installer.exe')
    
    # Descargar el instalador
    print("Descargando RustDesk...")
    download_file(rustdesk_url, installer_path)
    
    # Ejecutar el instalador
    print("Instalando RustDesk...")
    subprocess.run([installer_path, '/S'], check=True)
    
    # Limpiar el instalador descargado
    os.remove(installer_path)
    print("Instalación completada y archivo de instalación eliminado.")

if __name__ == "__main__":
    install_rustdesk()