from django.db import models

# Create your models here.
class Boleto (models.Model):
    cod_cliente = models.IntegerField(max_length=20)
    nome_cliente = models.CharField(max_length=20)
