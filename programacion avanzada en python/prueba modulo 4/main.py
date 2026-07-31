from abc import ABC, abstractmethod
from typing import List
from datetime import date


class Anuncio(ABC):
    def __init__(
        self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str
    ):
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1

        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 1

        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self.__alto = valor
        else:
            self.__alto = 1

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self.__ancho = valor
        else:
            self.__ancho = 1

    @property
    def url_archivo(self):

        @staticmethod
        def mostrar_formatos(self):
            for clase_hija in Anuncio.__subclasses__():
                print(f"{clase_hija.formato}:")
                for sub_tipo in clase_hija.sub_tipos:
                    print("{sub_tipo}")
            print("")

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Social(Anuncio):
    formato = "social"
    sub_tipos = ("Facebook", "Linkedin")

    def comprimir_anuncio(self):
        return super().comprimir_anuncio

    def redimensionar_anuncio(self):
        return super().redimensionar_anuncio()


class Video(Anuncio):
    formato = "Video"
    sub_tipos = ("instream", "outstream")

    def __init__(self, url_archivo, url_click, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_click, sub_tipo)
        self.__duracion = duracion

    def comprimir_anuncio(self):
        return super().comprimir_anuncio()


class Campaña(Anuncio):
    def __init__(
        self, nombre, fecha_inicio: date, fecha_termino: date, anuncios: List[Anuncio]
    ):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios

    def __str__(self):
        return "Campaña"

    def addAnuncio(self, anuncio: Anuncio):
        pass


class Error(Exception):
    pass


class SubTipoInvalidoError(Error):
    pass


###
Anuncio.mostrar_formatos()
