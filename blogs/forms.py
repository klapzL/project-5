from django import forms
from .models import Blog
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    # author = forms.models.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = (
            'title', 'text', 'category', 'author', 'tags'
        )