from tienda import Tienda
from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

# 1 crear la tienda

print("Bienvenido al menu")
nombre = input("ingresa el nombre de la tienda: ")
costo_delivery = int(input("ingresa el costo del delivery: "))

print(
    "que tipo de tienda deseas crear\n 1. Restaurante \n 2. Supermercado \n 3. Farmacia"
)
tipo = input("ingresa tu opcion: ")

if tipo == "1":
    mi_tienda = Restaurante(nombre, costo_delivery)
elif tipo == "2":
    mi_tienda = Supermercado(nombre, costo_delivery)
elif tipo == "3":
    mi_tienda = Farmacia(nombre, costo_delivery)
else:
    print("Opción no válida. Cerrando el programa...")
    exit()
