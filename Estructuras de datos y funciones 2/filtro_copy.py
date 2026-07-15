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

if len(sys.argv) == 2:
    operacion = "mayor"
else:
    operacion = sys.argv[2]

# Lógica de filtrado
if operacion == "mayor":
    nuevo_diccionario = []
    for producto, precio in precios.items():
        if precio > umbral:
            nuevo_diccionario.append(producto)

    print(f"Los productos mayores al umbral son: {', '.join(nuevo_diccionario)}")

elif operacion == "menor":
    seleccionados = []
    for producto, precio in precios.items():
        if precio < umbral:
            seleccionados.append(producto)

    print(f"Los productos menores al umbral son: {', '.join(seleccionados)}")

else:
    print("Lo sentimos, no es una operación válida")
