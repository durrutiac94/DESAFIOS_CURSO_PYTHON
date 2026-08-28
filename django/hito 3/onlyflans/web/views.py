from django.shortcuts import render, redirect
from . import models
from . import forms


# Create your views here.
def indice(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=False)}
    return render(request, "index.html", contexto)


def bienvenido(request):
    contexto = {"productos": models.Flan.objects.filter(is_private=True)}
    return render(request, "welcome.html", contexto)


def acerca(request):
    return render(request, "about.html")


def contacto(request):
    if request.method == "POST":
        print(request.POST)
        form = forms.ContactFormForm(request.POST)
        if form.is_valid():
            # guardar la respuesta del usuario en la base de datos
            """
            INSERT INTO ContactForm
            VALUES(...,...,...);
            """
            models.ContactForm.objects.create(**form.cleaned_data)

            return redirect("exito")

    elif request.method == "GET":
        form = forms.ContactFormForm()
    contexto = {"form": form}
    return render(request, "contactus.html", contexto)


def exito(request):
    contexto = {}
    return render(request, "success.html", contexto)
