# repasos conjuntos
import os; os.system('clear')

A = {"JUAN","MARIA","PEDRO","JOSE","ROCIO",}
B= {"PEDRO","JUAN","PABLO","MATEO","ESTHER",}



print(f"A : {A}\nc2 : {B}\nc3 ")

print("\nUnion: ")
print(f"A union B : {A.union(B)}")

print("\nIntersección: ")
print(f"A inteseccion B: {A.intersection(B)}")

print("\nDiferencia:")
print(f"A diferencia B: {A.difference(B)}")

print("\nDiferencia simetrica:")
print(f"A diferenia simetrica B: {A.symmetric_difference(B)}")

print("\nProbar por subconjuntos:")
print(f"B es subconjunto de A? : {B.issubset(A)} ")

print("\nProbar por supersubconjuntos:")
print(f"A es superconjunto de B ? : {A.issuperset(B)}")

print("\nVerficar la presencia de un elemento en el conjunto:")
print(f" 2 esta en c1 ? : {'PEDRO' in A}")
print(f" 6 no esta en c2 ? : {'LILIA' not in B}")

