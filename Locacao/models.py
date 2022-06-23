from django.db import models

# Create your models here.
class Locacao (models.Model):
    data_deso = models.DateField(max_length=10)
    periodo = models.DateField(max_length=10)
    garantia = models.CharField(max_length=10)
    fiador = models.CharField(max_length=30)
