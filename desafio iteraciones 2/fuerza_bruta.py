"""Utilizar from string import ascii_lowercase
○ ascii_lowercase es un string con todas las letras del abecedario en
minúsculas(sinlañ).
● Noconsiderarlañ.
● Consideramayúsculasyminúsculascomounamismaletra.
● Seconsidera"intento" cadavezquesecomparaunaletra
"""

import sys
from string import ascii_lowercase

# crear input para ingresar la contraseña
ingresa_contraseña = input("ingresa tu contraseña\n (no usar letra Ñ)")

# convertir ese input a letras minusculas en una nueva variable
contraseña = ingresa_contraseña.lower()
print(f"tu contraseña elegida es: {contraseña}")

comparacion = ascii_lowercase
print(f"el listado de comparacion es {comparacion}")

# definir variable para los intentos
intentos = 0

# realizar ciclo para comparar cada letra de la contraseña con el abecedario
for letra_objetivo in contraseña:
    print(f"letra objetivo: {letra_objetivo}")
    for letra_intento in comparacion:
        print(f"letra intento {letra_intento}")

        intentos += 1
        if letra_intento == letra_objetivo:
            print(f"letra encontrada: {letra_objetivo}, siguiente ")
            break

print(f"la contrasena fue forzada en {intentos} intentos")
