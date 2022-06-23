from django.db import models

# Create your models here.
class CLiAviso (models.Model):
    mensagem = models.CharField(max_length=60)
