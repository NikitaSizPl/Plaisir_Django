from django.shortcuts import render, redirect, get_object_or_404
from basket.models import Basket, BasketItem
from products.models import Product
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def basket_base(request):
    # если пользователь авторизован
    if request.user.is_authenticated:
        # получаем корзину авторизованого пользователя
        basket = Basket.objects.filter(user=request.user).first()
        if not basket:
            # создаем корзину для пользователя
            basket = Basket.objects.create(user=request.user)
    # если пользователь не авторизован
    else:
        # получаем корзину из сессии
        basket_id = request.session.get(settings.BASKET_SESSION_ID)
        if not basket_id:
            # создаем корзину для сессии
            basket = Basket.objects.create()
            request.session[settings.BASKET_SESSION_ID] = basket.id
        else:
            # получаем корзину если она создана
            basket = Basket.objects.get(id=basket_id)
    context = {
        'basket': basket,
        'basket_item': BasketItem.objects.filter(basket=basket),
    }
    return render(request, 'basket/basket.html', context)


def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    # Для анонимных пользователей
    else:
        basket_id = request.session.get('basket_id')
        basket = Basket.objects.get(id=basket_id)
        if not basket_id:
            basket = Basket.objects.create()
            request.session['basket_id'] = basket.id
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()

    if basket_item:
        basket_item.quantity += 1
        basket_item.save()
    else:
        BasketItem.objects.create(basket=basket, product=product, quantity=1)
    return redirect('basket:basket')


def del_from_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    else:
        # Для анонимных пользователей
        basket = request.session.get('basket_id')
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()
    if basket_item:
        basket_item.delete()
    return redirect('basket:basket')


def del_all(request):
    # Для авторизованых пользователей
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
    # Для анонимных пользователей
    else:
        basket_id = request.session.get('basket_id')
        basket = Basket.objects.get(id=basket_id)
    if basket:
        basket.clear()
    else:
        return redirect('products:index')
    return redirect('products:index')