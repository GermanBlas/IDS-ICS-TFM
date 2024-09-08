#!/bin/bash

# Recorre todos los archivos .pcapng en el directorio actual
for PCAPNG in *.pcapng; do
    # Verificar que el archivo es un archivo regular
    if [ -f "$PCAPNG" ]; then
        echo "Procesando $PCAPNG..."

        # Calcular el número de la primera línea a partir de la cual leer el log
        PRIMERA_LINEA=$(($(wc -l /var/log/remote/ait29.us.es | cut -d" " -f1)+1))
        echo "Primera línea a partir de la cual leer el log: $PRIMERA_LINEA"

        # Mostrar el nombre del archivo .pcapng antes de ejecutar tcpreplay-edit
        echo "Ejecutando tcpreplay-edit con $PCAPNG..."
        
        # Ejecutar tcpreplay-edit con el archivo .pcapng y la interfaz vnet6
        sudo tcpreplay-edit -i vnet6 -d 1 -m 65520 --mtu-trunc --mbps 10 "$PCAPNG"

        # Esperar 60 segundos
        sleep 30

        # Filtrar el archivo de log buscando la cadena 'srcintf="port7"'
        tail -n +${PRIMERA_LINEA} /var/log/remote/ait29.us.es | grep 'srcintf="port7"' > ./"$PCAPNG".log

        echo "Filtrado del log completo para $PCAPNG guardado en ./${PCAPNG}.log"
    else
        echo "No se encontró ningún archivo .pcapng en el directorio actual."
    fi
done
