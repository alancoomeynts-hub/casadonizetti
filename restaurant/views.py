from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Restaurant

from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings

def restaurant_homepage(request):
    restaurant=get_object_or_404(Restaurant,pk=1)
    return render(request, 'restaurant/homepage.html', {'restaurant': restaurant})

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response=super().form_valid(form)

        messages.success(self.request, f"Welcome {form.cleaned_data['first_name']}. Your Account created successfully")

        return response