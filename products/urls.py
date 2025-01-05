from django.urls import path

from .views import categories, categories_id, item, item_id

urlpatterns = [

    path("categories/", categories, name="categories"),
    path('categories/<int:cat_id>/', categories_id, name='categories_id'),
    path("item/", item, name="item"),
    path('item/<int:id>', item_id, name='item_id')
]
