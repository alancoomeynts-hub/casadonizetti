from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from bookings.forms import ReservationForm
from bookings.models import Reservation, Table


# Create your views here.
@login_required
def reservation_view(request):
    form=ReservationForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
            reservation= form.save(commit=False)
            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted=datetime.strptime(time,'%H:%M').time()
            reservation.reservation_for=datetime.combine(date,time_converted)

            reserved_tables=Reservation.objects.filter(reservation_for=reservation.reservation_for).values_list('table_id',flat=True)

            available_tables=Table.objects.filter(capacity__gte=reservation.party_size).exclude(id__in=reserved_tables).order_by("capacity").first()

            if available_tables is None:
                form.add_error(None,'Sorry, no tables are available at that time or party size.')

            else:
                reservation.table=available_tables
                reservation.user = request.user
                reservation.contact_name = request.user.username
                reservation.contact_email = request.user.email

                reservation.save()
                return redirect('homepage')

    return render(
        request,
        "reserve.html",
        {'form':form}

    )
