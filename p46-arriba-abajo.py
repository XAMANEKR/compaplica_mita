#imprimir numeros desde 1 a n o de n a 1 segun elija 


while(True):

    print("imprimir numeros desde 1 a n o de n a 1 segun elija ") 
    print("[1] numeros de 1 a n")
    print("[2]numeros de n a 100")

    op= int(input(f"/n elige una opcion"))
    n= int(input("limite n"))

    if op == 1:
        print(f"/n imprimiendo numeros de 1 hasta {n}")
        for x in range (1 , n+1, 1):
            print(x, end= " ")
    elif op == 2:
        print(f"/n imprimiendo numeros de {n} hasta 1")
        for x in range (1 , 0, -1):
            print(x, end= " ")   
    else:
        print("opcion incorrecta")  

    res = input("/n deseas continuar(s/n)").upper()
    if res == "N":
        break

print("gracias por usar nuestro servicio")