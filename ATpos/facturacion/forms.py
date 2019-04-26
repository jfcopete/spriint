from django import forms
from .models import *
from django.forms import ModelChoiceField

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'




class VentaForm(forms.ModelForm):
    #caja = CajaModelChoiceField(queryset=Caja.objects.all())
    class Meta:
        model = Venta
        fields = fields = '__all__'

class FacturaForm(forms.ModelForm):
    #caja = CajaModelChoiceField(queryset=Caja.objects.all())
    class Meta:
        model = Factura
        fields = fields = '__all__'

