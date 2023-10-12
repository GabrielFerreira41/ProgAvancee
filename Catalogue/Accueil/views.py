from django.shortcuts import render
from django.shortcuts import render
from Films.models import Films
from Realisateur.models import Realisateur
from Acteurs.models import Acteur
from django.db.models import Q

def accueil(request):
    return render(request,template_name='Accueil.html')

def search(request):
    query = request.GET.get('query', '')
    results = []
    print('COUCOUCCCCC')
    print(query)
    if query:
        # Recherche les acteurs, films et réalisateurs dont le nom ou le prénom correspondent à la requête
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



