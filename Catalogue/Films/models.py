from django.db import models
from Realisateur.models import Realisateur
from datetime import datetime, timedelta, date
from django.utils.html import format_html



class Films(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duree = models.CharField(max_length=250)
    created_date = models.DateField()
    imageName = models.ImageField(upload_to='')  # Utilisez ImageField au lieu de FileField
    realisateur_name = models.ForeignKey(Realisateur, on_delete=models.CASCADE, related_name="films")

    def __str__(self):
        return self.title

        