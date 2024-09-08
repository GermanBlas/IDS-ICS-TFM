import os
import sys
import stat

# Definimos los directorios base
base_dir = "/home/dit/TFM/"
dir_pcaps = os.path.join(base_dir, "pcaps/")

# Función para crear directorios con permisos 777
def crear_directorio(directorio):
    os.makedirs(directorio, exist_ok=True)
    os.chmod(directorio, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # Permisos 777

# Iteramos sobre los valores de modo del 1 al 3
for modo in range(1, 4):
    modo_str = str(modo)

    # Definimos los directorios específicos para cada modo
    dir_analisis_snort = os.path.join(base_dir, "analisis_snort" + modo_str + "/")
    dir_sids = os.path.join(base_dir, "sids" + modo_str + "/")
    archivo_snort = "snort" + modo_str + ".conf"
    comando_snort = f"snort -q -k none -A console -c /etc/snort/{archivo_snort} -r"

    # Creamos los directorios con permisos 777
    crear_directorio(dir_analisis_snort)
    crear_directorio(dir_sids)

    lines = []

    with os.scandir(dir_pcaps) as pcaps:
        for pcap in pcaps:
            if pcap.is_file() and pcap.name.endswith('.pcapng'):
                # Iniciamos las alertas totales (con la variable cont contaremos todas las alertas, incluso las repetidas)
                cont = 0
                alerts = []
                str_alertas = ""

                if len(sys.argv) == 1:
                    print(f"Procesando pcapng: {pcap.name}")

                    attack = pcap.name.split(".")[0]  # Modificado para coincidir con la extensión .pcapng
                    os.system(f"{comando_snort} {dir_pcaps}{pcap.name} > {dir_analisis_snort}{attack}.txt")

                    print(f"Snort ha analizado {pcap.name}")

                    with open(f"{dir_analisis_snort}{attack}.txt") as f:
                        lines = f.readlines()

                        for line in lines:
                            if "[**]" in line:
                                var = line.split(":")[3]
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
                    print("Error en el numero de argumentos")

