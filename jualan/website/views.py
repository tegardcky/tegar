from django.shortcuts import render
from .models import Produk, Kategori, Kontak, Profil, Slide, Statis
from cart.models import Transaksi, DetailTransaksi
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .models import Kategori


def beranda(request):
    kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    slider = Slide.objects.filter(aktif=True).order_by('-id')
    jumlahkategori = Kategori.objects.all().annotate(produk_count=Count('produks')).order_by('-id')
    trending = Produk.objects.order_by('-dibeli')
    context = {
            "judul": "Halaman Beranda",
            "kategori" : kategori,       
            "jumlahkategori":jumlahkategori,
            "slide": slider,
            "trending":trending, 
            
    }

    return render(request, 'beranda.html', context)

def profil(request):
    profil =  Profil.objects.all().order_by('-id')[:1]
    context = {"judul": "Halaman Profil","profil":profil,}
    return render(request, 'profil.html', context)

def kontak(request):
    context = {
            "judul": "Halaman Hubungi Kami",
    }
    return render(request, 'kontak.html', context)

def produk(request):
    context = {
            "judul": "Halaman Hubungi Kami",
    }
    return render(request, 'produk.html', context)

def pemesanan(request):
    context = {
            "judul": "Halaman Hubungi Kami",
    }
    return render(request, 'pemesanan.html', context)

def kategori(request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    produk = kategori.produks.order_by('-id')
    context = {
        "judul": "Halaman Kategori",
        "detailkategori": produk,
        "categories":kategori
    }
    return render(request, 'kategori.html', context)


def kategoriberanda(request):
    kategori = Kategori.objects.filter(aktif=True).order_by('-id')
    return {'kategori':kategori} 

def modalberita(request): 
    modalproduk = Produk.objects.order_by('-id')     
    return {'modalproduk':modalproduk}
 
def statisweb(request): 
    statis = Statis.objects.get(id=4)   
    return {'statis':statis} 


