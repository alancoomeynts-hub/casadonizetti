from django.shortcuts import render, redirect
from datetime import datetime
from bookings.forms import ReservationForm

# Create your views here.
def reservation_view(request):
    reservation_form=ReservationForm(request.POST or None)
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            reservation_form = form.save(commit=False)
            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted=datetime.strptime(time,'%H:%M').time()
            reservation_form.reservation_for=datetime.combine(date,time_converted)
            reservation_form.save()

            return redirect('homepage')

    return render(
        request,
        "reserve.html",
        {'form':reservation_form}

    )
