from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # exemplo: adicionar campo extra
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
