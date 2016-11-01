from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from public_views import ListProjects, ProjectDetails

urlpatterns = [
    url(r'^$', ListProjects.as_view(), name='public_projects'),
    url(r'^(\d+)/$', ProjectDetails.as_view(), name='public_project_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)