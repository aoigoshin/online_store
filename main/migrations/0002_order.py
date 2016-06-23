# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя заказчика')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('order', models.CharField(max_length=255, verbose_name='Заказ')),
                ('summa', models.IntegerField(default=0, verbose_name='Сумма заказа')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
    ]
