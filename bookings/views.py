from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from bookings.forms import ReservationForm
from bookings.models import Reservation, Table
from django.utils import timezone


# Create your views here.
@login_required
def reservation_view(request):
    """Create a reservation for the logged-in user if a suitable table is available.

    On success, save the booking and redirect to the homepage with a confirmation message.
    """

    form=ReservationForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
            reservation= form.save(commit=False)
            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted=datetime.strptime(time,'%H:%M').time()
            reservation_datetime=datetime.combine(date,time_converted)
            reservation.reservation_for=timezone.make_aware(reservation_datetime)

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
                messages.add_message(
                    request, messages.SUCCESS, 'Your reservation has been made successfully.'
                )
                return redirect('homepage')

    return render(request,"reserve.html",{'form':form})


@login_required
def cancel_reservation(request,pk):
    """
    Cancel the logged-in user's reservation on POST and redirect to the profile page.
    """

    reservation=get_object_or_404(Reservation,pk=pk,user=request.user)

    if request.method == 'POST':
            reservation.delete()
            messages.add_message(request,messages.SUCCESS,'Your reservation has been cancelled successfully.')
            return redirect('profile')
    return redirect('profile')

@login_required
def edit_reservation(request,pk):
    """
    Update an existing reservation for the logged-in user.

    Reassign a table if one is available for the requested date, time, and party size.
    """

    reservation=get_object_or_404(Reservation,pk=pk,user=request.user)

    if request.method == 'POST':
        form=ReservationForm(request.POST,instance=reservation)
        if form.is_valid():
            reservation=form.save(commit=False)
            reservation.user=request.user

            date=form.cleaned_data['reservation_date']
            time=form.cleaned_data['reservation_time']
            time_converted = datetime.strptime(time, '%H:%M').time()
            reservation_datetime = datetime.combine(date, time_converted)
            reservation.reservation_for = timezone.make_aware(reservation_datetime)

            reserved_tables = Reservation.objects.filter(reservation_for=reservation.reservation_for).exclude(pk=reservation.pk).values_list(
                'table_id', flat=True)

            available_tables = Table.objects.filter(capacity__gte=reservation.party_size).exclude(
                id__in=reserved_tables).order_by("capacity").first()

            if available_tables is None:
                messages.error(request, 'Sorry, no tables are available at that time or party size.')
            else:
                reservation.table = available_tables
                reservation.user = request.user
                reservation.save()
                messages.add_message(request,messages.SUCCESS,'Your reservation has been updated successfully.')
                return redirect('profile')

    return redirect('profile')