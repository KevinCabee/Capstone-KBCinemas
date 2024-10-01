from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Food

# Create your views here.
class FoodAndDrinkView(ListView):
    model = Food
    template_name = 'food/food_snacks.html'
    context_object_name = 'foods'

