from django.test import TestCase
from django.urls import reverse
from Acteurs.models import Acteur
from django.middleware import csrf
from Realisateur.models import Realisateur
from .models import Films
from .views import FilmForm
from django.core.files.base import ContentFile
from django.contrib.staticfiles import finders
from django.contrib.auth.models import User

class FilmsAppTests(TestCase):
      
    def setUp(self):
        self.superuser = User.objects.create_superuser('gabriel', '', 'root')
        self.client.login(username='gabriel', password='root')
        self.realisateur = Realisateur.objects.create(nom='Nolan', prenom='Christoper', age=54)
        self.film = Films.objects.create(title='Test Film', description='Test Description', created_date='2023-10-17', imageName='Films/ww_fkP07rU.jpeg', realisateur_name=Realisateur.objects.get(id=1))
        self.acteur = Acteur.objects.create(nom='Doe', prenom='John', age=40)

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_add_film_view(self):
        response = self.client.get(reverse('addFilm'))
        self.assertEqual(response.status_code, 200)


        image_path = finders.find('Films/ww_fkP07rU.jpeg')
        with open(image_path, 'rb') as f:
                image_data = f.read()
        image_name = 'Films/ww_fkP07rU.jpeg'

        image_file = ContentFile(image_data, name=image_name)

        data = {
            'title': 'Nouveau Film',
            'description': 'Description du nouveau film',
            'created_date': '2023-10-17',
            'realisateur_name': self.realisateur.id,
            'acteurs': [self.acteur.id],
        }

        form = FilmForm(data=data,files={'imageName': image_file})
        self.assertTrue(form.is_valid())
        
    def test_home_view(self):
        response = self.client.get(reverse('films'))
        self.assertEqual(response.status_code, 200)

    def test_film_view(self):
        response = self.client.get(reverse('film_view', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_film_view(self):
        response = self.client.get(reverse('deleteFilm', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_film_view(self):
        response = self.client.get(reverse('updateFilm', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
    #     response = self.client.get(reverse('updateFilm', args=[self.film.id]))
    #     self.assertEqual(response.status_code, 200)

    #     # Simulez la modification des données du film
    #     image_path = finders.find('Films/ww_fkP07rU.jpeg')
    #     with open(image_path, 'rb') as f:
    #         image_data = f.read()
    #     image_name = 'Films/ww_fkP07rU.jpeg'
    #     image_file = ContentFile(image_data, name=image_name)

    #     data = {
    #         'title': 'Nouveau Film',
    #         'description': 'Description du nouveau film',
    #         'created_date': '2023-10-17',
    #         'realisateur_name': self.realisateur.id,
    #         'acteurs': [self.acteur.id],
    #     }
        
    #     form = FilmForm(data=data, files={'imageName': image_file})
    #     self.assertTrue(form.is_valid())

    #     response = self.client.post(reverse('updateFilm', args=[self.film.id]), data)

    #     self.assertContains(response, 'Un film avec ce nom existe déjà.')
