from pizza import Pizza

# 5a.
print(Pizza.proteina)
print(Pizza.vegetales)
print(Pizza.masa)
print(Pizza.precio)
print(Pizza.tamaño)

# 5.b
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# 5.c
pedido_pizza = Pizza()
pedido_pizza.pedir()

# 5.d
print(pedido_pizza.proteina)
print(pedido_pizza.vegetales)
print(pedido_pizza.masa)
print(pedido_pizza.es_valida)

# 5.e
print(Pizza.es_valida)
