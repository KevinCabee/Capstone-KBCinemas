from django.db import models
from django.contrib.auth.models import User
from food.models import Food
from movies.models import Movie

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


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address_number = models.CharField(max_length=200)
    address_street = models.CharField(max_length=200)
    address_city = models.CharField(max_length=200)
    address_state = models.CharField(max_length=200)
    address_zip = models.CharField(max_length=20)

    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.CASCADE) 
    movie_adult_quantity = models.IntegerField(null=True, blank=True)
    movie_child_quantity = models.IntegerField(null=True, blank=True)
    movie_senior_quantity = models.IntegerField(null=True, blank=True)
    movie_total = models.IntegerField(null=True, blank=True )

    food = models.ForeignKey(Food, blank=True, null=True, on_delete=models.CASCADE)
    food_quantity = models.IntegerField(null=True, blank=True)
    food_total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if (self.movie):
            return f"MOVIE - {self.movie.title}"
        else:
            return f"FOOD - {self.food.title}"