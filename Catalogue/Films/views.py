from django.shortcuts import render
from django.http import HttpResponse
from .models import Films
from django.forms import ModelForm, Textarea
from django.contrib import messages


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
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),}

def home(request):
    films = Films.objects.all()
    return render(request,template_name='films.html',context={'films':films})


def film_view(request,id):
        id = int(id)
        film = Films.objects.get(id=id)
        return render(request,template_name='film.html',context={'film':film})

def addFilm(request):
    # on instancie un formulaire
    form = FilmForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = FilmForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            # on prépare un nouveau message
            messages.success(request,'Nouveau contact '+new_contact.name+' '+new_contact.email)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'contact.html', context)


def deleteFilm(request,id):
    film = Films.objects.get(id=id)
    film.delete()
    films = Films.objects.all()
    return render(request,template_name='films.html',context={'films':films})

def updateFilm(request,id):
    form = FilmForm(instance=Films)
    if request.method == "PUT":
        form = FilmForm(request.POST)
        if form.is_valid():
            #
            # 
            # UPDATE 
            # 
            #
            film = Films.objects.get(id=id)
            return render(request,template_name='film.html',context={'film':film})
    film = Films.objects.get(id=id)
    form_view = {'form': form}
    return render(request,template_name='film.html',context={'film':film,'update':True,'form':form_view})