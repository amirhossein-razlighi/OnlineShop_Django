from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart_sessions import Cart
from cart.forms import AddToCartForm
from shop.models import Product


def detail(request):
    cart = Cart(request=request)
    return render(request, 'cart/detail.html', context={'cart': cart})


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        c_data = form.cleaned_data
        cart.add(product=product, quantity=c_data['quantity'])
    return redirect('cart:detail')
