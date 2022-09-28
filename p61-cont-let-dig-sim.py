#contar letras numeros o simbolos

print("contar letras numeros o digitos")

frase = input("ingresa una frase")

let =dig = sim = 0
print("frase")
print(f"\n la frase tiene {len(frase)} caracteres")

for l in frase:
    if l.isalpha():
        let = let+1
    elif l.isdigit():
        dig = dig+1
    else: sim=sim+1

print(f"la frase tiene {let} letras\n")

print(f"la frase tiene {sim} simbolos\n")

print(f"la frase tiene {dig} digitos")