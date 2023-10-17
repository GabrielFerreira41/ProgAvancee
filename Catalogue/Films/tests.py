from django.test import TestCase
from django.urls import reverse
from Acteurs.models import Acteur
from django.middleware import csrf
from Realisateur.models import Realisateur
from .models import Films
from .views import FilmForm

class FilmsAppTests(TestCase):
      
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    # def test_add_film_view(self):
    #     response = self.client.get(reverse('addFilm'))
    #     self.assertEqual(response.status_code, 200)

    #     # Créez un réalisateur et un acteur
    #     realisateur = Realisateur.objects.create(nom='Nolan', prenom='Christopher', age=54)
    #     acteur = Acteur.objects.create(nom='Doe', prenom='John', age=40)
    #     csrf_token = csrf.get_token(self.client)

    #     # Testez l'ajout d'un nouveau film
    #     data = {
    #         'title': 'New Film',
    #         'description': 'Description of the new film',
    #         'duree': '120',
    #         'created_date': '17/10/2020',
    #         'imageName': 'Films/ww_fkP07rU.jpeg',
    #         'realisateur_name': realisateur.id,
    #         'acteurs':[acteur.id],
    #         'csrfmiddlewaretoken': csrf_token,  # Ajoutez le jeton CSRF
    #     }
    #     form = FilmForm(data)
    #     print(form)
    #     self.assertTrue(form.is_valid())

    #     response = self.client.post(reverse('addFilm'), data)
    #     self.assertEqual(response.status_code, 200)

    #     # Testez l'ajout d'un film avec un titre en double
    #     data['title'] = 'New Film'
    #     response = self.client.post(reverse('addFilm'), data)
    #     self.assertContains(response, 'Un film avec ce nom existe déjà.')
        
    def test_home_view(self):
        response = self.client.get(reverse('films'))
        self.assertEqual(response.status_code, 200)

    def test_film_view(self):
        realisateur = Realisateur.objects.create(nom='Nolan', prenom='Christoper',age=54)
        film = Films.objects.create(title='Test Film', description='Test Description', created_date='2023-10-17',imageName='Films/ww_fkP07rU.jpeg',realisateur_name=Realisateur.objects.get(id=1))
        response = self.client.get(reverse('film_view', args=[film.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_film_view(self):
        realisateur = Realisateur.objects.create(nom='Nolan', prenom='Christoper',age=54)
        film = Films.objects.create(title='Test Film', description='Test Description', created_date='2023-10-17',imageName='Films/ww_fkP07rU.jpeg',realisateur_name=Realisateur.objects.get(id=1))
        response = self.client.get(reverse('deleteFilm', args=[film.id]))
        self.assertEqual(response.status_code, 200)

    # def test_update_film_view(self):
    #     realisateur = Realisateur.objects.create(nom='Nolan', prenom='Christoper',age=54)
    #     film = Films.objects.create(title='Test Film', description='Test Description', created_date='2023-10-17',imageName='Films/ww_fkP07rU.jpeg',realisateur_name=Realisateur.objects.get(id=1))
    #     response = self.client.get(reverse('updateFilm', args=[film.id]))
    #     self.assertEqual(response.status_code, 200)

    #     # Test updating a film with a duplicate title
    #     data = {
    #         'title': 'New Film',
    #         'description': 'Updated Description',
    #         'created_date': '10/10/2020',
    #         'imageName': 'Films/ww_fkP07rU.jpeg',
    #         'realisateur_name': Realisateur.objects.get(id=1),
    #     }
    #     form = FilmForm(data)
    #     self.assertTrue(form.is_valid())

    #     response = self.client.post(reverse('updateFilm', args=[film.id]), data)
    #     self.assertContains(response, 'Un film avec ce nom existe déjà.')
