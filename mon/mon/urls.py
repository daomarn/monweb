from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mon.views.home', name='home'),
    # url(r'^mon/', include('mon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^',include('mon.apps.pag.urls')),
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
#	url(r)
)
#if settings.DEBUG:
#	urlpatterns += patterns('',
#	(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
#)
