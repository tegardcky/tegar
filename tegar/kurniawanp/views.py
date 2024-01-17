from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from decky.models import Produk
from .keranjang import Cart
from .forms import CartAddProductForm



def cart_add(request, product_id):
    cart = Cart(request)  # Create a new cart object passing it the request object
    product = get_object_or_404(Produk, id=product_id)
    quantity = int(request.POST.get('quantity'))
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=quantity, update_quantity=cd['update'])
    
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produk, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    context = {
        'judul': 'Halaman Pemesanan Produk',
        'cart': cart
    }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'pemesanan.html', context)
