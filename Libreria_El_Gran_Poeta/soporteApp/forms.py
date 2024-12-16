from django import forms
from .models import TicketSoporte

class TicketSoporteForm(forms.ModelForm):
    class Meta:
        model = TicketSoporte
        fields = ['asunto', 'descripcion', 'prioridad']
        widgets = {
            'asunto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingresa el asunto del ticket'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Describe el problema con detalle',
                'rows': 5
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'asunto': 'Asunto',
            'descripcion': 'Descripción',
            'prioridad': 'Prioridad',
        }
