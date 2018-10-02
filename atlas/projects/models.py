from django.db import models
from tinymce.models import HTMLField

from atlas.accounts.models import Account
from atlas.web.models import TechnicalSkill


def s3_bucket_photo_upload(instance, filename):
    """
    This method is responsible for creating the directory where the project photo will be uploaded to
    on the S3 bucket configured by BOTO3
    """
    return 'projects/{0}/{1}'.format(instance.project.id, filename)


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    account = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    active_development = models.BooleanField(default=True)
    project_completed = models.BooleanField(default=False)
    display_on_website = models.BooleanField(default=True)
    public_repo = models.BooleanField(default=False)
    featured_project = models.BooleanField(default=False)
    retired = models.BooleanField(default=False)
    tech_stack_display = models.CharField(max_length=75, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    technology_description = HTMLField(blank=True, null=True)
    deploy_description = HTMLField(blank=True, null=True)
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

    def __str__(self):
        return self.name


class ProjectPhoto(models.Model):
    photo = models.ImageField(upload_to=s3_bucket_photo_upload, blank=True, null=True)
    main_photo = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name
