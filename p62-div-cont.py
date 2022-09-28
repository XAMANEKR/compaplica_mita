#dividir una frase en palabras y cont consonantes y vocales
print("dividir una frase en palabras y cont consonantes y vocales")

frase=input("dame una frase")

print(f"{len(frase)}- {frase}\n")

palabras = frase.split()

print(f"lista de palabras{palabras} \n")

for palabra in palabras:
    print(f"{len(palabra):>4}-{palabra:<12}",end=" ")
    v=c=0
    for letra in palabra:
        if letra.isalpha():
            if letra.lower() in "aeiou" : v = v +1
            else: c=c+1
    
    print(f"-v{v:>4} c:{c:>4}")

print(f"{'final':-^35}")


