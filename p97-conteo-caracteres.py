#cuenta caracteres

cadena=input("Escribr una palabra: ")
dic={}

for i in range(len(cadena)):
    dic[cadena[i]]=0
for e in dic.keys():
    cont=0
    for a in range(len(cadena)):
        if e == cadena[a]:
            cont+=1          
    dic[e]=cont
print(f"{dic}")