# calcular la ssuma y el promedio de tres calificaciones 

print("calcular la ssuma y el promedio de tres calificaciones\n")
#c1 = int(input("calificacion 1"))
#c2 = int(input("calificacion 2"))
#c3 = int(input("calificacion 3"))

print("dame las 3 calificaciones separadas por un espacio")
c1,c2,c3 = input().split()
c1,c2,c3 =[int(c1),int(c2),int(c3)]
suma = c1 + c2 + c3
prom = suma / 3
print(f"los numeros fueron{c1},{c2},{c3}")
print(f"la suma {suma}")
print(f"el promedio {prom}")
