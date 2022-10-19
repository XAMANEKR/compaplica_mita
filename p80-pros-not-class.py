#procesar notas de clase hasta introducir 0

print("procesar n calificaciones introducidas por el usuario")
print("introduce calificaciones de 1...10, usa 0 para parar\n")


import os; os.system("cls")
n=0
num=[]
s=p=0

while n!="0":
    n=int(input("Numero > "))
    if n>0 and n<=100:
        num.append(n)
        s=s+n
    elif n == 0 :
        break

p = s / len(num)
menor=[]
mp=[]   
for num in num:
        if num>p:
            mp.append(num)
        elif num<p:
           menor.append(num)


print(f"Las notas ingresadas son : {len(num)} - {num}")
print(f"La suma es: {s}")
print(f"El promedio es: {p}")
print(f"El numero menor es  : {min(num)} - {menor}")
print(f"El numero mayor es  : {max(num)}") 