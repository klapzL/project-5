from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True, default='user_images/person.svg', upload_to='user_images')
    birth_date = models.DateField(null=False)
    bio = models.TextField(null=True)
    education = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username