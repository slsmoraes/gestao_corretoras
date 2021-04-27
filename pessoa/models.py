from django.db import models
from qualificacao.models import Qualificacao
from uf.models import UF
from seguradora.models import Seguradora, Insurance


# Create your models here.
class Pessoa(models.Model):
    # Prospect / Cliente
    qualificacao = models.OneToOneField(Qualificacao, on_delete=models.PROTECT)
    # CPF:xxx.xxx.xxx-xx (15) CNPJ:0xx.xxx.xxx/xxxx-xx (19)
    cpf_cnpj        = models.CharField(max_length=19)
    nome            = models.CharField(max_length=60)
    email           = models.CharField(max_length=70, blank=True, null=True)
    data_nascimento = models.DateField
    fax             = models.CharField(max_length=15, blank=True, null=True)
    telefone        = models.CharField(max_length=14, blank=True, null=True)
    celular         = models.CharField(max_length=15, blank=True, null=True)
    cnh_nro         = models.CharField(max_length=11, blank=True, null=True)
    cnh_data_validade = models.DateField
    cnh_categoria   = models.CharField(max_length=2, blank=True, null=True)
    seguradora      = models.OneToOneField(Insurance, related_name='nome_fantasia', on_delete=models.PROTECT)
    cep             = models.CharField(max_length=10, blank=True, null=True)
    logradouro      = models.CharField(max_length=60, blank=True, null=True)
    numero          = models.CharField(max_length=7, blank=True, null=True)
    complemento     = models.CharField(max_length=20, blank=True, null=True)
    bairro          = models.CharField(max_length=25, blank=True, null=True)
    cidade          = models.CharField(max_length=25, blank=True, null=True)
    estado          = models.OneToOneField(UF, on_delete=models.PROTECT, blank=True, null=True)
    data_cadastro   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pessoa'

    def __str__(self):
        return self.cpf_cnpj

