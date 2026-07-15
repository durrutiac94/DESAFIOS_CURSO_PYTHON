import sys

# ingresar la primera condicion de respuesta a estimulos

estimulos = input("responde a estimulos? (si/no)\n")

if estimulos == "no":
    print("abrir la via aerea")
elif estimulos == "si":
    print("llevarlo al hospital")
    sys.exit()

# ingresar la segunda condicion de via aerea
via_aerea = input("Respira? (si/no)\n")

if via_aerea == "no":
    print("Administrar ventilaciones")
elif via_aerea == "si":
    print("Permitirle posición de ventilación ")
    sys.exit()

# ingresar tercera condicion dentro de un ciclo while, para iterar si no llega la ambulancia
while True:
    signos = input("Signos de vida? (si/no)\n")

    if signos == "no":
        print("Administrar compresiones hasta que llegue la ambulancia")
    elif signos == "si":
        print("Reevaluar a la espera de ambulancia")

    ambulancia = input(f"llego la ambulancia? (si/no)\n")

    if ambulancia == "si":
        break
