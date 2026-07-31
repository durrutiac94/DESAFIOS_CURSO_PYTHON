# Ejercicio 28: edad exacta en dias
# Enunciado: pide fecha de nacimiento (AAAA-MM-DD) y calcula edad aproximada en dias.
# En este ejercicio, import sirve para trabajar con fechas reales usando datetime.
# Input de ejemplo: nacimiento = 2000-01-01
# Output esperado (si se corrige): Edad en dias: un numero positivo
import datetime

texto = input("Fecha de nacimiento (AAAA-MM-DD): ")
nacimiento = datetime.datetime.strptime(texto, "%Y-%m-%d").date()
hoy = datetime.date.today()

dias = (hoy-nacimiento ).days

print(f"Edad en dias: {dias}")
