import time

from django.db import models


# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# <name attr>__gte = num --> >=
# <name attr>__lte = num --> <=


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    fio = models.CharField(max_length=255)
    blog_name = models.CharField(max_length=255)

    def __str__(self):
        return self.fio


