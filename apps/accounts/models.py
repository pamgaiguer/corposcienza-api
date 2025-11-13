from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome = models.CharField("Nome completo", max_length=150, blank=True)
    is_equipe = models.BooleanField("É da equipe?", default=False)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome or self.username
