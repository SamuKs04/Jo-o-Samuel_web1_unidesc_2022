from django.db import models

# Create your models here.
class Pagamento (models.Model):
    valor_pag = models.IntegerField(max_length=20)
    forma_pag = models.CharField(max_length=20)
    parcelas_pag = models.IntegerField(max_length=20)
    data_pag = models.DateField(max_length=10)
    banco_pag = models.CharField(max_length=30)
    agencia_pag = models.IntegerField(max_length=20)
    conta_pag = models.IntegerField(max_length=20)
