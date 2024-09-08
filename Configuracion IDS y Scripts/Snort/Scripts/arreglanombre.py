import os

def renombrar_archivos(directorio):
    # Recorremos el directorio y sus subdirectorios
    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            # Comprobamos si el archivo contiene '.pcapng' pero no termina con '.pcapng'
            if '.pcapng' in archivo and not archivo.endswith('.pcapng'):
                ruta_antigua = os.path.join(carpeta_raiz, archivo)
                nuevo_nombre = archivo.replace('.pcapng', '')
                ruta_nueva = os.path.join(carpeta_raiz, nuevo_nombre)
                print(f"Renombrando archivo: {ruta_antigua} -> {ruta_nueva}")
                os.rename(ruta_antigua, ruta_nueva)

if __name__ == "__main__":
    # Directorio actual
    directorio_actual = os.getcwd()
    renombrar_archivos(directorio_actual)
    print("Proceso completado.")

