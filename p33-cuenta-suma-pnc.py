#cuenta numeros , los suma, cuenta , negativos, posotivos, ceros

num = cuenta = suma = 0
cuenta_positivos = cuenta_negativos = cuenta_ceros = 0
print("cuenta numeros , los suma, cuenta: positivos, negativos, ceros")


while(True):
    num = int(input("numero"))
    if num != 999:
        cuenta += 1
        suma+=num
        if num > 0 :
            cuenta_positivos += 1
        elif num <0 :
            cuenta_negativos +=1
        elif num == 0 :
            cuenta_ceros +=1
        print(f"se introdujeron {cuenta} numeros")
        print("la suma de los numeros es", suma)
        print("positivos :", cuenta_positivos)
        print("negativos:", cuenta_negativos)
        print("ceros :", cuenta_ceros)
    else: 
        break
