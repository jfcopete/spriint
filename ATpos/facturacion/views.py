# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib import messages
from django.http import *
from django.urls import reverse
from .forms import *
from cryptography.fernet import Fernet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

import json

def index(request):
    return render(request, 'index.html')
def base_layout(request):
	template='base.html'
	return render(request,template)
def getdata(request):
	results=Producto.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)
def Productos(request):
    queryset = Producto.objects.all()[:10]
    context = {
        'productos': queryset
    }
    return render(request, 'Producto/productos.html', context)

def Facturas(request):
    queryset = Factura.objects.all()[:10]
    context = {
        'facturas': queryset
    }
    return render(request, 'Factura/facturas.html', context)

def Ventas(request):
    queryset = Venta.objects.all()[:10]
    context = {
        'ventas': queryset
    }
    return render(request, 'Venta/ventas.html', context)


def ProductoSearch(request):
	p = request.GET.get('q', '');
	queryset = Producto.objects.filter(nombre__icontains=p)[:10]
	context = {
		'productos': queryset,
		'p': p,
	}
	return render(request, 'Producto/search.html', context)

def ProductoCreate(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			measurement = form.save()
			measurement.save()
			messages.add_message(request, messages.SUCCESS, 'Producto creado correctamente')
		else:
			print(form.errors)
	else:
		form = ProductoForm()

	context = {
		'form': form,
	}

	return render(request, 'Producto/producto.html', context)

def VentaCreate(request):
	if request.method == 'POST':
		form = VentaForm(request.POST)
		if form.is_valid():
			measurement = form.save()
			measurement.save()
			messages.add_message(request, messages.SUCCESS, 'Producto creado correctamente')
			#return HttpResponseRedirect(reverse('VentaSerializer'))
		else:
			print(form.errors)
	else:
		form = VentaForm()

	context = {
		'form': form,
	}

	return render(request, 'Venta/venta.html', context)

def FacturaCreate(request):
	if request.method == 'POST':
		form = FacturaForm(request.POST)
		if form.is_valid():
			measurement = form.save()
			measurement.save()
			messages.add_message(request, messages.SUCCESS, 'Factura creado correctamente')
			#return HttpResponseRedirect(reverse('VentaSerializer'))
		else:
			print(form.errors)
	else:
		form = FacturaForm()

	context = {
		'form': form,
	}

	return render(request, 'Factura/factura.html', context)

# auth0login/views.py

def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
