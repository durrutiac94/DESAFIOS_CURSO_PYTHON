from django.shortcuts import render
from . import models
from django.templatetags.static import static


# Create your views here.
def indice(request):
    contexto = {
        "productos": [
            models.Producto("flan1", "descripcion", static("images.jfif")),
            models.Producto("flan2", "descripcion", static("images (1).jfif")),
            models.Producto("flan3", "descripcion", static("images (2).jfif")),
            models.Producto("flan4", "descripcion", static("images (3).jfif")),
            models.Producto("flan5", "descripcion", static("images (4).jfif")),
            models.Producto("flan6", "descripcion", static("images (5).jfif")),
        ]
    }
    return render(request, "index.html", contexto)


def acerca(request):
    return render(request, "about.html")


def bienvenido(request):
    return render(request, "welcome.html")
