from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CheckoutForm
from .models import Movie

# Create your views here.

class UserHomePageView(View):
    template_name = 'movies/home.html'

    def get(self, request):
        return render(request, self.template_name)

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/list.html'
    context_object_name ='movies'

    
class UserTicketView(View):
    template_name = 'movies/tickets.html'

    def get(self, request):
    
        return render(request, self.template_name)
    
class MovieDetailPage(DetailView):
    model = Movie
    template_name = 'movies/detail.html'

class TicketDetailView(View):
    model = Movie
    template_name = 'movies/ticket_detail.html'

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect('checkout_success')
    else:
        form = CheckoutForm()
    
    return render(request, 'movies/checkout.html', {'form': form})

def checkout_success(request):
    return render(request, 'movies/checkout_success.html')