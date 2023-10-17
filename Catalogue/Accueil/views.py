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
    query = query.split()
    results = []
    print('COUCOUCCCCC')
    print(query)
    print(len(query))
    if query:
        if len(query)==1:
        # Recherche les acteurs, films et réalisateurs dont le nom ou le prénom correspondent à la requête
            acteurs = Acteur.objects.filter(Q(nom__icontains=query[0]) | Q(prenom__icontains=query[0]))
            films = Films.objects.filter(title__icontains=query[0])
            realisateurs = Realisateur.objects.filter(Q(nom__icontains=query[0]) | Q(prenom__icontains=query[0]))
        else:
            acteurs = Acteur.objects.filter((Q(nom__icontains=query[1]) & Q(prenom__icontains=query[0])) | (Q(nom__icontains=query[0]) & Q(prenom__icontains=query[1])))
            films = Films.objects.filter(title__icontains=' '.join(query))
            realisateurs = Realisateur.objects.filter((Q(nom__icontains=query[0]) & Q(prenom__icontains=query[1])) | (Q(nom__icontains=query[0]) & Q(prenom__icontains=query[1])))


        results = {
            'acteurs': acteurs,
            'films': films,
            'realisateurs': realisateurs,
        }

        print(results)

    return render(request, 'Search.html', {'results': results, 'query': ' '.join(query)})



