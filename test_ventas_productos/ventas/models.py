from django.db import models
from django.utils import timezone


class Tienda(models.Model):
    descripcion = models.CharField(max_length=255, null=True)


class Marca(models.Model):
    descripcion = models.CharField(max_length=255, null=True)


class Categoria(models.Model):
    descripcion = models.CharField(max_length=255, null=True)


class SubCategoria(models.Model):
    id_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255, null=True)


class Producto(models.Model):
    id_marca = models.ForeignKey('Marca', on_delete=models.PROTECT)
    id_subcategoria = models.ForeignKey(
        'SubCategoria', on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Venta(models.Model):
    id_producto = models.ForeignKey('Producto', on_delete=models.PROTECT)
    id_tienda = models.ForeignKey('Tienda', on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=timezone.now)
    venta_unidades = models.IntegerField()
    venta_pesos = models.DecimalField(max_digits=14, decimal_places=2)
    venta_descuento = models.DecimalField(max_digits=14, decimal_places=2)
