from django.test import TestCase
from .models import Acteur
from .views import ActeurForm
from django.core.files.base import ContentFile
from django.contrib.staticfiles import finders
from django.urls import reverse


class ActeurFormTest(TestCase):
    def test_valid_form(self):
        image_path = finders.find('Acteurs/Chrispratt.jpeg')
        with open(image_path, 'rb') as f:
                image_data = f.read()
        image_name = 'Acteurs/Chrispratt_xTsxhlj.jpeg'

        image_file = ContentFile(image_data, name=image_name)

        data = {
            'prenom': 'John',
            'nom': 'Doe',
            'age': 30,
            'description': 'Un acteur talentueux',
        }

        form = ActeurForm(data=data, files={'imageName': image_file})

        self.assertTrue(form.is_valid())
 

    def test_invalid_form(self):
        data = {
            'prenom': 'John',
            'nom': 'Doe',
            'age': 'Error',
            'description': 'Un acteur talentueux',
        }
        form = ActeurForm(data=data)
        self.assertFalse(form.is_valid())


class ActeurViewTest(TestCase):
    def setUp(self):
        self.acteur = Acteur.objects.create(prenom='John', nom='Doe', age=30, description='Un acteur talentueux', imageName='Acteurs/Chrispratt_xTsxhlj.jpeg',
)

    def test_homeActeurs_view(self):
        response = self.client.get(reverse('acteurs'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['acteurs'], [self.acteur])

    def test_acteurView_view(self):
        response = self.client.get(reverse('acteurView', args=[self.acteur.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['acteur'], self.acteur)

    def test_add_acteur(self):
        response = self.client.get(reverse('addActeur'))
        self.assertEqual(response.status_code, 200)

        # Charger l'image de profil de l'acteur depuis vos fichiers statiques
        image_path = finders.find('Acteurs/Chrispratt_xTsxhlj.jpeg')
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_name = 'Acteurs/Chrispratt_xTsxhlj.jpeg'

        # Créer un objet ContentFile à partir des données de l'image
        image_file = ContentFile(image_data, name=image_name)

        data = {
            'nom': 'Doe',
            'prenom': 'John',
            'age': 40,
            'description':'acteur'
        }

        form = ActeurForm(data=data, files={'imageName': image_file})
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('addActeur'), data, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_updateActeur_view(self):
        response = self.client.get(reverse('updateActeur', args=[self.acteur.id]))
        self.assertEqual(response.status_code, 200)

    def test_deleteActeur_view(self):
        response = self.client.get(reverse('deleteActeur', args=[self.acteur.id]))
        self.assertEqual(response.status_code, 200)

