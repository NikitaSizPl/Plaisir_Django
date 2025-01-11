from django.urls import path
from .views import profil


urlpatterns = [

    path('profile', profil, name="profil")
]
