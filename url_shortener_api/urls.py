from django.conf.urls import url
from django.contrib import admin
from shortener.views import redirect_view, home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_view),
    url(r'^(?P<shortcode>[\w-]+)/$', redirect_view),
]
