from django.shortcuts import render
from .models import User

# Create your views here.

def get_users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'user/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, name=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
            return profile(request, username)
    else:
        return render(request, 'user/login.html')

def creat_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(name=username).exists():
            messages.error(request, f'{username} - уже зарегистрирован')
            return redirect('creat')
        user = User.objects.create(name=username, password=password)
        user.save()
        return redirect('index')
    return render(request, 'user/creat.html')


