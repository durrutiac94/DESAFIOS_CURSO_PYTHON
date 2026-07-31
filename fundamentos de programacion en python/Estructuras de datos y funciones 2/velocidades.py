import sys

velocidades = [
    25,
    12,
    19,
    16,
    11,
    11,
    24,
    1,
    14,
    14,
    16,
    10,
    6,
    23,
    13,
    25,
    4,
    19,
    14,
    20,
    18,
    9,
    18,
    4,
    18,
    1,
    3,
    4,
    2,
    14,
    23,
    19,
    23,
    9,
    18,
    20,
    22,
    14,
    1,
    10,
    5,
    23,
    3,
    5,
    9,
    5,
    3,
    12,
    20,
    5,
    11,
    10,
    18,
    10,
    14,
    5,
    23,
    20,
    23,
    21,
]


# crear la funcion
def correas(velocidades):
    # calcular promedio
    promedio = sum(velocidades) / len(velocidades)

    # crear lista para agregar los valores sobre el promedio
    posiciones_sobre_promedio = []

    # recorrer la lista para tener el indice de esos valores

    for indice, velocidad in enumerate(velocidades):
        if velocidad > promedio:
            posiciones_sobre_promedio.append(indice)
    print(posiciones_sobre_promedio)


# llamar a la funcion
correas(velocidades)
