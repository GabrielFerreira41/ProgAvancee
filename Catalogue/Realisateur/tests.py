from django.test import TestCase
from .models import Realisateur
from .views import RealisateurForm
from django.core.files.base import ContentFile
from django.contrib.staticfiles import finders
from django.urls import reverse
from django.contrib.auth.models import User

class RealisateurFormTest(TestCase):
    def test_valid_form(self):
        self.superuser = User.objects.create_superuser('gabriel', '', 'root')
        self.client.login(username='gabriel', password='root')
        image_path = finders.find('Realisateurs/nono_tm4ickv.webp')
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_name = 'Realisateurs/nono_tm4ickv.webp'

        image_file = ContentFile(image_data, name=image_name)

        data = {
            'prenom': 'John',
            'nom': 'Doe',
            'age': 30,
            'description': 'Un réalisateur talentueux',
        }

        form = RealisateurForm(data=data, files={'imageName': image_file})

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        self.superuser = User.objects.create_superuser('gabriel', '', 'root')
        self.client.login(username='gabriel', password='root')
        data = {
            'prenom': 'John',
            'nom': 'Doe',
            'age': 'Error',
            'description': 'Un réalisateur talentueux',
        }
        form = RealisateurForm(data=data)
        self.assertFalse(form.is_valid())

class RealisateurViewTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('gabriel', '', 'root')
        self.realisateur = Realisateur.objects.create(prenom='John', nom='Doe', age=30, description='Un réalisateur talentueux', imageName='Realisateurs/JohnDoe_xTsxhlj.jpeg')

    def test_homeRealisateurs_view(self):
        self.client.login(username='gabriel', password='root')
        response = self.client.get(reverse('acteurs'))
        response = self.client.get(reverse('realisateurs'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['realisateurs'], [self.realisateur])

    def test_realisateur_view(self):
        self.client.login(username='gabriel', password='root')
        response = self.client.get(reverse('acteurs'))
        response = self.client.get(reverse('Realisateur_view', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['realisateur'], self.realisateur)

    def test_add_realisateur(self):
        self.client.login(username='gabriel', password='root')
        response = self.client.get(reverse('acteurs'))
        response = self.client.get(reverse('addRealisateur'))
        self.assertEqual(response.status_code, 200)

        image_path = finders.find('Realisateurs/nono_tm4ickv.webp')
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_name = 'Realisateurs/nono_tm4ickv.webp'

        image_file = ContentFile(image_data, name=image_name)

        data = {
            'nom': 'Doe',
            'prenom': 'John',
            'age': 40,
            'description': 'réalisateur'
        }

        form = RealisateurForm(data=data, files={'imageName': image_file})
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('addRealisateur'), data, format='multipart')
        self.assertEqual(response.status_code, 200)

    def test_updateRealisateur_view(self):
        self.client.login(username='gabriel', password='root')
        response = self.client.get(reverse('acteurs'))
        response = self.client.get(reverse('updateRealisateur', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)

    def test_deleteRealisateur_view(self):
        self.client.login(username='gabriel', password='root')
        response = self.client.get(reverse('acteurs'))
        response = self.client.get(reverse('deleteRealisateur', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)
