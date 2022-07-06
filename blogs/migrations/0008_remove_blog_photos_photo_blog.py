# Generated by Django 4.0.5 on 2022-07-06 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_remove_photo_blog_blog_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photos',
        ),
        migrations.AddField(
            model_name='photo',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.blog'),
        ),
    ]