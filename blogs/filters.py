from unicodedata import category
import django_filters
from .models import Blog, CATEGORIES_CHOICES


class BlogFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=CATEGORIES_CHOICES)
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='По заголовку')

    class Meta:
        model = Blog
        fields = []
