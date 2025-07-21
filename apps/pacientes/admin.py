from django.contrib import admin
from .models import Paciente, Financeiro
from apps.endereco.models import Endereco
from apps.contato_emergencia.models import ContatoEmergencia

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'sexo_biologico')
    search_fields = ('nome', 'cpf')
    list_filter = ('sexo_biologico',)
    autocomplete_fields = ('endereco', 'contato_emergencia')

@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'nome_responsavel', 'forma_pagamento']
    search_fields = ['paciente__nome', 'nome_responsavel']