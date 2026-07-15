import sys

precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}

umbral = int(sys.argv[1])
menor_mayor = sys.argv[2]


def filtrar(precio, umbral):
    for producto, precio in precios.items():
        if precio > umbral:
            nuevo_diccionario = {}
            nuevo_diccionario[producto] = precio
        return nuevo_diccionario


print(filtrar(precios, 20000))
