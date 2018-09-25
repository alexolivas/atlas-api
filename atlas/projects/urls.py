from django.urls import path

from atlas.projects.views import ListProjects, ProjectDetails

urlpatterns = [
    path('projects/', ListProjects.as_view()),
    path('projects/<int:pk>', ProjectDetails.as_view()),
]
