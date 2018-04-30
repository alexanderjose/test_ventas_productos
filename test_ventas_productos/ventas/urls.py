from django.conf.urls import url
from test_ventas_productos.ventas import views


urlpatterns = [
    url(r'^tiendas/$', views.listado_tiendas),
    url(r'^marcas/$', views.listado_marcas),
    url(r'^categorias/$', views.listado_categorias),
    url(r'^subcategorias/$', views.listado_subcategorias),
    url(r'^listado/$', views.listado_ventas),
    url(r'^unidades/$', views.listado_ventas_unidades),
    url(
        r'^unidades/tienda/(?P<tienda>[0-9]+)/$',
        views.ventas_unidades_tienda
    ),
    url(
        r'^unidades/marca/(?P<marca>[0-9]+)/$',
        views.ventas_unidades_marca
    ),
    url(
        r'^unidades/tienda/(?P<tienda>[0-9]+)/marca/(?P<marca>[0-9]+)/$',
        views.ventas_unidades_tienda_marca
    ),
    url(r'^pesos/$', views.listado_ventas_pesos),
    url(r'^pesos/tienda/(?P<tienda>[0-9]+)/$', views.ventas_pesos_tienda),
    url(
        r'^pesos/marca/(?P<marca>[0-9]+)/$',
        views.ventas_pesos_marca
    ),
    url(
        r'^pesos/tienda/(?P<tienda>[0-9]+)/marca/(?P<marca>[0-9]+)/$',
        views.ventas_pesos_tienda_marca
    ),
    url(r'^descuentos/$', views.listado_ventas_descuentos),
    url(
        r'^descuentos/tienda/(?P<tienda>[0-9]+)/$',
        views.ventas_descuentos_tienda
    ),
    url(
        r'^descuentos/tienda/(?P<tienda>[0-9]+)/marca/(?P<marca>[0-9]+)/$',
        views.ventas_descuentos_tienda_marca
    ),
    url(
        r'^descuentos/marca/(?P<marca>[0-9]+)/$',
        views.ventas_descuentos_marca
    ),
    url(r'^costos/$', views.listado_ventas_costo),
    url(r'^costos/tienda/(?P<tienda>[0-9]+)/$', views.ventas_costos_tienda),
    url(
        r'^costos/tienda/(?P<tienda>[0-9]+)/marca/(?P<marca>[0-9]+)/$',
        views.ventas_costos_tienda_marca
    ),
    url(
        r'^costos/marca/(?P<marca>[0-9]+)/$',
        views.ventas_costos_marca
    ),
    url(r'^dashboard$',
        views.DashboardView.as_view(),
        name='dashboard_home'),
]
