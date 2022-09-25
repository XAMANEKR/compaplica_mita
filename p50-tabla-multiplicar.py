#imprime la tabla de multiplicar que el usuario pide, hasta donde pide

import os

while (True):
    os.system("clear")
    print("imprime la tabla de multiplicar que el usuario pide")

    t = int(input("que tabla quieres"))
    n= int (input("hasta donde"))

    for i in range (1, n+1):
        print (f'{t} x {i} = {t*i}')
    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        break
    print("Gracias por utilizar este programa")
