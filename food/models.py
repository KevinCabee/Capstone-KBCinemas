from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Food(models.Model):
    picture = models.ImageField(upload_to='food/', null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    

