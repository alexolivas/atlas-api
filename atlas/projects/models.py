# import StringIO
import os

# from PIL import Image
# from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from tinymce.models import HTMLField

from atlas.accounts.models import Account
from atlas.web.models import TechnicalSkill


def s3_bucket_photo_upload(instance, filename):
    return 'projects/%s/%s' % (instance.id, filename,)


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

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     # This is turned off for now, the quality is not good enough, I'm doing this manually
    #     # I will revisit this later.
    #     # TODO: Crop instead of resize
    #     # Use https://tinypng.com to improve quality
    #     self.create_thumbnails()
    #     super(Project, self).save()

    # def create_thumbnails(self):
    #     for field in Project._meta.fields:
    #         # Check if this is a FileField with 'photo' in the column name but is not a thumbnail
    #         if 'FileField' in field.get_internal_type() and 'photo' in field.name\
    #                 and 'thumb' not in field.name:
    #             project_photo = getattr(self, field.name)
    #             if project_photo:
    #                 photo_str = self.resize_image(project_photo, 600, 600, False)
    #                 project_photo_resized = InMemoryUploadedFile(
    #                     photo_str, None, project_photo.name, 'image/png', photo_str.len, None)
    #                 setattr(self, field.name, project_photo_resized)
    #
    #                 # Make a thumbnail copy of the original
    #                 thumbnail_str = self.resize_image(project_photo, 500, 500, True)
    #                 # thumbnail_str = self.resize_image(project_photo, (350, 515))
    #
    #                 # Get ONLY the file name without the extension and full file path
    #                 basename, extension = os.path.splitext(os.path.basename(project_photo.name))
    #                 thumb_name = basename + '_thumb' + extension
    #
    #                 # Save the thumb in memory
    #                 project_photo_thumb = InMemoryUploadedFile(
    #                     thumbnail_str, None, thumb_name, 'image/png', thumbnail_str.len, None)
    #
    #                 # Add the thumb copy of the photo to the model, in the corresponding "*_thumb" column
    #                 setattr(self, field.name + '_thumb', project_photo_thumb)

    # @staticmethod
    # def resize_image(project_photo, width, height, is_thumbnail):
    #     # TODO This needs to be cropped to fit 303x227
    #     # TODO: Crop example > https://gist.github.com/sigilioso/2957026
    #     # TODO: I need to re-sample this image >> http://brantsteen.com/blog/pil-quality/
    #     # TODO: http://stackoverflow.com/questions/20361444/cropping-an-image-with-python-pillow
    #     # Get a copy of the original photo and make it smaller
    #     img = Image.open(project_photo)
    #     if is_thumbnail:
    #         # img.thumbnail(size, Image.ANTIALIAS)
    #         img.crop((0, 0, 200, 200))
    #     else:
    #         img.resize((width, height), Image.ANTIALIAS)
    #
    #     image_str = StringIO.StringIO()
    #     img.save(image_str, 'png')
    #     return image_str

    # Use: http://boto.readthedocs.io/en/latest/s3_tut.html
    # Example: http://tech.marksblogg.com/file-uploads-amazon-s3-django.html


class ProjectPhoto(models.Model):
    photo = models.ImageField(upload_to=s3_bucket_photo_upload, blank=True, null=True)
    main_photo = models.BooleanField(default=False, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo
