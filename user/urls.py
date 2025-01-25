from django.urls import path
from .views import profile, login_user, creat_user


urlpatterns = [
    path('login', login_user, name="login"),
    path('creat', creat_user, name='creat'),
    path('user/<str:username>', profile, name='profile')

]
