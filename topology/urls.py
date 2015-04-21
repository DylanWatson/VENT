from django.conf.urls import patterns, url
from topology import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
url(r'^machine/(?P<ip>.*)/$',views.machine, name='machine'),)
