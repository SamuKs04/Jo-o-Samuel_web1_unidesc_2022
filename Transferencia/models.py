from django.db import models

# Create your models here.
class Transferencia (models.Model):
    tipo = models.CharField(max_length=20) 
    identificacao = models.IntegerField(max_length=20)
