from rest_framework import serializers
from .models import Paciente, Endereco, ContatoEmergencia, Financeiro

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ContatoEmergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoEmergencia
        fields = '__all__'

class FinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financeiro
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=False)
    contato_emergencia = ContatoEmergenciaSerializer(required=False)
    financeiro = FinanceiroSerializer(required=False)

    class Meta:
        model = Paciente
        fields = '__all__'
