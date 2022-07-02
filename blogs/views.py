from django.shortcuts import get_object_or_404, render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import Blog, Photo
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import BlogForm, PhotoForm
from .filters import BlogFilter

BLOGS_PER_PAGE = 5


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
    context = {'blogs': page, 'ordering': ordering, 'q': q, 'q_user': q_user}
    return render(request, 'blogs/blog_list.html', context)


def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    return render(request, 'blogs/blog_create.html', {'form': form})


def blog_update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(request.POST or None, instance=blog)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    return render(request, 'blogs/blog_update.html', {'form': form})


@login_required(login_url='login_page')
def blog_create(request):
    blog_form = BlogForm
    PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=3)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST or None, files=request.FILES)
        formset = PhotoFormSet(request.POST,
                               request.FILES,
                               queryset=Photo.objects.none())
        if blog_form.is_valid() and formset.is_valid():
            blog_form = BlogForm.save(commit=False)
            form.user = request.user
            form.save()

            for form in formset.cleaned_data:
                if form:
                    photo = Photo(blog=form, photo=form)
            return redirect('blog_list')
    return render(request, 'blogs/blog_create.html', {
        'blog_form': form,
        'formset': formset
    })


@login_required(login_url='login_page')
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blogs/blog_delete.html', {
        'blog': blog,
    })


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/blog_details.html', {'blog': blog})


def blog_list_f(request):
    f = BlogFilter(request.GET, queryset=Blog.objects.all())
    context = {
        'filter': f,
    }
    return render(request, 'blogs/blog_list_f.html', context)


def blog_list_a(request):
    blogs = Blog.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(blogs, BLOGS_PER_PAGE)
    blogs = paginator.get_page(page_num)
    context = {
        'blogs': blogs,
    }
    if page_num == 1 or page_num is None:
        return render(request, 'blogs/blog_list_a.html', context)
    return render(request, 'blogs/_blog_list_ajax.html', context)
        