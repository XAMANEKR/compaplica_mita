# sumar 2 listas de n numeros en una tercer lista

import os;os.system("clear")

print(" sumar 2 listas de n numeros en una tercer lista")

c = int(input("cuantos elementos?"))

#leer lista
lista1=[]
print("\n leyendo elementos de la lista 1")

for i in range(c):
    n=int(input(f"numero{1}?"))
    lista1.append(n)
print(f"lista 1 : {len (lista1)} {lista1}")

#leer lista 2
lista2=[]
print("\n leyendo elementos de la lista 2")
for i in range (c):
    n = int(input(f"numero{i}?"))
    lista2.append(n)
print(f"lista 2 : {len (lista2)} {lista2}")

print("\nCalculando e imprimiendo la suma de las listas")
lista3=[]
for i in range(c):
    lista3.append(lista1[i]+lista2[i])
print(f"\nLista3 : {lista3}")