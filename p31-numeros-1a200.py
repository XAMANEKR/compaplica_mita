#imprime numeros del 1 al 200

print("numeros del 10 al 200")

c = 1
while c <= 200 :
    c += 1
    if c % 10 != 0:
            continue
    print( c , end=" ")
