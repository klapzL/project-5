from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
def blog_list(request):
    ordering = request.GET.get('ordering', '-id')
    blogs = Blog.objects.all()
    if ordering == 'id':
        blogs = blogs.order_by('id')
        ordering = '-id'
    else:
        blogs = blogs.order_by('-id')
        ordering = 'id'
    context = {
        'blogs': blogs,
        'ordering': ordering
    }
    return render(request, 'blogs/blog_list.html', context)

@login_required(login_url='login_page')
def blog_create(request):
    # if request.METHOD == 'POST':

    context = {

    }
    return render (request, 'blogs/blog_create.html', context)