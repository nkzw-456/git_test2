from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, default='')
    text = models.TextField(max_length=500, default='')
    author = models.CharField(max_length=30, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_st = models.DateField(auto_now=True)
    images = models.ImageField(blank=True, upload_to='images/')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=500, default='')
    name = models.CharField(max_length=20, default='')
    created_at = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    text = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.name
