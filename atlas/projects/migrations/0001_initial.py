# Generated by Django 2.0.3 on 2018-10-02 00:04

import atlas.projects.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('active_development', models.BooleanField(default=True)),
                ('project_completed', models.BooleanField(default=False)),
                ('display_on_website', models.BooleanField(default=True)),
                ('public_access', models.BooleanField(default=False)),
                ('featured_project', models.BooleanField(default=False)),
                ('retired', models.BooleanField(default=False)),
                ('tech_stack_display', models.CharField(blank=True, max_length=75, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('technology_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('deploy_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('repo_url', models.URLField(blank=True, null=True)),
                ('stage_url', models.URLField(blank=True, null=True)),
                ('production_url', models.URLField(blank=True, null=True)),
                ('cloud_platform', models.CharField(blank=True, max_length=25, null=True)),
                ('cloud_platform_account', models.CharField(blank=True, max_length=50, null=True)),
                ('cloud_platform_console', models.URLField(blank=True, null=True)),
                ('domain_provider', models.CharField(blank=True, max_length=25, null=True)),
                ('domain_provider_account', models.CharField(blank=True, max_length=50, null=True)),
                ('domain_provider_console', models.URLField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('technology', models.ManyToManyField(to='web.TechnicalSkill')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=atlas.projects.models.s3_bucket_photo_upload)),
                ('main_photo', models.BooleanField(default=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
