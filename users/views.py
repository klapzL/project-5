from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm

# Create your views here.
def register_page(request):
    context = {

    }
    return render(request, 'users/register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                redirect('register_page')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)