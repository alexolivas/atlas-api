from django.db import models
from tinymce.models import HTMLField


def s3_bucket_photo_upload(instance, filename):
    """
    This method is responsible for creating the directory where the project photo will be uploaded to
    on the S3 bucket configured by BOTO3
    """
    return 'about/{0}-photo'.format(instance.location, filename)


class CareerSnapshot(models.Model):
    company = models.CharField(max_length=150)
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
        db_table = "career_snapshot"

    def __str__(self):
        return self.company


class AboutInfo(models.Model):
    HOME = 'home'
    ABOUT = 'about'
    LOCATION_CHOICES = (
        (HOME, 'Home Page'),
        (ABOUT, 'About Page')
    )
    description = HTMLField()
    location = models.CharField(max_length=6, choices=LOCATION_CHOICES, default=HOME, unique=True)
    profile_photo = models.ImageField(upload_to=s3_bucket_photo_upload, blank=True, null=True)

    class Meta:
        verbose_name_plural = "about info"
        db_table = "about_info"

    def __str__(self):
        return self.location


class TechnicalSkill(models.Model):
    FRAMEWORK = '00'
    PROGRAMMING_LANGUAGE = '01'
    DATA = '02'
    DEPLOYMENT = '03'
    DEV_TOOL = '04'
    TECHNICAL_SKILL_CHOICES = (
        (FRAMEWORK, 'Framework'),
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (DATA, 'Data'),
        (DEPLOYMENT, 'Deployment'),
        (DEV_TOOL, 'Development Tool'),
    )
    name = models.CharField(max_length=90)
    skill_type = models.CharField(max_length=2, choices=TECHNICAL_SKILL_CHOICES, default=FRAMEWORK)
    description = HTMLField()

    class Meta:
        db_table = "technical_skill"

    def __str__(self):
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
    font_awesome_icon = models.CharField(max_length=90, blank=True, null=True)
    description = HTMLField()

    class Meta:
        verbose_name_plural = "expertise"
        db_table = "expertise"

    def __str__(self):
        return self.area
