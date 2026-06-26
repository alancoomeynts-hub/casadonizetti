from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from bookings.models import Reservation
from bookings.forms import ReservationForm
from .models import Restaurant, Profile
from django.contrib import messages
from allauth.account.views import SignupView

def restaurant_homepage(request):
    restaurant=get_object_or_404(Restaurant,pk=1)
    return render(request, 'restaurant/homepage.html', {'restaurant': restaurant})

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response=super().form_valid(form)
        messages.success(self.request, f"Welcome {form.cleaned_data['first_name']}. Your Account created successfully")

        return response

@login_required
def profile_view(request):
    user=request.user
    profile=get_object_or_404(Profile,user=user)
    reservations=Reservation.objects.filter(user=user)
    form=ReservationForm()

    return render(request,'restaurant/profile.html',{'user':user,'profile':profile,'reservations':reservations,'form':form})