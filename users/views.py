from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from .forms import RegistrationForm


# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Code's working!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('blog_list')