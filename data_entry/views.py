from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Pengguna
from .forms import SearchForm, PenggunaForm, UploadFileForm
import os


def set_pengguna(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')

        request.session['email'] = email
        request.session['city'] = city
        request.session['state'] = state

        Pengguna.objects.create(
            email=email,
            address_1='-', 
            city=city,
            state=state
        )

        return redirect('data_entry:content')
    return render(request, 'data_entry/set_pengguna.html')


def content(request):
    email = request.session.get('email', '')
    list_pengguna = Pengguna.objects.all()

    return render(request, 'data_entry/content.html', {
        'email': email,
        'list_pengguna': list_pengguna
    })


def view_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    return render(request, 'data_entry/pengguna_detail.html', {
        'pengguna': pengguna
    })


def update_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    form = PenggunaForm(request.POST or None, instance=pengguna)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('data_entry:content')

    return render(request, 'data_entry/update_pengguna.html', {
        'form': form,
        'pengguna': pengguna
    })


def delete_pengguna(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)

    if request.method == 'POST':
        pengguna.delete()
        return redirect('data_entry:content')

    return render(request, 'data_entry/delete_confirm.html', {
        'pengguna': pengguna
    })


def search_pengguna(request):
    form = SearchForm()
    results = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            results = Pengguna.objects.all()
            if city:
                results = results.filter(city__icontains=city)
            if state:
                results = results.filter(state__icontains=state)

    return render(request, 'data_entry/search_pengguna.html', {
        'form': form,
        'results': results
    })


def upload_file(request):
    email = request.session.get('email', 'Belum diisi')
    city = request.session.get('city', '-')
    state = request.session.get('state', '-')

    if request.method == 'POST' and request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            return redirect('data_entry:upload_success')
    else:
        form = UploadFileForm()

    return render(request, 'data_entry/upload_file.html', {
        'form': form,
        'email': email,
        'city': city,
        'state': state
    })


def upload_success(request):
    return render(request, 'data_entry/upload_success.html')


def photo_list(request):
    media_dir = settings.MEDIA_ROOT
    files = []

    for filename in os.listdir(media_dir):
        filepath = os.path.join(settings.MEDIA_URL, filename)
        files.append({'name': filename, 'url': filepath})

    return render(request, 'data_entry/menu_upload/photo_list.html', {'files': files})
