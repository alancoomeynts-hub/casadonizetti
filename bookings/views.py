from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from bookings.forms import ReservationForm
from bookings.models import Reservation


# Create your views here.
def reservation_view(request):
    form=ReservationForm(request.POST or None, user=request.user)
    if request.method == 'POST'and form.is_valid():
            reservation= form.save(commit=False)
            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted=datetime.strptime(time,'%H:%M').time()
            reservation.reservation_for=datetime.combine(date,time_converted)


            if request.user.is_authenticated:
                reservation.user=request.user
                reservation.contact_name=request.user.username
            elif form.cleaned_data['create_account']:
                new_user=User.objects.create_user(username=form.cleaned_data['contact_name'],
                                                  email=form.cleaned_data['contact_email'],
                                                  password=form.cleaned_data['password'],
                                                  )
                reservation.user=new_user

            reservation.save()
            return redirect('homepage')

    return render(
        request,
        "reserve.html",
        {'form':form}

    )
