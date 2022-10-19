import os;os.system("cls")
nmes=["","1","2","3","4","5","6","7","8","9","10","11","12",]

mes=["","Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","dic",]

dias=[0,31,28,31,30,31,30,31,31,30,31,30,31]


num=input("ingresa un mes en formato 00\n")

if num in nmes:
    print(f"El mes {num}")
    pos=nmes.index(num)
    print(f'{mes[pos]} , {dias[pos]}')