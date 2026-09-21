from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Region(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}{self.id}"


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


class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=200)


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
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    dueno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    texto = models.TextField()
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    aceptado = models.BooleanField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aceptacion = models.DateTimeField(auto_now=True)
