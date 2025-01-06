from .models import Catigories, Item
from django.shortcuts import render


# def index(request):
# return HttpResponse("index")


def categories(request):
    categor = Catigories.objects.all()
    return render(request,
                  "products/categories.html",
                  {"categor": categor}
                  )


def items_categor(request, cat_name):
    cat = Catigories.objects.get(name=cat_name)
    items = Item.objects.filter(categories__name=cat_name)
    return render(request,
                  "products/categories_slug.html",
                  {"items": items, "cat": cat}
                  )


def item_id(request, item_str):
    item = Item.objects.get(name=item_str)
    return render(request,
                  "products/item_id.html",
                  {'item': item}
                  )
