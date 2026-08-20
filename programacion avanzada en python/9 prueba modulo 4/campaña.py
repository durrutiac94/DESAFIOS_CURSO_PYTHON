from abc import ABC, abstractmethod
from typing import List
from datetime import date
from anuncio import *


class Campaña:
    def __init__(
        self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list
    ):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.__anuncios = []
        for anuncio in anuncios:
            if anuncio["FORMATO"] == "Video":
                nuevo_anuncio = Video(
                    anuncio["URL_ARCHIVO"],
                    anuncio["URL_CLIC"],
                    anuncio["SUB_TIPO"],
                    anuncio["DURACION"],
                )
                self.__anuncios.append(nuevo_anuncio)

            elif anuncio["FORMATO"] == "Social":
                nuevo_anuncio = Social(
                    anuncio["ANCHO"],
                    anuncio["ALTO"],
                    anuncio["URL_ARCHIVO"],
                    anuncio["URL_CLIC"],
                    anuncio["SUB_TIPO"],
                )
                self.__anuncios.append(nuevo_anuncio)

            elif anuncio["FORMATO"] == "Display":
                nuevo_anuncio = Display(
                    anuncio["ANCHO"],
                    anuncio["ALTO"],
                    anuncio["URL_ARCHIVO"],
                    anuncio["URL_CLIC"],
                    anuncio["SUB_TIPO"],
                )
                self.__anuncios.append(nuevo_anuncio)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoException("el nombre supera los 250 caracteres")
        else:
            self.__nombre = valor

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor):
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        cantidad_video = 0
        cantidad_display = 0
        cantidad_social = 0

        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                cantidad_video += 1
            elif isinstance(anuncio, Display):
                cantidad_display += 1
            elif isinstance(anuncio, Social):
                cantidad_social += 1

        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {cantidad_video} Video, {cantidad_display} Display, {cantidad_social} Social"
