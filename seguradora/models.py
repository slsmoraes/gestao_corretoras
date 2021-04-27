from django.db import models
from uf.models import UF

# Create your models here.

class Insurance(models.Model):
    nome_fantasia = models.CharField(max_length=30)

    class Meta:
        db_table = 'insurance'

    def __str__(self):
        return (self.nome_fantasia)

class Seguradora(models.Model):
    cnpj = models.CharField(max_length=19)
    codigo = models.IntegerField
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=70, blank=True, null=True)
    site = models.CharField(max_length=70, blank=True, null=True)
    gerente_responsavel = models.CharField(max_length=70, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    endereco = models.CharField(max_length=60)
    complemento = models.CharField(max_length=20)
    numero = models.CharField(max_length=7)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=25)
    estado = models.OneToOneField(UF, on_delete=models.CASCADE, primary_key=True,)
    observacao = models.TextField
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'seguradora'

    def __str__(self):
        return (self.codigo, self.nome)