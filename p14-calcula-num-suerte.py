#calcula numero de la suerte

import math

num = int(input("dame tu año de nacimiento"))

millares = math.trunc(num/1000)
centenas = math.trunc((num - (millares*1000)) / 100)
decenas = math.trunc((num - (millares*1000 + centenas*100)) / 10)
unidades = math.trunc(num -(millares * 1000 +centenas * 100 +decenas *10))

num_de_la_suerte = millares+ centenas + decenas + unidades

print(f"el numero de las suerte es {num_de_la_suerte}")

