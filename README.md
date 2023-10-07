# Programmation Avancée


### Groupe

    Gabriel Ferreira
    Léo Bouffard

### Temps
    4 séances

### Sujet
    Ce projet Django consiste à gérer une collection de Films, Séries ou Jeux Vidéos incluant leur année de
    sortie, leur titre, réalisateur (ou Studio) et dʼautres informations de votre choix.
    
    Etape 0 (une seule table pour commencer):
    
        - création du Projet (mis en place urls, settings, etc.)
        - création de l'application
        - création du modèle avec une unique table Film contenant le réalisateur + migration 0001
        - création des vues et des templates associées pour le CRUD des films (héritage de templates)
    
    Etape 1: mise en place d'une relation 1-N
        
        - modification du modèle avec une nouvelle table Réalisateur associée à Film + migration 0002
        - création des vues associés pour le CRUD sur cette table
        - création des templates associés
    
    Etape 2: mise en place d'une relation N-N
    
        - modification du modèle avec une nouvelle table Acteur associée à Film + migration
        - L'ajout des acteurs (et éventuellement du réalisateur) en BD devra se faire uniquement via le formulaire de création d'un film.
