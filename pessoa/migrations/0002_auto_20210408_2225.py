# Generated by Django 3.1.7 on 2021-04-09 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uf', '0001_initial'),
        ('seguradora', '0002_auto_20210408_1100'),
        ('qualificacao', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='estado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='uf.uf'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='logradouro',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='numero',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='qualificacao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='qualificacao.qualificacao'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='seguradora',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='seguradora.seguradora'),
        ),
        migrations.AlterModelTable(
            name='pessoa',
            table='pessoa',
        ),
    ]
