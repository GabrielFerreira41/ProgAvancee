from django.contrib import admin
from .models import Acteur

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'age', 'description')
    search_fields = ('prenom', 'nom')
    list_filter = ('age',)

    fieldsets = (
        (None, {
            'fields': ('prenom', 'nom', 'age', 'description', 'imageName')
        }),
    )

    ordering = ('nom', 'prenom')
