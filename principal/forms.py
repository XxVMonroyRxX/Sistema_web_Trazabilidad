from django import forms
from .models import *

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
            "title",
            "description",
        ]

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
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
            "contrasena",
             "tipo_usuario",
            "sesion"
        ]

class SesionesForm(forms.ModelForm):
    class Meta:
        model = Sesiones
        fields = [
            "estado",
            "fecha_conexion",
        ]

class Tipos_usuariosForm(forms.ModelForm):
    class Meta:
        model = Tipos_usuarios
        fields = [
            "nombre",
            "nivel",
        ]

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
