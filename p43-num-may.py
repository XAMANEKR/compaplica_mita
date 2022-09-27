total=int(input("escribe el total de num a calcular"))

while (True):
    x=1
    
    while x<= total:
        n=int(input("escribe un numero"))
        numero_mayor = n
        x=x+1
        if x == 1:
            numero_mayor=n
        elif n > numero_mayor:
            numero_mayor=n

    
    print(f"el numero mayor es:{numero_mayor}")