from error import DimensionError


class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str):
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("El valor ingresado no es válido", ancho, self.MAX)
        else:
            self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        if alto < 1 or alto > self.MAX:
            raise DimensionError("El valor ingresado no es válido", alto, self.MAX)
        else:
            self.__alto = alto


##Prueba
if __name__ == "__main__":
    try:
        mi_foto = Foto(1920, 1080, "viaje.jpg")
        print(f"foto creada: {mi_foto.ancho}x{mi_foto.alto}")
        mi_foto.ancho = 3000

    except DimensionError as e:
        print(f"Error {e}")
