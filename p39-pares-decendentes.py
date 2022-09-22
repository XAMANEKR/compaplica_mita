while True:
    print("ingrese el numero inicial")
    c = int(input())
    f = 0
    suma = 0
    print("los numeros pares son")

    while c >= f:
        
        if c % 2 == 0:
            print (c)
            suma = suma +c
        c-=1
        print(f"la suma es{suma}")
    res = input("deseas continuar {S/N}").upper()
    if res =="N":
        break
   

 