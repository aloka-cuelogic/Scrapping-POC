from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_results/$', 'core.views.get_results',
        name='get_results'),
)
