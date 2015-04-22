from django.conf.urls import patterns, url
from topology import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
url(r'^machine/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/attacker/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.attacker, name='attacker'),
url(r'^machine/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.machine, name='machine'),)
