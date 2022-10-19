#repaso conjuntos

A ={50,60,70,80,90,100,200}
B ={60,90,100,300,400,500}
C ={10,20,60,90,70,100,600,700}


print(f"A: {A}\nB : {B}\nC : {C}\n")

print("\nUnion: ")
print(f"A union B : {A.union(B)}")
print(f"B union C : {B | C}")

print("\nDiferencia:")
print(f"A diferencia C: {A.difference(C)}")

print("\nDiferencia simetrica:")
print(f"B diferenia simetrica C: {B.symmetric_difference(C)}")

print("\nProbar por subconjuntos:")
print(f"A es subconjunto de B ? : {A.issubset(B)} ")
print(f"C es subconjunto de A ? : {C<=A} ")

print("\nVerficar la presencia de un elemento en el conjunto:")
print(f" 100 esta en A ? : {100 in A}")
print(f" 60 esta en A,B,C ? : {60 in A,B,C}")
print(f" 900 no esta en C ? : {900 not in A,B,C}")