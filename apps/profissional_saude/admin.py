from django.contrib import admin
from .models import ProfissionalSaude
from apps.endereco.models import Endereco
from apps.contato_emergencia.models import ContatoEmergencia

@admin.register(ProfissionalSaude)
class ProfissionalSaudeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'especialidade', 'numero_registro')
    search_fields = ('nome', 'cpf', 'especialidade', 'numero_registro')
    list_filter = ('especialidade',)
    autocomplete_fields = ('endereco', 'contato_emergencia')
