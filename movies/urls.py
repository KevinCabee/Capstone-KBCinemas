from django.urls import path
from .views import MovieListView, UserTicketView, MovieDetailPage, TicketDetailView, checkout, checkout_success

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movies'),
    path('tickets/', UserTicketView.as_view(), name='tickets'), 
    path('details/<int:pk>/', MovieDetailPage.as_view(), name='movie_detail'),  
    path('purchases/', TicketDetailView.as_view(), name='purchases'),
    path('checkout/', checkout, name='checkout'),
    path('checkout/success/', checkout_success, name='checkout_success'),
]
