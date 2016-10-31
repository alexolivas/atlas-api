from django.contrib import admin
from models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'repo_url',)
    list_filter = ('active', 'display_on_website',)
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)
