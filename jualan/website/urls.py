from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name="beranda"),
    path('profil-kami', views.profil, name="profil"),
    path('hubungi-kami', views.kontak, name="kontak"),
    path('produk-kami', views.produk, name="produk"),
    path('pemesanan-kami', views.pemesanan, name="pemesanan"),
    path('<slug:slug>', views.kategori, name='kategori'),
    
]

