from django.urls import path
from .views import UserMovieView, UserTicketView

urlpatterns = [
    path('list/', UserMovieView.as_view(), name='movies'),
    path('tickets/', UserTicketView.as_view(), name='tickets'), 
]