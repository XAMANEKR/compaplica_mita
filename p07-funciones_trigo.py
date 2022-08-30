#uso de funciones trigoometricas
import math

print("uso de las funciones trigonometricasde python")
angulo =int(input("dame el angulo en rad"))

seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)

salida = ("resumen de funciones trigonometricas \n"
f"el seno es {seno} \n"
f"el coseno es {coseno} \n"
f"el tangente es {tangente} \n"
f"el angulo es {angulo} en radianes, equivale a {grados} grados \n"
)

print(salida)
