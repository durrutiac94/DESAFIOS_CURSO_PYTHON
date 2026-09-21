from django.contrib import admin
from .models import Inmueble, Usuario, Region, Comuna, Solicitud

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Solicitud)
