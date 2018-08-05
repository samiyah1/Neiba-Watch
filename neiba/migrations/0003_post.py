# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-03 08:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neiba', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('postDate', models.DateTimeField(auto_now_add=True)),
                ('NeighbourHood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neiba.NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-postDate'],
            },
        ),
    ]
