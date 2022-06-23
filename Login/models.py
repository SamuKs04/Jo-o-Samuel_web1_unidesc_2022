from django.db import models

# Create your models here.
class Login (models.Model):
    email = models.CharField(max_length=40)
    senha = models.CharField(max_length=40)
    permissao = models.CharField(max_length=40) 
