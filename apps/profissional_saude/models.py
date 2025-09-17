from django.db import models
from apps.endereco.models import Endereco
from apps.contato_emergencia.models import ContatoEmergencia

class ProfissionalSaude(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=255)


    SEXO_BIOLOGICO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo_biologico = models.CharField(max_length=1, choices=SEXO_BIOLOGICO_CHOICES)
    
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    especialidade = models.CharField(max_length=100)
    numero_registro = models.CharField(max_length=50)


    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    contato_emergencia = models.ForeignKey(ContatoEmergencia, on_delete=models.SET_NULL, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='profissional')
    contato_emergencia = models.OneToOneField(ContatoEmergencia, on_delete=models.CASCADE, related_name='profissional')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"
