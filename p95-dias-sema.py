# pide un numero da un dia
import os; os.system("cls")
grupo = {"1":"Lunes",
"2":"Martes",
"3":"Miercoles",
"4":"Jueves",
"5":"Viernes",
"6":"Sabado",
"7":"Domingo"}


num=input("Ingrese el número del dia (del 1 al 7): ")
print(f"El dia de la semana es: {grupo[num]}")



