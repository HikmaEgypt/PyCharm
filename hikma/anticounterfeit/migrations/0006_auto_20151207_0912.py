# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anticounterfeit', '0005_auto_20151207_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publiccode',
            name='productFK',
        ),
        migrations.RemoveField(
            model_name='usercode',
            name='productFK',
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(default=b'1', on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.State'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='City',
            field=models.ForeignKey(default=b'1', on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.City'),
        ),
        migrations.AddField(
            model_name='publiccode',
            name='Product',
            field=models.ForeignKey(default=b'1', on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.Product'),
        ),
        migrations.AddField(
            model_name='usercode',
            name='Product',
            field=models.ForeignKey(default=b'1', on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.Product'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='City',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.City'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'images/product-original.jpg', upload_to=None),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('city', 'State')]),
        ),
        migrations.AlterUniqueTogether(
            name='doctor',
            unique_together=set([('doctor', 'City')]),
        ),
    ]
