from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views_api import ContentViewSet  # pastikan ContentViewSet sudah dibuat

app_name = 'data_entry'

# Router untuk API
router = DefaultRouter()
router.register(r'api/content', ContentViewSet)

urlpatterns = [
    path('', views.set_pengguna, name='set_pengguna'),
    path('view/<int:pk>/', views.view_pengguna, name='view_pengguna'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('content/', views.content, name='content'),
    path('search/', views.search_pengguna, name='search_pengguna'),
    
    path('pengguna/<int:id>/delete', views.delete_pengguna, name='deletedata'),
    path('uploads/', views.photo_list, name='photo_list'),
    path('pengguna/<int:id>/view', views.view_pengguna, name='viewdata'),
    path('pengguna/<int:id>/update', views.update_pengguna, name='updatedata'),
    



    # Tambah ini:
    path('', include(router.urls)),
]
