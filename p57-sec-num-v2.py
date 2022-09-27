#e desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee
print("se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee")

print("impirme triangulo de numeros secuenciales")
n = int(input('Cuantos renglones ? '))

for i in range(1,n+1):
    
    for j in range(1,i+1):
       
        print(j, end=" ")
    print("\r")
