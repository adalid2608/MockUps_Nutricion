from rest_framework import viewsets
from .models import tbl_cliente,tbl_rol
from .serializer import *
from pymongo import  MongoClient
from django.http import JsonResponse

class tbl_clienteViewSet(viewsets.ModelViewSet):
	queryset = tbl_cliente.objects.all()
	serializer_class = tbl_clienteSerializer

class tbl_rolViewSet(viewsets.ModelViewSet):
	queryset = tbl_rol.objects.all()
	serializer_class = tbl_rolSerializer
 
class personasviewset(viewsets.ModelViewSet):
	queryset = personas.objects.all()
	serializer_class = personasserializer

class usuariosviewset(viewsets.ModelViewSet):
	queryset = usuarios.objects.all()
	serializer_class = usuariosserializer
 
class empleadosviewset(viewsets.ModelViewSet):
	queryset = empleados.objects.all()
	serializer_class = empleadosserializer
 
class sucursalesviewset(viewsets.ModelViewSet):
	queryset = sucursales.objects.all()
	serializer_class = sucursalesserializer
 
class dietasviewset(viewsets.ModelViewSet):
	queryset = dietas.objects.all()
	serializer_class = dietasserializer
 
class indicadores_nutricionalesviewset(viewsets.ModelViewSet):
	queryset = indicadores_nutricionales.objects.all()
	serializer_class = indicadores_nutricionalesserializer
 
class valoraciones_nutricionalesviewset(viewsets.ModelViewSet):
	queryset = valoraciones_nutricionales.objects.all()
	serializer_class = valoraciones_nutricionalesserializer
 
class dietas_usuariosviewset(viewsets.ModelViewSet):
	queryset = dietas_usuarios.objects.all()
	serializer_class = dietas_usuariosserializer
 
class seguimientos_dietas_usuariosviewset(viewsets.ModelViewSet):
	queryset = seguimientos_dietas_usuarios.objects.all()
	serializer_class = seguimientos_dietas_usuariosserializer
 
class preguntas_nutricionalesviewset(viewsets.ModelViewSet):
	queryset = preguntas_nutricionales.objects.all()
	serializer_class = preguntas_nutricionalesserializer

class membresiasviewset(viewsets.ModelViewSet):
	queryset = membresias.objects.all()
	serializer_class = membresiasserealizer

class membresias_usuariosviewset(viewsets.ModelViewSet):
	queryset = membresias_usuarios.objects.all()
	serializer_class = membresias_usuariosserealizer

class miembrosviewset(viewsets.ModelViewSet):
	queryset = miembros.objects.all()
	serializer_class = miembrosserealizer
 

def ObtenerHistoriales(req):
	conexion = MongoClient("mongodb://localhost:27017")
	bd = conexion["gimnasio"]
	col = bd["historiales_medicos"]
	data = list(col.find())

	nuevo_arreglo = []

	# Recorre cada documento obtenido y estructúralo en el formato deseado
	for documento in data:
		nuevo_arreglo.append({
			"numero_expediente": documento["numero_expediente"],
			"ficha_identificacion": documento["ficha_identificacion"]
		})


	return JsonResponse(nuevo_arreglo, safe=False)

