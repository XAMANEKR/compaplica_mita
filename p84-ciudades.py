#Leer n nombres de ciudades en una lista hasta introducir $
# Imprimir cuantos elementos son, y la lista completa
# Ordenar la lista en orden descendente y mostrar (sort)
# Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

import os;os.system("cls")

noms=[]
nombre=" "

print("Introducir nombres de las ciudades (finaliza con $)")

while True:
    nombre=input()
    if nombre!="$":
        
        noms.append(nombre)
    else:
        
        break
print(f"Son {len(noms)} ciudades - {noms}")
noms.sort(reverse=True)
print(f"La lista ordenada de forma descendente: {noms}")
ciudades=[]

for c in noms:
    if not c[0] in "AEIOUaeiou":

        ciudades.append(c)

print(f"Las ciudades que inician con consonante son {len(ciudades)} - {ciudades}")