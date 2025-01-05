from django.http import HttpResponse
from .models import Catigories, Item


def index(request):
    return HttpResponse("index")


def categories(request):
    get_cat = Catigories.objects.all()
    cat_names = ', '.join([cat.name for cat in get_cat])
    return HttpResponse(f"Categories: {cat_names}")


def categories_id(request, cat_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % cat_id)


def item(request):
    get_item = Item.objects.all()
    item_names = ', '.join([item.name for item in get_item])
    return HttpResponse(f"Items: {item_names}")


def item_id(request, id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % id)
