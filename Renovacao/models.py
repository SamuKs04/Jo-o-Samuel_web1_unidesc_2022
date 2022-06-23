from django.db import models

# Create your models here.
class Renovacao (models.Model):
    data_deso = models.DateField(max_length = 10) 
    data_reno = models.DateField(max_length = 10) 
    cartorio = models.CharField(max_length= 10)
