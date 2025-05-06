from django.shortcuts import render, get_object_or_404
from .forms import PenggunaForm
from .models import Pengguna

def set_pengguna(request):
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PenggunaForm()
    
    pengguna_list = Pengguna.objects.all()
    return render(request, 'data_entry/input_data_1.html', {
        'form': form,
        'list_pengguna': pengguna_list
    })

def view_pengguna(request, pk):
    pengguna = get_object_or_404(Pengguna, pk=pk)
    return render(request, 'data_entry/pengguna_detail.html', {
        'pengguna': pengguna
    })
