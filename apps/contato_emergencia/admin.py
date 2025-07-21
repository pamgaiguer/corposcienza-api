from django.contrib import admin
from .models import ContatoEmergencia

@admin.register(ContatoEmergencia)
class ContatoEmergenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome', 'telefone')
    list_filter = ('nome',) 