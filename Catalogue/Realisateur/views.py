from django.shortcuts import render

from Films.models import Films
from .models import Realisateur
from django.contrib import messages
from django import forms
from django.http import Http404
from django.contrib.auth.decorators import login_required



class RealisateurForm(forms.ModelForm):
    class Meta:
        model = Realisateur
        fields = ('prenom', 'nom', 'age', 'description', 'imageName')
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'imageName': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

@login_required(login_url='/login')
def addRealisateur(request):
    form = RealisateurForm()

    if request.method == "POST":
        form = RealisateurForm(request.POST, request.FILES)

        if form.is_valid():
            newRealisateur = form.save()
            messages.success(request, 'Nouveau Realisateur ' + newRealisateur.prenom + newRealisateur.nom)
            return render(request, template_name='realisateur.html', context={'realisateur': newRealisateur})

    context = {'form': form}
    return render(request, 'addRealisateur.html', context)



def home(request):
    realisateur = Realisateur.objects.all()
    return render(request,template_name='realisateurs.html',context={'realisateurs':realisateur})


def realisateur_view(request,id):
    id = int(id)
    realisateur = Realisateur.objects.get(id=id)
    films = Films.objects.filter(realisateur_name=realisateur)
    return render(request,template_name='realisateur.html',context={'realisateur':realisateur,'films':films})

@login_required(login_url='/login')
def deleteRealisateur(request,id):
    realisateur = Realisateur.objects.get(id=id)
    realisateur.delete()
    realisateurs = Realisateur.objects.all()
    return render(request,template_name='realisateurs.html',context={'realisateurs':realisateurs})

@login_required(login_url='/login')
def updateRealisateur(request, id):
    try:
        realisateur = Realisateur.objects.get(id=id)
    except Realisateur.DoesNotExist:
        raise Http404("Realisateur non trouvé")

    if request.method == "POST":
        form = RealisateurForm(request.POST, request.FILES, instance=realisateur)
        if form.is_valid():
            form.save()
            new_image = request.FILES.get('imageName', None)
            if new_image:
                realisateur.imageName = new_image
                realisateur.save()
            realisateur = Realisateur.objects.get(id=id)
            films = Films.objects.filter(realisateur_name=realisateur)

            return render(request, template_name='realisateur.html', context={'realisateur': realisateur, 'update': False,'films':films})
    else:
        form = RealisateurForm(instance=realisateur)
    return render(request, template_name='realisateur.html', context={'realisateur': realisateur, 'update': True, 'form': form})

