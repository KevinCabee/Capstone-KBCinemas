from django.urls import path
from .views import UserFoodAndDrinkView

urlpatterns = [
    path('', UserFoodAndDrinkView.as_view(), name = 'food'),
]