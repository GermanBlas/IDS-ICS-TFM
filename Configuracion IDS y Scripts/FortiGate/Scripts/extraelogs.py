import csv
import re
import glob
import os

# Expresión regular para extraer campos en formato clave=valor
pattern = re.compile(r'(\w+)="([^"]*)"|(\w+)=([^\s]*)')

# Expresión regular para extraer el valor de 'repeated <numero> times' en el campo 'msg'
repeated_pattern = re.compile(r'repeated (\d+) times')

# Campos que quieres extraer para cada CSV
campos_a_extraer_all = [
    'date', 'time', 'devname', 'devid', 'srcip', 'dstip', 'severity', 'attack', 'msg',
    'attackid', 'app', 'appid', 'sessionid', 'repeated','app-ctrl', 'service', 'type', 
    'subtype', 'eventtype', 'url'
]

campos_a_extraer_ips = [
    'attackid', 'sessionid', 'repeated', 'severity', 'attack', 'service', 'srcip', 
    'dstip', 'subtype', 'eventtype', 'url'
]

campos_a_extraer_app_ctrl = [
    'appid', 'sessionid', 'repeated', 'app', 'app-ctrl', 'apprisk', 'service', 'srcip', 'dstip', 
    'subtype', 'eventtype', 'url', 'parameters', 'filename'
]

# Crear carpetas si no existen
csv_dir = 'csvs'
csv_dir_ips = 'csvs_ids'
csv_dir_app_ctrl = 'csvs_app-ctrl'
csv_dir_full = 'csvs_full'

for directory in [csv_dir, csv_dir_ips, csv_dir_app_ctrl, csv_dir_full]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Obtener la lista de todos los archivos .log en el directorio actual
log_files = glob.glob("*.log")

# Procesar cada archivo de log y guardar en archivos CSV separados en las carpetas correspondientes
for log_file in log_files:
    # Obtener el nombre base del archivo (sin extensión)
    base_filename = os.path.splitext(log_file)[0]

    # Crear los nombres para los archivos CSV
    csv_filename = os.path.join(csv_dir, f"{base_filename}.csv")
    csv_filename_ips = os.path.join(csv_dir_ips, f"{base_filename}_ips.csv")
    csv_filename_app_ctrl = os.path.join(csv_dir_app_ctrl, f"{base_filename}_app-ctrl.csv")
    csv_filename_full = os.path.join(csv_dir_full, f"{base_filename}_full.csv")

    # Abrir el archivo log y crear los archivos CSV correspondientes
    with open(log_file, 'r') as f, \
         open(csv_filename, 'w', newline='') as csvfile_all, \
         open(csv_filename_ips, 'w', newline='') as csvfile_ips, \
         open(csv_filename_app_ctrl, 'w', newline='') as csvfile_app_ctrl, \
         open(csv_filename_full, 'w', newline='') as csvfile_full:
        
        # Crear escritores para los cuatro archivos con los campos personalizados
        writer_all = csv.DictWriter(csvfile_all, fieldnames=campos_a_extraer_all)
        writer_ips = csv.DictWriter(csvfile_ips, fieldnames=campos_a_extraer_ips)
        writer_app_ctrl = csv.DictWriter(csvfile_app_ctrl, fieldnames=campos_a_extraer_app_ctrl)

        # Extraer todos los campos posibles del archivo log para el CSV completo
        all_fieldnames = set()

        # Primera pasada para detectar todos los campos y crear el CSV full
        for line in f:
            # Extraer campos del log usando la expresión regular
            fields = {}
            for match in pattern.finditer(line):
                if match.group(1):  # Para claves con valores entre comillas
                    fields[match.group(1)] = match.group(2)
                    all_fieldnames.add(match.group(1))  # Agregar el campo al conjunto
                else:  # Para claves sin comillas
                    fields[match.group(3)] = match.group(4)
                    all_fieldnames.add(match.group(3))  # Agregar el campo al conjunto

        # Crear el escritor para el CSV full con todos los campos detectados
        writer_full = csv.DictWriter(csvfile_full, fieldnames=list(all_fieldnames))
        writer_full.writeheader()

        # Regresar al inicio del archivo para procesar nuevamente
        f.seek(0)

        # Escribir las cabeceras en los tres archivos CSV personalizados
        writer_all.writeheader()
        writer_ips.writeheader()
        writer_app_ctrl.writeheader()

        # Procesar cada línea del log y escribir los valores en los CSV
        for line in f:
            # Extraer campos del log usando la expresión regular
            fields = {}
            for match in pattern.finditer(line):
                if match.group(1):  # Para claves con valores entre comillas
                    fields[match.group(1)] = match.group(2)
                else:  # Para claves sin comillas
                    fields[match.group(3)] = match.group(4)

            # Filtrar solo los campos que quieres guardar y escribir en cada CSV
            log_filtrado_all = {campo: fields.get(campo, '') for campo in campos_a_extraer_all}
            log_filtrado_ips = {campo: fields.get(campo, '') for campo in campos_a_extraer_ips}
            log_filtrado_app_ctrl = {campo: fields.get(campo, '') for campo in campos_a_extraer_app_ctrl}

            # Verificar el campo 'msg' para extraer el valor 'repeated <numero> times'
            msg = fields.get('msg', '')
            repeated_match = repeated_pattern.search(msg)
            if repeated_match:
                repeated_value = repeated_match.group(1)
                log_filtrado_all['repeated'] = repeated_value
                log_filtrado_ips['repeated'] = repeated_value
                log_filtrado_app_ctrl['repeated'] = repeated_value
            else:
                log_filtrado_all['repeated'] = ''
                log_filtrado_ips['repeated'] = ''
                log_filtrado_app_ctrl['repeated'] = ''

            # Escribir los datos filtrados en los archivos CSV personalizados
            writer_all.writerow(log_filtrado_all)
            writer_full.writerow(fields)  # Escribir todos los campos sin filtrar en el CSV full

            # Comprobar el valor del campo 'subtype' y escribir en los CSV específicos
            subtype = fields.get('subtype', '')
            if subtype == 'ips':
                writer_ips.writerow(log_filtrado_ips)
            elif subtype == 'app-ctrl':
                writer_app_ctrl.writerow(log_filtrado_app_ctrl)

    print(f"Archivos CSV generados: {csv_filename}, {csv_filename_ips}, {csv_filename_app_ctrl}, {csv_filename_full}")

print("Procesamiento completado.")
