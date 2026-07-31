# velocidad de escape = raiz cuadrada (2*g*rmet)

import math

g=float(input("ingrese la constante g: (m/s)\n"))
r=float(input("Ingrese el radio en Kilómetros:\n"))
rmet=(r*1000)
ve= math.sqrt(2*g*rmet)
ve=round(ve,2)
print(f"La velocidad de Escape es {ve}  [m/s].")