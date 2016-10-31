from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField


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
    description = HTMLField()

    def __unicode__(self):
        return self.title


class CareerSnapshotAchievement(models.Model):
    title = models.CharField(max_length=150)
    milestone = models.ForeignKey(CareerSnapshot)
    active = models.BooleanField(default=True)
    month = models.IntegerField()
    year = models.IntegerField()
    description = HTMLField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class AboutInfo(models.Model):
    home_page_description = HTMLField()
    about_page_description = HTMLField()
    personal_description = HTMLField()

    class Meta:
        verbose_name_plural = "about info"


class TechnologyStack(models.Model):
    name = models.CharField(max_length=90)
    font_icon_class = models.CharField(max_length=25)
    experience_description = HTMLField()

    def __unicode__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=90)
    technology_stack = models.ForeignKey(TechnologyStack)
    experience_description = HTMLField(blank=True, null=True)
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

    class Meta:
        verbose_name_plural = "Technologies"
