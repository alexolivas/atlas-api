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
    description = HTMLField(blank=True, null=True)

    class Meta:
        db_table = "career_position"

    def __unicode__(self):
        return self.title


class AboutInfo(models.Model):
    home_page_description = HTMLField()
    about_page_description = HTMLField()
    personal_description = HTMLField()

    class Meta:
        verbose_name_plural = "about info"
        db_table = "about_info"


class TechnicalSkill(models.Model):
    FRAMEWORK = '00'
    PROGRAMMING_LANGUAGE = '01'
    DATA = '02'
    DEPLOYMENT = '03'
    TECHNICAL_SKILL_CHOICES = (
        (FRAMEWORK, 'Framework'),
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (DATA, 'Data'),
        (DEPLOYMENT, 'Deployment'),
    )
    name = models.CharField(max_length=90)
    skill_type = models.CharField(max_length=2, choices=TECHNICAL_SKILL_CHOICES, default=FRAMEWORK)
    description = HTMLField()

    class Meta:
        db_table = "technical_skill"

    def __unicode__(self):
        return self.name


class Expertise(models.Model):
    FRONTEND = '00'
    BACKEND = '01'
    DEVOPS = '02'
    LEARNING = '03'
    EXPERTISE_AREA_CHOICES = (
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (DEVOPS, 'DevOps'),
        (LEARNING, 'Learning'),
    )
    area = models.CharField(max_length=2, choices=EXPERTISE_AREA_CHOICES, default=BACKEND)
    description = HTMLField()

    class Meta:
        verbose_name_plural = "expertise"
        db_table = "expertise"

    def __unicode__(self):
        return self.area


# NOT SURE I AM KEEPING THE MODELS BELOW


class TechnologyStack(models.Model):
    name = models.CharField(max_length=90)
    font_icon_class = models.CharField(max_length=25)
    experience_description = HTMLField()

    class Meta:
        verbose_name_plural = "technology stack"
        db_table = "technology_stack"

    def __unicode__(self):
        return self.name


# class Technology(models.Model):
#     name = models.CharField(max_length=90)
#     technology_stack = models.ForeignKey(TechnologyStack)
#     experience_description = HTMLField(blank=True, null=True)
#     FRAMEWORK = '00'
#     PROGRAMMING_LANGUAGE = '01'
#     OTHER = '02'
#     TECHNOLOGY_TYPE_CHOICES = (
#         (FRAMEWORK, 'Framework'),
#         (PROGRAMMING_LANGUAGE, 'Programming Language'),
#         (OTHER, 'Other')
#     )
#     technology_type = models.CharField(max_length=2, choices=TECHNOLOGY_TYPE_CHOICES, default=FRAMEWORK)
#
#     def __unicode__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "Technologies"
