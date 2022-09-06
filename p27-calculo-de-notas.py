#calculo de notas 

print ("calcula el promedio")

c1, c2, c3, c4, c5, = float(input()), float(input()), float(input()), float(input()), float(input())

suma = c1 + c2 + c3 + c4 + c5  
prom = (suma / 5 )

print (f"el promedio es {prom}")
if prom >= 0 and prom <= 6 :
    print("reprobado")

if prom >=6.1 and prom <= 7 :
    print("panzaso")

if prom >= 7.1 and prom <= 8 :
    print("Muy bien pero puedes mejorar")

if prom >=8.1 and prom <= 9:
    print("exelente sigue asi ")

if prom >= 9.1 and prom <= 10:
    print("exelente sigue asi ")
