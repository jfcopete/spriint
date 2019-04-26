from rest_framework import serializers
from . import models


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Producto

class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        fields =  '__all__'
        model = models.Venta

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        fields =  '__all__'
        model = models.Factura