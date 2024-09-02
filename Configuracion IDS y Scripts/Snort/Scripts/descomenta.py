import os
import sys

lines = []
modified_lines = []


if len(sys.argv) == 2: 
	with open(sys.argv[1]) as f:
		lines = f.readlines()
	for line in lines:
		if ("ET DELETED" not in line) and ("#alert" in line):
			modified_line = line[1:]
			modified_lines.append(modified_line)
		else:
			modified_lines.append(line)

else:
		print("Error en el numero de argumentos")


with open(sys.argv[1], "w") as f:
		f.writelines(modified_lines)
