# Contar las vocales y consonantes en una fras
frase = input("dame una frase")

voc=0
cons=0
otr = 0
print(f"{frase}\n")
print(f"lafrase tiene {len(frase)} caracter")

for letra in frase:
    if letra.isalpha():
        if letra in "aeiouAEIOU":
            voc = voc + 1
        elif letra in "bcdfghjklmnpqrstvwxyzñÑBCDFGHJKLMNOPQRSTVWXYZ":
            cons = cons + 1
        else :
            otr = otr +1
        
print("vocales =",voc)
print("consonante =",cons)
print("otros=",otr)
