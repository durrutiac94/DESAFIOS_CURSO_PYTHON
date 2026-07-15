# rentabilidad= P * U - GT #
# paso 1

precio= int(input("ingesa el precio (numero entero)\n"))
cantidad_de_usuarios =int(input("ingesa el numero de suscriptores (numero entero)\n"))
gasto_total = int(input("ingesa el gasto total (numero entero)\n"))

utilidad= (precio*cantidad_de_usuarios-gasto_total)
print(f"La utilidad es {utilidad}")