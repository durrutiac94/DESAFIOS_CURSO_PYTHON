import sys

precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}

# umbral
umbral = int(sys.argv[1])

# condiciones
if len(sys.argv) == 2:
    condicion = "mayor"
else:
    condicion = sys.argv[2].lower()

# funcion de filtrado


def filtrado(umbral, condicion):
    nuevo_diccionario = {}
    if condicion == "mayor":
        for producto, precio in precios.items():
            if precio > umbral:
                nuevo_diccionario[producto] = precio

        print(f"Los productos mayores al umbral son: {', '.join(nuevo_diccionario)}")

    elif condicion == "menor":
        for producto, precio in precios.items():
            if precio < umbral:
                nuevo_diccionario[producto] = precio

        print(f"Los productos menores al umbral son: {', '.join(nuevo_diccionario)}")

    else:
        print("Lo sentimos, no es una operación válida")


# llamar a la funcion
filtrado(umbral, condicion)
