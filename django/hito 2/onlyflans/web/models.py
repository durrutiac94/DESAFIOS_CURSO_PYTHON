from django.db import models


# Create your models here.
class Producto:
    def __init__(self, nombre, descripcion, url):
        self.nombre = nombre
        self.descripcion = descripcion
        self.url = url
