from __future__ import unicode_literals
from django.db import models


class CareerSnapshot(models.Model):
    title = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    ACADEMIC = '00'
    INDUSTRY = '01'
    SNAPSHOT_TYPE_CHOICES = (
        (ACADEMIC, 'Academic'),
        (INDUSTRY, 'Industry'),
    )
    snapshot_type = models.CharField(max_length=2, choices=SNAPSHOT_TYPE_CHOICES, default=ACADEMIC)
    month = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.title


class CareerSnapshotAchievement(models.Model):
    title = models.CharField(max_length=150)
    milestone = models.ForeignKey(CareerSnapshot)
    active = models.BooleanField(default=True)
    month = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.title


# TODO: Add a class for to upload profile photos and foreign key-it on the AboutMeInfo object
class AboutMeInfo(models.Model):
    home_page_description = models.TextField()
    about_page_description = models.TextField()
    personal_description = models.TextField()


class TechnologyStack(models.Model):
    name = models.CharField(max_length=90)
    font_icon_class = models.CharField(max_length=25)
    experience_description = models.TextField()

    def __unicode__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=90)
    technology_stack = models.ForeignKey(TechnologyStack)
    experience_description = models.TextField(blank=True, null=True)
    FRAMEWORK = '00'
    PROGRAMMING_LANGUAGE = '01'
    OTHER = '02'
    TECHNOLOGY_TYPE_CHOICES = (
        (FRAMEWORK, 'Framework'),
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (OTHER, 'Other')
    )
    technology_type = models.CharField(max_length=2, choices=TECHNOLOGY_TYPE_CHOICES, default=FRAMEWORK)

    def __unicode__(self):
        return self.name
