#imprime las tablas de multiplicar desde el 1 hasta la que el usuario pida

print("imprime las tablas de multiplicar desde el 1 hasta la que el usuario pida")

n = int(input("hasta que tabla quieres"))
m = int(input("hasta donde la quieres"))

for i in range (1 , n+1):
    for j in range(1, m+1):
        print(f"{i}x{j}= {i*j}")
    print("")