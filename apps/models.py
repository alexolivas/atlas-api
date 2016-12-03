from __future__ import unicode_literals
from django.db import models


# This is an app registration service, register JIRA, HEROKU, Webfaction i.e. similar to hobsons's onelogin
class App(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=150)
