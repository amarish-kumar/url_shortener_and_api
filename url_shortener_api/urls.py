from django.conf.urls import url, include
from django.contrib import admin
from shortener.views import redirect_view, home_view
from shortener.api.views import URLListView, URLDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_view),
    url(r'^api/urls/$', URLListView),
    url(r'^api/urls/(?P<shortcode>[\w-]+)/$', URLDetails),
    url(r'^(?P<shortcode>[\w-]+)/$', redirect_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)