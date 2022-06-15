from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.db.models import Q


# Create your views here.
def blog_list(request):
    q = request.GET.get('q', '')
    q_user = request.GET.get('q_user', '')
    ordering = request.GET.get('ordering', '-id')
    blogs = Blog.objects.all()
    if q or q_user:
        blogs = Blog.objects.filter((Q(title__icontains=q) | Q(text__icontains=q)) & Q(author__username__icontains=q_user))
    if ordering == 'id':
        blogs = blogs.order_by('id')
        ordering = '-id'
    else:
        blogs = blogs.order_by('-id')
        ordering = 'id'
    context = {
        'blogs': blogs,
        'ordering': ordering,
        'q': q,
        'q_user': q_user
    }
    return render(request, 'blogs/blog_list.html', context)

@login_required(login_url='login_page')
def blog_create(request):
    # if request.METHOD == 'POST':

    context = {

    }
    return render (request, 'blogs/blog_create.html', context)