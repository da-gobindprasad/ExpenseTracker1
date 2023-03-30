from django.shortcuts import render

# Create your views here.


def loginView(request):
    return render(request, 'users/login.html')


def registerView(request):
    return render(request, 'users/register.html')
