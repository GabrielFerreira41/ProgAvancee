from django.db import models
from datetime import datetime, timedelta, date
from django.utils.html import format_html
from Films.models import Realisateur

class Series(models.Model):
        title = models.CharField(max_length=250)
        description = models.TextField()
        created_date = models.DateField()
        imageName = models.CharField(max_length=250)
        realisateur_name = models.ForeignKey(Realisateur, on_delete=models.CASCADE, related_name="series")

        def __str__(self):
            return self.name
        