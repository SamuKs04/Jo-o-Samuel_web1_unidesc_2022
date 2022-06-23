from winreg import REG_NOTIFY_CHANGE_SECURITY
from django.db import models

# Create your models here.
class Funcionario (models.Model):
    cpf_fun  = models.IntegerField(max_length=11)
    rg_fun = models.IntegerField(max_length=7) 
    nome_fun = models.CharField(max_length=30)
    sexo_fun = models.CharField(max_length=5)
    data_nasc = models.DateField(max_length=11)
    carteira_fu = models.IntegerField(max_length=11)
    salario_fun= models.IntegerField(max_length=11) 
    pis_fun= models.IntegerField(max_length=11)


def __str__(self):
    return self.Funcionario

