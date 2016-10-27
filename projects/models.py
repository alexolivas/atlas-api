from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)
    display_on_website = models.BooleanField(default=True)
    description = HTMLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    # prod_web_server
    # technologies_used > ManyToMany

    def __unicode__(self):
        return self.name
