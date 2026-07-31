# importar las listas de ingredientes
from ingredientes import *


# 1 crear la clase pizza y sus atributos de clase
class Pizza:
    proteina = ingredientes_proteicos
    vegetales = ingredientes_vegetales
    masa = tipo_de_masa
    precio = 10000
    tamaño = "familiar"

    # 2 crear metodo para validar elemento dentro de una lista
    # a. elemento a validar
    # b. los valores posibles a considerar (lista de textos)

    @staticmethod
    def validar(elemento, valores_posibles):
        if elemento in valores_posibles:
            return True

        else:
            return False

    # 3 en la clase pizza agregar metodo para realizar pedido
    # dentro del def solicitar al usuario el ingrediente proteico,
    # luego el primer vegetal y luego el segundo, al final la masa.
    # cada ingreso debe almacenarse en un atributo de instancia.
    #

    def pedir(self):
        self.prot = input(f"ingresa tu ingrediente proteico: {ingredientes_proteicos}")
        vegetal1 = input(f"inrgesa el primer vegetal {ingredientes_vegetales}")
        vegetal2 = input(f"inrgesa el segundo vegetal {ingredientes_vegetales}")
        self.veg = [vegetal1, vegetal2]
        self.masa = input(f"ingresa el tipo de masa: {tipo_de_masa}")

        # 4 realizar validacion
        validar_proteina = Pizza.validar(self.prot, Pizza.proteina)
        validar_veg1 = Pizza.validar(vegetal1, Pizza.vegetales)
        validar_veg2 = Pizza.validar(vegetal2, Pizza.vegetales)
        validar_masa = Pizza.validar(self.masa, Pizza.masa)

        self.es_valida = (
            validar_proteina and validar_veg1 and validar_veg2 and validar_masa
        )
