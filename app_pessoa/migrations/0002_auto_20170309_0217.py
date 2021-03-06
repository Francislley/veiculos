# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=30, verbose_name='Nome do Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_admissao', models.DateField(verbose_name='Data de Admissão')),
                ('Id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pessoa.Cargo')),
            ],
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(blank=True, help_text='Inclua o número se tiver celular da Claro', max_length=60, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(max_length=250, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='Id_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pessoa.Pessoa'),
        ),
    ]
