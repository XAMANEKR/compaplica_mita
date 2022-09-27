n = int(input("hasta donde"))
#pares
s = 0
print("\n numeros pares:")
for x in range(2,n+2,2):
        print(x, end="")
        s = s + x
print(f"\nSuma : {s}")