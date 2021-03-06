# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 03:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('neighbourhood', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('comments', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('neighbourhood', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Coast', 'Coast'), ('Nanyuki', 'Nanyuki'), ('Mombasa', 'Mombasa')], default='green', max_length=6)),
                ('rating', multiselectfield.db.fields.MultiSelectField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=9)),
                ('comments', models.TextField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
