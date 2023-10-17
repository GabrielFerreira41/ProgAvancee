from django.test import TestCase
from django.urls import reverse
from .models import Realisateur

class RealisateurViewTests(TestCase):

    def setUp(self):
        # Crée un réalisateur de test pour les tests
        self.realisateur = Realisateur.objects.create(
            prenom="John",
            nom="Doe",
            age=40,
            description="Un réalisateur de test",
            imageName='Realisateurs/nono_tm4ickv.webp'
        )

    def test_home_view(self):
        response = self.client.get(reverse('realisateurs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realisateurs.html')

    def test_realisateur_view(self):
        response = self.client.get(reverse('Realisateur_view', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realisateur.html')

    def test_add_realisateur_view(self):
        response = self.client.get(reverse('addRealisateur'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addRealisateur.html')

    def test_delete_realisateur_view(self):
        response = self.client.get(reverse('deleteRealisateur', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realisateurs.html')

    def test_update_realisateur_view(self):
        response = self.client.get(reverse('updateRealisateur', args=[self.realisateur.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realisateur.html')
