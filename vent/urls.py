from django.conf.urls import patterns, include, url
from django.contrib import admin
from vent.home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vent.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^topology/', include('topology.urls')),
	url(r'^$', 'home.views.index'),
)
