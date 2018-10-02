from django.urls import path

from atlas.web.views.about_views import *
from atlas.web.views.projects_views import ListFeaturedProjects, ListProjects, ProjectDetails

from atlas.web.views.career_views import ResumeTimeline

urlpatterns = [
    path('about-expertise/', ExpertiseDetails.as_view(), name='expertise'),
    path('about-info/', AboutDetails.as_view(), name='about'),
    path('about-skills/programming/', ProgrammingDetails.as_view(), name='programming-skills'),
    path('about-skills/development/', DevelopmentToolDetails.as_view(), name='devops-tools'),
    path('about-skills/database/', DataStorageDetails.as_view(), name='data-skills'),
    path('about-skills/deployment/', DeploymentDetails.as_view(), name='devops-skills'),
    path('career/resume/', ResumeTimeline.as_view(), name='resume'),
    path('projects/', ListProjects.as_view(), name='portfolio-projects'),
    path('projects/featured/', ListFeaturedProjects.as_view(), name='featured-projects'),
    path('projects/<int:project_id>/', ProjectDetails.as_view(), name='project-details'),
]
