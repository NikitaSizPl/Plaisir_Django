from django.urls import path
from .views import basket_base, add_to_basket, del_from_basket, del_all

app_name = 'basket'

urlpatterns = [
    path('basket/', basket_base, name='basket'),
    path('add/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('del/<int:product_id>/', del_from_basket, name='del_from_basket'),
    path('del/all/', del_all, name='del_all'),
    # path('upg/<int:product_id>/', upg_from_basket, name='upg_from_basket'),
]
