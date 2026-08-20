from alternativa import Alternativa


class Pregunta:
    def __init__(
        self, enunciado: str, requerida: bool, alternativas: list, ayuda: str = ""
    ):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida

        self.__alternativas = [
            Alternativa(alt["contenido"], alt.get("ayuda", "")) for alt in alternativas
        ]

    @property
    def alternativas(self):
        return self.__alternativas

    def mostrar_pregunta(self):
        pass
