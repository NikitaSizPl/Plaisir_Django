from django.urls import path

from .views import *

urlpatterns = [

    path("", index, name="index"),
    path("delivery/", delivery, name="delivery"),
    path("infopay/", infopay, name="infopay"),
    path("contact/", contact, name="contact"),
    path("categories/", categories, name="categories"),
    path("categories/<str:cat_name>/items", items_categor, name="items_categor"),
    path('item/<str:item_str>', item_id, name='item_id')
]
