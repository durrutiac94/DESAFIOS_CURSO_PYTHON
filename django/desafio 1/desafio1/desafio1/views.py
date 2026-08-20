
from django.contrib.contenttypes import admin
from django.shortcuts import render

def home(requests):
    return render(requests,'home.html',{})

def about(requests):
    return render(requests,'about.html',{})

def contact(requests):
    return render(requests,'contact.html',{})


    