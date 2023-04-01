from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.


def registerView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been added')

            return redirect('login')

    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
