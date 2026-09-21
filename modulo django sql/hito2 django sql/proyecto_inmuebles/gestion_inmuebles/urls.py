from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="indice"),
    path("cuenta/", include("django.contrib.auth.urls")),
    path("cuenta/registro/", views.registro, name="registro"),
]
