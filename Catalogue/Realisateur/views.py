from django.shortcuts import render
from .models import Realisateur
from django.contrib import messages
from django import forms
from django.http import Http404


class RealisateurForm(forms.ModelForm):
    class Meta:
        model = Realisateur
        fields = '__all__'

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
    return render(request,template_name='realisateur.html',context={'realisateur':realisateur})

def deleteRealisateur(request,id):
    realisateur = Realisateur.objects.get(id=id)
    realisateur.delete()
    realisateurs = Realisateur.objects.all()
    return render(request,template_name='realisateurs.html',context={'realisateurs':realisateurs})


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
            return render(request, template_name='realisateur.html', context={'realisateur': realisateur, 'update': False})
    else:
        form = RealisateurForm(instance=realisateur)
    return render(request, template_name='realisateur.html', context={'realisateur': realisateur, 'update': True, 'form': form})

