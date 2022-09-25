#imprime el factor del numero

print("imprime el factorial de un numero \n")
n = int(input ("dame un numero entero"))
f= 1
for i in range(1, n+1):
    print(i, end="X")
    print("\n el factorial es",f)