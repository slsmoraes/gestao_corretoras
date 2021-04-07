from django.db import models

# Create your models here.
class CadPessoa(models.Model):
    qualificacao = models.CharField(max_length=10) #Prospect / Cliente
    # CPF:xxx.xxx.xxx-xx (15) CNPJ:0xx.xxx.xxx/xxxx-xx (19)
    cpf_cnpj = models.CharField(max_length=19)
    nome = models.CharField(max_length=60)
    nome_fantasia = models.CharField(max_length=30)

    cep = models.fields.IntegerField
    endereco = models.CharField(max_length=60)
    complemento = models.CharField(max_length=20)
    numero = models.CharField(max_length=7)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=25)
    estado =models.CharField(max_length=2)

    email = models.CharField(max_length=70, blank=True, null=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    cnh_nro = models.CharField(max_length=11, blank=True, null=True)
    cnh_data_validade = models.DateTimeField()
    cnh_categoria = models.CharField(max_length=2, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cadPessoa'

    def __str__(self):
        return self.nome_fantasia + ' ' + self.nome