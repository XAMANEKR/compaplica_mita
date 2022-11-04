# Nombres y edades
import os; os.system('cls')

dat = {}

print('Introduce nombres y edades (nmbre vacio para terminar)')

datos= {}
while True:
    nombre = input('Dame el nombre ? ')
    if nombre!='':
        edad= int(input("dame la edad"))
        datos[nombre] = edad
    else:

        break
s=p=0

print(f'los dats son \n {len(dat)} - {dat}\n')

for n,e in dat.items():
    print(f'{n:<20} - {e:2}')
    s= s + e
print(f'\n\nSuma: {s} y promedio: {s/len(dat)}')