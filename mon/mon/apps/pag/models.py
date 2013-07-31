from django.db import models

class servicio(models.Model):
        nombre          = models.CharField(max_length=20)
        descrip_corta   = models.TextField(max_length=300)
        descrip_larga	= models.TextField(max_length=500)
	nombre_completo	= models.CharField(max_length=100)

        def __unicode__(self):
                return self.nombre

class servicio_especifico(models.Model):
	nombre          = models.CharField(max_length=100)
	n_q_consiste    = models.TextField(max_length=1000,null=True,blank=True)
        alcance         = models.TextField(max_length=1000,null=True,blank=True)
        q_aporta        = models.TextField(max_length=1000,null=True,blank=True)
        duracion        = models.TextField(max_length=1000,null=True,blank=True)
        para_quien      = models.TextField(max_length=1000,null=True,blank=True)
	servicio 	= models.ForeignKey('pag.servicio',null=True,blank=True)

	def __unicode__(self):
                return self.nombre

class post(models.Model):
	titulo 	= models.CharField(max_length=60)
	cuerpo 	= models.TextField()
	creado 	= models.DateTimeField(auto_now_add=True)
	servicio = models.ForeignKey('pag.servicio')
	usuario = models.ForeignKey('pag.usuario',null=True,blank=True)
	def __unicode__(self):
		return self.titulo

class usuario(models.Model):
	nombre		= models.CharField(max_length=100)
        apellido        = models.CharField(max_length=100)
	bio		= models.TextField(max_length=500)
	facebook	= models.CharField(max_length=100)
	twitter		= models.CharField(max_length=50)
	mail		= models.EmailField()
	telf		= models.CharField(max_length=50)
	def __unicode__(self):
                nombreCompleto = "%s %s"%(self.nombre,self.apellido)
                return nombreCompleto


