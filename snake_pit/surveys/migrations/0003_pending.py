# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-16 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
        ('surveys', '0002_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateField()),
                ('surveyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]
