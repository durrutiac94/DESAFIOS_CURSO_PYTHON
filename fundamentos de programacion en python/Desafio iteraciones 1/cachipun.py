# piedra-papel-tijera

# importar librerias
import sys
import random

# solicitar al usuario ingresar su jugada
jugada = str(input("ingresa tu jugada \n"))

# definir jugadas permitidas
jugadas_permitidas = {"piedra", "papel", "tijera"}
if jugada not in jugadas_permitidas:
    print(f"El tipo {jugada} no es permitida")
    print(f"Usa alguna de estas opciones: {jugadas_permitidas}")
    sys.exit()

print(f"Tu jugada es: {jugada} ")

# crear jugada del computador usando libreria random
jugada_computador = random.choice(list(jugadas_permitidas))
print(f"la jugada del computador es: {jugada_computador}")

# crear las reglas de victoria, derrota o empate
if jugada == jugada_computador:
    print(f"empate")
elif (
    (jugada == "piedra" and jugada_computador == "tijera")
    or (jugada == "papel" and jugada_computador == "piedra")
    or (jugada == "tijera" and jugada_computador == "papel")
):
    print(f"tu ganas")

else:
    print(f"tu pierdes")
