from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms


# Create your views here.
def index(request):
    return render(request, "index.html", {})


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
