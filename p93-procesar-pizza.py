# Procesar pizza
import os; os.system("cls")

print("pedido de pizza")
ingr = {"E":4,"T":1.50, "P":3.50, "C":3.74, "A":0.40}
base = 15
st = 0
tot = 0
pedido = input("ingredientes [T]omate, [P]iñon, [C]hampiñon, [A]guacate [E]xtraqueso\n ").upper()

for i in pedido:
    if i in "TPCAE":
        st = st + ingr[i]
st = st + base

if st >=20 :
    tot = st - (st * 0.05)

print(f"El subtotal es : {st}")
print(f"El total es : {tot}")