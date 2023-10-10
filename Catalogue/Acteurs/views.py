from django.shortcuts import render
from .models import Acteur
from django.contrib import messages
from django import forms
from django.http import Http404


class ActeurForm(forms.ModelForm):
    class Meta:
        model = Acteur
        fields = '__all__'

def addActeur(request):
    form = ActeurForm()

    if request.method == "POST":
        form = ActeurForm(request.POST, request.FILES)

        if form.is_valid():
            newActeur = form.save()
            messages.success(request, 'Nouveau Acteur ' + newActeur.prenom + newActeur.nom)
            return render(request, template_name='acteur.html', context={'acteur': newActeur})

    context = {'form': form}
    return render(request, 'addActeur.html', context)



def homeActeurs(request):
    acteurs = Acteur.objects.all()
    return render(request,template_name='acteurs.html',context={'acteurs':acteurs})


def acteurView(request,id):
    id = int(id)
    acteur = Acteur.objects.get(id=id)
    return render(request,template_name='acteur.html',context={'acteur':acteur})

def deleteActeur(request,id):
    acteur = Acteur.objects.get(id=id)
    acteur.delete()
    acteurs = Acteur.objects.all()
    return render(request,template_name='acteurs.html',context={'acteurs':acteurs})


def updateActeur(request, id):
    try:
        acteur = Acteur.objects.get(id=id)
    except Acteur.DoesNotExist:
        raise Http404("Acteur non trouvé")

    if request.method == "POST":
        form = ActeurForm(request.POST, request.FILES, instance=acteur)
        if form.is_valid():
            form.save()
            new_image = request.FILES.get('imageName', None)
            if new_image:
                acteur.imageName = new_image
                acteur.save()
            acteur = Acteur.objects.get(id=id)
            return render(request, template_name='acteur.html', context={'acteur': acteur, 'update': False})
    else:
        form = ActeurForm(instance=acteur)
    return render(request, template_name='acteur.html', context={'acteur': acteur, 'update': True, 'form': form})

