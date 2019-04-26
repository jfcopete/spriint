# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class AdminProducto (admin.ModelAdmin):
	search_fields=['nombre',]
	class Meta:
		model=Producto

class AdminVenta (admin.ModelAdmin):
	search_fields=['nombre',]
	class Meta:
		model=Venta

# Register your models here.
admin.site.register(Producto, AdminProducto)
admin.site.register(Comprador)
admin.site.register(Inventario)
admin.site.register(PuntoDeVenta)
admin.site.register(Caja)
admin.site.register(Venta, AdminVenta)
admin.site.register(Item)
admin.site.register(Factura)