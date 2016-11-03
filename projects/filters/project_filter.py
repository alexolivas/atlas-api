import django_filters
from django_filters.rest_framework import FilterSet
from projects.models import Project


class ProjectFilter(FilterSet):
    account_name = django_filters.CharFilter(name="account__name")

    class Meta:
        model = Project
        fields = [
            'account',
            'account_name',
            'active_development',
            'project_completed'
        ]
