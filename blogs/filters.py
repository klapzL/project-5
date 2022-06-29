from unicodedata import category
import django_filters
from .models import Blog, CATEGORIES_CHOICES


class BlogFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=CATEGORIES_CHOICES)

    class Meta:
        model = Blog
        fields = {
            'title' : ['icontains'], 
            'text': ['icontains'], 
        }
