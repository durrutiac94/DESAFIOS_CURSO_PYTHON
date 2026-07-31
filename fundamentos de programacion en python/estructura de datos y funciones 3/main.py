# importar todas las funciones del modulo
from funciones_pizza import *

# diccionario donde se va guardando la pizza armada
pizza_actual = {
    "masa": "Masa Tradicional",
    "salsa": "Salsa de Tomate",
    "ingredientes": [],
}

# crear el menu usando ciclo while

menu_activo = True

while menu_activo:
    print("\n---BIENVENIDO AL MENU DE PIZZA JAT---\n")
    print("1. Cambiar Tipo de Masa")
    print("2. Cambiar Tipo de Salsa")
    print("3. Agregar Ingrediente")
    print("4. Eliminar Ingrediente")
    print("5. Mostrar Pizza Actual")
    print("6. Confirmar Pedido (Ver Tiempo y Salir)")

    opcion = input("\n --- Por favor selecciona una opcion (1-6): ---\n")

    if opcion == "1":
        cambiar_masa(pizza_actual)

    elif opcion == "2":
        cambiar_salsa(pizza_actual)

    elif opcion == "3":
        agregar_ingrediente(pizza_actual)

    elif opcion == "4":
        eliminar_ingrediente(pizza_actual)

    elif opcion == "5":
        mostrar_pizza(pizza_actual)

    elif opcion == "6":
        if confirmar_pedido(pizza_actual):
            menu_activo = False

    else:
        print("No es una opción disponible por favor selecciona nuevamente (1-6)")
