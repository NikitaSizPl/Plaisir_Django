from django.urls import path

from .views import categories, items_categor, item_id

urlpatterns = [

    path("", categories, name="categories"),
    path("categories/<str:cat_name>/items", items_categor, name="items_categor"),
    path('item/<str:item_str>', item_id, name='item_id')
]
