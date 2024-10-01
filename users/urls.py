from django.urls import path
from .views import UserLoginView, UserRegisterView, UserContactView, log_user_out, EditProfile, UserCartView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_user_out, name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),    
    path('contact/', UserContactView.as_view(), name='contact'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('cart/', UserCartView.as_view(), name='cart'),
]