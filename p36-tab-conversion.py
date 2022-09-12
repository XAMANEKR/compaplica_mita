#tabla para convertir peso a dolar


while (True):
    tc = 19.91
    print("tabla de conversion de peso a dolar")

    pi = float(input("valor inicial: }"))
    pf =float(input("valor pesos final :"))
    c= pi
    c = print("-"*15)
    print("peso/dolar")
    print("-"*15)

    while( c <= pf ) :
        print(f"{c}\t{c / tc :.4f}")

        c+=1

        print("-"*15)
        resp = input("deseas continuar{S/N}").upper
        if resp == "N":
            break