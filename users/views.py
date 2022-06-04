from django.shortcuts import render

# Create your views here.
def register(request):
    context = {

    }
    return render(request, 'users/register.html', context)


def login(request):
    context = {

    }
    return render(request, 'users/login.html', context)