"""Utilizando una estructura de datos apropiada, cuente la cantidad de
caracteresdistintosquecomponenuntexto.

Cuente el número de palabras distintas que componen el texto ingresado.
Parasepararuntextoporespaciospuedeutilizarelmétodo .split("")."""

import sys

with open("lorem_ipsum.txt", "r", encoding="utf-8") as file:
    texto = file.read()


print(texto)

caracteres = set()

for caracter in texto:
    caracteres.add(caracter)

print(f" el numero de caracteres distintos es: {len(caracteres)}")

palabras = len(set(texto.split(" ")))

print(f" el numero de palabras distintas es: {palabras}")
