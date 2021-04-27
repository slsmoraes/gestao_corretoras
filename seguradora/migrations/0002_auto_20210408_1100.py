# Generated by Django 3.1.5 on 2021-04-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uf', '0001_initial'),
        ('seguradora', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seguradora',
            name='id',
        ),
        migrations.AlterField(
            model_name='seguradora',
            name='codigo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seguradora',
            name='estado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uf.uf'),
        ),
    ]