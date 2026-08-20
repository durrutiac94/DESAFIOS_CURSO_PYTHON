from abc import ABC, abstractmethod
from error import *


class Anuncio(ABC):
    def __init__(
        self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str
    ):
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            self.__ancho = 1
        else:
            self.__ancho = valor

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            self.__alto = 1
        else:
            self.__alto = valor

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, valor):
        self.__url_archivo = valor

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, valor):
        self.__url_clic = valor

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(
                f"Subtipo invalido: {valor}. Los subtipo valido son: {self.SUB_TIPOS}"
            )
        self.__sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        for clase_hija in Anuncio.__subclasses__():
            print(f"{clase_hija.formato}:")
            for sub_tipo in clase_hija.SUB_TIPOS:
                print(sub_tipo)
        print("")

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor):
        if valor <= 0:
            self.__duracion = 5
        else:
            self.__duracion = valor

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    @abstractmethod
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    @abstractmethod
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
