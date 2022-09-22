
num = cuenta = suma = 0
cuenta_positivos = cuenta_negativos = cuenta_ceros = 0
print("cuenta numeros , los suma, cuenta: positivos, negativos, ceros")



while(True):
    print("ingresa las temperaturas separadas por un enter")
    T1,t2 = int(input("temperatura inicial en grados centigrados")), int (input("temperatura final en grados centigrados"))
    
    while T1 < t2:
        if T1 <=t2 :
            far = (T1 * 9 / 5) +32
            print(f"la temperatura en grados centigrados es{far} ")
            T1 += 1 
    res = input("deseas continuar {S/N}").upper()
    if res == "N":
        break