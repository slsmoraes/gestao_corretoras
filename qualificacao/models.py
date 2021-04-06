from django.db import models

# Create your models here.
class Qualificacao(models.Model):
    qualificacao = models.CharField(max_length=10) #Prospect / Cliente
    class Meta:
        db_table = 'qualificacao'

    def __str__(self):
        return self.qualificacao
