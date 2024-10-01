from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse                            
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .forms import UserRegisterForm, ProfileEditForm
from .models import Profile, Cart


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

class UserCartView(CreateView):
    model = Cart
    template_name = 'user/cart.html'
    context_object_name = 'cart'
    fields = ['food', 'quantity', 'price']