# definir la clase que permita instanciar productos con ecapsulamiento


class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self.stock = 0

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self.stock

    @stock.setter
    def stock(self, stock_nuevo):
        if self.stock_nuevo < 0:
            self.stock = 0
        else:
            self.stock = stock_nuevo

    def __eq__(self, other):
        if self.nombre == other.nombre:
            return True
        else:
            return False

    def __add__(self, other):
        return self.stock + other.stock

    def __sub__(self, other):
        return self.stock - other.stock
