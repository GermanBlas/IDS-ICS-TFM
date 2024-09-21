import csv
import glob
import os
from collections import Counter

# Función para contar las ocurrencias de valores en el campo 'app'
def contar_ocurrencias_app_en_archivo(csv_filename):
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # Crear una lista con todos los valores del campo 'app'
        apps = [row['app'] for row in reader if 'app' in row and row['app']]

    # Contar las ocurrencias de cada valor del campo 'app'
    conteo_apps = Counter(apps)

    # Mostrar las ocurrencias en pantalla
    print(f"\nArchivo: {csv_filename}")
    for app, count in conteo_apps.items():
        print(f"{app}: {count} veces")


# Función para analizar todos los archivos CSV en la carpeta del script en orden alfabético
def contar_ocurrencias_app_en_carpeta_actual():
    # Obtener la carpeta donde se encuentra el script
    carpeta_actual = os.getcwd()

    # Obtener la lista de todos los archivos .csv en la carpeta
    archivos_csv = glob.glob(os.path.join(carpeta_actual, "*.csv"))

    # Ordenar los archivos en orden alfabético
    archivos_csv.sort()

    # Procesar cada archivo CSV y contar ocurrencias del campo 'app'
    for csv_filename in archivos_csv:
        contar_ocurrencias_app_en_archivo(csv_filename)

# Llamar a la función para contar las ocurrencias en todos los archivos CSV en la carpeta actual
contar_ocurrencias_app_en_carpeta_actual()

