from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # NOTE: images need pillow to be installed (python3 -m pip install pillow)
    imgage = models.ImageField(upload_to="images/posts/", null=True, blank=True)

    # Create a Relation between 2 tables/models
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    # Options

    