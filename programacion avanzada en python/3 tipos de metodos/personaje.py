class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        print(f"nombre: {self.nombre}")
        print(f"nivel: {self.nivel}")
        print(f"experiencia: {self.experiencia}")

    @estado.setter
    def estado(self, experiencia_ganada):
        experiencia_total = (
            (self.nivel - 1) * 100 + self.experiencia + experiencia_ganada
        )
        if experiencia_total < 0:
            experiencia_total = 0
        self.experiencia = experiencia_total % 100
        self.nivel = 1 + (experiencia_total // 100)

    def __lt__(self, other):
        if self.nivel < other.nivel:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.nivel > other.nivel:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.nivel == other.nivel:
            return True
        else:
            return False

    def probabilidad_de_ganar(self, other):
        if self.nivel < other.nivel:
            return 0.33

        elif self.nivel > other.nivel:
            return 0.66

        elif self.nivel == other.nivel:
            return 0.5

    @staticmethod
    def info(probabilidad):
        print(f"Ha aparecido un orco, tienes {probabilidad*100}% probabilidad de ganar")
        print(
            "si ganas obtienes 50 exp y el orco pierde 30, si pierdes se restan 30 exp y el orco gana 50"
        )
        accion_jugador = input("deseas 1. atacar o 2. huir?")
        return accion_jugador
