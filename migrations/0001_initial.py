# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('isbn', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=60)),
                ('imagen', models.FileField(blank=True, null=True, upload_to='')),
                ('autor', models.CharField(max_length=60)),
                ('editorial', models.CharField(max_length=60)),
                ('pais', models.CharField(max_length=30)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha_prestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_devolucion_previsto', models.DateTimeField()),
                ('fecha_devolucion_real', models.DateTimeField()),
                ('cliente', models.ForeignKey(to='blogbiblioteca.Cliente')),
                ('libro', models.ManyToManyField(to='blogbiblioteca.Libro')),
            ],
        ),
    ]
