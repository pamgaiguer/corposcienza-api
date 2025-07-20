from django.contrib import admin
from .models import Paciente, Endereco, ContatoEmergencia, Financeiro

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email']
    search_fields = ['nome', 'cpf']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'cidade', 'estado']
    search_fields = ['paciente__nome', 'cidade']

@admin.register(ContatoEmergencia)
class ContatoEmergenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'paciente']
    search_fields = ['nome', 'paciente__nome']

@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'nome_responsavel', 'forma_pagamento']
    search_fields = ['paciente__nome', 'nome_responsavel']
