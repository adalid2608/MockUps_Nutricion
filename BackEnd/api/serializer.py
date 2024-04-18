from rest_framework import serializers
from .models import *

class tbl_clienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = tbl_cliente
		fields = '__all__'
		
class tbl_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = tbl_rol
		fields = '__all__'

class personasserializer(serializers.ModelSerializer):
	class Meta:
		model = personas
		fields = '__all__'
		
class usuariosserializer(serializers.ModelSerializer):
	class Meta:
		model = usuarios
		fields = '__all__'
  
class empleadosserializer(serializers.ModelSerializer):
	class Meta:
		model = empleados
		fields = '__all__'
  
class sucursalesserializer(serializers.ModelSerializer):
	class Meta:
		model = sucursales
		fields = '__all__'
  
class dietasserializer(serializers.ModelSerializer):
	class Meta:
		model = dietas
		fields = '__all__'
  
class indicadores_nutricionalesserializer(serializers.ModelSerializer):
	class Meta:
		model = indicadores_nutricionales
		fields = '__all__'
  
class valoraciones_nutricionalesserializer(serializers.ModelSerializer):
	class Meta:
		model = valoraciones_nutricionales
		fields = '__all__'
  
class dietas_usuariosserializer(serializers.ModelSerializer):
	class Meta:
		model = dietas_usuarios
		fields = '__all__'
  
class seguimientos_dietas_usuariosserializer(serializers.ModelSerializer):
	class Meta:
		model = seguimientos_dietas_usuarios
		fields = '__all__'
  
class preguntas_nutricionalesserializer(serializers.ModelSerializer):
	class Meta:
		model = preguntas_nutricionales
		fields = '__all__'

class membresiasserealizer(serializers.ModelSerializer):
	class Meta:
		model=membresias
		fields = '__all__'

class membresias_usuariosserealizer(serializers.ModelSerializer):
	class Meta:
		model=membresias_usuarios
		fields = '__all__'

class miembrosserealizer(serializers.ModelSerializer):
	class Meta:
		model=miembros
		fields = '__all__'
