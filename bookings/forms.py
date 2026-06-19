from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('contact_name', 'contact_email', 'contact_phone', 'party_size', 'reservation_for',)
        widgets= {
            'reservation_for': forms.DateTimeInput(format='%Y-%m-%dT%H:%M',attrs={
                'type':'datetime-local',
                'step':'900',
                'class':'form-control' }),
        }
