El script convertir_pcap_a_pcapng_y_truncar_MTU.sh cambia la extensión de los archivos PCAP del directorio a PCAPNG y trunca los paquetes necesarios para que cumplan con la MTU.

El script convertir_pcapng_a_pcapng_y_truncar_MTU.sh trunca los paquetes necesarios para que cumplan con la MTU.

El script script_deteccion_falta_SYN.py usa tres scripts (detector_syn.sh, txt_to_csv.py y checkSYN.py) para devolver un Excel que muestra los flujos truncados de los PCAPNG del directorio usado

El script detector_syn.sh analiza los PCAPNG para extraer los datos de los distintos flujos. 

El script txt_to_csv.py convierte los txt generados anteriormente y los pasa a formato cvs.

El script checkSYN.py usa los cvs y comprueba cada uno de los flujos para ver si están truncados y guarda la información de los flujos truncados al Excel RESULTADOS_EXCEL.xlsx.

El script descomenta.py extrae las reglas, que no contienen ET DELETED, del conjunto de reglas ET Open.

El script newextrae_sid_snort2.py analizara con Snort todos los PCAPNGs de un directorio,y extrae los sids resultantes. Está preparado para trabajar con Snort 2.

El script newextrae_sid_snort3.py analizara con Snort todos los PCAPNGs de un directorio,y extrae los sids resultantes. Está preparado para trabajar con Snort 3.

El script une_sids.py analiza dos directorios diferentes y por cada par de archivos del mismo nombre generará un fichero que contenga los SIDs de ambos, eliminando las repeticiones.

El script newfixer.py regenera los checksum de los PCAPNGs.
