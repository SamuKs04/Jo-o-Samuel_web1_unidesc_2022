from django.db import models

# Create your models here.
class PJ (models.Model):
    cnpj = models.IntegerField(max_length=20)
    razao = models.CharField(max_length=30)
    representante = models.CharField(max_length=30)
