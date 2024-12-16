from django import forms
from django.contrib.auth.models import User
from LibreriaApp.models import Bodega, Libro, Autor

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'