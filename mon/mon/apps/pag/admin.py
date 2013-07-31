from django.contrib import admin
from mon.apps.pag.models import usuario,servicio,post,servicio_especifico

admin.site.register(usuario)
admin.site.register(servicio)
admin.site.register(post)
admin.site.register(servicio_especifico)
