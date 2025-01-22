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
    cat = Catigories.objects.get(name=cat_name)
    items = Item.objects.filter(categories__name=cat_name)
    context = {
        'items' : items,
        'cat': cat
    }
    return render(request,
                  "products/categories_slug.html",
                  context
                  )


def item_id(request, item_str):
    item = Item.objects.get(name=item_str)
    context = {
        'item': item
    }
    return render(request,
                  "products/item_id.html",
                  context
                  )


def index(request):
    return render(request,
                  'products/index.html'
                  )
def delivery(request):
    return render(request,
                  'add/delivery.html'
                  )

def delivery(request):
    return render(request,
                  'products/delivery.html'
                  )

def infopay(request):
    return render(request,
                  'products/infopay.html'
                  )

def contact(request):
    return render(request,
                  'products/contact.html'
                  )