from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Enable the URLs when implemented
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.home'),
    url(r'^core/', include('core.urls', namespace='core')),
)
