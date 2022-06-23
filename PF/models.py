from django.db import models

# Create your models here.
class PF (models.Model):
    cpf_pf = models.IntegerField(max_length=11)
    rg_pf = models.IntegerField(max_length=7)
    nome_pf = models.CharField(max_length=30)
    sexo_pf = models.CharField(max_length=20)
    dataNasc_pf = models.DateField(max_length=10)

