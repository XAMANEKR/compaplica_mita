#imprimir la suma y los promedios de los numeros ingresados por el usuario

print("imprimir la suma y los promedios de los numeros ingresados por el usuario")

c= int(input("cuantos numeros deseas?"))

s = 0

for x in range (1, c+1 1):
    n=int(input(f"numero{x}"))
    s = s + n

int (f"\n la suma es {s}")
print(f"\n el promedio es :{s/c}")
