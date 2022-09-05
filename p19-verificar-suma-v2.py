#verificar suma v2

print("verificar si la suma de dos numeros es igual a un tercero")
print("dame 3 numeros enteros separados por un espacio:")

n1, n2, n3, = input().split()
n1, n2, n3, = [int(n1), int(n2), int(n3)]

if n1 + n2 == n3 :
    print(f"{n1} + {n2} = {n3}")
elif n1 + n3 == n2 :
    print (F"{n1} + {n3} = {n2}")
elif n2 + n3 == n1 :
    print (F"{n2} + {n3} = {n1}")
elif n2 == n3 == n1:    
    print (F"{n1} = {n3} = {n2}")
else :
    print("ninguna combinacion de numeros funciona")

