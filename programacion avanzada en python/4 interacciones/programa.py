from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

# crear menu interactivo

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

while True:
    opcion = input(
        "Que deseas hacer: \n 1. ingresar producto \n 2. listar productos \n 3. realizar una venta \n 4. Salir \n"
    )

    if opcion == "1":
        nombre = input("ingresa nombre: ")
        precio = int(input("ingresa precio: "))
        stock = int(input("ingresa stock: "))
        producto = Producto(nombre, precio, stock)
        mi_tienda.ingresar_producto(producto)
        print(f"el producto{nombre}fue ingresado")
    elif opcion == "2":
        print(mi_tienda.listar_productos())
    elif opcion == "3":
        nombre = input("ingresa el nombre del producto: ")
        cantidad = int(input("ingresa la cantidad: "))
        mi_tienda.realizar_venta(nombre, cantidad)
        print(f"venta: {cantidad} {nombre}")
    elif opcion == "4":
        print("saliendo del programa...")
        exit()
    else:
        print("Opcion no valida, por favor ingresa nuevamente...")
