from django.urls import path

from .views import basket, add_to_basket, remove_to_basket

urlpatterns = [

    path("", basket, name="basket"),
    path('add/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('remove/<int:product_id>/', remove_to_basket, name='add_to_basket'),
]
