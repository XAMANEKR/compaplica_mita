#clasificar angulo debido a los grados

print("Mostrar el tipo de angulo en base a los grados")

angulo = int (input("dame un angulo entre (0..360)"))

if angulo >= 0 and angulo <=360:
    if angulo < 90:
        print("angulo agudo")
    elif angulo == 90:
        print("angulo obtuso")
    elif angulo > 90:
        print("angulo recto")
    elif angulo == 180:
        print("angulo lleno")
    elif angulo > 180:
        print("angulo concavo")
    
else:
    print(f"el anfulo{angulo} esta fuera de rango")