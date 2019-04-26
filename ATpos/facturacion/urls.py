from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.urls import path

urlpatterns = [
    url('^$', views.index),
   # url(r'', include('pwa.urls')),
    url(r'^productos/', views.Productos),
    url(r'^ventas/', views.Ventas),
    url(r'^facturas/', views.Facturas),
    url(r'^producto/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
    url(r'^factura/$', csrf_exempt(views.FacturaCreate), name='facturaCreate'),
    url(r'^venta/$', csrf_exempt(views.VentaCreate), name='ventaCreate'),
    url(r'^productoSearch/', views.ProductoSearch),
    url(r'^base_layout/', views.base_layout),
    url(r'^getdata/', views.getdata),

    url(r'^index/', views.index),

    #path('', views.index),

    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),

]
