# masas, salsas e ingredientes

masas_disponibles = ["tradicional", "delgada", "bordes de queso"]
salsas_disponibles = [
    "tomate",
    "alfredo",
    "barbecue",
    "pesto",
]
ingredientes_disponibles = [
    "tomate",
    "champiñones",
    "aceituna",
    "cebolla",
    "pollo",
    "jamón",
    "carne",
    "tocino",
    "queso",
]


def cambiar_masa(pizza_actual):
    print(f"\n Masas disponibles: {masas_disponibles}")
    nueva_masa = input("Escribe el nombre de la masa que deseas: ").lower()
    if nueva_masa in masas_disponibles:
        pizza_actual["masa"] = nueva_masa
        print(f"¡Masa cambiada a {nueva_masa}!")
    else:
        print("no es una opcion valida por favor ingresa nuevamente tu masa")


def cambiar_salsa(pizza_actual):
    print(f"\n Salsas disponibles: {salsas_disponibles}")
    nueva_salsa = input("Escribe el nombre de la salsa que deseas: ").lower()
    if nueva_salsa in salsas_disponibles:
        pizza_actual["salsa"] = nueva_salsa
        print(f"¡Salsa cambiada a {nueva_salsa}!")
    else:
        print("no es una opcion valida por favor ingresa nuevamente tu salsa")


def agregar_ingrediente(pizza_actual):
    print(f"\nIngredientes disponibles: {ingredientes_disponibles}")
    nuevo_ing = input("Escribe el ingrediente que deseas agregar: ").lower()
    if nuevo_ing in ingredientes_disponibles:
        pizza_actual["ingredientes"].append(nuevo_ing)
        print(f"¡{nuevo_ing} agregado a tu pizza!")
    else:
        print("no es una opcion valida por favor ingresa nuevamente tus ingredientes")


def eliminar_ingrediente(pizza_actual):
    print(f"\nIngredientes actuales en tu pizza: {pizza_actual['ingredientes']}")
    ing_a_quitar = input(
        "Escribe el nombre del ingrediente que deseas quitar: "
    ).lower()
    if ing_a_quitar in pizza_actual["ingredientes"]:
        pizza_actual["ingredientes"].remove(ing_a_quitar)
        print(f"{ing_a_quitar} eliminado de tu pizza")
    else:
        print("Ese ingrediente no se encuentra en tu pizza actual")


def mostrar_pizza(pizza_actual):
    print("\n--- TU PIZZA ACTUAL ---")
    print(pizza_actual)


def confirmar_pedido(pizza_actual):
    # Cálculo del tiempo solicitado por el cliente
    tiempo_estimado = 20 + (2 * len(pizza_actual["ingredientes"]))

    print("\n--- RESUMEN DE TU PEDIDO ---")
    print(f"Masa: {pizza_actual['masa']}")
    print(f"Salsa: {pizza_actual['salsa']}")
    print(f"Ingredientes: {pizza_actual['ingredientes']}")
    print(f"Su orden tomará aproximadamente {tiempo_estimado} minutos.")

    confirmar = input("\n¿Desea confirmar su orden? (si/no): ")
    if confirmar.lower() == "si":
        print("¡Pedido confirmado! Su pizza entrará al horno ahora.")
        return True
    else:
        print("Volviendo al menú para que edites tu pizza.")
        return False
