# funcion factorial
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# funcion productoria
def calcular_productoria(lista_numeros):
    resultado = 1
    for numero in lista_numeros:
        resultado *= numero
    return resultado


# funcion de control
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact" in clave:
            res = calcular_factorial(valor)
            print(f"El factorial de {valor} es {res}")
        elif "prod" in clave:
            res = calcular_productoria(valor)
            print(f"La productoria de {valor} es {res}")


# ejecutar la funcion calcular

calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)
