"""IMC = W / H^2
W : corresponde al peso de la persona en Kg.
H: corresponde a la altura en metros.
IMC: EL valor del IMC, en [Kg/m2]
"""

"""IMC Clasificación OMS
< 18.5 Bajo Peso
[ 18.5, 25 [ Adecuado
[ 25, 30 [ Sobrepeso
[ 30, 35[ Obesidad Grado I
[ 35, 40 [ Obesidad Grado II
> 40 Obesidad Grado III
"""

# importar librerias
import sys
import math

# solicitar al usuario su peso y altura
peso = int(input("ingrese su peso en kilogramos \n"))
altura = int(input("ingrese su altura en centimetros \n"))

# realizar el calculo según formula y transformar altura a metros
IMC = peso / (altura / 100) ** 2
IMC = round(IMC, 2)
print(f"Su IMC es de {IMC} kg/m2")

# comparar IMC con datos de tabla OMS y mostrar resultado
if IMC < 18.5:
    print(f"La clasificación OMS es: Peso bajo")
elif IMC > 18.5 and IMC < 25:
    print(f"La clasificación OMS es: Peso adecuado")
elif IMC > 25 and IMC < 30:
    print(f"La clasificación OMS es: Sobrepeso")
elif IMC > 30 and IMC < 35:
    print(f"La clasificación OMS es: Obesidad grado I")
elif IMC > 35 and IMC < 40:
    print(f"La clasificación OMS es: Obesidad grado II")
else:
    print(f"Obesidad Grado III")
