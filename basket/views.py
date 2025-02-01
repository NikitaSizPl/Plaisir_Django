from django.shortcuts import render, redirect, get_object_or_404
from basket.models import Basket, BasketItem
from products.models import Product


# Create your views here.
def basket_base(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        if not basket:
            basket = Basket.objects.create(user=request.user)
    else:
        basket_id = request.session.get('basket_id')
        if not basket_id:
            basket = Basket.objects.create()
            request.session['basket_id'] = basket.id
        else:
            basket = Basket.objects.get(id=basket_id)
    context = {
        'basket': basket,
        'basket_item': BasketItem.objects.filter(basket=basket)
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket, create = Basket.objects.get_or_create(user=request.user)
    basket_item, create = BasketItem.objects.get_or_create(basket=basket, product=product, quantity=1)
    if not create:
        if product in basket_item:
            basket_item.quantity += 1
            basket_item.save()
    return redirect('basket:basket')


def del_from_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket, create = Basket.objects.get_or_create(user=request.user)
    basket_item, create = BasketItem.objects.get_or_create(basket=basket, product=product)
    if not create:
        basket_item.quantity -= 1
        basket_item.save()
    return redirect('basket:basket')


def del_all(request):
    basket = Basket.objects.get(user=request.user)
    if basket:
        basket.clear()
    return redirect('basket:basket')