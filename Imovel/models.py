from distutils.command.upload import upload
from types import NoneType
from django.db import models

# Create your models here.
class Imovel (models.Model):
    matricula_imo = models.IntegerField(max_length=8)
    rua_imo = models.CharField(max_length=2)
    cep_imo = models.CharField(max_length=9)
    bairro_imo = models.CharField(max_length=50)
    cidade_imo = models.CharField(max_length=30)
    uf_imo = models.CharField(max_length=2)
    tamanho_imo = models.IntegerField(max_length=100)
    comodos_imo = models.CharField(max_length=50)
    garagem_imo = models.CharField(max_length=50)
    valor_imo = models.IntegerField(max_length=100)
    tipo_imo  = models.CharField(max_length=50)
    status_imo  = models.CharField(max_length=50)



