from django.db import models

# Create your models here.
class Corretor (models.Model):
    comissao = models.IntegerField(max_length=20)
    id_corretor = models.IntegerField(max_length=20)

