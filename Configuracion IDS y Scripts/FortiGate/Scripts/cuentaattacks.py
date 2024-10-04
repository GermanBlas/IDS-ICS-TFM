import csv
import glob
import os
from collections import Counter

# Función para contar las ocurrencias de los campos 'attack' y 'repeated', y calcular el total
def contar_ocurrencias_attack_repeated_en_archivo(csv_filename):
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # Crear listas con tuplas (attack, repeated)
        attacks_repeated = [(row['attack'], row['repeated']) for row in reader if 'attack' in row and 'repeated' in row and row['attack']]

    # Contar las ocurrencias de cada combinación (attack, repeated)
    conteo_attacks_repeated = Counter(attacks_repeated)

    total_suma = 0

    # Mostrar las ocurrencias en pantalla y calcular el total
    print(f"\nArchivo: {csv_filename}")
    print("Conteo de 'attack' con 'repeated':")
    for (attack, repeated), count in conteo_attacks_repeated.items():
        repeated_value = int(repeated) if repeated else 1  # Si 'repeated' está vacío, considerarlo como 1 por defecto
        total_parcial = repeated_value * count  # Multiplicar repeated por el número de ocurrencias
        total_suma += total_parcial  # Sumar al total
        print(f"'Attack': {attack}, 'Repeated': {repeated_value} veces => {count} ocurrencias (Total parcial: {total_parcial})")

    print(f"Total para el archivo {csv_filename}: {total_suma}")
    return total_suma


# Función para analizar todos los archivos CSV en la carpeta del script en orden alfabético
def contar_ocurrencias_attack_repeated_en_carpeta_actual():
    # Obtener la carpeta donde se encuentra el script
    carpeta_actual = os.getcwd()

    # Obtener la lista de todos los archivos .csv en la carpeta
    archivos_csv = glob.glob(os.path.join(carpeta_actual, "*.csv"))

    # Ordenar los archivos en orden alfabético
    archivos_csv.sort()

    suma_total = 0

    # Procesar cada archivo CSV y contar ocurrencias de 'attack' y 'repeated', acumulando el total
    for csv_filename in archivos_csv:
        suma_total += contar_ocurrencias_attack_repeated_en_archivo(csv_filename)

    # Mostrar la suma total de todos los archivos
    print(f"\nSuma total de todos los archivos CSV: {suma_total}")

# Llamar a la función para contar las ocurrencias y calcular el total en todos los archivos CSV en la carpeta actual
contar_ocurrencias_attack_repeated_en_carpeta_actual()

