from django import forms
from .models import Pengguna

class SearchForm(forms.Form):
    city = forms.CharField(label='Kota', max_length=100, required=False)
    state = forms.CharField(label='Provinsi', max_length=100, required=False)

class PenggunaForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = ['email', 'address_1', 'city', 'state']


class UploadFileForm(forms.Form):
    file = forms.FileField()