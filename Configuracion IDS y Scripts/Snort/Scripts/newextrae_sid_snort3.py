#!/usr/bin/env python3
import os
import sys

# Este script analizará con snort todos los pcaps de un directorio,
# y extraerá los sids resultantes. Está pensado para ser usado con Snort 3

# Definimos los directorios
dir_pcaps = "/home/dit/TFM/pcaps/"

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)  # Crear la carpeta sin permisos específicos
        os.chmod(directory, 0o777)  # Forzar permisos 777

# Recorrer los modos del 4 al 5
for modo in range(4, 6):
    dir_analisis_snort = f"/home/dit/TFM/analisis_snort{modo}/"
    dir_sids = f"/home/dit/TFM/sids{modo}/"
    comando_snort = f"snort -k none -q -c /usr/local/snort/etc/snort/snort{modo}a.lua -A full -r"

    # Crear directorios si no existen
    create_directory_if_not_exists(dir_analisis_snort)
    create_directory_if_not_exists(dir_sids)

    lines = []

    with os.scandir(dir_pcaps) as pcaps:
        for pcap in pcaps:
            # Solo procesar archivos .pcapng
            if pcap.is_file() and pcap.name.endswith('.pcapng'):
                # Iniciamos las alertas totales (con la variable cont contaremos todas las alertas
                # , incluso las repetidas)
                cont = 0
                alerts = []
                str_alertas = ""

                if len(sys.argv) == 1:
                    print(f"Procesando pcapng: {pcap.name}")
                    attack = pcap.name.split(".p")[0]
                    os.system(f"{comando_snort} {dir_pcaps}{pcap.name} > {dir_analisis_snort}{attack}.txt")
                    print(f"Snort ha analizado {pcap.name}")

                    with open(f"{dir_analisis_snort}{attack}.txt") as f:
                        lines = f.readlines()
                        for line in lines:
                            if "[**]" in line:
                                var = line.split(":")[1]
                                cont += 1
                                if var not in alerts:
                                    alerts.append(var)
                                    
                        for i in alerts:
                            if i != alerts[-1]:
                                str_alertas += (i + ",")
                            else:
                                str_alertas += i

                        str_alertas += f". Hay {len(alerts)} alertas no repetidas y un total de {cont}."
                        print(str_alertas)

                        os.system(f"echo {str_alertas} > {dir_sids}{attack}.txt")

                else:
                    print("Error en el número de argumentos")


