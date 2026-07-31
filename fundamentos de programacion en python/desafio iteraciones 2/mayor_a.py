import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

umbral = int(sys.argv[1])

nuevo_diccionario = {}

contador = 0

meses = list(ventas.keys())

while contador < len(ventas):
    mes = meses[contador]
    venta = ventas.get(mes)
    if venta > umbral:
        nuevo_diccionario[mes] = venta
    contador += 1

print(nuevo_diccionario)
