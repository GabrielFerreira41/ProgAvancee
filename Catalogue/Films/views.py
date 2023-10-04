from django.shortcuts import render
from django.http import HttpResponse
from .models import Films
from django.forms import ModelForm, Textarea
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django import forms



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
    # on instancie un formulaire
    form = FilmForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        print('okkkkkkkkk')
        # Si oui on récupère les données postées
        form = FilmForm(request.POST,request.FILES)
        print(form)
        # on vérifie la validité du formulaire
        if form.is_valid():
            print('FORMmmmmmmmmmmm')
            newFilm = form.save()
            # on prépare un nouveau message
            messages.success(request,'Nouveau film '+newFilm.title)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            return render(request,template_name='film.html',context={'film':newFilm})
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'addFilm.html', context)


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
    film = Films.objects.get(id=id)

    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)  # Pass the instance to update
        if form.is_valid():
            form.save()  # Save the updated data to the database
            film = Films.objects.get(id=id)
            return render(request,template_name='film.html',context={'film':film,'update':False})
    else:
        form = FilmForm(instance=film)  # Populate the form with existing data

    return render(request,template_name='film.html',context={'film':film,'update':True,'form':form})