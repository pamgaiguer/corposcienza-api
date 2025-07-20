# pacientes/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PacienteViewSet,
    EnderecoViewSet,
    ContatoEmergenciaViewSet,
    FinanceiroViewSet,
)

# Criando o roteador padrão e registrando os ViewSets
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'contatos-emergencia', ContatoEmergenciaViewSet)
router.register(r'financeiro', FinanceiroViewSet)

# Incluindo as URLs do roteador
urlpatterns = [
    path('', include(router.urls)),
]
