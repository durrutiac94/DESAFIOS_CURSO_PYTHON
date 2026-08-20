from personaje import *
import random

bienvenida = input(
    "--Bienvenido a Gran Fantasia,\n ingresa el nombre de tu personaje:--\n"
)

jugador = Personaje(bienvenida)

jugador.estado

orco = Personaje("Orco")

probabilidad = jugador.probabilidad_de_ganar(orco)

opcion_juego = Personaje.info(probabilidad)


while opcion_juego == "1":
    azar = random.uniform(0, 1)
    if azar <= probabilidad:
        print(
            "Le has ganado al orco, felicidades,  recibiras 50 puntos de experiencia "
        )
        jugador.estado = 50
        orco.estado = -30

    else:
        print("El orco te ha ganado, has perdido 30 puntos de experiencia")
        jugador.estado = -30
        orco.estado = 50

    jugador.estado
    orco.estado
    probabilidad = jugador.probabilidad_de_ganar(orco)
    opcion_juego = Personaje.info(probabilidad)

print("has huido")
