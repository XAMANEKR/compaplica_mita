#calcula el area de un circulo 
import math


print("calculando el area de un circulo ...")

radio = float(input("inseta valor del radio"))
# area = 3.1416*radio+radio
area = math.pi * radio ** 2
print(f"el circulo del radio {radio} tiene un area de {area}")