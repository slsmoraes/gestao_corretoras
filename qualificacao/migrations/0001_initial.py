# Generated by Django 3.1.7 on 2021-04-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificacao', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'qualificacao',
            },
        ),
    ]
