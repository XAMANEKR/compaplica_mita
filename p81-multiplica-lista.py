#lee listas multiplicalas y guardalas en una nueva
import os;os.system("cls")

print("lee listas multiplica y guarda en una nueva ")

l1=[]
for i in range(5) :
    print("lista 1")
    n=int(input("numero: "))
    l1.append(n)
    print("lista 2")
l2=[]
for i in range(5):
    n=int(input('Numero: '))
    l2.append(n)
l3=[]
for i in range(5):
    l3.append(l1[i] * l2[i])

print(f"\nlista 1 : {l1}")
print(f"\nlista 2 : {l2}")
print(f"Lista 3 (resultado de la multiplicacion de lista1xlista2 ): {l3}")