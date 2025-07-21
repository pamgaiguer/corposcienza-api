from django.db import models

class ContatoEmergencia(models.Model):
    # paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name="contato_emergencia")
    
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    email = models.EmailField()
    
    estado_civil = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    # Endereço (opcional, pode ser o mesmo do paciente)
    # cep = models.CharField(max_length=9, blank=True, null=True)
    # rua = models.CharField(max_length=255, blank=True, null=True)
    # numero = models.CharField(max_length=20, blank=True, null=True)
    # complemento = models.CharField(max_length=100, blank=True, null=True)
    # bairro = models.CharField(max_length=100, blank=True, null=True)
    # cidade = models.CharField(max_length=100, blank=True, null=True)
    # estado = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.telefone})"