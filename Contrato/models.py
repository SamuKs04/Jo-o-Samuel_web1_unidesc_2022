from django.db import models

# Create your models here.
class Contrato (models.Model):
    dados_cliente = models.CharField (max_length=50)
    dados_corretor = models.CharField (max_length=50)
    descricao_imo = models.CharField (max_length=50)
    valorCont = models.CharField (max_length=50)
    doc = models.CharField (max_length=50)
    clausula = models.CharField (max_length=50)