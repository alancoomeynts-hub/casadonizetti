from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Restaurant


def restaurant_homepage(request):
    restaurant=get_object_or_404(Restaurant,pk=1)
    return render(request, 'restaurant/homepage.html', {'restaurant': restaurant})