from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tbl_cliente)
admin.site.register(tbl_rol)
admin.site.register(personas)
admin.site.register(usuarios)
admin.site.register(empleados)
admin.site.register(sucursales)
admin.site.register(dietas)
admin.site.register(indicadores_nutricionales)
admin.site.register(valoraciones_nutricionales)
admin.site.register(dietas_usuarios)
admin.site.register(seguimientos_dietas_usuarios)
admin.site.register(preguntas_nutricionales)
admin.site.register(membresias)
admin.site.register(membresias_usuarios)
admin.site.register(miembros)

