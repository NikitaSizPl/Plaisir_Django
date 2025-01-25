from django.urls import path

from .views import *

urlpatterns = [

    path("", index, name="index"),
    path("categories/", categories, name="categories"),
    path("categories/<str:cat_name>/items", items_categor, name="items_categor"),
    path('item/<int:item_id>', item_id, name='item_id')
]
