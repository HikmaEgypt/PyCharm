# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anticounterfeit', '0008_auto_20151207_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.State'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='City',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.City'),
        ),
        migrations.AlterField(
            model_name='publiccode',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.Product'),
        ),
    ]
