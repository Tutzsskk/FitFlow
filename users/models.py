from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Masculino'),
        (GENDER_FEMALE, 'Feminino'),
    ]

    email = models.EmailField(unique=True)
    height = models.FloatField(null=True, blank=True, help_text="Altura em metros (ex: 1.75)")
    weight = models.FloatField(null=True, blank=True, help_text="Peso em kg (ex: 72.5)")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username ainda é obrigatório, mas login será com email

    def __str__(self):
        return self.email
