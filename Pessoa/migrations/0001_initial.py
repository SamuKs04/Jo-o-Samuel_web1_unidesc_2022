# Generated by Django 4.0.5 on 2022-06-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(max_length=11)),
                ('telefone', models.IntegerField(max_length=13)),
                ('cep_pes', models.IntegerField(max_length=11)),
                ('rua_pes', models.CharField(max_length=50)),
                ('bairro_pes', models.CharField(max_length=30)),
                ('cidade_pes', models.CharField(max_length=30)),
                ('uf_pes', models.CharField(max_length=2)),
            ],
        ),
    ]
