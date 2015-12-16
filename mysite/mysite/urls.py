from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #here we are telling the URL parser to include the configured urls from data.urls at the empty path
    #make sure you created the urls.py file in the data directory
    url(r'^', include('data.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
