from personaje import *
import random

bienvenida = input("--Bienvenido,\n ingresa el nombre de tu personaje:--\n")

jugador = Personaje(bienvenida)

jugador.estado

orco = Personaje("Orco")

probabilidad = jugador.probabilidad_de_ganar(orco)

opcion_juego = Personaje.info(probabilidad)


while opcion_juego == "1":
    azar = random.uniform(0, 1)
    if azar <= probabilidad:
        print("ganas")
        jugador.estado = 50
        orco.estado = -30

    else:
        print("pierdes")
        jugador.estado = -30
        orco.estado = 50

    jugador.estado
    orco.estado
    probabilidad = jugador.probabilidad_de_ganar(orco)
    opcion_juego = Personaje.info(probabilidad)

print("has huido")
