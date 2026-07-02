from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from bookings.models import Reservation
from bookings.forms import ReservationForm
from .forms import ContactUsForm
from .models import Restaurant, Profile
from django.contrib import messages
from allauth.account.views import SignupView

def restaurant_homepage(request):
    """Render the restaurant homepage."""
    restaurant=get_object_or_404(Restaurant,pk=1)
    return render(request, 'restaurant/homepage.html', {'restaurant': restaurant})

class CustomSignupView(SignupView):
    """Customize signup success feedback for new users."""
    def form_valid(self, form):
        """Extend the default signup flow with a success message."""
        response=super().form_valid(form)
        messages.success(
            self.request,
            f"Welcome {form.cleaned_data['first_name']}. Your Account created successfully",
        )
        return response

@login_required
def profile_view(request):
    """Render the logged-in user's profile and reservations."""
    user=request.user
    profile=get_object_or_404(Profile,user=user)
    reservations=Reservation.objects.filter(user=user)
    form=ReservationForm()

    return render(
        request,
        'restaurant/profile.html',
        {
            'user': user,
            'profile': profile,
            'reservations': reservations,
            'form': form,
        },
    )

def contact_us(request):
    if request.method == 'POST':
        form=ContactUsForm(data=request.POST)
        if form.is_valid():
            contact_form=form.save(commit=False)
            contact_form.restaurant=Restaurant.objects.get(pk=1)
            contact_form.save()
            if contact_form.request_type == 'inquiry':
                messages.add_message(request,messages.SUCCESS,'Your inquiry has been sent successfully. We will get back to you soon.')
            else:
                messages.add_message(request,messages.SUCCESS,'Your private dining request has been logged. We will get back to you soon to discuss details.')
        return redirect('homepage')
    else:
        form=ContactUsForm()

    return render(
        request,
        "restaurant/contact_us.html",
        {"form":form},
    )
