from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import Profile


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

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
    if request.user.is_authenticated:
        return redirect('main_page')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Code's working!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                u_id = user.id
                print(u_id)
                return redirect('profile_page', profile_id=user.profile.id)
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('blog_list')


def profile_page(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id
    )
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context)

