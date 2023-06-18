from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class Sesiones(models.Model):
    estado = models.CharField(max_length=200)
    fecha_conexion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sesion {self.id}  - {self.estado}  - {self.fecha_conexion}"
    class Meta:
        db_table = "sesiones"


class CustomUserManager(BaseUserManager):
    def validar_datos(self,nombre,correo,contrasena,sesion):
        if not nombre or nombre is None or nombre=='':
            raise ValueError('Se necesita especificar un nombre')
        if not correo or correo is None or correo=='':
            raise ValueError('Se necesita especificar un correo')
        if not contrasena or contrasena is None or contrasena=='':
            raise ValueError('Se necesita especificar una contrasena')


    def create_user(self,nombre,correo,contrasena ):
        self.validar_datos(nombre,correo,contrasena)

        user = self.create_user(
          nombre=nombre,correo=correo,password=contrasena
        )
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user


    def create_superuser(self,nombre,correo,contrasena):
        self.validar_datos(nombre,correo,contrasena)

        user = self.create_user(
          nombre=nombre,correo=correo,password=contrasena
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Usuarios(AbstractUser):
    username = None
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    sesion = models.OneToOneField(Sesiones,on_delete=models.DO_NOTHING,verbose_name="sesion de usuario",default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = [nombre,correo,password] # Email & Password are required by default.
    def verificar_contrasena(self,rcontrasena):
        if rcontrasena==self.password:
            return True
        else:
            return False
    def get_full_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
	    return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_admin(self):
        return self.is_admin
    def __str__(self):
        return f"Usuarios {self.id}  - {self.nombre} - {self.correo}"
    class Meta:
        db_table = "usuarios"
class Campus(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"Campus {self.id}  - {self.nombre}"
    class Meta:
        db_table = "campus"
class Departamentos(models.Model):
    nombre = models.CharField(max_length=50)
    campus = models.OneToOneField(Campus,on_delete=models.CASCADE,verbose_name="campus del departamento")
    def __str__(self):
        return f"Departamento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "departamentos"
class Seguimientos(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_recibo = models.DateField()
    nombre_empleado_origen = models.CharField(max_length=200)
    nombre_empleado_destino = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    producto = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="producto del seguimiento")
    departamento_inicial = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="departamento inicial del seguimiento",related_name='sesiones_departamento_inicial')
    departamento_final = models.OneToOneField(Sesiones,on_delete=models.CASCADE,verbose_name="departamento final del seguimiento",related_name='sesiones_departamento_final')
    def __str__(self):
        return f"Seguimiento {self.id}  - {self.nombre}"
    class Meta:
        db_table = "seguimientos"

class CatMatPeligroso(models.Model):
    nombre = models.CharField(max_length=200)
    cretib = models.CharField(max_length=200)
    descripcion = models.TextField()
    ficha_seguridad =models.FileField(upload_to='fichas_seguridad/',null=True,blank=True)
    imagen = models.ImageField(null=True,blank=True)
    def __str__(self):
        return f"CatMatPeligroso {self.id}  - {self.nombre} - {self.cretib}"
    class Meta:
        db_table = "cat_mat_peligroso"
class USubProducto(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_sub_producto"
class UProducto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_caducidad = models.DateTimeField()
    cat_material_peligro = models.OneToOneField(CatMatPeligroso,on_delete=models.CASCADE)
    u_sub_producto = models.OneToOneField(USubProducto,on_delete=models.CASCADE)
    def __str__(self):
        return f"Producto {self.id}  - {self.nombre}"
    class Meta:
        db_table = "u_producto"
class AuditoriasE(models.Model):
    departamento = models.OneToOneField(Departamentos,on_delete=models.CASCADE)
    seguimiento = models.OneToOneField(Seguimientos,on_delete=models.CASCADE)
    producto = models.OneToOneField(UProducto,on_delete=models.CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_e"
class AuditoriasS(models.Model):
    producto = models.OneToOneField(UProducto,on_delete=models.CASCADE)
    departamento = models.OneToOneField(Departamentos,on_delete=models.CASCADE)
    fecha_auditoria = models.DateField()
    estatus = models.CharField(max_length=200)
    etiquetado = models.CharField(max_length=200)
    vida_util = models.IntegerField()
    def __str__(self):
        return f"Auditoria {self.id} de {self.producto} realizada el {self.fecha_auditoria}"
    class Meta:
        db_table = "auditorias_s"
class RegAlmacen(models.Model):
    lote = models.CharField(max_length=200)
    factura = models.IntegerField()
    proveedor = models.CharField(max_length=200)
    fecha_llegada = models.DateTimeField()
    producto = models.OneToOneField(UProducto,on_delete=models.CASCADE,verbose_name="producto del almacen")
    def __str__(self):
        return f"RegAlmacen {self.id}  - {self.producto}"
    class Meta:
        db_table = "reg_almacen"
