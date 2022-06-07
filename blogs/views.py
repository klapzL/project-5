from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_list(request):
    context = {

    }
    return render(request, 'blogs/blog_list.html', context)

@login_required
def blog_create(request):
    # if request.METHOD == 'POST':

    context = {

    }
    return render (request, 'blogs/blog_create.html', context)