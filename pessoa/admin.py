from django.contrib import admin
from pessoa.models import Pessoa
from seguradora.models import Insurance

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Insurance)