from abc import ABC, abstractmethod
from typing import List
from datetime import date

"""De la clase Anuncio:
● Al crear, o al querer modificar el alto o el ancho de un anuncio ya creado, debe
consultar si el valor que se quiere asignar es mayor a cero. De ser así, se asigna el
valor ingresado. De no ser así, se asigna 1.
● Para esta etapa no se le solicita implementar las reglas de los atributos url_archivo
ni url_clic, pero sí debe definir sus getter y setter con la lógica básica de
asignación de un nuevo valor al atributo correspondiente.
● Al querer modificar el sub_tipo de algún anuncio ya creado, se debe validar que se
esté ingresando un subtipo dentro de los permitidos en el tipo de la instancia actual.
Los subtipos permitidos para las instancias de cada clase corresponden a los
elementos de la tupla definida en el atributo de clase SUB_TIPOS respectivo. En caso
de no cumplirse esta condición al momento de querer cambiar el valor del atributo
sub_tipo, se debe lanzar una excepción SubTipoInvalidoException.
● El método mostrar_formatos es un método estático que muestra en pantalla los
formatos y sus subtipos asociados disponibles para crear anuncios."""


class SubTipoInvalidoException(Exception):
    pass


class Anuncio(ABC):
    SUB_TIPOS = ()

    def __init__(
        self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str
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
        self.__url_clic = url_clic
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
    def url_click(self):
        return self.url_clic

    @url_click.setter
    def url_click(self, valor):
        self.url_clic = valor

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoException
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


class Social(Anuncio):
    formato = "social"
    SUB_TIPOS = ("Facebook", "Linkedin")

    def comprimir_anuncio(self):
        return super().comprimir_anuncio

    def redimensionar_anuncio(self):
        return super().redimensionar_anuncio()


class Video(Anuncio):
    formato = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion

    def comprimir_anuncio(self):
        return super().comprimir_anuncio()


class Campaña:
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


class SubTipoInvalidoError(SubTipoInvalidoException):
    pass


###
Anuncio.mostrar_formatos()
