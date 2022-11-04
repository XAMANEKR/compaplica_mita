# Estudiantes y sus datos
#{10,40,50,80}
#{"hola","mundo"}
import os; os.system('clear')
grupo = [
{'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
{'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]

print(f'Grupo original {grupo}')
n = int(input("Cuantos estudiantes deseas procesar ?"))

for i in range(n):
    print(f'\nEstudiante {i+1}')
    datos = {}
    datos['nombre'] = input('Nombre ? ')
    datos['edad'] = int(input('Edad? '))
    datos['carrera'] = input('Carrera ? ')
    datos['promedio'] = float(input('Promedio? '))

    grupo.append(datos)

print(f'Grupo final: \n {len(grupo)}-{grupo}\n\n')

for e in grupo:

    for dato,valor in e.items():
        print(f'{dato:<10} : {valor}')
    print('')