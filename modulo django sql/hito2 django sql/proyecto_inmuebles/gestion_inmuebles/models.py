from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Region(models.Model):
    nombre = models.CharField(max_length=200)


class Comuna(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Usuario(AbstractUser):
    rut = models.CharField(max_length=13, unique=True, verbose_name="RUT")
    direccion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    telefono = models.CharField(
        max_length=12,
        blank=True,
        null=True,
    )
    TIPO_USUARIO = [("arrendador", "arrendador"), ("arrendatario", "arrendatario")]
    tipo_usuario_por_defecto = models.CharField(choices=TIPO_USUARIO)


class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    TIPO_INMUEBLE = [
        ("casa", "casa"),
        ("departamento", "departamento"),
        ("parcela", "parcela"),
    ]
    tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLE)
    dueno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    aceptado = models.BooleanField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aceptacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Solicitudes"


"""from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta():
        verbose_name_plural = "Regiones"



class Comuna(models.Model):
    nombre = models.CharField(max_length=250)
    region = models.ForeignKey(Region, verbose_name="Region", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rut = models.CharField(max_length=13, unique=True, verbose_name="RUT")
    direccion = models.CharField(max_length=300, blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=12, blank=True, null=True, verbose_name="Teléfono")
    TIPO_USUARIO = [
        ("arrendador", "Arrendador"),
        ("arrendatario","Arrendatario")
        ]
    tipo_usuario_defecto = models.CharField(max_length=100, choices=TIPO_USUARIO, verbose_name="Por defecto entrar como:")


class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")
    m2_construidos = models.PositiveIntegerField()
    m2_totales = models.PositiveIntegerField()
    estacionamientos = models.PositiveIntegerField()
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField(verbose_name="Baños:")
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    TIPO_INMUEBLE = [
        ("casa","Casa"),
        ("departamento","Departamento"),
        ("parcela", "Parcela")
    ]
    tipo_inmueble = models.CharField(max_length=50, choices=TIPO_INMUEBLE, verbose_name="Tipo de Inmueble")
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)], verbose_name='Precio Mensual')
    dueno = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="dueño:")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación:")
    ultima_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última modificación:")

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField(default="Hola, estoy intentando contactarte ...")
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    aprobada = models.BooleanField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_aceptacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Solicitudes"""
