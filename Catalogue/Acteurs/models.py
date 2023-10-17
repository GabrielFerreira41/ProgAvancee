from django.db import models

class Acteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    age = models.IntegerField()
    description = models.TextField()
    imageName = models.ImageField(upload_to='Acteurs')

    def __str__(self):
        return self.prenom + ' ' + self.nom

        