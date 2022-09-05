# aceptar estudiante en base a algunos estandares
print('Universidad Patito SA de CV')

nombre = input('ingresa tu nombre > ')

edad = int(input('ingresa tu edad > '))

if edad>=18 :
    print('dame 2 calificaciones > ')
    c1, c2 = int(input()), int(input())
    if c1<8 or c2<8 :
        print(f'{nombre} bienvenid@ a la Universidad, tu edad {edad} y calificaciones {c1} y {c2} lo permiten') 
    else :
     print('solo aceptamos alumnos con calificaciones superiores a 8')

else:
    print("no aceptamos menores")