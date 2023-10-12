from django.core.urlresolvers import resolve
from django.test import TestCase
from Films.views import home


class HomePageTest(TestCase):
'''
Test unitaire de la page accueil sur la racine du projet
On vérifie que la méthode home() est bien invoquée sur /
'''
    def test_root_url_resolves_to_home_view(self):
      found = resolve('Films/')
      self.assertEqual(found.func, home)