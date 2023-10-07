from django.shortcuts import render
from django.http import HttpResponse
from .models import Realisateur
from django.forms import ModelForm, Textarea
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404



def addRealisateur(request):
    ...


def home(request):
    realisateur = Realisateur.objects.all()
    return render(request,template_name='realisateurs.html',context={'realisateurs':realisateur})


def realisateur_view(request,id):
    id = int(id)
    realisateur = Realisateur.objects.get(id=id)
    return render(request,template_name='realisateur.html',context={'realisateur':realisateur})

def deleteRealisateur(request,id):
    ...


def updateRealisateur(request, id):
    ...


