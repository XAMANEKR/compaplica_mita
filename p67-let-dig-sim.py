#contar letras numeros o simbolos

print("contar letras numeros o digitos")

frase = input("ingresa una frase")

let =dig = sim = 0
print("frase")
print(f"\n la frase tiene {len(frase)} caracteres")
letra ="abcdefghijklmnopqrstuvwxyzñABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
digito = "01234567889"
simbolo =""
for l in frase:
    if l.isalpha():
        for a in frase:
            if a in letra:
                 print(f"tiene la letra {a}")
        let = let+1
    elif l.isdigit():
        for b in frase:
            if b in digito:
                 print(f"tiene el digito {b}")
        dig = dig+1
    else: sim=sim+1
    

print(f"la frase tiene {let} letras\n")