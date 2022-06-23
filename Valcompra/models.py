from django.db import models

# Create your models here.
class Valcompra (models.Model):
    compra = models.IntegerField(max_length=30)
