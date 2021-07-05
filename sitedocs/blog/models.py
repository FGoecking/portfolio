from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length=55, unique=True)
    thumb = models.ImageField(upload_to='images/projeto/thumb' ,max_length=255, null=True, blank=True)
    carrossel1 = models.ImageField(upload_to='images/projeto/thumb' ,max_length=255, null=True, blank=True)
    carrossel2 = models.ImageField(upload_to='images/projeto/thumb' ,max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    feito = models.TextField( null=True, blank=True)
    necessario = models.TextField( null=True, blank=True)
    aprendi = models.TextField( null=True, blank=True)
    conclusao = models.TextField( null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
