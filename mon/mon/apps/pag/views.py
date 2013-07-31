# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from mon.apps.pag.models import post, servicio, usuario, servicio_especifico
def index_view(request):
	servicios = servicio.objects.all()
#	sfgsdgsdg =sdfds
	if request.method == "GET":
		ctx = {'servicios': servicios}
        	return render_to_response('pag/index.html',ctx,context_instance=RequestContext(request))

def servicios_view(request):
	servicios = servicio.objects.all
	if request.method == "POST":
		ser = servicio.objects.get(nombre = request.POST.get('servicio'))
		if ser.nombre == "cloud":
			return HttpResponseRedirect('/cloud')
		if ser.nombre == "tv":
			return HttpResponseRedirect('/tv')
		if ser.nombre == "app":
                        return HttpResponseRedirect('/app')		
		ctx = {'servicios':servicios}
		return render_to_response('pag/servicios.html',ctx,context_instance=RequestContext(request))
	else:
		ctx = {'servicios':servicios}
		return render_to_response('pag/servicios.html',ctx,context_instance=RequestContext(request))
def servicios_especificos_view(request,id):
	serv_esp = servicio_especifico.objects.get(id = id)
	servicios = servicio.objects.all
	servs = servicio_especifico.objects.filter(servicio = serv_esp.servicio)
#	dfgfgs =bsdgsdbs
	if request.method == "GET":
                ctx = {'serv':serv_esp,'servicios':servicios,'servs':servs}
                return render_to_response('pag/serv_especificos.html',ctx,context_instance=RequestContext(request))

def cloud_view(request):
	serv = servicio.objects.get(nombre= 'cloud')
	ctx = {'servicio':serv}
	return HttpResponseRedirect('/serv_especificos/1',ctx)
def tv_view(request):
        serv = servicio.objects.get(nombre= 'tv')
        ctx = {'servicio':serv}
        return HttpResponseRedirect('/serv_especificos/3',ctx)
def app_view(request):
        serv = servicio.objects.get(nombre= 'app')
        ctx = {'servicio':serv}
        return HttpResponseRedirect('/serv_especificos/4',ctx)
