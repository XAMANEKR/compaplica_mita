#verifica si los numeros son consecutivos

print("verifica si los numero son consecutivos ")

print("ingresa tres numeros diferentes separados por enter")
num1,num2,num3, = int(input()), int(input()), int(input())

if num1 != num2 and num2 != num3 :
    print("...")
    if num1 +1 == num2 :
        print("num 2 es consecutivo a num1")
    if num2 +1 == num3:
        print("num3 es consecutivo a num2")
    if num3 -1 == num2 :
        print("todos son consecutivos")
else :
    print("no son consecutivos")
    