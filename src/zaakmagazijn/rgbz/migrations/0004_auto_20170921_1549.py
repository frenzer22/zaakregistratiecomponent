# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import zaakmagazijn.utils.fields
import zaakmagazijn.utils.stuf_datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rgbz', '0003_auto_20170920_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='besluit',
            name='tijdstip_registratie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(default=zaakmagazijn.utils.stuf_datetime.now, max_length=18),
        ),
        migrations.AlterField(
            model_name='object',
            name='identificatie',
            field=models.CharField(help_text='De unieke identificatie van het OBJECT', max_length=100),
        ),
    ]
