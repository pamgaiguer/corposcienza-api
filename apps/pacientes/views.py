from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente, Endereco, ContatoEmergencia, Financeiro
from .serializers import (
    PacienteSerializer,
    EnderecoSerializer,
    ContatoEmergenciaSerializer,
    FinanceiroSerializer
)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatoEmergenciaViewSet(viewsets.ModelViewSet):
    queryset = ContatoEmergencia.objects.all()
    serializer_class = ContatoEmergenciaSerializer

class FinanceiroViewSet(viewsets.ModelViewSet):
    queryset = Financeiro.objects.all()
    serializer_class = FinanceiroSerializer
