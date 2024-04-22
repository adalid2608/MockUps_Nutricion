from django.urls import path,include
from rest_framework import routers
from api import views
from .views import *

router = routers.DefaultRouter()
router.register(r'tbl_cliente', views.tbl_clienteViewSet)
router.register(r'tbl_rol', views.tbl_rolViewSet)
router.register(r'personas', views.personasviewset)
router.register(r'usuarios', views.usuariosviewset)
router.register(r'empleados', views.empleadosviewset)
router.register(r'sucursales', views.sucursalesviewset)
router.register(r'dietas', views.dietasviewset)
router.register(r'indicadores_nutricionales', views.indicadores_nutricionalesviewset)
router.register(r'valoraciones_nutricionales', views.valoraciones_nutricionalesviewset)
router.register(r'dietas_usuarios', views.dietas_usuariosviewset)
router.register(r'seguimientos_dietas_usuarios', views.seguimientos_dietas_usuariosviewset)
router.register(r'preguntas_nutricionales', views.preguntas_nutricionalesviewset)
router.register(r'membresias', views.membresiasviewset)
router.register(r'membresias_usuarios', views.membresias_usuariosviewset)
router.register(r'miembros', views.miembrosviewset)


urlpatterns = [
	path('api/v1',include(router.urls)),
	path('',ObtenerHistoriales)
]

