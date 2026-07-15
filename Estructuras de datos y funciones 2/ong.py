# 1. Función para calcular el factorial (Multiplicación sucesiva)
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# 2. Función para calcular la productoria (Multiplicación de elementos de una lista)
def calcular_productoria(lista_numeros):
    resultado = 1
    for numero in lista_numeros:
        resultado *= numero
    return resultado


# 3. Función de control principal que acepta argumentos variables (**kwargs)
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact" in clave:
            res = calcular_factorial(valor)
            print(f"El factorial de {valor} es {res}")
        elif "prod" in clave:
            res = calcular_productoria(valor)
            print(f"La productoria de {valor} es {res}")


# Ejemplo de ejecución interna tal como lo solicita el PDF
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
