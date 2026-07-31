# rentabilidad= P * U - GT #
# paso 3 utilidad del año anterior #

precio= int(input("ingresa el precio (numero entero)\n"))
cantidad_de_usuarios =int(input("ingesa el numero de suscriptores (numero entero)\n"))
gasto_total = int(input("ingesa el gasto total (numero entero)\n"))
utilidad_anterior= int(input("ingresa la utilidad del año anterior (numero entero)\n"))


utilidad= (precio*cantidad_de_usuarios-gasto_total)
razon= (utilidad/utilidad_anterior)
razon=round(razon, 2)
print(f"La utilidad es {utilidad}")
print(f"La razon es {razon}")