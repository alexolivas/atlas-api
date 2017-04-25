from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from accounts.models import Account
from web.models import TechnicalSkill


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    account = models.ForeignKey(Account, blank=True, null=True)
    active_development = models.BooleanField(default=True)
    project_completed = models.BooleanField(default=False)
    display_on_website = models.BooleanField(default=True)
    featured_project = models.BooleanField(default=False)
    retired = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    main_photo = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_1 = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_2 = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_3 = models.FileField(upload_to='photos', blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    technology_description = HTMLField(blank=True, null=True)
    release_instructions = HTMLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    stage_url = models.URLField(blank=True, null=True)
    production_url = models.URLField(blank=True, null=True)
    technology = models.ManyToManyField(TechnicalSkill)
    cloud_platform = models.CharField(max_length=25, blank=True, null=True)
    cloud_platform_account = models.CharField(max_length=50, blank=True, null=True)
    cloud_platform_console = models.URLField(blank=True, null=True)
    domain_provider = models.CharField(max_length=25, blank=True, null=True)
    domain_provider_account = models.CharField(max_length=50, blank=True, null=True)
    domain_provider_console = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    # Use: http://boto.readthedocs.io/en/latest/s3_tut.html
    # Example: http://tech.marksblogg.com/file-uploads-amazon-s3-django.html


# class ProjectBilling(models.Model):
#     pass
