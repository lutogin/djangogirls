from django.db import models
from django.utils import timezone
from django.conf import settings


# class Author(models.Model):
#     name = models.CharField(max_length=64)
#     email = models.EmailField(max_length=255)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
