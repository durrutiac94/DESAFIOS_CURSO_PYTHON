class Te:
    duracion = "365 dias"

    @staticmethod
    def tiempo_recomendacion(sabor):
        if sabor == 1:
            tiempo = 3
            recomendacion = "al desayuno"
        elif sabor == 2:
            tiempo = 5
            recomendacion = "al medio día"
        elif sabor == 3:
            tiempo = 6
            recomendacion = "al atardecer"

        return tiempo, recomendacion

    @staticmethod
    def formato_te(formato):
        if formato == 300:
            precio = 3000
        elif formato == 500:
            precio = 5000

        return precio
