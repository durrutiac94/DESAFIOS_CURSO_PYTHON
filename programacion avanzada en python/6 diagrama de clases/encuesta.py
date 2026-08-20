from pregunta import Pregunta


class Encuesta:
    def __init__(self, nombre: str, preguntas: list):
        self.nombre = nombre
        self.__listados_respuestas = []

        self.__preguntas = [
            Pregunta(
                p["enunciado"], p["requerida"], p["alternativas"], p.get("ayuda", "")
            )
            for p in preguntas
        ]

    def mostrar_encuesta(self):
        pass

    def agregar_listado_respuestas(self, listado):
        pass


class EncuestaLimitadaEdad(Encuesta):
    def __init__(
        self, nombre: str, preguntas: list, edad_minima: int, edad_maxima: int
    ):
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado):
        pass


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones: list):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    def agregar_listado_respuestas(self, listado):
        pass
