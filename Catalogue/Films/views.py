from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Films
from django.forms import ModelForm, Textarea

class FilmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilmForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom "
        self.fields['firstname'].label = "Prenom"
        self.fields['email'].label = "mél"
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


def contact(request):
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