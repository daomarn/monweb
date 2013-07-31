from django.conf.urls.defaults import patterns,url
from django.conf.urls import include
urlpatterns = patterns('mon.apps.pag.views',
	url(r'^$','index_view',name='vista_principal'),	
	url(r'^servicios/$','servicios_view',name='vista_servicios'),
	url(r'^blog/', include('zinnia.urls'),name='vista_blog'),
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^serv_especificos/(?P<id>.*)/$','servicios_especificos_view',name='vista_servs'),
	url('^cloud/','cloud_view',name='vista_cloud'),
	url('^tv/','tv_view',name='vista_tv'),
	url('^app/','app_view',name='vista_app'),
)
