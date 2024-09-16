from django.shortcuts import render
from django.views import View

# Create your views here.
class UserFoodAndDrinkView(View):
    template_name = 'food/food_snacks.html'

    def get(self, request):
        return render(request, self.template_name)