from django.db import models

# Create your models here.
class Deposito (models.Model):
    id_deposito = models.IntegerField(max_length=20)
