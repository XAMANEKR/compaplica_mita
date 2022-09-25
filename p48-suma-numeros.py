#imprimir la suma y los promedios de los numeros ingresados por el usuario

print("imprime la suma y el promedio de n numeros introducidos")

c = int(input("cuantos numeros deseas"))
s= 0

for x in range(1, c+1, 1 ):
    n= int (input(f"numero{x}"))
    s = s + n

print(f"\n la suma es {s}")
print(f"\n el promedio es {s/c}")
    
