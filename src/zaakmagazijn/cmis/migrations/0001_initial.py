# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.BigIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, unique=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In progress')], default='in_progress', max_length=20)),
            ],
            options={
                'verbose_name': 'Changelog',
                'verbose_name_plural': 'Changelogs',
                'ordering': ('created_on',),
            },
        ),
    ]