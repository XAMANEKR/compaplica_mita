print(" imprimir la secuencia de números mostrados el numero de renglones que el usuario desee")

n = int(input("inserta numero"))

suma=""
s=0.

for i in range(1,n+1):
    for x in range(1,i+1):
        print('1',end="")
        suma += "1"
    s += int(suma)
    suma = ""
    if x!=n :
        print("+",end="")
print(f"\n La suma de terminos es : {s}")