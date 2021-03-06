from django import forms
from .models import Blog, Tag, Photo
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    # author = forms.models.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = (
            'title', 'text', 'category', 'author', 'tags'
        )


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = (
            'name',
        )


class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(label='image')
    class Meta:
        model = Photo
        fields = ('photo',)
