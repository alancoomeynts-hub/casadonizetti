from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('contact_name', 'contact_email', 'contact_phone', 'party_size', 'reservation_for',)