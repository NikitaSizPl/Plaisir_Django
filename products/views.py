from .models import Catigories, Item
from django.shortcuts import render


def categories(request):
    categor = Catigories.objects.all()
    context = {
        "categor": categor
    }
    return render(request,
                  "products/categories.html",
                  context
                  )


def items_categor(request, cat_name):
    categor = Catigories.objects.get(name=cat_name)
    products = Item.objects.filter(categories__name=cat_name)
    context = {
        'products' : products,
        'categor': categor
    }
    return render(request,
                  "products/categories_slug.html",
                  context
                  )


def item_id(request, item_id):
    product = Item.objects.get(id=item_id)
    context = {
        'product': product
    }
    return render(request,
                  "products/item_id.html",
                  context
                  )


def index(request):
    items = Item.objects.all()
    categor = Catigories.objects.all()
    context = {
        'items': items,
        'categor': categor
    }
    return render(request,
                  'products/index.html',
                  context
                  )