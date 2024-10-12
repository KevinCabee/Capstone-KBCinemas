from typing import Any
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.urls import reverse                            
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.views import View
from .forms import UserRegisterForm, ProfileEditForm
from .models import Profile, Cart
from movies.models import Movie
from food.models import Food
from django.views.generic import ListView, DetailView, DeleteView


# Create your views here by creating classes. 

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    # def get_success_url(self):
    #     # after login, send the user to home page

    #     return reverse('home')

    # def get(self, request):
    #     return render(request, self.template_name)

def log_user_out(request):
    logout(request)
    return redirect('login')
    
class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        user = form.save(commit=False) # read and dont save yet
        # hash the password
        pass_text = form.cleaned_data['password']
        user.set_password(pass_text) # this will hash the text and saved the hash version
        user.save() # now save the user with hashed password

        # Every user should have a profile
        # After creating the user 
        # Auto-create the profile
        Profile.objects.create(user=user)

        return super().form_valid(form)
    
    def get_success_url(self):
        # after register, send the user to login page
        return reverse('login')
    
class UserContactView(View):

    template_name = 'users/contact.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(request):
        return render(request, 'users/contact.html')
    
class EditProfile(UpdateView):
    model = User
    template_name = 'users/profile_edit.html'
    form_class = ProfileEditForm

    def get_object(self):
        # return the profile to be modifed
        return self.request.user
    
    def get_success_url(self):
        return reverse('home')

class UserCartView(ListView):
    model = Cart
    template_name = 'users/cart.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # calculate totals
        total = 0
        for record in context['records']:
            if record.movie:
                total += record.movie_total
            else:
                total += record.food_total

        context['total'] = total
        return context


def add_movies(request):
    movie_id = request.POST.get('movie_id')
    adult_quantity = request.POST.get('adult_quantity')
    child_quantity = request.POST.get('child_quantity')
    senior_quantity = request.POST.get('senior_quantity')
    adult_price = request.POST.get('adult_price')
    child_price = request.POST.get('child_price')
    senior_price = request.POST.get('senior_price')

    # Calculate total ticket price
    total = (int(adult_quantity) *  float(adult_price))  + (int(child_quantity) * float(child_price)) + (int(senior_quantity) * float(senior_price))
 
    # Add movie to the cart
    movie = Movie.objects.get(id=movie_id)
    Cart.objects.create(
        movie=movie, 
        movie_adult_quantity=adult_quantity, 
        movie_child_quantity=child_quantity, 
        movie_senior_quantity=senior_quantity, 
        movie_total=total
    )

    return redirect('food')


def add_food(request):
    food_id = request.POST.get('food_id')
    food_quantity = request.POST.get('food_quantity')
    food_price = request.POST.get('food_price')

    # Calculate total food price
    total = (int(food_quantity) * float(food_price))
 
    # Add movie to the cart
    food = Food.objects.get(id=food_id)
    Cart.objects.create(
        food=food, 
        food_quantity=food_quantity, 
        food_total=total
    )

    return redirect('food')



class DeleteItemView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart')