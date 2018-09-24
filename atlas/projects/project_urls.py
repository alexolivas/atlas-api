from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from atlas.projects.projects_views import ListProjects, ProjectDetails

urlpatterns = [
    url(r'^$', ListProjects.as_view(), name='projects'),
    url(r'^(\d+)/$', ProjectDetails.as_view(), name='project_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)