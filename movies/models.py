from django.db import models
from django.contrib.auth.models import User

# Create your models here.\
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.CharField(max_length=20)
    length = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    


