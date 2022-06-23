from django.db import models

# Create your models here.
class Agendamento (models.Model):
    data_agen  = models.DateField(max_length=10)
    hora_agen  = models.TimeField(max_length=10)
    local_agen  = models.CharField(max_length=50)
