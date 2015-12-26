# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anticounterfeit', '0020_auto_20151210_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueRandomNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueRandomNumber', models.CharField(max_length=12, unique=True, verbose_name=b'Unique Random Number')),
            ],
        ),
        migrations.CreateModel(
            name='UniqueRandomNumbersGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internalOrExternal', models.CharField(max_length=8, verbose_name=b'Internal Or External')),
                ('batchNumber', models.PositiveSmallIntegerField(verbose_name=b'Batch Number')),
                ('dateAndTime', models.DateTimeField(unique=True, verbose_name=b'Date and Time')),
                ('active', models.BooleanField(default=False, verbose_name=b'Active')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='publiccode',
            name='product',
        ),
        migrations.RemoveField(
            model_name='usercode',
            name='product',
        ),
        migrations.RenameField(
            model_name='check',
            old_name='doctorFK',
            new_name='doctorCityFK',
        ),
        migrations.RenameField(
            model_name='check',
            old_name='pharmacyFK',
            new_name='pharmacyCityFK',
        ),
        migrations.AlterField(
            model_name='check',
            name='checkerMobile',
            field=models.CharField(max_length=11, verbose_name=b'Cheaker Mobile'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=20, unique=True, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor',
            field=models.CharField(max_length=50, unique=True, verbose_name=b'Doctor'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy',
            field=models.CharField(max_length=50, unique=True, verbose_name=b'Pharmacy'),
        ),
        migrations.DeleteModel(
            name='publicCode',
        ),
        migrations.DeleteModel(
            name='UserCode',
        ),
        migrations.AddField(
            model_name='uniquerandomnumber',
            name='uniqueRandomNumbersGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anticounterfeit.UniqueRandomNumbersGroup'),
        ),
    ]