from django import forms
from .models import Dispositivo

class dispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'categoria','zona', 'consumo_maximo', 'estado']