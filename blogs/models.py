from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-id']