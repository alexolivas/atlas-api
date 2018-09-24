from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from web.views.about_views import *
from web.views.portfolio_views import ListFeaturedProjects, ListProjects, ProjectDetails

from atlas.web.views.career_views import ResumeTimeline

urlpatterns = [
    url(r'^about/expertise/$', ExpertiseDetails.as_view(), name='expertise'),
    url(r'^about/info/$', AboutInfoDetails.as_view(), name='about'),
    url(r'^about/skills/programming/$', ProgrammingDetails.as_view(), name='programming_details'),
    url(r'^about/skills/development/$', DevelopmentToolDetails.as_view(), name='development_tool_details'),
    url(r'^about/skills/data/$', DataStorageDetails.as_view(), name='data_storage_details'),
    url(r'^about/skills/deployment/$', DeploymentDetails.as_view(), name='deployment_details'),
    url(r'^career/resume/$', ResumeTimeline.as_view(), name='resume'),
    url(r'^portfolio/projects/$', ListProjects.as_view(), name='portfolio_projects'),
    url(r'^portfolio/projects/featured$', ListFeaturedProjects.as_view(), name='featured_portfolio_projects'),
    url(r'^portfolio/projects/(\d+)/$', ProjectDetails.as_view(), name='portfolio_project_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)