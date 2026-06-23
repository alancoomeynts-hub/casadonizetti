from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from bookings.forms import ReservationForm
from bookings.models import Reservation, Table


# Create your views here.
def reservation_view(request):


    form=ReservationForm(request.POST or None, user=request.user)
    if request.method == 'POST'and form.is_valid():
            reservation= form.save(commit=False)
            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted=datetime.strptime(time,'%H:%M').time()
            reservation.reservation_for=datetime.combine(date,time_converted)

            reserved_tables=Reservation.objects.filter(reservation_for=reservation.reservation_for).values_list('table_id',flat=True)

            available_tables=Table.objects.filter(capacity__gte=reservation.party_size).exclude(id__in=reserved_tables).first()

            if available_tables is None:
                form.add_error(None,'Sorry, no tables are available at that time or party size.')

            else:
                reservation.table=available_tables

                if request.user.is_authenticated:
                    reservation.user=request.user

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
