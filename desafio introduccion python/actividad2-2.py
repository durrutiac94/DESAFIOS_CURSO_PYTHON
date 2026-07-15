# rentabilidad= P * U - GT 
# paso 2 usuarios premium #


precio= int(input("ingresa el precio (pesos chilenos)\n"))
cantidad_de_usuarios_normal =int(input("ingresa el numero de suscriptores (numero entero)\n"))
cantidad_de_usuarios_premium =int(input("ingresa el numero de suscriptores premium (numero entero)\n"))
gasto_total = int(input("ingresa el gasto total (numero entero)\n"))

utilidad= ((precio*cantidad_de_usuarios_normal)+(cantidad_de_usuarios_premium*precio*1.5)-gasto_total)
print(f"La utilidad es {utilidad}")