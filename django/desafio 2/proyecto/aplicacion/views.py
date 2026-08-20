from django.shortcuts import render


# Create your views here.
def aplicacion(request):
    contexto = {"aplicacion": ["Juan", "Pedro", "Maria"]}
    return render(request, "aplicacion/aplicacion.html", contexto)
