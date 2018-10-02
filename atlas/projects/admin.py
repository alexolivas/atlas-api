from django.contrib import admin
from atlas.projects.models import Project, ProjectPhoto


class ProjectPhotosInline(admin.TabularInline):
    model = ProjectPhoto


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'project_completed', 'active_development', 'repo_url',)
    list_filter = ('active_development', 'project_completed', 'display_on_website',)
    search_fields = ['name', 'account']
    inlines = [
        ProjectPhotosInline,
    ]
    # exclude = ('main_photo_thumb',)


admin.site.register(Project, ProjectAdmin)
