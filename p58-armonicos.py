print("imprime el termino armónico")

n= int(input("inserta numero"))
s=0

for i in range(1,n+1):
    if i==1:
        print("1+",end=" ")
        s += 1
    if i==n:
        print(f"1/{i}",end=" ")
        s += (1/i)
    else:
        print(f'1/{i}',end='+')
        s += (1/i)
print(f'La suma de los armonicos es: {s}')