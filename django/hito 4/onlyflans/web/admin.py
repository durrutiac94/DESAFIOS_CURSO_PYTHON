from django.contrib import admin

# importar modelos
from . import models

# Register your models here.
admin.site.register(models.Flan)
admin.site.register(models.ContactForm)
