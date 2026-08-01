# definir la o las clases necesarias para instanciar los distintos tipos de tienda

from abc import ABC, abstractmethod
from producto import Producto


# crear clase padre con abstractmethod
class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self.listado_productos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_delivery(self):
        return self._costo_delivery

    def ingresar_producto(self, nuevo_producto):
        encontrado = False

        for producto_existente in self.listado_productos:
            if producto_existente == nuevo_producto:
                producto_existente.stock = producto_existente + nuevo_producto
                encontrado = True
                break

        if not encontrado:
            self.listado_productos.append(nuevo_producto)

    def listar_productos(self):
        texto = " "
        for producto in self.listado_productos:
            texto += f"nombre:{producto.nombre}, precio:{producto.precio}, stock:{producto.stock}"
        return texto


# crear clase restaurante stock 0
class Restaurante(Tienda):
    def ingresar_producto(self, nuevo_producto):

        if nuevo_producto not in self.listado_productos:
            nuevo_producto.stock = 0
            self.listado_productos.append(nuevo_producto)
        else:
            pass

    def listar_productos(self):
        texto = " "
        for producto in self.listado_productos:
            texto += f"nombre:{producto.nombre}, precio:{producto.precio}"
        return texto

    def realizar_venta(self, nombre_producto, cantidad):
        pass


# crear clase supermercado pocos productos si stock <10  validar stock para venta
class Supermercado(Tienda):

    def listar_productos(self):
        texto = " "
        for producto in self.listado_productos:
            texto += f"nombre:{producto.nombre}, precio:{producto.precio}, stock{producto.stock}"
            if producto.stock < 10:
                texto += f" Pocos productos disponibles"

        return texto

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.listado_productos:
            if producto.nombre == nombre_producto:
                if producto.stock < cantidad:
                    producto.stock = 0
                else:
                    producto.stock -= cantidad
                break


class Farmacia(Tienda):
    def listar_productos(self):
        texto = " "
        for producto in self.listado_productos:
            texto += f"nombre:{producto.nombre}, precio:{producto.precio}"
            if producto.precio > 15000:
                texto += f" Envio gratis al solicitar este producto"

        return texto

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return

        for producto in self.listado_productos:
            if producto.nombre == nombre_producto:
                if producto.stock < cantidad:
                    producto.stock = 0
                else:
                    producto.stock -= cantidad
                break
