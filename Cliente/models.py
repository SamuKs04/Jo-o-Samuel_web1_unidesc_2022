from django.db import models

# Create your models here.
class Cliente (models.Model):
    dataCadastro = models.DateField(max_length=4)
    


