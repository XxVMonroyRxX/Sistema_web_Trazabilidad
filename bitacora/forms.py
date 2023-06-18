from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class CatMatPeligrosoForm(forms.ModelForm):
    class Meta:
        model = CatMatPeligroso
        fields = [
            "nombre",
            "cretib",
            "descripcion",
             "ficha_seguridad",
             "imagen"

        ]
class RegAlmacenForm(forms.ModelForm):
    class Meta:
        model = RegAlmacen
        fields = [
            "lote",
            "factura",
             "proveedor",
            "fecha_llegada",
            "producto"
        ]
class SeguimientosForm(forms.ModelForm):
    class Meta:
        model = Seguimientos
        fields = [
            "nombre",
            "fecha_recibo",
                "nombre_empleado_origen",
            "nombre_empleado_destino",
                "estado",
            "producto",
                "departamento_inicial",
            "departamento_final"
        ]

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = [
            "nombre",
            "campus"
        ]
def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campus'].queryset = Campus.objects.all()

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = [
            "nombre"
        ]

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            "nombre",
           "correo",
            "password",
            "sesion"
        ]

class SesionesForm(forms.ModelForm):
    class Meta:
        model = Sesiones
        fields = [
            "estado",]



class USubProductoForm(forms.ModelForm):
    class Meta:
        model = USubProducto
        fields = [
            "nombre",
            "cantidad",
              "descripcion"
        ]

class UProductoForm(forms.ModelForm):
    class Meta:
        model = UProducto
        fields = [
            "nombre",
            "fecha_caducidad",
                "cat_material_peligro",
            "u_sub_producto"
        ]

class AuditoriasEForm(forms.ModelForm):
    class Meta:
        model = AuditoriasE
        fields = [
            "departamento",
            "seguimiento",
                    "producto",
            "fecha"
        ]

class AuditoriasSForm(forms.ModelForm):
    class Meta:
        model = AuditoriasS
        fields = [
            "producto",
            "departamento",
                    "fecha_auditoria",
            "estatus",
                    "etiquetado",
            "vida_util"
        ]
class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            "correo",
            "password",
        ]
        labels = {
            "password": _("Contrasena"),
        }
        help_texts = {
              "correo": _("Ingresa tu correo."),
              "password": _("Ingresa tu contrasena."),
        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'password','is_active','is_superuser' ]
        labels = {
            "password": _("Contrasena"),
             "is_superuser": _("Es un usuario administrador"),
 "is_active": _("Es un usuario activo"),
        }
        help_texts = {
            "nombre": _("Ingresa el nombre completo del usuario."),
              "correo": _("Ingresa el correo del usuario."),
              "password": _("Ingresa la contrasena del usuario."),
              "is_active": _("¿El usuario estara activo en el sistema?"),
              "is_superuser": _("¿El usuario tendra permisos de administrador?."),
        }

