#convierte temperatura de farnheit a centigrados y viseversa

print("convertir temperatura ")
print("|C|convertir a centigrados")
print("|F| convertir a farenheit \n")
opcion = str.upper(input ("elige"))

if opcion == "C":
    print("elegiste convertir a centigrados\n")
    temp = float(input("dame los grados farenheit"))
    res = (temp - 32) * 5 / 9
    print(f"{temp} grados farenheit equivale a {res} grados centigrados")


else:
    print("elegiste convertir a farenheit\n")
    temp = float(input("dame los grados centigrados"))
    res = (temp * 9 / 5 )+ 32  
    print(f"{temp} grados centigrados equivale a {res} grados farenheit")
