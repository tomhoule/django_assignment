# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('a_value', models.FloatField()),
                ('b_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='dataentry',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Site'),
        ),
    ]
