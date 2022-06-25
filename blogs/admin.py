from django.contrib import admin
from .models import Blog, Tag


# Register your models here. 
class BlogAdmin(admin.ModelAdmin):
    list_filter = ('author__username',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)