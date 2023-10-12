from django.shortcuts import render
from django.http import HttpResponse

from Acteurs.models import Acteur
from .models import Films
from django.forms import ModelForm, Textarea
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404





class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ('title', 'description', 'created_date', 'imageName', 'realisateur_name', 'acteurs')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),
            'imageName': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'realisateur_name': forms.Select(attrs={'class': 'form-control'}),
        }
    
    acteurs = forms.ModelMultipleChoiceField(
        queryset=Acteur.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={}),
    )


    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['created_date'].label = "Date de création"
        self.fields['imageName'].label = "Image"
        self.fields['realisateur_name'].label = "Réalisateur"
        self.fields['description'].label = "Description"
        self.fields['acteurs'].label = "Acteurs"



def addFilm(request):
    form = FilmForm()

    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            title = form.cleaned_data['title']
            normalized_title = title.lower()
            
            existing_film = Films.objects.filter(title__iexact=normalized_title).first()
            
            if existing_film:
                errorAddMessage = 'Un film avec ce nom existe déjà.' # Message pour le pop up d'erreur lorsque l'utilisateur choissi un titre de film deja existant
                return render(request, 'addFilm.html', {'form': form,'errorAddMessage':errorAddMessage}) # on oubli pas d'ajouter le message d'erreur
            else:
                new_film = form.save()
                successAddMessage = "Ajout du film '"+ new_film.title +"' reussi" # Message pour le pop up de reussite d'ajout d'un film en BD
                return render(request, template_name='film.html', context={'film': new_film,'successAddMessage':successAddMessage}) # on oubli pas d'ajouter le message de reussite


    context = {'form': form}
    return render(request, 'addFilm.html', context)



def home(request):
    films = Films.objects.all()
    return render(request,template_name='films.html',context={'films':films})


def film_view(request,id):
        id = int(id)
        film = Films.objects.get(id=id)
        acteurs = film.acteurs.all()
        return render(request,template_name='film.html',context={'film':film,'acteurs': acteurs})

def deleteFilm(request,id):
    film = Films.objects.get(id=id)
    film.delete()
    films = Films.objects.all()
    successfulDeleteMessage = "Suppression du film '" +film.title + "' reussi" #message pop up de reussite de suppression du film
    print(successfulDeleteMessage)
    return render(request,template_name='films.html',context={'films':films,'successfulDeleteMessage':successfulDeleteMessage})


def updateFilm(request, id):
    try:
        film = Films.objects.get(id=id)
        filmTitle = film.title
    except Films.DoesNotExist:
        raise Http404("Film non trouvé")

    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            new_title = form.cleaned_data['title']
            if new_title != filmTitle:
                lowerNewTitle = new_title.lower()
                existing_film = Films.objects.filter(title__iexact=lowerNewTitle).first()
                if existing_film:
                    errorUpdateMessage = 'Un film avec ce nom existe déjà.' #Message pour le pop d'erreur lorsque l'utilisateur rentre en nom de film déja existant
                    return render(request, 'film.html', {'form': form,'film': film,'update': True,'errorUpdateMessage':errorUpdateMessage})

            form.save()
            new_image = request.FILES.get('imageName', None)
            if new_image:
                film.imageName = new_image
                film.save()
            film = Films.objects.get(id=id)
            sucessUpdateMessage = 'Mise à jour reussi' # Message pour le pop up de reussite de modification d'un film
            return render(request, template_name='film.html', context={'film': film, 'update': False,'sucessUpdateMessage':sucessUpdateMessage})
    else:
        form = FilmForm(instance=film)
    return render(request, template_name='film.html', context={'film': film, 'update': True, 'form': form})


