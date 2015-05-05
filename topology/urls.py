from django.conf.urls import patterns, url
from topology import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
    url(r'^attacker/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.attacker, name='attacker'),
    url(r'^machine/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.machine, name='machine'),
    url(r'^blackhole_add/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.blackhole_add, name='blackhole_result'),
    url(r'^blackhole_del/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.blackhole_del, name='blackhole_result'),
    url(r'^port_scan/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.port_scan, name='portscan_results'),
    url(r'^admin_actions/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',views.admin_actions, name='admin_actions'),
    url(r'^attackers/$', views.attackers, name='attackers'),
    url(r'^report/$', views.report, name='attackers'),
    url(r'^about/$', views.about, name='about'),
)
