from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Inmueble
from . import models
from django.shortcuts import get_object_or_404
from django.db.models import Count


# Create your views here.
def index(request):
    inmuebles = models.Inmueble.objects.all()
    region_id = request.GET.get("region")
    if region_id:
        inmuebles = inmuebles.filter(comuna__region=region_id)

    comuna_id = request.GET.get("comuna")
    if comuna_id:
        inmuebles = inmuebles.filter(comuna=comuna_id)
    regiones = models.Region.objects.annotate(total_inmuebles=Count("comuna__inmueble"))
    comunas = models.Comuna.objects.annotate(total_inmuebles=Count("inmueble"))
    contexto = {
        "inmuebles": inmuebles,
        "regiones": regiones,
        "comunas": comunas,
    }
    return render(request, "index.html", contexto)


@login_required
def dashboard(request):
    inmuebles = models.Inmueble.objects.filter(dueno=request.user)
    contexto = {"inmuebles": inmuebles}
    return render(request, "dashboard.html", contexto)


def registro(request):
    if request.user.is_authenticated:
        return redirect("indice")

    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically logs the user in after registration
            return redirect("indice")  # Change 'home' to your desired redirect URL name
    else:
        form = forms.CustomUserCreationForm

    return render(request, "registration/register.html", {"form": form})


def actualizar_perfil(request):
    if request.method == "POST":
        form = forms.ActualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = forms.ActualizarUsuarioForm(instance=request.user)
        return render(request, "actualizar_perfil.html", {"form": form})


def agregar_inmueble(request):
    if request.method == "POST":
        form = forms.AgregarInmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.dueno = request.user
            inmueble.save()
            return redirect("dashboard")

    else:
        form = forms.AgregarInmuebleForm()
        return render(request, "agregar_inmueble.html", {"form": form})


def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(klass=models.Inmueble, id=id)
    if request.method == "POST":
        form = forms.ActualizarInmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = forms.ActualizarInmuebleForm(instance=inmueble)

    return render(request, "actualizar_inmueble.html", {"form": form})


def borrar_inmueble(request, id):
    inmueble = get_object_or_404(klass=models.Inmueble, id=id)
    inmueble.delete()
    return redirect("dashboard")
