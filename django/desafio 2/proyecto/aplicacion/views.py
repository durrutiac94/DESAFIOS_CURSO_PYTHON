from django.shortcuts import render


# Create your views here.
def aplicacion(request):
    contexto = {
        "aplicacion": [
            "Juan",
            "Pedro",
            "Maria",
            "Daniel",
            "Claudia",
            "Katherine",
            "Eric",
        ]
    }
    return render(request, "aplicacion/aplicacion.html", contexto)
