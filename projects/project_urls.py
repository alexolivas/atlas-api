from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from public_views import ListProjects

urlpatterns = [
    url(r'^$', ListProjects.as_view(), name='public_projects'),
]

urlpatterns = format_suffix_patterns(urlpatterns)