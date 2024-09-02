import os
import sys

# Este script analizara con snort todos los pcaps de un directorio,
# y extraera los sids resultantes. Esta preparado para trabajar con Snort 2.

# Definimos los directorios
modo = "3"
dir_pcaps = "/home/dit/TFM/pcaps/"
dir_analisis_snort = "/home/dit/TFM/analisis_snort"+ modo +"/"
dir_sids = "/home/dit/TFM/sids"+ modo +"/"
archivo_snort = "snort"+ modo +".conf"
comando_snort = "snort -q -A console -c /etc/snort/" + archivo_snort + " -r"


lines = []


with os.scandir(dir_pcaps) as pcaps:

	for pcap in pcaps:

		# Iniciamos las alertas totales (con la variable cont contaremos todas las alertas
		# , incluso las repetidas)
		cont = 0
		alerts = []
		str_alertas = ""

		if len(sys.argv) == 1: 

			print("Procesando pcap: " + pcap.name)
			attack = pcap.name.split(".p")[0]
			os.system(comando_snort + " " + dir_pcaps + pcap.name + " > " + dir_analisis_snort + attack + ".txt")
			print("Snort ha analizado " + pcap.name)

			with open(dir_analisis_snort + attack + ".txt") as f:
				lines = f.readlines()
				for line in lines:
					if "[**]" in line:
						var = line.split(":")[3]
						cont += 1
						if var not in alerts:
							alerts.append(var)
							
				for i in alerts:
					#os.system('touch sids/' + sys.argv[1]) 
					if i != alerts[len(alerts)-1]:
						str_alertas += (i+",")
					else:
						str_alertas += i

				str_alertas += ". Hay " + str(len(alerts)) + " alertas no repetidas y un total de " + str(cont) + "."
				print(str_alertas)

				os.system("echo " + str_alertas + " > " + dir_sids + attack + ".txt")

		else:
			print("Error en el numero de argumentos")