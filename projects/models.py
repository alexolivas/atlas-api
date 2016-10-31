from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from accounts.models import Account


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    account = models.ForeignKey(Account, blank=True, null=True)
    active = models.BooleanField(default=True)
    display_on_website = models.BooleanField(default=True)
    main_photo = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_1 = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_2 = models.FileField(upload_to='photos', blank=True, null=True)
    # photo_3 = models.FileField(upload_to='photos', blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    detailed_description = HTMLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    stage_server_location = models.URLField(blank=True, null=True)
    prod_server_location = models.URLField(blank=True, null=True)
    # technologies_used > ManyToMany

    def __unicode__(self):
        return self.name

    # Use: http://boto.readthedocs.io/en/latest/s3_tut.html
    # Example: http://tech.marksblogg.com/file-uploads-amazon-s3-django.html


# class ProjectBilling(models.Model):
#     pass
