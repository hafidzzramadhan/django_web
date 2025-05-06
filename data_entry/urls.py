from django.urls import path
from . import views

app_name = 'data_entry'

urlpatterns = [
    path('', views.set_pengguna, name='set_pengguna'),
    path('view/<int:pk>/', views.view_pengguna, name='view_pengguna'),
]
