#Generar 2 listas de 10 números aleatorios
# Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
# Imprime las 3 lista

import random;
import os;os.system("cls")

lista1=[]
lista2=[]
lista3=[]

print("Lista de numeros aleatorios.... ")
for i in range(10):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))

print("\nListas de números originales")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

for n in range(10):
    lista1[n]=pow(lista1[n],2)
    lista2[n]=pow(lista2[n],2)
    if (lista1[n]%2!=0) and (lista2[n]%2!=0):
        lista3.append(lista1[n]+lista2[n])

print("\nListas de números")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista de numeros sumados: {lista3}")