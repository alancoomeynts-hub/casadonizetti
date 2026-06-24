from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    reservation_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    TIME_CHOICES=[]

    for i in range(16, 23, 1):
        for j in range(0, 60, 15):
            TIME_CHOICES.append((f"{i}:{j:02d}", f"{i}:{j:02d}"))

    reservation_time=forms.ChoiceField(choices=TIME_CHOICES,
                                       widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = Reservation
        fields = (

            'party_size',
            'reservation_date',
            'reservation_time',

        )



