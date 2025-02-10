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

def install_zip():
    # URL del instalador de RustDesk
    zip_url = "https://www.7-zip.org/a/7z2409-x64.exe"
    
    # Ruta donde se guardará el instalador
    installer_path = os.path.join(os.getenv('TEMP'), 'sevenzip.exe')
    
    # Descargar el instalador
    print("Descargando 7zip...")
    download_file(zip_url, installer_path)
    
    # Ejecutar el instalador
    print("Instalando 7zip...")
    subprocess.run([installer_path, '/S'], check=True)
    
    # Limpiar el instalador descargado
    os.remove(installer_path)
    print("Instalación completada y archivo de instalación eliminado.")
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    install_zip()