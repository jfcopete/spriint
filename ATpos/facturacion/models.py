# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from cryptography.fernet import Fernet
import hashlib


# Create your models here.

class Producto (models.Model):
	nombre= models.CharField(max_length=100, blank= False, null=False)
	precio= models.DecimalField(max_digits=10, decimal_places=2)
	iva= models.BooleanField()
	cantidad= models.IntegerField()

	def __str__(self):
		return self.nombre

class Comprador( models.Model):
	nombre= models.CharField(max_length=34, blank= False, null=False)
	apellido=models.CharField(max_length=34, blank= False, null=False)
	direccion=models.CharField(max_length=54, blank= False, null=False)

	cc=models.IntegerField()

	def __str__(self):
		return self.nombre

class Inventario (models.Model):
	fecha= models.DateTimeField()

	def __str__(self):
		return self.fecha

class PuntoDeVenta (models.Model):
	direccion= models.CharField(max_length=34, blank= False, null=False)

	def __str__(self):
		return self.direccion

class Caja (models.Model):
	punto = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
	numero=models.IntegerField()

	def __str__(self):
		return self.punto.direccion

class Venta (models.Model):

	Caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
	fecha= models.DateTimeField(default= timezone.now())
	total = models.CharField(max_length=34, blank=False, null=False)

	def __str__(self):
		return self.total


class Item (models.Model):

	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

	venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='photos')
	costo= models.DecimalField(max_digits=10, decimal_places=2)
	iva= models.DecimalField(max_digits=10, decimal_places=2,default='0.19')

	def __str__(self):
		return self.producto.nombre


class Factura( models.Model):
	#venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
	comprador = models.ForeignKey(Comprador,on_delete = None, null=True)

	def __str__(self):
		return self.comprador.nombre

def crearLlave():
	key = Fernet.generate_key()
	file = open('key.key', 'wb')
	file.write(key)
	file.close()

def leerLlave():
	file = open('C:\\Users\m.diazt\Arqui\ISIS2503-201910-S4-InfiniteLoop\ATpos\docs\key.key', 'r')
	key = file.read()  # The key will be type bytes
	file.close()

def encriptar(mensaje, llave):
	mens = mensaje.encode()
	f = Fernet(llave)
	cifrado = f.encrypt(mens)
	return cifrado

def decriptar(mensajeCifrado, llave):
	f = Fernet(llave)
	decriptado = f.decrypt(mensajeCifrado)
	return decriptado.decode()

def hash(mensaje):
	mes = mensaje.encode()
	return hashlib.md5(mes).hexdigest()

