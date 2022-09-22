
num = cuenta = suma = prom =0

print("cuenta numeros , los suma, cuenta: positivos, negativos, ceros")


while(True):
    num = int(input("numero"))
    if num != 0:
        cuenta += 1
        suma+=num
        prom = suma / cuenta 
        print ({cuenta})
        print({prom})
        print({suma})

    else: 
        break

        
