from django.contrib import admin
from qualificacao.models import Qualificacao
from uf.models import UF
from seguradora.models import Seguradora


# Register your models here.
admin.site.register(Qualificacao)
admin.site.register(UF)
admin.site.register(Seguradora)