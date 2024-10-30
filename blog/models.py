from django.db import models
from django.utils.text import slugify


# Create your models here.
# 👉---------------------------Dinamik modellar-----------------------------👈

class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    img = models.ImageField(upload_to='News/')
    create_time = models.DateField(auto_now=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    sort_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BreakingNews(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    sort_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Flickr(models.Model):
    img = models.ImageField(upload_to='flickr/')

    def __str__(self):
        return "rasm"



# 👉---------------------------Dinamik modellar uchun ------------------------------👈

# 👉---------------------------forms modellar ------------------------------👈

class Newslatter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Comment(models.Model):
    name = models.CharField(max_length=100)
    emailComment = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

# 👉---------------------------forms modell end ------------------------------👈





