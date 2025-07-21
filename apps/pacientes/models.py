from django.db import models
from apps.endereco.models import Endereco
from apps.contato_emergencia.models import ContatoEmergencia

class Paciente(models.Model):
    # ID padrão do Django já atua como número de prontuário
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    contato_emergencia = models.ForeignKey(ContatoEmergencia, on_delete=models.SET_NULL, null=True)
    
    SEXO_BIOLOGICO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo_biologico = models.CharField(max_length=1, choices=SEXO_BIOLOGICO_CHOICES)
    
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    estado_civil = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    possui_convenio_medico = models.BooleanField(default=False)
    convenio_nome = models.CharField(max_length=100, blank=True, null=True)
    numero_carteirinha = models.CharField(max_length=50, blank=True, null=True)
    validade_carteirinha = models.CharField(max_length=7, blank=True, null=True)  # mm/aaaa

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Financeiro(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name="financeiro")

    responsavel_eh_paciente = models.BooleanField(default=True)

    nome_responsavel = models.CharField(max_length=255)
    cpf_responsavel = models.CharField(max_length=14)
    telefone_responsavel = models.CharField(max_length=20)
    email_responsavel = models.EmailField()

    # Endereço de cobrança (opcional)
    cep = models.CharField(max_length=9, blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)

    FORMA_PAGAMENTO_CHOICES = [
        ('cartao', 'Cartão'),
        ('boleto', 'Boleto'),
        ('pix', 'PIX'),
        ('dinheiro', 'Dinheiro'),
        ('outro', 'Outro'),
    ]
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES)

    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Financeiro de {self.paciente.nome}"