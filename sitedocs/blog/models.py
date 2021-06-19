from django.db import models


class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length=55, unique=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
