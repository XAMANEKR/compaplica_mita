# generar numeros de 1 a 200 y sumarlos hasta dar 100

c=1
suma=0
while c <=200:
    suma += c
    if suma ==100:
        print("suma =",suma)
        print(f"use{c}numeros")
    c += 1