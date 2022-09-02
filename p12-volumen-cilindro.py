#calcula el volumen de un cilindro
from math import pi


print("calcula el volumen de un cilindro ")

print("ingrese radio y altura separados por un enter")

radio,altura = float(input()),float(input())
vol = ( pi ( radio ** 2) * altura )

print(f"el volumen del cilindro es {vol}")