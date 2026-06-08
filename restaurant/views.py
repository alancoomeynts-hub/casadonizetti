from django.shortcuts import render
from .models import Restaurant


def restaurant_homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', {'restaurant': restaurant})