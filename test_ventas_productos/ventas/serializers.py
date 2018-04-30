from rest_framework import serializers
from .models import (Tienda, Marca, Categoria, SubCategoria, Venta)


class TiendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ('id', 'descripcion')


class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'descripcion')


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'descripcion')


class SubCategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = ('id', 'descripcion')


class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = (
            'id', 'fecha', 'venta_unidades', 'venta_pesos', 'venta_descuento'
        )


def VentasUnidadesSerializers(ventas):
    # import dateutil.parser as parser
    from dateutil.parser import parse
    listado_unidades = []
    unidades_mes = {}
    for v in ventas:
        # print(v.get('month'))
        unidades_mes['year'] = parse(str(v.get('year'))).year
        unidades_mes['month'] = parse(str(v.get('month'))).month
        unidades_mes['units'] = v.get('unidades')
        listado_unidades.append(unidades_mes)
        unidades_mes = {}
    return listado_unidades


# def VentasDescuentoSerializers(ventas):
#     # import dateutil.parser as parser
#     from dateutil.parser import parse
#     listado_unidades = []
#     unidades_mes = {}
#     for v in ventas:
#         # print(v.get('month'))
#         unidades_mes['year'] = parse(str(v.get('year'))).year
#         unidades_mes['month'] = parse(str(v.get('month'))).month
#         unidades_mes['units'] = v.get('cantidades')
#         listado_unidades.append(unidades_mes)
#         unidades_mes = {}
#     return listado_unidades
