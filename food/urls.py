from django.urls import path
from .views import FoodAndDrinkView

urlpatterns = [
    path('', FoodAndDrinkView.as_view(), name='food'),
]