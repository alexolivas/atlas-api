from django.conf.urls import include, url
from django.contrib import admin

from atlas.authentication import auth_urls
from atlas.projects import urls
from atlas.web import urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# polls_patterns = ([
#     url(r'^web/', include(web_urls, namespace='web')),
# ], 'web')  # 'polls' is the app_name

urlpatterns = [
    url(r'^web/', include(urls)),

    url(r'^auth/', include(auth_urls)),
    url(r'^projects/', include(urls)),

    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'Atlas API'
