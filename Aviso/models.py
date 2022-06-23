from django.db import models

# Create your models here.
class Aviso (models.Model):
    matricula = models.IntegerField(max_length=30)
    assunto = models.CharField(max_length=10)
    data = models.DateField(max_length=10)
