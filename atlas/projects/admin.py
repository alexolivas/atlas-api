from django.contrib import admin
from models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'project_completed', 'active_development', 'repo_url',)
    list_filter = ('active_development', 'project_completed', 'display_on_website',)
    search_fields = ['name', 'account']
    # exclude = ('main_photo_thumb',)

admin.site.register(Project, ProjectAdmin)
