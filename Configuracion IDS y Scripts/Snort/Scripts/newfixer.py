import os
import re
from scapy.all import *

# Configuración de directorios
dir_pcaps = "/home/dit/TFM/pcaps/"
# Los archivos de salida se guardarán en el mismo directorio para este ejemplo.
# Cambia esta ruta si deseas que los archivos de salida se guarden en otro directorio.
dir_salida = dir_pcaps

#------------------------Get The Layer and Fix Checksum-------------------------------

def getLayer(p):
    for paktype in (IP, TCP, UDP, ICMP):
        try:
            p.getlayer(paktype).chksum = None
        except AttributeError:
            pass
    return p

#-----------------------Fix a single pcap file and write to output file----------------

def fixpcap(input_file, output_file):
    paks = rdpcap(input_file)
    fc = list(map(getLayer, paks))  # Convertimos map a lista
    wrpcap(output_file, fc)
    print(f"Processed: {input_file} -> {output_file}")

#-----------------------Generate the output file name---------------------------------

def generate_output_filename(pcap_file):
    # Buscamos el patrón nombre[numero].pcapng
    match = re.match(r"^(.*)\[(\d+)\]\.pcapng$", pcap_file)
    if match:
        base_name = match.group(1)
        number = match.group(2)
        # Formato del archivo de salida: nombre_fixed[numero].pcapng
        return f"{base_name}_fixed[{number}].pcapng"
    else:
        print(f"El archivo {pcap_file} no sigue el formato esperado. Saltando.")
        return None

#-----------------------Process all pcap files in directory------------------------

def process_all_pcaps_in_folder():
    with os.scandir(dir_pcaps) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('.pcapng'):
                input_file = entry.path
                output_file = os.path.join(dir_salida, generate_output_filename(entry.name))
                if output_file:
                    fixpcap(input_file, output_file)

#-----------------------Main logic----------------------------------------------------

# Ejecutamos directamente sin recibir argumentos, procesando todos los archivos .pcapng
process_all_pcaps_in_folder()



