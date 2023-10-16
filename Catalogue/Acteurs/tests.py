from django.test import TestCase
from Acteurs.models import Acteur
# Create your tests here.

class ActeurTestCase(TestCase):
        Acteur.objects.create()
        Acteur.objects.create()

    
