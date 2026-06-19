from django.shortcuts import render
from bookings.forms import ReservationForm

# Create your views here.
def reservation_view(request):
    reservation_form=ReservationForm(request.POST or None)

    return render(
        request,
        "reserve.html",
        {'form':reservation_form}

    )
