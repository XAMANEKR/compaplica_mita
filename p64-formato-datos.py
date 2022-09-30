#cadenas de formato
import os
os.system("clear")

ciudad1= "zacatecas"
ciudad2= "guadalupe"
ciudad3="fresnillo"

print("\n Sailida con argumentos por posicion")
print("\n Posicion numerada en orden: {0} {1} {2}".format(ciudad1,ciudad2,ciudad3))
print("\n posicion sin numero: {} {} {}".format(ciudad1,ciudad2,ciudad3))
print("\n posicion enumerada sin orden: {2} {1} {0}".format(ciudad1,ciudad2,ciudad3))
print("repetir posiciones: {2} {2} - {1} {1} - {0}".format(ciudad1,ciudad2,ciudad3))

print("\n argumentos por nombres: {x1} / {x2} / {x3}",format(x1=5,x2=125,x3="jerez"))

txt = "maestria en ingenieria y tecnologia aplicada"

print("\n alinear el texto y especificar longitud\n")
print('-{0:*^60}-'.format(txt))
print('-{0:<60}-'.format(txt))
print('-{0:>60}-'.format(txt))
print('-{0:^60}-'.format(txt))

num = 1235
print('\nmostrar numeros en distintas bases: \n')
print('Decimal    0....9 : {0:d}'.format(num))
print('Hexadecimal 0....9 ABCDEF : {0:x}'.format(num))
print('Octal : 0...8 {0:o}'.format(num))
print('Binario 0,1: {0:b}'.format(num))

num = 12345854684945.565516856789
desc = .20
print('\nFormateo de números: \n')
print("numero decimal : {15}".format(num))
print('Con dos decimales: {:.2f}'.format(num))
print('Relleno : {:15.2f}'.format(num))
print('Exponencial : {0:e}'.format(num))
print('en porcentaje: {0:.2%}'.format(desc))
print("separado por miles : {:,.2f}".format(num))
