# Llenar un lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
# Calcular e imprimir la suma y promedio de los números
# Mostrar los números que son divisibles entre 3 y sumarlos
# Pedir un elemento a buscar en la lista original y decir si esta y en que posición

impares=[]
suma=0
prom=0
n=int(input("Insertar valor de n: "))

for i in range(1,n+1,2):
    impares.append(i)
    suma+=i
print(f"Los impares son: {impares}")
promedio=suma/len(impares)

print(f"La suma es: {suma},  el promedio es: {prom:.2f}")

div=[]
sumaDiv=0
for i in impares:
    if i%3==0:
        div.append(i)
        sumaDiv+=i
        
print(f"Los  divisibles entre 3 son : {div} la suma da: {sumaDiv}")

busqueda=int(input("Insertar el numero que busca: "))

if busqueda in impares:
    pos=impares.index(busqueda)
    print(f"Se encontro!!, en la posición : {pos}")
else:
    print("No se encontro")