# Imprimir pares impares 2 o 1 hasta n y su suma


n = int(input("hasta donde"))
#pares
s = 0
print("\n numeros pares:")
for x in range(2,n+2,2):
        print(x, end="")
        s = s + x
print(f"\nSuma : {s}")

# impares
s = 0
print("\n numeros impares:")
for x in range(1,n+1,2):
        print(x, end="")
        s = s + x 
print(f"\n suma : {s}")