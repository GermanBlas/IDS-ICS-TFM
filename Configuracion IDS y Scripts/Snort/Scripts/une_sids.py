#!/bin/bash
import os
import sys

# Este script analizará dos directorios diferentes y por cada
# par de archivos del mismo nombre generará un fichero que contenga
# los SIDs de ambos, eliminando las repeticiones.

# Definimos los directorios
dir_1 = "./ETOpen_por_defecto/sids1/"
dir_2 = "./ETOpen_Optimizada/sids2/"
dir_3 = "./QuickDraw/sids3/"
dir_4 = "./Talos_Community/sids4/"
dir_5 = "./Talos_Registered/sids5/"

# Recorremos los valores del modo 2 al 4
for modo in range(2, 5):
    dir_des = "./RS" + str(modo) + "/"
    
    linesf1 = []
    linesf2 = []
    dir_ori1 = ""
    dir_ori2 = ""

    # Definimos los directorios según el modo
    match modo:
        case 2:
            dir_ori1 = dir_1
            dir_ori2 = dir_4
        case 3:
            dir_ori1 = dir_1
            dir_ori2 = dir_5
        case 4:
            dir_ori1 = dir_2
            dir_ori2 = dir_5
        case _:
            print("Modo no reconocido")

    with os.scandir(dir_ori1) as ficheros1:
        for aux in ficheros1:
            with open(aux, 'r') as f1:
                union = []
                linesf1 = f1.readlines()
                alertsf1 = linesf1[0].split(".")[0].split(",")
                total1 = linesf1[0].split(".")[1].split(" ")[10]
                for alertf1 in alertsf1:
                    if alertf1 != "":
                        union.append(alertf1)
                with os.scandir(dir_ori2) as ficheros2:
                    for aux2 in ficheros2:
                        with open(aux2, 'r') as f2:
                            if os.path.basename(f2.name) == os.path.basename(f1.name):
                                linesf2 = f2.readlines()
                                alertsf2 = linesf2[0].split(".")[0].split(",")
                                total2 = linesf2[0].split(".")[1].split(" ")[10]
                                for alertf2 in alertsf2:
                                    igual = False
                                    for alertu in union:
                                        if alertu == alertf2:
                                            igual = True
                                            break
                                    if not igual:
                                        if alertf2 != "":
                                            union.append(alertf2)
                                str_alertas = ""
                                for i in union:
                                    if i != union[len(union) - 1]:
                                        str_alertas += (i + ",")
                                    else:
                                        str_alertas += i

                                suma_total = int(total1) + int(total2)

                                str_alertas += ". Hay " + str(len(union)) + " alertas no repetidas y un total de " + str(suma_total) + "."

                                print(str_alertas)
                                os.system("echo " + str_alertas + " > " + dir_des + os.path.basename(f1.name))

