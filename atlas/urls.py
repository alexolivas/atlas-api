from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.documentation import include_docs_urls

from atlas.authentication import auth_urls
from atlas.web import urls


urlpatterns = [
    url(r'^web/', include(urls)),

    url(r'^auth/', include(auth_urls)),
    url(r'^projects/', include(urls)),

    url(r'^docs/', include_docs_urls(title='Atlas API', authentication_classes=[], permission_classes=[])),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'Atlas API'
