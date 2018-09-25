from django.urls import path

from atlas.web.views.about_views import *
from atlas.web.views.portfolio_views import ListFeaturedProjects, ListProjects, ProjectDetails

from atlas.web.views.career_views import ResumeTimeline

urlpatterns = [
    path('about/expertise/', ExpertiseDetails.as_view(), name='expertise'),
    path('about/info/', AboutInfoDetails.as_view(), name='about'),
    path('about/skills/programming/', ProgrammingDetails.as_view(), name='programming-skills'),
    path('about/skills/development/', DevelopmentToolDetails.as_view(), name='devops-tools'),
    path('about/skills/data/', DataStorageDetails.as_view(), name='data-skills'),
    path('about/skills/deployment/', DeploymentDetails.as_view(), name='devops-skills'),
    path('career/resume/', ResumeTimeline.as_view(), name='resume'),
    path('portfolio/projects/', ListProjects.as_view(), name='portfolio-projects'),
    path('portfolio/projects/featured/', ListFeaturedProjects.as_view(), name='featured-projects'),
    path('portfolio/projects/<int:pk>/', ProjectDetails.as_view(), name='project-details'),
]
