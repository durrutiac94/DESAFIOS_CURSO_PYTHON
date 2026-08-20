class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension == None and self.maximo == None:
            return super().__str__()
        else:
            return f"{self.mensaje}, tu foto es de {self.dimension},y el maximo permitido es {self.maximo}"
