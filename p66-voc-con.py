print("dividir una frase en palabras y cont consonantes y vocales")

frase=input("dame una frase")
Voc ="aeiouAEIOU"
Con ="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZÑ"
palabras = frase.split()
voc=0
cons=0
otr = 0
print(f"{frase}\n")
print(f"lafrase tiene {len(frase)} caracter")

for letra in frase:

    if letra.isalpha():
        if letra in "aeiouAEIOU":
            for c in frase:
                if c in Voc:
                    print(f"Tiene la vocal {c}")
           
            voc = voc + 1
        elif letra in "bcdfghjklmnpqrstvwxyzñÑBCDFGHJKLMNOPQRSTVWXYZ":
            for a in frase :
                if a in Con:
                    print(f"tiene la consonante {a}")
            cons = cons + 1
        else :
            otr = otr +1
        
print("vocales =",voc)
print("consonante =",cons)
print("otros=",otr)
