"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blogs.views import blog_list, blog_create, blog_update, blog_delete,blog_details, blog_list_f, blog_list_a

urlpatterns = [
    path('list/', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('update/<int:blog_id>/', blog_update, name='blog_update'),
    path('delete/<int:blog_id>/', blog_delete, name='blog_delete'),
    path('<int:blog_id>/', blog_details, name='blog_details'),
    path('list1/', blog_list_f, name='blog_list_f'),
    path('list2/', blog_list_a, name='blog_list_a'),
]
