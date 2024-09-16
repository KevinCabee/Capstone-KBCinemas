from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views import View

# Create your views here by creating classes. 

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class UserRegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        return render(request, self.template_name)    
    
class UserContactView(View):
    template_name = 'users/contact.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(request):
        return render(request, 'users/contact.html')