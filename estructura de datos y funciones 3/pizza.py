# Listas de opciones disponibles de la pizzería
OPCIONES_MASA = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
OPCIONES_SALSA = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
INGREDIENTES_DISPONIBLES = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

# Estado inicial de la pizza
pizza_actual = {
    "masa": "Masa Tradicional",
    "salsa": "Salsa de Tomate",
    "ingredientes": []
}

menu_activo = True

while menu_activo:
    print("\n=== PIZZA JAT - MENU DE COMPRA ===")
    print("1. Cambiar Tipo de Masa")
    print("2. Cambiar Tipo de Salsa")
    print("3. Agregar Ingrediente")
    print("4. Eliminar Ingrediente")
    print("5. Mostrar Pizza Actual")
    print("6. Confirmar Pedido (Ver Tiempo y Salir)")
    
    opcion = input("\nSeleccione una opción (1-6): ")
    
    if opcion == "1":
        print(f"\nMasas disponibles: {OPCIONES_MASA}")
        nueva_masa = input("Escribe el nombre exacto de la masa que deseas: ")
        pizza_actual["masa"] = nueva_masa
        print(f"¡Masa cambiada a {nueva_masa}!")
        
    elif opcion == "2":
        print(f"\nSalsas disponibles: {OPCIONES_SALSA}")
        nueva_salsa = input("Escribe el nombre exacto de la salsa que deseas: ")
        pizza_actual["salsa"] = nueva_salsa
        print(f"¡Salsa cambiada a {nueva_salsa}!")
        
    elif opcion == "3":
        print(f"\nIngredientes disponibles: {INGREDIENTES_DISPONIBLES}")
        nuevo_ing = input("Escribe el ingrediente que deseas agregar: ")
        pizza_actual["ingredientes"].append(nuevo_ing)
        print(f"¡{nuevo_ing} agregado a tu pizza!")
        
    elif opcion == "4":
        print(f"\nIngredientes actuales en tu pizza: {pizza_actual['ingredientes']}")
        ing_a_quitar = input("Escribe el nombre del ingrediente que deseas quitar: ")
        pizza_actual["ingredientes"].remove(ing_a_quitar)
        print(f"¡{ing_a_quitar} eliminado de tu pizza!")
        
    elif opcion == "5":
        print("\n--- TU PIZZA ACTUAL ---")
        print(f"Masa: {pizza_actual['masa']}")
        print(f"Salsa: {pizza_actual['salsa']}")
        print(f"Ingredientes: {pizza_actual['ingredientes']}")
        
    elif opcion == "6":
        # Cálculo del tiempo solicitado por el cliente
        tiempo_estimado = 20 + (2 * len(pizza_actual["ingredientes"]))
        
        print("\n=== RESUMEN DE TU PEDIDO ===")
        print(f"Masa: {pizza_actual['masa']}")
        print(f"Salsa: {pizza_actual['salsa']}")
        print(f"Ingredientes: {pizza_actual['ingredientes']}")
        print(f"Su orden tomará aproximadamente {tiempo_estimado} minutos.")
        
        confirmar = input("\n¿Desea confirmar su orden? (si/no): ")
        if confirmar.lower() == "si":
            print("¡Pedido confirmado! Su pizza entrará al horno ahora.")
            menu_activo = False
        else:
            print("Volviendo al menú para que edites tu pizza.")