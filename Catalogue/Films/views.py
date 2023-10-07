from django.shortcuts import render
from django.http import HttpResponse
from .models import Films
from django.forms import ModelForm, Textarea
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404





class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"
        self.fields['created_date'].label = "Date de création"
        self.fields['imageName'].label = "Image"
        self.fields['realisateur_name'].label = "Réalisateur"
        self.fields['description'].label = "Description"

    class Meta:
        model = Films
        fields = ('title', 'description', 'created_date','imageName','realisateur_name')
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),
        }


def addFilm(request):
    form = FilmForm()

    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            try:
                existing_film = Films.objects.get(title=title)
                messages.error(request, 'Un film avec ce nom existe déjà.')
                return render(request, 'addFilm.html', {'form': form})
            except ObjectDoesNotExist:
                newFilm = form.save()
                messages.success(request, 'Nouveau film ' + newFilm.title)
                return render(request, template_name='film.html', context={'film': newFilm})

    context = {'form': form}
    return render(request, 'addFilm.html', context)



def home(request):
    films = Films.objects.all()
    return render(request,template_name='films.html',context={'films':films})


def film_view(request,id):
        id = int(id)
        film = Films.objects.get(id=id)
        return render(request,template_name='film.html',context={'film':film})

def deleteFilm(request,id):
    film = Films.objects.get(id=id)
    film.delete()
    films = Films.objects.all()
    return render(request,template_name='films.html',context={'films':films})


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
                try:
                    existing_film = Films.objects.get(title=new_title)
                    messages.error(request, 'Un film avec ce nom existe déjà.')
                    return render(request, 'film.html', {'film': film, 'update': True, 'form': form})
                except Films.DoesNotExist:
                    pass

            form.save()

            new_image = request.FILES.get('imageName', None)
            if new_image:
                film.imageName = new_image
                film.save()
            film = Films.objects.get(id=id)
            return render(request, template_name='film.html', context={'film': film, 'update': False})
    else:
        form = FilmForm(instance=film)
    return render(request, template_name='film.html', context={'film': film, 'update': True, 'form': form})


