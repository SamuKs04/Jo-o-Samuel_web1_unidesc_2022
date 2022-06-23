from django.db import models

# Create your models here.
class Cheque (models.Model):
    financeiro = models.IntegerField(max_length=30)
    nome_cliente = models.CharField(max_length=30)
    numero_cheque = models.IntegerField(max_length=20)
    dataAb = models.DateField(max_length=10)

