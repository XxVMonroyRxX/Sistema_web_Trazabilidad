from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.contrib import messages
from .models import *
from .forms import *
import datetime
import logging
logger = logging.getLogger(__name__)

def listar_auditorias_s(request):
    logger.warning('Se ejecuta la funcion listar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["dataset"] = AuditoriasS.objects.all()
    context["titulo"] = "Auditorias_S"
    return render(request, "principal/auditorias_s/listar.html", context)
def visualizar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion visualizar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["data"] = AuditoriasS.objects.get(id = id)
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Visualizar"
    return render(request, "principal/auditorias_s/detalle.html", context)
def crear_auditorias_s(request):
    logger.warning('Se ejecuta la funcion crear_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Creacion"
    form = AuditoriasSForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/auditorias_s/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                logger.warning('Se crea una auditoria a las  '+str(datetime.datetime.now())+' horas!')
                return redirect('listar_auditorias_s')
            else:
                messages.error(request, 'Porfavor corrige los errores:')
                logger.warning('Error de validacion')
                return render(request, "principal/auditorias_s/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion eliminar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    obj = get_object_or_404(AuditoriasS, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Auditoria {id} eliminada de manera exitosa.')
        messages.success(request, f'Auditoria {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("listar_auditorias_s")
    return render(request, "principal/auditorias_s/listar.html", context)
def actualizar_auditorias_s(request, id):
    logger.warning('Se ejecuta la funcion actualizar_auditorias_s a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_S"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(AuditoriasS, id = id)
    form = AuditoriasSForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/auditorias_s/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'La auditoria {id} ha sido actualizada de manera exitosa.')
                messages.success(request, f'La auditoria {id} ha sido actualizada de manera exitosa.')
                return HttpResponseRedirect('listar_auditorias_s')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/auditorias_s/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def listar_auditorias_e(request):
    logger.warning('Se ejecuta la funcion listar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["dataset"] = AuditoriasE.objects.all()
    return render(request, "principal/auditorias_e/listar.html", context)
def visualizar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion visualizar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Visualizacion"
    context["data"] = AuditoriasE.objects.get(id = id)
    return render(request, "principal/auditorias_e/detalle.html", context)
def crear_auditorias_e(request):
    logger.warning('Se ejecuta la funcion crear_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Creacion"
    form = AuditoriasEForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/auditorias_e/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La auditoria ha sido creada de manera exitosa.')
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                return redirect('listar_auditorias_e')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/auditorias_e/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def eliminar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion eliminar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    obj = get_object_or_404(AuditoriasE, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Auditoria {id} eliminada de manera exitosa.')
        messages.success(request, f'Auditoria {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("listar_auditorias_e")
    return render(request, "principal/auditorias_e/listar.html", context)
def actualizar_auditorias_e(request, id):
    logger.warning('Se ejecuta la funcion actualizar_auditorias_e a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Auditorias_E"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(AuditoriasE, id = id)
    form = AuditoriasEForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/auditorias_e/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'La auditoria {id} ha sido actualizada de manera exitosa.')
                messages.success(request, f'La auditoria {id} ha sido actualizada de manera exitosa.')
                return HttpResponseRedirect('listar_auditorias_e')
            else:
                logger.warning('Porfavor corrige los errores:')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/auditorias_e/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def listar_u_producto(request):
    logger.warning('Se ejecuta la funcion listar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["dataset"] = UProducto.objects.all()
    return render(request, "principal/u_producto/listar.html", context)
def visualizar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion visualizar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Visualizacion"
    context["data"] = UProducto.objects.get(id = id)
    return render(request, "principal/u_producto/detalle.html", context)
def crear_u_producto(request):
    logger.warning('Se ejecuta la funcion crear_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Creacion"
    form = UProductoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/u_productos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La auditoria ha sido creada de manera exitosa.')
                messages.success(request, 'La auditoria ha sido creada de manera exitosa.')
                return redirect('listar_u_producto')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/u_productos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def eliminar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion eliminar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    obj = get_object_or_404(UProducto, id = id)
    if request.method =="POST":
        obj.delete()
        messages.success(request, f'Producto {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("listar_u_producto")
    return render(request, "principal/u_producto/listar.html", context)


def actualizar_u_producto(request, id):
    logger.warning('Se ejecuta la funcion actualizar_u_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Productos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(UProducto, id = id)
    form = UProductoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/u_productos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El producto {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El producto {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("listar_u_producto")
            else:
                logger.warning(f'Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/u_productos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning(f'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def listar_u_sub_producto(request):
    logger.warning('Se ejecuta la funcion listar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["dataset"] = USubProducto.objects.all()
    return render(request, "principal/u_sub_producto/listar.html", context)
def visualizar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion visualizar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Visualizacion"
    context["data"] = USubProducto.objects.get(id = id)
    return render(request, "principal/u_sub_producto/detalle.html", context)
def crear_u_sub_producto(request):
    logger.warning('Se ejecuta la funcion crear_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Creacion"
    form = USubProductoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/u_sub_producto/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Subproducto ha sido creado de manera exitosa.')
                messages.success(request, 'Subproducto ha sido creado de manera exitosa.')
                return redirect('u_sub_productos')
            else:
                logger.warning('Se generaron errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/u_sub_productos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')




def eliminar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion eliminar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    obj = get_object_or_404(USubProducto, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Sub Producto {id} eliminado de manera exitosa.')
        messages.success(request, f'Sub Producto {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/u_sub_producto/listar.html", context)
def actualizar_u_sub_producto(request, id):
    logger.warning('Se ejecuta la funcion actualizar_u_sub_producto a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "U_Sub_Productos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(USubProducto, id = id)
    form = USubProductoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/u_sub_productos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El subproducto {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El subproducto {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("/"+id)
            else:
                logger.warning(f'Se ha generado un error de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/u_sub_productos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning(f'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def listar_cat_mat_peligroso(request):
    logger.warning('Se ejecuta la funcion listar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["dataset"] = CatMatPeligroso.objects.all()
    return render(request, "principal/cat_mat_peligroso/listar.html", context)
def visualizar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion visualizar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["accion"] = "Visualizacion"
    context["data"] = CatMatPeligroso.objects.get(id = id)
    return render(request, "principal/cat_mat_peligroso/detalle.html", context)
def crear_cat_mat_peligroso(request):
    logger.warning('Se ejecuta la funcion crear_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligroso"
    context["accion"] = "Creacion"
    form = CatMatPeligrosoForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/cat_mat_peligroso/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Categoria material peligroso ha sido creado de manera exitosa.')
                messages.success(request, 'Categoria material peligroso ha sido creado de manera exitosa.')
                return redirect('cat_mat_peligroso')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/cat_mat_peligroso/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion eliminar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    obj = get_object_or_404(CatMatPeligroso, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Cat Mat Peligroso {id} eliminado de manera exitosa.')
        messages.success(request, f'Cat Mat Peligroso {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/cat_mat_peligroso/listar.html", context)

def actualizar_cat_mat_peligroso(request, id):
    logger.warning('Se ejecuta la funcion actualizar_cat_mat_peligroso a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Cat_Mat_Peligrosos"
    context["accion"] = "Actualizacion"
    obj = get_object_or_404(CatMatPeligroso, id = id)
    form = CatMatPeligrosoForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/cat_mat_peligroso/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning( f'Categoria Mat Peligroso {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Categoria Mat Peligroso {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("/"+id)
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/cat_mat_peligroso/detalle.html", {'context':context,'form':form})
        except:
            logger.warning( 'Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def listar_reg_almacen(request):
    logger.warning('Se ejecuta la funcion listar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "RegAlmacen"
    context["dataset"] = RegAlmacen.objects.all()
    return render(request, "principal/reg_almacen/listar.html", context)
def visualizar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion visualizar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "RegAlmacen"
    context["accion"] = "Visualizacion"
    context["data"] = RegAlmacen.objects.get(id = id)
    return render(request, "principal/reg_almacen/detalle.html", context)


def crear_reg_almacen(request):
    logger.warning('Se ejecuta la funcion crear_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Reg_Almacen"
    context["accion"] = "Creacion"
    form = RegAlmacenForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/reg_almacen/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Reg Almacen ha sido creado de manera exitosa.')
                messages.success(request, 'Reg Almacen ha sido creado de manera exitosa.')
                return redirect('cat_mat_peligroso')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/reg_almacen/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion eliminar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "RegAlmacen"
    obj = get_object_or_404(RegAlmacen, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Reg Almacen {id} eliminado de manera exitosa.')
        messages.success(request, f'Reg Almacen {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/reg_almacen/listar.html", context)


def actualizar_reg_almacen(request, id):
    logger.warning('Se ejecuta la funcion actualizar_reg_almacen a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Reg_Almacen"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(RegAlmacen, id = id)
    form = RegAlmacenForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/reg_almacen/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Reg Almacen {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Reg Almacen {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("reg_almacen")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/reg_almacen/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')



def listar_seguimientos(request):
    logger.warning('Se ejecuta la funcion listar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["dataset"] = Seguimientos.objects.all()
    return render(request, "principal/seguimientos/listar.html", context)
def visualizar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion visualizar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Visualizacion"
    context["data"] = Seguimientos.objects.get(id = id)
    return render(request, "principal/seguimientos/detalle.html", context)
def crear_seguimientos(request):
    logger.warning('Se ejecuta la funcion crear_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Creacion"
    form = SeguimientosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/seguimientos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Seguimiento ha sido creado de manera exitosa.')
                messages.success(request, 'Seguimiento ha sido creado de manera exitosa.')
                return redirect('cat_mat_peligroso')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/seguimientos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion eliminar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Eliminacion"

    obj = get_object_or_404(Seguimientos, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Seguimiento {id} eliminado de manera exitosa.')
        messages.success(request, f'Seguimiento {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/seguimientos/listar.html", context)
def actualizar_seguimientos(request, id):
    logger.warning('Se ejecuta la funcion actualizar_seguimientos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Seguimientos"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Seguimientos, id = id)
    form = SeguimientosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/seguimientos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Seguimiento {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Seguimiento {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("reg_almacen")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/seguimientos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def listar_departamentos(request):
    logger.warning('Se ejecuta la funcion listar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["dataset"] = Departamentos.objects.all()
    return render(request, "principal/departamentos/listar.html", context)
def visualizar_departamentos(request, id):
    logger.warning('Se ejecuta la funcion visualizar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Visualizacion"
    context["data"] = Departamentos.objects.get(id = id)
    return render(request, "principal/departamentos/detalle.html", context)


def crear_departamentos(request):
    logger.warning('Se ejecuta la funcion crear_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Creacion"
    form = DepartamentosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/departamentos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Departamento ha sido creado de manera exitosa.')
                messages.success(request, 'Departamento ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/departamentos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_departamentos(request, id):
    logger.warning('Se ejecuta la funcion eliminar_departamentos a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Departamentos"
    obj = get_object_or_404(Departamentos, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Departamento {id} eliminado de manera exitosa.')
        messages.success(request, f'Departamento {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/departamentos/listar.html", context)
def actualizar_departamentos(request, id):
    logger.warning('Se ejecuta la funcion actualizar_departamentos a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Departamentos"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Departamentos, id = id)
    form = DepartamentosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/departamentos/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Departamento {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Departamento {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("departamentos")
            else:
                logger.warning(f'Departamento {id} ha sido actualizado de manera exitosa.')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/departamentos/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')


def listar_campus(request):
    logger.warning('Se ejecuta la funcion listar_campus a las  '+str(datetime.datetime.now())+' horas!')
    context ={}
    context["titulo"] = "Campus"
    context["dataset"] = Campus.objects.all()
    return render(request, "principal/campus/listar.html", context)
def visualizar_campus(request, id):
    logger.warning('Se ejecuta la funcion visualizar_campus a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Visualizacion"

    context["data"] = Campus.objects.get(id = id)
    return render(request, "principal/campus/detalle.html", context)
def crear_campus(request):
    logger.warning('Se ejecuta la funcion crear_campus a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Creacion"

    form = CampusForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/campus/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('El Campus ha sido creado de manera exitosa.')
                messages.success(request, 'El Campus ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/campus/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def eliminar_campus(request, id):
    logger.warning('Se ejecuta la funcion eliminar_campus a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Campus"
    obj = get_object_or_404(Campus, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Campus {id} eliminado de manera exitosa.')
        messages.success(request, f'Campus {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/campus/listar.html", context)
def actualizar_campus(request, id):
    logger.warning('Se ejecuta la funcion actualizar_campus a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Campus"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Campus, id = id)
    form = CampusForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/campus/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'El campus {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'El campus {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/campus/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')

def listar_sesiones(request):
    logger.warning('Se ejecuta la funcion listar_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["dataset"] = Sesiones.objects.all()
    return render(request, "principal/sesiones/listar.html", context)
def visualizar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion visualizar_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Visualizacion"

    context["data"] = Sesiones.objects.get(id = id)
    return render(request, "principal/sesiones/detalle.html", context)
def crear_sesiones(request):
    logger.warning('Se ejecuta la funcion crear_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Creacion"

    form = SesionesForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/sesiones/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('La sesion ha sido creado de manera exitosa.')
                messages.success(request, 'La sesion ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/sesiones/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
def eliminar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion eliminar_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    obj = get_object_or_404(Sesiones, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning( f'Sesion {id} eliminada de manera exitosa.')
        messages.success(request, f'Sesion {id} eliminada de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/sesiones/listar.html", context)
def actualizar_sesiones(request, id):
    logger.warning('Se ejecuta la funcion actualizar_sesiones a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Sesiones"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Sesiones, id = id)
    form = SesionesForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/sesiones/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning( f'Sesion {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Sesion {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/sesiones/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.n')
            messages.error(request, 'Ha ocurrido un error inesperado.')
def listar_tipos_usuarios(request):
    logger.warning('Se ejecuta la funcion listar_tipos_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Tipos de Usuarios"
    context["dataset"] = Tipos_usuarios.objects.all()
    return render(request, "principal/tipos_usuarios/listar.html", context)
def visualizar_tipos_usuarios(request, id):
    logger.warning('Se ejecuta la funcion visualizar_tipos_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Tipos de Usuarios"
    context["accion"] = "Visualizacion"

    context["data"] = Tipos_usuarios.objects.get(id = id)
    return render(request, "principal/tipos_usuarios/detalle.html", context)
def crear_tipos_usuarios(request):
    logger.warning('Se ejecuta la funcion crear_tipos_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Tipos de Usuarios"
    context["accion"] = "Creacion"

    form = Tipos_usuariosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/tipos_usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('Tipo de usuario ha sido creado de manera exitosa.')
                messages.success(request, 'Tipo de usuario ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/tipos_usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
def eliminar_tipos_usuarios(request, id):
    logger.warning('Se ejecuta la funcion eliminar_tipos_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Tipos de Usuarios"
    obj = get_object_or_404(Tipos_usuarios, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Tipo de usuario {id} eliminado de manera exitosa.')
        messages.success(request, f'Tipo de usuario {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/tipos_usuarios/listar.html", context)
def actualizar_tipos_usuarios(request, id):
    logger.warning('Se ejecuta la funcion actualizar_tipos_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Tipos de Usuarios"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Tipos_usuarios, id = id)
    form = Tipos_usuariosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/tipos_usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Tipo de usuario {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Tipo de usuario {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/tipos_usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')









def listar_usuarios(request):
    logger.warning('Se ejecuta la funcion listar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["dataset"] = Usuarios.objects.all()
    return render(request, "principal/usuarios/listar.html", context)
def visualizar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion visualizar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Visualizacion"

    context["data"] = Usuarios.objects.get(id = id)
    return render(request, "principal/usuarios/detalle.html", context)
def crear_usuarios(request):
    logger.warning('Se ejecuta la funcion crear_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Creacion"

    form = UsuariosForm(request.POST or None)
    if request.method == 'GET':
        context['form']= form
        return render(request, "principal/usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning('El usuario ha sido creado de manera exitosa.')
                messages.success(request, 'El usuario ha sido creado de manera exitosa.')
                return redirect('departamentos')
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
def eliminar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion eliminar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    obj = get_object_or_404(Usuarios, id = id)
    if request.method =="POST":
        obj.delete()
        logger.warning(f'Usuario {id} eliminado de manera exitosa.')
        messages.success(request, f'Usuario {id} eliminado de manera exitosa.')
        return HttpResponseRedirect("/")
    return render(request, "principal/usuarios/listar.html", context)

def actualizar_usuarios(request, id):
    logger.warning('Se ejecuta la funcion actualizar_usuarios a las  '+str(datetime.datetime.now())+' horas!')

    context ={}
    context["titulo"] = "Usuarios"
    context["accion"] = "Actualizacion"

    obj = get_object_or_404(Usuarios, id = id)
    form = UsuariosForm(request.POST or None, instance = obj)
    if request.method == 'GET':
        context["form"] = form
        return render(request, "principal/usuarios/detalle.html", context)
    elif request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                logger.warning(f'Usuario {id} ha sido actualizado de manera exitosa.')
                messages.success(request, f'Usuario {id} ha sido actualizado de manera exitosa.')
                return HttpResponseRedirect("campus")
            else:
                logger.warning('Se han generado errores de validacion')
                messages.error(request, 'Porfavor corrige los errores:')
                return render(request, "principal/usuarios/detalle.html", {'context':context,'form':form})
        except:
            logger.warning('Ha ocurrido un error inesperado.')
            messages.error(request, 'Ha ocurrido un error inesperado.')
