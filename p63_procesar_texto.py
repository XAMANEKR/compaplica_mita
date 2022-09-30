import os


txt = """Aprender a programar python es una tarea /
que requiere tiempo y constancia, la practica es lo que/
da la experiencia"""

os.system("clear")
print(f"texto:{len(txt)} - {txt}")

pal= input ("dame la palabra")
pos= txt.find(pal)

if pos!=1 :
    print (f"la palabra{pal} no fue encontrada")
    if txt.startswith(pal):
        print(f"la palabra {pal} esta al inicio")
    elif txt.endswith(pal):
        print(f"la palabra {pal} esta al final del texto")
    else:
        print(f"La palabra {pal} aparece en la posicion {pos}")
        print(f"La palabra {pal} aparece {txt.count(pal)} veces")
        txt2 = txt.replace(pal, "#")
        print(f"textomodificado {txt2}")
        
else:
    print(f"la palabra{pal} no fue encontrada")

print("\n procesamiento de texto\n")

print(f"mayusculas : {txt.upper()}\n")      
print(f"mayusculas : {txt.lower()}\n")     
print(f"mayusculas : {txt.title()}\n") 

txt3 =txt.slipt()
print(f"separar : {txt3}\n")
print(f'unir : {"_".join(txt3)}')


