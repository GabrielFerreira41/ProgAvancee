from django.shortcuts import render
from django.shortcuts import render
from Films.models import Films
from Realisateur.models import Realisateur
from Acteurs.models import Acteur
from django.db.models import Q
from django import forms




def accueil(request):
    return render(request,template_name='Accueil.html')

def search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        acteurs = Acteur.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))
        films = Films.objects.filter(title__icontains=query)
        realisateurs = Realisateur.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))

        results = {
            'acteurs': acteurs,
            'films': films,
            'realisateurs': realisateurs,
        }

        print(results)

    return render(request, 'Search.html', {'results': results, 'query': query})



