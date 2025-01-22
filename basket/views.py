from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket, BasketItem
from products.models import Item



# Create your views here.
def get_or_creat_basket(request):
    basket_id = request.session.get('basket_id')
    if not basket_id:
        basket = Basket.objects.create()
        request.session['basket_id'] = basket.id
    else:
        basket = get_object_or_404(Basket, id=basket_id)
    return basket



def basket(request):
   basket = get_or_creat_basket(request)
   context = {'basket': basket}
   return render(request,
                 'basket/get_all.html',
                 context)

def add_to_basket(request, product_id):
    item = get_object_or_404(Item, id=product_id)
    basket = get_or_creat_basket(request)
    quantity = int(request.POST.get('quantity', 1))
    basket_item, creat = BasketItem.objects.get_or_create(basket=basket, item=item)
    if creat:
        basket_item.quantity = quantity
    else:
        basket_item.quantity += quantity
    basket_item.save()
    return redirect("basket")

def remove_to_basket(request, product_id):
    item = get_object_or_404(Item, id=product_id)
    basket = get_or_creat_basket(request)
    basket_item = BasketItem.objects.get_or_create(basket=basket, item=item)
    if basket_item:
        basket_item.quantity -= 1
        if basket_item <= 0:
            basket_item.delete()
        else:
            basket_item.save()
    return redirect("basket")
