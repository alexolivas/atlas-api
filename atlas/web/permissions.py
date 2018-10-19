from rest_framework import permissions


class WebsiteAccessPermission(permissions.BasePermission):
    """
    Global permission check to determine if the user belongs the 'Web Clients' group
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Web Clients').count() == 1
