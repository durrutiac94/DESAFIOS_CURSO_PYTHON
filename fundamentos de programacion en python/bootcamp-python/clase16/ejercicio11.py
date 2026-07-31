# Ejercicio 11: total de compra con descuento
# Enunciado: pide precio, cantidad y descuento; calcula el total final.
# Input de ejemplo: precio = 900, cantidad = 2, descuento = 5
# Output esperado (si se corrige): Total a pagar: 1710.0

precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = float(input("Descuento (%): "))
subtotal = precio * cantidad
total = subtotal - (subtotal * descuento / 100)
print(f"Total a pagar: {total}")
