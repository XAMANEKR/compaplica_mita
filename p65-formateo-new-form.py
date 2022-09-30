# formateo de datos ejemplo 2

import os; os.system('clear')

noms = 'Juan Carlos Pedro Luis Jose Maria Julian Teresa Francisco Leticia Rafael'

nombres = noms.split()

edad = 25

sueldo = 15345.1234

tasa = 0.40

print('Salida datos con f: \n')

print(f'Nombre: {nombres[5]}, Edad: {edad}, Sueldo: {sueldo:.2f} Tasa: {tasa:.2%} \n')
print(f'Los nombres: \n\n{nombres}\n')

print(f"{'Tabla de datos':-^43}")

print(f"{'Nombre':<10}{'Edad':^10}{'Sueldo':>15}")
print('-'*47)


for i in range(len(nombres)):
    print(f'{nombres[i]:<15}{edad+i:^15}{sueldo*i:>15,.2f}')
    print('-'*47)
print(f'{"final" :-^47}')
