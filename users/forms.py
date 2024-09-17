from django.forms import Form
from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserRegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','password']


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['picture', 'phone_number', 'address_number', 'address_street', 'address_city', 'address_state', 'address_zip', 'bio']