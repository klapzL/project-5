from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    CATEGORIES_CHOICES = (
        ('T', 'Текстовый блог'),
        ('P', 'Фотоблог'),
        ('A', 'Артблог'),
        ('M', 'Музыкальный блог'),
    )
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORIES_CHOICES, default="Haven't choosen")
    created_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


