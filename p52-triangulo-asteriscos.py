#impirme triangulo de asteriscos
print("impirme triangulo de asteriscos")
r = int(input("cuantos renglones"))

for i in range(1, r+1):
    for j in range(1, r+1):
        print("*", end= " ")
    print()