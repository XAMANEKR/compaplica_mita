#imprime un cuadro de asteriscos
print("imprime un cuadro de asteriscos")

r=int(input("cuantos renglones"))

f=int(input("cuantas columnas"))
c= input("de que caracter")
for i in range(1, r+1):
    for j in range(1,f+1):
        print(c,end= "")
    print()