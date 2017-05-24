# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170103_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('experience_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('technology_type', models.CharField(choices=[('00', 'Framework'), ('01', 'Programming Language'), ('02', 'Other')], default='00', max_length=2)),
                ('technology_stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.TechnologyStack')),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
    ]
