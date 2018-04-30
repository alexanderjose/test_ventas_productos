# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from test_ventas_productos.ventas.models import (
    Tienda, Marca, Categoria, SubCategoria, Venta, Producto
)
from test_ventas_productos.ventas.serializers import (
    TiendasSerializer, MarcasSerializer, CategoriasSerializer,
    SubCategoriasSerializer, VentasSerializer, VentasUnidadesSerializers
)
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.generic import (
    TemplateView
)
from django.db.models.functions import TruncYear, TruncMonth
from django.db.models import Sum


@csrf_exempt
def listado_tiendas(request):
    """
    """
    if request.method == 'GET':
        ventas = Tienda.objects.all()
        serializer = TiendasSerializer(ventas, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = VentasSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JSONResponse(serializer.data, status=201)
    #     return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def listado_marcas(request):
    """
    """
    if request.method == 'GET':
        mentas = Marca.objects.all()
        serializer = MarcasSerializer(mentas, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def listado_categorias(request):
    """
    """
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def listado_subcategorias(request):
    """
    """
    if request.method == 'GET':
        subcategorias = SubCategoria.objects.all()
        serializer = SubCategoriasSerializer(subcategorias, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def listado_ventas(request):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.all()
        serializer = VentasSerializer(ventas, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def listado_ventas_unidades(request):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.annotate(
                year=TruncYear('fecha')
            ).annotate(
                month=TruncMonth('fecha')
            ).values(
                'year', 'month'
            ).annotate(
                unidades=Sum('venta_unidades')
            ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_unidades_tienda(request, tienda):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.filter(
            id_tienda=tienda
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_unidades')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_unidades_tienda_marca(request, tienda, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        print(productos)
        ventas = Venta.objects.filter(
            id_tienda=tienda,
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_unidades')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_unidades_marca(request, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_unidades')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def listado_ventas_pesos(request):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.filter().annotate(
                year=TruncYear('fecha')
            ).annotate(
                month=TruncMonth('fecha')
            ).values(
                'year', 'month'
            ).annotate(
                unidades=Sum('venta_pesos')
            ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_pesos_tienda(request, tienda):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.filter(
            id_tienda=tienda
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_pesos')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_pesos_tienda_marca(request, tienda, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        print(productos)
        ventas = Venta.objects.filter(
            id_tienda=tienda,
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_pesos')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_pesos_marca(request, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_pesos')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def listado_ventas_descuentos(request):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.annotate(
                year=TruncYear('fecha')
            ).annotate(
                month=TruncMonth('fecha')
            ).values(
                'year', 'month'
            ).annotate(
                unidades=(Sum('venta_pesos') - Sum('venta_descuento'))
            ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_descuentos_tienda(request, tienda):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.filter(
            id_tienda=tienda
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=(Sum('venta_pesos') - Sum('venta_descuento'))
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_descuentos_tienda_marca(request, tienda, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_tienda=tienda,
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=(Sum('venta_pesos') - Sum('venta_descuento'))
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_descuentos_marca(request, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=(Sum('venta_pesos') - Sum('venta_descuento'))
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def listado_ventas_costo(request):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.annotate(
                year=TruncYear('fecha')
            ).annotate(
                month=TruncMonth('fecha')
            ).values(
                'year', 'month'
            ).annotate(
                unidades=Sum('venta_descuento')
            ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_costos_tienda(request, tienda):
    """
    """
    if request.method == 'GET':
        ventas = Venta.objects.filter(
            id_tienda=tienda
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_descuento')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_costos_tienda_marca(request, tienda, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_tienda=tienda,
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_descuento')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


@csrf_exempt
def ventas_costos_marca(request, marca):
    """
    """
    if request.method == 'GET':
        productos = Producto.objects.filter(id_marca=marca).values('id')
        ventas = Venta.objects.filter(
            id_producto__in=productos
        ).annotate(
            year=TruncYear('fecha')
        ).annotate(
            month=TruncMonth('fecha')
        ).values(
            'year', 'month'
        ).annotate(
            unidades=Sum('venta_descuento')
        ).order_by('fecha')
        serializer = VentasUnidadesSerializers(ventas)
        return JsonResponse(serializer, safe=False)


class DashboardView(TemplateView):
    template_name = 'ventas/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        # user = self.request.user
        # if user.is_anonymous():
        #     return super(DashboardView, self).dispatch(
        #         request, *args, **kwargs)

        return super(DashboardView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['grettings'] = 'Hola'
        return context
