from django.db import models

class Tipos_usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nivel = models.PositiveIntegerField()
    def __str__(self):
        return f"Tipo de Usuario {self.id}  - {self.nombre} - {self.nivel}"
    class Meta:
        db_table = "tipos_usuarios"
class Sesiones(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=200)
    fecha_conexion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sesion {self.id}  - {self.estado}  - {self.fecha_conexion}"
    class Meta:
        db_table = "sesiones"
class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=200)
    contrasena = models.CharField(max_length=200)
    tipo_usuario = models.OneToOneField(Tipos_usuarios,on_delete=models.CASCADE,verbose_name="tipo de usuario")
    sesion = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="sesion de usuario")
    def __str__(self):
        return f"Usuarios {self.id}  - {self.nombre}"
    class Meta:
        db_table = "usuarios"
class Campus(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"Campus {self.id}  - {self.nombre}"
    class Meta:
        db_table = "campus"
class Departamentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    campus = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="campus del departamento")
    def __str__(self):
        return f"Departamento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "departamentos"
class Seguimientos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha_recibo = models.DateField()
    nombre_empleado_origen = models.CharField(max_length=200)
    nombre_empleado_destino = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    producto = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="producto del seguimiento")
    departamento_inicial = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="departamento inicial del seguimiento")
    departamento_final = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="departamento final del seguimiento")
    def __str__(self):
        return f"Seguimiento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "seguimientos"
class RegAlmacen(models.Model):
    id = models.BigAutoField(primary_key=True)
    lote = models.CharField(max_length=200)
    factura = models.IntegerField()
    proveedor = models.CharField(max_length=200)
    fecha_llegada = models.DateTimeField()
    producto = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="producto del almacen")
    def __str__(self):
        return f"RegAlmacen {self.id}  - {self.producto}"
    class Meta:
        db_table = "reg_almacen"
class CatMatPeligroso(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    cretib = models.CharField(max_length=200)
    descripcion = models.TextField()
    ficha_seguridad = models.TextField()
    imagen = models.ImageField()
    def __str__(self):
        return f"CatMatPeligroso {self.id}  - {self.nombre} - {self.cretib}"
    class Meta:
        db_table = "cat_mat_peligroso"
class USubProducto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_sub_producto"
class UProducto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha_caducidad = models.DateTimeField()
    cat_material_peligro = models.OneToOneField(CatMatPeligroso,on_delete=models.CASCADE)
    u_sub_producto = models.OneToOneField(USubProducto,on_delete=models.CASCADE)
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_producto"
class AuditoriasE(models.Model):
    id = models.BigAutoField(primary_key=True)
    departamento = models.OneToOneField(Departamentos,on_delete=models.CASCADE)
    seguimiento = models.OneToOneField(Seguimientos,on_delete=models.CASCADE)
    producto = models.OneToOneField(UProducto,on_delete=models.CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_e"
class AuditoriasS(models.Model):
    id = models.BigAutoField(primary_key=True)
    producto = models.OneToOneField(UProducto,on_delete=models.CASCADE)
    departamento = models.OneToOneField(Departamentos,on_delete=models.CASCADE)
    fecha_auditoria = models.DateField()
    estatus = models.CharField()
    etiquetado = models.CharField()
    vida_util = models.IntegerField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_s"
