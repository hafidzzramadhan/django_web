from django import forms
from .models import Pengguna

class PenggunaForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = '__all__'
