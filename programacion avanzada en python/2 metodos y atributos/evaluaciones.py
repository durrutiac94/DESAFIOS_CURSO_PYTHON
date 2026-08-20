from pizza import Pizza

# 5a.
print(f"ingredientes proteicos: {Pizza.proteina}")
print(f"ingredientes vegetales: {Pizza.vegetales}")
print(f"tipo de masa:  {Pizza.masa}")
print(f"precio: ${Pizza.precio}")
print(f"tamaño: {Pizza.tamaño}")

# 5.b
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# 5.c
pedido_pizza = Pizza()
pedido_pizza.pedir()

# 5.d
print("\n-- tu pizza: \n")
print(pedido_pizza.proteina)
print(pedido_pizza.vegetales)
print(pedido_pizza.masa)
print(pedido_pizza.es_valida)

# 5.e
print(Pizza.es_valida)
