from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    contexto = {
        "productos": [
            models.Producto("flan1", "descripcion"),
            models.Producto("flan2", "descripcion"),
            models.Producto("flan3", "descripcion"),
            models.Producto("flan4", "descripcion"),
            models.Producto("flan5", "descripcion"),
            models.Producto("flan6", "descripcion"),
        ]
    }
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html")


def welcome(request):
    return render(request, "welcome.html")
