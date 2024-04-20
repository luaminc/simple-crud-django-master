# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2024-04-20 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaIndustria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('descripcion_industria', models.IntegerField(verbose_name='Nombre Industria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rut', models.CharField(max_length=20, unique=True, verbose_name='RUT')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('pais', models.CharField(max_length=100, verbose_name='País')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('image', models.ImageField(upload_to='proveedor', verbose_name='Imagen')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.CategoriaIndustria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
