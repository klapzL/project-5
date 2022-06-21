from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import BlogForm

BLOGS_PER_PAGE = 6


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    q = request.GET.get('q', '')
    q_user = request.GET.get('q_user', '')
    page_number = request.GET.get('page')
    ordering = request.GET.get('ordering', '-id')
    paginator = Paginator(blogs, BLOGS_PER_PAGE)
    if q or q_user:
        blogs = Blog.objects.filter((Q(title__icontains=q)
                                     | Q(text__icontains=q))
                                    & Q(author__username__icontains=q_user))
    if ordering == 'id':
        blogs = blogs.order_by('id')
        paginator = Paginator(blogs, BLOGS_PER_PAGE)
        ordering = '-id'
    elif ordering == '-id':
        blogs = blogs.order_by('-id')
        paginator = Paginator(blogs, BLOGS_PER_PAGE)
        ordering = 'id'
    page = paginator.get_page(page_number)
    context = {
        'blogs': page, 
        'ordering': ordering, 
        'q': q, 
        'q_user': q_user}
    return render(request, 'blogs/blog_list.html', context)


def blog_update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(request.POST or NONE, instance=blog)
    if request.METHOD == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    return render(request, 'blogs/blog_update.html', {'form': form})


@login_required(login_url='login_page')
def blog_create(request):
    form = BlogForm
    if request.METHOD == 'POST':
        BlogForm(request.POST or NONE, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    return render(request, 'blogs/blog_create.html', {'form': form})
