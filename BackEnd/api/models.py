from django.db import models
from django.utils import timezone

class tbl_cliente(models.Model):
	d_nombre = models.CharField(max_length=50)
	d_apellidoPaterno = models.CharField(max_length=50)
	d_apellidoMaterno = models.CharField(max_length=50)
	d_direccion = models.CharField(max_length=150)
	d_telefono = models.CharField(max_length=15)
	d_correo = models.CharField(max_length=100)
	d_contrasena = models.CharField(max_length=50)
	#website = models.URLField(max_length=100)
	#foundation = models.PositiveIntegerField()
    #TextField(blanck=True)
	def __str__(self):
		return self.d_nombre
	
class tbl_rol(models.Model):
	ro_nombre = models.CharField(max_length=50)
	# website = models.URLField(max_length=100)
	# foundation = models.PositiveIntegerField()
	# TextField(blanck=True)
	def __str__(self):
		return self.ro_nombre

class personas(models.Model):
    titulo_cortecia = models.CharField(max_length=20)
    nombre = models.CharField(max_length=80)
    primer_apellido = models.CharField(max_length=80)
    segundo_apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateTimeField(auto_now=True)
    fotografia = models.CharField(max_length=100)
    genero = models.CharField(max_length=20, choices=(
        ("Masculino", "M"),
        ("Femenino", "F"),
        ("No Binario", "N/B"),
    ), default="Masculino")
    tipo_sangre = models.CharField(max_length=10, choices=(
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ), default="A+")
    estatus = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'personas'
    def __str__(self):
        return self.nombre
 
class usuarios(models.Model):
    persona = models.ForeignKey('personas', on_delete=models.CASCADE)
    password = models.BinaryField(max_length=256)
    tipo = models.CharField(max_length=20, choices=(
		("Empleado", "Empleado"),
		("Vicitante", "Vicitante"),
		("Miembro", "Miembro"),
		("Instructor", "Instructor"),
	), default="Empleado")
    estatus_conexion = models.CharField(max_length=20, choices=(
		("Online", "Online"),
		("Offline", "Offline"),
		("Banned", "Banned"),
	), default="Online")
    ultima_conexion = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=60)
    class Meta:
        db_table = 'usuarios'
    def __str__(self):
        return self.username
    
class empleados(models.Model):
    persona = models.ForeignKey(personas,on_delete=models.CASCADE)
    puesto = models.CharField(max_length=50)
    area = models.CharField(max_length=60)
    numero_empleado = models.IntegerField()
    sucursal = models.ForeignKey('sucursales',on_delete=models.CASCADE)
    fecha_contratacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'empleados'
    def __str__(self):
        return self.puesto
    
class sucursales(models.Model):
	nombre = models.CharField(max_length=150)
	direccion = models.CharField(max_length=250)
	responsable = models.ForeignKey('empleados',on_delete=models.CASCADE)
	total_clientes_atendidos = models.IntegerField()
	promedio_clientes_x_dia = models.IntegerField()
	capacidad_maximo = models.IntegerField()
	total_empleados = models.IntegerField()
	horario_disponibilidad = models.TextField()
	estatus = models.BooleanField(default=True)
	class Meta:
		db_table = 'sucursales'
	def __str__(self):
		return self.nombre

class dietas(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.TextField()
    objetivo = models.TextField()
    restricciones = models.TextField()
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = 'dietas'
    def __str__(self):
        return self.nombre

class indicadores_nutricionales(models.Model): 
	edad = models.IntegerField()
	IMC = models.DecimalField(max_digits=5, decimal_places=3)
	circunferencia_cintura = models.DecimalField(max_digits=5, decimal_places=2)
	nivel_nutriente_sangre = models.TextField()
	class Meta:
		db_table = 'indicadores_nutricionales'
	def __str__(self):
		return self.nivel_nutriente_sangre
 
class valoraciones_nutricionales(models.Model): 
	usuario = models.ForeignKey('usuarios',on_delete=models.CASCADE)
	indicador_nutricional = models.ForeignKey('indicadores_nutricionales',on_delete=models.CASCADE)
	valor = models.CharField(max_length=20) 
	fecha_valoracion = models.DateTimeField(auto_now=True) 
	empleado = models.ForeignKey('empleados',on_delete=models.CASCADE)
	comentarios = models.TextField() 
	def __str__(self):
		return self.valor
	class Meta:
		db_table = 'valoraciones_nutricionales'

class dietas_usuarios(models.Model): 
    usuario = models.ForeignKey('usuarios',on_delete=models.CASCADE)
    dieta = models.ForeignKey('dietas',on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now=True) 
    fecha_inicio = models.DateTimeField(auto_now=True) 
    fecha_fin = models.DateTimeField(auto_now=True) 
    observaciones = models.TextField()
    estatus = models.BooleanField(default=True)
    def __str__(self):
        return self.observaciones
    class Meta:
        db_table = 'dietas_usuarios'
    
class seguimientos_dietas_usuarios(models.Model): 
	dieta_usuario = models.ForeignKey('dietas_usuarios',on_delete=models.CASCADE)
	descripcion = models.TextField()
	empleado = models.ForeignKey('empleados',on_delete=models.CASCADE)
	estatus =  models.CharField(max_length=20, choices=(
		("Programada", "Programada"),
		("Iniciada", "Iniciada"),
		("Seguimiento", "Seguimiento"),
		("Suspendida", "Suspendida"),
		("Finalizada", "Finalizada"),
	), default="Programada")
	porcentaje_avance = models.CharField(max_length=20, choices=(
		("0% a 10%", "0% a 10%"),
		("11% a 20%", "11% a 20%"),
		("21% a 30%", "21% a 30%"),
		("31% a 40%", "31% a 40%"),
		("41% a 50% ", "41% a 50%"),
		("51% a 60% ", "51% a 60%"),
		("61% a 70% ", "61% a 70%"),
		("71% a 80% ", "71% a 80%"),
		("81% a 90% ", "81% a 90%"),
		("91% a 100% ", "91% a 100%"),
	), default="0% a 10%")
	def __str__(self):
		return self.descripcion
	class Meta:
		db_table = 'seguimientos_dietas_usuarios'

class preguntas_nutricionales(models.Model): 
    persona = models.ForeignKey('personas',on_delete=models.CASCADE)
    comidas_x_dia = models.CharField(max_length=20, choices=(
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5 o mas", "5 o mas"),
	), default="2")
    variedad_comidas = models.CharField(max_length=20, choices=(
		("Nunca", "Nunca"),
		("Algunas Veces", "Algunas Veces"),
		("Normalmente", "Normalmente"),
		("Siempre", "Siempre"),
	), default="Nunca")
    regularidad_carbohidratos = models.CharField(max_length=20, choices=(
		("Nunca", "Nunca"),
		("Algunas Veces", "Algunas Veces"),
		("Normalmente", "Normalmente"),
		("Siempre", "Siempre"),
	), default="Nunca")
    grasa_g = models.CharField(max_length=20, choices=(
		("10g", "10g"),
		("30g", "30g"),
		("60g", "60g"),
		("100g o mas", "100g o mas"),
	), default="10g")
    calorias_consumidas = models.CharField(max_length=20, choices=(
		("Menos de 1000 Kcal", "Menos de 1000 Kcal"),
		("1000 Kcal", "1000 Kcal"),
		("1500 Kcal", "1500 Kcal"),
		("2000 Kcal", "2000 Kcal"),
		("2500 Kcal", "2500 Kcal"),
		("3000 Kcal", "3000 Kcal"),
		("3500 Kcal", "3500 Kcal"),
		("4000 Kcal", "4000 Kcal"),
		("Mas de 4000 Kcal", "Mas de 4000 Kcal"),
	), default="Menos de 1000 Kcal")
    def __str__(self):
        return self.grasa_g
    class Meta:
        db_table = 'preguntas_nutricionales'
        
class bitacora(models.Model):
    usuario = models.CharField(max_length=50)
    operacion = models.CharField(max_length=20, choices=(
		("Create", "Create"),
		("Read", "Read"),
		("Update", "Update"),
		("Delete", "Delete"),
	), default="Create")
    tabla = models.CharField(max_length=60)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField(auto_now=True)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = 'bitacora'
    def _str_(self):
        return self.usuario
    
class membresias(models.Model):
    codigo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=(
		("Individual", "Individual"),
		("Familiar", "Familiar"),
		("Empresarial", "Empresarial"),
	), default="Individual")
    tipo_servicios = models.CharField(max_length=20, choices=(
		("Basicos", "Basicos"),
		("Completa", "Completa"),
		("Coaching", "Coaching"),
		("Nutriólogo", "Nutriólogo"),
	), default="Basicos")
    tipo_plan = models.CharField(max_length=20, choices=(
		("Anual", "Anual"),
		("Semestral", "Semestral"),
		("Trimestral", "Trimestral"),
		("Bimestral", "Bimestral"),
		("Mensual", "Mensual"),
		("Semanal", "Semanal"),
		("Diaria", "Diaria"),
	), default="Anual")
    nivel = models.CharField(max_length=20, choices=(
		("Nuevo", "Nuevo"),
		("Plata", "Plata"),
		("Oro", "Oro"),
		("Diamante", "Diamante"),
	), default="Nuevo")
    fecha_inicio = models.DateTimeField(auto_now=True)
    fecha_fin = models.DateTimeField(auto_now=True)
    estatus = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'membresias'
    def _str_(self):
        return self.codigo
    
class membresias_usuarios(models.Model):
    membresia =  models.ForeignKey('membresias',on_delete=models.CASCADE)
    usuarios =  models.ForeignKey('usuarios',on_delete=models.CASCADE)
    fecha_ultima_visita = models.DateTimeField(auto_now=True)
    estatus = models.BooleanField(default=True)
    class Meta:
        db_table = 'membresias_usuarios'
    def _str_(self):
        return self.usuario
    
class miembros(models.Model):
    persona =  models.ForeignKey('personas',on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=(
		("Frecuente", "Frecuente"),
		("Ocasional", "Ocasional"),
		("Nuevo", "Nuevo"),
		("Esporádico", "Esporádico"),
		("Una sola visita", "Una sola visita"),
	), default="Frecuente")
    membresia_activa = models.BooleanField(default=True)
    antiguedad = models.CharField(max_length=80)
    class Meta:
        db_table = 'miembros'
    def _str_(self):
        return self.usuario
