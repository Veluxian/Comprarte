from django import forms
from django.contrib.auth.models import User
from .models import Obras

class clienteFormulario(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email",]
        labels = {'first_name':'Nombre',
                  'last_name':'Apellido',
                  'email':'Correo Electronico',}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

class ObrasFormulario(forms.ModelForm):
    class Meta:
        model = Obras
        exclude = ('idUsuario',)
        fields = ["Obras","descripcion","imagen","estado"]
        widgets = {
            'estado': forms.TextInput(attrs={'type': 'hidden'}),
        }