from django.contrib import admin
from .models import Films

@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'realisateur_name')
    list_filter = ('created_date', 'realisateur_name')
    search_fields = ('title', 'realisateur_name__nom')  # Replace 'nom' with the actual field name in your Realisateur model
    date_hierarchy = 'created_date'

    fieldsets = [
        ('Informations sur le film', {'fields': ['title', 'description', 'duree', 'created_date', 'imageName']}),
        ('Associations', {'fields': ['realisateur_name', 'acteurs']}),
    ]
