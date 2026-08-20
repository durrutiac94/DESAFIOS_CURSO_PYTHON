from abc import ABC
from abc import abstractmethod


class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    precio = 0
    dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia):
        if 4 >= nueva_membresia >= 1:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self


class Basica(Membresia):
    precio = 3000
    dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia):
        if 4 >= nueva_membresia >= 2:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)


class Familiar(Basica):
    precio = 5000
    dispositivos = 5

    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.dias_de_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def modificar_control_parental(self):
        pass


class SinConexion(Basica):
    precio = 3500
    dispositivos = 2

    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.dias_de_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

    def modificar_contenido_disponible(self):
        pass


class Pro(Familiar, SinConexion):
    precio = 7000
    dispositivos = 6

    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.dias_de_regalo = 15

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self


# PRUEBA
mi_membresia = Gratis("correo@prueba.cl", "123456789")
print(type(mi_membresia))
nueva_membresia = mi_membresia.cambiar_suscripcion(2)
print(type(nueva_membresia))
