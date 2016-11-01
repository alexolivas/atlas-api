from django.conf.urls import include, url
from django.contrib import admin
from authentication import auth_urls
from projects import project_urls
from web import web_urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^web/', include(web_urls)),

    url(r'^auth/', include(auth_urls)),
    url(r'^projects/', include(project_urls)),

    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = 'Atlas API'
