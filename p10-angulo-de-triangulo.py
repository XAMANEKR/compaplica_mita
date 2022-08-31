#calcula el tercer angulo de un triangulo 

print("calculando el angulo faltante")
print("Escribe el anfulo 1 y el 2 separado por un enter")

angulo1,angulo2, = int(input()),int(input())

angulo3 = 180 - (angulo1+angulo2)

print(f"el angulo faltante es{angulo3}")
