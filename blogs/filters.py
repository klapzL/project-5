from cProfile import label
from unicodedata import category
import django_filters
from .models import Blog, Tag,CATEGORIES_CHOICES


class BlogFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=CATEGORIES_CHOICES)
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='По заголовку')
    tags = django_filters.ModelMultipleChoiceFilter(label='Теги', field_name='tags', queryset=Tag.objects.all())

    class Meta:
        model = Blog
        fields = []
