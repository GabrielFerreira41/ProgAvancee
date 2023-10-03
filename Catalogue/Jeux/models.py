from django.db import models
from datetime import datetime, timedelta, date
from django.utils.html import format_html


class Editeur(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()

class Jeux(models.Model):
        title = models.CharField(max_length=250)
        description = models.TextField()
        created_date = models.DateField()
        imageName = models.CharField(max_length=250)
        editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, related_name="jeux")

        def __str__(self):
            return self.name
        