from django.shortcuts import render
from .models import User

# Create your views here.

def get_users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'user/profile.html', context)

