from .views import UserLoginView, UserRegisterView, UserContactView
from django.urls import path


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),    
    path('contact/', UserContactView.as_view(), name='contact'),
]