#divicion de cifras 
import math

print("dividir un numero entero de 3 cifras en centenas decenas unidades")
num = int(input("dame un numero entero de 3 cifras"))


centenas = math.trunc ( num / 100 )
decenas = math.trunc ( centenas * 100 / 10 )
unidades = num - (centenas * 100 + decenas * 10)

print(f"centenas {centenas}, decenas {decenas} unidades {unidades}")