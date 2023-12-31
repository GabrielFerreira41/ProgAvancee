from django.db import models

class Realisateur(models.Model):
    prenom = models.CharField(max_length=250)
    nom = models.CharField(max_length=250)
    age = models.IntegerField()
    description = models.TextField()
    imageName = models.ImageField(upload_to='Realisateurs')


    def __str__(self):
        return self.prenom + ' ' + self.nom