# Nombres y edades
import os; os.system('cls')

dat = {}

print('Introduce nombres y edades (nmbre vacio para terminar)')

while True:
    nombre = input('Dame el nombre ? ')
    if nombre!='':
        dat[nombre]=int(input('Edad ? '))

    else:

        break
print(f'El diccionario de datos creado: \n{len(dat)} - {dat}\n')
print('\nListado y promedio de edades:')

s=0

for n,e in dat.items():
    print(f'{n:<20} - {e:2}')
    s+=e
print(f'\n\nSuma: {s} y promedio: {s/len(dat)}')