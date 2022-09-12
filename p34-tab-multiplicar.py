#imprime la tabla de multiplicar deseada del 1 al 10 

import os

while(True):
    os.System("clear") #borra pantalla
    print("imprime la tabla de multiplicar deseada del 1 al 10 ")

    t = int(input("que tabla quieres?"))
    n = int(input("hasta donde"))
c = 1

while (c<=n):

    print(f"{C} x{t} = {c*t}")
    
    c+=1
    res = input("deseas continuar {S/N}").upper()
    if res ==N:
        break
    print("\n gracias por usar el programa")

