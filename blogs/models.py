from django.db import models
from django.contrib.auth.models import User


CATEGORIES_CHOICES = (
    ('T', 'Текстовый блог'),
    ('P', 'Фотоблог'),
    ('A', 'Артблог'),
    ('M', 'Музыкальный блог'),
)
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORIES_CHOICES, default="Haven't choosen")
    created_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='blogs')

    class Meta:
        ordering = ['id']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class Photo(models.Model):
    photo = models.ImageField(upload_to='blogs_photos')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="photos")