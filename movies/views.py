from django.shortcuts import render
from django.views import View

# Create your views here.

class UserHomePageView(View):
    template_name = 'movies/home.html'

    def get(self, request):
        return render(request, self.template_name)

class UserMovieView(View):
    template_name = 'movies/movies.html'

    def get(self, request):
        return render(request, self.template_name)
    
class UserTicketView(View):
    template_name = 'movies/tickets.html'

    def get(self, request):
        return render(request, self.template_name)