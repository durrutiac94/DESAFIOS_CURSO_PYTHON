"""Crear un archivo conversiones.py y una estructura de datos apropiada que permita
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
(4 Puntos)
Para ello considere las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
Además ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa
debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
Al ejecutar el programa se espera el siguiente output:
python conversiones.py 0.0046 0.093 0.0013 10000
Respuesta esperada:
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
13.0 Dólares
"""

import sys
import math

# crear diccionario con los valores ingresados en al terminal
conversiones = {
    "Soles": float(sys.argv[1]),
    "Pesos Argentinos": float(sys.argv[2]),
    "Dolares": float(sys.argv[3]),
    "Pesos Chilenos": float(sys.argv[4]),
}

print(conversiones)

# ciclo for para multiplicar cada valor del diccionario según el nombre de  su llave, con el valor de CLP

print(f"Los {conversiones["Pesos Chilenos"]} Pesos Chilenos equivalen a: \n")

for peso, conversion in conversiones.items():
    if peso == "Soles" or peso == "Pesos Argentinos" or peso == "Dolares":
        print(f" {conversion * conversiones["Pesos Chilenos"]} {peso}")
