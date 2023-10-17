from django.contrib import admin
from .models import Realisateur

@admin.register(Realisateur)
class RealisateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'age')
    search_fields = ('prenom', 'nom')
