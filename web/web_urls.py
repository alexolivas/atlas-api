from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from web.views.portfolio_views import ListProjects, ProjectDetails
from web.views.about_views import AboutInfo
from web.views.career_views import ResumeTimeline
from web.views.expertise_views import ExpertiseDetails


urlpatterns = [
    url(r'^about/expertise/$', ExpertiseDetails.as_view(), name='expertise'),
    url(r'^about/info/$', AboutInfo.as_view(), name='about'),
    url(r'^career/resume/$', ResumeTimeline.as_view(), name='resume'),
    url(r'^portfolio/projects/$', ListProjects.as_view(), name='portfolio_projects'),
    url(r'^portfolio/projects/(\d+)/$', ProjectDetails.as_view(), name='portfolio_project_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)