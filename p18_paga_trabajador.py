# Calcular la paga total de un trabajador
#datos
print('Calculando la paga total de un trabajador \n\n' )
nombre = input("dame el nombre")
horas = int(input("dame las horas trabjadas"))
paga= float(input("dame pago por hora"))
tasa = 0.3

# Calculos
if horas <= 40 :
    pagabruta = horas * paga
else:
    extra = horas - 40
    pagabruta = (40 * paga)+ (extra * paga * 2)



impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#salidas
print("\n resumen de pago \n")
print(f"el trabjador{ nombre}")
print(f"paga bruta{pagabruta}")
print(f"impuesto {impuesto}")
print(f"paga neta{paganeta}")