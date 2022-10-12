#calcular nombre y edad hasta introducir "*"

import os;os.system('clear')

print('Nombres y edades\n')
print("Introduce los nombres y edades: * en nombre termina\n")

nombres=[]
edades=[]
#introducir datos
while True:
    nombre=input("Nombre: ")

    if nombre=="*":
        break
    else:
        nombres.append(nombre)
        edad=int(input("Edad: "))
        edades.append(edad)

#imprimir nom y edad
print("\n")
print(f"nombres: {len(nombres)- (nombres)}\n")
print(f"nombres: {len(edades)- (edades)}\n")

#rrecorre areglo para may edadd
print("\nAlumnos mayores de edad:\n")
for i in range(len(nombres)):
    if edades[i]>=18:
        print(f"Nombre: {nombres[i]} , Edad: {edades[i]}")

#alumno max edad
mayor= max(edades)
pos=edades.index(max(edades))
print(f"Alumno de mayor edad: {nombres[pos]}, {edades[pos]}")