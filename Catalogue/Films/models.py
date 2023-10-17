from django.db import models
from Realisateur.models import Realisateur
from Acteurs.models import Acteur

class Films(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duree = models.CharField(max_length=250)
    created_date = models.DateField()
    imageName = models.ImageField(upload_to='Films')
    realisateur_name = models.ForeignKey(Realisateur, on_delete=models.CASCADE, related_name="films")
    acteurs = models.ManyToManyField(Acteur)

    def __str__(self):
        return self.title

        