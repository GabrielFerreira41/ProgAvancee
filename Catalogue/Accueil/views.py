from django.shortcuts import render

def accueil(request):
    return render(request,template_name='Accueil.html')
