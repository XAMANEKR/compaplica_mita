#calcular la hipotenusa de un triangulo

import math
print("calculando la hipotenusa del triangulo")
print("dame la longitud de lado 1 y lado 2 separada por enter")
long1,long2 =float(input()),float(input())
hipotenusa = math.sqrt(long1*long1+long2*long2)

print(f"la hipotenusa es{hipotenusa}")

