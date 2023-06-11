from django.urls import path
from . import views

urlpatterns = [

    path('sesiones/listado', views.listar_sesiones,name="listar_sesiones"),
    path('sesiones/visualizar/<int:id>', views.visualizar_sesiones,name="visualizar_sesiones"),
    path('sesiones/crear',views.crear_sesiones,name="crear_sesiones"),
    path('sesiones/eliminar/<int:id>', views.eliminar_sesiones,name="eliminar_sesiones"),
    path('sesiones/actualizar/<int:id>', views.actualizar_sesiones,name="actualizar_sesiones"),

    path('auditorias_s/listado', views.listar_auditorias_s,name="listar_auditorias_s"),
    path('auditorias_s/visualizar/<int:id>', views.visualizar_auditorias_s,name="visualizar_auditorias_s"),
    path('auditorias_s/crear',views.crear_auditorias_s,name="crear_auditorias_s"),
    path('auditorias_s/eliminar/<int:id>', views.eliminar_auditorias_s,name="eliminar_auditorias_s"),
    path('auditorias_s/actualizar/<int:id>', views.actualizar_auditorias_s,name="actualizar_auditorias_s"),

    path('auditorias_e/listado', views.listar_auditorias_e,name="listar_auditorias_e"),
    path('auditorias_e/visualizar/<int:id>', views.visualizar_auditorias_e,name="visualizar_auditorias_e"),
    path('auditorias_e/crear',views.crear_auditorias_e,name="crear_auditorias_e"),
    path('auditorias_e/eliminar/<int:id>', views.eliminar_auditorias_e,name="eliminar_auditorias_e"),
    path('auditorias_e/actualizar/<int:id>', views.actualizar_auditorias_e,name="actualizar_auditorias_e"),

    path('u_producto/listado', views.listar_u_producto,name="listar_u_producto"),
    path('u_producto/visualizar/<int:id>', views.visualizar_u_producto,name="visualizar_u_producto"),
    path('u_producto/crear',views.crear_u_producto,name="crear_u_producto"),
    path('u_producto/eliminar/<int:id>', views.eliminar_u_producto,name="eliminar_u_producto"),
    path('u_producto/actualizar/<int:id>', views.actualizar_u_producto,name="actualizar_u_producto"),

    path('u_sub_producto/listado', views.listar_u_sub_producto,name="listar_u_sub_producto"),
    path('u_sub_producto/visualizar/<int:id>', views.visualizar_u_sub_producto,name="visualizar_u_sub_producto"),
    path('u_sub_producto/crear',views.crear_u_sub_producto,name="crear_u_sub_producto"),
    path('u_sub_producto/eliminar/<int:id>', views.eliminar_u_sub_producto,name="eliminar_u_sub_producto"),
    path('u_sub_producto/actualizar/<int:id>', views.actualizar_u_sub_producto,name="actualizar_u_sub_producto"),

    path('cat_mat_peligroso/listado', views.listar_cat_mat_peligroso,name="listar_cat_mat_peligroso"),
    path('cat_mat_peligroso/visualizar/<int:id>', views.visualizar_cat_mat_peligroso,name="visualizar_cat_mat_peligroso"),
    path('cat_mat_peligroso/crear',views.crear_cat_mat_peligroso,name="crear_cat_mat_peligroso"),
    path('cat_mat_peligroso/eliminar/<int:id>', views.eliminar_cat_mat_peligroso,name="eliminar_cat_mat_peligroso"),
    path('cat_mat_peligroso/actualizar/<int:id>', views.actualizar_cat_mat_peligroso,name="actualizar_cat_mat_peligroso"),

    path('reg_almacen/listado', views.listar_reg_almacen,name="listar_reg_almacen"),
    path('reg_almacen/visualizar/<int:id>', views.visualizar_reg_almacen,name="visualizar_reg_almacen"),
    path('reg_almacen/crear',views.crear_reg_almacen,name="crear_reg_almacen"),
    path('reg_almacen/eliminar/<int:id>', views.eliminar_reg_almacen,name="eliminar_reg_almacen"),
    path('reg_almacen/actualizar/<int:id>', views.actualizar_reg_almacen,name="actualizar_reg_almacen"),

    path('seguimientos/listado', views.listar_seguimientos,name="listar_seguimientos"),
    path('seguimientos/visualizar/<int:id>', views.visualizar_seguimientos,name="visualizar_seguimientos"),
    path('seguimientos/crear',views.crear_seguimientos,name="crear_seguimientos"),
    path('seguimientos/eliminar/<int:id>', views.eliminar_seguimientos,name="eliminar_seguimientos"),
    path('seguimientos/actualizar/<int:id>', views.actualizar_seguimientos,name="actualizar_seguimientos"),

    path('departamentos/listado', views.listar_departamentos,name="listar_departamentos"),
    path('departamentos/visualizar/<int:id>', views.visualizar_departamentos,name="visualizar_departamentos"),
    path('departamentos/crear',views.crear_departamentos,name="crear_departamentos"),
    path('departamentos/eliminar/<int:id>', views.eliminar_departamentos,name="eliminar_departamentos"),
    path('departamentos/actualizar/<int:id>', views.actualizar_departamentos,name="actualizar_departamentos"),

    path('campus/listado', views.listar_campus,name="listar_campus"),
    path('campus/visualizar/<int:id>', views.visualizar_campus,name="visualizar_campus"),
    path('campus/crear',views.crear_campus,name="crear_campus"),
    path('campus/eliminar/<int:id>', views.eliminar_campus,name="eliminar_campus"),
    path('campus/actualizar/<int:id>', views.actualizar_campus,name="actualizar_campus"),

    path('tipos_usuarios/listado', views.listar_tipos_usuarios,name="listar_tipos_usuarios"),
    path('tipos_usuarios/visualizar/<int:id>', views.visualizar_tipos_usuarios,name="visualizar_tipos_usuarios"),
    path('tipos_usuarios/crear',views.crear_tipos_usuarios,name="crear_tipos_usuarios"),
    path('tipos_usuarios/eliminar/<int:id>', views.eliminar_tipos_usuarios,name="eliminar_tipos_usuarios"),
    path('tipos_usuarios/actualizar/<int:id>', views.actualizar_tipos_usuarios,name="actualizar_tipos_usuarios"),

    path('usuarios/listado', views.listar_usuarios,name="listar_usuarios"),
    path('usuarios/visualizar/<int:id>', views.visualizar_usuarios,name="visualizar_usuarios"),
    path('usuarios/crear',views.crear_usuarios,name="crear_usuarios"),
    path('usuarios/eliminar/<int:id>', views.eliminar_usuarios,name="eliminar_usuarios"),
    path('usuarios/actualizar/<int:id>', views.actualizar_usuarios,name="actualizar_usuarios"),



]
