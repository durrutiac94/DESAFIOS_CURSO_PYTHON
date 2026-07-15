import sys

# Lista de velocidades entregada en el requerimiento
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

# 1. Calculamos el promedio de manera nativa
promedio = sum(velocidades) / len(velocidades)

# 2. Inicializamos la lista para almacenar las posiciones
posiciones_sobre_promedio = []

# 3. Recorremos usando enumerate para obtener índice y valor al mismo tiempo
for indice, velocidad in enumerate(velocidades):
    if velocidad > promedio:
        posiciones_sobre_promedio.append(indice)

# 4. Mostramos el resultado esperado en la terminal
print(posiciones_sobre_promedio)
