from django.db import models

# Create your models here.
class UF(models.Model):
    sigla_estado = models.CharField(max_length=2)
    class Meta:
        db_table = 'uf'

    def __str__(self):
        return self.sigla_estado
