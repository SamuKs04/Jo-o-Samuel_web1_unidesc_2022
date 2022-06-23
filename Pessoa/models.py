from optparse import BadOptionError
from types import CellType
from django.db import models

# Create your models here.
class Pessoa (models.Model):
    matricula = models.IntegerField(max_length=11)
    telefone = models.IntegerField(max_length=13)
    cep_pes = models.IntegerField(max_length=11)
    rua_pes = models.CharField(max_length=50)
    bairro_pes = models.CharField(max_length=30)
    cidade_pes  = models.CharField(max_length=30)
    uf_pes  = models.CharField(max_length=2)