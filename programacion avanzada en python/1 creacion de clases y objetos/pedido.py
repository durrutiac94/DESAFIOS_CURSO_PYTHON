from te import Te

sabor_pedido = int(
    input("que sabor de te desea?\n 1. negro\n 2. verde\n 3. hierbas\n ")
)
formato_pedido = int(input("que formato desea? 300 o 500 gramos\n "))

if sabor_pedido == 1:
    sabor_texto = "te negro"
elif sabor_pedido == 2:
    sabor_texto = "te verde"
elif sabor_pedido == 3:
    sabor_texto = "te de hierbas"

tiempo, recomendacion = Te.tiempo_recomendacion(sabor_pedido)
precio = Te.formato_te(formato_pedido)

print("\nEste es tu pedido\n")
print(f"Sabor del té: {sabor_texto}")
print(f"Formato: {formato_pedido} gramos")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación de consumo: {recomendacion}")
